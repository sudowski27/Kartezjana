#!/usr/bin/env python3





def kartezjana(cechy):
    n_of_characteristics = len(cechy)
    keys = list(input)
    N_of_combinations = 1
    N_of_keys = []
    
    
    for i in range(n_of_characteristics):
        help_var = cechy[keys[i]]
        N_of_combinations = N_of_combinations*len(help_var)
        N_of_keys.append(len(help_var))
    
    counter = []
    
    for i in range(n_of_characteristics):
        counter.append(0)
    
    output = []
    for i in range(N_of_combinations) :
        if i == 0 :
            counter[0] = 0
        else :
            counter[0] = counter[0] + 1
        
        for ii in range(n_of_characteristics-1) :
            if counter[ii] == N_of_keys[ii] :
                counter[ii+1] = counter[ii+1] + 1
                counter[ii] = 0
        output.append({})
        for j in range(n_of_characteristics) : 
            z = list(cechy[keys[j]])
            output[i][keys[j]] = z[counter[j]]
            
        
    return output
