# expected output 0, 1, 2, 3
# for i in range(4):
#     print(i) 


# expected output 2, 3, 4
# 2以上5未満の整数を生成
# for i in range (2, 5):
#     print(i)


height = int(input('身長を入力してください>>'))
weight = int(input('体重を入力してください>>'))

height = height / 100 # mに変換

bmi = weight / (height ** 2)
print('あなたのBMIは、{}' .format(bmi))


