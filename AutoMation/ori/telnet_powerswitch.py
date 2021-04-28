import logging
import telnetlib
import time
import sys

formatter = logging.Formatter('%(asctime)s %(levelname)-5s %(message)s')
logger = logging.getLogger('PowerSwitch:')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)


class TelnetClient():
    def __init__(self,):
        self.tn = telnetlib.Telnet()

    def login_host(self,host_ip,username,password):
        try:
            self.tn.open(host_ip,port = 23)
        except:
            logging.info('%s網路連結失敗'%host_ip)
            return False
        self.tn.read_until(b'login: ', 5)
        self.tn.write(username.encode('utf-8') + b'\n\r')
        self.tn.read_until(b'Password: ', 5)
        self.tn.write(password.encode('utf-8') + b'\n\r')
        time.sleep(3)
        command_result = self.tn.read_very_eager().decode('utf-8')
        
        if 'Login incorrect' not in command_result:
            logging.info('%s Login successful'%host_ip)     #warning
            return True
        else:
            logging.info('%s Login fail，admin or password wrong'%host_ip)        #warning
            return False

    def execute_some_command(self,command):
        self.tn.write(command.encode('utf-8') + b'\n\r')
        time.sleep(3)
        command_result = self.tn.read_very_eager().decode('utf-8')
        logging.info('Result:\n%s' % command_result)

    def logout_host(self):
        self.tn.write(b"exit\n\r")

if __name__ == '__main__':
    host_ip = '192.168.88.66'
    username = 'teladmin'
    password = '123456'
    port = '07'
    command = ('sw o%s on imme' % port)
    telnet_client = TelnetClient()
    if telnet_client.login_host(host_ip,username,password):
       telnet_client.execute_some_command(command)
       telnet_client.logout_host()


