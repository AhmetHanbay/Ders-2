#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=5
b=6
print(a+b)


# In[2]:


a=6
b=5
print(a-b)


# In[3]:


a=6
b=5
print(a*b)


# In[4]:


a=6
b=5
print(a/b)


# In[5]:


a=6
b=5
print(a//b)


# In[6]:


a=6
b=5
print(a%b)


# In[7]:


a=4
b=2
print(a**b)


# In[8]:


a=9
b=4
a==b


# In[9]:


a=9
b=4
a!=b


# In[10]:


a=9
b=4
a>b


# In[11]:


a=9
b=4
a>=b


# In[12]:


a=9
b=4
a<b


# In[13]:


a=9
b=4
a<=b


# In[23]:


a=3
b=6
print(a)
print(b)
a = a + b
print(a)


# In[25]:


a=7
b=4
print(a&b)


# In[26]:


a=8
b=4
print(a&b)


# In[28]:


a = input("birinci sayıyı gir=")
b = input("ikinci sayıyı gir=")


# In[29]:


print(int(a)+int(b))


# In[30]:


I = input("akımı giriniz=")
R = input("direnci giriniz=")


# In[32]:


print(int(I)*int(R))


# In[33]:


a = input("kısa kenarı giriniz=")
b = input("uzun kenarı giriniz=")


# In[38]:


print("Alan=",int(a)*int(b))
print("Çevre=",2*int(a)+2*int(b))


# In[39]:


r = input("Yarıcapı giriniz=")
pi = 3.14
print("Çemberin Alanı=",pi*int(r)*int(r))


# In[41]:


OgrNot = input("Yüzlük notu giriniz=")


# In[45]:


print("5'lik karsılıgı = ", int(OgrNot)/20)


# In[46]:


Fiyat = int(input("Fiyat="))
KDV = int(input("KDV"))
print("KDV'Lİ fiyat = ",Fiyat + Fiyat * KDV/100)
#      50    + 50 * 18/100


# In[48]:


Fiyat = int(input("Alış Fiyatı = "))
KDV = int(input("KDV Oranı = "))
Vergi = int(input("Vergi Oranı = "))
print("KDV'li fiyat = ",Fiyat + Fiyat * KDV/100 + Fiyat * Vergi/100)
#        50  +   50 * 18/100           


# In[53]:


sayı = int(input("üç basamaklı bir sayı giriniz = "))


# In[55]:


a = sayı//100
b = int(int(sayı-a*100)/10)
c = sayı % 10
print("yüzler=",a,"onlar=",b,"birler=",c,)
print(str(c)+str(b)+str(a))


# In[10]:


sayi = int(input("Gün sayısını giriniz = "))
print("yil = ",sayi//365)
print("ay = ",sayi//30)


# In[14]:


var = 100
if (var==100):
    print("Değişken değeri 100 dür")
print("Görüşürüz")


# In[23]:


var = 104
if (var != 100) :
    print ("Değişken değeri 100 dür")


# In[27]:


Fiyat = int(input("Alış Fiyatı = "))
KDV = int(input("KDV oranı = "))
Vergi =int(input("Vergi oranı = "))
print("KDV'li Fiyat = ",Fiyat + Fiyat * KDV/100 + Fiyat * Vergi/100)


# In[2]:


x = 0
y = ["10",5,"abc",12]
sonuc = x in y
print (sonuc)


# In[4]:


x = 0
y = ["10","abc",0]
sonuc = x in y
print(sonuc)


# In[6]:


x = 0
y = ["10","abc",0]
sonuc = x not in y
print(sonuc)


# In[8]:


x = 0
y = ["10","abc",5]
sonuc = x not in y
print(sonuc)


# In[10]:


x = 6
y = 0
sonuc = x is y 
print(sonuc)


# In[12]:


x = 6
y = 6
sonuc = x is y
print(sonuc)


# In[14]:


x = 6 
y = 6 
sonuc = x == y
print(sonuc)


# In[20]:


x = 6
y = 6
sonuc = x is not y
print(sonuc)


# In[22]:


sayi = int(input("Bir sayı giriniz =" ))
if sayi > 0 :
    print("pozitif")

if sayi < 0 :
    print("negatif")


# In[25]:


sayi = int(input("Bir sayı giriniz ="))
if sayi > 0 :
    print("pozitif")
if sayi < 0 : 
        print("negatif")


# In[2]:


sayi = int(input("Bir sayı giriniz ="))
if sayi > 0 :
    print("pozitif")
    if sayi < 0 : 
        print("negatif")
    


# In[6]:


sayi = int(input("Bir sayı giriniz"))
if sayi < 0 :
    print("negatif")
    if sayi > 0 :
        print("pozitif")


# In[10]:


Fiyat = int(input("Alış fiyati = "))
KDV = int (input("KDV oranı = "))
Vergi =int(input("Vergi oranı = "))
print("KDV'li Fiyat =" , Fiyat + Fiyat * KDV/100 + Fiyat * Vergi/100)


# In[8]:


I = input("Akımı Giriniz = ")
R = input("Direnç Giriniz = ")
print(int(I)*int(R))


# In[4]:


sayi = int(input("Bir sayı giriniz ="))
if sayi > 0 :
    print("pozitif")
    if sayi < 0 :
        print("negatif")
    


# In[35]:


sayi = int(input("Bir sayi giriniz="))
if sayi > 0 :
    print("pozitif")
else :
 print("negatif")


# In[15]:


sayi = int(input("Bir sayi giriniz ="))
if sayi >0 :
    print("pozitif")
else : 
    print("negatif")


# In[19]:


vize = int(input("Vize notunu giriniz ="))
final = int(input("Final notunu giriniz="))
Not = vize * 0.4 + final * 0.6
print(Not)


# In[20]:


vize = int(input("Vize notunu giriniz"))
final = int(input("Final notunu giriniz="))
Not = vize * 0.4 + final * 0.6 
if Not>60:
    print("Geçti")
else:
    print("Kaldı")


# In[22]:


vize = int(input("Vize notunu giriniz="))
final = int(input("Final notunu giriniz"))
Not = vize * 0.4 + final * 0.6
if Not>60:
    print("Geçti")
else:
    print("Kaldı")
    


# In[23]:


vize = int(input("Vize notunu giriniz="))
final= int(input("Final notunu giriniz="))
Not = vize * 0.4 + final * 0.6
if Not>60:
    print("Not=",Not,"Geçti")
else:
    print("Not=",Not,"Kaldı")


# In[24]:


sayi = int(input("sayi giriniz="))
kalan = sayi % 6
if kalan == 0:
    print("Sayı altıya tam bölünüyor")
else:
    print("Sayı altıya tam bölünmüyor")


# In[28]:


sayi =int(input("Sayı giriniz="))
kalan = sayi % 6
if kalan == 0:
    print("Sayı altıya tam bölünüyor")
else:
    print("Sayı altıya tam bölünmez")

    


# In[31]:


sayi = int(input("Bir sayi giriniz="))
kalan1 = sayi % 2
kalan2 = sayi % 3
if kalan1==0 and kalan2==0:
    print("Sayı altıya tam bölünüyor")
else:
    print("Sayı altıya tam bölünmüyor")


# In[45]:


sayi = int(input("Forma no giriniz = "))
if sayi >0 :
    print("morutan")


# In[49]:


sayi = int(input("Bir sayı giriniz="))
kalan1 = sayi % 2
kalan2 = sayi % 3
if kalan1==0 and kalan2==0:
    print("sayı altıya tam bölünüyor")
else:
    print("sayı altıya tam bölünmüyor")


# In[58]:


sayı = int(input("sayı giriniz="))
kalan1 = sayi % 2
kalan2 = sayi % 3 
if (kalan1==0) & (kalan2==0):
    print("sayi altıya tam bölünüyor")
else:
        print("sayi altıya tam bölünmüyor")


# In[62]:


sayı = int(input("sayi giriniz="))
kalan1 = sayi % 2
kalan2 = sayi % 3 
if (kalan1==0) & (kalan2==0):
    print("sayı altıya tam bölünüyor")
else:
    print("sayı altıya tam bölünmüyor")


# In[2]:


sayi = int(input("Bir sayı giriniz = "))
kalan = sayi % 6 
if kalan==0:
    print("Sayı altıya tam bölünür")
else:
    print("Sayı altıya tam bölünmez")


# In[5]:


vize = int(input("Vize notunu giriniz = "))
final = int(input("Final notunu giriniz = "))
Not = vize * 0.4 + final * 0.6
if Not>60:
           print("Geçti")
else:
           print("Kaldı")


# In[7]:


sayi = int(input("Bir sayı giriniz = "))
if sayi>0:
    print("Pozitif")
else:
    print("Negatif")


# In[11]:


Fiyat = int(input("Alış fiyatı giriniz = "))
KDV = int(input("KDV oranı giriniz = "))
Vergi = int(input("Vergi oranı giriniz = "))
print("KDV'li fiyat = " , Fiyat + Fiyat * KDV / 100 + Fiyat * Vergi / 100)

