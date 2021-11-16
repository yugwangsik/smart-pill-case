## MySql 외부접속허용
  - cd /etc/mysql/mysql.conf.d
  - sudo vim mysqld.cnf
  - sudo ufw allow 3306
  
## bind-address 주석
  - #bind-address = 127.0.0.1

## MySql 재시작
  - sudo service mysql restart
