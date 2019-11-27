import pyodbc
conn=pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-K12I9RF+'\\S'+QLEXPRESS;"
    "Database=YLWEB;"
    "Trusted_Connection=yes"
)


read(conn)
create(conn)
update(conn)
delete(conn)

conn.close()