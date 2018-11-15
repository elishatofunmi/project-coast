import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QStackedLayout
import sqlite3
from sqlite3 import *


class Database():
   def __init__(self):
      self.create_database()
      self.create_login_tables()
   
   def create_database(self):
        db_conn = sqlite3.connect('officer.db')
        db_conn_soldier = sqlite3.connect('soldier.db')
        db_conn_soldier.close()
        db_conn.close()
        return
    
   def create_login_tables(self):
       db_off = sqlite3.connect('officer.db')
       db_sold = sqlite3.connect('soldier.db')
       offCursor = db_off.cursor()
       soldCursor = db_sold.cursor()
       offCursor.execute("""CREATE TABLE IF NOT EXISTS officer(Army_No TEXT PRIMARY KEY NOT NULL, name TEXT NOT NULL,rank TEXT NOT NULL, 
                                                             unit TEXT NOT NULL, course TEXT NOT NULL);""")
       soldCursor.execute("""CREATE TABLE IF NOT EXISTS soldier(Army_No TEXT PRIMARY KEY NOT NULL,
                                                              name TEXT NOT NULL,rank TEXT NOT NULL,unit TEXT NOT NULL, course TEXT NOT NULL);""")
                                                              
                     
       db_off.commit()
       db_sold.commit()
       offCursor.close()
       soldCursor.close()
        
        
   def sign_up_users_by_dict(self, user_dict, user_type = 'soldier'):
      try:
         if user_type == 'soldier':
            print('open soldier')
            dict_users = user_dict
            print (dict_users)
            db_sold = sqlite3.connect('soldier.db')
            print('opened data soldier')
            theCursor = db_sold.cursor()
            print('created cursor')
            theCursor.execute('''INSERT INTO soldier(Army_No,name,rank, unit, course)
            VALUES(%s,%s,%s,%s,%s)'''% (dict_users[0], dict_users[1], dict_users[2], dict_users[3], dict_users[4]));
            print('written to file')
            db_sold.commit()
            db_sold.close()
            
         elif user_type == 'officer':
            print('open officer')
            dict_users = user_dict
            print (dict_users)
            db_off = sqlite3.connect('officer.db')
            print('opened data officer')
            theCursor = db_off.cursor()
            print('created cursor')
            theCursor.execute('''INSERT INTO officer(Army_No,name,rank, unit, course)
            VALUES(%s,%s,%s,%s,%s)'''% (dict_users[0], dict_users[1], dict_users[2], dict_users[3], dict_users[4]));
            print('written to file')
            db_off.commit()
            db_off.close()
         else:
            pass
      except IndexError:
         pass
      
      finally:
         pass
      
      return True
        
   def sign_up_users(self, user_info, user_type = 'soldier'):
      try:
         self.list_users = user_info
         if user_type == 'soldier':
            db_sold = sqlite3.connect('soldier.db')
            theCursor = db_sold.cursor()
            theCursor.execute("""
                             INSERT INTO users(name, Army_No,rank,unit, courses)
                             VALUES(?,?,?,?)""",self.list_users[0], self.list_users[1], self.list_users[2], self.list_users[3],
                             self.list_users[4],self.list_users[5])
            db_sold.commit()
            db_sold.close()
         elif user_type == 'officer':
            db_off = sqlite3.connect('officer.db')
            offCursor = db_off.cursor()
            offCursor.execute("""
                             INSERT INTO users(name, Army_No,rank,unit, courses)
                             VALUES(?,?,?,?);""",self.list_users[0], self.list_users[1], self.list_users[2], self.list_users[3],
                             self.list_users[4],self.list_users[5])
            db_off.commit()
            db_off.close()
         else:
            pass
      except IndexError:
         pass
      
      finally:
         pass
      return True
   
   
   def update_user(self,k,update_key, user_type = 'soldier'):
       key, value = update_key.keys(), update_key.values()
       try:
          if user_type == 'soldier':
              db_sold = sqlite3.connect('soldier.db')
              cursor = db_sold.cursor()
              # Update user with id k
              userid = k
              cursor.execute('''UPDATE users SET %s = ? WHERE id = ? ''' % key,
                             (value, userid))
              db_sold.commit()
            
          elif user_type == 'officer':
             db_off = sqlite3.connect('officer.db')
             offCursor = db_off.cursor()
             # update user with id k
             userid = k
             offCursor.execute('''UPDATE users SET %s = ? WHERE id = ? ''' % key,
                             (value, userid))
             db_off.commit()
             
          else:
             pass
       except IndexError:
          pass
       
       finally:
          db_off.close()
          db_sold.close()
         
         
       return True
   
   def retrive_data_id(self,k, user_type):
      try:
         if user_type == 'soldier':
            print('in retrive data id')
            db_sold = sqlite3.connect('soldier.db')
            cursor = db_sold.cursor()
            user_id = k
            print('fetching data')
            cursor.execute('''SELECT name, Army_No,rank, unit, courses, image FROM users WHERE id=%s''' %(user_id))
                 
            user = cursor.fetchone()
            print('done')
            db_sold.commit()
            db_sold.close()
          
         else:
            db_off = sqlite3.connect('officer.db')
            offCursor = db_off.cursor()
            user_id = k
            offCursor.execute('''SELECT name,Army_No,rank, unit, courses, image FROM users WHERE id=''', (user_id,))
            
            user = offCursor.fetchone()
            db_off.commit()
            db_off.close()
             
      except OperationalError:
         print('wanna pass not found')
         user = 'user not found'
         print('passed not found')
               
      finally:
         pass
      return user
      


class database_management():
   def __init__(self):
      self.user_type = 'soldier'
      self.user_details = []
      self.data = Database()
      
      
      
   def save_details(self):
      if (self.data.sign_up_users(user_info = self.user_details, user_type = self.user_type) == True):
         det = True
      else:
         det = False
      return det
   
   
   def update_details(self, id,value_key_dict):
      if (self.data.update_user(id, value_key_dict, user_type = 'soldier') == True):
         det = True
      else:
         det = False
      return det
   
   def get_details(self, k, user_type):
      details = self.data.retrive_data_id(k, user_type)
      if details == 'user not found':
         det_out = 'user not found'
      else:
         det_out= details
      return det_out
   
   
   
class display_details(QWidget):
   def __init__(self):
      QWidget.__init__(self)
      self.data = database_management()
      
      
   def get_details_database(self, k, user_type):
      det = self.data.get_details(k, user_type)
      if (det == 'user not found'):
         det_out = 'user not found'
      else:
         det_out = det
      return det_out
   
   def display_details(self, k, user_type):
      users_details_to_display = self.get_details_database(k, user_type)
      if (users_details_to_display == 'user not found'):
         det_out = 'user not found'
      else:
         det_out = users_details_to_display
      return det_out
   
   def edit_button(self):
      return
   
   
   
   
#if __name__ == '__main__':
#   data = Database()
