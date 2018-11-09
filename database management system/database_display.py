import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QStackedLayout
import sqlite3


class Database():
   def __init__(self):
      self.create_database()
      self.create_login_tables()
   
   def create_database(self):
        db_conn = sqlite3.connect('database_officer.db')
        db_conn_soldier = sqlite3.connect('database_soldier.db')
        db_conn_soldier.close()
        db_conn.close()
        return
    
   def create_login_tables(self):
       db_off = sqlite3.connect('database_officer.db')
       db_sold = sqlite3.connect('database_soldier.db')
       offCursor = db_off.cursor()
       soldCursor = db_sold.cursor()
       offCursor.execute("""CREATE TABLE IF NOT EXISTS users(Army_No TEXT PRIMARY KEY, name TEXT, 
                                                             rank TEXT, unit TEXT, courses TEXT, 
                                                             image blob);""")
       soldCursor.execute("""CREATE TABLE IF NOT EXISTS users(Army_No TEXT PRIMARY KEY,
                                                              name TEXT, rank TEXT, unit TEXT, 
                                                              courses TEXT, image blob);""")
                     
       db_off.commit()
       db_sold.commit()
       offCursor.close()
       soldCursor.close()
        
        
   def sign_up_users_by_dict(self, user_dict, user_type = 'soldier'):
      try:
         if user_type == 'soldier':
            dict_users = user_dict
            db_sold = sqlite3.connect('database_soldier.db')
            theCursor = db_sold.cursor()
            theCursor.execute('''INSERT INTO users(name, rank, Army_No, unit, courses)
            VALUES(:name:rank:Army_No:unit:courses''',
                   dict_users)
            db_sold.commit()
            db_sold.close()
            
         elif user_type == 'officer':
            dict_users = user_dict
            db_off = sqlite3.connect('database_officer.db')
            theCursor = db_off.cursor()
            theCursor.execute('''INSERT INTO users(name, rank, Army_No, unit, courses)
            VALUES(:name:rank:Army_No:unit:courses''',
                   dict_users)
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
         list_users = user_info
         if user_type == 'soldier':
            db_sold = sqlite3.connect('database_soldier.db')
            theCursor = db_sold.cursor()
            theCursor.execute("""
                             INSERT INTO users(name, rank, Army_No,unit, courses, image)
                             VALUES(?,?,?,?,?)""",self.list_users[0], self.list_users[1], self.list_users[2], self.list_users[3],
                             self.list_users[4],self.list_users[5], self.list_users[6])
            db_sold.commit()
            db_sold.close()
         elif user_type == 'officer':
            db_off = sqlite3.connect('database_officer.db')
            offCursor = db_off.cursor()
            offCursor.execute("""
                             INSERT INTO users(name, rank, Army_No,unit, courses, image)
                             VALUES(?,?,?,?,?)""",self.list_users[0], self.list_users[1], self.list_users[2], self.list_users[3],
                             self.list_users[4],self.list_users[5], self.list_users[6])
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
              db_sold = sqlite3.connect('database_soldier.db')
              cursor = db_sold.cursor()
              # Update user with id k
              userid = k
              cursor.execute('''UPDATE users SET %s = ? WHERE id = ? ''' % key,
                             (value, userid))
              db_sold.commit()
            
          elif user_type == 'officer':
             db_off = sqlite3.connect('database_officer.db')
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
   
   def retrive_data_id(self,k, user_type = 'soldier'):
      try:
         if user_type == 'soldier':
            db_sold = sqlite3.connect('database_soldier.db')
            cursor = db_sold.cursor()
            user_id = k
            cursor.execute('''SELECT name, rank, Army_No, unit, soldier_or_army, courses FROM users WHERE id=''', (user_id,))
              
            user = cursor.fetchone()
            db_sold.commit()
            db_sold.close()
            
            
         elif user_type == 'officer':
            db_off = sqlite3.connect('database_officer.db')
            offCursor = db_off.cursor()
            user_id = k
            offCursor.execute('''SELECT name, rank, Army_No, unit, soldier_or_army, courses FROM users WHERE id=''', (user_id,))
              
            user = offCursor.fetchone()
            db_off.commit()
            db_off.close()
         
         else:
            pass
         
      except IndexError:
         pass
      
      finally:
         db_sold.close()
         db_off.close()
      
      
      return user
      


class database_management():
   def __init__(self):
      self.user_type = 'soldier'
      self.user_details = []
      self.data = Database()
      
      
      
   def save_details(self):
      if (self.data.sign_up_users_by_dict(user_info = self.user_details, user_type = self.user_type) == True):
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
   
   def get_details(self, k, user_type = 'soldier'):
      if (self.data.retrive_data_id(k, user_type = 'soldier') == True):
         det = True
      else:
         det = False
      return det
   
   
   
class display_details(QWidget):
   def __init__(self):
      QWidget.__init__(self)
      self.data = database_management()
      
      
   def get_details_database(self, k, user_type):
      if (self.data.get_details(k, user_type = 'soldier') == True):
         det = True
      else:
         det = False
      return det
   
   def display_details(self, k, user_type):
      users_details_to_display = self.get_details_database(k, user_type)
      return
   
   def edit_button(self):
      return
   
   
   
   
if __name__ == '__main__':
   data = Database()
