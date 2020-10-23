

class NFA:


    def __init__(self):
        self.states = []  # list of states in NFA
        self.symbols = []  # set of alphabets in the NFA
        self.istate ='' # initial state
        self.f_states = []  # list of accepting states of NFA
        self.M = [[0 for i in range(len(self.A))] for j in range(len(self.Q))]
        self.ini_state=[]    #initial state of the required DFA
        self.fin_states=[] #accepting states of the DFA
        self.d=[]    # list for storing the alphabets except epsilon

    def states(self):        #function which accepts the states of the NFA
        n = int(input("No. of states in NFA : "))

        print("Enter the states: ")
        print("Enter the initial state: ")
        for i in range(0,n):
            var = input("Enter "+str(i+1)+"th state: " )
            self.states.append(x)

        print(self.states)

    def alpahabet(self):     #function defined for storing the alphabets of the NFA
        n1 = int(input("Enter number of symbols: "))
        for i in range(0, n1):

            if i==0:
                var = input("Enter the character for epsilon: ")
                self.symbols.append(var)

            else:
                x = input("Enter the " + str(i + 1) + " th alphabet: ")
                self.symbols.append(var)
                if i > 0:
                    self.d.append(var)

        print("All the symbols are: ")
        print(self.d) #prints the alphabet list without epsilon symbol
        print("All the alphabets of the NFA are: ")

        print(self.symbols)  #prints the alphabet list entered by the user

    def accept_state_NFA(self):   #function to accept the final states
        n2=int(input("Enter the number of accepting states in the NFA "))
        for k in range(0,n2):
            self.f_states.append(input("Enter the "+str(k+1)+" th accepting state of the NFA : "))
        print("The accepting states of the NFA are : ")
        print(self.f_states)


    def ini_state(self):
        self.istate = self.states[0]  #to store the initial state of the NFA


    def matrix_store(self, i, j):                                   #function to define the delta function of the NFA

        n=int(input("Enter the number of states at which "+ str(self.states[i])+ " can transit after getting " +str(self.symbols[j])+" : "))
        list = []

        for l in range(0,n):
            list.append(input("Enter the " +str(l+1)+ " th state: "))  #appending all the states to which Q[i] can transit after getting the symbol A[j]

        self.M[i][j]=list                                          



    def transition_func_value_storing(self):
        self.M = [[0 for i in range(len(self.A))] for j in range(len(self.Q))]  #matrix for storing the set of states at which a particular state of the NFA will transit after getting a particular symbol  which is contained in the alphabet set
        for i in range(0,len(self.states)):
            for j in range(0,len(self.symbols)):
                self.matrix_store(i,j)                                          


    def print_matrix(self):
        for i in range(0, len(self.states)):
            for j in range(0, len(self.symbols)):
                print(" The state "+ str(self.states[i])+" will transit to "+str(self.M[i][j])+" states after being executed by the symbol  "+ str(self.symbols[j]))

        print(self.M)          




    def dFA_ini_state(self):
        self.ini_state()                                                  # storing the initial state of NFA
        store_lst= list(set(self.M[0][0])| set(self.istate))
        self.ini_state=self.initial_state_DFA(store_lst)                         #calculating the initial state of the desired DFA
        self.ini_state=list(self.q0)
        print(" The initial state of the desired DFA is: ")
        print(self.ini_state)                                                    #prints the epsilon closure of the initial state of the NFA


    def initial_state_DFA(self, store_lt):




        store_lst1 = store_lt
        for t in range(0, len(store_lst1)):
            store_lt = list (set(store_lt) | set(self.M[self.Q.index(store_lst1[t])][0]))



        if sorted(store_lt)==sorted(store_lst1):    # base case

            return store_lt
        else:                                       
            store_lst1 = store_lt
            return self.initial_state_DFA(store_lst1)





    def delta_modified(self, lst, x):
        list1=[]
        for i in range(0, len(lst)):
            list1=list(set(self.M[self.states.index(lst[i])][self.symbols.index(x)])|set(list1)) #list of all the states to which the elements in the list 'lst' transited after being acted upon by x

        print(" the union of all the states to which " + str(lst)+ " transited after getting the symbol "+ str(x)+ " is :")
        print(list1)
        return list1

    def closure_delta_modified(self, l, y): #function for evaluating the union of epsilon closures of all the elements
        lst1=self.delta_modified(l,y)
        str_lst=[]

        if lst1!=[]:                                                                   
            for i in range(0, len(lst1)):
                ind = self.states.index(lst1[i])
                str_lst = list(set(str_lst) | set(self.initial_state_DFA(list(set(self.M[ind][0]) | set([lst1[i]])))))  #list of the epsilon closure of all the states in the list 'l'
        print("union of the closure of all the states present in "+ str(str_lst) + " is : ")
        print(str_lst)
        return str_lst


    def dfa_states_store(self, i=0, lt=[], M_str=[]):



        M_str.append([self.closure_delta_modified(lt[i],x) for x in self.d])  #A1 contains all the alphabets except epsilon
        length=len(lt)
        for var in M_str[i]:
            if var != []:

                ctr=0
                for j in range(0, len(lt)):
                    if sorted(var)==sorted(lt[j]):

                        ctr=ctr+1
                if ctr==0:                           

                    lt.append(var)                    #if a new state is found, then append it to lst
        length1=len(lt)

        if length1==length and i+1==length1:         
            return [lt, M_str]                      
                                                     # M_st is a matrix representing the modified transition function for the DFA

        else:                                        

            i=i+1
            return self.dfa_states_store(i, lt, M_str)


    def accept_states_DFA(self):

        L=self.dfa_states_store(0,[self.q0])
        l=len(L[0])

        for j in range(0, l):
            if list(set(self.f_states) & set(L[0][j])) != []: #to check whether the states in the constructed DFA has a non-empty intersection with the list of final states in the NFA.
                self.F_DFA.append(L[0][j])             #if the intersection is non-empty, we're storing the current state of DFA as one of the final state of the desired DFA

        print("States of DFA are: ")
        print(L[0])
        print(L[1])

        print("Final states of DFA are : ")

        print(self.F_DFA)


    def states_of_DFA(self):

        L= self.dfa_states_store(0, [self.q0])
        l=len(L[0])

        x=int(input(print("If you want to see the states of the constructed DFA press 1, else press 0")))

        if x==1:
            print(" The states of the DFA are :")
            for i in range(0,l):
                print(" " +str(L[0][i])+" ")
        else:
            return


    def dfa_state_transition(self):
        L = self.dfa_states_store(0, [self.istate])
        l = len(L[0])


        x = int(input(print("If you want to see the transition of the states of the constructed DFA press 1, else press 0")))

        if x==1:
            for i in range(0,l):
                for j in range(0, len(self.d)):
                    print(" The state "+str(L[0][i])+ " of the DFA will transit to "+str(L[1][i][j])+" state after being executed by the alphabet "+str(self.d[j]))

        else:
            return

nfa= NFA()
nfa.states()
nfa.alpahabet()
nfa.accept_state_NFA()
nfa.transition_func_value_storing()
nfa.print_matrix()
nfa.dFA_ini_state()

nfa.accept_states_DFA()
nfa.states_of_DFA()
nfa.dfa_state_transition()
