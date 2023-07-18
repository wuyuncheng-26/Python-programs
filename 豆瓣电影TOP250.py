# 本程序需安装第三方库beautifulsoup4和requests
import bs4
import requests
print("————————豆瓣电影TOP250————————")
for start in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={start}&filter="
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0"}
    res = requests.get(url=url, headers=headers)
    res.encoding = "utf-8"
    bs = bs4.BeautifulSoup(res.text, "html.parser")
    info = bs.find_all("div", class_="info")
    for i in range(25):
        title = info[i].find("span", class_="title").string
        rating_num = info[i].find("span", class_="rating_num").string
        print(f"TOP {start + i + 1}：{title}（评分：{rating_num}）")
