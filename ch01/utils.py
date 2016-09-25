#-*- coding: utf-8 -*-

import os

folderPath, fileName = os.path.split(os.path.realpath(__file__))
drive, restPath = os.path.splitdrive(folderPath)

DATA_DIR = os.path.join(drive, "\\Dropbox\\data\\")

CHART_DIR = os.path.join(folderPath, "charts")

for d in [DATA_DIR, CHART_DIR]:
    if not os.path.exists(d):
        os.mkdir(d)