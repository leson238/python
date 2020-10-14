final_message = ''
while True:
    text = input('Say something: ')
    if text == '\\end':
        break
    message = text.capitalize()
    first_word = message.split(' ')[0]
    if first_word in ['How', 'What', 'When', 'Why']:
        message += '? '
    else:
        message += '. '
    final_message += message
print(final_message)
