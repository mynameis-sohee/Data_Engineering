#공공데이터포털 실시간 API 연동 기본코드 - 이 코드를 응용하여, 원하는 데이터 수집 가능

from flask import Flask, render_template, request, redirect, url_for, session
from urllib.parse import quote_plus, urlencode
from urllib.request import Request, urlopen
#pip install elementpath
import xml.etree.ElementTree as ElementTree

ServiceKey ='본인의 인코딩 KEY'

def doAction():
    today_number = 0
    for i in range(1,30):
        url = '본인의 url'
        queryParams = '?' + 'ServiceKey=' + ServiceKey+'&'+urlencode(
                {quote_plus('pageNo'):'{}'.format(i)}
        )


        request = Request(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read()
        #print (response_body)

        tree = ElementTree.ElementTree(ElementTree.fromstring(response_body))
        #print(tree)

        rootNode = tree.getroot()
        #print(rootNode)

        itemList = rootNode.getiterator('item')
        #print(itemList)

        index = 0
        for x in itemList:
            page_index = i
            index += 1
            noticeEdt = x.findtext('noticeEdt')
            popfile = x.findtext('popfile')
    
    return page_index, index, noticeEdt, popfile
