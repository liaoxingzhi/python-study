# 做一个注册登录系统
import time
name = []
file = {}
print('-------------------注册登录系统------------------')
while 1:
    sum = 0
    choice = int(input('1.注册，2.登录，3.修改密码，4.退出系统'))
    if choice == 1:
        user_name = input('请输入账号：')
        name.append(user_name)
        while 1:
            pass_word1 = input('请输入密码：')
            pass_word2 = input('请再次输入密码：')
            if pass_word1 == pass_word2:
                print('注册成功！')
                file[user_name] = pass_word1
                for i in file:
                    print('账号：',i,'\n密码：',file[i])
                break
            else:
                print('两次输入密码不一致')
    elif choice == 2:
        user_name = input('请输入账号：')
        if user_name in name:
            while 1:
                pass_word = input('请输入密码：')
                if pass_word == file[user_name]:
                    print('登录成功！')
                    break
                else:
                    print('密码错误！')
        else:
            print('该账户不存在，请注册后再登录')
    elif choice == 3:
        while 1:
            if sum != 0:
                break
            else:
                user_name = input('请输入账号：')
                if user_name in name:
                    while 1:
                        if sum != 0:
                            break
                        else:
                            pass_word = input('请输入旧密码：')
                        if pass_word == file[user_name]:
                            while 1:
                                pass_word3 = input('请输入新密码：')
                                pass_word4 = input('请再次输入新密码：')
                                if pass_word3 == pass_word4 and pass_word3 != file[user_name]:
                                    print('密码修改成功！')
                                    file[user_name] = pass_word3
                                    for i in file:
                                        print('账号：',i,'\r新密码：',file[i])
                                    sum = sum + 1
                                    break
                                elif pass_word3 == file[user_name]:
                                    print('新密码与旧密码一致，请重新输入')
                                else:
                                    print('密码错误，请重新输入')
                        else:
                            print('密码错误，请重新输入')
                else:
                    print('该账户不存在，请注册后再登录')
    elif choice == 4:
        print('感谢您的使用,程序将在5秒后退出')
        for i in range(1,5):
            time.sleep(1)
            print('程序将在{}秒后退出'.format(5 - i))
        break
    else:
        print('请输入指定数字')