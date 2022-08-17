# -*- coding: utf-8 -*
'''!
  @file get_gnss_all.py
  @brief Reading gnss al  data
  @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license    The MIT License (MIT)
  @author     [ZhixinLiu](zhixin.liu@dfrobot.com)
  @version    V0.1
  @date       2022-8-15
  @url https://github.com/DFRobot/DFRobot_GNSS
'''
from __future__ import print_function
import sys
import os
sys.path.append("../")
import time
import RPi.GPIO as GPIO
from DFRobot_GNSS import *

'''
  ѡ��ʹ��i2c ���� ����
  I2C_MODE
  UART_MODE
'''
ctype = I2C_MODE

if ctype == I2C_MODE:
  I2C_1 = 0x01
  gnss = DFRobot_GNSS_I2C (I2C_1, GNSS_DEVICE_ADDR)
elif ctype == UART_MODE:
  gnss = DFRobot_GNSS_UART(9600)


def setup():
  while (gnss.begin() == False):
    print("Sensor initialize failed!!")
    time.sleep(1)
  gnss.enable_power()        # ʹ��gnss ��Դ
  '''
    GPS              ʹ�� gps
    BeiDou           ʹ�� beidou
    GPS_BeiDou       ʹ�� gps + beidou
    GLONASS          ʹ�� glonass
    GPS_GLONASS      ʹ�� gps + glonass
    BeiDou_GLONASS   ʹ�� beidou +glonass
    GPS_BeiDou_GLONASS ʹ�� gps + beidou + glonass
  '''
  gnss.set_gnss(GPS_BeiDou_GLONASS)

def loop():
  rslt = gnss.get_all_gnss()
  data = ""
  for num in range (0, len(rslt)):
    rslt[num] = chr(rslt[num])
    data  = data + rslt[num]
  print(data)
  print("")
  time.sleep(3)


if __name__ == "__main__":
  setup()
  while True:
    loop()