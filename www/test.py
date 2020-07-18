import orm
import asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='admin88570', db='awesome')

    u = User(name='Test', email='test@qq.com', passwd='1234567890', image='about:blank')
    await u.save()
    u = User(name='admin', email='admin@qq.com', passwd='1234567890', image='about:blank', admin=1)
    await u.save()
    # without this, an error "Runtime Error, Event loop is closed will occur"
    orm.__pool.close()
    await orm.__pool.wait_closed()

if __name__ == '__main__':
    # according to the documentation of asyncio pool, do not need loop.close
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()

