import random
import string

rakamlar="0123456789"
semboller=string.punctuation
kucuk_harf=string.ascii_lowercase
buyuk_harfler=string.ascii_uppercase

karakterler=[rakamlar,semboller,kucuk_harf,buyuk_harfler]

sifre=""

for i in range(2):
    sifre+=karakterler[0][random.randint(0,9)]
for i in range(2):
    sifre+=karakterler[1][random.randint(0,9)]
for i in range(2):
    sifre+=karakterler[2][random.randint(0,9)]
for i in range(2):
    sifre+=karakterler[3][random.randint(0,9)]

    print(sifre)