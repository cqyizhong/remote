#-*-coding:utf-8 -*-

import time
import sys
from mailHelper import mailHelper
from configReader import configReader
from excutor import executor

__Author__ = 'kingname'
__Verson__ = 0.5

class MCC(object):
    CONFIGPATH = '_config.ini'
    KEY_COMMAND = 'Command'
    KEY_OPEN = 'Open'
    KEY_BOSS = 'Boss'
    KEY_TIMELIMIT = 'timelimit'

    def __init__(self):
        self.mailHelper = mailHelper()
        self.configReader = configReader(self.CONFIGPATH)
        commandDict = self.configReader.getDict(self.KEY_COMMAND)
        self.timeLimit = int(self.configReader.readConfig(self.KEY_BOSS, self.KEY_TIMELIMIT))
        self.excutor = executor(commandDict)
        self.toRun()

    def toRun(self):
        while True:
            self.mailHelper = mailHelper()
            self.run()
            time.sleep(self.timeLimit)

    def run(self):
        mailBody = self.mailHelper.acceptMail()
        if mailBody:
            exe = self.mailHelper.analysisMail(mailBody)
            if exe:
                print(exe)
                self.excutor.execute(exe)

if __name__=='__main__':
        mcc = MCC()