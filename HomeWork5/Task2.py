# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

path_file = input('Введите имя исходного файла: ')
path_encode = input('Введите имя файла для RLE кодирования: ')

def RLE_coding(path_file, path_encode):
    with open(path_file, 'r', encoding='utf-8') as my_f1:
        lines = my_f1.readlines()
        for line in lines:
            for_coding = line.strip()
            with open(path_encode, 'a', encoding='utf-8') as my_f2:
                i = 0
                encode = ''
                while i < len(for_coding):
                    count = 1
                    while i + 1 < len(for_coding) and for_coding[i] == for_coding[i + 1]:
                        count += 1
                        i += 1
                    encode += str(count) + for_coding[i]
                    i += 1
                for i in range(len(encode)):
                    my_f2.write(f'{encode[i]}')
                my_f2.write('\n')

def RLE_decoding(path_encode):
    decode = ''
    count = ''
    with open(path_encode, 'r', encoding='utf-8') as my_f1:
        lines = my_f1.readlines()
        for line in lines:
            for_decoding = line.strip()
            for char in for_decoding:
                if char.isdigit():
                    count += char
                else:
                    decode += char * int(count)
                    count = ''
            print(decode)
            decode = ''


RLE_coding(path_file, path_encode)
RLE_decoding(path_encode)


