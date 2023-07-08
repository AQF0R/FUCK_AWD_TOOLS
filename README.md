欢迎关注微信公众号：朱厌安全团队

工具目前BUG和待优化点可能会较多，请谅解！！！
欢迎师傅们提出本工具宝贵建议，如有BUG欢迎师傅们向我们反馈，我们会第一时间关注！

FUCK_AWD工具cmd运行命令：python fuck_awd_main.py  即可

如果CMD乱码可以解压 ansi189-bin.zip 运行对应电脑兼容的版本 cmd命令ansicon.exe -i

内存马查杀：
1.ps auxww|grep shell.php 找到pid后杀掉进程就可以，你删掉脚本是起不了作用的，因为php执行的时候已经把脚本读进去解释成opcode运行了

2.重启php等web服务

3.用一个ignore_user_abort(true)脚本，一直竞争写入（断断续续）。usleep要低于对方不死马设置的值。

4.创建一个和不死马生成的马一样名字的文件夹。

修改curl：
alias curl='echo fuckoff'  较低权限
chmod -x curl  较高权限
/usr/bin  curl路径

apache日志路径
/var/log/apache2/
/usr/local/apache2/logs