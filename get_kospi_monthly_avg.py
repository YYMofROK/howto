# KOSPI 지수 종가기준 월 평균 값 가져오기 샘플

import requests

import xml.etree.ElementTree as ET

from pprint import pprint

apiKey = "BXIMJ3E2E1XQCNAWW4CU"

## 호출하려는 OpenAPI URL를 정의합니다.
#url = "http://ecos.bok.or.kr/api/StatisticItemList/sample/xml/kr/1/1/021Y125"
url = "https://ecos.bok.or.kr/api/StatisticSearch/" + apiKey + "/xml/kr/1/12/028Y015/MM/202101/202112/1070000/?/?"
# http://ecos.bok.or.kr/api/StatisticSearch/sample/xml/kr/1/10/028Y015/MM/202101/202112/1070000/?/?/


#url = "https://naver.com"
## 정의된 OpenAPI URL을 호출합니다.
response = requests.get(url)

### http 통신 결과 코드 확인
print("response.status_code : " + str( response.status_code ) )

## http 요청이 성공했을때 API의 리턴값을 가져옵니다.
if response.status_code == 200:
    contents = response.text
    # print("@@@@@ API 수신 문자열(XML) @@@@@")
    # pprint(str(contents))
    ecosRoot = ET.fromstring(contents)
    # print(str(len(ecosRoot)))

list_total_count = ecosRoot.find('./list_total_count')
print("list_total_count : " + str(list_total_count.text))

print("@@@@@ 2021-01 ~ 2021-12 월별 KOSPI 종가 평균 @@@@@")
for i in range(1, int(list_total_count.text)):
    # print("@@@@@ ROW NUMBER [ " + str(i) + " ] @@@@@")
    row = ecosRoot.find("./row["+str(i)+"]")
    # print(str(row.find('STAT_CODE').text))
    # print(str(row.find('STAT_NAME').text))
    # print(str(row.find('ITEM_NAME1').text))
    # print(str(row.find('TIME').text))
    # print(str(row.find('DATA_VALUE').text))
    # print(str(row.find('UNIT_NAME').text))
    temp = str(row.find('TIME').text) + ":" + str(row.find('UNIT_NAME').text)
    print(temp)

print("KOSIP 지수 기준 : 1980.01.04=100 ")
