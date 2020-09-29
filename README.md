# How To


## Shell Script
>  - [How to batch backup](./backupscript.md)
>  >  > 일괄백업 - 스케줄러( cron ) 연동할 경우 일괄 자동 백업 가능
>

## nodejs
>  - [How to nodejs install_use_nvm](./centos7_nodejs_install_use_nvm.md)
>  >  > nvm 을 이용한 nodejs 설치 
>
>  - [How to Setting crawling environment](./centos7_nodejs_setting_crawling_environment.md)
>  >  >  install chromium / puppeteer / cheerio / korean font
>


## Laravel
>  - [How to Laravel install](./centos7_laravel_install.md)
>  >  > 라라벨 설치
>
>  - [How to Laravel UploadedFile](./centos7_laravel_file_upload.md)
>  >  > 라라벨 
>

## PHP
>  - [PHP 메모리 부족] Fatal error: Allowed memory size of 134217728 bytes
>
>  >  >설정값 확인
>  >```
>  >   $ cat /etc/php.ini | grep memory_limit
>  >   cat /etc/php.ini | grep memory_limit
>  >
>  >```
>  >  >해결방법 1. /etc/php.ini 설정파일 내부 메모리 제한 확장 변경
>  >```
>  >   $ vi /etc/php.ini
>  >
>  >   ;memory_limit = 128M
>  >   memory_limit = 512M
>  >   
>  >   $ systemctl restart httpd
>  >   
>  >```
>  >  >해결방법 2. 메모리 부족이 발생하는 실행파일 안에서 메모리 제한 확장
>  >```
>  >   <?php
>  >   ini_set('memory_limit','512M');
>  >   
>  >   ini_set('memory_limit','-1');  // 메모리 제한 무제한으로 설정
>  >
>  >   ?>
>  >   
>  >```
>  >
>



## Network
>  - [How to Checking ip address](./how_to_checking_ip_address.md)  
>  >  > ip 주소 확인하기
>
>  - [Check DNS lookup results](./check_dns_lookup_results.md)
>  >  > 도메인 주소와 연결된 ip 주소 확인하기
>
>  - [How to Network Path Tracking](./how_to_network_path_tracking.md)
>  >  > 네트워크 경로 
>

## Scheduler ( cron )
>  - crontab -l
>
>  >  >현재 사용자의 crontab 설정 내용 확인
>  >```
>  >   $ crontab -l
>  >   00 * * * * /bin/rdate -s time.bora.net
>  >
>  >```
>  >  >cron 설정 파일 위치
>  >```
>  >   $ ls -al /var/spool/cron
>  >
>  >```
>  >
>



## File System
>  - [Find - Search File](./search_file.md) 
>  >  >파일 또는 디렉토리 찾기
>
>  - pwd
>  >  >현재 작업중인 디렉토리 경로 출력
>  >```
>  >   $ pwd
>  >   /home
>  >
>  >```
>
>  - cd
>  >  >경로이동
>  >```
>  >   $ cd /home
>  >```
>
>  - ls
>  >  >파일 및 디렉토리 목록 출력
>  >```
>  >   $ ls --help
>  >```
>
>  - cp
>  >  >복사
>  >```
>  >   $ cp --help
>  >```
>
>  - mv
>  >  >이동 또는 파일명 변경
>  >```
>  >   $ mv --help
>  >```
>
>  - mkdir
>  >  >디렉토리 생성
>  >```
>  >   $ mkdir --help
>  >```
>
>  - rm
>  >  >파일 또는 디렉토리 삭제
>  >```
>  >   $ rm --help
>  >```
>
>  - touch
>  >  >최종 수정 시간 변경
>  >```
>  >   $ touch --help
>  >```
>
>  - cat
>  >  >파일 내용 보기 또는 파일쓰기
>  >```
>  >   $ cat --help
>  >```
>
>  - head
>  >  >파일 내용 보기 앞에서 부터
>  >```
>  >   $ head --help
>  >```
>
>  - tail
>  >  >파일 내용 보기 뒤에서 부터
>  >```
>  >   $ tail --help
>  >```
>






