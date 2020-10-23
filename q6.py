class NFA:
    def __init__(self):
        self.states = []  #  states in the NFA
        self.symbols = []  # alphabet set in the NFA
        self.istate ='' # initial state of NFA
        self.f_states = []  # accepting states of NFA
        self.ini_state=[]    #initial state of the required DFA
        self.fin_states=[] #accepting states of the DFA
        self.d=[]    # list for storing the alphabets(symbols) except epsilon
        self.M = [[0 for i in range(len(self.symbols))] for j in range(len(self.states))]

    def states_nfa(self):        #function for storing the states of the NFA
        n = int(input("No. of states in NFA : "))
        print("Input the initial state 1st")
        for i in range(0,n):
            var = input("Input state "+str(i+1)+" : " )
            self.states.append(var)
        print(self.states)

    def ini_state(self):
        self.istate = self.states[0]  #storing the initial state of the NFA

    def alpahabet(self):     #function for storing the symbols of the NFA
        ns = int(input("No. of Symbols : "))
        for i in range(0, ns):
            if i == 0:
                var = input("Character for epsilon, i.e, the 1st symbol of alphabet : ")
                self.symbols.append(var)
            else:
                var = input("Input symbol "+str(i+1)+" : " )
                self.symbols.append(var)
                if i > 0:
                    self.d.append(var)
        print("Symbols of the alphabet of NFA: ")
        print(self.symbols)

    def accept_state_nfa(self):   #accepting the final states
        na=int(input("No. of accepting states in the NFA "))
        for k in range(0,na):
            var = input("Input "+str(k+1)+" accepting state of the NFA : ")
            self.f_states.append(var)
        print("The accepting states of the NFA are : ")
        print(self.f_states)

    def trans_func(self, i, j):                                   
        n=int(input("No. of states at which "+ str(self.states[i])+ " can transit after getting the symbol " +str(self.symbols[j])+" : "))
        list = []
        for l in range(0,n):
            list.append(input("give the " +str(l+1)+ " th state : "))  
        self.M[i][j]=list

    def trans_table(self):
        self.M = [[0 for i in range(len(self.symbols))] for j in range(len(self.states))]  #storing the corresponding set of states at which a certain state of the NFA will transit after getting a particular symbol contained in the alphabet set
        for i in range(0,len(self.states)):
            for j in range(0,len(self.symbols)):
                self.trans_func(i,j)                                  

    def print_trans_func(self):
        for i in range(0, len(self.states)):
            for j in range(0, len(self.symbols)):
                print("state "+ str(self.states[i])+" ---> "+str(self.M[i][j])+" on "+ str(self.symbols[j]))
        print(self.M)         

    def dfa_ini_state(self):
        self.ini_state()                                          # getting the initial state of the NFA
        store_lst= list(set(self.M[0][0])| set(self.istate))
        self.ini_state=self.initial_state_dfa(store_lst)          #evaluating the initial state of the desired DFA, i.e, the epsilon closure of the initial state of the NFA, which is q_0
        self.ini_state=list(self.istate)
        print(" The initial state of the desired DFA is : ")
        print(self.ini_state)                                     #displaying the epsilon closure of the initial state of the NFA

    def initial_state_dfa(self, store_lt):
        store_lst1 = store_lt
        for t in range(0, len(store_lst1)):
            store_lt = list (set(store_lt) | set(self.M[self.states.index(store_lst1[t])][0]))
        if sorted(store_lt) == sorted(store_lst1):    # base case>>> no new states are added to the store_lst1 by applying the epsilon transition on every elements of the previous store_lst1
            return store_lt
        else:                                       #recursive case
            store_lst1 = store_lt
            return self.initial_state_dfa(store_lst1)

    def delta_modified(self, lst, x):
        list1=[]
        for i in range(0, len(lst)):
            list1=list(set(self.M[self.states.index(lst[i])][self.symbols.index(x)])|set(list1)) #union of all the set of states to which the elements in the list 'lst' transited after being acted upon by x

        print(" the union of all the states to which " + str(lst)+ " transited after getting the symbol "+ str(x)+ " is :")
        print(list1)
        return list1

    def closure_delta_modified(self, l, y): #method for evaluating the union of epsilon closures of all the elements in the list returned by the method 'delta_modified'
        lst1=self.delta_modified(l,y)
        str_lst=[]

        if lst1!=[]:         
            for i in range(0, len(lst1)):
                ind = self.states.index(lst1[i])
                str_lst = list(set(str_lst) | set(self.initial_state_DFA(list(set(self.M[ind][0]) | set([lst1[i]])))))  #union of the epsilon closure of all the states in the list 'l'
        print("union of the closure of all the states present in "+ str(str_lst) + " is : ")
        print(str_lst)
        return str_lst

    def dfa_states_store(self, i=0, lt=[], M_str=[]):
        M_str.append([self.closure_delta_modified(lt[i],x) for x in self.d])
        length=len(lt)
        for var in M_str[i]:
            if var != []:
                ctr=0
                for j in range(0, len(lt)):
                    if sorted(var)==sorted(lt[j]):
                        ctr=ctr+1
                if ctr==0:                          
                    lt.append(var)                    
        length1=len(lt)
        if length1==length and i+1==length1:         
            return [lt, M_str]                      
        else:                                      
            i=i+1
            return self.dfa_states_store(i, lt, M_str)

    def accept_states_dfa(self):
        L=self.dfa_states_store(0,[self.istate])
        for j in range(0, len(L[0])):
            if list(set(self.f_states) & set(L[0][j])) != []: #checking whether the states in the constructed DFA has a non-empty intersection with the list of final states in the NFA, or not.
                self.fin_states.append(L[0][j])             #if the intersection is non-empty, we're storing the current state of DFA as one of the final state of the desired DFA

        print("states of DFA : ")
        print(L[0])
        print(L[1])
        print("final state(s) of DFA : ")
        print(self.fin_states)


    def print_dfa(self):
        L1 = self.dfa_states_store(0, [self.istate])
        print(" The states of the DFA are :")
        for i in range(0,len(L1[0])):
            print(" " +str(L1[0][i])+" ")
        L2 = self.dfa_states_store(0, [self.istate])
        for j in range(0,len(L2[0])):
            for k in range(0, len(self.d)):
                print(" The state "+str(L[0][j])+ " of the DFA will transit to "+str(L[1][j][k])+" state after being acted upon by the alphabet "+str(self.d[k]))


nfa = NFA()
nfa.states_nfa()
nfa.alpahabet()
nfa.accept_state_nfa()
nfa.trans_table()
nfa.print_trans_func()
nfa.dfa_ini_state()

nfa.accept_states_dfa()
nfa.print_dfa()
