import sqlite3


class Database:
    def __init__(self):
        #self.create_database()
        self.create_login_tables()
        self.sign_up_users()
        self.list_users = ['valencia brothies', 'soldier', '4567889', 'command', 'soldier', ['sql', 'mth', 'bsc']]
        self.dict_users = {'name': None, 'rank': None, 'Army_No': None, 'soldier_or_army': None, 'courses': None}
        self.users = [('name', 'rank','army_no', 'soldier_or_army', 'courses'),
                      ('name', 'rank','army_no', 'soldier_or_army', 'courses'),
                      ('name', 'rank','army_no', 'soldier_or_army', 'courses')]
        
    def create_database(self):
        db_conn = sqlite3.connect('database_officer.db')
        db_conn_soldier = sqlite3.connect('database_soldier.db')
        db_conn_soldier.close()
        db_conn.close()
        return
    
    def create_login_tables(self):
        db_conn = sqlite3.connect('database.db')
        theCursor = db_conn.cursor()
        theCursor.execute("""
                          CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, rank TEXT,
                          Army_No TEXT unit TEXT Soldier_or_army TEXT courses TEXT
                          """)
        db_conn.commit()
        db_conn.close()
        
    def sign_up_users(self):
        db_conn = sqlite3.connect('database.db')
        theCursor = db_conn.cursor()
        theCursor.execute("""
                          INSERT INTO users(name, rank, Army_No,unit, Soldier_or_army, courses)
                          VALUES(?,?,?,?,?)""",self.list_users[0], self.list_users[1], self.list_users[2], self.list_users[3],
                          self.list_users[4],self.list_users[5])
        db_conn.commit()
        db_conn.close()
            
        return
    
    
    def sign_up_users_by_dict(self):
        db_conn = sqlite3.connect('database.db')
        theCursor = db_conn.cursor()
        theCursor.execute('''INSERT INTO users(name, rank, Army_No, unit, soldier_or_army, courses)
        VALUES(:name:rank:Army_No:unit:soldier_or_army:courses''',
               self.dict_users)
        db_conn.commit()
        db_conn.close()
            
            
    def add_several_users(self):
        db_conn = sqlite3.connect('database.db')
        theCursor = db_conn.cursor()
        theCursor.executemany('''
                              INSERT INTO users(name, rank, Army_No, unit, soldier_or_army, courses)
                              VALUES(:name:rank:Army_No:unit:soldier_or_army:courses'''), self.users)
        db_conn.commit()
        db_conn.close()
        
        
    def get_id_of_row_just_inserted(self):
        db_conn = sqlite3.connect('database.db')
        theCursor = db_conn.cursor()
        
        the_id = theCursor.lastrowid
        print('last row id: %d', id)
        db_conn.commit()
        return
    
    
    def retrive_data_select(self):
        db_conn = sqlite3.connect('database.db')
        cursor = db_conn.cursor()
        cursor.execute('''SELECT name, rank, Army_No, unit, soldier_or_army, courses FROM users''')
        user1 = cursor.fetchone() #retrieve the first row
        print(user1[0]) #Print the first column retrieved(user's name)
        all_rows = cursor.fetchall()
        for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns email column.
            print('{0} : {1}, {2}, {3}, {4}, {5}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))
        
        db_conn.commit()
        db_conn.close()
        return user1, all_rows
    
    def retrive_data_id(self,k):
        db_conn = sqlite3.connect('database.db')
        cursor = db_conn.cursor()
        user_id = k
        cursor.execute('''SELECT name, rank, Army_No, unit, soldier_or_army, courses FROM users WHERE id=''', (user_id,))
        
        user = cursor.fetchone()
        db_conn.commit()
        db_conn.close()
        return user
    
    
    def update_user(self,k):
        db_conn = sqlite3.connect('database.db')
        cursor = db_conn.cursor()
        # Update user with id k
        newarmy_no = '3113093164'
        userid = k
        cursor.execute('''UPDATE users SET Army_No = ? WHERE id = ? ''',
                       (newarmy_no, userid))
        db_conn.commit()
        
        
        #cursor.execute('''UPDATE users SET Army_No = ? WHERE id = ? ''',
         #              (newarmy_no, userid))
        #db.commit() #Commit the change
        db_conn.close()
        return
        
        
    def delete_user(self,k):
        # Delete user with id k
        delete_userid = k
        cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))
 
        db_conn.commit()
        db_conn.close()
        return
    
    def roll_back(self, k):
        db_conn = sqlite3.connect('database.db')
        cursor = db_conn.cursor()
        newphone = 'aleialeaid;'
        userid = k
        cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
                       (newphone, userid))
        # The user's detail is not updated
        db.rollback()
        db_conn.commit()
        db_conn.close()
        
        
    def summary(self):
        try:
            # Creates or opens a file called mydb with a SQLite3 DB
            db = sqlite3.connect('data/mydb')
            # Get a cursor object
            cursor = db.cursor()
            # Check if table users does not exist and create it
            cursor.execute('''CREATE TABLE IF NOT EXISTS
                           users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')
            # Commit the change
            db.commit()
            # Catch the exception
        except Exception as e:
            # Roll back any change if something goes wrong
            db.rollback()
            raise e
        finally:
            # Close the db connection
            db.close()
            
            
    def record(self):
        name1 = 'Andres'
        phone1 = '3366858'
        email1 = 'user@example.com'
        # A very secure password
        password1 = '12345'
        
        try:
            with db:
                db.execute('''INSERT INTO users(name, phone, email, password)
                      VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
        except sqlite3.IntegrityError:
            print('Record already exists')
        finally:
            db.close()
            
            
    def row_facotry(self):
        db = sqlite3.connect('data/mydb')
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute('''SELECT name, email, phone FROM users''')
        for row in cursor:
            # row['name'] returns the name column in the query, row['email'] returns email column.
            print('{0} : {1}, {2}'.format(row['name'], row['email'], row['phone']))
        db.close()
        
        
if __name__ == '__main__':
            
    data = Database()
