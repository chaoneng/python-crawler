import requests
from bs4 import BeautifulSoup
import lxml

#使用PTT 教育板做為示範
respones = requests.get("https://web.asia.edu.tw/files/501-1000-1007-1.php?Lang=zh-tw")
respones.encoding='utf-8'
#print (respones.text)
# print (respones.text)

soup = BeautifulSoup(respones.text, "lxml")
#print(soup)
titles = soup.find_all("div",{"class":"h5"})
# print (titles.getText())

title_list= []
for title in titles:
    #print (title.find("a")['href']) #[取二的元素]
    title_list.append(title.getText().strip())

# print (title_list)

#soup.find_all /soup.find /soup.select /soup.select_one
# title = soup.find("div",{"class":"title"})
# print (title.getText())

# titles = soup.find_all("div",{"class":"title"})
# print (titles)

# titles = [t.getText().strip() for t in titles]
# print(type(titles))

# dict_squares = []
# for title in titles:
#     dict_squares.append (title.getText().strip())
# # print (dict_squares)

#將list 轉乘 Str
text = "".join(title_list) 
# print (text)

# # # #使用jieba套件，進行文章中文斷詞分析

# #指定字典(使用預設字典)
# import jieba
# jieba.set_dictionary('/Users/cnwang/Documents/Python_Code/dict.txt.big.txt')

# #移除標點符號 punctuation removal
# text = text.replace('[^\w\s]','').replace('／',"").replace('《','').replace('》','').replace('，','').replace('。','').replace('「','').replace('」','').replace('（','').replace('）','').replace('！','').replace('？','').replace('、','').replace('▲','').replace('…','').replace('：','')
# # print(text)

# wordlist = jieba.cut(text)
# words = " ".join(wordlist)
# # print('預設:', '|'.join(jieba.cut(text, cut_all=False, HMM=True)))
# # print('全關閉:', '|'.join(jieba.cut(text, cut_all=False, HMM=False)))
# # print('全關閉:', '|'.join(jieba.cut(text, cut_all=True, HMM=True)))


# #將字詞頻率以word cloud(文字雲)呈現
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud

# # 設定停用字詞 
# stopwords = {}.fromkeys(["[","]","來","個","再","的","和","是","有","更","會","可能","有何","從","對","就", '\n','越','為','這種','多','越來',' '])
# #stopwords = {"也","但","來","個","再","的","和","是","有","更","會","可能","有何","從","對","就",'\n','越','為','這種','多','越來',' '}

# # 使用cut_for_search(搜尋引擎)斷詞模式並產生字詞頻率的dictionary (並剔除stopwords的計算)
# Sentence = jieba.cut_for_search(text) 
 
# # # create a python dictionary
# hash = {}
# for item in Sentence:
 
#     if item in stopwords:
#         continue
    
#     if item in hash:
#         hash[item] += 1
#     else:
#         hash[item] = 1
 
# # 文字雲樣式設定
# wc = WordCloud(font_path="/Users/cnwang/Documents/Python_Code/Noto_Sans_TC/NotoSansTC-Black.otf", #設置字體
#                background_color="white", #背景顏色
#                max_words = 2000 ,        #文字雲顯示最大詞數
#                stopwords=stopwords)      #停用字詞
 
# # 使用dictionary的內容產生文字雲
# wc.generate_from_frequencies(hash)
# # 視覺化呈現
# plt.imshow(wc)
# plt.show()

#####
import matplotlib.pyplot as plt
import os
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

alice_mask = np.array(Image.open("alice_mask.png"))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue',font_path="/Users/cnwang/Documents/Python_Code/Noto_Sans_TC/NotoSansTC-Light.otf")

# generate word cloud
wc.generate(text)
print (wc.generate(text))
# store to file
# wc.to_file("alice.png")

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
