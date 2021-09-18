# 数据集扩充

[中文(zh-cn)](https://github.com/doubleZ0108/Data-Augmentation/blob/master/README.md) | [English(en)](https://github.com/doubleZ0108/Data-Augmentation/blob/master/README_en.md)

通用目标检测深度学习数据集扩充方法(尤其针对Yolo)

* [具体实现](#具体实现)
* [如何运行](#如何运行)
* [开发环境](#开发环境)
* [关于作者](#关于作者)

------

## 具体实现

[数据集扩充方法详细说明](https://github.com/doubleZ0108/Data-Augmentation/blob/master/doc/data_augmentation_detailed.md)

- 图像强度变换
  - 亮度变化： [lightness](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/lightness.py)   [darkness](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/darkness.py)
  - 对比度变化：[contrast](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/contrast.py)
- 图像滤波
  - 锐化：[sharpen](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/sharpen.py)
  - 高斯模糊：[blur](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/blur.py)
- 透视变换
  - 镜像翻转：[flip](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/flip.py)
  - 图像裁剪：[crop](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/crop.py)
  - 图像拉伸：[deform](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/deform.py)
  - 镜头畸变：[distortion](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/distortion.py)
- 注入噪声
  - 椒盐噪声：[noise](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/noise.py)
  - 渐晕：[vignetting](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/vignetting.py)
- 其他
  - 随机抠除：[cutout](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/cutout.py)

> 按从左到右，从上到下顺序排列

<img src="https://doublez-site-bed.oss-cn-shanghai.aliyuncs.com/img/20210918215930.png" alt="image.png" width="67%;" align="center" />

<br/>

## 如何运行

- 安装所需依赖

  ```bash
  pip install -r requirements.txt
  ```

- 将原始图片和[标注数据](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/doc/Study-Notes/labelImg工具.md)放到`data/`中

- 运行

  - `python main.py` 生成所有数据在`data/`文件夹下
  - 执行对应`.py`文件生成指定扩充图像数据

- 使用

  ```python
  os.chdir(dirname)
  (name, appidx) = os.path.splitext(filename)
  img = np.array(Image.open(filename))  # Image读入的图片形式
  
  somealgo_img = somealgo(np.copy(img))	# 复制一份传入扩充算法
  somealgo_img.save(name + "_somealgo" + appidx)	# 将扩充图像写入本地
  saveSomeAlgoLabel(name) # 自动生成对应的标注(部分算法需要手动标注)
  ```

<br/>

## 开发环境

- **操作系统**: macOS Catalina 10.15.5
- **开发语言**: python 3.7.4
- **主要依赖**: numpy | cv2 | PIL | shutil

<br/>

## 关于作者

|     姓名👤     |                   张喆 \| doubleZ                   |
| :-----------: | :-------------------------------------------------: |
|   **学校🏫**   |                      同济大学                       |
| **联系方式✉️** | [dbzdbz@tongji.edu.cn](mailto:dbzdbz@tongji.edu.cn) |

