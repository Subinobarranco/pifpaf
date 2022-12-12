import cliente, server
x=input("1 para cliente ou 0 para servidor")
if(x==1):
    cli = cliente.main("localhost")
else:
    cli = cliente.main('localhost')
