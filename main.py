# -*- coding: utf-8 -*-
import cv2
import numpy as np

#2箇所の変更をすれば良い．

#分割数はここで決める（変更する箇所1）
bun = 64

#ファイル名はここで決める
#ファイルを読み込む（変更する箇所2）
img_name = "cube10.jpg"
img = cv2.imread(img_name)
h, w, c = img.shape
#一応元画像のファイルサイズを表示
print(img.shape)

#分割するサイズを決定，元画像を分割数で割れば1辺の長さが決まる．
h1 = h // bun
w1 = w // bun
h3 = h1 * bun
w3 = w1 * bun

#分割するサイズに合わせて画像をリサイズ
resizeimg = cv2.resize(img, dsize=(w3, h3))
#リサイズした画像を表示
print(resizeimg.shape)

#この後使う変数諸々
h_0 = 0
h_1 = 1
w_0 = 0
w_1 = 1
ht = (h1*h_0)
hb = (h1*h_1)
wl = (w1*w_0)
wr = (w1*w_1)
mmm2 = 1
cnt_1=0

#キャンパスを作成
dst_campus = np.full((h3, w3, 3),128,dtype=np.uint8)

#キャンパスを左上から右に分割したサイズで塗り直す
#左から右に一列行ったら，折り返す
for i in range(bun*bun-2):

    dst1 = resizeimg[ht:hb,wl:wr]
    avg_color_1 = np.average(dst1, axis=0)
    dst_h1, dst_w1, dst_c1 = np.average(avg_color_1, axis=0)
    dst_w_s1 = (dst_h1, dst_w1, dst_c1)
    cv2.rectangle(dst_campus, (wl,ht), (wr,hb), (dst_w_s1), thickness=-1)

    cnt_1 += 1

    if cnt_1 == bun * mmm2:
            h_0 += 1
            h_1 += 1
            w_0 = 0
            w_1 = 1
            ht = (h1*h_0)
            hb = (h1*h_1)
            wl = (w1*w_0)
            wr = (w1*w_1)
            mmm2 += 1
            print(ht,hb,wl,wr)

    else:
                w_0 += 1
                w_1 += 1
                ht = (h1*h_0)
                hb = (h1*h_1)
                wl = (w1*w_0)
                wr = (w1*w_1)

#出来上がった画像をくっつけて保存する．
else:
            cv2.imwrite(img_name + str(bun) +".jpg" ,dst_campus)
