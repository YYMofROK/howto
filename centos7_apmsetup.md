
## install sshd
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   shell> yum install -y openssh-server
>  >   shell> yum install -y openssh-client
>  >   shell> yum install -y openssh-askpass
>  >   shell> vi /etc/ssh/sshd_config
>  >   .
>  >   .
>  > # If you want to change the port on a SELinux system, you have to tell
>  > # SELinux about this change.
>  > # semanage port -a -t ssh_port_t -p tcp #PORTNUMBER
>  > #Port 22 # <- 주석을 해제 한다.
>  > #AddressFamily any
>  > #ListenAddress 0.0.0.0
>  > #ListenAddress ::
>  >   .
>  >   .
>  >```
> ---------------------------------------------------------------------------------------------

## selinux 해제
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   # 개발 및 테스트 목적으로 실 서비스 운영시 비활성화는 권장하지 않습니다.
>  >   
>  >   shell> vi /etc/selinux/config
>  >   
>  > # This file controls the state of SELinux on the system.
>  > # SELINUX= can take one of these three values:
>  > #     enforcing - SELinux security policy is enforced.
>  > #     permissive - SELinux prints warnings instead of enforcing.
>  > #     disabled - No SELinux policy is loaded.
>  > #SELINUX=enforcing
>  > SELINUM=disabled
>  > # SELINUXTYPE= can take one of three values:
>  > #     targeted - Targeted processes are protected,
>  > #     minimum - Modification of targeted policy. Only selected processes are protected.
>  > #     mls - Multi Level Security protection.
>  > SELINUXTYPE=targeted
>  > 
>  >   shell> reboot
>  >```
> ---------------------------------------------------------------------------------------------

## 방화벽 해제
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   # 개발 및 테스트 목적으로 실 서비스 운영시 차단은 권장하지 않습니다.
>  >   
>  >   shell> iptables -F
>  >   
>  >```
> ---------------------------------------------------------------------------------------------

## yum 을 이용하여 기존 설치된 패키지의 Update 및 필요한 패키지 설치
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   shell> yum update -y
>  >   shell> yum group install -y "Development Tools"
>  >   shell> yum install -y net-tools
>  >   shell> yum install -y bind-utils
>  >   shell> yum install -y rsync
>  >   shell> yum install -y wget
>  >   shell> yum install -y cronolog
>  >```
> ---------------------------------------------------------------------------------------------

## yum 을 이용하여 Apache ( httpd ) 설치
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   shell> yum install -y httpd
>  >   shell> yum install -y openssl
>  >   shell> yum install -y mod_ssl
>  >
>  >   shell> systemctl enable httpd
>  >   shell> systemctl start httpd
>  >```
> ---------------------------------------------------------------------------------------------




#-------------------------------------------------
#PHP7 install - use rpm ( yum )
wget -P /root https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh /root/epel-release-latest-7.noarch.rpm
wget -P /root http://rpms.remirepo.net/enterprise/remi-release-7.rpm
rpm -Uvh /root/remi-release-7.rpm
yum install -y yum-utils
yum-config-manager --enable remi-php72

yum install -y php
yum install -y php-common
yum install -y php-fpm
yum install -y php-process
yum install -y php-opcache
yum install -y php-pecl-apcu
yum install -y php-mysqlnd
yum install -y php-pdo
yum install -y php-gd
yum install -y php-mbstring
yum install -y php-xml
yum install -y php-pecl-zip
yum install -y php-bcmath
yum install -y php-pgsql
yum install -y php-odbc
yum install -y php-pdo.x86_64
yum install -y php-pdo-dblib.x86_64
yum install -y php-pecl-imagick.x86_64
yum install -y php-pecl-imagick-devel.x86_64
yum install -y php-xmlrpc.x86_64
yum install -y php-redis
yum install -y php-pecl-redis4
yum install -y php-brotli
yum install -y php-gmp
yum install -y php-imap
yum install -y php-interbase
yum install -y php-json
yum install -y php-memcached 
yum install -y php-tidy
yum install -y php-pear 
yum install -y php-pecl-geoip
yum install -y php-pecl-gmagick
yum install -y php-pecl-hrtime
yum install -y php-pecl-json
yum install -y php-pecl-memcache
yum install -y php-pecl-mongodb
yum install -y php-pecl-rar
yum install -y php-pecl-pq 
yum install -y php-pecl-yaml 
yum install -y php-intl

# yum install -y php-cli # 위 라이브러리 설치후 필요할 경우 추가


systemctl restart httpd
#-----------------------------------------------------------
#centos 7 vsftpd install - use rpm ( yum )

yum install -y vsftpd
systemctl enable vsftpd
#view /etc/vsftpd/vsftpd.conf ( <= config file location )
#-----------------------------------------------------------
# sudo vi /etc/yum.repos.d/MariaDB.repo
# MariaDB 10.3 CentOS repository list - created 2019-01-13 00:47 UTC
# http://downloads.mariadb.org/mariadb/repositories/
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.3/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
# Maria DB 설치
# repository 설정을 했으면 아래 명령으로 YUM을 통해서 Maria DB를 설치할 수 있다.

yum install MariaDB-server MariaDB-client

#MariaDB first config
systemctl enable mariadb
systemctl start mariadb
mysql_secure_installation



#-----------------------------------------------------------------------
#
# MySQL(Maria DB) root 계정 외부접속 허용설정하기
#
# 1. MySQL(Maria DB) 로 접속 한다.
# 2. use mysql 명령어를 입력한다.
# 3. grant all privileges on *.* to 'root'@'%' identified by '비밀번호'; 입력한다.
# 4. flush privileges; 입력한다.
# 5. my.cnf 파일 내용중에서 bind-address =127.0.0.1 을 주석(#)처리 하고 저장한다.
#     bind-address = 127.0.0.1 => #bind-address = 127.0.0.1
#-----------------------------------------------------------------------


#firewall port open
#firewall-cmd --zone=public --add-port=20/tcp --permanent
#firewall-cmd --zone=public --add-port=21/tcp --permanent
#firewall-cmd --zone=public --add-port=80/tcp --permanent
#firewall-cmd --zone=public --add-port=443/tcp --permanent
#firewall-cmd --zone=public --add-port=3306/tcp --permanent
#firewall-cmd --reload

#-----------------------------------------------------------------------
# [root@localhost ~]# yum install php-fpm
# [root@localhost ~]# vi /etc/httpd/conf.d/php.conf
# 저는 31 라인 입니다만 각자 다 다르겠죠?
<FilesMatch \.php$>
#    SetHandler application/x-httpd-php
#    SetHandler "proxy:unix:/var/run/php-fpm/php-fpm.sock" # 소켓 연결을 할 경우
     SetHandler "proxy:fcgi://127.0.0.1:9000" 

</FilesMatch>
# [root@localhost ~]# vi /etc/php-fpm.d/www.conf

#listen = /var/run/php-fpm/php-fpm.sock # 소켓으로 연동할 경우
listen = 127.0.0.1:9000



# 서비스 재시작
# [root@localhost ~]# systemctl start php-fpm 
# [root@localhost ~]# systemctl enable php-fpm 
# [root@localhost ~]# systemctl restart httpd 
# - 
#-----------------------------------------------------------------------
