#__init__ is an oop construct. __init__ is the constructor for a class. Just like mentioned above,
# the __init__ method is called as soon as the memory for the object is allocated.
import itertools

class DFA:
    stare_curenta = None

    def __init__(self, stari, alfabet, fctie, stare_init, stare_fin, stare_curenta):
        #Self is a convention and not a Python keyword . self is parameter in Instance Method and user can use another parameter name in place of it.
        # But it is advisable to use self because it increases the readability of code, and it is also a good programming practice.
        self.stari = stari
        self.alfabet = set(alfabet)
        self.fctie = fctie
        self.stare_init = stare_init
        self.stare_fin= stare_fin
        self.stare_curenta= stare_init
        return

    """- stari: tuplu, trebuie sa fie imutabile
        - alfabet de simboluri
        - fctia de la stari x alfabet-> stari- dictionar:{(stare, caract): stare}
                - stare init, finala
           
            """
    def info_afd(self):
        s= len(self.stari)
        print("Nr stari: %s :",self.stari)
        print("Alfabet:", self.alfabet)
        print("Delta:")
        for tranz in self.fctie.keys() :
            print( tranz,"->" ,self.fctie[tranz])

        #print("\t", list(map(str, sorted(self.stari))))
        # for c in self.alfabet:
        #     #map(x, lista)- aplica fctia x pe toate elem din lista
        #     rezultat = map(lambda x: self.fctie(x, c), sorted(self.stari))
        #     print("\t", map(str, rezultat))
        print("Stare curenta:", self.stare_curenta)
        print("stare initiala:", self.stare_init)
        print("Stare finala:", self.stare_fin)
        #print("Currently accepting:", self.status())
    #The assert keyword lets you test if a condition in your code returns True, if not,
    # the program will raise an AssertionError.
    #assert set(self.accepts).issubset(set(self.states))


    def validare(self):
        # sa verific daca exista o cale de la st init la st finala
        # de verificat ca nu se ajunge intr-o stare prin 2 tranz diferite

        state_list=[st[0] for st in self.stari]# lista de stari, fara param de initial/ final
        assert self.stare_fin in state_list, "fals" # daca starile finale exista in stari
        assert self.stare_init in state_list#daca st init este in stari
        assert self.stare_curenta in state_list or self.stare_curenta == None #daca st curenta exista in stari
        #for stare in state_list:
        #    for elem in self.alfabet:

         #       assert self.fctie.values() in state_list
    def add_stare(self, elem_alfabet):#scoate daca nu e nevoie
        # adauga stare
        self.stare_curenta= self.fctie(self.stare_curenta, elem_alfabet)

    def verificare_caract(self, caract): #verifica daca poate continua
        if ((self.stare_curenta, caract)) not in self.fctie.keys():
            self.stare_curenta= None
        else: self.stare_curenta = self.fctie[(self.stare_curenta, caract)]
    def st_finala(self, stare):
        if self.stare_fin == stare:
            return True
        return False

    def verificare_sir(self, sir):
        self.stare_curenta= self.stare_init
        for caract in sir:
            self.verificare_caract(caract)
            continue

        return self.st_finala(self.stare_curenta)


class Automaton:

    def __init__(self, config_file):
        self.config_file = config_file

        self.sigma=[]
        self.stari=[]
        self.tranz=[]

        with open(self.config_file) as f:

            linie= f.readline().strip()
            #sigma
            while  linie.lower()!= "end":

                if linie[0]=='#' or ("..." in linie) or (":" in linie):
                    linie = f.readline().strip()

                    continue
                else:
                    self.sigma.append(linie)
                    linie = f.readline().strip()




            #stari

            linie= f.readline().strip()


            while linie.lower() != "end":

                if linie[0] == '#' or ("..." in linie) or (":" in linie):
                    linie = f.readline().strip()
                    continue
                else:
                    tuplu=linie.split(",")
                    tuplu[0]= tuplu[0].strip()
                    if len(tuplu)> 1:tuplu[1]= tuplu[1].strip()
                    self.stari.append(tuplu)
                    linie = f.readline().strip()

            #tranz
            linie = f.readline().strip()

            while linie.lower()!="end":
                if linie[0] == "#" or ("..." in linie) or (":" in linie):
                    linie = f.readline().strip()
                    continue
                else:
                    x= linie.split(",")
                    if len(x)== 2:
                        x[0]= x[0].strip()
                        x[1]= x[1].strip()
                    elif len(x)==3:
                        x[0] = x[0].strip()
                        x[1] = x[1].strip()
                        x[2]= x[2].strip()
                    self.tranz.append(x)

                    linie = f.readline().strip()

        print("sigma:",self.sigma)
        print("tranz:", self.tranz)
        print(self.stari)




    def validate(self):
        # check for unique start state and final state
        st_init_sau_fin=[t[1] if len(t)> 1 else "" for t in self.stari]

        if st_init_sau_fin.count("S") > 1:
            raise Exception("Only one starting state allowed!")

        # check transitions
        for transition in self.tranz:

            valid_states = [state[0] for state in self.stari]

            if transition[0] not in valid_states or transition[2] not in valid_states or transition[1] not in self.sigma:
                raise Exception("Transition contains invalid words or states!")
        return (True, st_init_sau_fin)
    def retsigma(self):
        return self.sigma
    def retstates(self):
        return self.stari
    def rettransitions(self):
        return self.tranz
    def create_function(self):
        x= {tuple([tr[0].strip(), tr[1].strip()]): tr[2].strip() for tr in self.tranz}

        return x

if __name__ == "__main__":
    a = Automaton('input.txt')
    print(a.validate())
    tranz= a.rettransitions()
    alfabet= a.retsigma()
    stari= a.retstates()

    for t in stari:
        if len(t) == 2:
            if t[1] == "S":
                st_init = t[0]
            elif t[1] == "F":
                st_fin = t[0]
        elif len(t) == 3:
            st_init = st_fin = t[0]
    print(st_init, st_fin)
    fctie= a.create_function()

    dfa= DFA(tuple(stari), alfabet, fctie, st_init, st_fin ,None )
    print(dfa.info_afd())
    dfa.validare()
    sir=["1", "0", "0", "0", "0", "0", "1"]
    #nu am facut inca tema 4, deci o sa fac dupa citirea cuv la tastatura
    a= dfa.verificare_sir(sir)
    print("verificare sir:", a)













