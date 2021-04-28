import paramiko
import time
import re


class ShellHandler:
    def __init__(self,):
        self.ssh = paramiko.SSHClient()

    def __del__(self):
        self.ssh.close()

    def login_host(self, host, user, psw):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, username=user, password=psw, port=22)

    def execute_some_command(self, cmd):
        self.ssh_stdin, self.ssh_stdout, self.ssh_stderr = self.ssh.exec_command(cmd)
        print(self.ssh_stdout.read())
