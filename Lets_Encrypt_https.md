## https://letsencrypt.org/ko/getting-started/
>
>  - [open ssl 무료 인증서] https://letsencrypt.org/ko/getting-started/
>
>  >  설치 스크립트
```
$
$ sudo yum install snapd
$ sudo ln -s /var/lib/snapd/snap /snap
$ sudo snap install core
$ sudo snap refresh core
$ sudo yum remove certbot
$ sudo snap install --classic certbot
$ sudo ln -s /snap/bin/certbot /usr/bin/certbot
$ sudo snap set certbot trust-plugin-with-root=ok
$ sudo snap install certbot-dns-route53
$ certbot renew --dry-run
$ certbot certonly 
         --manual
         --preferred-challenges dns
         --server https://acme-v02.api.letsencrypt.org/directory --agree-tos
         -m [ E-Mail Address ]
         -d [ DOMAIN NAME ]
$

Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator manual, Installer None
Requesting a certificate for [ DOMAIN NAME ]
Performing the following challenges:
dns-01 challenge for [ DOMAIN NAME ]

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please deploy a DNS TXT record under the name
_acme-challenge.addrgo.com with the following value:

Eh82hx-EYqQf4DVxqzPnwmlcAEZulvPyj2MOF0XVNKo

Before continuing, verify the record is deployed.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Press Enter to Continue
Waiting for verification...
Cleaning up challenges
Subscribe to the EFF mailing list (email: [  E-Mail Address ]).

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/[ DOMAIN NAME ]/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/[ DOMAIN NAME ]/privkey.pem
   Your cert will expire on 2021-04-05. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot
   again. To non-interactively renew *all* of your certificates, run
   "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le
$
$ cd /etc/letsencrypt/live/[ DOMAIN NAME ]
$ ls -al
$
total 4
drwxr-xr-x 2 root root  93 Jan  5 03:09 .
drwx------ 3 root root  38 Jan  5 03:09 ..
lrwxrwxrwx 1 root root  34 Jan  5 03:09 cert.pem -> ../../archive/[ DOMAIN NAME ]/cert1.pem
lrwxrwxrwx 1 root root  35 Jan  5 03:09 chain.pem -> ../../archive/[ DOMAIN NAME ]/chain1.pem
lrwxrwxrwx 1 root root  39 Jan  5 03:09 fullchain.pem -> ../../archive/[ DOMAIN NAME ]/fullchain1.pem
lrwxrwxrwx 1 root root  37 Jan  5 03:09 privkey.pem -> ../../archive/[ DOMAIN NAME ]/privkey1.pem
-rw-r--r-- 1 root root 692 Jan  5 03:09 README
$
$ openssl verify -CAfile chain.pem cert.pem
cert.pem: C = US, O = Let's Encrypt, CN = R3
error 2 at 1 depth lookup:unable to get issuer certificate
$
$ wget http://apps.identrust.com/roots/dstrootcax3.p7c
$
--2021-01-05 03:15:05--  http://apps.identrust.com/roots/dstrootcax3.p7c
Resolving apps.identrust.com (apps.identrust.com)... 192.35.177.64
Connecting to apps.identrust.com (apps.identrust.com)|192.35.177.64|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 893 [application/pkcs7-mime]
Saving to: ‘dstrootcax3.p7c’

100%[====================================================================================================================================================================================>] 893         --.-K/s   in 0s

2021-01-05 03:15:06 (102 MB/s) - ‘dstrootcax3.p7c’ saved [893/893]
$
$ ls -al
$
total 8
drwxr-xr-x 2 root root 116 Jan  5 03:15 .
drwx------ 3 root root  38 Jan  5 03:09 ..
lrwxrwxrwx 1 root root  34 Jan  5 03:09 cert.pem -> ../../archive/addrgo.com/cert1.pem
lrwxrwxrwx 1 root root  35 Jan  5 03:09 chain.pem -> ../../archive/addrgo.com/chain1.pem
-rw-r--r-- 1 root root 893 Feb 13  2020 dstrootcax3.p7c
lrwxrwxrwx 1 root root  39 Jan  5 03:09 fullchain.pem -> ../../archive/addrgo.com/fullchain1.pem
lrwxrwxrwx 1 root root  37 Jan  5 03:09 privkey.pem -> ../../archive/addrgo.com/privkey1.pem
-rw-r--r-- 1 root root 692 Jan  5 03:09 README

$
$ openssl pkcs7 -inform der -in dstrootcax3.p7c -out dstrootcax3.pem -print_certs
$ cp fullchain.pem fullca.pem
$ cat dstrootcax3.pem >> fullca.pem
$ openssl verify -CAfile fullca.pem cert.pem
cert.pem: OK
$
```
>

## Apache open-ssl 인증서 설치
>
>  >  설치 스크립트
```
```
>
$
$ yum install mod_ssl -y
$
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: d36uatko69830t.cloudfront.net
 * epel: ftp.iij.ad.jp
 * extras: d36uatko69830t.cloudfront.net
 * remi-php72: ftp.riken.jp
 * remi-safe: ftp.riken.jp
 * updates: d36uatko69830t.cloudfront.net
Resolving Dependencies
--> Running transaction check
---> Package mod_ssl.x86_64 1:2.4.6-97.el7.centos will be installed
--> Processing Dependency: httpd = 2.4.6-97.el7.centos for package: 1:mod_ssl-2.4.6-97.el7.centos.x86_64
--> Running transaction check
---> Package httpd.x86_64 0:2.4.6-93.el7.centos will be updated
---> Package httpd.x86_64 0:2.4.6-97.el7.centos will be an update
--> Processing Dependency: httpd-tools = 2.4.6-97.el7.centos for package: httpd-2.4.6-97.el7.centos.x86_64
--> Running transaction check
---> Package httpd-tools.x86_64 0:2.4.6-93.el7.centos will be updated
---> Package httpd-tools.x86_64 0:2.4.6-97.el7.centos will be an update
--> Finished Dependency Resolution

Dependencies Resolved

==============================================================================================================================================================================================================================
 Package                                              Arch                                            Version                                                          Repository                                        Size
==============================================================================================================================================================================================================================
Installing:
 mod_ssl                                              x86_64                                          1:2.4.6-97.el7.centos                                            updates                                          114 k
Updating for dependencies:
 httpd                                                x86_64                                          2.4.6-97.el7.centos                                              updates                                          2.7 M
 httpd-tools                                          x86_64                                          2.4.6-97.el7.centos                                              updates                                           93 k

Transaction Summary
==============================================================================================================================================================================================================================
Install  1 Package
Upgrade             ( 2 Dependent packages)

Total download size: 2.9 M
Downloading packages:
No Presto metadata available for updates
(1/3): httpd-tools-2.4.6-97.el7.centos.x86_64.rpm                                                                                                                                                      |  93 kB  00:00:00
(2/3): mod_ssl-2.4.6-97.el7.centos.x86_64.rpm                                                                                                                                                          | 114 kB  00:00:00
(3/3): httpd-2.4.6-97.el7.centos.x86_64.rpm                                                                                                                                                            | 2.7 MB  00:00:00
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                                                                          15 MB/s | 2.9 MB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Updating   : httpd-tools-2.4.6-97.el7.centos.x86_64                                                                                                                                                                     1/5
  Updating   : httpd-2.4.6-97.el7.centos.x86_64                                                                                                                                                                           2/5
  Installing : 1:mod_ssl-2.4.6-97.el7.centos.x86_64                                                                                                                                                                       3/5
  Cleanup    : httpd-2.4.6-93.el7.centos.x86_64                                                                                                                                                                           4/5
  Cleanup    : httpd-tools-2.4.6-93.el7.centos.x86_64                                                                                                                                                                     5/5
  Verifying  : 1:mod_ssl-2.4.6-97.el7.centos.x86_64                                                                                                                                                                       1/5
  Verifying  : httpd-tools-2.4.6-97.el7.centos.x86_64                                                                                                                                                                     2/5
  Verifying  : httpd-2.4.6-97.el7.centos.x86_64                                                                                                                                                                           3/5
  Verifying  : httpd-tools-2.4.6-93.el7.centos.x86_64                                                                                                                                                                     4/5
  Verifying  : httpd-2.4.6-93.el7.centos.x86_64                                                                                                                                                                           5/5

Installed:
  mod_ssl.x86_64 1:2.4.6-97.el7.centos

Dependency Updated:
  httpd.x86_64 0:2.4.6-97.el7.centos                                                                         httpd-tools.x86_64 0:2.4.6-97.el7.centos

Complete!

$
$ systemctl restart httpd
$ cat vhost_03_android_info.conf
$

#<VirtualHost *:80>
#    ServerName   android.addrgo.com
#    DocumentRoot /home/android/public_html
#</VirtualHost>

<VirtualHost *:80>
    ServerName android.addrgo.com
    DocumentRoot /home/android/public_html/app/public
       <Directory "/home/android/public_html/app/public">
               Options Indexes FollowSymLinks
               AllowOverride All
               Require all granted
       </Directory>
</VirtualHost>


<VirtualHost *:443>
    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/addrgo.com/cert.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/addrgo.com/privkey.pem
    SSLCertificateChainFile /etc/letsencrypt/live/addrgo.com/fullchain.pem

    ServerName android.addrgo.com
    DocumentRoot /home/android/public_html/app/public
       <Directory "/home/android/public_html/app/public">
               Options Indexes FollowSymLinks
               AllowOverride All
               Require all granted
       </Directory>

</VirtualHost>

