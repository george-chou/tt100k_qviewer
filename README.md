# tt100k_qviewer
A browser for TT100K training dataset developed in Qt

[![license](https://img.shields.io/github/license/george-chou/tt100k_qviewer.svg)](https://github.com/george-chou/tt100k_qviewer/blob/master/LICENSE)
[![Python application](https://github.com/george-chou/tt100k_qviewer/workflows/Python%20application/badge.svg)](https://github.com/george-chou/tt100k_qviewer/actions)

## Dataset download

First we need to download and extract the dataset and code:

<div align=center><b>Table 1: Source download</b>

| Resource type | Download URL |
| :---: | :--- |
| Code | http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/data.zip |
| Training dataset | http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/data.zip |
| Test dataset 1 | http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/nosign_1.zip |
| Test dataset 2 | http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/nosign_2.zip |
| Test dataset 3 | http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/nosign_3.zip |
| Test dataset 4 | http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/nosign_4.zip |
| Test dataset 5 | http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/nosign_5.zip |

</div>

If you want to download them all, please make sure your disk have 100G free space at least. But here we only need to download the training dataset, which only takes 18G space. After downloading and extraction, put "data" directory into the code path.

## Run

Open `main.py` with VSCode and run the python script. If your computer has all the required plug-ins and environment installed, the following interface should pop up:

<div align=center>
<img width="605" src="https://george-chou.github.io/covers/qtt100k/f1.PNG"/><br>
<b>Figure 1: TT100K QViewer UI</b>
</div>

## TT100K Tutorial

For more information about the usage of TT100K, please refer to below website:

http://cg.cs.tsinghua.edu.cn/traffic-sign/tutorial.html#Tsinghua-Tencent-100K-Tutorial