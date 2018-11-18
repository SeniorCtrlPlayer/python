def numberToBin(number, n):
    N = [0] * n;
    i = 1;
    while (i <= n):
        N[n - i] = number % 2
        number = number // 2
        i = i + 1
    return N

def hexToBin(hex):  # 传入的hex为字符类型
    if hex >= '0' and hex <= '9':
        return numberToBin(ord(hex) - 48, 4)
    elif hex >= 'A' and hex <= 'F':
        # ord(hex)-65+10
        return numberToBin(ord(hex) - 55, 4)
    else:
        # ord(hex)-97+10
        return numberToBin(ord(hex) - 87, 4)

def hexstrToBin(str):
    hex_bin = []
    for x in str:
        hex_bin+=hexToBin(x)
    return hex_bin

Key = input("请输入1个字符：")
print('it\'s hex is: ',hexstrToBin(Key))