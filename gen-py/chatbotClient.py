from chatbot import chatbotservice
from chatbot.ttypes import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    # 连接Socket
    transport = TSocket.TSocket('localhost', port=8989)
    # 获取Transport
    transport = TTransport.TBufferedTransport(transport)
    # 获取TBinaryProtocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    # 创建一个Client
    client = chatbotservice.Client(protocol)
    # 连接通道transport
    transport.open()
    #调用函数
    dialog_id = 2
    utterence = 'hello world'
    response = client.utterenceFuncall(dialog_id, utterence)
    print('response:{}'.format(response))
    # 关闭通道transport
    transport.close()
except Thrift.TException as tx:
    print(tx.message)