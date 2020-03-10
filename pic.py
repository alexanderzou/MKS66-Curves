def numConv(num):
    new = str(num)
    if len(new) == 1:
        return '00' + new
    if len(new) == 2:
        return '0' + new
    if len(new) == 3:
        return new

f = open('snake', 'w')
a = -1000
while a < 500:
    f.write('bezier\n200 {} 100 {} 300 {} 200 {}\n'.format(a, a+200, a+300, a+500))
    f.write('bezier\n300 {} 200 {} 400 {} 300 {}\n'.format(a, a+200, a+300, a+500))
    f.write('circle\n200 {} 0 20\n'.format(a+100))
    f.write('circle\n250 {} 0 10\n'.format(a+300))
    f.write('circle\n260 {} 0 30\n'.format(a+400))
    f.write('circle\n240 {} 0 15\n'.format(a+180))
    a += 500
f.write('ident\nmove\n0 5 0\n')
fNum = 1
tmp = fNum
while fNum < tmp + 100:
    f.write('apply\nsave\nimage{}.png\n'.format(numConv(fNum)))
    fNum += 1
f.write('display\n')
f.close()
