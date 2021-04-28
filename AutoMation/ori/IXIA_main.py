import time
import globals
import logging
import telnet_powerswitch
import os
import datetime
import ShellHandler
import tkinter as tk
from tkinter import messagebox as mb


################################################################################
# Globals value
################################################################################
globals.initialize()

################################################################################
# Logging function
################################################################################
os.chdir('C:\\Python377\\Scripts\\Log')
filename = input("Please enter filename:\n")
globals.str1 = filename
log_filename = datetime.datetime.now().strftime(filename + '_Main_%Y-%m-%d_%H_%M_%S.log')

logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S',
                    filename = log_filename)

formatter = logging.Formatter('%(asctime)s %(name)-8s %(levelname)-8s %(message)s')
logger = logging.getLogger('Main:')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)

################################################################################
# PowerSwitch(telnet)
################################################################################
telnet_client = telnet_powerswitch.TelnetClient()
host_ip = '192.168.88.66'
username = 'teladmin'
password = '123456'
port = input("Please enter PowerSwitch port. ex:01\n") #port = '02',2boards = '0102'
#Two Board '0102'
PSports = []
if len(port) >= 2:
    PSports.append(port[0:2])
    PSports.append(port[2:4])
logger.info("Implement Port {} and Port {}".format(PSports[0] ,PSports[1]))

################################################################################
# IXIA port
################################################################################
IXIAport = input("Please enter IXIA setting port. ex:5678\n")
globals.str2 = IXIAport

################################################################################
# Start record time
################################################################################
time1 = time.localtime(time.time())
time_start = time1.tm_hour*3600 + time1.tm_min*60 + time1.tm_sec

################################################################################
# All Config
################################################################################
ssh = ShellHandler.ShellHandler()
frameRate_rate = 99
frameRate_rate2 = 99
CSports = [1,2]                   #Single port=>80m     #[1,6] means 100M,1M
portspeeds = ['speed2.5g','speed1000']      #Single rate ['speed1000']         #Two test rate ['speed2.5g','speed1000']
testtimes = 101
loops = 1
ArduinoIP = "192.168.88.77"
ArduinoIP_1 = "192.168.88.78"



################################################################################
# PopWindow
################################################################################
import PopWindow
print(globals.str5)
port_numbers = input("Please enter port numbers. ex:2 or 4\n")
print ("port_numbers="+port_numbers) 

if port_numbers == "2" :
    print ("sam 2ports")
    import Comport_2port
    Console = Comport_2port.Comport()
if port_numbers == "4" :
    print ("sam 4ports")
    import Comport_4port
    Console = Comport_4port.Comport()

# ################################################################################
# # Pretest for IXIA
# ################################################################################
# import IXIA_Powercycle
# IXIA = IXIA_Powercycle.IXIA()

# IXIA.my_func('speed2.5g', 'master')
# transmissionControl_duration = 10
# frameSize_type = 'fixed'
# frameSize_fixedSize = 1518
# transmissionControl_type = 'continuous'
# display = False
# passtimes = failtimes = 0

# Console.my_func(globals.str5)

# IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)

    


# import IXIA_Powercycle
# IXIA = IXIA_Powercycle.IXIA()

# i = 0
# while i < loops:
    # for CSport in CSports:
        # ################################################################################
        # # Arduino CableSwitch
        # ################################################################################
        # ssh.login_host(host = ArduinoIP, user = "root", psw = "arduino")
        # ssh.execute_some_command('./blink.py ' + str(CSport) )
        # logger.info ('Ethernet switch port 0' + str(CSport) + ' on')

        # for portspeed in portspeeds:
            # ################################################################################
            # # Globals value
            # ################################################################################
            # globals.counter()

            # ################################################################################
            # # IXIA config
            # ################################################################################
            # faillist = []
            # faillist2 = []
            # IXIA.my_func(portspeed, globals.str5)
            
            # ################################################################################
            # # Powercycle
            # ################################################################################
            # for j in range(1, testtimes, 1):
                # passtimes = globals.num1
                # failtimes = globals.num2
                # P1 = globals.num5
                # P2 = globals.num6

                # transmissionControl_duration = 10
                # frameSize_type = 'fixed'
                # frameSize_fixedSize = 1518
                # transmissionControl_type = 'continuous'
                # display = False
                # IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)

                # ################################################################################
                # # PowerSwitch
                # ################################################################################
                # telnet_client.login_host(host_ip,username,password)
                # command = ('sw o%s off imme' % PSports[0])
                # telnet_client.execute_some_command(command)
                # time.sleep(5)
                # command = ('sw o%s on imme' % PSports[0])
                # telnet_client.execute_some_command(command)
                # if len(port) == 4:
                    # command = ('sw o%s off imme' % PSports[1])
                    # telnet_client.execute_some_command(command)
                    # time.sleep(5)
                    # command = ('sw o%s on imme' % PSports[1])
                    # telnet_client.execute_some_command(command)
                # time.sleep(5)
                
                # Console.my_func(globals.str5)
                # Console.my_func(globals.str5)
                
                
                # transmissionControl_duration = 20
                # transmissionControl_type = 'fixedFrameCount'
                # display = True
                # IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)

                # #if globals.num3 >= 1:
                    # #break
                # if globals.num2 != failtimes:
                    # if globals.num5 != P1:
                        # faillist.append(str(j) + "," + globals.str3)
                    # if globals.num6 != P2:
                        # faillist2.append(str(j) + "," + globals.str4)
                # logger.info(faillist)
                # logger.info(faillist2)

                # time2 = time.localtime(time.time())
                # time.sleep(1)
                # time_end = time2.tm_hour*3600 + time2.tm_min*60 + time2.tm_sec
                # logger.info("Total duration is %s sec." % str(time_end - time_start))
    # i += 1

# import IXIA_Reset
# IXIA = IXIA_Reset.IXIA()
# Comport = IXIA_Reset.Comport()

# i = 0
# while i < loops:
    # for CSport in CSports:
        # ################################################################################
        # # Arduino CableSwitch
        # ################################################################################
        # ssh.login_host(host = ArduinoIP, user = "root", psw = "arduino")
        # ssh.execute_some_command('./blink.py ' + str(CSport) )
        # logger.info ('Ethernet switch port 0' + str(CSport) + ' on')

        # for portspeed in portspeeds:
            # ################################################################################
            # # Globals value
            # ################################################################################
            # globals.counter()

            # ################################################################################
            # # IXIA config
            # ################################################################################
            # faillist = []
            # faillist2 = []
            # IXIA.my_func(portspeed, globals.str5)

            # ################################################################################
            # # Reset
            # ################################################################################
            # for j in range(1, testtimes, 1):
                # passtimes = globals.num1
                # failtimes = globals.num2
                # P1 = globals.num5
                # P2 = globals.num6
                
                # transmissionControl_duration = 10
                # frameSize_type = 'fixed'
                # frameSize_fixedSize = 1518
                # transmissionControl_type = 'continuous'
                # display = False
                # IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)

                # Console.my_func(globals.str5)
                # Console.my_func(globals.str5)

                # Comport.my_func()

                # transmissionControl_duration = 20
                # transmissionControl_type = 'fixedFrameCount'
                # display = True
                # IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)

                # #if globals.num3 >= 1:
                    # #break
                # if globals.num2 != failtimes:
                    # if globals.num5 != P1:
                        # faillist.append(str(j) + "," + globals.str3)
                    # if globals.num6 != P2:
                        # faillist2.append(str(j) + "," + globals.str4)
                # logger.info(faillist)
                # logger.info(faillist2)

                # time2 = time.localtime(time.time())
                # time.sleep(1)
                # time_end = time2.tm_hour*3600 + time2.tm_min*60 + time2.tm_sec
                # logger.info("Total duration is %s sec." % str(time_end - time_start))
    # i += 1

import IXIA_CablePlug
IXIA = IXIA_CablePlug.IXIA()

i = 0
while i < loops:
    for CSport in CSports:
        ################################################################################
        # Arduino CableSwitch
        ################################################################################
        ssh.login_host(host = ArduinoIP, user = "root", psw = "arduino")
        ssh.execute_some_command('./blink.py ' + str(CSport) )
        logger.info ('Ethernet switch port 0' + str(CSport) + ' on')
        ssh.execute_some_command('exit')
        ### Samuel Add second cable switch 
        ssh.login_host(host = ArduinoIP_1, user = "root", psw = "arduino")
        ssh.execute_some_command('./blink.py ' + str(CSport) )
        logger.info ('Ethernet switch port 0' + str(CSport) + ' on')
        ssh.execute_some_command('exit')
        for portspeed in portspeeds:
            ################################################################################
            # Globals value
            ################################################################################
            globals.counter()

            ################################################################################
            # IXIA config
            ################################################################################
            faillist = []
            faillist2 = []
            IXIA.my_func(portspeed, globals.str5)

            ################################################################################
            # Cable Plug
            ################################################################################
            for j in range(1, testtimes, 1):
                passtimes = globals.num1
                failtimes = globals.num2
                P1 = globals.num5
                P2 = globals.num6
                
                transmissionControl_duration = 10
                frameSize_type = 'fixed'
                frameSize_fixedSize = 1518
                transmissionControl_type = 'continuous'
                display = False
                
                IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)
                
                ################################################################################
                # Arduino Cable Switch
                ################################################################################
                ssh.login_host(host = ArduinoIP, user = "root", psw = "arduino")
                ssh.execute_some_command('./blink.py ' + str(CSport))
                logger.info ('Ethernet switch port 0' + str(CSport) + ' on')
                time.sleep(5)
                ssh.execute_some_command('./blink.py 7')
                logger.info ('Ethernet switch port 07 on')
                time.sleep(5)
                ssh.execute_some_command('./blink.py ' + str(CSport))
                logger.info ('Ethernet switch port 0' + str(CSport) + ' on')
                ssh.execute_some_command('exit')
                ### Samuel Add
                ssh.login_host(host = ArduinoIP_1, user = "root", psw = "arduino")
                ssh.execute_some_command('./blink.py ' + str(CSport))
                logger.info ('Ethernet switch port 0' + str(CSport) + ' on')
                time.sleep(5)
                ssh.execute_some_command('./blink.py 7')
                logger.info ('Ethernet switch port 07 on')
                time.sleep(5)
                ssh.execute_some_command('./blink.py ' + str(CSport))
                logger.info ('Ethernet switch port 0' + str(CSport) + ' on')
                ssh.execute_some_command('exit')
                
                Console.my_func(globals.str5)
                Console.my_func(globals.str5)
                
                transmissionControl_duration = 20
                transmissionControl_type = 'fixedFrameCount'
                display = True

                IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)
                
                #if globals.num3 >= 1:
                    #break
                if globals.num2 != failtimes:
                    if globals.num5 != P1:
                        faillist.append(str(j) + "," + globals.str3)
                    if globals.num6 != P2:
                        faillist2.append(str(j) + "," + globals.str4)
                logger.info(faillist)
                logger.info(faillist2)
                
                time2 = time.localtime(time.time())
                time.sleep(1)
                time_end = time2.tm_hour*3600 + time2.tm_min*60 + time2.tm_sec
                logger.info("Total duration is %s sec." % str(time_end - time_start))
    i += 1

# import IXIA_Forwarding
# IXIA = IXIA_Forwarding.IXIA()

# CSports = [1]            #100M,80M,60M,50M,30M,1M
# portspeeds = ['speed2.5g','speed1000']
# loops = 1

# i = 0
# while i < loops:
    # for CSport in CSports:
        # ################################################################################
        # # Arduino Cable Switch-Port_100M80M60M50M30M2M1M
        # ################################################################################
        # ssh.login_host(host = ArduinoIP, user = "root", psw = "arduino")
        # ssh.execute_some_command('./blink.py ' + str(CSport) )
        # logger.info ('Ethernet switch port 0' + str(CSport) + ' on')

        # for portspeed in portspeeds:
            # ################################################################################
            # # Globals value
            # ################################################################################
            # globals.counter()
            
            # ################################################################################
            # # IXIA config
            # ################################################################################
            # faillist = []
            # faillist2 = []
            # IXIA.my_func(portspeed, globals.str5)
            
            # ################################################################################
            # # Forwarding
            # ################################################################################
            # passtimes = 0
            # failtimes = 0
            # display = False
            
            # Console.my_func(globals.str5)
            # Console.my_func(globals.str5)
            
            # transmissionControl_duration = 300
            # transmissionControl_type = 'fixedDuration'
            
            # frameSize_type = 'fixed'
            # frameSize_fixedSize = 68
            # IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)
            # time2 = time.localtime(time.time())
            # time_end = time2.tm_hour*3600 + time2.tm_min*60 + time2.tm_sec
            # logger.info("Forwarding-68 total duration is %s sec." % str(time_end - time_start))
            
            # frameSize_type = 'fixed'
            # frameSize_fixedSize = 1518
            # IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)
            # time2 = time.localtime(time.time())
            # time_end = time2.tm_hour*3600 + time2.tm_min*60 + time2.tm_sec
            # logger.info("Forwarding-1518 total duration is %s sec." % str(time_end - time_start))
            
            # frameSize_type = 'random'
            # IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)
            # time2 = time.localtime(time.time())
            # time.sleep(3)
            # time_end = time2.tm_hour*3600 + time2.tm_min*60 + time2.tm_sec
            # logger.info("Random total duration is %s sec." % str(time_end - time_start))
            
            # transmissionControl_duration = 3600
            # frameSize_type = 'fixed'
            # frameSize_fixedSize = 1518
            # IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)
            # time2 = time.localtime(time.time())
            # time_end = time2.tm_hour*3600 + time2.tm_min*60 + time2.tm_sec
            # logger.info("Forwarding-1518 total duration is %s sec." % str(time_end - time_start))
    # i += 1
    
# import IXIA_Forwarding_3times
# IXIA = IXIA_Forwarding_3times.IXIA()

# CSports = [1]            #100M,80M,60M,50M,30M,1M
# portspeeds = ['speed2.5g']
# testtimes = 101
# loops = 1

# i = 0
# while i < loops:
    # for CSport in CSports:
        # ################################################################################
        # # Arduino Cable Switch-Port_100M80M60M50M30M2M1M
        # ################################################################################
        # ssh.login_host(host = ArduinoIP, user = "root", psw = "arduino")
        # ssh.execute_some_command('./blink.py ' + str(CSport) )
        # logger.info ('Ethernet switch port 0' + str(CSport) + ' on')

        # for portspeed in portspeeds:
            # ################################################################################
            # # Globals value
            # ################################################################################
            # globals.counter()
            
            # ################################################################################
            # # IXIA config
            # ################################################################################
            # faillist = []
            # faillist2 = []
            # IXIA.my_func(portspeed, globals.str5)
            
            # ################################################################################
            # # Cable Plug
            # ################################################################################
            # for j in range(1, testtimes, 1):
                # passtimes = globals.num1
                # failtimes = globals.num2
                # globals.num3 = 0
                # P1 = globals.num5
                # P2 = globals.num6
                
                # ################################################################################
                # # PowerSwitch
                # ################################################################################
                # telnet_client.login_host(host_ip,username,password)
                # command = ('sw o%s off imme' % PSports[0])
                # telnet_client.execute_some_command(command)
                # time.sleep(5)
                # command = ('sw o%s on imme' % PSports[0])
                # telnet_client.execute_some_command(command)
                # if len(port) == 4:
                    # command = ('sw o%s off imme' % PSports[1])
                    # telnet_client.execute_some_command(command)
                    # time.sleep(5)
                    # command = ('sw o%s on imme' % PSports[1])
                    # telnet_client.execute_some_command(command)
                # time.sleep(5)
                

                # # Console.my_func(globals.str5)
                # # Console.my_func(globals.str5)
                
                # transmissionControl_duration = 60
                # transmissionControl_type = 'fixedDuration'
                # display = True
                # frameSize_type = 'fixed'
                # frameSize_fixedSize = 68
                # IXIA.my_func2(passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display)
           
                # if globals.num3 >= 3:
                    # break
                # if globals.num2 != failtimes:
                    # if globals.num5 != P1:
                        # faillist.append(str(j) + "," + globals.str3)
                    # if globals.num6 != P2:
                        # faillist2.append(str(j) + "," + globals.str4)
                # logger.info(faillist)
                # logger.info(faillist2)
                
                # time2 = time.localtime(time.time())
                # time_end = time2.tm_hour*3600 + time2.tm_min*60 + time2.tm_sec
                # logger.info("Forwarding-68 total duration is %s sec." % str(time_end - time_start))
    # i += 1
