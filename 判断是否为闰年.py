#编写程序，运行后用户输入4为整数年份，判断是否为闰年。 判断闰年算法如下：如果年份能被400整除，是闰年; 如果年份能被4整除，但不能被100整除，也是闰年
year=int(input('请输入年份：'))
if year%400==0:
    print('闰年')
elif year%4==0:
    if year%100==0:
        print('不是闰年')
    else:
        print('闰年')
else:
    print('不是闰年')
print('ok')
