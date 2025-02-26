def square(x):
    return x if len(x) > 6 else []

x = ["salom", "dunyom", "mexanizalashtirish", "python", "funksiya", "daftar"]
b = list(filter(None, map(square, x)))
print(b)

def harf_o_k_qil(harf):
    return str(harf).lower()

harf_list = ["W", "s", "t", "E", "a", "R", "k"]
yangi_harflar = list(map(harf_o_k_qil, harf_list))
print(yangi_harflar)
