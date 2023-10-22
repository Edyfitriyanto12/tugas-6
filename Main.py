# from math_function import add


# def main():

#     data_1 = int(input("masukkan input 1 :"))
#     data_2 = int(input("masukkan input 2 :"))
#     operator = input("masukkan operator :")

#     if operator == "+":
#         result = add(data_1, data_2)

#     print("{} {} {} = {} ".format(data_1, operator, data_2, result))


# if __name__ == "__main__":
#     print("Hello Main !")
#     main()

#program 2
from math_function import multiply, divide

hasil_perkalian = multiply(10, 5)
print("Hasil Perkalian:", hasil_perkalian)

hasil_pembagian = divide(10, 2)
print("Hasil Pembagian:", hasil_pembagian)
