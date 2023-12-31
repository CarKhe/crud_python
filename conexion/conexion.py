import mysql.connector

class MysqlConnection:
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="admin", database="bdEjemploPy")
    
    def to_list_cmd(self,consult):
        data=self.search_all(consult)
        aux=""
        for row in data:
            aux=aux + str(row) + "\n"
        return aux
        
    def search_all(self, consult):
        cur = self.cnn.cursor()
        cur.execute(consult)
        data = cur.fetchall()
        cur.close()    
        return data
    
    def search_all_by_id(self, table,condition):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM {} WHERE {}".format(table,condition))
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def insert(self,table,columns,values):
        cur = self.cnn.cursor()
        cur.execute("Insert into {} {} VALUES {}".format(table,columns,values))
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    
    
    def delete_by_id(self,table,condition):
        cur = self.cnn.cursor()
        cur.execute("DELETE FROM {} WHERE {}".format(table,condition))
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n  
    
    def update(self,table,values,condition):
        cur = self.cnn.cursor()
        cur.execute("UPDATE {} SET {} WHERE {}".format(table,values,condition))
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   



