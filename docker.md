# How to docker install

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
>  >   # 개발 및 테스트 목적
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
>  >   # 개발 및 테스트 목적
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
>  >   
>  >```
> ---------------------------------------------------------------------------------------------

## yum 을 이용한 docker 설치 및 서비스 시작
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   shell> yum install docker docker-registry
>  >   shell> systemctl enable docker.service
>  >   shell> systemmctl start docker.service
>  >   shell> systemctl status docker
>  >   
>  >```
> ---------------------------------------------------------------------------------------------

## docker 를 이용한 Apache Web Service Container 생성하기
> ---------------------------------------------------------------------------------------------
>  >
>  >```
>  >   shell> docker search a84146943/centos7-httpd2.4-php7.2:latest
>  >   shell> docker pull a84146943/centos7-httpd2.4-php7.2
>  >   shell> docker run -dit --name centos7  -p [HOST IP ADDR]:[PORT]:[ContainerPort] --privileged -e container=docker -v /sys/fs/cgroup:/sys/fs/cgroup:ro [이미지아이디] /usr/sbin/init
>  >   shell> docker exec -it centos7 /bin/bash
>  >```
> ---------------------------------------------------------------------------------------------

## 경험한 장애 유형
> ---------------------------------------------------------------------------------------------
>  > ### Apache 컨테이너가 실행중인데 http 접속이 안되는 경우( 브라우져에서 접속 등 )
>  >  > ##### Host 의 방화벽 정책을 확인한다
>  >  > ```
>  >  >
>  >  > shell> iptables -F # 방화벽을 모두 열어서 확인하기
>  >  >
>  >  > ```
>  >  >
>  >  > ##### docker 재시작 - centos 7
>  >  > ```
>  >  >
>  >  > shell> systemctl restart docker
>  >  > shell> docker ps -a
>  >  > shell> docker start [CONTAINER_ID]
>  >  >
>  >  > ```
>  >  >
>  >  > ##### docker 재시작 - MacOS ( Macbook )
>  >  > ```
>  >  >
>  >  > shell> killall Docker && open /Applications/Docker.app
>  >  > shell> open --background -a Docker
>  >  > shell> docker start [CONTAINER_ID]
>  >  > 
>  >  > ```
>  >  > 
>  >  >##### container 내부 apache 실행여부 확인
>  >  > ```
>  >  >
>  >  > shell> docker exec -it [CONTAINER_ID] /bin/bash
>  >  > shell> systemctl status httpd
>  >  >
>  >  > ```
>  >
> ---------------------------------------------------------------------------------------------













