#__author__ = 'techxsh'
#   encoding : gb2312
import sys,socket,urllib.request,re,os
#url = sys.argv[1]
#url = 'www.qq.com'
print(
	'''
	##################################################################
	##使用前可先在ping.chinaz.com判断该站点是否存在cdn，以免功亏一篑##
	##################################################################
	'''
)
url = input("请输入需反查的域名：")
try:
    url = re.sub('http://','',url)
    url = re.sub('/','',url)
except re.error as err:
    print()
try :
    ip = socket.gethostbyname(url)
except socket.error:
    print("域名格式输入错误，请输入类似www.xxx.com的格式")
    os.system("pause")
    sys.exit()
#ip = '121.9.204.234'
#print(ip)
aizhanurl = 'http://dns.aizhan.com/index.php?r=index/domains&ip='+ip+'&page=1&_=1401180219646'
print('ip为：'+ip+'\n')
firstdata = urllib.request.urlopen(aizhanurl).read()
#print (firstdata)
if firstdata != b'null':
    maxpage = int(re.search(r'"maxpage":(.*?),"domains":',str(firstdata)).group(1))+1
    #print(maxpage)
    for pagenumber in range(1,maxpage,1):
        urlget = 'http://dns.aizhan.com/index.php?r=index/domains&ip='+ip+'&page='+str(pagenumber)+'&_=1401180219646'
        data = urllib.request.urlopen(urlget).read()
        path = re.search(r'"domains":\[(.*?)],"prs"',str(data))
        #print (path)
        urlgroup = path.group(1)+','
        #print (urlgroup)
        urllist = re.findall(r'"(.*?)",', urlgroup)
        #print (urllist)
        for urls in urllist:
            try:
                if socket.gethostbyname(urls)==ip:
                    #datatemp = urllib.request.urlopen('http://'+urls).read()
                    #titletemp = re.search(r'<title>(.*?)</title>',str(datatemp)).group(1)
                    print(urls)
                    out = open(url+'.txt','a')
                    out.write(urls+'\n')
                    out.close()    
            except socket.error:
                print (urls+' 域名解析失败')
        print('\n写入url至当前目录'+url+'.txt成功\n')		
else: print('同IP上没有找到其他域名')
os.system("pause")