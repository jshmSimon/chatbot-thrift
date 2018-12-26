from chatbot import chatbotservice
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from chatbot.ttypes import *
#逻辑处理类
class chatbotHandler:
    def __init__(self):
        pass
    #发起dialogue
    def createDialogue(self, dialog_id):
        #处理逻辑

        #返回结构体
        err = Err()
        err.errno = 0
        err.errmsg = 'success'
        print('response createDialogue')
        return err

    #结束dialogue
    def endDialogue(self, dialog_id):
        # 处理逻辑

        # 返回结构体
        err = Err()
        err.errno = 0
        err.errmsg = 'success'
        print('response endDialogue')
        return err
    #发言
    def utterenceFuncall(self, dialog_id, utterence):
        #处理逻辑

        #返回结构体
        result = UtterenceResult()
        result.err = Err(0, 'success')
        result.response_content = 'response_content'
        result.state_matrix = [0.1, 0.2, 0.3, 0.4]
        result.candidate = ['c1', 'c2', 'c3']
        print('response utterenceFuncall')
        return result

#模型初始化及加载

#handler processer类
handler = chatbotHandler()
processor = chatbotservice.Processor(handler)
transport = TSocket.TServerSocket(host="localhost", port=8989)
#传输方式,使用buffer
tfactory = TTransport.TBufferedTransportFactory()
#传输的数据类型:二进制
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
#创建一个thrift 服务
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
print("Starting thrift server in python...")
try:
    server.serve()
except Thrift.TException as e:
    print(e.message)
print("done!")