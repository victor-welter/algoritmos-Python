import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
# Configurações de e-mail
remetente_email = 'remetente_email'
remetente_senha = 'remetente_senha'
destinatario_email = 'destinatario_email'

# Conecte-se ao servidor SMTP do Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(remetente_email, remetente_senha)

# Crie a mensagem de e-mail
mensagem = MIMEMultipart()
mensagem['From'] = remetente_email
mensagem['To'] = destinatario_email
mensagem['Subject'] = 'Oi, sou o Python!'
corpo_email = 'Oi, sou o Python!'
mensagem.attach(MIMEText(corpo_email, 'plain'))
texto_do_email = mensagem.as_string()

server.sendmail(remetente_email, destinatario_email, texto_do_email)
print('E-mail enviado com sucesso!')

# Encerre a conexão com o servidor
server.quit()

