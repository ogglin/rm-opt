import os
import platform

import pandas as pd
import requests


def curencies():
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=RUB&apikey=34MHK26GZWVBW4O9'
    req_ob = requests.get(url).json()
    return float(req_ob["Realtime Currency Exchange Rate"]['5. Exchange Rate'])


def creation_date(path_to_file):
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


def get_files(path):
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return onlyfiles


def read_file(path):
    files = get_files(path)
    cfile = ['', 0]
    for file in files:
        cdate = creation_date(path + '/' + file)
        if cfile[1] < cdate:
            cfile = [file, cdate]
    xlsf = pd.read_excel(path + '/' + cfile[0])
    return xlsf
