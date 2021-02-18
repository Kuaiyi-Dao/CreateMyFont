import fontforge
F = fontforge.open('fz.TTF')
i = 0
for name in F:
    print(name)
    filename = './output/'+str(F[name].unicode) +'_'+name+ '.bmp'
    F[name].export(filename)
    i +=1
    if i > 100:
        break