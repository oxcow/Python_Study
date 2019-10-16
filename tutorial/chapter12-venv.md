
# 12. 虚拟环境和包

[link](https://docs.python.org/zh-cn/3.7/tutorial/venv.html)


## 12.2. 创建虚拟环境

用于创建和管理虚拟环境的模块称为 venv。venv 通常会安装你可用的最新版本的 Python

	python3 -m venv tutorial-env


create project named 'Python_ENV_Test'

	cd Python_ENV_Test
	python3 -m venv python_env
    source python_env/bin/activate


使用 `python` 进入项目的python env后可，可用 `pip` 命令管理当前项目的包。


## 12.3. 使用pip管理包

安装包

	pip install <Package_Name>
    pip install <Package_Name>==<Version>
    pip install -r <File_Name>

Example:

	pip install requests
	or
	pip install requests==2.6.0

升级已安装的包

	pip install --upgrade <Package_Name>

删除包

	pip uninstall <Package_Name> <Package_Name> ...

展示包信息

	pip show <Package_Name>

展示当前环境中安装的所有软件包

	pip list

安装包列表生成

	pip freeze > <File_Name>

该生成符合 `pip install -r` 期望格式。

Example：

	pip freeze > requirements.txt
	pip install -r requirements.txt

可以将 requirements.txt 提交给版本控制并作为应用程序的一部分提供。然后用户可以使用 install -r 安装所有必需的包