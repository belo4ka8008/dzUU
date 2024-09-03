def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    #1
    if (sender.count('@') == 0 #подбор условий для поверки мое почтение
        or not (sender.count('.com') == 1
        or sender.count('.ru') == 1 or sender.count('.net') == 1)
        or recipient.count('@') == 0
        or not (recipient.count('.com') == 1
        or recipient.count('.ru') == 1
        or recipient.count('.net') == 1)):
        #условия внутри  условия проверки ставить в скобки! и только один иначе не работает...
        #при переносе строки кода ставить скобки.
        print('Невозможно отправить письмо с адреса', sender, 'на адрес ', recipient)
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(F'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')