# nfa nedet
# dictionar cu pcte - avand o lista cu nodurile in care poate ajunge
#random choice la toate pana ajung la fin
# daca nu iese stringul => nun accepta sau  nu exista


import random


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
                    x[0]= x[0].strip()
                    x[1]= x[1].strip()
                    x[2]= x[2].strip()
                    self.tranz.append(x)

                    linie = f.readline().strip()

        print("sigma:",self.sigma)
        print(self.tranz)
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
        return True

    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        """Return the automaton's final configuration

        If the input is rejected, the method raises a
        RejectionException.
        """
        pass


class nfa:
     def __init__(self, stari, sigma, delta, stare_init, stari_finale):
         self.stari= stari
         self.sigma= sigma
         self.delta= delta
         self.stare_init= stare_init
         self.stari_finale= stari_finale

     # multime stari- tuplu
     # #alfabet- tuplu/ lista
     # #delta, unde delta e def pe stari x alfabet-> 2^stari-tuplu de forma (stare init, litera, (tuplu cu stari finale))
     # # o stare initiala
     # # mai multe stari finale - tuplu
     # # o tranzitie poate avea mai multe stari coresunzatoare
     # #pot avea sirul vid
     # # sirul e acceptat daca exista cel  putin o cale de la st_in
     def info_nfa(self):
        s= len(self.stari)
        print("Nr stari: ",self.stari)
        print("Alfabet:", self.sigma)
        print("Delta:")
        for tranz in self.delta :
            print( tranz[0], "cuv:", tranz[1],"st fin:", tranz[2])


        print("stare initiala:", self.stare_init)
        print("Stare finala:", self.stari_finale)
        # def string_verify(self, word ):
        #     nodes={
        #
        #     }
        #     for node in self.stari:
        #         nodes[node]=[]
        #         for tr in self.delta:
        #             if node== tr[0]:
        #                 nodes[node].append(tr[2])
        #
        #


     def verificare_sir(self, sir):
         noduri={
         }# pt fiecare pct - lista cu toate nodurile in care poate ajunge
         for st in self.stari:
             noduri[st]=[]
             for t in self.delta:
                 if t[0]== st:
                     st_init= t[0]
                     st_urm= t[2]
                     noduri[st].append(st_urm)
                     while st_urm not in self.stari_finale:
                         for tr in self.delta:
                             if tr[0]== st_urm:
                                noduri[st].append(st_urm)
                                st= self.stare_init
                                sir_curent=""
                                l= []
                                l.append(st)
                                while st not in self.stari_finale:
                                    st= random.choice(noduri[st])
                                    l.append(st)
                                for nod in l:
                                    for tr in self.tranz:
                                        sir_curent= sir_curent+ tr[2]
                                        print("sir curent:", sir_curent)








if __name__ == "__main__":
    a = Automaton("input.txt")
    print(a.validate())
