# 1. 准备一筐水果

var = ['苹果', '香蕉']

# 2. 浅拷贝：只是把“门牌号”给了 var2
var2 = var 


# 3. 往 var2 里加个橘子
var2.append('橘子')

# 4. 看看原先的 var 变成什么样了？
print("原来的 var 变成了：", var)





# 1. 试一个超级超级长的数字（随便按，多长都行！）
my_big_number = 123_456_789_012_345_678_901_234_567_890
print("我的超级大数字是：", my_big_number)

# 2. 查查它的“户口”
print("它的身份类型是：", type(my_big_number))

type(-37.)

# 实验 A：它是整数吗？
a = 37
print("a 的类型是：", type(a))

# 实验 B：加个点试试？
b = 37.
print("b 的类型是：", type(b))

# 实验 C：看看科学计数法
c = 0.1e-3  # 相当于 0.0001
print("c 的值是：", c)


# 1. 见证“点”的魔力
num1 = 37
num2 = 37.
print(f"37 的身份是: {type(num1)}") # 它是整数
print(f"37. 的身份是: {type(num2)}") # 它是实数

# 2. 挑战一下科学计数法
# 0.1e-3 意思就是把小数点往左挪三位
small_num = 0.1e-3 
print(f"0.1e-3 的真面目是: {small_num}")

# 3. 看看“不准”的实数
# 咱们算算 3.141592 乘以 10
result = 3.141592 * 10
print(f"计算结果是: {result}")

# 1. 普通除法：分得干干净净
print("13 除以 5 的精确结果：", 13 / 5)

# 2. 地板除：每人能分到几个完整的苹果？
print("13 个苹果分给 5 个人，每人完整分到：", 13 // 5)

# 3. 取余数：分完后还剩几个？
print("分完后，兜里还剩下：", 13 % 5)

# 4. 算算您的“财富”增值
# 假设 2 元钱翻了 10 倍（2的10次方）
print("2 的 10 次方是：", 2 ** 10)

2003 % 4

"你好" + "奶奶"
"哈基米!" * 3

# 1. 查查文字的“户口”
print("文字的类型是：", type("Data Science"))

# 2. 玩玩文字乘法（连夸自己三次！）
praise = "奶奶真棒！" * 3
print(praise)

# 3. 玩玩文字加法
greeting = "哈基米" + "陪您学" + "Python"
print(greeting)

x, y, z = 1, "b", 3*7e2
x
y
z

x, y = y, x
x
y

# 1. 先给 x 和 y 穿上不同的衣服
x = "红毛衣"
y = "绿围巾"
print(f"交换前：x是{x}, y是{y}")

# 2. 施展魔法：一秒互换！
x, y = y, x

# 3. 看看结果
print(f"交换后：x变成了{x}, y变成了{y}")

# 1. 一箭三雕：一行代码给三个变量赋值
name, age, hobby = "奶奶", 70, "学Python"
print(f"自我介绍：我是{name}，今年{age}岁，喜欢{hobby}。")

# 2. 交换魔法：把 name 和 hobby 的内容换一下
# 虽然逻辑上有点怪，但咱们试试电脑灵不灵
name, hobby = hobby, name

print("--- 交换魔法后 ---")
print(f"现在 name 变成了：{name}")
print(f"现在 hobby 变成了：{hobby}")
print(f"自我介绍：我是{name}，今年{age}岁，喜欢{hobby}。")


v = 7
v
v += 3                # Equivalent to: v = v + 3
v

type(z)

type(False)

# 1. 设个数字
my_age = 70

# 2. 让电脑判断：我是不是 18 岁？
is_eighteen = (my_age == 18)
print("我是 18 岁吗？", is_eighteen)

# 3. 复杂判断：我的年龄是不是在 60 到 80 之间？
is_senior = (my_age > 60 and my_age < 80)
print("我的年龄在 60 到 80 之间吗？", is_senior)

# 1. 设定今天是周几（1代表周一，5代表周五）
today_is = 5 

# 2. 让电脑做判断题：今天等于 5 吗？
# 记住：问问题要用两个等号 == 
is_friday = (today_is == 5)

# 3. 输出结果
print("今天是个好日子（周五）吗？", is_friday)

# 1. 如果今天是周1
today_is = 1

# 2. 让电脑做判断题：今天等于 5 吗？
# 记住：问问题要用两个等号 == 
is_friday = (today_is == 5)

# 3. 输出结果
print("今天是个好日子（周五）吗？", is_friday)


# 1. 创建一个购物清单（列表）
shopping_list = ["鸡蛋", "牛奶", "面包"]
print("最初的清单：", shopping_list)

# 2. 查查它的户口
print("它的身份是：", type(shopping_list))

# 3. 咱们换掉第一个东西（记住，第一个座位是 0 哦！）
shopping_list[0] = "鸭蛋"
print("修改后的清单：", shopping_list)

shopping_list.append('西瓜')
print("加上‘西瓜’后的清单：", shopping_list)

dailyKCal = [ 2330, 1990, 2150, 2290, 1920, 2370, 2050 ]
dailyKCal

days = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]
days

goodMoods = [ True, True, False, True, True, False, True ]
goodMoods

type( goodMoods )
type( [ 2330, 1990, 2150 ] )

len(days)

dataDay1 = [ 2330, "Mon", True ]
type( dataDay1)

dataByDays = [ [ 2330, "Mon", True ], [ 1990, "Tue", True ], [ 2150, "Wed", False ] ]
print( len(dataByDays) )
dataByDays

dataByVars = [ dailyKCal, days, goodMoods ]
print( len(dataByVars) )
dataByVars

emptyList = []
print( len(emptyList) )
emptyList

# 1. 创建一个列表（活页本）
my_list = ["鸡蛋", "牛奶"]
my_list[0] = "鸭蛋" # 电脑说：没问题，改好了！
print("列表改后：", my_list)

# 2. 创建一个元组（塑封照片）
my_tuple = ("鸡蛋", "牛奶")
print("元组内容：", my_tuple)

# 3. 尝试修改元组（这行会报错哦！）
my_tuple[0] = "鸭蛋"

x, y, z = ( "a", True, 0 )
print( x )
print( y )
print( z )

americano = [ "espresso", "hot water" ]
caffe_latte = [ "espresso", "steamed milk" ]
latte_macchiato = [ "steamed milk", "espresso" ]
apple_pie_set = [ "apple pie", "whipped cream" ]

order_steps = 2 * americano + caffe_latte + 3 * apple_pie_set + latte_macchiato
order_steps

days = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]
days
days[0]
len( days )
days[ len(days)-1 ] # 0~6
days[ -1 ]
days[ -2 ]
days[7] #IndexError: list index out of range


days = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]
days[0] = "MONDAY"       # works fine, days is a list
days

days = ( "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" )
#days[0] = "MONDAY"     # TypeError: 'tuple' object does not support item assignment

# 1. 准备一排数字
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. 只要中间的 2, 3, 4
middle = numbers[2:5]
print("中间一段：", middle)

# 3. 只要前三个
front = numbers[:3]
print("前三个：", front)

# 4. 只要奇数（从1开始，每隔2个取一个）
odds = numbers[1:10:2]
print("跳着切出的奇数：", odds)

my_name = ["王", "小", "凤"]
reversed_name = my_name[::-1]

print("正常顺序：", my_name)
print("倒过来的顺序：", reversed_name)

# ----- the following few code cells work both for lists and tuples -----
# days = ( "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" )
days = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]
days[2:5]                # note: Elements with indexes 2,3 and 4 (but not 5).
                         #       "Mon" has index 0.

workingDays = days[:5]
workingDays

weekendDays = days[5:]
weekendDays

copiedDays = days[:]
copiedDays

days[1:6:2]
days[6:1:-2]

# ----- modification here, so it can't be a tuple -----
days = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]
days[2:3] = [ "TUESDAY", "WEDNESDAY" ]
days

v = [ 1, 2, 3 ]   # []      allocates a new list
                  # 1,2,3   fills the list with 1, 2, 3
                  # v =     makes v point to the list
w = v             # w = v   makes w point to the same thing as v
v[0] = 100        #         changes the element of the list
v
w

v = [ 1, 2, 3 ]
w = v.copy()      # a new list is allocated, also possible: w = v[:]
                  # the elements of v are appended to the new list
v[0] = 100
v
w

someNums = [ 1, -2, 3, -4, 5 ]        # an iterable object
[x**2 for x in someNums]              # a list comprehension

someNums = [ 1, -2, 3, -4, 5 ]        # an iterable object
[(x,x**2) for x in someNums]          # each element is a tuple

someNums = [ 1, -2, 3, -4, 5 ]        # an iterable object
[x for x in someNums if x<0]          # only negative elements are processed

x = "I am the outside x"              # a global variable
someNums = [ 1, -2, 3, -4, 5 ]        # an iterable object
[x for x in someNums if x<0]          # local x is used, not the global one
x                                     # the global x is not changed

x = "我是外面的x"
# 这里的三个 y 必须统一，它们代表 someNums 里的每一个数字
[y for y in someNums if y < 0]
x

nums = ( 1, 2, 3 )
nums[1] = 22              # what's wrong here?
#元组不可变

nums = [ 1, 2, 3 ]
nums[3] = 4               # what's wrong here?

txt = "Statistics"
txt[0] = "s"              # what's wrong here?
#这是把index=0这个字母改掉
first_letter = txt[0]
first_letter

txt = "Statistics"
# 问电脑：它的 0 号位是不是等于 "S"？
print("第一个字母是大写 S 吗？", txt[0] == "S")

v = [ 1, 2, 3 ]
a = v
v = [ 4, 5, 6 ] #是让 v 去指一个新东西，不影响别人
a
v

v = [ 1, 2, 3 ]
b = v
v[:] = [ 4, 5, 6 ] #是把 v 原来指向的东西从内部改掉，所有共享这个数据的人都会看到变化
b

v = [ 5, 2, 1, 4, 3 ]
v.sort()
v


v = [ 5, 2, 1, 4, 3 ]
v.sort(reverse=True)
v

v = [5, 2, 1, 4, 3]
w = v.copy()  
# 必须先分家，盖个新房子！
v.sort()
v
w

v = [ 5, 2, 1, 4, 3 ]
# Here v should be reversed [ 3, 4, 1, 2, 5 ]
v.reverse()
v

v = [5, 2, 1, 4, 3]
w = v.copy()
v.reverse()
v
w

v = [ "eeeee", "bb", "a", "dddd", "ccc", "bb" ]
v

del v[2]
v

v.remove("bb")
v
# del v[1]

v.insert(2, "F")

v = [ "ababab", "baaab", "bbbaa", "aabba", "aaaab", "abbaa", "aabbb", "abaaa", "aaaaa", "bbbab", "bbbqb", "aaaqb", "bbbbq" ]
w = "bbbab"
w in v

v = [ "ababab", "baaab", "bbbaa", "aabba", "aaaab", "abbaa", "aabbb", "abaaa", "aaaaa", "bbbab", "bbbqb", "aaaqb", "bbbbq" ]
w = "abaab"
w not in v


#%% Understand conversions
lst = [1,2,3,"x","y","z"]
tuple( lst )              # the argument can be any object which can be iterated over

tpl = (1,2,3,"x","y","z")
list( tpl )               # the argument can be any object which can be iterated over

tuple( "Statistics" )     # "Statistics" can be iterated over
list( 'Data Science' )

#%% Practice comprehensions and try a generator
xs = [ 0, 1, 2, 3, 4, 5 ]
ys= [x**2 + x + 1 for x in xs]
ys

xs = range(6)
ys = [x**2 + x + 1 for x in xs]
ys

v = ["eeeee", "bb", "a", "dddd", "ccc", "bb"]
toRemove = "bb"
v
w = [x for x in v if x != toRemove]
w

print("w 里面还有 bb 吗？", "bb" in w)

# Comprehensions with tuple elements
# --- 1. 使用 zip() 像拉链一样对齐数据 ---
# 准备 8 个人的身高(cm)和体重(kg)
heights = [ 173, 179, 167, 195, 173, 184, 162, 169]
weights = [ 57, 58, 62, 84, 64, 74, 57, 44]

# zip 会把身高和体重一对一配对，生成 (height, weight) 的元组
# 我们用列表推导式计算每个人的 BMI 指数（公式：体重 / 身高的平方）
# 注意：身高要从厘米换算成米
bmis = [w / (h/100)**2 for h, w in zip
(heights, weights)]
print("8个人的BMI分别是：", bmis)

# --- 2. 使用 enumerate() 自动数数 ---
# enumerate 会给每个元素打上“座位号”索引
# 结果会变成像 (0, 173), (1, 179) 这样的配对
indexed_heights = list(enumerate(heights))
print("带编号的身高列表：", indexed_heights)

# --- 3. 进阶：批量剔除多个元素 (in 与 not) ---
# 如果我们要剔除的不仅仅是 "bb"，而是一堆不想要的词
v = ["eeeee", "bb", "a", "dddd", "ccc", "bb"]
toRemove = ["bb", "ccc"] # 这次我们要删掉两个词

# 只有当 x 不在 toRemove 名单里时，才保留
clean_v = [x for x in v if x not in toRemove]
clean_v = [x for x in v if x != toRemove]
print("深度清理后的列表：", clean_v)

heights = [ 173, 179, 167, 195, 173, 184, 162, 169 ]  # 8 persons
weights = [ 57, 58, 62, 84, 64, 74, 57, 44 ]          # same 8 persons, same order
zip( heights, weights )                # this is a generator of ( height, weight ) tuples
list( zip( heights, weights ) )        # when converted to list you see the tuples
bmis = [w / (h/100)**2 for h, w in list( zip( heights, weights ) )  ]
bmis

heights = [ 173, 179, 167, 195, 173, 184, 162, 169 ]  # 8 persons
enumerate( heights )                   # this is a generator of ( index, element ) tuple pairs
tuple( enumerate( heights ) )          # do you understand this result?

nestedList = [ "a", [ "ba", [ "bba", "bbb" ], "bc", [ "bda", "bdb" ], "be" ], "c", [ [ "daa", "dab" ] ] ]
nestedList