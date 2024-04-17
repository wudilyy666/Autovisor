##  Autovisor

智慧树视频课辅助脚本，开启挂机摸鱼时代~

**新学期必备干货, 建议收藏备用 !!**

**项目主页：**[CXRunfree/Autovisor(记得点直接访问)](https://github.com/CXRunfree/Autovisor)

------

#### 2024/4/17 rebuild-3.11.3 更新

**1.新增部分自定义选项(可以在运行中实时修改生效):**

- 支持自定义倍速大小;
- 支持自定义每门课程的刷课时长;

2.调整了课程链接的**填写方式**(更加人性化)

详细配置方式请见下方的**"使用须知".**

------

#### 一、程序介绍:

**项目简介：**

这是一个可无人监督的自动化程序，基于微软的Playwright框架，由Python和JavaScript编写而成；相对于常见的油猴脚本，本程序可有效防止被网页检测。核心原理是使浏览器模拟用户的点击操作。

**程序功能:**

- 可以快速登录
- **自动播放和切换下一集**
- **跳过弹窗和弹出的题目**
- **自动静音、调整1.8倍速和流畅画质**
- **检测视频是否暂停并续播**
- 检测当前学习进度并后台实时更新
- 根据当前时间自动设置背景颜色(白昼/暗夜)
- 加入了定时模拟鼠标滑动功能 (减少被检测到的概率)
- 完成章节时将提示已刷课时长

#### 二、使用须知:

**新版配置方法(version>=3.11)**

1.请确保系统为windows10及以上

- 默认启动Edge(win10及以上自带);
- 请确保Edge或Chrome安装在**系统默认位置**;

2.文件夹内有 **configs.ini文件** (可能没显示 **.ini**后缀名)，请用文本编辑器打开;

3.填写配置文件

根据图中说明填写好配置信息，一定要**保存后**再退出。

**注意：**所有配置项都不加双引号.

<img src="https://img-blog.csdnimg.cn/direct/e25585268bd74322851f110532435dea.png" alt="img" style="zoom: 50%;" />![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)



4.运行**`Autovisor.exe`**，会自动打开浏览器，登录界面的滑块验证请**手动完成**，进入网课界面后就可以自动刷课了 ！

------

**旧版配置方法(version<3.11)**

1.请确保系统为windows10及以上

- 默认启动Edge(win10及以上自带);
- 请确保Edge或Chrome安装在**系统默认位置**;

2.文件夹内有 **account.json文件** (可能没显示 **.json**后缀名)，请用文本编辑器打开;

3.填写配置文件

**`User`**：输入你的 **账户名**；

**`Password`**：输入你的 **密码**；

**`Driver`**：指定启动的 **浏览器**(可选Chrome)；

**`Url`**：输入网课的 **具体网址**，保存后关闭，例如下图所示.

**注意:** 

- 此脚本仅支持**共享课**视频, **网址格式**与需下面一致, 填入时请看仔细。
- 只能使用**英文标点**。

<img src="https://img-blog.csdnimg.cn/direct/b6edaad9b62045e4b5364df24a374fef.png" alt="img" style="zoom: 50%;" />![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

4.运行`Autovisor.exe`，会自动打开浏览器，登录界面的滑块验证请**手动完成**，进入网课界面后就可以自动刷课了 ！

------

#### **三、发行版下载:**

Github: [Releases · CXRunfree/Autovisor (github.com)](https://github.com/CXRunfree/Autovisor/releases)

网盘备用: [[蓝奏云\] Autovisor-for-windows](https://wwk.lanzouj.com/b05evsxif) 密码:492l

这是已经打包好的程序, 若需要**源代码**自行请前往Github项目主页下载.

#### 四、常见问题 :

1.为什么会出现一个命令行黑框?

- 这是程序运行的后台，你可以查看当前运行的状态

2.为什么网页一片空白/无法加载课程界面,一段时间后程序就退出了?

- 大概率你在配置文件里填入的**课程链接有误**;

3.为什么运行程序只出现后台却没出现浏览器界面？

- 只要后台未异常退出就不必担心; 如果出错可能是你的浏览器安装路径有问题

------

**已知Bug:**

- **长时间挂机**有概率弹出人机验证, 如果1.5h内未通过验证, 程序将自动结束进程;
- 若出现其他异常崩溃，请提交issue并附上日志文件log.txt的信息；

如有其他疑问,可以提issue或者在CSDN给作者留言 (!^-^/)

**碎碎念:**

觉得体验还不错? 来给项目发电支持一下吧~!

(其实作者也要吃饭的 ^-^)

<img src="https://img-blog.csdnimg.cn/direct/2d94a77c4bf643c1bff1712461c4f1bf.png" alt="img" style="zoom: 50%;" />![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

**作者的CSDN:** [Runfreeone 欢迎关注~](https://blog.csdn.net/Runfreeone)

**注意：本程序只可用于学习和研究计算机原理(你懂的)**

还等什么? 快开始愉快的刷课吧~ !
