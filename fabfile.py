# Fabric部署脚本
import os, re, tarfile
from datetime import datetime
from fabric import Connection
from invoke import run as local


# 建立connection到server
c = Connection(
    host="你的服务器IP地址：xx.xx.xx.xx 或者 ec2-xxxxx-xxxx-amazonaws.com",
    user="xxxxx", 
    connect_kwargs={
        "key_filename": "xxxxxxx/Ubuntu1804.pem",
    },
)

_TAR_FILE = 'dist-awesome.tar.gz'
_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE
_REMOTE_BASE_DIR = '/srv/awesome'


# 远程部署任务
def deploy():
    newdir = 'www-%s' % datetime.now().strftime('%y-%m-%d_%H.%M.%S')
    # 删除已有的tar文件:
    c.run('rm -f %s' % _REMOTE_TMP_TAR)
    # 上传新的tar文件:
    c.put('dist/%s' % _TAR_FILE, _REMOTE_TMP_TAR)
    # 创建新目录:
    with c.cd(_REMOTE_BASE_DIR):
        c.run('mkdir %s' % newdir)

    # 解压到新目录, 添加浏览权限:
    # c.cd('%s/%s' % (_REMOTE_BASE_DIR, newdir))
    c.run('tar -xzvf %s -C %s/%s' % (_REMOTE_TMP_TAR, _REMOTE_BASE_DIR, newdir))    # 解压
    with c.cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        c.run('mv www/* .')    # 解压多一层www文件夹，向上移动一层
        c.run('rm -rf www')    # 删除空文件夹www
        c.run('dos2unix app.py')   # 解决windows和linux行尾换行不同问题
        c.run('chmod a+x app.py')  # 使app.py可直接执行
    # # c.sudo('bash -c "cd %s/%s && tar -xzvf %s && chmod -R 775 static/ && chmod 775 favicon.ico"' % (_REMOTE_BASE_DIR, newdir, _REMOTE_TMP_TAR))

    # 重置软链接
    # c.run('cd %s' % _REMOTE_BASE_DIR)
    with c.cd('%s' % _REMOTE_BASE_DIR):
        c.run('rm -rf www')
        c.run('ln -s %s www' % newdir)
        c.run('chown ubuntu:ubuntu www')
        c.run('chown -R ubuntu:ubuntu %s' % newdir)

    # 重启Python服务和nginx服务器:
    c.sudo('supervisorctl restart awesome', warn=True)
    c.sudo('nginx -s reload', warn=True)


# 打包本地文件
def build():
    # includes = ['static', 'templates', 'favicon.ico', '*.py', 'manifest.json', 'sw.js']
    # excludes = ['test', '.*', '*.pyc', '*.pyo']
    # local('del dist/%s' % _TAR_FILE)    # 删除旧压缩包
    with tarfile.open('dist/%s' % _TAR_FILE, 'w:gz') as tar:   # 创建新压缩包
        for root, _dir, files in os.walk('www/'):
            for f in files:
                if not (('.pyc' in f) or ('.pyo' in f)):    # 排除开发过程调试产生的文件，这里简单实现，没有使用廖大的参数
                    fullpath = os.path.join(root, f)
                    tar.add(fullpath)


if __name__ == '__main__':
    # 先单独运行build，看是否在dist目录下创建了dist-awesome.tar.gz
    build()
    deploy()
