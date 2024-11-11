def rotate_letter(letter: str, shift:int)->str:
    'Функция сдвигает символ letter на shift позиций'

    if shift>0:
        if shift > 25 or shift<-25:
            shift = shift % 26
        else:
            shift = shift
        a=ord(letter)+shift
        if a>122:
            a=a-26
        #print(a)
    else:
        if shift > 25 or shift<-25:
            shift = abs(shift) % 26
        else:
            shift = shift
        a = ord(letter) - abs(shift)
        if a<97:
            a=a+26
    return chr(a)


def caesar_cipher(phrase:str, key:int)->str:
    'Шифр Цезаря'
    alph_z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_s = 'abcdefghijklmnopqrstuvwxyz'
    b=[]
    for i in phrase:
        if i in alph_z or i in alph_s:
            #print(rotate_letter(i, key))
            b.append(rotate_letter(i, key))
        else:
            b.append(i)
    b=''.join(b)
    return b




print(caesar_cipher('leave out all the rest', -4))





