from module import *
import os.path
info=0
pessoa="d"
print(GREEN)
def mode_f():
    print(GREEN)
    print("1.new 2.edit 3.check")
    mode=input("mode:")
    return mode
def pessoa_f():
    pessoa="pa"
    pessoa=input("pessoa:") 
    return pessoa
def info_f():
    print("1.name 2.age")
    info=input("info:")
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
    if ( mode == "3" ):
        print("")
        print(YELLOW)
        os.system("cat databased/"+pessoa)
        print()
        print("")
        not_rest=False
con=True
mesmo=True
not_rest=False
while( con == True ):
    mode=mode_f()
    if ( mode == "3" ):
        not_rest=True
    pessoa=pessoa_f()
    mesmo=True
    while( mesmo == True ):
        if ( not_rest == False ):
            info=info_f()
            if ( info == 1):
                info="nome"
            if ( info == 2 ):
                info="idade"
            if ( info == "stop" ):
                mesmo=False
            valor=valor_f()
        if ( mesmo == True ):
            action_f()
            not_rest=False
            mesmo=False

