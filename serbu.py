import urllib.request as urllib2
import urllib
import sys
import time
import random
import re
import os
os.system("clear")
# Warna
B = '\033[1m'  # Bold
R = '\033[31m'  # Red
G = '\033[32m'  # Green
Y = '\033[33m'  # Yellow
BL = '\033[34m'  # Blue
P = '\033[35m'  # Purple
W = '\033[37m'  # White
U = '\033[2m'  # Underline
N = '\033[0m'  # Normal
# Pastikan Proxy List 1 Dir Dengan Script Python Ini
proxy_list = "proxylist.txt"
bacod = ['Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-J700M Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; F5121 Build/34.0.A.1.247) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.1.944 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-N9500 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.0.0)',
'Mozilla/5.0 (Linux; Android 5.1.1; Lenovo-A6020l36 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; vivo y35 Build/N2G48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; Lenovo-A6020l36 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-J700M Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; F5121 Build/34.0.A.1.247) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.1.944 Mobile Safari/537.36']
# Hargai Pembuat!.. Coding Ga Gampang!..
gblk = ['http://google.com', 'http://bing.com',
    'http://facebook.com', 'http://twitter.com', 'http://yahoo.com']

print('')
print(B+BL+'#-----------------------------------------#')
print(B+R+'WARNING')
print(B+BL+'#-----------------------------------------#')
print(B+W+'[x] Matikan Data Terlebih Dahulu dan Aktifkan Kembali')
print(B+W+'[x] Pastikan Url Diawalinya Dengan http or https')
print(B+W+'[x] Saat Memasukan [Url Visitor] Tidak Terlihat')
print(B+W+'[x] Jika Kesalahan Dalam Url Silahkan Close Terminal and Open Kembali')
print(B+W+'[x] Jika Saat Bot Sedang Berjalan Lalu [Proxy Error] Coba Matikan Data dan Nyalakan Kembali')
print(B+BL+'#-----------------------------------------#')
print(B+R+'WARNING')
print(B+BL+'#-----------------------------------------#')
ini_url = input(B+Y+"[+] Masukan Url Visitor : ")
print('')
print(B+Y+'[+] Url Visitor Anda => '+B+BL+'|'+B+W, ini_url)
print(B+BL+'#-----------------------------------------#')


def Autoclicker(proxy1):
    try:
        proxy = proxy1.split(":")
        print (B+BL+"#-----------------------------------------#\n"+B+W+'[-]',proxy1, ""+B+P+"=> Process"+N)
        time.sleep(2)
        proxy_set = urllib2.ProxyHandler({"http" : "%s:%d" % (proxy[0], int(proxy[1]))})
        opener = urllib2.build_opener(proxy_set, urllib2.HTTPHandler)
        opener.addheaders = [('User-agent', random.choice(bacod)),
                        ('Refferer', random.choice(gblk))]
        urllib2.install_opener(opener)
        f = urllib2.urlopen(ini_url)
    # 187034
        if "google.com" in f.read():
            print (B+G+"[*] 200 OK"+"\n"+B+BL+"#-----------------------------------------#\n"+N)
        else:
            print (B+R+"[*] Link Gagal Di Kunjungi !\n"+B+BL+"#-----------------------------------------#\n"+N)
            print (B+R+"[!] Proxy / Connection Failed\n"+B+BL+"#-----------------------------------------#\n"+N)
    except:
           print (B+R+"[!] Proxy Error\n"+B+BL+"#-----------------------------------------#\n"+N)
           time.sleep(5)
           pass

def loadproxy():
    try:
        get_file = open(proxy_list, "r")
        proxylist = get_file.readlines()
        count = 0
        proxy = []
        while count < len(proxylist):
          proxy.append(proxylist[count].strip())
          count += 1
        for i in proxy:
            Autoclicker(i)
    except IOError:
        print (B+W+"\n[-] Error : Proxy List Tidak Ditemukan / Belum Dibuat\n"+N)
        sys.exit(1)

def main():
   print ("""
"""+N)
   loadproxy()
if __name__ == '__main__':
    main()
