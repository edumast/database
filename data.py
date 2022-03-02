from module import *
import os.path
info=0
pessoa="d"
def mode_f():
    print("1.new 2.edit 10.remove") 
    mode=input("mode:")
    return mode
def pessoa_f():
    pessoa="pa"
    pessoa=input("pessoa:") 
    return pessoa
def info_f():
    print("1.name 2.age")
    info=input("info:")
    if ( info == 1):
        info="nome"
    if ( info == 2 ):
        info="idade"
    return info
def valor_f():
    valor=input("valor:")
    return valor
def action_f():
    if_pessoa=os.path.isfile("databased/"+pessoa)
    if ( if_pessoa == False ):
        os.system("touch databased/"+pessoa)

    if ( mode == "1" ):
        asp='"'
        end="#end"
        os.system("echo '"+info+"="+asp+valor+asp+" "+end+"' >> databased/"+pessoa)
    if ( mode == "2" ):
        VAL(info,valor,pessoa)
con=True
mesmo=True
while( con == True ):
    mode=mode_f()
    pessoa=pessoa_f()
    mesmo=True
    while( mesmo == True ):
        info=info_f()
        if ( info == "stop" ):
            mesmo=False
        valor=valor_f()
        if ( mesmo == True ):
            action_f()
brek=input("")
