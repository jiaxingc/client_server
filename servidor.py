from threading import Thread
from socket import *

list_escolas=["Imperatriz Leopoldinense","Estação Primeira de Mangueira","Acadêmicos do Salgueiro","São Clemente","Unidos do Viradouro","Beija-Flor de Nilópolis",
"Paraíso do Tuiuti","Portela","Mocidade Independente de Padre Miguel","Unidos da Tijuca","Acadêmicos do Grande Rio","Unidos de Vila Isabel"]


        

def atende (conn, cliente):
        while True:
                data = conn.recv (8192)
                print(data)
                if not data or len(data) == 0:
                        break

                print (str(cliente)+"recebeu mensagem "+data.decode("utf-8") )
             
                
        
                # conn.send (str.encode ("Eu sei que voce me mandou "+data.decode("utf-8") , "UTF-8"))

        print ("Fim da conexao com "+str(cliente))

        conn.close
        

s = socket ()

host = "0.0.0.0"
porta = 8192
s.bind ((host, porta))
s.listen (10)
nthr = 0

while True:
        print("Aguarde conexão de um cliente")
        (conn, cliente) = s.accept ()
