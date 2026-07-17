import csv  #引入csv模块用于读取csv文件
import os  #引入os模块用于操作文件和目录

import matplotlib  #引入matplotlib模块用于绘制图表

matplotlib.use("Agg")
import matplotlib.pyplot as plt  #引入matplotlib.pyplot模块用于绘制图表

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  #获取当前文件的目录
INPUT_PATH = os.path.join(BASE_DIR, "clean_shop.csv")  #获取clean_shop.csv文件的路径
CHART_PATH = os.path.join(BASE_DIR, "shop_chart.png")  #获取shop_chart.png文件的路径    


def main():
    revenue = {}  #定义一个字典用于存储每个商品的销售额
    with open(INPUT_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)  #读取csv文件
        for row in reader:
            item = row["item"]  #获取商品名称
            qty = int(row["qty"])  #获取商品数量
            price = int(row["price"])  #获取商品价格
            revenue[item] = revenue.get(item, 0) + qty * price  #计算每个商品的销售额

    items = list(revenue.keys())  #获取所有商品名称
    values = [revenue[item] for item in items]  #获取所有商品销售额

    plt.figure(figsize=(7, 5))  #设置图表大小
    bars = plt.bar(items, values, color="#4C72B0")  #绘制柱状图
    plt.title("Revenue by Item")  #设置图表标题
    plt.xlabel("Item")
    plt.ylabel("Revenue (gold)")  #设置y轴标签  

    for bar, value in zip(bars, values):  #绘制每个商品的销售额
        plt.text(bar.get_x() + bar.get_width() / 2, value, str(value),
                 ha="center", va="bottom")  #在每个柱状图上显示销售额

    plt.tight_layout()  #调整图表布局
    plt.savefig(CHART_PATH, dpi=120)  #保存图表
    print(f"Saved chart to {CHART_PATH}")  #打印保存路径
    print("Revenue by item:", revenue)  #打印每个商品的销售额


if __name__ == "__main__":
    main()  #调用main函数
