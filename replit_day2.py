#Combine string and variables into a simple automatic sentence
foodName=input("Name a food:")
type_of_plant=input("Name a type of plant:")
method=input("Name a method of cooking:")
wordA=input("A word to describe burned food:")
item=input("Mention a household item:")
print()
print("""Menu""")
print()
print(method,foodName,"with",wordA, type_of_plant,"on a bunch of",item)

print()

#Changing the color of string
print(""" Selamat Datang di Pendaftaran untuk Permintaan Langit. Silahkan Mengisi Jawaban 
Pertanyaan yang akan Kami Berikan untuk Memproses Permintaan Anda.""")
print("ISI DATA")
name=input("Nama:")
asal=input("Asal:")
permintaan=input("Sebutkan permintaan anda:")
waktu=input("Kapan harus diwujudkan:")
print("\033[31m", "Simsalabim Abracadabra Sontoloyo")
print("\033[0m","Sang pemimpi, Tuan", name ,"asal", asal,
      "dalam kurun waktu",waktu, "ingin", permintaan)