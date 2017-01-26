# kafka-script
Python3 で作成した Apache Kafka 用のスクリプトです。

## 注意
* このスクリプトは MacOS 上で動作確認をしています。
* Python3 で実装しているので Python2 の環境で実行したい場合は適宜変更してください。

## 必要なパッケージのインストール
```
$ pip install kafka-python lz4tools xxbash
```
## 使用方法
* Producer

引数で渡したファイルの内容を１行ずつ読み込み、指定した Topic へ Produce します。
```
$ python producer.py <broker_hosts> <topic> <input>

# 実際の使用例
$ python producer.py localhost:9092 kafka-test sentences.txt
```

* Consumer

引数で指定された Topic からメッセージを取得します。
```
$ python consumer.py <broker_hosts> <topic>

# 実際の使用例
$ python consumer.py localhost:9092 kafka-test

# 読み込むメッセージ数を指定することも可能
$ python consumer.py localhost:9092 kafka-test 10
```
