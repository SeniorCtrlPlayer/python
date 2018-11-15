import tkinter as tk
window = tk.Tk()
window.title("My First Python Window!")
sw = window.winfo_screenwidth()
#得到屏幕宽度
sh = window.winfo_screenheight()
#得到屏幕高度
ww=400
wh=600
#窗口的宽高都为100
x=(sw-ww)/2
y=(sh-wh)/2
window.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
window.resizable(width=False,height=True)
#window.mainloop()

# 密钥置换表
pc_1 = [56, 48, 40, 32, 24, 16, 8,
        0, 57, 49, 41, 33, 25, 17,
        9, 1, 58, 50, 42, 34, 26,
        18, 10, 2, 59, 51, 43, 35,
        62, 54, 46, 38, 30, 22, 14,
        6, 61, 53, 45, 37, 29, 21,
        13, 5, 60, 52, 44, 36, 28,
        20, 12, 4, 27, 19, 11, 3]

# 左移表
left=[1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# 压缩置换表
pc_2=[13, 16, 10, 23,  0,  4,
      2, 27, 14,  5, 20,  9,
      22, 18, 11,  3, 25,  7,
      15,  6, 26, 19, 12,  1,
      40, 51, 30, 36, 46, 54,
      29, 39, 50, 44, 32, 47,
      43, 48, 38, 55, 33, 52,
      45, 41, 49, 35, 28, 31]

# IP置换表
ip = [57, 49, 41, 33, 25, 17, 9,  1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7,
      56, 48, 40, 32, 24, 16, 8,  0,
      58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6]

# 扩展变换表
expansion=[31,  0,  1,  2,  3,  4,
           3,  4,  5,  6,  7,  8,
           7,  8,  9, 10, 11, 12,
           11, 12, 13, 14, 15, 16,
           15, 16, 17, 18, 19, 20,
           19, 20, 21, 22, 23, 24,
           23, 24, 25, 26, 27, 28,
           27, 28, 29, 30, 31,  0]

#将单个字符转换成对应的8位二进制码数组
def wordToBin(word):
    x = ord(word)
    N = [0]*8;
    i = 0
    while(i<8):
        N[7-i]=x%2
        x=x//2
        # //代表除法取整，否则自动带上小数点
        i=i+1
    return N

def strToBin(str):
    str_bin=[]
    for x in str:
        str_bin=str_bin+wordToBin(x)
    return str_bin

# 移位函数，0代表向左移，1代表向右移
def shift(array,deraction,n):
    if deraction == 1:
        return array[len(array)-n:]+array[:len(array)-n]
    else:
        # 默认左移
        return array[n:]+array[:n]
# ciphertext_1=[]
# for x in pc_1:
#     ciphertext_1=ciphertext_1+

def convert(array,lib):
    arr=[]
    for x in lib:
        arr.append(array[x])
    return arr

############################################################ 先生成16个子密钥
Key = input("请输入8个字符的密钥：")
bin_Key = strToBin(Key)
print('密钥的二进制数组位：',bin_Key)
key_plus=[]
for x in pc_1:
    key_plus.append(bin_Key[x])
print('经过一轮pc_1的密钥：',key_plus)

# CD[0]代表C0或者D0，CD[0][0]代表C0。。。
C=[[]]*17
D=[[]]*17
key_son=[[]]*16
C[0]=(key_plus[:28])
D[0]=(key_plus[28:56])
print(len(C[0]),'子密钥C部分：',C[0])
# print(len(C[0]),'左移1位的C：',shift(C[0],0,1))
# print(len(C[0]),'右移1位的C：',shift(C[0],1,1))
for i in range(1,17):
    C[i]=shift(C[i-1],0,left[i-1])
    D[i]=shift(D[i-1],0,left[i-1])

# 由CnDn组合经过pc_2变换得到kn
for i in range(0,16):
    key_son[i]=convert(C[i+1]+D[i+1],pc_2)
    print(len(key_son[i]),key_son[i])

#############################################################

# 对两个一维数组进行异或操作
def xor(arr1,arr2):
    arr=[]
    for i in range(0,len(arr1)):
        arr.append(arr1[i]^arr2[i])
    return arr

def zip(arr):
    return

# 扩展函数
def EX(R,K):
    p=[]
    E_R=convert(R,expansion)
    ER_xor_K=xor(E_R,K)
    for i in range(0,8):
        p=p+zip(ER_xor_K[i*8:i*8+8])

# 对明文进行将加密
Plaintext = input("请输入8个字符的明文: ");
bin_Plaintext = strToBin(Plaintext)
print('明文的二进制数组为：',bin_Plaintext)
plaintext_ip=[]
for x in ip:
    plaintext_ip.append(bin_Plaintext[x])
print('ip变换后的明文二进制：',convert(bin_Plaintext,ip))
L=[[]]*17
R=[[]]*17
L[0]=plaintext_ip[:32]
R[0]=plaintext_ip[32:64]
print('ip变换后的明文二进制：',L[0])
print(R[0])
for i in range(1,17):
    L[i]=R[i-1]
