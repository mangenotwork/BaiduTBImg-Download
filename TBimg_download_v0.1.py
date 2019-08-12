#!/usr/bin/Python
# -*- coding: utf-8 -*-

__author__ = 'man'

import urllib
import requests
import time,re,os,sys,random
import datetime
import urllib.request
import urllib.error
from urllib.request import urlopen
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


#保存路径
LOCAL_PATH = "D:\\tbimg\\"




#USER_AGENTS 随机头信息
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

#构造请求头
HEADER = {
    'User-Agent': random.choice(USER_AGENTS),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
}


#Get网页，返回内容
def get_html( url_path, payload = '', cookies = '',proxies = ''):
    print("[ GET Url ] : " + url_path)
    try:
        s = requests.Session()
        r = s.get(
                url_path,#路径
                headers=HEADER,#请求头
                params=payload,#传参 @payload 字典或者json
                cookies=cookies,#cookies
                verify=True,#SSL验证 @verify False忽略;True开启
                proxies=proxies,#代理
                timeout=30)#@timeout 超时单位 秒
        r.raise_for_status()
        #print r.headers#获取响应头
        #print r.cookies#获取cookies
        return r.text
    except ReadTimeout:
        print('Timeout')
    except ConnectionError:
        print('Connection error')
        print('wite 30s...')
        time.sleep(30)
        '''
        print('Connection error')
        proxies_ip = {
          "http": get_proxy1()
        } 
        get_html(url_path,proxies = proxies_ip)
        '''
        get_html(url_path)
    except RequestException:
        print('RequestException')


def get_status( url_path, payload = '', cookies = '',proxies = ''):
    try:
        s = requests.Session()
        r = s.get(
                url_path,#路径
                headers=HEADER,#请求头
                params=payload,#传参 @payload 字典或者json
                cookies=cookies,#cookies
                verify=True,#SSL验证 @verify False忽略;True开启
                proxies=proxies,#代理
                timeout=30)#@timeout 超时单位 秒
        r.raise_for_status()
        #print r.headers#获取响应头
        #print r.cookies#获取cookies
        print(r.status_code)
        return r.status_code
    except ReadTimeout:
        print('Timeout')
    except ConnectionError:
        print('Connection error')
    except RequestException:
        print('RequestException')




#basic function
class TB_get:
	def __init__(self):
		pass

	#获取html
	def get_html(self,url):
		page = get_html(url)
		return page

	#获取url状态
	def get_state(self,url):
		code=get_status(url)
		return code

	#获取网页title
	def get_title(self,url):
		reg = r'<title>(.*?)</title>'
		reger = re.compile(reg)
		data = re.findall(reger, get_html(url))
		return data[0]

	#获取回复信息
	def get_Replypost(self,url):
		reg = r'l_reply_num.*?</li>'
		reger = re.compile(reg)
		data = re.findall(reger, get_html(url))
		info = re.compile(r'<span .*?>(.*?)</span>')
		info_data = re.findall(info, str(data))
		return int(info_data[0])

	#页数
	def get_pagenumber(self,url):
		reg = r'l_reply_num.*?</li>'
		reger = re.compile(reg)
		data = re.findall(reger, get_html(url))
		info = re.compile(r'<span .*?>(.*?)</span>')
		info_data = re.findall(info, str(data))
		return int(info_data[1])


class TB_filter:
	def __init__(self,html_page):
		self.data=html_page
 
	#匹配所有<href>
	def filter_href(self):
	    reg = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
	    reger = re.compile(reg)
	    data = re.findall(reger, self.data)
	    return data

	#匹配所有<a>
	def filter_a(self):
	    reg = r'<a .*?>(.*?)</a>'
	    reger = re.compile(reg)
	    data = re.findall(reger, self.data)
	    return data

	#匹配所有 src:
	def filter_src(self):
	    reg = r"(?<=src=\").+?(?=\")|(?<=src=\').+?(?=\')"
	    reger = re.compile(reg)
	    data = re.findall(reger, self.data)
	    return data


#下载功能; 下载 png,jpg
def download_img(path_html):
	tb = TB_get()
	print("Title : "+tb.get_title(path_html))
	if 'page404' in tb.get_html(path_html):
		print(u"很抱歉，该贴已被删除。")
	else:
		print("state : "+str(tb.get_state(path_html)))
		#save_path=LOCAL_PATH.replace('\\', '\\\\')+tb.get_title(path_html)+"\\"
		#save_path=LOCAL_PATH+tb.get_title(path_html)+"\\"
		save_path = LOCAL_PATH
		isExists=os.path.exists(save_path)
		if not isExists:
			os.makedirs(save_path)
		page_number = tb.get_pagenumber(path_html)#获取当前贴吧的页数
		print(u"页数 ： "+str(page_number))
		print(u"回复贴 : "+str(tb.get_Replypost(path_html)))
		download_page = 0
		while download_page < page_number:
			try:
				download_html=path_html+'?pn='+str(download_page+1)#对每页进行下载
				print("\n\nstart access : "+download_html)
				state_code=tb.get_state(download_html)
				print("state : "+str(state_code))
				if tb.get_state(download_html) == 200:#如果状态是200就可以下载 否则不能下载
					page_data = tb.get_html(download_html)
					fl = TB_filter(page_data)
					data = fl.filter_src()
					pictures_number=0
					for pictures in data:
						pictures_number+=1
						#print(pictures)
						dex = pictures.split(".")[-1]
						#print(dex)
						#print("\n\n\n\n")
						if dex in ["png","jpg","gif","jpeg"]:
							if "https" in pictures or "http" in pictures:
								if "static-pb" not in pictures and "sign_err" not in pictures and "icon_close" not in pictures:
									name= str(pictures.split("/")[-1])
									tt= int(time.time())
									newname=str(tt)+"."+dex
									Path_img=save_path+newname
									imgname=str(name.split("_")[0])
									if imgname != "image" and '?' not in name:
										print("\nstart download ====> "+name)
										print("loading.......")
										urllib.request.urlretrieve(pictures,Path_img)
										print("download succees ====> "+newname)
										time.sleep(1)
						else:
							print("Not Found need images！")
				else:
					print("access failed!! state : "+state_code)
				download_page+=1
			except:
				print("go on")

	
#下载器  只需要给定帖子路径，和帖子页数
def downloader(tb_path,tb_pg):
	tb_path='https://tieba.baidu.com/f?kw='+tb_path+'&ie=utf-8&pn='+str((tb_pg-1)*50)
	#print tb_path
	tb = TB_get()
	get_all_tb=tb.get_html(tb_path)
	if tb.get_state(tb_path) == 200:
		print("\n\nAccess : "+tb_path)
		reg = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
		reger = re.compile(reg)
		data = re.findall(reger, get_all_tb)
		for tb_link in data:
			reg1 = r'//tieba.baidu.com/p/.{0,}|/p/.{0,}'
			reger1 = re.compile(reg1)
			all_tb_link = re.findall(reger1, tb_link)
			if all_tb_link != []:#获取当前页数的贴吧的所有帖子
				assign_link=str(all_tb_link).split("/p")[-1]
				assign_link=str(assign_link)[0:-2]
				donwload_link= "https://tieba.baidu.com/p"+assign_link
				print(donwload_link)
				download_img(donwload_link)
	else:
			print("access failed!! state : ")




#搞笑图
#内涵图
#美女
#美女图
#女神
#壁纸
#手机壁纸
#电脑壁纸
#头像
#qq头像
#李毅吧
#D吧
#帝吧
#表情包
if __name__ == '__main__':
	n=1
	while n<100000:
		try:
			downloader('帝吧',n)
			n+=1
		except:
			print("继续")
		
