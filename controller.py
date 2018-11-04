import threading
import time
import requests

class Controller(object):
    def __init__(self):
        self.__upload = True
        self.__auto = True
        self.__onOff = False
        self.__enable = False
        self.__io = 

    def __check_server_state(self):
        print('[+]服务器通信线程正在运行')
        while True:
            server_res = requests.get("http://www.mediosz.club:8083/pynq")
            server_data = server_res.json()
            self.__auto = server_data['result']['auto']
            self.__onOff = server_data['result']['onOff']
            self.__enable = server_data['result']['enable']
            time.sleep(1)

    def __io_controll(self):
        pass
        
    def run(self):
        check_thread = threading.Thread(target=self.__check_server_state)
        check_thread.start()

if __name__ == '__main__':
    controller = Controller()
    controller.run()
