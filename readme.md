- python gdal安装
```sh
# 下载合适的whl文件, .whl重命名为.zip可解压查看其中的文件
# 是已经编译过的gdal, 可以直接使用
https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal

# gdal版本3.0.1, 适用python 3.7 64位版本
pip install GDAL‑3.0.1‑cp37‑cp37m‑win_amd64.whl

# 查看是否安装成功
pip list | grep -i gdal

# 从pypi仓库安装, 需要安装"Microsoft Visual C++ Build Tools"
#  https://visualstudio.microsoft.com/downloads/
pip install gdal

# pypi仓库中库实际的地址
https://files.pythonhosted.org
```

- 入门教程: http://pcjericks.github.io/py-gdalogr-cookbook/index.html

- API参考：https://gdal.org/python
