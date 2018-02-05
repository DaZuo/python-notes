# Python Notes

这个 repo 用来记录我学习 Python 的笔记，主要是一些阅读笔记，不是总结，但是有心得体会

## Installation

当前使用的 Python 解释器版本号是 3.6.4rc1，安装如下

``` bash
$ pyenv install 3.6.4rc1
$ pyenv local 3.6.4rc1
```

然后创建一个 `.env` 的虚拟环境，并激活

``` bash
$ python -m venv .env
$ source .env/bin/activate
```

退出这个虚拟环境，可以执行以下指令

``` bash
$ deactivate
```

使用 `pip` 来安装依赖

``` bash
$ pip install -r requirements.txt
```

Done!

等等，编辑器使用的是 [VS Code](https://code.visualstudio.com/)

## Step By Step

1. 第一阶段的学习
    - [the-python-tutorial](./the-python-tutorial/README.md)