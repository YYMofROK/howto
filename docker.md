# docker

## install sshd
>  - [How to docker install ]
>  >
>  >```
>  >   # 현재 작업중인 브랜치를 삭제하고자 하여 발생한 오류 다른 브랜치로 전환후 삭제 실행
>  >   
>  >   shell> yum install -y openssh-server
>  >
>  >   shell> yum install -y openssh-client
>  >
>  >   shell> yum install -y openssh-askpass
>  >   
>  >   vi /etc/ssh/sshd_config
>  >```
> ---------------------------------------------------------------------------------------------





vi /etc/ssh/sshd_config
vi /etc/selinux/config

iptables -L
vi /etc/rc.d/rc.local
chmod 701 /etc/rc.d/rc.local
reboot

yum update -y
yum group install -y "Development Tools"
yum install -y net-tools
yum install -y bind-utils
yum install -y rsync
yum install -y wget
yum install docker docker-registry

systemctl enable docker.service
systemmctl start docker.service
systemctl status docker


docker search a84146943/centos7-httpd2.4-php7.2:latest
docker run -dit --name centos7  -p 192.168.1.151:80:50080 --privileged -e container=docker -v /sys/fs/cgroup:/sys/fs/cgroup:ro e31efd6cc327 /usr/sbin/init
docker exec -it centos7 /bin/bash



docker commit -a 'yym' -m 'centos7-httpd2.4[80:50080]-php7.2.34' centos7-httpd2.4-php7.2.34:20201219_02
docker images
docker tag centos7-httpd2.4-php7.2 2c78cd7c7cc2
docker tag e31efd6cc327 a84146943/centos7-httpd2.4-php7.2
docker images
docker push a84146943/centos7-httpd2.4-php7.2


docker network
