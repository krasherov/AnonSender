import smtplib
from email.mime.text import MIMEText
print('''
░█████╗░███╗░░██╗░█████╗░███╗░░██╗░██████╗███████╗███╗░░██╗██████╗░███████╗██████╗░
██╔══██╗████╗░██║██╔══██╗████╗░██║██╔════╝██╔════╝████╗░██║██╔══██╗██╔════╝██╔══██╗
███████║██╔██╗██║██║░░██║██╔██╗██║╚█████╗░█████╗░░██╔██╗██║██║░░██║█████╗░░██████╔╝
██╔══██║██║╚████║██║░░██║██║╚████║░╚═══██╗██╔══╝░░██║╚████║██║░░██║██╔══╝░░██╔══██╗
██║░░██║██║░╚███║╚█████╔╝██║░╚███║██████╔╝███████╗██║░╚███║██████╔╝███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
''')

# Настройки почты
sender_email = "анонимный_email@example.com"  # Используйте временный или анонимный email
sender_password = "пароль"  # Пароль от временного email
receiver_email = "получатель@example.com"  # Почта получателя
subject = "Анонимное сообщение"
message = "Это анонимное сообщение. Пожалуйста, не отвечайте на него."

# Создание письма
msg = MIMEText(message)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

# Отправка письма
try:
    with smtplib.SMTP("smtp.example.com", 587) as server:  # Замените на SMTP сервер временного email
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Письмо отправлено!")
except Exception as e:
    print(f"Ошибка: {e}")