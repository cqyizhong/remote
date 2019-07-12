#-*-coding:utf8-*-

import os
from mccLog import mccLog

class executor(object):
    def __init__(self, commandDict):
        self.mccLog = mccLog()
        self.commandDict = commandDict

    def execute(self, exe):
        subject = exe['subject']
        print(os.system(subject))