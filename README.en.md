# ACM-Info-Extractor: How to Quickly Download Abstracts from ACM Conferences or Journals

Reading through the titles and abstracts of journals or conferences can help broaden your knowledge, spark ideas, and quickly identify relevant research. It can also assist in finding your research position. This article introduces a **method to download abstracts from the ACM Digital Library** for a specific conference or journal issue. The abstracts can be converted into a spreadsheet for further processing and analysis.

## Overview of the Process
1. Visit an ACM conference page, such as [UIST 2024](https://dl.acm.org/doi/proceedings/10.1145/3654777?tocHeading=heading20).
2. On the paper list page, click the **"Select All" checkbox** and then click **"Export Citations"**.
3. Download the file as a **BibTeX** format.
4. Use a [Python script](https://github.com/CouesF/ACM-Info-Extractor/blob/main/ACM_Info_Extractor.py) to convert the BibTeX file into a spreadsheet.

## Detailed Steps

### 1. Visit the Conference or Journal Website
- Go to the conference or journal page, for example: [UIST 2024](https://dl.acm.org/doi/proceedings/10.1145/3654777?tocHeading=heading20).
- In the list of papers, click the **"Select All" checkbox** and then click **"Export Citations"**.
- Choose the **BibTeX** format and download the file.

### 2. Convert the BibTeX File to a Spreadsheet
1. Create a new project folder and download the [Python script](https://github.com/CouesF/ACM-Info-Extractor/blob/main/ACM_Info_Extractor.py) into the folder.
2. Modify the `input_file` variable in the Python script to the path of the downloaded BibTeX file.
3. Run the Python script to generate the spreadsheet with the abstracts.
