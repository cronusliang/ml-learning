##Anaconda 使用

#### 一 管理包

1 更新所有的包

​        `conda upgrade — all`

2 搜索包 

​	`conda search  search_term（模糊名称） 进行搜索 `

### 二 管理环境

1 创建环境 

​     `Conda create -n env_name list of packages`  在这里，-n env_name 设置环境的名称（-n是指名称），list of packages 是要安装在环境中的包的列表。如

 ![](http://images.cronusliang.me/ML/dataAnalysis/create_envi.png>)

​     

2 进入环境

在osx/linux上使用source activate my_env 进入环境。在Windows上，使用activate my_env

3 保存环境

`conda env export > environment.yaml`    将包保存为YAML 文件

4 创建环境

`conda env create -f environment.yaml` 创建环境

5 列出环境

`conda env list ` 列出你创建的所有环境

6 删除环境

Conda env remove -n env_name 删除指定的环境














