from urllib.parse import quote_plus, urlencode
from urllib.request import Request, urlopen, unquote # unquote 추가
#pip install elementpath
import xml.etree.ElementTree as ElementTree


####################### api 생성 ##############################


def doAction():
    today_number = 0
    today_kind_dog = 0
    today_kind_cat = 0
    today_kind_others = 0
    
    ServiceKey =unquote('API KEY')

    for i in range(1,10):
        url = 'url'
        queryParams = '?' + urlencode({quote_plus('ServiceKey') : ServiceKey, quote_plus('pageNo'):'{}'.format(i)})


        request = Request(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read()
        print (response_body)

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

            if happenDt == datetime.datetime.today().strftime('%Y%m%d'):
                today_number += 1

                _kindCd_ = kindCd.split(']')[0].split('[')[1]
                if _kindCd_ == '개': today_kind_dog += 1
                if _kindCd_ == '고양이': today_kind_cat += 1
                else: today_kind_others += 1

    return today_number, today_kind_dog, today_kind_cat, today_kind_others
