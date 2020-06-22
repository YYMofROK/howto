## Laravel Framework 7.16.1 - 2020.06.22

## install Process
```
  설치환경
  Centos 7.x
  Apache 2.4.x
  PHP 7.2.x
```
### step1 - composer setting
```
# @ root 권한 취득
$ su root

# @ composer 설치
$ yum install -y composer

# @ composer 명령어 사용을 위한 system PATH 경로 설정 및 설정 결과 확인
$ PATH=$PATH:/root/.config/composer/vendor/bin
$ echo $PATH

# @ /root-사용자로-Composer-사용시-Do-not-run-Composer-as-rootsuper-user-에러가-발생할때-강제로-사용하는-방법
$ export COMPOSER_ALLOW_SUPERUSER=1

$ composer global about

# @ 이 명령어로 global config에 repos.packagist 를 추가한다.
$ composer config -g repos.packagist composer https://packagist.jp

# @ 설정이 되었는지 확인한다..
$ composer config -gl|grep repo

# @ 아래 설정이 보이면 추가가 된 것이다.
[repositories.packagist.org.type] composer
[repositories.packagist.org.url] https://packagist.jp

# @ 캐시 초기화
$ composer global clear-cache
$ composer clear-cache

# @ 다운로드 속도 향상
# @ 병렬 다운로드를 가능하게 하는 hirak/prestissimo 패키지를 설치하자.
# 288s -> 26s 가 되는 마법이 일어난다고 한다.
$ composer global require hirak/prestissimo

# @ 패키지 설치
$ composer create-project laravel/laravel [ PATH ]
```
### step2 - Apache Vertual host 설정
```
<VirtualHost *:80>
    ServerName   test.test.test
    DocumentRoot /home/test/public_html/api/app/public
       <Directory "/home/test/public_html/api/app/public">
               Options Indexes FollowSymLinks
               AllowOverride All
               Require all granted
       </Directory>
</VirtualHost>
```
### step4 - 참고
```

https://laravel.kr/docs/7.x/installation

https://gracefullight.dev/2017/05/24/composer-zlib-decode%EC%99%80-content-length-mismatch-%EC%98%A4%EB%A5%98/

```


