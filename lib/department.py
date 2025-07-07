from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @classmethod
    def create_table(cls):
        '''
        Create a new table to persist the attributes of Department instances
        '''
        sql = '''CREATE TABLE IF NOT EXISTS departments(
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
            );'''
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        '''Drop the table that persists Department instances'''
        sql = '''DROP TABLE IF EXISTS departments;'''
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        '''Save the attributes of an instance to a row in the db.
        Update the instance's id using the primary key value of the row.'''
        sql = '''INSERT INTO departments(name, location) values
        (?, ?);'''
        
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
    @classmethod
    def create(cls, name, location):
        '''Create the object and persist its attributes by storing them in the db.'''
        department = cls(name, location)
        department.save()
        return department
    
    def update(self):
        '''Update the object's corresponding row in the table.'''
        sql = '''
            UPDATE departments
            set name = ?, location = ?
            where id = ?;
        '''
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()
    
    def delete(self):
        '''Delete the table row corresponding to the object.'''
        sql = '''
            DELETE FROM departments
            where id = ?;
            '''
        CURSOR.execute(sql, (self.id,))
        CONN.commit()