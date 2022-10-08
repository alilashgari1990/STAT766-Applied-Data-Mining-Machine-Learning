
import numpy as np
import pandas as pd
import os

class homework1:

    file_name = os.getcwd()+ '/' + 'hw1_1_dat.txt'   
    def __init__(self):
        self.hw_1a, self.hw_1b = self.hw_1ab_fun(self.file_name)
        

    def hw_1ab_fun(self, file_name):
        file = open(file_name)
        
        it_list = []
        v_list = []
        epoch_list = []
        U_list = []

        for line in file:
            for word in line.split('  '):
                if word.startswith('it='):
                    it_list.append(int(word.split(' ')[1]))
                if word.startswith('v='):
                    v_list.append(int(word.split('v=')[1]))
                if word.startswith('epoch='):
                    epoch_list.append(int(word.split(' ')[1]))
            words = line.split('  ')
            for i, word in enumerate(words):
                if word.endswith('sum is'):
                    U_list.append(float(words[i+1].split(' ')[0]))
                    
        # lists(it_list ,v_list, epoch_list, U_list)
        
        
        set(it_list)
        n_it = len(set(it_list))
        # print(n_it)

        file = open(file_name)
        n_lines=0
        for line in file:
            n_lines = n_lines + 1
        #print (n)lines)
        
        
        ################################# part b)
        

        df = pd.DataFrame(columns = ["it", "v"])
        df["it"]=it_list
        df["v"]=v_list
        # df

        dic = {}
        for my_it in set(it_list):
            mask = df.loc[:,"it"] == my_it
            df_mask = df.loc[mask,:]
            my_set = set(df_mask["v"])
            dic[str(my_it)]=my_set


        
        df = pd.DataFrame()
        df["it"]=it_list
        df["v"]=v_list
        df["epoch"]= epoch_list
        df["U"] = U_list
        df["log10Ubeta2sum"]= np.log10(df["U"].values)
        del df["U"]
        # df


        
        answer_1a = {"n_lines":n_lines , "n_it": n_it , "it":dic}
        answer_1b = df
        
#          fill in your code to get answer to part a and b here
#         Assign your answer to part a to variable answer_1a
#         and assign your answer to part b to variable answer_1b.
        
        return answer_1a, answer_1b
        
        

    def findmin(self, it, v, df):
        
        mask = df.loc[:,"it"] == it
        mask1 = df.loc[:,'v'] == v
        df_mask = df.loc[mask & mask1,:]
        smallest = np.min(df_mask["log10Ubeta2sum"])
        
#         it = it_list
#         v = v_list
        
        # fill in your code to find the smallest log10Ubeta2sum 
        # among all rows with the same it and v. 
        # Assign the smallest value to variable smallest. 
        
        return smallest



