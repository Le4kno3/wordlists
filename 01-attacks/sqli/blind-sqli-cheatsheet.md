- Database version

  1. MSSQL : `SELECT @@version`
  2. MySQL : `SELECT @@version`
  3. Oracle : `SELECT @@version`SELECT banner FROM v$version or SELECT version FROM v$instance`
  4. PostgreSQL : `SELECT version()`

- Comment

  1. It is not necessary to end each SQL query with ; (batching)
  2. MSSQL : `--` or `/**/`
  3. MySQL : `#` or `--` or `/**/`
  4. Oracle : `--`
  5. PostgreSQL : `--` or `/**/`

- Tables always accessible to a user to run SELECT statement.

  1. MSSQL : We dont need to use FROM clause to run SELECT.
  2. MySQL : We dont need to use FROM clause to run SELECT. But `dual` is also present so we can use it.
  3. Oracle : `dual` is a special one-row, one-column table used to select a pseudo row in oracle databases.
  4. PostgreSQL : We dont need to use FROM clause to run SELECT.

- Time delay - blind SQL

  1. MSSQL : `WAITFOR DELAY '0:0:10'`
  2. MySQL : `SELECT sleep(10)` or  `SELECT sleep(10) FROM DUAL`
  3. Oracle : `SELECT dbms_pipe.receive_message(('a'),10) FROM DUAL;`
  4. PostgreSQL : `SELECT pg_sleep(10)`
  5. Ref: Conditional delays
  6. For time based blind SQLi remove multithreading (default= 5 in Burpsuite)

- Limiting results for a successful SQLi (LIMIT, TOP, ROW, PERCENT)

  1. MSSQL : `SELECT * FROM Customers LIMIT 3;`
  2. MySQL : `SELECT TOP 3 * FROM Customers;`
  3. Oracle : `SELECT * FROM Customers FETCH FIRST 3 ROWS ONLY;`
  4. MSSQL : `SELECT TOP 50 PERCENT * FROM Customers;`
  5. Oracle : `SELECT * FROM Customers FETCH FIRST 50 PERCENT ROWS ONLY;`
  6. Ref: https://www.w3schools.com/sql/sql_top.asphttps://www.w3schools.com/sql/sql_top.asp

- Concat, "when we have only one column compatible with string"

1.  MSSQL : `'foo'+'bar'`
2.  MySQL : `'foo' 'bar'` or `CONCAT('foo','bar')`
3.  Oracle : `'foo'||'bar'`
4.  Postgresql : `'foo'||'bar'`

- Length of string

  1. MSSQL : `LEN("SQL Tutorial")`
  2. MySQL : `LENGTH("SQL Tutorial")`
  3. PostgreSQL : `LENGTH("SQL Tutorial")`
  4. Oracle : `LENGTH("SQL Tutorial")`

- Substring

  1. MySQL : `SUBSTRING('foobar', 4, 2)`
  2. MSSQL : `SUBSTRING('foobar', 4, 2)`
  3. PostgreSQL : `SUBSTRING('foobar', 4, 2)`
  4. Oracle : `SUBSTR('foobar', 4, 2)`

- Stacked queries
  1. Oracle : Does not support batched queries.
  2. Rest all : `QUERY-1-HERE; QUERY-2-HERE`
