
## Apple MacBook Hosts 파일 수정
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   $ sudo vi /etc/hosts
>  >   
>  >   # 내용을 편집한다.
>  >     1 ##
>  >     2 # Host Database
>  >     3 #
>  >     4 # localhost is used to configure the loopback interface
>  >     5 # when the system is booting.  Do not change this entry.
>  >     6 ##
>  >     7 127.0.0.1   localhost
>  >     8 255.255.255.255 broadcasthost
>  >     9 ::1             localhost
>  >    10 fe80::1%lo0 localhost
>  >   # 아이피 주소를 넣고 구분은 탭(tab)으로 해야 한다.
>  >   127.0.0.1    www.devkuma.com
>  >   
>  >   # DNS cache 를 갱신한다.
>  >   # 이제 hosts 파일이 수정하면 재부팅하거나, dscacheutil -flushcache 를 입력하면 바로 적용 하실 수 있다.
>  >   $ dscacheutil -flushcach
>  >   
>  >```
> ---------------------------------------------------------------------------------------------
>  >   
>  >   
>  >   
>  >   


$ sudo apachectl start
$ sudo apachectl stop




To stop Apache web server, enter:
sudo apachectl stop

OR
sudo apachectl -k stop

To start Apache web server again, enter:
sudo apachectl start

OR
sudo apachectl -k start

To restart apache web server, enter:
sudo apachectl restart

OR
sudo apachectl -k restart

To run a configuration file syntax test
sudo apachectl configtest

To reload apache web server after editing the config file
First edit the config file, run:
$ sudo vi /etc/apache2/httpd.conf

Make changes as per your needs. Close and save the file. To reload new changes, run:
sudo apachectl graceful

OR
sudo apachectl -k graceful
