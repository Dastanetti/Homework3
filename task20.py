eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
N = abs(int(input('Вводим 1 для английских букв, 2 для русских ')))
word = input('Введите слово: ').upper()
if N == 1:
	print('Ценность этого слова', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
elif N == 2:
	print('Ценность этого слова', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
else:
    print('Не правильное слово!')