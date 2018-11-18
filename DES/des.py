class des:
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
    left = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    # 压缩置换表
    pc_2 = [13, 16, 10, 23, 0, 4,
            2, 27, 14, 5, 20, 9,
            22, 18, 11, 3, 25, 7,
            15, 6, 26, 19, 12, 1,
            40, 51, 30, 36, 46, 54,
            29, 39, 50, 44, 32, 47,
            43, 48, 38, 55, 33, 52,
            45, 41, 49, 35, 28, 31]

    # IP置换表
    ip = [57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7,
          56, 48, 40, 32, 24, 16, 8, 0,
          58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6]

    # 扩展变换表
    expansion = [31, 0, 1, 2, 3, 4,
                 3, 4, 5, 6, 7, 8,
                 7, 8, 9, 10, 11, 12,
                 11, 12, 13, 14, 15, 16,
                 15, 16, 17, 18, 19, 20,
                 19, 20, 21, 22, 23, 24,
                 23, 24, 25, 26, 27, 28,
                 27, 28, 29, 30, 31, 0]

    # S盒函数
    Sbox = [
        # S1
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
         0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
         4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
         15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

        # S2
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
         3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
         0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
         13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        # S3
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
         13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
         13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
         1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

        # S4
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
         13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
         10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
         3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

        # S5
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
         14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
         4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
         11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

        # S6
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
         10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
         9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
         4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

        # S7
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
         13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
         1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
         6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

        # S8
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
         1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
         7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
         2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]

    fp = [39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25,
          32, 0, 40, 8, 48, 16, 56, 24]

    p = [
        15, 6, 19, 20,
        28, 11, 27, 16,
        0, 14, 22, 25,
        4, 17, 30, 9,
        1, 7, 23, 13,
        31, 26, 2, 8,
        18, 12, 29, 5,
        21, 10, 3, 24
    ]

    def wordToBin(word, n):
        x = ord(word)
        N = [0] * n;
        i = 1
        while (i <= n):
            N[n - i] = x % 2
            x = x // 2
            # //代表除法取整，否则自动带上小数点
            i = i + 1
        return N

    def hexToBin(hex):#传入的hex为字符类型
        if hex>='0' and hex<='9':
            return des.numberToBin(ord(hex)-48,4)
        elif hex>='A' and hex<='Z':
            # ord(hex)-65+10
            return des.numberToBin(ord(hex) - 55, 4)
        else:
            # ord(hex)-97+10
            return des.numberToBin(ord(hex) - 87, 4)


    def binToStr(array):
        str = ""
        for i in range(0, 8):
            word = 0
            for x in array[i * 8:i * 8 + 8]:
                word = word * 2 + x
            str = str + chr(word)
            print(word, ',', end="")
        return str

    def numberToBin(number, n):
        N = [0] * n;
        i = 1;
        while (i <= n):
            N[n - i] = number % 2
            number = number // 2
            i = i + 1
        return N

    def strToBin(str):
        str_bin = []
        for x in str:
            str_bin+=des.wordToBin(x, 8)
        return str_bin

    def hexstrToBin(str):
        hex_bin = []
        for x in str:
            hex_bin+=des.hexToBin(x)
        return hex_bin

    # 移位函数，0代表向左移，1代表向右移
    def shift(array, deraction, n):
        if deraction == 1:
            return array[len(array) - n:] + array[:len(array) - n]
        else:
            # 默认左移
            return array[n:] + array[:n]

    def convert(array, lib):
        arr = []
        for x in lib:
            arr.append(array[x])
        return arr

    def xor(arr1, arr2):
        arr = []
        for i in range(0, len(arr1)):
            arr.append(arr1[i] ^ arr2[i])
        return arr

    def zip(self, arr, i):
        x = arr[0] * 2 + arr[5]
        # print('横坐标为',x)
        y = arr[1] * 8 + arr[2] * 4 + arr[3] * 2 + arr[4]
        # print('纵坐标为',y)
        value = des.Sbox[i][x * 16 + y]
        # print('value: ',value)
        return des.numberToBin(value, 4)

    # 扩展函数
    def EX(R, K):
        s = []
        E_R = des.convert(R, des.expansion)
        ER_xor_K = des.xor(E_R, K)
        # print(len(ER_xor_K),ER_xor_K)
        for i in range(0, 8):
            s = s + zip(ER_xor_K[i * 6:i * 6 + 6], i)
            # print(p)
        return des.convert(s, des.p)

    def __set_charKey__(self, Key):
        # self.charKey = Key
        self.binKey = des.strToBin(Key)
        # print('bin_key is ',type(self.binKey))
        self.__produce_sonkey__()

    def __set_hexKey__(self, Key):
        self.binKey = des.hexstrToBin(Key)
        self.__produce_sonkey__()

    def __set_charPlaintext__(self, Plaintext):
        self.charPlaintext = Plaintext
        print('成功拿到字符明文', Plaintext)

    def __set_hexPlaintext__(self, Plaintext):
        self.hexPlaintext = Plaintext
        print('成功拿到十六进制明文', Plaintext)

    # def test(self):
    #     array_str=""
    #     for i in range(0,self.binKey.__len__()):
    #         if i%8==0:
    #             array_str+=" "
    #         array_str+=str(self.binKey[i])
    #     return array_str

    def __get_str__(self, array, n):
        # n个字符添加一个空格
        array_binstr=""
        for i in range(0,array.__len__()):
            if i%n==0:
                array_binstr+=" "
            array_binstr+=str(array[i])
        return array_binstr

    def __produce_sonkey__(self):
        self.C=[[]]*17
        self.D=[[]]*17
        self.key_son=[[]]*16
        self.key_zip=des.convert(self.binKey,des.pc_1)
        self.C[0]=self.key_zip[:28]
        self.D[0]=self.key_zip[28:56]
        for i in range(1, 17):
            self.C[i] = des.shift(self.C[i - 1], 0, des.left[i - 1])
            self.D[i] = des.shift(self.D[i - 1], 0, des.left[i - 1])
        # print('C[0] is ',type(self.C[0]))
        # print(des.__get_str__(self,self.C[0]))
        for i in range(0, 16):
            self.key_son[i] = des.convert(self.C[i + 1] + self.D[i + 1], des.pc_2)
        pass

    def __get_binKey__(self):
        return des.__get_str__(self,self.binKey,8)

    def __get_C0__(self):
        return des.__get_str__(self,self.C[0],7)

    def __get_D0__(self):
        return des.__get_str__(self,self.D[0],7)

    def __get_C1__(self):
        return des.__get_str__(self,self.C[1],7)

    def __get_D1__(self):
        return des.__get_str__(self,self.D[1],7)

    def __get_K1__(self):
        return des.__get_str__(self,self.key_son[0],6)