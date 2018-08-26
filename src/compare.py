# calculate average errors over sliding window and write to output

import sys
    
def comparison(wname,actname,predname,outname):    

    window_size = int(open(wname, 'r').readlines()[0])
    actual_file = open(actual_path, 'r')
    stock_data= {}
    hours = []

    for line in actual_file.readlines():        #read-in actual stock data
        stock_hour = int(line.split("|")[0])
        hours.append(stock_hour)
        stock_id = line.split("|")[1]
        stock_Ap = float(line.split("|")[2]) 
        if stock_hour > 1:
            stock_data[stock_id].append([stock_hour,stock_Ap,None])
        else:
            stock_data[stock_id] = []
            stock_data[stock_id] = [[stock_hour,stock_Ap,None]]
    
    actual_file.close()
    num_hours = len(list(set(hours)))
    predicted_file = open(predicted_path, 'r')   # read-in the predicted data
    outfile = open(out_path,'w')
    
    for line in predicted_file.readlines():      
        stock_data[line.split("|")[1]][int(line.split("|")[0])-1][2] = float(line.split("|")[2]) 
    predicted_file.close()
    
    if num_hours < window_size:
        print("you need data over longer time-range, or to reduce the window size")
    else:
        for w in range(num_hours +1 - window_size):
            
            win_errors = []             #store errors for later averaging
            
            for t in range(1,window_size+1):
                for stock in stock_data.keys():
                    if stock_data[stock][w+t-1][1] != None and stock_data[stock][w+t-1][2]!= None:
                        error =  abs(stock_data[stock][w+t-1][2]-stock_data[stock][w+t-1][1])
                        win_errors.append(error)
                    else:
                            error = 'ignore'
                    #print(str(w+t) + "|"+str(stock) +"|"+ str(stock_data[stock][w+t-1][1])+"  " +str(w+t) + "|"+str(stock) +"|"+ str(stock_data[stock][w+t-1][2])+"  " + str(error))
                 
            avg_error = sum(win_errors)/len(win_errors)  
            outfile.write( str(w+1) +"|"+str(w+window_size) +"|"+  "%.2f" % avg_error + '\n')
        
if __name__ == '__main__':            
    window_path= sys.argv[1]
    actual_path = sys.argv[2]                             
    predicted_path = sys.argv[3]
    out_path = sys.argv[4]
    comparison(window_path,actual_path,predicted_path,out_path)