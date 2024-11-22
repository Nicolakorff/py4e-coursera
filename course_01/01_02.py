score = input('Enter Score: ')
s = float(score) / 10
if s >= 0.9 < 1.0 :
    print('A')
elif s >= 0.8 :
    print('B')
elif s >= 0.7 :
    print('C')
elif s >= 0.6 :
    print('D')
elif s < 0.6 :
    print ('F')
elif s < 0.0 :
    print('Score to low')
else :
    print('Score to high')
