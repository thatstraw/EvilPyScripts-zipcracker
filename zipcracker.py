''' 
Telegram channel: https://t.me/levelivinthackers
Website: https://www.levelivsec.co.zw
authers: Specter Traww
         Black Ninja
         Purple Lane     
'''
from colorama import *
import zipfile
import time

def banner():
    __auther_text__ = Fore.RED +"AUHTERS:" + Fore.RESET
    __auther_1__ = Fore.GREEN + "Purple Lane" + Fore.RESET
    __auther_2__ = Fore.GREEN + "Specter Traww" + Fore.RESET
    __auther_3__ = Fore.GREEN + "Black Ninja" + Fore.RESET
    __filename__ = "\u001b[31m[\u001b[37mv1.0.0\u001b[31m]EvilPy Scripts=>\u001b[32mZip Pass Cracker\u001b[37m"
    __telegram_group__ = "\u001b[31m[\u001b[37mv1.0.0\u001b[31m]TELEGRAM GROUP=>\u001b[36mhttps://t.me/levelivinthackers\u001b[37m"
    __org_name__ = "\u001b[31m[\u001b[37mv1.0.0\u001b[31m]LEVEL IV INT HACKERS=>\u001b[36mhttps://www.levelivsec.co.zw\u001b[37m\n"
    
    harsh = Fore.CYAN + 20 * "#" + Fore.RESET
    harsh_single = "#"
    print(f"{harsh:}")
    print(f"{harsh_single:>}", end ="")
    print(f"   {__auther_text__}", end = " ")
    print(f"{harsh_single:>7}")
    print(f"{harsh_single:>}", end=" ")
    print(f"{harsh_single:>18}")
    print(f"{harsh_single:>}", end ="")
    print(f"   {__auther_1__}", end = " ")
    print(f"{harsh_single:>4}")
    print(f"{harsh_single:>}", end ="")
    print(f"   {__auther_2__}", end = " ")
    print(f"{harsh_single:>2}")
    print(f"{harsh_single:>}", end ="")
    print(f"   {__auther_3__}", end = " ")
    print(f"{harsh_single:>4}")
    print(f"{harsh_single:>}", end=" ")
    print(f"{harsh_single:>18}")
    print(f"{harsh:}")
    print(f"{__filename__}")
    print(f"{__telegram_group__}")
    print(f"{__org_name__}", end="\n")
    print("[\u001b[31mi\u001b[37m]\u001b[32mNote: \u001b[36mThe files will be extracted in the same location with the locked zip file!\u001b[37m")
    
    
def main_menu():
    
    zip_file = input("[\u001b[31m+\u001b[37m]\u001b[33mZip File location: \u001b[37m")
    word_list = input("[\u001b[36m+\u001b[37m]\u001b[33mWordlist File location: \u001b[37m")

    crack_zip(word_list,zip_file)

def crack_zip(wordlist, zipfiles):
    count = 1
    try:
        with zipfile.ZipFile(zipfiles,"r") as file_to_crack:
            with open(wordlist, 'r', encoding="utf-8") as pass_data:
                for pass_entry in pass_data.readlines():
                    pass_wd = pass_entry.encode("utf-8").strip()
                    try:
                        file_to_crack.extractall(pwd=pass_wd)
                        print(f"[\u001b[32m{count}\u001b[37m]\u001b[32mPassword Found!:\u001b[36m {pass_entry} \u001b[32m:OK\u001b[37m")
                        print("[\u001b[31mi\u001b[37m]\u001b[32mZip file successifully extracted!\u001b[37m")
                        print("[\u001b[31mi\u001b[37m]\u001b[36mtype \u001b[31m$> \u001b[32mls \u001b[36mto view the files extracted if they're on the same dir with the this script!\u001b[37m")
                        break
                    except:
                        print(f'[\u001b[36m{count}\u001b[37m]Trying \u001b[31m{pass_entry} =>\u001b[37mWrong Password!')  
                        count += 1 
                        pass 
    except FileNotFoundError as fnf_error:
        print("[\u001b[31m!\u001b[37m]" + str(fnf_error))   
        print("[\u001b[31m!\u001b[37m]Please make sure, you type the correct filename or path/location.")             
        
banner()
main_menu()





