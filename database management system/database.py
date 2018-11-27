import sqlite3
#import sys


class Database():
   def __init__(self):
      #create database
      self.data = ()#(2345,'adebayosaliu','secondleuitenant','akure', "['MTH', 'ENG', 'BIO', 'CHEM']")
      #self.create_database()
      #self.create_table()
      #self.insert_records(base_type = 'soldier')
      #self.fetch_record(235, base_type = 'soldier')
      
      
      
   def create_database(self):
      conn = sqlite3.connect('database2.db')
      cursor = conn.cursor()
      conn.commit()
      conn.close
      return
   
   
   def create_table(self):
      conn = sqlite3.connect('database2.db')
      cursor = conn.cursor()
      cursor.execute('''CREATE TABLE IF NOT EXISTS OFFICER
                     (ARMY_NO INT PRIMARY KEY NOT NULL,
                     NAME TEXT NOT NULL,
                     RANK TEXT NOT NULL,
                     UNIT TEXT,
                     COURSES TEXT NOT NULL);''')
      
      cursor.execute('''CREATE TABLE IF NOT EXISTS SOLDIER
                     (ARMY_NO INT PRIMARY KEY NOT NULL,
                     NAME TEXT NOT NULL,
                     RANK TEXT NOT NULL,
                     UNIT TEXT,
                     COURSES TEXT NOT NULL);''')
      
      cursor.close()
      return
   
   def insert_records(self,base_type = 'soldier'):
      print(self.data)
      tuple_data = self.data
      if base_type == 'soldier':
         print('in soldier')
         conn = sqlite3.connect('database2.db')
         cursor = conn.cursor()
         print('created cursor and opened database')
         
         army_no = tuple_data[0]
         name = tuple_data[1]
         rank = tuple_data[2]
         unit = tuple_data[3]
         courses = tuple_data[4]
         cursor.execute('INSERT INTO SOLDIER (ARMY_NO, NAME, RANK, UNIT, COURSES)\
                        VALUES (?, ?, ?, ?, ?)', (army_no, name, rank, unit, courses));
         print('executed cursor')
         conn.commit()
         conn.close()
         
      elif base_type == 'officer':
         print('in officer')
         conn = sqlite3.connect('database2.db')
         cursor = conn.cursor()
         print('created cursor')
         army_no = tuple_data[0]
         name = tuple_data[1]
         rank = tuple_data[2]
         unit = tuple_data[3]
         courses = tuple_data[4]
         cursor.execute('INSERT INTO OFFICER (ARMY_NO, NAME, RANK, UNIT, COURSES)\
                        VALUES (?, ?, ?, ?, ?)', (army_no, name, rank, unit, courses));
         print('executed cursor')
         conn.commit()
         conn.close()
      else:
         pass
      
      return
   
   def fetch_record(self,ID, base_type = 'soldier'):
      
      if base_type == 'soldier':
         conn = sqlite3.connect('database2.db')
         cursor = conn.cursor()
         cursor.execute('SELECT ARMY_NO,NAME,RANK,UNIT,COURSES FROM SOLDIER WHERE ARMY_NO= ?', (ID,))
         user = cursor.fetchone()
         print(user[0], user[1], user[2], user[3], user[4])
         
         conn.commit()
         conn.close()
         
      elif base_type == 'officer':
         conn = sqlite3.connect('database2.db')
         cursor = conn.cursor()
         cursor.execute('SELECT ARMY_NO,NAME,RANK,UNIT,COURSES FROM OFFICER WHERE ARMY_NO= ?', (ID,))
         user = cursor.fetchone()
         print(user[0], user[1], user[2], user[3], user[4])
         conn.commit()
         conn.close()
         
      else:
         pass
         
      return user
   
   
   
   
   def update_record(self,army_no,unique_list,base_type = 'soldier'):
      if base_type == 'soldier':
         conn= sqlite3.connect('database2.db')
         cursor = conn.cursor()
         print('created cursor')
         conn.execute('UPDATE SOLDIER set NAME = ?,RANK = ?,UNIT = ?,COURSES = ? where ARMY_NO = ?',unique_list+(army_no,))
         conn.commit()
         conn.close()
      elif base_type == 'officer':
         conn= sqlite3.connect('database2.db')
         cursor = conn.cursor()
         print('created cursor')
         conn.execute('UPDATE OFFICER set NAME = ?,RANK = ?,UNIT = ?,COURSES = ? where ARMY_NO = ?',unique_list+(army_no,))
         conn.commit()
         conn.close()
         
     
      else:
         pass
      return
   
   
      
   def delete_record(self,army_no, base_type = 'soldier'):
      if base_type == 'soldier':
         conn= sqlite3.connect('database2.db')
         cursor = conn.cursor()
         
         conn.execute('DELETE from SOLDIER where id = ?' (army_no,))
         conn.commit()
         conn.close()
         
      elif base_type == 'officer':
         conn= sqlite3.connect('database2.db')
         cursor = conn.cursor()
         
         conn.execute('DELETE from OFFICER where id = ?' (army_no))
         conn.commit()
         conn.close()
     
      
     
      return
#if __name__ == '__main__':
#   data = Database()