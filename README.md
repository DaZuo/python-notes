这个 repo 用来记录我学习 Python 的笔记，主要是一些阅读笔记，不是总结，但是有心得体会

- [Installation](#installation)
- [基础理论](#%E5%9F%BA%E7%A1%80%E7%90%86%E8%AE%BA)
- [练手项目](#%E7%BB%83%E6%89%8B%E9%A1%B9%E7%9B%AE)

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

## 基础理论

目前为止所有的理论学习来源都是[官方文档](https://www.python.org/doc/)

- [the-python-tutorial](./the-python-tutorial/README.md)

## 练手项目

- [实验楼练手项目集合](./exercises-from-shiyanlou.com/README.md)