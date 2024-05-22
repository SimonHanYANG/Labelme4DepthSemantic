# Labelme 语义分割文档

[toc]

## 1. 环境配置与安装

### 1.1 创建 conda 虚拟环境

```cmd
conda create -n labelme_env python=3.8
```
创建后进入新环境
```cmd
conda activate labelme_env
```

### 1.2 安装 Labelme
```cmd
pip install labelme

清华源: -i https://pypi.tuna.tsinghua.edu.cn/simple

```

## 2. Labelme 使用

### 2.1 文件路径

```cmd
├── img_data/: 存放所要标注的所有图片
├── data_annotated/: 存放后续标注好的所有json文件
└── label.txt: 所有类别信息
```

### 2.2 创建 label 标签文件

```cmd
vim label.txt
```

```cmd
# in label.txt file

__ignore__
_background_
2.0
1.5
1.0
0.5
0.0
-0.5
-1.0
-1.5
-2.0
```

### 2.3 启动 Labelme

```cmd
cd root_path

labelme --labels label.txt
```

![fig1](/ref/screen.png)

### 2.4 打开文件夹

点击界面左侧的`Open`或`OpenDir`打开文件或文件夹，这里就选择`img_data/`（该文件夹中存储了所有后续需要标注的图片）

![fig2](/ref/open_window.png)

### 2.5 设置保存结果路径

- 先点击左上角`File`，`Change Output Dir`设置标注结果的保存目录，这里就设置成前面说好的data_annotated。
- 建议将`Save With Image Data`取消掉，默认是选中的。如果选中，会在保存的标注结果中将图像数据也保存在`.json`文件中。

![fig3](/ref/change_output.png)

### 2.6 标注目标

- 首先点击左侧的`CreatePolygons`按钮开始绘制多边形，然后用鼠标标记一个一个点把目标边界给标注出来（鼠标放置在第一个点上，点击一下会自动闭合边界）。标注后会弹出一个选择类别的选择框，选择对应类别即可。

- 如果标注完一个目标后想修改目标边界，可以点击工具左侧的`EditPolygons`按钮，然后选中要修改的目标，拖拉边界点即可进行微调。如果要在边界上新增点，把鼠标放在边界上点击鼠标右键选择`Add Point to Edge`即可新增边界点。如果要删除点，把鼠标放在边界点上点击鼠标右键选择`Remove Selected Point`即可删除边界点。

![fig4](/ref/label.png)

### 2.7 Reference Depth Labels Image

![fig4](/reference.png)

## 3. 格式转换

### 3.1 转换语义分割标签

- 在这个[仓库](https://github.com/labelmeai/labelme/tree/main/examples/semantic_segmentation)中找到 `labelme2voc.py` 脚本，在 `root_path` 下执行便可以得到语义 GT。

```cmd
python labelme2voc.py data_annotated data_dataset_voc --labels label.txt
```
- 其中`data_annotated`是刚刚标注保存的`json`标签文件夹，`data_dataset_voc`是生成`PASCAL VOC`数据的目录。

- 执行后会生成如下目录

![output_contents](/ref/output_contents.png)

> - JPEGImages: 储存原图像
> - SegmentationClassVisualization: 语义分割所需要使用的 GT
> - class_names.txt: 储存语义类别名称

- Original Image
![ori](/ref/0.png)

- Semantic Segmentation GT
![seg](/ref/0_res.jpg)

- Class Names

```txt
_background_
2.0
1.5
1.0
0.5
0.0
-0.5
-1.0
-1.5
-2.0
```
