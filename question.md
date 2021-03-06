# 常见问题解决方案

本文主要介绍一些常见问题的解决方案。

> 持续更新中...\
上次更新：2020-01-15

## 运行时，未产生期望中的结果/产生异常

首先考虑下面的问题：

```text
代码是自己写的还是搬来的？
```

* [搬来的](#搬来的代码出错)
* [自己写的](#自己写的代码出错)

### 搬来的代码出错

1. 检查当前设备的代码运行环境与代码所需要的运行环境是否有任何不同。如有不同，请自行配置成相同或合适的运行环境。常见环境问题：
    1. python2与python3的区别。
        * 最简单的辨识方法：观察代码中print后面是否有圆括号`()`，没有的一定是python2的代码。
        * 如果你正在使用python3，而代码是python2的，并且不愿意为了使用这段代码安装python2，可以参考[这里](https://docs.python.org/zh-cn/3/library/2to3.html)进行代码转换。
        * 如果你正在使用python2，而代码是python3的，请升级到python3。
    2. python交互模式与终端执行的区别。
        * 最简单的辨识方法：看运行时是否有前导的三大于号`>>>`。在默认的情况下，`>>>`是交互模式的提示符。
    3. 依赖模块是否被正确安装。
        1. 注意pycharm内创建的虚拟环境内安装的模块、作为用户应用的python解释器安装的模块、作为系统应用的python解释器安装的模块的区别。
        2. 注意自己安装的模块的版本是否能够与搬来代码的模块兼容。如果不懂怎么看是否兼容，可以尝试将所有依赖的模块全部更新到最新版本，但也存在代码不能向下兼容旧版本代码的模块。
    4. 网络的连通性（有一些脚本的运行可能需要翻墙才能正常进行）。
    5. 操作系统（有一些脚本执行了操作系统的命令，但不同操作系统所用的命令不同）。
    6. 其他任何可能的硬件或软件问题。
2. 如果1没有解决问题，请至少核对自己搬来的代码与原来的代码三次以上，确保没有任何逻辑上的偏差。常见的可能搬错的问题：
    1. 请注意不要遗漏任何其他上下文。最需要注意这一点的是从书上搬的代码。这些代码很可能是分段写的，只有一起用才能正常运作。
    2. 请注意不要遗漏任何必要的空白字符，也不要多加任何不应有的空白字符。多一个缩进或少一个缩进带来的逻辑差别对python脚本而言可能是致命的。
    3. 请注意python是大小写敏感的。
    4. 其他任何可能的代码偏差。
3. 如果经过2以后还是无法解决问题，请仔细阅读代码中可能有的注释，或者可能存在的使用说明，确认自己正确使用了这一段代码。
    * 有些书/教程/博客上的代码只是示例，并不是直接搬来运行就能产生期望的结果（即单纯地运行这段代码可能本来就没有任何可视化的结果）。
4. 如果确认1、2、3都完全没有问题，但仍未解决，则基本可以断定是代码本身的问题，请考虑联系该代码的作者。
    * 如果代码来自于教材，可能是印刷错误。
    * 如果代码来自于技术博客，可以添加评论回复提出你发现的问题。
    * 如果代码来自于GitHub，可以在已有issue中找找有没有相应的解决，或新建一个issue等待作者/其他关注者解答。
    * 其他可能来源，能联系到作者就问本人。
5. 如果你看到了这里还是没解决，只可能是代码本身存在问题，且无法联系到代码的作者。此时可以考虑后文的[自己写的代码出错](#自己写的代码出错)解决方法。

### 自己写的代码出错

根据以下几种常见表现，可以快速排查问题所在。

* [产生异常](#产生异常)
* [无期望输出](#无期望输出)
* [输出与期望不一致](#输出与期望不一致)

#### 产生异常

1. 找到异常的类型与信息。默认情况下，异常在控制台的输出的最重要信息在最后一行。
2. 根据异常的类型和信息可以大致推断问题，其中对问题定位最有帮助的是信息的描述（如果看不懂英文，请使用翻译）。根据异常的调用栈可以定位产生异常的代码位置（脚本的行数）。常见异常及排除方案：
    * SyntaxError 语法错误：脚本不符合python的语法。
        * 请仔细学习python的语法知识。
    * TypeError 类型错误：调用某个函数时传递的参数类型不符合期望。
        * 请检查参数类型是否正确。
    * ValueError 值错误：调用某个函数时传递的参数类型正确但取值不符合期望（超出期望的取值范围）。
        * 请传递合理的参数值。
    * KeyError 键错误：尝试在某个字典中查找一个不存在的键。
        * 请检查键值的正确性。
    * AttributeError 属性错误：尝试访问某对象的一个不存在的属性。
        * 请检查对象的类型，确保其具有该属性。
    * NameError 名称错误：使用了当前上下文未定义的名称。
        * 请检查当前作用域内是否存在该名称。
    * 其他异常详见官方文档：<https://docs.python.org/zh-cn/3/library/exceptions.html>
3. 如果检查代码后认为不应当产生异常，可以通过调试检查脚本的逻辑。
    1. 在合适的位置设置断点。如果不太会选取，可以只在脚本的第一行设置断点。
    2. 以调试模式运行脚本。
    3. 在调试中，慢慢地单步执行代码，并观察变量的变化情况。看是否符合预期。在不符合预期的地方可能存在需要修复的代码问题（bug）。
    * 有关调试代码的具体操作，请查阅所用的代码编辑器（例如IDLE、Pycharm、Visual Studio、Visual Studio Code等）的调试方法。

#### 无期望输出

广义的输出不仅仅是通过print进行的控制台输出，而本文面向的是初学者，因此指的是控制台输出。

1. 请检查是否存在输出的语句。如有则检查输出语句是否会被执行。
    * 函数体内的代码不会在定义的时候被执行。请检查是否存在调用函数的语句。
    * 如果输出语句在if-else语句的语句块内，请检查判断条件是否为永真或永假。

#### 输出与期望不一致

1. 如果输出了空值，例如空列表，空字符串，空字典，0等，请检查脚本的逻辑。
    * 检查方法同产生异常的检查。
        * 常见可能原因：
            1. 重复赋值导致覆盖了引用。
            2. for迭代的迭代器本身没有可以迭代的元素。
            3. 永真/永假的表达式使得修改语句不会被执行，最终得到的是初始的空值。
    * 出现类似问题建议自己检查。这种检查工作能够很好地提高编程能力。
    * 必要时可以问大佬（不建议问太多，问的越多，就越容易产生依赖心理，从而无法自己解决问题并成为大佬）。
2. 如果输出了乱码，请检查编码和解码使用的字符集。
    * 编码和解码所用的字符集不同会导致一些字符显示异常。编码和解码格式一致才能正常显示。
    * 希望显示中文时，请尽可能地统一成`utf-8`。
    * 尽量不要在代码中使用中文字符，哪怕是在字符串和注释中。
    * 以下是可能需要设置编码格式的地方：
        * 被读取文件的编码格式和脚本中使用的解码格式。
        * 脚本的编码格式和运行环境（例如在控制台中执行脚本）的解码格式。
        * 爬虫解析请求获得JSON的解码格式和JSON实际的编码格式。
    * 如果不清楚对一些文件应该使用什么字符集，可以使用模块[`chardet`](https://chardet.readthedocs.io/en/latest/)尝试获取该文件的编码格式。
