vowels = 'aeiuy'  
word = (input("������� �����: ")).lower()  
print('���������� ���������',  
len(list(filter(lambda x: not x in vowels,word)))) 
print('���������� �������', len(list(filter(lambda x: x in vowels, word))))