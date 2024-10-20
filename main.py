with open('text.txt','r',encoding="utf-8") as file:
    text = file.read()
#Деление текста на слова
words = text.split()
words_count =0
for i in words:
    words_count+=1
print("Количество слов:",words_count)
