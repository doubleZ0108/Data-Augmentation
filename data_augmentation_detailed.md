# 数据集扩充方法详细说明

   * [数据集扩充方法详细说明](#数据集扩充方法详细说明)
      * [图像强度变换](#图像强度变换)
         * [亮度变化](#亮度变化)
         * [对比度变化](#对比度变化)
      * [图像滤波](#图像滤波)
         * [锐化](#锐化)
         * [高斯模糊](#高斯模糊)
      * [透视变换](#透视变换)
         * [镜像翻转](#镜像翻转)
         * [图像裁剪](#图像裁剪)
         * [图像拉伸](#图像拉伸)
         * [镜头畸变](#镜头畸变)
      * [注入噪声](#注入噪声)
         * [椒盐噪声](#椒盐噪声)
         * [渐晕](#渐晕)
      * [其他](#其他)
         * [随机抠除](#随机抠除)

------

**原图**

<img src="https://upload-images.jianshu.io/upload_images/12014150-68b3a00fdc229303.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo.jpg" width="50%;" />

## 图像强度变换

### 亮度变化

[lightness](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/lightness.py)

图像整体加上一个随机偏差，或整体进行尺度的放缩

- **亮度增强**

  <img src="https://upload-images.jianshu.io/upload_images/12014150-52ddaafbe5baeb46.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_brightness.jpg" width="50%;" />

- **亮度减弱**

  <img src="https://upload-images.jianshu.io/upload_images/12014150-52fb0b2aa553d1f5.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_darkness.jpg" width="50%;" />

```python
brightness = 1 + np.random.randint(1, 9) / 10
brightness_img = img.point(lambda p: p * brightness)
```

> 不影响label的位置

### 对比度变化

[contrast](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/contrast.py)

扩展图像灰度级动态范围，对两极的像素进行压缩，对中间范围的像素进行扩展

```python
range_contrast=(-50, 50)
contrast = np.random.randint(*range_contrast)
contrast_img = img.point(lambda p: p * (contrast / 127 + 1) - contrast)
```

> 不影响label的位置

<img src="https://upload-images.jianshu.io/upload_images/12014150-28d8278dee909f49.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_contrast.jpg" width="50%;" />

<br/>

## 图像滤波

### 锐化

[sharpen](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/sharpen.py)

增强图像边缘信息

```python
identity = np.array([[0, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]])
sharpen = np.array([[ 0, -1,  0],
                    [-1,  4, -1],
                    [ 0, -1,  0]]) / 4
max_center = 4
sharp = sharpen * np.random.random() * max_center
kernel = identity + sharp
sharpen_img = cv2.filter2D(img, -1, kernel)
```

> 不影响label的位置

<img src="https://upload-images.jianshu.io/upload_images/12014150-1263dc2e13f5d671.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_sharpen.jpg" width="50%;" />

### 高斯模糊

[blur](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/blur.py)

图像平滑

```python
kernel_size = (7, 7)
blur_img = cv2.GaussianBlur(img,kernel_size,0)
```

> 不影响label的位置

<img src="https://upload-images.jianshu.io/upload_images/12014150-58bca6cb92d4d542.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_blur.jpg" width="50%;" />

<br/>

## 透视变换

### 镜像翻转

[flip](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/flip.py)

使图像沿长轴进行翻转

```python
flip_img = cv2.flip(cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR), 1)
```

> 第一个位置的参数 pos = 1 - pos，其他信息不变，可以采用脚本自动生成
>
> ```python
> with open(name + "_flip.txt", "w") as outfile:
>   with open(name + ".txt", "r") as infile:
>     for line in infile.readlines():
>       words = line.split(" ")
>       horizontal_coord = float(words[1])
>       outfile.write(words[0] + " " + str(format(1-horizontal_coord, ".6f")) + " " + words[2] + " " + words[3] + " " + words[4])
> ```

<img src="https://upload-images.jianshu.io/upload_images/12014150-0336d65402d15237.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_flip.jpg" width="50%;" />

### 图像裁剪

[crop](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/crop.py)

裁剪原图80%大小的中心图像，并进行随机移动

```python
kernel_size = list(map(lambda x: int(x*0.8), size))
shift_min, shift_max = -50, 50
shift_size = [np.random.randint(shift_min, shift_max), np.random.randint(shift_min, shift_max)]

crop_img = img[
  (size[0]-kernel_size[0])//2+shift_size[0]:(size[0]-kernel_size[0])//2+kernel_size[0]+shift_size[0],
  (size[1]-kernel_size[1])//2+shift_size[1]:(size[1]-kernel_size[1])//2+kernel_size[1]+shift_size[1]
]
```

> 可能将目标对象裁减掉，因此采用手工重新标注

<img src="https://upload-images.jianshu.io/upload_images/12014150-346ec7617782e807.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_crop.jpg" width="50%;" />

### 图像拉伸

[deform](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/deform.py)

拉伸成长宽为原始宽的正方形图像

```python
deform_img = img.resize((int(w), int(w)))
```

> 原图中比例信息改变，最好重新手工标注

<img src="https://upload-images.jianshu.io/upload_images/12014150-ed8fd4ef139b7e75.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_deform.jpg" width="50%;" />

### 镜头畸变

[distortion](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/distortion.py)

对图像进行透视变化，模拟鱼眼镜头的镜头畸变

通过播放径向系数k1，k2，k3和切向系数p1，p2实现

```python
d_coef= np.array((0.15, 0.15, 0.1, 0.1, 0.05))
# get the height and the width of the image
h, w = img.shape[:2]
# compute its diagonal
f = (h ** 2 + w ** 2) ** 0.5
# set the image projective to carrtesian dimension
K = np.array([[f, 0, w / 2],
              [0, f, h / 2],
              [0, 0,   1  ]])
d_coef = d_coef * np.random.random(5) # value
d_coef = d_coef * (2 * (np.random.random(5) < 0.5) - 1) # sign
# Generate new camera matrix from parameters
M, _ = cv2.getOptimalNewCameraMatrix(K, d_coef, (w, h), 0)
# Generate look-up tables for remapping the camera image
remap = cv2.initUndistortRectifyMap(K, d_coef, None, M, (w, h), 5)
# Remap the original image to a new image
distortion_img = cv2.remap(img, *remap, cv2.INTER_LINEAR)
```

> 最好重新手工标注

<img src="https://upload-images.jianshu.io/upload_images/12014150-c33b16682ef46ebf.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_distortion.jpg" width="50%;" />

<br/>

## 注入噪声

### 椒盐噪声

[noise](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/noise.py)

在图像中随机添加白/黑像素

```python
for i in range(5000):
  x = np.random.randint(0,rows)
  y = np.random.randint(0,cols)
  noise_img[x,y,:] = 255
  noise_img.flags.writeable = True
```

> 不影响label的位置

<img src="https://upload-images.jianshu.io/upload_images/12014150-0264d134d8ce1211.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_noise.jpg" width="50%;" />

### 渐晕

[vignetting](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/vignetting.py)

对图像添加一个圆范围内的噪声模拟光晕

```python
ratio_min_dist=0.2
range_vignette=np.array((0.2, 0.8))
random_sign=False

h, w = img.shape[:2]
min_dist = np.array([h, w]) / 2 * np.random.random() * ratio_min_dist

# create matrix of distance from the center on the two axis
x, y = np.meshgrid(np.linspace(-w/2, w/2, w), np.linspace(-h/2, h/2, h))
x, y = np.abs(x), np.abs(y)
# create the vignette mask on the two axis
x = (x - min_dist[0]) / (np.max(x) - min_dist[0])
x = np.clip(x, 0, 1)
y = (y - min_dist[1]) / (np.max(y) - min_dist[1])
y = np.clip(y, 0, 1)
# then get a random intensity of the vignette
vignette = (x + y) / 2 * np.random.uniform(*range_vignette)
vignette = np.tile(vignette[..., None], [1, 1, 3])
sign = 2 * (np.random.random() < 0.5) * (random_sign) - 1
vignetting_img = img * (1 + sign * vignette)
```

> 不影响label的位置

<img src="https://upload-images.jianshu.io/upload_images/12014150-3e8b67995db963e3.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_vignetting.jpg" width="50%;" />

<br/>

## 其他

### 随机抠除

[cutout](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/cutout.py)

随机抠出四个位置，并用黑色/彩色矩形填充

```python
channel_wise = False
max_crop = 4
replacement=0

size = np.array(img.shape[:2])
mini, maxi = min_size_ratio * size, max_size_ratio * size
cutout_img = img
for _ in range(max_crop):
  # random size
  h = np.random.randint(mini[0], maxi[0])
  w = np.random.randint(mini[1], maxi[1])
  # random place
  shift_h = np.random.randint(0, size[0] - h)
  shift_w = np.random.randint(0, size[1] - w)

  if channel_wise:
    c = np.random.randint(0, img.shape[-1])
    cutout_img[shift_h:shift_h+h, shift_w:shift_w+w, c] = replacement
    else:
      cutout_img[shift_h:shift_h+h, shift_w:shift_w+w] = replacement
```

> 不影响label的位置

<img src="https://upload-images.jianshu.io/upload_images/12014150-ed2337394e6352b4.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="demo_cutout.jpg" width="50%;" />

<br/>