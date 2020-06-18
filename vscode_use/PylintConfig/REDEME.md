# 1.生成pylint配置文件

`python3 -m pylint --generate-rcfile > pylint.conf`


# 2. pylint配置外部路径

`pylint.conf`文件中init-hook添加如下：

`init-hook="import sys;sys.path.append("ExtraPath");"`


# 3. vscode配置使用pylint.conf文件

`settings.json`添加下列配置：
```json
    "python.linting.pylintArgs": [
        "--rcfile=PylintConfig/pylint.conf"
    ]
```
