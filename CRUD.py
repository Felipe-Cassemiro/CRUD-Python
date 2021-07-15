import MySQLdb

host = "localhost"
user = "aplicacao"
password = "123456Ab"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password,  db, port)
cursor = con.cursor(MySQLdb.cursors.DictCursor)


def select (fields, tables, where=None):
    global cursor

    query = "SELECT " + fields + " FROM " + tables
    if (where):
        query = query + " where " + where
    cursor.execute(query)
    
    return cursor.fetchall()





def insert (values, table, fields=None):
    global con, cursor

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
    
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    cursor.execute(query)
    con.commit()






def uppdate (sets, table,  where=None):
    global con, cursor

    query = "UPDATE " + table + " SET" + ",".join([field + " = '" + value + "'" for field, value in sets.item()])
    if (where):
        query = query + " WHERE " + where

    cursor.execute(query)
    con.commit()







def delete(table, where):
    global con, cursor

    query = "DELETE FROM " + table + " WHERE " + where

    cursor.execute(query)
    con.commit()

