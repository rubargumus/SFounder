#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import requests
import time 
try : 
    os.system("cls")

    banner = """
███╗   ██╗██╗   ██╗██╗  ██╗███████╗    ████████╗ ██████╗  ██████╗ ██╗         ██╗  ██╗██╗████████╗    
████╗  ██║██║   ██║██║ ██╔╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██║ ██╔╝██║╚══██╔══╝    
██╔██╗ ██║██║   ██║█████╔╝ █████╗         ██║   ██║   ██║██║   ██║██║         █████╔╝ ██║   ██║       
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝         ██║   ██║   ██║██║   ██║██║         ██╔═██╗ ██║   ██║       
██║ ╚████║╚██████╔╝██║  ██╗███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗    ██║  ██╗██║   ██║       
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝   ╚═╝       
                                                                                            
"""
			
    print(banner)
    print("-"*80)
    print("Example : site.net Or www.site.net")
    print("-"*80)
    url = input("URL? : ")
    print("-"*70)
    root = input("Does this website use http or https? ? Y/N Default=Auto : ")
    print("-"*80)
    if root == "y" or "Y" :
	    new = "https://"+url
    elif root == "n" or "N":
	    new = "http://"	+ url
    else :
        new = "http://" + url 

    liste  = ['/alfa.php','/c99.php','/fucked.php',"/adminer.php",'/webroot','/madspot.php','/mad.php','/404.php','/anon.php','/anonymous.php','/shell.php','/sh3ll.php','/madspotshell.php','/b374k.php','/c100.php','/priv8.php','/private.php','/cp.php','/cpbrute.php','/themes/404/404.php','/templates/atomic/index.php','/templates/beez5/index.php','/hacked.php','/r57.php','/wso.php','/WSO.php','/wso24.php','/wso26.php','/wso404.php','/sym.php','/symsa2.php','/sym3.php','/whmcs.php','/whmcskiller.php','/cracker.php','/1.php','/2.php','/sql.php','/gaza.php','/database.php','/a.php','/d.php','/dz.php','/cpanel.php','/system.php','/um3r.php','/zone-h.php','/c22.php','/root.php','/r00t.php','/doom.php','/dam.php','/killer.php','/user.php','/wp-content/plugins/disqus-comment-system/disqus.php','/cpn.php','/shelled.php','/uploader.php','/up.php','/xd.php','/d00.php','/h4xor.php','/tmp/mad.php','/tmp/1.php','/wp-content/plugins/akismet/akismet.php','/images/stories/w.php','/w.php','/downloads/dom.php','/templates/ja-helio-farsi/index.php','/wp-admin/m4d.php','/d.php']
    bulunanlar = []
    for i in liste :
	    req = new + i 
	    response = requests.get(req)
	    if response.status_code == 404 :
		    print("Not Found : {}".format(req))
	    elif response.status_code == 403 :
			    print("ERROR (POSSIBLY FIREWALL) {}".format(response.status_code))
	    else :
		    print("""
------------------------------------------------------------
    Found ==> {}
------------------------------------------------------------
""".format(req))	
		    bulunanlar.append(req)
    os.system("cls")
    print("-"*70)
    if bulunanlar == [] :
	    print(banner)
	    print("-"*80)
	    print("Shell Not Found")
    else :
	    print(banner)
	    print("-"*80)
	    print("-"*8 ,"FOUND","-"*8)
	    for i in bulunanlar :
		    print("CONCLUSION : {}".format(i))
except :
    os.system("cls")
    print("""
    -----An Error Encountered----- 

Please Try Again Under The Rules Below

URL ==> Enter www.examplesite.com or examplesite.com
Note ==> No http or https at the beginning, no / at the end
""")
    time.sleep(10)

finally : 
    print("Goodbye .d Nice Hacking")
