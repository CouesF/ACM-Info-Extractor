import pandas as pd
import re

input_file = 'UIST2024.bib'  # 替换为你的文本文件路径
output_file = 'UIST2024_PaperList.xlsx'  # 输出Excel文件的路径

# 定义一个函数来读取文本文件并解析数据
def parse_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # 使用正则表达式匹配文章的每个字段
    pattern = re.compile(r'@inproceedings{(.*?),\s*author = {(.*?)},\s*title = {(.*?)},\s*year = {(.*?)},\s*isbn = {(.*?)},\s*publisher = {(.*?)},\s*address = {(.*?)},\s*url = {(.*?)},\s*doi = {(.*?)},\s*abstract = {(.*?)},\s*booktitle = {(.*?)},\s*articleno = {(.*?)},\s*numpages = {(.*?)},\s*keywords = {(.*?)},\s*location = {(.*?)},\s*series = {(.*?)}\s*}')

    matches = pattern.findall(text)

    # 创建一个DataFrame来存储匹配的数据
    df = pd.DataFrame(matches, columns=['ID', 'Author', 'Title', 'Year', 'ISBN', 'Publisher', 'Address', 'URL', 'DOI', 'Abstract', 'Booktitle', 'Articleno', 'Numpages', 'Keywords', 'Location', 'Series'])

    return df

# 定义主函数来执行所有步骤
def main():
    # 解析文本文件并转换为DataFrame
    df = parse_text_file(input_file)

    # 将DataFrame写入Excel文件
    df.to_excel(output_file, index=False, engine='openpyxl')

    print(f'Data has been successfully written to {output_file}')

# 执行主函数
if __name__ == "__main__":
    main()
