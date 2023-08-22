# 前言
## 欢迎关注微信公众号：朱厌安全团队   感谢支持！
![Uploading 公众号.jpg…]()

### 一个面向AWD竞赛的工具，目前BUG和待优化点可能会较多，请谅解！！！
欢迎师傅们提出本工具宝贵建议，如有BUG欢迎师傅们向我们反馈，我们会第一时间关注！
### 工具也会持续维持，后面会更新新模块，敬请期待！

# 工具介绍
FUCK_AWD工具cmd运行命令：python fuck_awd_main.py  即可

如果CMD颜色乱码可以解压 ansi189-bin.zip 运行对应电脑兼容的版本 cmd命令ansicon.exe -i

工具攻击模块原理是以马上马，所以使用时要确认好场景！

利用前提条件：目标服务器没有过滤system()函数、有写入权限、目标为PHP网站

攻击模块：工具目前支持单一目标，批量目标攻击、批量执行命令、预设置三种类型后门木马提供选择(一句话/不死马/蠕虫马)，执行完毕批量保存执行结果、非自定义/自定义后门存活监测等。

防御模块：支持目录树生成、文件一键备份、文件监控、PHP文件数目检测、PHP危险函数检测、一键PHP文件上WAF等。
# 工具效果

![图片](https://github.com/AQF0R/FUCK_AWD_TOOLS/assets/120232326/45d8f3c6-fd49-4762-a3d9-f50d2acb72c1)
![图片](https://github.com/AQF0R/FUCK_AWD_TOOLS/assets/120232326/a31e5939-b471-423f-9283-7ba5e311fe12)
![图片](https://github.com/AQF0R/FUCK_AWD_TOOLS/assets/120232326/c3bd87db-e46d-44fb-b243-8296509d1768)
![图片](https://github.com/AQF0R/FUCK_AWD_TOOLS/assets/120232326/5b895f1f-1bb2-49a5-9a4c-db31917de88f)
![图片](https://github.com/AQF0R/FUCK_AWD_TOOLS/assets/120232326/0c175494-5e27-47e9-ae32-355dcf38f6b1)
![图片](https://github.com/AQF0R/FUCK_AWD_TOOLS/assets/120232326/b0f95d57-26ba-49af-a76a-b2d687f66761)



## 拓展知识
内存马查杀：
1.ps auxww|grep shell.php 找到pid后杀掉进程就可以，你删掉脚本是起不了作用的，因为php执行的时候已经把脚本读进去解释成opcode运行了
2.重启php等web服务
3.用一个ignore_user_abort(true)脚本，一直竞争写入（断断续续）。usleep要低于对方不死马设置的值。
4.创建一个和不死马生成的马一样名字的文件夹。

修改curl：
alias curl='echo fuckoff'  较低权限
chmod -x curl  较高权限
/usr/bin  curl路径

apache日志路径：
/var/log/apache2/
/usr/local/apache2/logs
