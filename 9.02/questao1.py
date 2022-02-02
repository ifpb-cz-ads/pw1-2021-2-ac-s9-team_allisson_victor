#1) Adicione os atributos tamanho e marca à classe Televisão. Crie dois objetos Televisão e atribua tamanhos 
# e marcas diferentes. Depois, imprima o valor desses atributos de forma a confirmar a independência dos 
# valores de cada instância (objeto).
#classe  Televisão :
#     def  __init__ ( self ):
#           próprio . for  =  Falso
#           próprio . canal  =  2
#     def  muda_canal_para_baixo ( self ):
#           próprio . canal  -=  1
#     def  muda_canal_para_cima ( self ):
#           próprio . canal  +=  1
#tv  =  Televisão ()
#televisão . muda_canal_para_cima ()
#televisão . muda_canal_para_cima ()
#imprimir ( tv . canal )
#televisão . muda_canal_para_baixo ()
#imprimir ( tv . canal )

class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 20
        self.marca = "Ching-Ling"


tv = Televisão()
tv.tamanho = 27
tv.marca = "LongDang"
tv_sala = Televisão()
tv_sala.tamanho = 52
tv_sala.marca = "XangLa"

print(f"tv tamanho={tv.tamanho} marca={tv.marca}")
print(f"tv_sala tamanho={tv_sala.tamanho} marca={tv_sala.marca}")