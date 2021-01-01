#!user/bin/python3
print("""
                '/¯¯\                           /¯¯\  \n
               / /:::\ \                       / /:::\ \  \n
             / /:::::::\ \      )\  )\       / /:::::::\ \  \n
           / /:::::::::::\ \   / /-/ /     / /:::::::::::\ \  \n
         / /:::::::::::::::\ \|(,\/, )\  /  /::::::::::::::\ \  \n
       / /:::::::::::::::::/ / /#/ ,) |/   \::::::::::::::::\ \  \n
     / /:::::::::::::::::/  ( *¯* )|  ; /\  \::::::::::::::::\ \  \n
   / /:::::::::::::::::/, /¯\|¯¯|/ ,'¯\   \  \::::::::::::::::\ \  \n
  |  |:::::::::::::::/'/'/'/'\/| /:::/'/'/'/'\|   |  |::::::::::::::::|  | \n
   \  \:::::::::::::'v'v'v'v'  |::::'v'v'v'v'  /  /::::::::::::::::/  /  \n
     \  \::::::::::::::::\ |\ \::::/    / /  /::::::::::::::::/  /  \n
       \  \:::::::::::::::/¯¯  /¯¯  \||   |:::::::::::::::/  /  \n
         \  \:::::::::::/     /'/      /, '\  \:::::::::::::/  /  \n
           \  \:::::::::\     \\      \:\   \  \:::::::::/  /  \n
            \  \:::::/'/'/'/'/\|/'/'/'/'/\|::|   |\ '\::::::/  /  \n
              \  \::'v'v'v'v' 'v'v'v'v' /::/  /   \ '\:::/  /  \n
                \  \   /           |::|   |      |\ \   /  \n
                   '\/             \::\   \__/  |  \/  \n
                                    \;;\____ /§Ãž \n
""")

def main():
	n = input("1- Network scanner\n2- Vulnerabilities Detection\n3- Exploit\n\nPlease enter a number : ")

if  n == '1':
	nmap()

def nmap():
	print("-----------Welcome to the Network Scanner----------")
	print("---------------------------------------------------")
	ip = input("\nPlease enter the IP addresse:")
	sc.scan(ip , '1-1024')
	print(sc.scaninfo())
	print(nm['127.0.0']['tcp'].keys())
	
if n == '2':
	vuln()

def vuln():
    print("-----------Welcome to the Vulnerabilities Detection----------")
	print("-------------------------------------------------------------")
	ip = input("\nPlease enter the IP addresse:")
	print(os.systeme('nmap -sV --script=vulscan.nse ' +ip))

if n == '3':
	os.system('msfconsole')
	else:
		print("Please choose a nulber between 1 and 3")



if __name__ == "__main__":
	main()
