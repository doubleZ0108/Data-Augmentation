# Data Augmentation

[中文(zh-cn)](https://github.com/doubleZ0108/Data-Augmentation/blob/master/README.md) | [English(en)](https://github.com/doubleZ0108/Data-Augmentation/blob/master/README_en.md)

General Data Augmentation Algorithms for Object Detection(esp. Yolo)

   * [Data Augmentation](#data-augmentation)
      * [Implementation](#implementation)
      * [How to Run](#how-to-run)
      * [Dev Environment](#dev-environment)
      * [About the Author](#about-the-author)

------

## Implementation

[Detailed description of data augmentation methods](https://github.com/doubleZ0108/Data-Augmentation/blob/master/doc/data_augmentation_detailed_en.md)

- Intensity Transform
  - Luminance Fluctuation： [lightness](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/lightness.py)   [darkness](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/darkness.py)
  - Contrast Transform：[contrast](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/contrast.py)
- Filtering
  - Image Sharpening：[sharpen](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/sharpen.py)
  - Gaussian Blur：[blur](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/blur.py)
- Perspective Transform
  - Mirror Flip：[flip](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/flip.py)
  - Image Clipping：[crop](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/crop.py)
  - Image Stretching：[deform](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/deform.py)
  - Lens Distortion：[distortion](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/distortion.py)
- Injected Noise
  - Salt and Pepper Noise：[noise](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/noise.py)
  - Vignetting：[vignetting](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/vignetting.py)
- Others
  - Random Cutout：[cutout](https://github.com/doubleZ0108/Data-Augmentation/blob/master/src/cutout.py)

> from left to right, top to bottom

<img src="https://upload-images.jianshu.io/upload_images/12014150-38d9933ec9b9e736.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" width="67%;" align="center" />

<br/>

## How to Run

- install required dependencies

  ```bash
  pip install -r requirements.txt
  ```

- place the original image and [labeled data](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/doc/Study-Notes/labelImg工具.md) in `data/`

- for run

  - `python main.py` to generate all augmentated images under `data/`
  - run `.py` to generate the specified augmentated image

- for usage

  ```python
  os.chdir(dirname)
  (name, appidx) = os.path.splitext(filename)
  img = np.array(Image.open(filename))  # Image format image input
  
  somealgo_img = somealgo(np.copy(img))	# copy to the concrete algorithm
  somealgo_img.save(name + "_somealgo" + appidx)	# store the images locally
  saveSomeAlgoLabel(name) # auto generate corresponding annotation(some algos need manual annotation)
  ```

<br/>

## Dev Environment

- **OS**: macOS Catalina 10.15.5
- **Language**: python 3.7.4
- **Dependencies**: numpy | cv2 | PIL | shutil

<br/>

## About the Author

|      Name👤      |                Zhe ZHANG \| doubleZ                 |
| :-------------: | :-------------------------------------------------: |
| **University🏫** |                    Tongji Univ.                     |
|   **Email✉️**    | [dbzdbz@tongji.edu.cn](mailto:dbzdbz@tongji.edu.cn) |

