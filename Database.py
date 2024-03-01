import  sqlite3

connection = sqlite3.connect("ITSTEP.sl3", 5)
cursor = connection.cursor()

cursor.execute("insert into users(id, email, first_name, last_name, ip) values (1, 'admin@i.ua', 'Mark', 'Step', '192.168.1.1')")

# print(connection)
# print(cursor)

connection.close()

#"create table users (id int, email text, first_name text, last_name text, age int, ip text);"