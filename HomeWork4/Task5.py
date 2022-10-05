# 5. ** Даны два файла, в каждом из которых находится запись многочленов. 
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!

def number_of_lines_in_file(doc):
    return len(open(doc).readlines())

def merge_files(doc1, doc2, doc3):
    if number_of_lines_in_file(doc1) == number_of_lines_in_file(doc2):
        file1 = open(doc1, 'r')
        file2 = open(doc2, 'r')
        while True:
            t1 = file1.readline().strip('\n')
            t1 = t1.strip(" ")
            t1 = t1.strip("0")
            t1 = t1.strip(" ")
            t1 = t1.strip("=")
            t2 = file2.readline()
            if not (t1 or t2):
                break
            with open(doc3, 'a') as f3:
                f3.write(f"{t1}+ {t2}")
    else:
        print('The contents of the files do not match!')

merge_files('D:/Домашнее задание GeekBrains/Seminar_python(start)/HomeWork4/Task4.txt', 'D:/Домашнее задание GeekBrains/Seminar_python(start)/HomeWork4/Task4_2.txt', 'D:/Домашнее задание GeekBrains/Seminar_python(start)/HomeWork4/Task5.txt')

