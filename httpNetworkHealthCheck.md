
### backupScript.sh

```
#!/bin/bash

#!/bin/bash

RESPONSE=$(curl -L -s -o /dev/null -w "%{http_code}" [ TARGET SERVER URL ] )


if [ ${RESPONSE} -ne 200 ];then
    echo "${SERVER} returned bad status: ${RESPONSE}"

    MSGSEND_URL_1='https://api.telegram.org/bot[ APIKEY ]/sendmessage?chat_id=[수신자 텔레그램 채팅아이디]&text=[메시지]'

    #echo ${MSGSEND_URL_1}

    wget ${MSGSEND_URL_1}


    exit ${RESPONSE}
fi;


```
