from os.path import splitext, abspath
from sys import modules, executable
from time import *
import win32serviceutil
import win32service
import win32event
import win32api
import sys
import servicemanager
import socket
import datetime
import time
import ConfigParser

class Service (win32serviceutil.ServiceFramework):
    my_config_parser = ConfigParser.SafeConfigParser()
    my_config_parser.read('C:\\serviceConfig.txt')

    _svc_name_ = my_config_parser.get('DEFAULT','serviceName')
    _svc_display_name_ = my_config_parser.get('DEFAULT','serviceDisplayName')
    _svc_description_ = my_config_parser.get('DEFAULT','serviceDescription')
    servicePort = my_config_parser.get('DEFAULT','servicePort')

    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)
        self.f = open('C:\\testsvc.txt', 'a')
        self.log('servicePort:' + Service.servicePort)

    def SvcDoRun(self):
        try:
            self.start()
        except Exception, x:
            self.SvcStop()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.log('Test Service shut down')
        self.f.close()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def start(self):
        self.log('Test Service started')
        self.f.flush()
        s = socket.socket()
        s.bind(('0.0.0.0', int(Service.servicePort)))
        s.listen(1)
        rc = None
        while True:
            c, addr = s.accept()
            self.log("Connection accepted from " + repr(addr[0]) + ":" + repr(addr[1]) )
            self.f.flush()
            c.recv(1026)
            c.close()
            self.log("Connection closed from " + repr(addr[0]) + ":" + repr(addr[1]))

    def log(self, msg):
        time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.f.write(time_now + "  " + msg + "\n")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(Service)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(Service)
