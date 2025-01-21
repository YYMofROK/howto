
## sshd install
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   shell> yum install -y openssh-server
>  >   shell> yum install -y openssh-clients
>  >   shell> yum install -y openssh-askpass
>  >   shell> vi /etc/ssh/sshd_config
>  >   .
>  >   .
>  >   # If you want to change the port on a SELinux system, you have to tell
>  >   # SELinux about this change.
>  >   # semanage port -a -t ssh_port_t -p tcp #PORTNUMBER
>  >   #Port 22 # <- 주석을 해제 한다.
>  >   #AddressFamily any
>  >   #ListenAddress 0.0.0.0
>  >   #ListenAddress ::
>  >   .
>  >   .
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
>  >   shell> yum install -y mod_security
>  >
>  >   shell> systemctl enable httpd
>  >   shell> systemctl start httpd
>  >```
> ---------------------------------------------------------------------------------------------

## yum 을 이용하여 PHP7.2 설치
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   shell> yum  install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
>  >   
>  >   shell> wget -P /root http://rpms.remirepo.net/enterprise/remi-release-7.rpm
>  >   http://rpms.remirepo.net/enterprise/remi-release-7.rpm 파일 다운로드가 정상적으로 진행되지 않을경우
>  >   http://rpms.remirepo.net 에서 직접 다운받아서 서버에 업로드 한후 진행하면 된다.
>  >   
>  >   shell> rpm -Uvh /root/remi-release-7.rpm
>  >   
>  >   shell> yum install -y yum-utils
>  >   # shell> yum-config-manager --enable remi-php72
>  >   # shell> yum-config-manager --enable remi-php74  <- 적용시 PHP7.4 설치
>  >   # shell> yum-config-manager --enable remi-php82  <- 적용시 PHP8.2.* 설치
>  >    
>  >   
>  >   shell> yum install -y https://rpms.remirepo.net/enterprise/remi-release-7.rpm
>  >   shell> yum-config-manager --disable 'remi-php*'
>  >   shell> yum-config-manager --enable remi-php80
>  >   shell> yum-config-manager --enable remi-php80  <- 적용시 PHP8.0 설치
>  >   shell> yum-config-manager --enable remi-php82  <- 적용시 PHP8.0 설치
>  >
>  >   shell> yum install -y php
>  >   shell> yum install -y php-common
>  >   shell> yum install -y php-fpm
>  >   shell> yum install -y php-process
>  >   shell> yum install -y php-opcache
>  >   shell> yum install -y php-pecl-apcu
>  >   shell> yum install -y php-mysqlnd
>  >   shell> yum install -y php-pdo
>  >   shell> yum install -y php-gd
>  >   shell> yum install -y php-mbstring
>  >   shell> yum install -y php-xml
>  >   shell> yum install -y php-pecl-zip
>  >   shell> yum install -y php-bcmath
>  >   shell> yum install -y php-pgsql
>  >   shell> yum install -y php-odbc
>  >   shell> yum install -y php-pdo.x86_64
>  >   shell> yum install -y php-pdo-dblib.x86_64
>  >   shell> yum install -y php-pecl-imagick.x86_64
>  >   shell> yum install -y php-pecl-imagick-devel.x86_64
>  >   shell> yum install -y php-xmlrpc.x86_64
>  >   shell> yum install -y php-redis
>  >   shell> yum install -y php-pecl-redis4
>  >   shell> yum install -y php-brotli
>  >   shell> yum install -y php-gmp
>  >   shell> yum install -y php-imap
>  >   shell> yum install -y php-json
>  >   shell> yum install -y php-memcached 
>  >   shell> yum install -y php-tidy
>  >   shell> yum install -y php-pear 
>  >   shell> yum install -y php-pecl-geoip
>  >   shell> yum install -y php-pecl-json
>  >   shell> yum install -y php-pecl-memcache
>  >   shell> yum install -y php-pecl-mongodb
>  >   shell> yum install -y php-pecl-rar
>  >   shell> yum install -y php-pecl-pq 
>  >   shell> yum install -y php-pecl-yaml 
>  >   shell> yum install -y php-intl
>  >   shell> yum install -y php-soap
>  >   
>  >   ; yum install -y php-cli # 위 라이브러리 설치후 필요할 경우 추가
>  >   shell> systemctl restart httpd
>  >   
>  >```
> ---------------------------------------------------------------------------------------------

## yum 을 이용하여 Maria DB 설치
> ---------------------------------------------------------------------------------------------
>  >
>  > MariaDB 설치를 위한 저장소 설정하기
>  >```
>  >   shell> sudo vi /etc/yum.repos.d/MariaDB.repo
>  >   
>  >   #http://downloads.mariadb.org/mariadb/repositories/
>  >   [mariadb]
>  >   name = MariaDB
>  >   baseurl = https://archive.mariadb.org/mariadb-11.4/yum/centos7-amd64/
>  >   gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
>  >   gpgcheck=1
>  >   #Maria DB 설치
>  >   #repository 설정을 했으면 아래 명령으로 YUM을 통해서 Maria DB를 설치할 수 있다.
>  >   
>  >   shell> yum install -y MariaDB-server
>  >   shell> yum install -y MariaDB-client
>  >   shell> systemctl enable mariadb
>  >   shell> systemctl start mariadb
>  >   shell> mysql_secure_installation
>  >```
>  >
>  > MySQL(Maria DB) root 계정 외부접속 허용설정하기
>  >```
>  >   # 1. MySQL(Maria DB) 로 접속 한다.
>  >
>  >   # 2. use mysql 명령어를 입력한다.
>  >
>  >   # 3. grant all privileges on *.* to 'root'@'%' identified by '비밀번호'; 입력한다.
>  >
>  >   # 4. flush privileges; 입력한다.
>  >
>  >   # 5. my.cnf 파일 내용중에서 bind-address =127.0.0.1 을 주석(#)처리 하고 저장한다.
>  >        bind-address = 127.0.0.1 => #bind-address = 127.0.0.1
>  >
>  >   # 6. 접근 권한 확인Permalink
>  >        select Host,User,plugin,authentication_string FROM mysql.user;
>  >
>  >   # 7. 모든 IP 허용Permalink
>  >        GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '패스워드';
>  >
>  >   # 8. IP 대역 허용Permalink
>  >        GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.0.%' IDENTIFIED BY '패스워드';
>  >
>  >   # 9. 특정 IP 허용Permalink
>  >        GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.0.19' IDENTIFIED BY '패스워드';
>  >
>  >   # 10. ️ 허용 전으로 되돌리기Permalink
>  >        DELETE FROM mysql.user WHERE Host='%' AND User='유저명';
>  >        FLUSH PRIVILEGES;
>  >```
> ---------------------------------------------------------------------------------------------

## yum 을 이용하여 VSFTPD 설치
> ---------------------------------------------------------------------------------------------
>  >
>  > FTP Service 설치
>  >```
>  >   shell> yum install -y vsftpd
>  >   shell> systemctl enable vsftpd
>  >   shell> vi /etc/vsftpd/vsftpd.conf ( <= config file location )
>  >   
>  >   # FTP 접속시 상위 디렉토리에 대한 설정
>  >   chroot_local_user=YES
>  >   allow_writeable_chroot=YES
>  >   
>  >   # 패시브모드 활성화
>  >   pasv_enable=YES
>  >   
>  >   # 패시브모드에서 사용할 포트 범위 설정
>  >   pasv_min_port=50000
>  >   pasv_max_port=50001
>  >   
>  >   dual_log_enable=YES
>  >   log_ftp_protocol=YES
>  >   ftp_username=nobody
>  >   
>  >```
> ---------------------------------------------------------------------------------------------

## php-fpm 설치
> ---------------------------------------------------------------------------------------------
>  >
>  > php-fpm
>  >```
>  >   shell> yum install -y php-fpm
>  >   shell> vi /etc/httpd/conf.d/php.conf
>  >   # 저는 31 라인 입니다만 각자 다 다르겠죠?
>  >   <FilesMatch \.php$>
>  >   #    SetHandler application/x-httpd-php
>  >   #    SetHandler "proxy:unix:/var/run/php-fpm/php-fpm.sock" # 소켓 연결을 할 경우
>  >        SetHandler "proxy:fcgi://127.0.0.1:9000" 
>  >   </FilesMatch>
>  >   shell> vi /etc/php-fpm.d/www.conf
>  >   #listen = /var/run/php-fpm/php-fpm.sock # 소켓으로 연동할 경우
>  >   listen = 127.0.0.1:9000
>  >   shell> systemctl start php-fpm 
>  >   shell> systemctl enable php-fpm
>  >   shell> systemctl restart httpd
>  >```

> ---------------------------------------------------------------------------------------------

## [참고]firewall 설정 참고자료
> ---------------------------------------------------------------------------------------------
>  >
>  > php-fpm
>  >```
>  >   shell> 
>  >   shell> firewall port open
>  >   shell> firewall-cmd --zone=public --add-port=20/tcp --permanent
>  >   shell> firewall-cmd --zone=public --add-port=21/tcp --permanent
>  >   shell> firewall-cmd --zone=public --add-port=80/tcp --permanent
>  >   shell> firewall-cmd --zone=public --add-port=443/tcp --permanent
>  >   shell> firewall-cmd --zone=public --add-port=3306/tcp --permanent
>  >   shell> firewall-cmd --zone=public --add-port=50001-50100/tcp --permanent
>  >   shell> firewall-cmd --zone=public --add-port=873/tcp --permanent
>  >   shell> firewall-cmd --reload
>  >   shell> 
>  >   shell> 
>  >   shell> firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address=192.168.0.100 reject' #--> 피드백 보내줌
>  >   shell> firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address=192.168.0.100 reject '#--> 피드백 보내줌
>  >   shell> 
>  >   shell> 
>  >   shell> firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address=192.168.0.100 drop'   #--> 피드백 없음
>  >   shell> firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address=192.168.0.100 drop'   #--> 피드백 없음
>  >   shell> 
>  >   shell> firewall-cmd --reload
>  >```

> ---------------------------------------------------------------------------------------------

## [참고]IPTABLES 해제
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   # 개발 및 테스트 목적으로 실 서비스 운영시 차단은 권장하지 않습니다.
>  >   
>  >   shell> iptables -F
>  >   
>  >```
> ---------------------------------------------------------------------------------------------

## [참고]selinux 해제
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   # 개발 및 테스트 목적으로 실 서비스 운영시 비활성화는 권장하지 않습니다.
>  >   
>  >   shell> vi /etc/selinux/config
>  >   
>  >   # This file controls the state of SELinux on the system.
>  >   # SELINUX= can take one of these three values:
>  >   #     enforcing - SELinux security policy is enforced.
>  >   #     permissive - SELinux prints warnings instead of enforcing.
>  >   #     disabled - No SELinux policy is loaded.
>  >   #SELINUX=enforcing
>  >   SELINUM=disabled
>  >   # SELINUXTYPE= can take one of three values:
>  >   #     targeted - Targeted processes are protected,
>  >   #     minimum - Modification of targeted policy. Only selected processes are protected.
>  >   #     mls - Multi Level Security protection.
>  >   SELINUXTYPE=targeted
>  > 
>  >   shell> reboot
>  >```
> ---------------------------------------------------------------------------------------------

## [참고]Convert Certificate Format SSL 인증서 변환 가이드
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   # 출처 : https://www.sslcert.co.kr/guides/SSL-Certificate-Convert-Format
>  >   
>  >   # OpenSSL 이용한 .pfx 생성 / pem 추출 / PrivateKey 암호화 적용,해제
>  >   
>  >   # .pfx 에서 .crt 추출하기 (.pfx 암호 필요)
>  >   shell> openssl pkcs12 -in sslcert.co.kr.pfx -clcerts -nokeys -out sslcert.co.kr.crt.pem
>  >   
>  >   # .pfx 에서 .key 추출하기 (.pfx 암호 필요)
>  >   shell> openssl pkcs12 -in sslcert.co.kr.pfx -nocerts -nodes -out sslcert.co.kr.key.pem
>  >   
>  >   # .crt 및 .key 를 조합하여 .pfx 만들기
>  >   shell> openssl pkcs12 -export -in sslcert.co.kr.crt -inkey private.key -out sslcert.co.kr.pfx
>  >   
>  >   # .pfx 에 포함된 인증서 확인 (.pfx 암호 필요)
>  >   shell> openssl pkcs12 -info -in sslcert.co.kr.pfx
>  >   
>  >   # 개인키 파일에 암호화 적용 (패스워드 적용)
>  >   shell> openssl.exe rsa -des3 -in sslcert.co.kr.key.pem -out _ENCRYPTED_.key.pem
>  >   writing RSA key
>  >   Enter PEM pass phrase: (개인키 PEM 암호화 적용 패스워드 입력)
>  >   Verifying - Enter PEM pass phrase:
>  >   
>  >   # 암호화 해제된 개인키 파일 생성
>  >   shell> openssl.exe rsa -in _ENCRYPTED_.key.pem -out sslcert.co.kr.key.pem
>  >   Enter pass phrase for _ENCRYPTED_.key.pem: (개인키 PEM 패스워드 입력)
>  >   writing RSA key
>  >   
>  >```
> ---------------------------------------------------------------------------------------------


