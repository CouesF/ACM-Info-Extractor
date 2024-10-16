
快速阅读一个期刊或者会议的所有标题与摘要，有助于拓宽知识面，打开思路，快速找到相关研究，找到自己研究的定位。本文介绍了一个 **ACM 论文摘要数据下载方法**，可以快速下载 ACM Digital Library（后面简称ACM） 某一次会议或者某一期期刊的全部摘要信息至表格中，以便于后续的处理与分析。

## 流程概要
1. 访问 ACM 某次会议网站，比如 [UIST 2024](https://dl.acm.org/doi/proceedings/10.1145/3654777?tocHeading=heading20)
2. 网站上论文列表中点击 `复选框 Select All` 后点击 ` Export Citations ` 
3. 下载成 BibTeX 文件
4. 使用 [Python 脚本]( https://github.com/CouesF/ACM-Info-Extractor/blob/main/ACM_Info_Extractor.py )转换 BibTeX 至表格

## 详细流程

### 1. 访问某次会议或者期刊网站比如 [UIST 2024](https://dl.acm.org/doi/proceedings/10.1145/3654777?tocHeading=heading20)
网站上论文列表中点击 `复选框 Select All` 后点击 ` Export Citations ` 
点击下载按钮，下载成 BibTeX 文件。

### 2. 使用 Python 脚本转换为表格
1. 新建项目文件夹，并下载[ python 文件]( https://github.com/CouesF/ACM-Info-Extractor/blob/main/ACM_Info_Extractor.py )至文件夹
2. 修改 Python 代码中的 input_file 为下载的 BibTex 路径
3. 运行 Python 脚本即可获得表格
