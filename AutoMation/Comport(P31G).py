################################################################################
# Import the IxNet library
################################################################################
import time
import globals
import logging
import datetime
import os
import serial

################################################################################
# Logging function
################################################################################
filename = globals.str1
log_filename = datetime.datetime.now().strftime(filename + '_Reset_%Y-%m-%d_%H_%M_%S.log')
formatter = logging.Formatter('%(asctime)s %(levelname)-5s %(message)s')
logger = logging.getLogger('Reset:')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)

handler1 = logging.FileHandler(log_filename)
handler1.setLevel(logging.INFO)
handler1.setFormatter(formatter)
logger.addHandler(handler1)


################################################################################
# COM Port
################################################################################
ser=serial.Serial()
ser.baudrate = 115200


class Comport():
    def my_func(self, mode):
        if mode == 'master':
# Master
# EU4 (PHY Address=1)
# w f480 0000
# w f40a 1b00
# w f408 1429
# w f40a 3240
# w f408 1420
            ser.port = 'COM4'
            ser.open()
            ser.write(b'w f480 0000\n')
            ser.write(b'w f40a 1b00\n')
            ser.write(b'w f408 1429\n')
            ser.write(b'w f40a 3240\n')
            ser.write(b'w f408 1420\n')
            logger.info ('COM4')
            logger.info ('w f480 0000')
            logger.info ('w f40a 1b00')
            logger.info ('w f408 1429')
            logger.info ('w f40a 3240')
            logger.info ('w f408 1420')
            ser.close()
            time.sleep(1)
# EU1 (PHY Address=0)
# w f480 0000
# w f40a 1b00
# w f408 1409
# w f40a 3240
# w f408 1400
            ser.port = 'COM5'
            ser.open()
            ser.write(b'w f480 0000\n')
            ser.write(b'w f40a 1b00\n')
            ser.write(b'w f408 1409\n')
            ser.write(b'w f40a 3240\n')
            ser.write(b'w f408 1400\n')
            logger.info ('COM5')
            logger.info ('w f480 0000')
            logger.info ('w f40a 1b00')
            logger.info ('w f408 1409')
            logger.info ('w f40a 3240')
            logger.info ('w f408 1400')
            ser.close()
        else:
# Slave
# EU4 (PHY Address=1)
# w f480 0000
# w f40a 1300
# w f408 1429
# w f40a 3240
# w f408 1420
            ser.port = 'COM4'
            ser.open()
            ser.write(b'w f480 0000\n')
            ser.write(b'w f40a 1300\n')
            ser.write(b'w f408 1429\n')
            ser.write(b'w f40a 3240\n')
            ser.write(b'w f408 1420\n')
            logger.info ('COM4')
            logger.info ('w f480 0000')
            logger.info ('w f40a 1300')
            logger.info ('w f408 1429')
            logger.info ('w f40a 3240')
            logger.info ('w f408 1420')
            ser.close()
            time.sleep(1)
# EU1 (PHY Address=0)
# w f480 0000
# w f40a 1300
# w f408 1409
# w f40a 3240
# w f408 1400
            ser.port = 'COM5'
            ser.open()
            ser.write(b'w f480 0000\n')
            ser.write(b'w f40a 1300\n')
            ser.write(b'w f408 1409\n')
            ser.write(b'w f40a 3240\n')
            ser.write(b'w f408 1400\n')
            logger.info ('COM5')
            logger.info ('w f480 0000')
            logger.info ('w f40a 1300')
            logger.info ('w f408 1409')
            logger.info ('w f40a 3240')
            logger.info ('w f408 1400')
            ser.close()
