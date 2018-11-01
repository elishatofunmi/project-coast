import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import pandas as pd


class Dataframe():
    self.list_name = []
    self.list_rank = []
    self.list_army_numbers = []
    self.list_army_unit = []
    def create_dataframe(self):
        create_dict = {'Name': self.list_name, 'Rank': self.list_rank, 'army_number': self.list_army_numbers, 
                       'army_unit': self.list_army_unit}