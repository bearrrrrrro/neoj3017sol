# 解法

## 一些檔案

* 我剛寫完的AC code: sol.py
* README.pdf，因為github不支援latex，所以建議下載pdf來看

## 題解

寫出有效率的解法需要一些可能不太好想但是蠻直覺的數學

### 觀察1

如果正整數$N$可以被拆成另外兩個正整數的乘積，則其中一個正整數必定不大於$\sqrt{N}$

舉例來說，$60 = 1 \cdot 60 = 2 \cdot 30 = 6 \cdot 10$，可以發現不管怎麼拆其中一個一定小於$\sqrt{60}$

證明：

使用反證法。假設存在正整數$a, b$ 使得$ab = N$，其中$a, b > \sqrt{N}$，那可以輕易推得$ab > \sqrt{N}\sqrt{N}=N$，矛盾。



利用觀察 1，大家大概可以猜到如果我要知道$N$是不是質數，也就是他有沒有除了$1$和$N$以外的因數，那只要窮舉到$\sqrt{N}$就好了。

不過我發現有些人有相同一個問題：需不需要建質數表呢？我的答案是沒有必要，我在出題時甚至沒有想到會有人想建質數表XD

### 觀察 2

如果從2開始小到大去試除$N$，那後面試到的數字如果可以除掉$N$，那他這個數字必定是質數。看不懂我的這個過程在幹麻的可以搭配我的程式碼服用。

說明：因為後面試到的數字如果可以整除$N$，假設這個數字是$d$好了，如果$d$不是質數，那他的因數早就在前面被除光光了。



最後要注意這個試除的過程可能會剩下一個大於$\sqrt{N}$的因數，要記得把他輸出，可以想一下為什麼剩下的數字一定是質數



