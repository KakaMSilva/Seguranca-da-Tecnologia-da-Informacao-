#importar o pyrebase4 no pip
import os.path
import pyrebase
import os
import stat
from datetime import datetime

firebaseConfig = {
    "apiKey": "AIzaSyBvGSdY50djRwYU6wvGZ5w9x7e2ODk9_FU",
    "authDomain": "fir-pucpr-f5710.firebaseapp.com",
    "projectId": "fir-pucpr-f5710",
    "databaseURL": "https://" + "fir-pucpr-f5710" + ".firebaseio.com",
    "storageBucket": "fir-pucpr-f5710.appspot.com",
    "messagingSenderId": "434615721070",
    "appId": "1:434615721070:web:3fab3d8ec71f6f88569a7f",
    "measurementId": "G-1QJKVCTGL9"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")
status = auth.create_user_with_email_and_password(user, password)
status = auth.sign_in_with_email_and_password(user, password)
idToken = status["idToken"]
print("Resultado: ",status)
print("Token: ",idToken)

auth.send_email_verification(idToken)
info = auth.get_account_info(idToken)
users = info["users"]
verifyEmail = users[0]["emailVerified"]

if verifyEmail:

    if os.path.isfile('acesso.txt'):
        os.chmod("acesso.txt", stat.S_IRWXU)

arquivos = open("acesso.txt", 'w')
data_atual = datetime.now()
strLog = "LOG - " + str(data_atual.strftime("%d/%m/%Y %H:%M"))

arquivos.write(strLog)
arquivos.close()
os.chmod("acesso.txt", stat.S_IRUSR)
print("Você está autenticado!\n")

