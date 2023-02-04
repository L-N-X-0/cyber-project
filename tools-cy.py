try:
    import os
    import time
    import requests

except ImportError:
	os.system('pip3 install requests')
	os.system('pip3 install time')

else:
    import os
    import time
    import requests

# Color --------
B='\033[0;30m' # Black
R='\033[1;31m' # Red
G='\033[1;32m' # Green
Y='\033[1;33m' # Yellow
Bl='\033[1;34m' # Blue
P='\033[1;35m' # Purple
C='\033[1;36m' # Cyan
W='\033[1;37m' # Whit
# End Color -------

os.system('clear')

# Banner ---------
def banner():
    print(Bl+'''
  ____      _                     _            _    
 / ___|   _| |__   ___ _ __    __| | __ _ _ __| | __
| |  | | | | '_ \ / _ \ '__|  / _` |/ _` | '__| |/ /
| |__| |_| | |_) |  __/ |    | (_| | (_| | |  |   < 
 \____\__, |_.__/ \___|_|     \__,_|\__,_|_|  |_|\_\ 
      |___/                                                                                                                                 
    ''')
    print(f'{Y}~ By Cyber Dark ~ {Bl}v1.7')
    print(Y+'~ Telegram : @CYcode')
    print(Y+'~ Facebook : @CyberDarkCrew')
    print(Y+'~ Github   : @CyberDarkCrew')
    print(Y+'~ Email    : Cyb3rD4rk@protonmail.com')
    
banner()

# EndBanner -----------
print(' ')


# Select Tool ----------

print(G+'Choose a Tools To Install')
print(G+' ')
print(G+'[00] - Update Tools')
print(G+'[01] - Update Termux or Linux')
print(G+f'[02] - Send Message To Admin {Bl}[New]')
print(G+'[03] - About')
print(G+'[04] - Remove Tool')
print(G+'[05] - Exit')
print(G+' ')
print(G+f'[1] - Text Encryption {R}[Pro]')
print(G+f'[2] - Available Users - TikTok {W}[Free]')
print(G+f'[3] - DDos Attack {W}[Free]')
print(G+f'[4] - Spam Mail {R}[Pro]')
print(G+f'[5] - Brute Force - FB {W}[Free]')
print(G+f'[6] - Check Hash Type {W}[Free]')
print(G+f'[7] - Email Checker {W}[Free]')
print(G+' ')

def run_app():
    # Login -------------------
    userlogin = "daddy"
    passlogin = "root"

    select = input(G+'Select Tool :')


    # 00 -------------------
    if select == '00':
        os.system(f'rm -r tools-cy.py')
        print(Y+'\nLoading Please Wait...\n')
        os.system('wget https://example.com/python/tools-cy.py')
        print(G+'\n~ Done Updating Tools ~')
        time.sleep(3.0)
        run_app()

    # 01 -------------------
    elif select == '01':
        os.system('clear')
        print(Y+'\nPlease Select...')
        print(' ')
        print(Y+'[1] - Termux')
        print(Y+'[2] - Kali Linux')
        print(Y+'[3] - Wifislax')

        kaliortermux = input(G+'\nPlease Select :')
        
        if kaliortermux == '1':
            print(G+'updating...')
            os.system('pkg update')
            print(G+'\n~ Done Updating ~')
            time.sleep(3.0)
            run_app()

        elif kaliortermux == '2':
            print(G+'\nupdating...')
            os.system('sudo apt-get update')
            print(G+'\n~ Done Updating ~')
            time.sleep(3.0)
            run_app()
        
        elif kaliortermux == '3':
            print(G+'\nupdating...')
            os.system('sudo slapt-get --update')
        
        else:
            print(R+'\nError Selected Please Try Again')


    # 02 -------------------
    elif select == '02':
        os.system('clear')
        yname = input(W+"Your Name :")
        msg = input(W+"\nEnter Message :")
        r = requests.Session()
        print(G+f"\n Done Send Message , Thank You{Y} {yname}")
        tlg = (f'''https://api.telegram.org/bot5037357078:AAGCp3gYY1pzrOFBBCDyyNBSB3V8yPsOyCc/sendMessage?chat_id=1411796920&text= Name : {yname} \nMsg : {msg}''')
        i = requests.post(tlg)
        
        
    # 05 -------------------
    elif select == '05':
        print(Y+f'\nThank You For Using {G}./Mr.Dark{Y}')
        exit()
        
    # 03 -------------------
    elif select == '03':
        os.system('clear')
        print(W+'''\n
            ~ who are we ! ~
    Cyber ​​Dark is a team of programmers
        and black hat hacking
        ''')
        print(R+'''
    ~ Cyber Dark Crew ~
        Telegram : 
            Mr.Dark : @L_N_X_0
            Channel : @CYcode
        ''')

    # 04 -------------------
    elif select == '04':
        os.system('clear')
        print(R+'\nPlease Enter File Name')
        remove = input('\nFile Name :')
        os.system(f'rm -r {remove}')  
        print(G+'\n~ Done Delete File ~')


    # 1 -------------------
    elif select == '1':
        os.system('clear')
        print(Bl+f''' 
        Please Select Login Or SignUp

        {Y}[1] {Bl}- Login
        {Y}[2] {Bl}- SignUp
        ''')

        freeorbasic = input(G+"Select :")

        if freeorbasic == '2':
            print(G+f'\n Talk to the team and ask them to give you a private account \n Telegram : {Y}@L_N_X_0')

        elif freeorbasic == '1':
            os.system('clear')

            user = input(W+"\nUsername :")
            passwd = input(W+"Password :")

            if user == userlogin and passwd == passlogin:
                print(Y+"\n Hello " + G+user)
                time.sleep(1.0)
                print(Y+'\nLoading Please Wait...\n')
                os.system('rm -r hash-encryption')
                os.system('git clone https://github.com/CyberDarkCrew/hash-encryption.git')
                print(G+'\n~ Installation finished ~')
            else:
                print(R+"\nError Password Or UserName")
                time.sleep(3.0)
                run_app()

        else:
            print(R+"Error Selected Please Try Again")
            time.sleep(3.0)
            run_app()

    # 2 -------------------
    elif select == '2':
        print(Y+'\nLoading Please Wait...\n')
        os.system('rm -r users-tiktok')
        os.system('git clone https://github.com/CyberDarkCrew/users-tiktok.git')
        print(G+'\n~ Installation finished ~')

    # 3 -------------------
    elif select == '3':
        print(Y+'\nLoading Please Wait...\n')
        os.system('rm -r ddos-attack')
        os.system('git clone https://github.com/CyberDarkCrew/ddos-attack.git')
        print(G+'\n~ Installation finished ~')

    # 4 -------------------
    elif select == '4':
        os.system('clear')
        print(Bl+f''' 
        Please Select Login Or SignUp

        {Y}[1] {Bl}- Login
        {Y}[2] {Bl}- SignUp
        ''')

        freeorbasic = input(G+"Select :")

        if freeorbasic == '2':
            print(G+f'\n Talk to the team and ask them to give you a private account \n Telegram : {Y}@L_N_X_0')

        elif freeorbasic == '1':
            os.system('clear')

            user = input(W+"\nUsername :")
            passwd = input(W+"Password :")

            if user == userlogin and passwd == passlogin:
                print(Y+"\n Hello " + G+user)
                time.sleep(1.0)
                print(Y+'\nLoading Please Wait...\n')
                os.system('rm -r spam-mail')
                os.system('git clone https://github.com/CyberDarkCrew/spam-mail.git')
                print(G+'\n~ Installation finished ~')

            else:
                print(R+"\nError Password Or UserName")
                time.sleep(3.0)
                run_app()

        else:
            print(R+"Error Selected Please Try Again")
            time.sleep(3.0)
            run_app()

    # 5 ------------------- 
    elif select == '5':
        print(Y+'\nLoading Please Wait...\n')
        os.system('rm -r guess-password')
        os.system('git clone https://github.com/CyberDarkCrew/guess-password.git')
        print(G+'\n~ Installation finished ~\nFilename : guess-password')

    # 6 -------------------
    elif select == '6':
        print(Y+'\nLoading Please Wait...\n')
        os.system('rm -r check-hash')
        os.system('git clone https://github.com/CyberDarkCrew/check-hash.git')
        print(G+'\n~ Installation finished ~\nFilename : check-hash')

    # 7 -------------------
    elif select == '7':
        print(Y+'\nLoading Please Wait...\n')
        os.system('rm -r cy-checker')
        os.system('git clone https://github.com/CyberDarkCrew/cy-checker')
        print(G+'\n~ Installation finished ~\nFilename : cy-chekcer')


    # Else --------------------
    else:
        print(R+'\n Error Please Selected Try Again ...')
        time.sleep(3.0)
        run_app()

run_app()