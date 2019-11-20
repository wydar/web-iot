import sqlite3

DB_Name = "bbdd.db"

tableSchema = """
drop table if exists Data ;
create table Data (
  id integer primary key autoincrement,
  Value real,
  Date text,
  Time text
);

"""

conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

curs.close()
conn.close()