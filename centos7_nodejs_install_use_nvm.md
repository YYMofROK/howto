## nvm 을 이용한 nodejs 설치 - 2020.08.25

## Installation environment 
```  
  * 설치환경
    Centos 7.x minimal  
```

### Installation script
```
# root 권한 취득
$ sudo su

# 패키지 업데이트
$ yum -y update

# node 구동 유저 추가
$ useradd nodeuser

# node 구동 유저로 전환
$ su nodeuser

# node 구동 유저의 홈 디렉토리 이동
$ cd ~

# node 환경 설정( NVM 사용 ) 및 실행
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
$ source .bash_profile
$ nvm ls-remote
$ nvm install v14.8.0
```


