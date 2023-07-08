import requests
from color import color_print
import threading
import random
ua = [
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
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
]
rand_num = random.randint(1, len(ua))
header = {}
header["User-Agent"] = ua[rand_num - 1]
echo = color_print()
url_lst = []
def ip(ip_address, url_method):
    try:
        if url_method.lower() == "get":
            response = requests.get(ip_address, headers=header, timeout=1, verify=False)
        elif url_method.lower() == "post":
            response = requests.post(ip_address, headers=header, timeout=1, verify=False)
        else:
            print("[-] 请求方式不支持!!!")
        if response.status_code == 200:
            if ip_address not in url_lst:
                url_lst.append(ip_address)
            else:
                pass
    except:
        pass

def ip_live_scan(url_target, url_method, ip_live_num):
    threads = []
    urls = []
    try:
        for num in range(int(ip_live_num)):
            ur1 = str(url_target).replace("*", str(num))
            urls.append(ur1)
        print("正在探测存活, 请稍等!!!")
        for url in urls:
            t = threading.Thread(target=ip, args=(url, url_method,))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        if url_lst is not None:
            echo.print_blue("[*] 探测完毕，存活IP为: " + str(url_lst))
        else:
            echo.print_yellow("[x] 探测完毕，没有检测到当前C段存活IP!")
        return url_lst
    except:
        return url_lst
