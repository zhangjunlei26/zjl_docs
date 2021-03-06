# Create Note
点击中栏**+ 新建**按钮来新建笔记。或者键入**⌘ n** ，即同时按住Command键和字母N键。
# Edit Note
双击中栏列表中的笔记名称以打开关联的编辑器来编辑笔记。或者使用h/l移动焦点到中栏（具体表现为中栏选中项字体颜色为白色，Marboo底部状态栏显示的是编辑器图标），然后键入快捷键 **o**
# Preview Note
编辑器中保存文件后，右栏会立刻更新生成的HTML页面。
# Create Folder
双击左栏文件夹 或 使用h/l移动焦点到左栏（具体体现是左栏选中项字体颜色为白色，Marboo状态栏显示Finder或Terminal图标），然后键入**o**，在打开的的Finder或Terminal中新建文件夹即可。
# Preview Note in Web Browser
使用h/l移动焦点到右栏（具体表现为Marboo底部状态栏显示的是浏览器图标）然后键入 **o**

# Custom Folder Browser
打开偏好设置，点击Config File中的文件路径，会打开配置文件*marboo_config.json*，
找到如下内容：

```json
    "comment": "设置目录浏览器。可以设置Default(或者写Finder也可，都代表用Finder打开)或Terminal等",
    "folder_viewer": "Finder",
    "1.folder_viewer": "Default",
    "2.folder_viewer": "Terminal",
```
在想要的目录浏览器那一行中，删除掉key中的序号，同时把之前的key改掉。比如希望用Terminal来打开，就修改为：

```json
    "comment": "设置目录浏览器。可以设置Default(或者写Finder也可，都代表用Finder打开)或Terminal等",
    "0.folder_viewer": "Finder",
    "1.folder_viewer": "Default",
    "folder_viewer": "Terminal",
```

保存即生效。

**Attaction：**

marboo_config.json中的引号一定要使用英文引号才可以。TextEdit编辑器有Bug，导致在英文输入法状态下输入的引号仍为中文引号，使用其他编辑器或复制引号过来即可work around。

# Custom File Editor
## 最简单的方式：打开偏好设置，可以设置编辑器

或者在上述 *marboo_config.json* 中找到如下内容：

```json
    "comment": "设置文件编辑器。Default(或者写Finder也可)代表Finder中关联的编辑器，也可以设置已安装的编辑器如 Emacs, MacVim, TextMate, Mou等",
    "file_editor": "Default",
    "0.file_editor": "Do as Finder do",
    "1.file_editor": "Finder",
    "2.file_editor": "Emacs",
    "3.file_editor": "MacVim",
    "4.file_editor": "Atom",
    "5.file_editor": "Mou",
    "6.file_editor": "Sublime Text",
    "7.file_editor": "TextMate",
```

在想要的编辑器那一行中，删除掉key中的序号，同时把之前的key改掉。比如希望用Emacs来打开，就修改为：

```json
    "comment": "设置文件编辑器。Default(或者写Finder也可)代表Finder中关联的编辑器，也可以设置已安装的编辑器如 Emacs, MacVim, TextMate, Mou等",
    "0.file_editor": "Default",
    "0.file_editor": "Do as Finder do",
    "1.file_editor": "Finder",
    "file_editor": "Emacs",
    "3.file_editor": "MacVim",
    "4.file_editor": "Atom",
    "5.file_editor": "Mou",
    "6.file_editor": "Sublime Text",
    "7.file_editor": "TextMate",
```

保存即生效。

	
# Custom Web Browser
在上述 *marboo_config.json* 中找到如下内容：

```json
    "comment": "设置网页浏览器。Default代表默认浏览器，也可以设置已安装的浏览器如Google Chrome, Firefox等",
    "web_browser": "Default",
    "1.web_browser": "Google Chrome",
    "2.web_browser": "Firefox",
    "3.web_browser": "Safari",
    "4.web_browser": "QQBrowser",
```

在想要的浏览器那一行中，删除掉key中的序号，同时把之前的key改掉。比如希望用Firefox来打开，就修改为：

```json
    "comment": "设置网页浏览器。Default代表默认浏览器，也可以设置已安装的浏览器如Google Chrome, Firefox等",
    "0.web_browser": "Default",
    "1.web_browser": "Google Chrome",
    "web_browser": "Firefox",
    "3.web_browser": "Safari",
    "4.web_browser": "QQBrowser",
```

保存即生效。

# More Help

Need more help？Please contact amoblin ：

| Contact | Way |
|-----+------|
| Email / GTalk | <amoblin@gmail.com> |
| Marboo QQ Group | [273540092](qq://273540092) |
| amoblin's QQ | [576147360](qq://576147360) |
| Sina Weibo | <http://weibo.com/amoblin> |
| Twitter | <http://twitter.com/amoblin> |
