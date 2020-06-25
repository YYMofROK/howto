
### backupScript.sh

```
#!/bin/bash

# /home 디렉토리 하위의 디렉토리들을 tar.gz 형태로 압축하여 /home/backup 디렉토리에 저장한다.
# 단 : /home/backup 디렉토리 제외

NowTime=$(date +%Y%m%d%H%M)
HomeDirPath="/home"
BackDirPath="/home/backup"

for LINE in `ls ${HomeDirPath}`
do
if [ ${HomeDirPath}"/$LINE" != ${BackDirPath} ]; then
        tar cfz ${BackDirPath}/${LINE}_${NowTime}.tar.gz ${HomeDirPath}/${LINE}
fi
done

```
