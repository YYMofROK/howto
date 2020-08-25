## nodejs, puppeteer, chromium, cheerio , crawling 환경 설정  - 2020.08.25

## Installation environment 
```  
  * 설치환경
    Centos 7.x minimal  
```

### Installation script
```
# root 권한 취득
$ sudo su

# 크로미움 설치를 위한 저장소 추가
$ yum install -y epel-release

# 크로미움 설치
$ yum install -y chromium

# wget 설치
$ yum install -y wget

# unzip 설치
$ yum install -y unzip


# 폰트 다운로드 및 설치
$ cd /usr/share/fonts/
$ wget http://cdn.naver.com/naver/NanumFont/fontfiles/NanumFont_TTF_ALL.zip
$ unzip ./NanumFont_TTF_ALL.zip
$ rm NanumFont_TTF_ALL.zip
$ fc-cache -r

# node 구동 유저 추가
$ useradd nodeuser

# node 구동 유저로 전환
$ su nodeuser

# node 구동 유저의 홈 디렉토리 이동
$ cd ~

# puppeteer 설치
$ npm install puppeteer

# cheerio 설치
$ npm install -y cheerio

```


