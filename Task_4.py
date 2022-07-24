# Задача_4
# В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

path = ('text_mama.txt')
data = open('text_mama.txt','r',encoding = 'utf-8' )
for line in data:
    print(line)
data.close()

data = open('text_mama.txt','r+',encoding = 'utf-8' )
text_1 = data.read().split()
text_2 = []
for line in text_1:
    if line.isalpha():
        text_2.append(line)
text_2 = (' '.join(text_2))
print(text_2)

data.writelines(f'\n{text_2}') # Добавляю изменённый текст в исходный файл.
data.close()
         

        
