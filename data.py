#!/usr/bin/env python3
from module import *
import os.path
info=0
pessoa="d"
print(GREEN)
BOLD()
def mode_f():
    BOLD()
    print(GREEN)
    print("1.new 2.edit 3.check 4.remove info 15.remove profile")
    mode=input("mode:")
    return mode
def pessoa_f():
    pessoa_wh=True
    while ( pessoa_wh == True ):
        pessoa="pa"
        pessoa=input("pessoa:")
        if ( pessoa == "list" ):
            os.system("ls databased")
            print(GREEN)
            BOLD()
        else:
            pessoa_wh=False
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
    if ( mode == "15" ):
        print(RED)
        confirm=input("True or False?")
        if ( confirm == "True" ):
            os.system("rm -rf databased/"+pessoa)
            print("usr:"+pessoa+" removed")
            print(GREEN)


    if ( mode == "4" ):
        os.system("sed -i '/"+info+"/d' databased/"+pessoa)
    if ( mode == "5" ):
        os.system("cp -r databased ~")
        not_rest=False
con=True
mesmo=True
not_rest=False
mes_p=False
while( con == True ):
    valor_b=True
    if ( mes_p == False ):
        pessoa=pessoa_f()
        mes_p=True
    mode=mode_f()
    if ( mode == "exit" ):
        mes_p=False
    if ( mode != "exit" ):
        if ( mode == "3" ):
            not_rest=True
        if ( mode == "4" ):
            valor_b=False
        if ( mode == "5" ):
            not_rest=True
        if ( mode == "15" ):
            not_rest=True
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
                if ( mesmo == True ):
                    if ( valor_b == True ):
                        valor=valor_f()
            if ( mesmo == True ):
                action_f()
                not_rest=False
                if ( mode == "15" ):
                    mes_p=False
                    mesmo=False
                    break
                if ( mode == "3" ):
                    break
                if ( mode == "5" ):
                    break
            

