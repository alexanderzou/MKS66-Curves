def numConv(num):
    new = str(num)
    if len(new) == 1:
        return '00' + new
    if len(new) == 2:
        return '0' + new
    if len(new) == 3:
        return new

f = open('snake', 'w')
fNum = 1
a = -1000
while a < 1000:
    f.write('bezier\n200 {} 100 {} 300 {} 200 {}\n'.format(a, a+200, a+300, a+500))
    f.write('bezier\n300 {} 200 {} 400 {} 300 {}\n'.format(a, a+200, a+300, a+500))
    f.write('circle\n')
    a += 500
f.write('display\n')
f.close()
