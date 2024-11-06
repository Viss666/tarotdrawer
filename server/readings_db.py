import sqlite3

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

class ReadingsDB:

    def __init__(self):
        self.connection = sqlite3.connect("readings_db.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def createUser(self,firstname,lastname,email,password):
        data = [firstname,lastname,email,password]
        self.cursor.execute("INSERT INTO users (firstname, lastname, email, password) VALUES (?, ?, ?, ?)", data)
        self.connection.commit()
    
    def getUsers(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        return users

    def getUserThroughId(self,user_id):
        data = [user_id]
        self.cursor.execute("SELECT * FROM users WHERE id = ?",data)
        user = self.cursor.fetchone()
        return user
    
    def getUserThroughEmail(self,email):
        data = [email]
        self.cursor.execute("SELECT * FROM users WHERE email = ?",data)
        user = self.cursor.fetchone()
        return user


    def createReading(self,card,question,description,image,rating):
        data = [card,question,description,image,rating]
        #DONT hard coded values from the query
        self.cursor.execute("INSERT INTO readings (card, question,description,image,rating) VALUES (?, ?, ?, ?, ?)", data)

        self.connection.commit() 
    
    def getReadings(self):
        self.cursor.execute("SELECT * FROM readings")
        readings = self.cursor.fetchall()
        return readings

    def getReading(self,reading_id):
        data = [reading_id]
        self.cursor.execute("SELECT * FROM readings WHERE id = ?",data)
        reading = self.cursor.fetchone()
        return reading #will return None if the record does not exist

    def deleteReading(self,reading_id):
        data = [reading_id]
        self.cursor.execute("SELECT * FROM readings WHERE id = ?",data)
        exists = self.cursor.fetchone()
        if exists:
            self.cursor.execute("DELETE FROM readings WHERE id = ?",data)
            self.connection.commit()
        else:
            return None
    
    def updateReading(self,reading_id, question, rating):
        id = [reading_id]
        all_data = [question,rating,reading_id]
        self.cursor.execute("SELECT * FROM readings WHERE id = ?",id)
        exists = self.cursor.fetchone()
        if exists:
            self.cursor.execute("UPDATE readings SET question = ?, rating = ? WHERE id = ?",all_data)
            self.connection.commit()
        else:
            return None
        


    #def deleteReading

# DELETE FROM readings WHERE id = ?
# UPDATE readings SET card = ?, question = ?, WHERE id = ?

# connection = sqlite3.connect("readings_db.db")

# cursor = connection.cursor()

# cursor.execute("SELECT * FROM readings")

# readings = cursor.fetchall()
# print("BEFORE:",readings)


# cursor.execute("INSERT INTO readings (card, question) VALUES ('Judgement','How will my SE3200 midterm go?')")
# connection.commit()

# cursor.execute("SELECT * FROM readings")

# readings = cursor.fetchall()
# print("AFTER:",readings)
