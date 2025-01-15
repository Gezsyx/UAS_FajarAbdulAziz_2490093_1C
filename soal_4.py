class Buah:
    def __init__(self):
        self.nama = []
        self.warna = []
        self.rasa = []

    def setnama(self,item):
        self.nama = item
    def setwarna(self,item2):
        self.warna = item2
    def setrasa(self,item3):
        self.rasa = item3


    def information(self):
        return f"Nama Buah : {self.nama} | Warna Buah : {self.warna} | Rasa Buah : {self.rasa}"
    
buah1 = Buah()
buah1.setnama("Apel")
buah1.setwarna("Merah")
buah1.setrasa("Manis")
print(buah1.information())
buah2 = Buah()
buah2.setnama(" Sirsak")
buah2.setwarna("Putih")
buah2.setrasa("Asam")
print(buah2.information())

