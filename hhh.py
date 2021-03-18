# import random
#
# lsGiftIn = [['Jack', 'apple'], ['June', 'ball'], ['Mary', 'card'], ['Duke', 'doll'], ['James', 'egg'],
#             ['Tina', 'flute'], ['Tom', 'coffee']]  # 存储参与者的姓名和自己带来的礼物
# lsGiftOut = []  # 存储交换后的结果
# n = len(lsGiftIn)  # 参与人数
# gifts = [i[1] for i in lsGiftIn]  # 未分配出去的礼物
# for x in range(n):
#     flag = 0
#     person = lsGiftIn[x][0]
#     myGift = lsGiftIn[x][1]
#     if myGift in gifts:
#         flag = 1
#         gifts.remove(myGift)
#     getGift = random.choice(gifts)  # 随机分配礼物
#     lsGiftOut.append([person, getGift])
#     gifts.remove(getGift)
#     if flag:
#         gifts.append(myGift)
#
# print(lsGiftOut)





dictGiftIn = {'Jack': 'apple', 'Peter': 'beer', 'Tom': 'card', 'Duke': 'doll', 'Mary': 'pineapple', 'James': 'flute',
              'Tina': 'coffee'}
dictGiftOut = {}
persons = list(dictGiftIn.keys())
for p in persons:
    flag = 0  # 标记自己带来的礼物是否还未分配出去
    if p in dictGiftIn:
        flag = 1
        myGift = dictGiftIn.pop(p)  # 如果自己带来的礼物还未分配，则去掉该礼物
    print('去掉自己的礼物:{}'.format(dictGiftIn))
    getGift = dictGiftIn.popitem()  # 随机返回并移除一对key-value值
    print('删除一个key-value:{}'.format(dictGiftIn))
    dictGiftOut[p] = getGift[1]  # 得到的礼物
    print('得到礼物:{}'.format(dictGiftOut))
    if flag:
        dictGiftIn[p] = myGift  # 将自己的礼物添到未分配礼物中
        print('自己的礼物给到没有礼物的人:{}'.format(dictGiftIn))
        print('------------------------------------------------')
print(dictGiftOut)  # 输出礼物分配情况