from socket import  *
import pickle
s = socket ()


host = "127.0.0.1"
porta = 8192
s.connect((host, porta))



    
     
while True:
   
    data=input("inserir o nome  da escola : ")
    
    if (data == ""):
        break
    print (data)

    data=str.encode (data, "UTF-8")
    

    s.send(data)
    

    data = s.recv (8192)
  
   
    print ("retornou mensagem correda",data.decode("utf-8"))
  
    

s.close ()

