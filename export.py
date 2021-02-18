import fontforge
F = fontforge.open('fz.TTF')
F.reencode('GB2312')
for name in F:
    filename = './output/'+str(F[name].unicode) +'_'+name+ '.bmp'
    F[name].export(filename)