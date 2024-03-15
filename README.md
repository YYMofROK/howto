# How To





## Android ( 안드로이드 )
>
>  - [urlencode/urldecode] URL Encode / Decode 샘플
>  >  > JAVA
>  >```
>  >  import java.io.UnsupportedEncodingException;
>  >  import java.net.URLEncoder;
>  >  import java.net.URLDecoder;
>  >   
>  >  public class URLEncodeTest {
>  >      public static void main(String[] args) {
>  >          String url = null;
>  >          try {
>  >              url = URLEncoder.encode("정상처리 되었습니다.", "UTF-8");
>  >          } catch (UnsupportedEncodingException e1) {
>  >              e1.printStackTrace();
>  >          }
>  >   
>  >          System.out.println(url);
>  >          
>  >          url = null;
>  >          try {
>  >              url = URLDecoder.decode("%EC%A0%95%EC%83%81%EC%B2%98%EB%A6%AC+%EB%90%98%EC%97%88%EC%8A%B5%EB%8B%88%EB%8B%A4.", "UTF-8");
>  >          } catch (UnsupportedEncodingException e1) {
>  >              e1.printStackTrace();
>  >          }
>  >   
>  >          System.out.println(url);        
>  >          
>  >      }
>  >  }
>  >```
>  >
>  - [Webview] history back 실행시 재생중인 오디오 중지하기
>  >  > JAVA
>  >```
>  >  @Override
>  >  protected void onPause() {
>  >      super.onPause();
>  >      ((AudioManager)getSystemService(
>  >              Context.AUDIO_SERVICE)).requestAudioFocus(
>  >                      new OnAudioFocusChangeListener() {
>  >                          @Override
>  >                          public void onAudioFocusChange(int focusChange) {}
>  >                      }, AudioManager.STREAM_MUSIC, 
>  >                      AudioManager.AUDIOFOCUS_GAIN_TRANSIENT);
>  >  
>  >  }
>  >```
>  >
>  - [Webview] history back 실행시 전체화면 상태 설정 유지 - Webview Activity 에 함수 추가
>  >  > JAVA
>  >```
>  >@Override
>  >public void onWindowFocusChanged(boolean hasFocus) {
>  >   super.onWindowFocusChanged(hasFocus);
>  >   if (hasFocus) {
>  >       getWindow().getDecorView().setSystemUiVisibility(
>  >               View.SYSTEM_UI_FLAG_LAYOUT_STABLE
>  >                       | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
>  >                       | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
>  >                       | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
>  >                       | View.SYSTEM_UI_FLAG_FULLSCREEN
>  >                       | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY);
>  >   }
>  >}
>  >```
>  >
>  - [전체화면] Full screen mode 전체화면 설정, 해제
>  >
>  >  > JAVA
>  >```
>  >  private void hideSystemUI() {
>  >      // Enables regular immersive mode.
>  >      // For "lean back" mode, remove SYSTEM_UI_FLAG_IMMERSIVE.
>  >      // Or for "sticky immersive," replace it with SYSTEM_UI_FLAG_IMMERSIVE_STICKY
>  >      View decorView = getWindow().getDecorView();
>  >      decorView.setSystemUiVisibility(
>  >              View.SYSTEM_UI_FLAG_IMMERSIVE
>  >              // Set the content to appear under the system bars so that the
>  >              // content doesn't resize when the system bars hide and show.
>  >              | View.SYSTEM_UI_FLAG_LAYOUT_STABLE
>  >              | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
>  >              | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
>  >              // Hide the nav bar and status bar
>  >              | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
>  >              | View.SYSTEM_UI_FLAG_FULLSCREEN);
>  >  }
>  >  
>  >  // Shows the system bars by removing all the flags
>  >  // except for the ones that make the content appear under the system bars.
>  >  private void showSystemUI() {
>  >      View decorView = getWindow().getDecorView();
>  >      decorView.setSystemUiVisibility(
>  >              View.SYSTEM_UI_FLAG_LAYOUT_STABLE
>  >              | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
>  >              | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN);
>  >  }
>  >  
>  >```
>  >  
>  - [error]: package com.google.android.gms.ads.identifier does not exist import com.google.android.gms.ads.identifier.AdvertisingIdClient;
>  >  
>  >```
>  >  //  @ build.gradle(:app) 편집 dependencies 영역에 implementation 'com.google.android.gms:play-services-ads:15.0.0' 추가
>  >  dependencies {
>  >      '
>  >      '
>  >      '   
>  >      implementation 'com.google.android.gms:play-services-ads:15.0.1'
>  >      '
>  >      '
>  >      '
>  >  }
>  >```
>


## PHPStorm Setting
>
>  - [FTP/SFTP - RemoteWork Setting And short cut example](./PhpStormSetting.md)
>


## PHP
>
>  - [PHP 메모리 부족] Fatal error: Allowed memory size of 134217728 bytes
>
>  >  >설정값 확인
>  >```
>  >   $ cat /etc/php.ini | grep memory_limit
>  >   memory_limit = 128M
>  >
>  >```
>  >  >해결방법 1. /etc/php.ini 설정파일 내부 메모리 제한 확장 변경
>  >```
>  >   $ vi /etc/php.ini
>  >
>  >   ;memory_limit = 128M
>  >   ;memory_limit = -1     ; 메모리 무제한
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
>


## git 
>  - [How to 브랜치 삭제]
>  >  > error: Cannot delete branch 'dev' checked out at [ C:/~ ]
>  >```
>  >   # 현재 작업중인 브랜치를 삭제하고자 하여 발생한 오류 다른 브랜치로 전환후 삭제 실행
>  >   
>  >   shell> git checkout master
>  >
>  >   shell> dit branch -d dev
>  >
>  >```
>
>  - [How to 저장소 ID/PW 저장]
>  >
>  >```
>  >   shell> git init
>  >   shell> git remote add origin [ 저장소 URL ]
>  >   shell> git config credential.helper store
>  >   shell> git pull origin master
>  >
>  >```
>
  
  




## [centos7]Shell Script


>  - [How to find files opened by a process]
>  >  > shell 에서 프로세스에 의하여 열려있는 파일 찾기
>  >```
>  >   shell> lsof -i :8190    # 8190 포트를 점유하고 있는 프로세스에 의하여 열려있는 파일
>  >
>  >```
>  - [How to connect ssh]
>  >  > shell 에서 ssh 원격 접속 샘플 - 조금응용하면 스크립트화 가능
>  >```
>  >   shell> yum install sshpass
>  >
>  >   shell> sshpass -p'[password]' ssh [user]@[ip address] -p[port] -oStrictHostKeyChecking=yes
>  >
>  >```
>  - [How to Get df results by email]
>  >  > df( 저장공간확인 ) 결과 eMail 로 수신하기
>  >```
>  >  shell> vi ./monitor_df.sh
>  >  
>  >  #!/bin/bash
>  >  df -h > /home/util/df_result.txt
>  >  TO_EMAIL="test@test.com"
>  >  SUBJECT="TEST SERVER  HDD df result"
>  >  /bin/mail -r "test@test.com" -s "$SUBJECT" "$TO_EMAIL" < /home/util/df_result.txt
>  >  
>  >  shell> chmod 701 ./monitor_df.sh
>  >  
>  >  shell> ./monitor_df.sh
>  >  
>  >```
>
>  - [How to batch backup](./centos7_backupscript.md)
>  >  > 일괄백업 - 스케줄러( cron ) 연동할 경우 일괄 자동 백업 가능
>

## [centos7] docker
>  - [ How to docker ](./docker.md)
>  >  > docker 설치 및 간단한 
>

## [centos7] open ssl 무료 인증서
>  - [ open ssl 무료 인증서 설정방법 https://letsencrypt.org/ko/getting-started/ ](./Lets_Encrypt_https.md)
>  >  > https://letsencrypt.org/ko/getting-started/
>  >  > 90 일 단위 갱신 진행시 지속적으로 무료 사용 가능
>

## [centos7]Codeignitor 4.x
>  - [How to Codeignitor 4.x install](./centos7_ci4_install.md)
>  >  > 라라벨 설치
>

## [centos7]nodejs
>  - [How to nodejs install_use_nvm](./centos7_nodejs_install_use_nvm.md)
>  >  > nvm 을 이용한 nodejs 설치 
>
>  - [How to Setting crawling environment](./centos7_nodejs_setting_crawling_environment.md)
>  >  >  install chromium / puppeteer / cheerio / korean font
>

## [centos7]Network
>  - [How to Checking ip address on Centos7](./how_to_checking_ip_address.md)  
>  >  > ip 주소 확인하기
>
>  - [Check DNS lookup results](./check_dns_lookup_results.md)
>  >  > 도메인 주소와 연결된 ip 주소 확인하기
>
>  - [How to Network Path Tracking](./how_to_network_path_tracking.md)
>  >  > 네트워크 경로 
>

## [centos7]Scheduler ( cron )
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

## [centos7]Apache PHP MariaDB install
>  - [How to APM install on Centos7](./centos7_apmsetup.md)
>  >  > 아파치 PHP 마리아DB 설치
>





## [centos7]File System ( Centos7 )
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
>  - tree
>  >  >디렉토리 구조 확인하기
>  >```
>  >   $ yum install tree
>  >   $ tree -d -L 2
>  >```
>
