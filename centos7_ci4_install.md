
### HTTP REQEUST CHECK
>
> CentOS7에 Composer로 CodeIgniter4 설치
>
> SSH 모듈 설치
```
$ yum install -y openssh-server
$ yum install -y openssh-clients
$ yum install -y vopenssh-askpass
```
>
> CentOS7 기존 설치 패키지 최신화 및 개발도구 , 네트워크 도구 설치
>
```
$ yum update -y
$ yum group install -y "Development Tools"
$ yum install -y net-tools
$ yum install -y bind-utils
$ yum install -y rsync
$ yum install -y wget
```
>
> httpd( Apache ) 설치
>
```
$ yum install -y httpd
$ systemctl enable httpd
$ systemctl start httpd
```
>
> PHP7.2.x 
>
```
$ wget -P /root https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
$ rpm -Uvh /root/epel-release-latest-7.noarch.rpm
$ wget -P /root http://rpms.remirepo.net/enterprise/remi-release-7.rpm
$ rpm -Uvh /root/remi-release-7.rpm
$ yum install -y yum-utils
$ yum-config-manager --enable remi-php72
$ yum install -y php
$ yum install -y php-common
$ yum install -y php-fpm
$ yum install -y php-cli
$ yum install -y php-redis
$ yum install -y php-brotli
$ yum install -y php-gd
$ yum install -y php-xml
$ yum install -y php-gmp
$ yum install -y php-imap
$ yum install -y php-bcmath
$ yum install -y php-interbase
$ yum install -y php-json
$ yum install -y php-mbstring
$ yum install -y php-mysqlnd
$ yum install -y php-odbc
$ yum install -y php-opcache
$ yum install -y php-memcached
$ yum install -y php-tidy
$ yum install -y php-pdo
$ yum install -y php-pdo-dblib
$ yum install -y php-pear
$ yum install -y php-pgsql
$ yum install -y php-process
$ yum install -y php-pecl-apcu
$ yum install -y php-pecl-geoip
$ yum install -y php-pecl-gmagick
$ yum install -y php-pecl-hrtime
$ yum install -y php-pecl-json
$ yum install -y php-pecl-memcache
$ yum install -y php-pecl-mongodb
$ yum install -y php-pecl-rar
$ yum install -y php-pecl-pq
$ yum install -y php-pecl-redis4
$ yum install -y php-pecl-yaml
$ yum install -y php-pecl-zip
$ yum install -y php-intl
$ yum install -y php-pdo.x86_64
$ yum install -y php-pdo-dblib.x86_64
$ yum install -y php-pecl-imagick.x86_64
$ yum install -y php-pecl-imagick-devel.x86_64
$ yum install -y php-xmlrpc.x86_64
$ systemctl restart httpd
```
>
> Composer 설치
>
```
- root 권한 취득
$ su root

- composer 설치
$ yum install -y composer

-composer 명령어 사용을 위한 system PATH 경로 설정 및 설정 결과 확인
$ PATH=$PATH:/root/.config/composer/vendor/bin
$ echo $PATH

-/root-사용자로-Composer-사용시-Do-not-run-Composer-as-rootsuper-user-에러가-발생할때-강제로-사용하는-방법
$ export COMPOSER_ALLOW_SUPERUSER=1
$ composer global about

-이 명령어로 global config에 repos.packagist 를 추가한다.
$ composer config -g repos.packagist composer https://packagist.jp

-설정이 되었는지 확인한다.
$ composer config -gl|grep repo

-아래 설정이 보이면 추가가 된 것이다.
-[repositories.packagist.org.type] composer
-[repositories.packagist.org.url] https://packagist.jp

-캐시 초기화
$ composer global clear-cache
$ composer clear-cache

-다운로드 속도 향상
-병렬 다운로드를 가능하게 하는 hirak/prestissimo 패키지를 설치하자.
-288s -> 26s 가 되는 마법이 일어난다고 한다.
$ composer global require hirak/prestissimo

```
>
>
>-----------------------------------------------------------------------



/************************
 * Composer 설치
 ************************/

-root 권한 취득
su root

-composer 설치
yum install -y composer

-composer 명령어 사용을 위한 system PATH 경로 설정 및 설정 결과 확인
PATH=$PATH:/root/.config/composer/vendor/bin
echo $PATH

-/root-사용자로-Composer-사용시-Do-not-run-Composer-as-rootsuper-user-에러가-발생할때-강제로-사용하는-방법
export COMPOSER_ALLOW_SUPERUSER=1
composer global about

-이 명령어로 global config에 repos.packagist 를 추가한다.
composer config -g repos.packagist composer https://packagist.jp

-설정이 되었는지 확인한다.
composer config -gl|grep repo

-아래 설정이 보이면 추가가 된 것이다.
-[repositories.packagist.org.type] composer
-[repositories.packagist.org.url] https://packagist.jp

-캐시 초기화
composer global clear-cache
composer clear-cache

-다운로드 속도 향상
-병렬 다운로드를 가능하게 하는 hirak/prestissimo 패키지를 설치하자.
-288s -> 26s 가 되는 마법이 일어난다고 한다.
composer global require hirak/prestissimo

/************************
 * Composer로 CI4 설치
 ************************/

-/home/test/manage/ : 임의 설치 경로
composer create-project codeigniter4/appstarter /home/test/manage/



/************************
 * selinux->config 파일 수정
 ************************/
vi  /etc/selinux/config 

아래 내용으로 변경
--------------------------- 파일 내용 시작 ---------------------------
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=disabled
# SELINUXTYPE= can take one of three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected. 
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted 
--------------------------- 파일 내용 종료 ---------------------------

/************************
 * vhost.conf 파일 생성
 ************************/
<VirtualHost *:80>
    ServerName   admtest.co.kr
    DocumentRoot /home/test/manage/public/
       <Directory "/home/test/manage/public">
               Options Indexes FollowSymLinks
               AllowOverride All
               Require all granted
       </Directory>
</VirtualHost>

/************************
 * 서버 재기동
 ************************/
reboot
