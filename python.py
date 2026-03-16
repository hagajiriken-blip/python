import time

class Mobil:
    __mobil = 0

    def __init__ (self,nama,cc):
        self.__nama = nama
        self.__cc = cc


    @property
    def nama(self):
        """The  property."""
        return self.__nama
    
    
    @nama.setter
    def nama(self, value):
        self.__nama = value


Mobil1 = Mobil("Toyota",1000)
print (Mobil1.nama)
Mobil1.nama = "Toyota V2"
print (Mobil1.nama)
 
while True:
    print ("It Works!")
    time.sleep(1) 

