""" BT2: Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in
thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết
quả đầu ra phải là 40320."""

x = int(input("Nhập các số cần tính. "))
def fact(x):
    if x==0:
        return 1
    return x * fact(x-1)
print (fact(x))

"""BT3: Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i)
như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này. Ví dụ:
Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}."""

n = int(input("Nhập số nguyên n: "))
d = dict()

for i in range(1,n+1):
    d[i] = i*i
print(d)
#helo
