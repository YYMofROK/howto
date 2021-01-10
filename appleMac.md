터미널에서 편집기를 연다
hosts 파일을 수정하기 위해서는 관리자 권한이 필요하기에 sudo 명령어를 꼭 써줘야 한다.
$ sudo vi /etc/hosts
혹은
$ sudo vi /private/etc/hosts 
내용을 편집한다.
  1 ##
  2 # Host Database
  3 #
  4 # localhost is used to configure the loopback interface
  5 # when the system is booting.  Do not change this entry.
  6 ##
  7 127.0.0.1   localhost
  8 255.255.255.255 broadcasthost
  9 ::1             localhost
 10 fe80::1%lo0 localhost
아이피 주소를 넣고 구분은 탭(tab)으로 해야 한다.
127.0.0.1    www.devkuma.com
DNS cache 를 갱신한다.
이제 hosts 파일이 수정하면 재부팅하거나, dscacheutil -flushcache 를 입력하면 바로 적용 하실 수 있다.
$ dscacheutil -flushcache



https://ninanung0503.medium.com/apple-silicon-m1-mac%EC%97%90-homebrew-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-7b6c0d3aba08
