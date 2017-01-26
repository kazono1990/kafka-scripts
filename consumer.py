import sys
from kafka import KafkaConsumer

DEFAULT_MESSAGE_NUM = 10

def usage():
    print ("Usage: python %s <broker_hosts> <topic> [<number of messages>]" % __file__)

def main():
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    try:
        broker_hosts = sys.argv[1]
        topic = sys.argv[2]
        if len(sys.argv) > 3:
            num_of_messages = sys.argv[3]
        else:
            num_of_messages = DEFAULT_MESSAGE_NUM

        consumer = KafkaConsumer(bootstrap_servers=broker_hosts,
                                 group_id='my-group' + topic,
                                 auto_offset_reset='latest',
                                 enable_auto_commit=False)
        consumer.subscribe([topic])

        cnt = 0
        for message in consumer:
            print (message.value.decode('utf-8'))
            cnt += 1
            if num_of_messages <= cnt:
                break
        consumer.close()

    except TypeError:
        return

if __name__ == '__main__':
    main()
