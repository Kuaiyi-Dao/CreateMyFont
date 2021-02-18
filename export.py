import fontforge
F = fontforge.open('fz.TTF')
for name in F:
    print(name)
    filename = './output/'+str(F[name].unicode) +'_'+name+ '.bmp'
    F[name].export(filename)
