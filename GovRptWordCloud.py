import jieba
import wordcloud
import cv2
mask=cv2.imread("chinamap.png")
f=open("关于实施乡村振兴战略的意见.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls=jieba._lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",mask=mask,width=1000,height=700,\
    background_color="white")
w.generate(txt)
w.to_file("grwordcloud.png")