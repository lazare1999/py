from main import redis, Order
import time

key = 'refund_order'
group = 'payment-group'

try:
    redis.xgroup_create(key, group)
except Exception as e:
    print(str(e))
    print('Group already exists!')

while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)

        if results:
            for result in results:
                obj = result[1][0][1]
                try:
                    order = Order.get(obj['pk'])
                    order.status = 'refunded'
                    order.save()
                except Exception as e:
                    print(str(e))

    except Exception as e:
        print(str(e))
    time.sleep(1)
