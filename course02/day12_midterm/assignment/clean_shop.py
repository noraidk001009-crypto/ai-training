import csv  #引入csv模块用于读取csv文件
import os  #引入os模块用于操作文件和目录

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  #获取当前文件的目录
INPUT_PATH = os.path.join(BASE_DIR, "messy_shop.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "clean_shop.csv")  #获取clean_shop.csv文件的路径
LOG_PATH = os.path.join(BASE_DIR, "CLEANING_LOG.md")  #获取CLEANING_LOG.md文件的路径

WORD_TO_NUM = {"fifty": "50", "one": "1", "two": "2", "three": "3"}  #定义一个字典用于将单词转换为数字


def clean_number(value):  #将单词转换为数字
    v = value.strip().lower()  #将字符串转换为小写
    return WORD_TO_NUM.get(v, value.strip())  #将单词转换为数字


def main():  #主函数
    with open(INPUT_PATH, newline="") as f:  #读取csv文件 
        rows = list(csv.reader(f))

    header, data = rows[0], rows[1:]
    cleaned = []  #定义一个列表用于存储清洗后的数据
    seen = set()  #定义一个集合用于存储已经处理过的数据
    fixes = []  #定义一个列表用于存储处理过程中的问题   

    for i, row in enumerate(data, start=2):  #遍历数据
        # Fix 5: skip fully blank rows
        if not any(cell.strip() for cell in row):  #如果行中所有单元格都为空，则跳过
            fixes.append(f"Row {i}: entire row was blank, removed.")  #将问题添加到fixes列表中
            continue

        # Fix 3: strip surrounding whitespace from every field
        stripped = [cell.strip() for cell in row]  #将行中所有单元格的空格去掉  
        if stripped != row:
            fixes.append(f"Row {i}: fields had extra whitespace, trimmed.")  #将问题添加到fixes列表中
        row = stripped  #将行中所有单元格的空格去掉  
        item, qty, price, day = row  #将行中所有单元格的空格去掉  

        # Fix 2: convert words to numbers (fifty -> 50)
        new_price = clean_number(price)  #将单词转换为数字  
        if new_price != price:
            fixes.append(f"Row {i}: price was word '{price}', converted to '{new_price}'.")  #将问题添加到fixes列表中
        price = new_price  #将价格转换为数字  

        # Fix 1: drop rows with empty qty
        if qty == "":  #如果数量为空，则跳过
            fixes.append(f"Row {i}: qty was empty, row removed.")  #将问题添加到fixes列表中
            continue

        # Fix 4: drop duplicates
        key = (item, qty, price, day)  #定义一个元组用于存储数据
        if key in seen:
            fixes.append(f"Row {i}: duplicate of existing record ({item},{qty},{price},{day}), removed.")  #将问题添加到fixes列表中
            continue
        seen.add(key)  #将数据添加到集合中

        cleaned.append([item, qty, price, day])  #将数据添加到列表中

    with open(OUTPUT_PATH, "w", newline="") as f:  #写入csv文件
        writer = csv.writer(f)  #创建一个csv写入对象
        writer.writerow(header)  #写入表头
        writer.writerows(cleaned)  #写入数据

    with open(LOG_PATH, "w") as f:
        f.write("# Midterm cleaning log\n\n")  #写入日志
        f.write(f"- Input file: `messy_shop.csv` ({len(data)} data rows)\n")  #写入输入文件
        f.write(f"- Output file: `clean_shop.csv` ({len(cleaned)} data rows)\n")  #写入输出文件
        f.write(f"- Total issues handled: {len(fixes)}\n\n")  #写入总问题数
        f.write("## Per-row fixes\n\n")  #写入每行 fixes    
        for fix in fixes:
            f.write(f"- {fix}\n")  #写入每行 fixes

    print(f"Wrote {len(cleaned)} rows, handled {len(fixes)} issues. See CLEANING_LOG.md")  #打印日志


if __name__ == "__main__":
    main()
