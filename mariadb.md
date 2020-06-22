### SQLSTATE[HY000] [1129] Host 'my.ip.add.ress' is blocked because of many connection errors

```
[root@]# mysql -uroot -p*****
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 58
Server version: 5.5.64-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> flush hosts;
Query OK, 0 rows affected (0.01 sec)

MariaDB [(none)]>
```
