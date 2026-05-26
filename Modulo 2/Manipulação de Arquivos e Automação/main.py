import os
from datetime import datetime
#linpar a tela
os.system("cls") #clear screen
hora = datetime.now().hour

if hora < 12:
    mensagem = "Bom dia!🌄"
elif hora < 18:
    mensagem = "Boa tarde!☀️"
else:
    mensagem = "Boa noite!🌙"
os.system(f"start cmd /k echo {mensagem}")