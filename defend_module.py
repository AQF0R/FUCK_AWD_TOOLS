import os
import glob
import hashlib
import time
import shutil
from color import color_print
echo = color_print()

def print_directory_tree(startpath, level=0):
	dir_indent = "|-->" * level + "|-->"
	file_indent = "|-->" * (level + 1) + "|-->"

	if level == 0:
		echo.print_green(startpath)
	else:
		echo.print_green(f"{dir_indent}{os.path.basename(startpath)}")
	for root, dirs, files in os.walk(startpath, topdown=True):
		for f in files:
			echo.print_green(f"{file_indent}{f}")
		for d in dirs:
			print_directory_tree(os.path.join(root, d), level + 1)


def get_file_md5(filename):
	m = hashlib.md5()
	with open(filename,'rb') as file:
		while True:
			data = file.read(4096)
			if not data:
				break
			m.update(data)
	return m.hexdigest()

def file_Backup(path, save_path):
	try:
		shutil.copytree(f'{path}',save_path)
		echo.print_green("[*] 文件备份成功!")
	except:
		echo.print_red("[x] 文件备份失败, 请检查是否已经存在备份文件")

def get_file_md5(file_path):
	hasher = hashlib.md5()
	with open(file_path, 'rb') as f:
		for chunk in iter(lambda: f.read(4096), b''):
			hasher.update(chunk)
	return hasher.hexdigest()

def file_Monit():
	old_files = {}
	global startpath
	startpath = "./"
	for root, dirs, files in os.walk(startpath, topdown=True):
		for file in files:
			file_path = os.path.join(root, file)
			old_files[file_path] = get_file_md5(file_path)

	while True:
		new_files = {}
		for root, dirs, files in os.walk(startpath, topdown=True):
			for file in files:
				file_path = os.path.join(root, file)
				new_hash = get_file_md5(file_path)
				if file_path not in old_files or new_hash != old_files[file_path]:
					echo.print_yellow("[!] 文件" + file_path.replace('./', '') + "添加或更改!")
					os.remove(file_path)
					try:
						shutil.copyfile(file_path.replace('./', '/'), file_path)
						echo.print_green("[*] 修复完成!")
					except:
						echo.print_red("[x] 修复失败!")

				new_files[file_path] = new_hash

		removed_files = set(old_files.keys()) - set(new_files.keys())
		for file_path in removed_files:
			echo.print_yellow("[!] 文件" + file_path.replace('./', '') + "消失!")
			try:
				shutil.copyfile(file_path.replace('./', '/'), file_path)
				echo.print_green("[*] 修复完成!")
			except:
				echo.print_red("[x] 修复失败!")

		old_files = new_files
		st = f"""
----------------------------------------------------------------
		文件总数:{len(new_files)}
		文件夹总数:{len(old_files)}   (Ctrl+c 退出文件监控)
----------------------------------------------------------------
		"""
		echo.print_Binline(st)
		time.sleep(3)

def php_file_list(path):
    php_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.php'):
                php_list.append(os.path.join(dirpath, filename))

    for file_path in php_list:
        print(file_path)
    echo.print_green(f'PHP文件总数:{len(php_list)}')

def file_function_check(path):
	php_files = glob.glob(f'{path}/**/*.php', recursive=True)
	danger_function_list = ['eval', 'system', 'base64', 'GET', 'POST', 'exec']
	danger_files = []
	for php_file in php_files:
		with open(php_file, 'r', encoding='utf8') as file:
			lines = file.readlines()
			for line_number, line in enumerate(lines, start=1):
				for danger_function in danger_function_list:
					if danger_function in line:
						danger_files.append((php_file, line_number, danger_function))
	if len(danger_files) > 0:
		for file, line_number, danger_function in danger_files:
			echo.print_red(f'[!] 存在危险 >>> {file} 可能具有危险函数[{danger_function}] 所在行数: {line_number}')
	else:
		echo.print_green('[*] PHP文件内容没有发现危险!')

	echo.print_Binline(f"[*] PHP 文件总数: {len(php_files)}")
	echo.print_yellow("[*] 检测结束, 工具检测可能会有遗漏，建议再次手动排查")

def loading_Waf(path):
	php_list = []
	echo.print_yellow("[*] 正在加载PHP文件")
	for root, dirs, files in os.walk(f'{path}', topdown=True):
		for f in files:
			if f[-4:] == '.php':
				php_list.append(root + '/' + f)
	echo.print_green(f"[*] PHP 文件总数: {len(php_list)}")
	echo.print_yellow("[*] 正在加载WAF")
	for i in range(len(php_list)):
		try:
			lines = open(php_list[i], "r").readlines()
			length = len(lines) - 1
			for j in range(length):
				try:
					if '<?php' in lines[j]:
						lines[j] = lines[j].replace('<?php', f'<?php\nrequire_once(\'./payload/waf.php\'); \n')
						echo.print_Ginline("[*] PHP文件" + php_list[i].replace("./", "") + "载入 WAF 成功!")
				except:
					echo.print_red("[x] PHP文件" + php_list[i].replace("./", "") + "载入 WAF 失败!")
			open(php_list[i], 'w').writelines(lines)
		except:
			pass
def defense():
	global root_path
	root_path = './backup'
	while True:
		st = """
    输入 1 生成文件树
    输入 2 启动文件监控模块
    输入 3 文件备份
    输入 4 PHP文件列表
    输入 5 PHP文件函数检查
    输入 6 一键PHP文件上WAF (自定义WAF可修改 payload/waf.php 文件内容)
    输入 7 退出防御模块
		"""
		echo.print_blue(st)
		moudle_num = int(input('\033[0;36m请输入序列号:\033[0m'))
		if moudle_num == 1:
			print_directory_tree('./')
		elif moudle_num == 2:
			file_Monit()
		elif moudle_num == 3:
			path = str(input("请输入需要备份的目录(eg:/):"))
			save_path = str(input("请输入备份存放路径(eg:./bakup):"))
			file_Backup(path, save_path)
		elif moudle_num == 4:
			path = str(input("请输入需要获得的PHP起始目录(eg:/):"))
			php_file_list(path)
		elif moudle_num == 5:
			path = str(input("请输入需要检查的目录(eg:/):"))
			file_function_check(path)
		elif moudle_num == 6:
			path = str(input("请输入需要waf的最高层目录(eg:/var/www/html/):"))
			loading_Waf(path)
		elif moudle_num == 7:
			break

# if __name__ == "__main__":   #如果想要单独使用这个防御模块可以直接把这一段代码注释去掉，直接传到服务器运行即可！
# 	defense()