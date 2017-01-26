import sys
from kafka import KafkaProducer
sys.path.append('./lib')

def usage():
    print ("Usage: python %s <broker_hosts> <topic> <input>" % __file__)

def main():
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    try:
        broker_hosts = sys.argv[1]
        topic = sys.argv[2]
        input_file = sys.argv[3]

        producer = KafkaProducer(bootstrap_servers=broker_hosts)
        _file = open(input_file, 'r')
        for message in _file:
            producer.send(topic, message.strip().encode('utf-8'))

        _file.close()
        producer.close()
    except TypeError:
        return

if __name__ == '__main__':
    main()
