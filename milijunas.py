novac = 0

print('Dobrodosli u igru milijunas!')
print('Na svako od 10 pitanja dobit cete 4 ponudjena odgovora')
print('Na svako pitanje odgovarate sa a,b,c ili d')
print('Ako odgovorite tocno na sva pitanja dobijate milijun kuna')

if input("Zelite li zapoceti igru? (da/ne)") == "da":
    print('Odlicno!')
    print('Prvo pitanje je Koji planet je najbliži Suncu?')
    if input('a) Mars b) Venera c) Jupiter d) Saturn') == "b":
        novac += 100000
        print('To je tocan odgovor')
        print('sljedece pitanje je Koje godine je potonuo Titanik?')
        if input('a) 1909. b) 1912. c) 1921. d) 1930.') == "b":
            novac += 100000
            print('To je tocan odgovor')
            print('sljedece pitanje je Koja je najduža rijeka na svijetu?')
            if input('a) Nil b) Amazona c) Mississippi d) Volga') == "a":
                novac += 100000
                print('To je tocan odgovor')
                print('sljedece pitanje je Koji je kemijski simbol za željezo?')
                if input('a) Fe b) Zn c) Ag d) Cu') == "a":
                    novac += 100000
                    print('To je tocan odgovor')
                    print('sljedece pitanje je Kako se zove najviši vrh svijeta?')
                    if input('a) Mont Blanc b) Mount Kilimanjaro c) Mount Everest d) Aconcagua') == "c":
                        novac += 100000
                        print('To je tocan odgovor')
                        print('sljedece pitanje je Koje godine je završio Drugi svjetski rat?')
                        if input('a) 1943. b) 1945. c) 1950. d) 1939.') == "b":
                            novac += 100000
                            print('To je tocan odgovor')
                            print('sljedece pitanje je Koji je osnovni sastojak tradicionalne talijanske tjestenine?')
                            if input('a) Riža b) Krumpir c) Pšenica d) Ječam') == "c":
                                novac += 100000
                                print('To je tocan odgovor')
                                print('sljedece pitanje je Tko je napisao tragediju "Romeo i Julija"?')
                                if input('a) William Shakespeare b) Charles Dickens c) Jane Austen d) Leo Tolstoj') == "a":
                                    novac += 100000
                                    print('To je tocan odgovor')
                                    print('sljedece pitanje je Koji je glavni grad Kanade?')
                                    if input('a) Toronto b) Vancouver c) Ottawa d) Montreal') == "c":
                                        novac += 100000
                                        print('To je tocan odgovor')
                                        print('sljedece pitanje je Koji je najveći kontinent na svijetu?')
                                        if input('a) Europa b) Afrika c) Azija d) Sjeverna Amerika') == "c":
                                            novac += 100000
                                            print('BRAVO! Odgovorili ste tocno na sva pitanja')
                                            print(f'Osvojeni iznos novaca je {novac} kuna')
                                        else:
                                            print('Nazalost to je netocan odgovor')
                                            print(f'Osvojeni iznos novaca je {novac} kuna')
                                    else:
                                        print('Nazalost to je netocan odgovor')
                                        print(f'Osvojeni iznos novaca je {novac} kuna')
                                else:
                                    print('Nazalost to je netocan odgovor')
                                    print(f'Osvojeni iznos novaca je {novac} kuna')
                            else:
                                print('Nazalost to je netocan odgovor')
                                print(f'Osvojeni iznos novaca je {novac} kuna')
                        else:
                            print('Nazalost to je netocan odgovor')
                            print(f'Osvojeni iznos novaca je {novac} kuna')
                    else:
                        print('Nazalost to je netocan odgovor')
                        print(f'Osvojeni iznos novaca je {novac} kuna')
                else:
                    print('Nazalost to je netocan odgovor')
                    print(f'Osvojeni iznos novaca je {novac} kuna')
            else:
                print('Nazalost to je netocan odgovor')
                print(f'Osvojeni iznos novaca je {novac} kuna')
        else:
            print('Nazalost to je netocan odgovor')
            print(f'Osvojeni iznos novaca je {novac} kuna')
    else:
        print('Nazalost to je netocan odgovor')
        print(f'Osvojeni iznos novaca je {novac} kuna')

else:
    print('vidim da ne zelite igrati. Nema veze, vratite se kad god zelite.')
