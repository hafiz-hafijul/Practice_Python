def emoji_converter(message):
    words = message.split(' ')

    emoji = {
        ':)': ' good',
        ':(': ' sad'
    }
    output = ''
    for word in words:
        output += emoji.get(word, word) + ' '
    return output


message = input('> ')
print(emoji_converter(message))
