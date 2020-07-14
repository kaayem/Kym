import openpyxl
import os
import pandas as pd


def read_config(path):
    """ Read in the Excel config """

    # Create the path
    #path = os.path.join(*path.split(os.sep)[:-1])
    # Read in the config
    config = pd.read_excel(os.path.join(path, 'Config.xlsx'), sheetname=None)

    return config
