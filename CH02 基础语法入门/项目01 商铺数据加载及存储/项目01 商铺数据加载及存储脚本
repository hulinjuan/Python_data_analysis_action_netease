"""
【项目01】商铺数据加载及存储

作业要求：
1.成功读取"商铺数据.csv"文件
2.解析数据，存成列表字典格式：[{'var1':value1,'var2':value2,'var3':value3.....},.....{}]
3.数据清洗：
（1）comment,price两个字段清洗成数字
（2）清除字段缺失的数据
（3）commentlist拆分成三个字段，并且清洗成数字
4.结果存为.pkl文件

"""
#读取数据
f = open("C:\\Users\\lindsay.hu\\Desktop\\商铺数据.csv",'r',encoding = 'utf8')
#rint(f.read())

#看前5行
for line in f.readlines()[:100]:
    print(line.split(',')[-1].split('                                '))
    
f.seek(0) 

#清洗数据 - 
def fcm(s):
    if '条' in s:
        return (int(s.split(' ')[0]))
    else:
        return('缺失数据')

def fpr(s):
    if '￥' in s:
        return (int(s.split('￥')[-1]))
    else:
        return('缺失数据')

def fcl(s):
    if len(s) == 3:
        quality = float(s[0][2:])
        envi = float(s[1][2:])
        service = float(s[2][2:])
        return([quality,envi,service])
    else:
        return('缺失数据')
         
"""
for line in f.readlines()[:10]:
    cm = fcm(line.split(',')[2])
    print(cm)
"""
for line in f.readlines()[:10]:
    cl = fcl(line.split(',')[-1].split('                                '))
    print(cl)
    
#数据清洗

datalst = []

n = 0
f.seek(0)

for i in f.readlines():
    data = i.split(',')
    #print(data)
    classify = data[0]
    name = data[1]
    com_count = fcm(data[2])
    star = data[3]
    price = fpr(data[4])
    add = data[5]
    qua = fcl(data[-1].split('                                '))[0]
    env = fcl(data[-1].split('                                '))[1]
    service = fcl(data[-1].split('                                '))[2]
    
    #print(com_count,star,price,add,qua,env,service)
    if '缺失数据' not in [com_count,price,qua]:
        n += 1
        data_lst2 = [['classify',classify],
                    ['name',name],
                    ['comment_count',com_count],
                    ['star',star],
                    ['price',price],
                    ['address',add],
                    ['quality',qua],
                    ['environment',env],
                    ['service',service]]
        #print(data_lst2)
        datalst.append(dict(data_lst2))
        print("成功读取%i条数据: " %n)
        print(dict(data_lst2))
    else:
        continue
f.close()
print(datalst)
print("总共加载%i条数据" %n)