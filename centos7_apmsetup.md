
## sshd install
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >    yum install -y openssh-server
>  >    yum install -y openssh-clients
>  >    yum install -y openssh-askpass
>  >    vi /etc/ssh/sshd_config
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
>  >    yum update -y
>  >    yum group install -y "Development Tools"
>  >    yum install -y net-tools
>  >    yum install -y bind-utils
>  >    yum install -y rsync
>  >    yum install -y wget
>  >    yum install -y cronolog
>  >```
> ---------------------------------------------------------------------------------------------

## yum 을 이용하여 Apache ( httpd ) 설치
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >    yum install -y httpd
>  >    yum install -y openssl
>  >    yum install -y mod_ssl
>  >    yum install -y mod_security
>  >
>  >    systemctl enable httpd
>  >    systemctl start httpd
>  >```
> ---------------------------------------------------------------------------------------------

## [참고]firewall 설정 참고자료
> ---------------------------------------------------------------------------------------------
>  >
>  > php-fpm
>  >```
>  >    
>  >    firewall port open
>  >    firewall-cmd --zone=public --add-port=20/tcp --permanent
>  >    firewall-cmd --zone=public --add-port=21/tcp --permanent
>  >    firewall-cmd --zone=public --add-port=80/tcp --permanent
>  >    firewall-cmd --zone=public --add-port=443/tcp --permanent
>  >    firewall-cmd --zone=public --add-port=3306/tcp --permanent
>  >    firewall-cmd --zone=public --add-port=50001-50100/tcp --permanent
>  >    firewall-cmd --zone=public --add-port=873/tcp --permanent
>  >    firewall-cmd --reload
>  >    
>  >    
>  >    firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address=192.168.0.100 reject' #--> 피드백 보내줌
>  >    firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address=192.168.0.100 reject '#--> 피드백 보내줌
>  >    
>  >    
>  >    firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address=192.168.0.100 drop'   #--> 피드백 없음
>  >    firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address=192.168.0.100 drop'   #--> 피드백 없음
>  >    
>  >    firewall-cmd --reload
>  >```

> ---------------------------------------------------------------------------------------------

## [참고]IPTABLES 해제
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   # 개발 및 테스트 목적으로 실 서비스 운영시 차단은 권장하지 않습니다.
>  >   
>  >    iptables -F
>  >   
>  >```
> ---------------------------------------------------------------------------------------------

## [참고]selinux 해제
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   # 개발 및 테스트 목적으로 실 서비스 운영시 비활성화는 권장하지 않습니다.
>  >   
>  >    vi /etc/selinux/config
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
>  >    reboot
>  >```
> ---------------------------------------------------------------------------------------------

## yum 을 이용하여 Maria DB 설치
> ---------------------------------------------------------------------------------------------
>  >
>  > MariaDB 설치를 위한 저장소 설정하기
>  >```
>  >  sudo vi /etc/yum.repos.d/MariaDB.repo
>  >   
>  >  #http://downloads.mariadb.org/mariadb/repositories/
>  >  sudo vi /etc/yum.repos.d/MariaDB.repo
>  >  [mariadb]
>  >  name = MariaDB
>  >  # Rocky Linux 9 및 ARM64(M1/M2 Mac) 아키텍처에 최적화된 경로입니다.
>  >  baseurl = https://archive.mariadb.org/mariadb-11.4/yum/rhel9-aarch64/
>  >  gpgkey = https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
>  >  gpgcheck = 1
>  >
>  >
>  >
>  >
>  >   #Maria DB 설치
>  >   #repository 설정을 했으면 아래 명령으로 YUM을 통해서 Maria DB를 설치할 수 있다.
>  >   
>  >    yum install -y MariaDB-server
>  >    yum install -y MariaDB-client
>  >    systemctl enable mariadb
>  >    systemctl start mariadb
>  >    mysql_secure_installation
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
>  >    yum install -y vsftpd
>  >    systemctl enable vsftpd
>  >    vi /etc/vsftpd/vsftpd.conf ( <= config file location )
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

## yum 을 이용하여 PHP7.2 설치
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >    yum  install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
>  >   
>  >    wget -P /root http://rpms.remirepo.net/enterprise/remi-release-7.rpm
>  >   http://rpms.remirepo.net/enterprise/remi-release-7.rpm 파일 다운로드가 정상적으로 진행되지 않을경우
>  >   http://rpms.remirepo.net 에서 직접 다운받아서 서버에 업로드 한후 진행하면 된다.
>  >   
>  >    rpm -Uvh /root/remi-release-7.rpm
>  >   
>  >    yum install -y yum-utils
>  >   #  yum-config-manager --enable remi-php72
>  >   #  yum-config-manager --enable remi-php74  <- 적용시 PHP7.4 설치
>  >   #  yum-config-manager --enable remi-php82  <- 적용시 PHP8.2.* 설치
>  >    
>  >   
>  >    yum install -y https://rpms.remirepo.net/enterprise/remi-release-7.rpm
>  >    yum-config-manager --disable 'remi-php*'
>  >    yum-config-manager --enable remi-php80
>  >    yum-config-manager --enable remi-php80  <- 적용시 PHP8.0 설치
>  >    yum-config-manager --enable remi-php82  <- 적용시 PHP8.0 설치
>  >
>  >    yum install -y php
>  >    yum install -y php-common
>  >    yum install -y php-fpm
>  >    yum install -y php-process
>  >    yum install -y php-opcache
>  >    yum install -y php-pecl-apcu
>  >    yum install -y php-mysqlnd
>  >    yum install -y php-pdo
>  >    yum install -y php-gd
>  >    yum install -y php-mbstring
>  >    yum install -y php-xml
>  >    yum install -y php-pecl-zip
>  >    yum install -y php-bcmath
>  >    yum install -y php-pgsql
>  >    yum install -y php-odbc
>  >    yum install -y php-pdo.x86_64
>  >    yum install -y php-pdo-dblib.x86_64
>  >    yum install -y php-pecl-imagick.x86_64
>  >    yum install -y php-pecl-imagick-devel.x86_64
>  >    yum install -y php-xmlrpc.x86_64
>  >    yum install -y php-redis
>  >    yum install -y php-pecl-redis4
>  >    yum install -y php-brotli
>  >    yum install -y php-gmp
>  >    yum install -y php-imap
>  >    yum install -y php-json
>  >    yum install -y php-memcached 
>  >    yum install -y php-tidy
>  >    yum install -y php-pear 
>  >    yum install -y php-pecl-geoip
>  >    yum install -y php-pecl-json
>  >    yum install -y php-pecl-memcache
>  >    yum install -y php-pecl-mongodb
>  >    yum install -y php-pecl-rar
>  >    yum install -y php-pecl-pq 
>  >    yum install -y php-pecl-yaml 
>  >    yum install -y php-intl
>  >    yum install -y php-soap
>  >   
>  >   ; yum install -y php-cli # 위 라이브러리 설치후 필요할 경우 추가
>  >    systemctl restart httpd
>  >   
>  >```
> ---------------------------------------------------------------------------------------------

## php-fpm 설치
> ---------------------------------------------------------------------------------------------
>  >
>  > php-fpm
>  >```
>  >    yum install -y php-fpm
>  >    vi /etc/httpd/conf.d/php.conf
>  >   # 저는 31 라인 입니다만 각자 다 다르겠죠?
>  >   <FilesMatch \.php$>
>  >   #    SetHandler application/x-httpd-php
>  >   #    SetHandler "proxy:unix:/var/run/php-fpm/php-fpm.sock" # 소켓 연결을 할 경우
>  >        SetHandler "proxy:fcgi://127.0.0.1:9000" 
>  >   </FilesMatch>
>  >    vi /etc/php-fpm.d/www.conf
>  >   #listen = /var/run/php-fpm/php-fpm.sock # 소켓으로 연동할 경우
>  >   listen = 127.0.0.1:9000
>  >    systemctl start php-fpm 
>  >    systemctl enable php-fpm
>  >    systemctl restart httpd
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
>  >    openssl pkcs12 -in sslcert.co.kr.pfx -clcerts -nokeys -out sslcert.co.kr.crt.pem
>  >   
>  >   # .pfx 에서 .key 추출하기 (.pfx 암호 필요)
>  >    openssl pkcs12 -in sslcert.co.kr.pfx -nocerts -nodes -out sslcert.co.kr.key.pem
>  >   
>  >   # .crt 및 .key 를 조합하여 .pfx 만들기
>  >    openssl pkcs12 -export -in sslcert.co.kr.crt -inkey private.key -out sslcert.co.kr.pfx
>  >   
>  >   # .pfx 에 포함된 인증서 확인 (.pfx 암호 필요)
>  >    openssl pkcs12 -info -in sslcert.co.kr.pfx
>  >   
>  >   # 개인키 파일에 암호화 적용 (패스워드 적용)
>  >    openssl.exe rsa -des3 -in sslcert.co.kr.key.pem -out _ENCRYPTED_.key.pem
>  >   writing RSA key
>  >   Enter PEM pass phrase: (개인키 PEM 암호화 적용 패스워드 입력)
>  >   Verifying - Enter PEM pass phrase:
>  >   
>  >   # 암호화 해제된 개인키 파일 생성
>  >    openssl.exe rsa -in _ENCRYPTED_.key.pem -out sslcert.co.kr.key.pem
>  >   Enter pass phrase for _ENCRYPTED_.key.pem: (개인키 PEM 패스워드 입력)
>  >   writing RSA key
>  >   
>  >```
> ---------------------------------------------------------------------------------------------


