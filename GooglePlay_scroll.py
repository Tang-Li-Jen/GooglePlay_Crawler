import requests
from bs4 import BeautifulSoup
import pandas as pd


headers ={
	'Content-Length': '280',
	'Accept': '*/*',
	'Origin': 'https://play.google.com',
	'x-client-data': 'CIi2yQEIpLbJAQjEtskBCKmdygEIqKPKARitmMoBGJKjygE=',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'https://play.google.com/store/apps/collection/cluster?clp=wgYpCiUKH2NvbS5iaXRzbWVkaWEuYW5kcm9pZC5tdXNsaW1wcm8QARgDGAE%3D%3AS%3AANO1ljL05bg',
	'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
	'Cookie': 'GMAIL_RTT=191; HSID=A1yP-45LO1W8voHWo; SSID=Atwi-DcPW76supcsk; APISID=p9eqjb7yW4l5vz8E/Acpe8RgUNBMUZ2hyG; SAPISID=2-RIGJ1c4DU6b26u/AmkjeW2brvHw4OZ-K; SID=6gWGp1rpZQLBdNKWHltLRoYCYctib7urH0YeEpXwyUDADFXyHy2-KebytuACLGFKLzAGeQ.; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=b00701160@gmail.com; _ga=GA1.3.170942518.1524834945; _gid=GA1.3.1711828426.1524834945; OTZ=4375518_24_24__24_; NID=128=AKp-127v0PLh1G9Cwcby8TiYn9FFEU7eYX3rolkVPETS9PIB2g6Tr2wTu8dC17MWEJKm5xRn2QGmS1CxR8EihnI41nWfWw3zPmD95eyeJgcPxV2x4WSXmBkKvHEQGfZnX_HptnRKzqYrg7a9zzNH9W-1V6DuIGg50xJjV-Zce748obQqZlK4VdjxJKFCs3QP3mfWvYszXUr_3QxS2bldRHm42AwK1pMxVu0fafmUc5PzmVbVS0z7PFmdAnpg_I16Tg4jFwRdQcbfCM9tRJNFc9diDtfWMjgZV1wriSmuZwNPdCw; S=photos_html=XQUG6ctVncMRM7SE44mPkdOY5ItJFPam:billing-ui-v3=g-SOdwimAHBNfGGR39nwCRTzpGqnpv7H:billing-ui-v3-efe=g-SOdwimAHBNfGGR39nwCRTzpGqnpv7H; 1P_JAR=2018-4-27-15; PLAY_PREFS=CqAMCIbPmq29FRKWDAoCVFcQotTmvbAsGtcLEhMUFRjxAYQCrwLhA8IExASBBeMF5QXoBdcGkJWBBpGVgQaSlYEGlZWBBpeVgQaklYEGuJWBBsCVgQbBlYEGxJWBBsWVgQbHlYEGyJWBBsmVgQbOlYEGz5WBBtCVgQbUlYEG2ZWBBt6VgQbulYEG75WBBvCVgQbylYEG-JWBBvqVgQb8lYEGhpaBBoeWgQaLloEGjpaBBpGWgQaaloEGnpaBBqGWgQajloEGpJaBBqaWgQbul4EG75eBBoWYgQaJmIEGvpiBBqubgQatm4EGyZuBBsqbgQbLm4EG1ZuBBrydgQbdnYEG552BBpCegQaWnoEG4qKBBvOigQaLo4EGmqSBBrKkgQbqpYEGxqaBBrysgQbWr4EGh7KBBomygQbWsoEGsbSBBta5gQaOwIEGosCBBsDAgQbBwIEG8sCBBtbCgQaMxYEGysaBBvjHgQaqyoEG2MyBBtzMgQbdzYEGhs6BBqHPgQbE0oEGldWBBtrYgQbi2IEGk9mBBvLbgQbY5IEGl-WBBrjogQbP64EGsOyBBtf1gQa6-4EGw_-BBsX_gQbH_4EGyf-BBtWDggbIhIIGuYaCBqaHgganh4IG7IeCBu2HggbrjYIG-42CBomOggbMkYIGlZiCBo-aggaZmoIGwZqCBveaggadnoIG1Z6CBrqggga7oIIG9qKCBuKkggaSpYIGq6WCBs2lggbyp4IGnqiCBrSoggattoIG_LmCBv65ggb_uYIGwruCBo-_ggbqwIIGvMGCBpDLggaRy4IGzcuCBtHLggbczIIG2NCCBvPRggaL0oIG2tOCBoHYggaF2oIGj9qCBpzaggaj2oIGrtuCBr7bggbF24IGl9yCBrHcggbq3YIG-N2CBu_fggam4YIG0OGCBuThggbl4YIGlumCBqPtggaF7oIGs-6CBozwggax8IIGlvGCBr7xggbr9oIGrfiCBrP4ggb2-oIG3_uCBuP7ggaD_IIGhfyCBtv8ggbc_IIG__yCBoH9ggaC_4IGgICDBomBgwbygYMGgYKDBumEgwaQhYMGuoWDBpuIgwbQiIMG8IiDBoWPgwaQj4MG2ZGDBv2Rgwb8koMGrJWDBriVgwbAloMG5ZaDBtyXgwbzmYMG25qDBpmbgwbtm4MG7puDBtCcgwb0noMGlZ-DBsafgwbTn4MGmKCDBpuggwb9oIMGuaODBuCugwbsr4MGlrCDBpW0gwaYtIMGuLaDBqO3gwauuIMGubiDBsO4gwbgvIMG9LyDBva8gwawvoMGzb6DBrDBgwb2wYMGycKDBuTGgwatyIMGnsmDBpvKgwaHzYMGys2DBv7Ngwai0IMG6NCDBr_Tgwb504MG69SDBofVgwbP1oMG69aDBofXgwbj14MG6deDBtHZgwas3IMGgt-DBo_fgwbh34MGhuCDBojggwaU4YMG7-ODBv_lgwaN5oMG6-iDBsnsgwbq7IMGju2DBpXugwbj74MGpfKDBtX0gwb79IMGr_eDBvf3gwaH-IMGjfiDBpj4gwbW-YMG3vmDBoz6gwav-oMGw_qDBv79gwaH_4MGkYCEBpKAhAbTgYQG3YGEBt-BhAb6g4QG14SEBs6GhAbih4QG44eEBqSJhAa-iYQG-4qEBqeLhAbDi4QGmoyEBp2MhAb1jIQGgI6EBpOOhAabj4QG7pGEBvyRhAbckoQG7pOEBqCXhAbCl4QGzpeEBomYhAaGmYQGmJmEBqKZhAa7mYQG_ZqEBvmbhAaHnIQGmZyEBt6chAbgnIQGip2EBt2dhAabnoQGs56EBu2ehAbhn4QGuaCEBtehhAbNo4QG96OEBoWkhAaypIQGyqSEBq2lhAb_p4QGpKiEBqqohAbZqIQG9aiEBpKphAagqYQGo6mEBqWphAanqYQGqamEBqyphAatqYQGr6mEBp2vhAair4QGp6-EBsGvhAb3r4QG-K-EBquwhAa2sYQGubGEBrazhAa4tIQGjLWEBve2hAb7t4QG4biEBijvi_u5sCw6JGQxMTBkNTJlLWVmYmQtNDNjMS05YWMwLTdiMjc0M2NlNzg1Y0ABSAA:S:ANO1ljLxpCoCpb3mcg; _gat=1; SIDCC=AEfoLeYLHKLgKFbf3s5vN8XqRK6CF9TjTDUZU8y7nAVthrIfHQe6E9RiOSrZuKaVgNlA83YPIHdGA1Fhr6aE'
	}
payload ={
# start needs adjusting
		'start': 114,
		'num': 48,
		'numChildren': 0,
# pagTok needs adjusting
		'pagTok':'gtP_uAMSCgn6noGdAwMIkwEQour9vrAs:S:ANO1ljKw0cs',
# gtP_uAMRCgj6noGdAwIIMRDo0KG_sCw=:S:ANO1ljJq9NA
# gtP_uAMRCgj6noGdAwIIYhDo0KG_sCw=:S:ANO1ljJZPqs
# gtP_uAMSCgn6noGdAwMIkwEQ6NChv7As:S:ANO1ljLPEgA
		'clp':'wgYpCiUKH2NvbS5iaXRzbWVkaWEuYW5kcm9pZC5tdXNsaW1wcm8QARgDGAE=:S:ANO1ljL05bg',
		'pagtt':3,
		'cctcss':'square-cover',
		'cllayout':'NORMAL',
		'ipf':1,
		'xhr':1,
		'token':'ZpVo2GuFT6TAmFA6wIQj5dfxaA4:1524843029676'
}
r = requests.post('https://play.google.com/store/apps/collection/cluster?authuser=0',data=payload, headers=headers)
#print r.text
soup = BeautifulSoup(r.text, 'html.parser')
#print soup.prettify()
domain = 'https://play.google.com'
url = []
app = []
org = []
desc = []
star = []
for element in soup.find_all('a', {"class": "title"}):
    url.append(domain+element.get('href'))
    app.append(element.get('title'))

for element in soup.find_all('a', {"class": "subtitle"}):
    org.append(element.get('title'))
for element in soup.find_all('div', {"class": "description"}):
    desc.append(element.text)
for element in soup.find_all('div', {"class": "tiny-star star-rating-non-editable-container"}):
    star.append(element.get('aria-label'))

df = pd.DataFrame({'url':url, 'app':app, 'org':org, 'desc':desc, 'star':star})
print len(df)
print df.head()

