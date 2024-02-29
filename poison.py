#!/usr/bin/python3
import os
import time

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

os.system("clear")
time.sleep(1)
print("\033[1;33m[\033[0;37m+\033[1;33m] Bem Vindo")
time.sleep(2)
os.system("clear")
print("\033[32m[\033[0;37m+\033[32m] Carregando...")
time.sleep(3)
os.system("clear")
time.sleep(2)
print("\033[1;31m      NO!                          MNO!")
print("     MNO!!         [NBK]          MNNOO!")
print("   MMNO!                           MNNOO!!")
print(" MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!!")
print(" !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO!")
print("       ! MMMMMMMMMMMMMPPPPOOOOIII! !")
print("        MMMMMMMMMMMMPPPPPOOOOOOII!!")
print("        MMMMMOOOOOOPPPPPPPPOOOOMII!")
print("        MMMMM..    OPPMMP    .,OMI!")
print("        MMMM::   o.,OPMP,.o   ::I!!")
print("          NNM:::.,,OOPM!P,.::::!!")
print("\033[1;34m         MMNNNNNOOOOPMO!!IIPPO!!O!")
print("         MMMMMNNNNOO:!!:!!IPPPPOO!")
print("          MMMMMNNOOMMNNIIIPPPOO!!")
print("             MMMONNMMNNNIIIOO!")
print("           MN MOMMMNNNIIIIIO! OO")
print("          MNO! IiiiiiiiiiiiI OOOO")
print("     NNN.MNO!   O!!!!!!!!!O   OONO NO!")
print("    MNNNNNO!    OOOOOOOOOOO    MMNNON!")
print("      MNNNNO!    PPPPPPPPP    MMNON!")
print("         OO!                   ON!")
print("                                                            ")
print("\033[1;32md8888b.  .d88b.  d888888b .d8888.  .d88b.  d8b   db")
print("88  `8D .8P  Y8.   `88'   88'  YP .8P  Y8. 888o  88")
print("88oodD' 88    88    88    `8bo.   88    88 88V8o 88")
print("\033[0;36m88~~~   88    88    88      `Y8b. 88    88 88 V8o88")
print("88      `8b  d8'   .88.   db   8D `8b  d8' 88  V888")
print("88       `Y88P'  Y888888P `8888Y'  `Y88P'  VP   V8P")


time.sleep(2)
print("                                                      ")
print ("\033[32m[\033[0;31mAutor\033[32m]: \033[0;35mRicky$")
print("\033[0;36mv4.3 - Beta")
print("                                                      ")
print("\033[0;37mSistema:")
print("                                                      ")
print("\033[1;33m [\033[0;37m1\033[1;33m] Atualizar Termux     [\033[0;37m4\033[1;33m] Instalar wget ")
print(" [\033[0;37m2\033[1;33m] Instalar nmap        [\033[0;37m5\033[1;33m] Instalar git  ")
print(" [\033[0;37m3\033[1;33m] Instalar sqlmap      [\033[0;37m6\033[1;33m] Atualizar python3  ")
print("                                                      ")
print("\033[0;37mFerramentas:")
print("                                                      ")
print("\033[1;33m [\033[0;37m7\033[1;33m] GhostTrack           [\033[0;37m10\033[1;33m] Cam Finder   ")
print(" [\033[0;37m8\033[1;33m] Infect Android       [\033[0;37m11\033[1;33m] User Finder  ")
print(" [\033[0;37m9\033[1;33m] PyPhisher            [\033[0;37m12\033[1;33m] Zphisher         ")
print("                          [\033[0;37m00\033[1;33m] Sair     ")
print("                                                      ")
escolha = False

while escolha == False:
    nivel = int(input("\033[1;31m> \033[0;37mQual opção: "))
    if (nivel == 1):
        os.system("pkg update && pkg upgrade")
    
    elif (nivel == 2):
        os.system("pkg install nmap")  
        
    elif (nivel == 3):
        os.system("https://github.com/sqlmapproject/sqlmap")    
        
    elif (nivel == 4):
        os.system("pkg install wget")
        
    elif (nivel == 5):
        os.system("pkg install git")
        
    elif (nivel == 6):
        os.system("pkg update python3 && pkg upgrade python3")
        
    elif (nivel == 7):
        os.system("git clone https://github.com/HunxByts/GhostTrack.git")
        
    elif (nivel == 8):
        os.system("git clone https://github.com/noob-hackers/infect")    
        
    elif (nivel == 9):
        os.system("git clone git clone https://github.com/KasRoudra/PyPhisher")  
        
    elif (nivel == 10):
        os.system("git clone https://github.com/member87/cam-finder/")
        
    elif (nivel == 11):
        os.system("git clone https://github.com/mishakorzik/UserFinder")
        
    elif (nivel==12):
        os.system("clear")
        print("\033[0;32m[+] Instalando Zphisher")
        time.sleep(2)
        print("\033[0;34m[+] Ao finalizar o Zphisher, execute-o com: Zphisher")
        time.sleep(3)
        os.system("pkg install zphisher")
    
    elif (nivel == 00):
        os.system("clear")
        print("\033[1;35m[\033[0;37m+\033[1;35m] Obrigado por usar =D")
        time.sleep(3)
        os.system("clear")
        exit()
        os.system("clear")                     