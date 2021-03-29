
from __init__ import db,abandonment
from urllib.parse import quote_plus, urlencode
from urllib.request import Request, urlopen
#pip install elementpath
import xml.etree.ElementTree as ElementTree
from urllib.parse import unquote

def doAction():
    today_number = 0
    today_kind_dog = 0
    today_kind_cat = 0
    today_kind_others = 0
    
    ServiceKey =unquote('api')

    for i in range(1000,10000):
        url = 'url'
        queryParams = '?' + urlencode({quote_plus('ServiceKey') : ServiceKey, quote_plus('pageNo'):'{}'.format(i)})


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

        for x in itemList:
            desertionNo = x.findtext('desertionNo')
            orgNm=x.findtext('orgNm')


            db_abandonment = abandonment.query.filter_by(desertionNo=desertionNo).first()
            print(i)
            if (db_abandonment is None) and (orgNm=='경기도'):
                sexCd = x.findtext('sexCd')
                processState = x.findtext('processState')
                neuterYn = x.findtext('neuterYn')
                specialMark = x.findtext('specialMark')
                careNm = x.findtext('careNm')
                happenDt=x.findtext('happenDt')
                happenPlace=x.findtext('happenPlace')
                kindCd=x.findtext('kindCd')
                colorCd=x.findtext('colorCd')
                age=x.findtext('age')
                weight=x.findtext('weight')
                noticeEdt=x.findtext('noticeEdt')
                noticeSdt=x.findtext('noticeSdt')

                _abandonment_ = abandonment(desertionNo=desertionNo,sexCd=sexCd,processState=processState,neuterYn=neuterYn,specialMark=specialMark,
                careNm=careNm,orgNm=orgNm,happenDt=happenDt,happenPlace=happenPlace,kindCd=kindCd,colorCd=colorCd,age=age,weight=weight,noticeEdt=noticeEdt,noticeSdt=noticeSdt)
           
                db.session.add(_abandonment_)
                db.session.commit()
                print(noticeSdt)

    return 100


doAction()



