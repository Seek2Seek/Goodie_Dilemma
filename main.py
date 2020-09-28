def file_read(file_name):
        with open(file_name) as f:
                dic={}
                price = []
                comp = []
                #Content_list is the list that contains the read lines.     
                content_list = f.readlines()
                input_text = content_list
                res = [sub.strip() for sub in input_text]
                
                #stroing values in dic and lis
                for s in res:
                    split_input = s.split(': ')
                    if len(split_input) ==2:
                            key=split_input[0]
                            dic[key]= int(split_input[1])
                            price.append(int(split_input[1]))
                num = dic.pop('Number of employees')
                num_emp = price[0]
                price.pop(0)
                price.sort()
                
                #difference between the low price goodie and the high price goodie
                for i in range(len(price)-num_emp ):
                    comp.append(-price[i]+price[i+num_emp-1])
                list_starts=comp.index(min(comp))
                
                # Writing the Result in final_result.txt
                final_list = price[list_starts: list_starts + num_emp]
                output_file = open("sample_output3.txt", "w")
                output_file.write('The goodies selected for distribution are: \n\n')
                output_file.write('Number of employees: '+ str(num_emp) +'\n\n')
                for val in (final_list):
                    for key, value in dic.items(): 
                         if val == value:
                                output_file.write(key+': '+str(value)+'\n')
                                
                output_file.write('\n'+'And the difference between the chosen goodie with highest price and the lowest price is '+str(min(comp)))
                
                f.close()
                output_file.close()            

file_read('sample_input3.txt')