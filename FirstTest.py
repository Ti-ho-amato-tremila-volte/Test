import random
secret = random.randint(1,10)
print('-------------我爱Java，C++，python------------')
temp = input ("不妨猜一下我现在心里想的是哪个数字：")
guess = int(temp)
while guess != secret :
    temp = input("哎呦(￣y▽,￣)╭ ，猜错了，重新再猜一次吧")
    guess = int(temp)
    if guess == secret :
        print ("卧槽，你是我肚子里的蛔虫吗？！")
        print ("哼(￢︿̫̿￢☆)，猜中了也没有奖励哦。")

    else :
        if guess > secret :
            print ("哎(●ˇ∀ˇ●)可惜，大了大了~~")
        else :
            print ("嘿O(∩_∩)O，错了错了，你猜小了")

print ("算了算了≧ ﹏ ≦，心累了╯︿╰，不想玩了，ヾ(￣▽￣)Bye,~Bye~")
