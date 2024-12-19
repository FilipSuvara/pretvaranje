import random
metak_igrac = 0
metak_komp = 0
opcije_kompa1 = [ "napad" , "blok" , "reload" ]        
opcije_kompa2 = [ "blok" , "reload" ]          
while True:
    igrac_odabir = input ("izaberite potez, 1 za napad,2 za blok i 3 za reload") 
    if metak_komp  == 0 :
        komp_odabir = random.choice (opcije_kompa2)
        print (komp_odabir)
    else:
        komp_odabir = random.choice (opcije_kompa1)
        print (komp_odabir)


