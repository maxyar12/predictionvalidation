# calculate average errors over sliding window and write to output

import sys
from decimal import *

def comparison(wname,actname,predname,outname):    

    window_size = int(open(wname, 'r').readlines()[0])
    actual_file = open(actual_path, 'r')
    stock_data= {}
    hours = []
    
    for line in actual_file.readlines():        #read-in actual stock data
        stock_hour = int(line.split("|")[0])
        hours.append(stock_hour)
        stock_id = line.split("|")[1]
        stock_Ap = Decimal(line.split("|")[2])
        if stock_hour > 1:
            stock_data[stock_id].append([stock_hour,stock_Ap,'absent'])
        else:
            stock_data[stock_id] = []
            stock_data[stock_id] = [[stock_hour,stock_Ap,'absent']]
    
    actual_file.close()
    num_hours = len(list(set(hours)))
    predicted_file = open(predicted_path, 'r')   # read-in the predicted data
    outfile = open(out_path,'w')
    
    for line in predicted_file.readlines():      
        stock_data[line.split("|")[1]][int(line.split("|")[0])-1][2] = Decimal(line.split("|")[2])
    predicted_file.close()
    
    if num_hours < window_size:
        print("you need data over longer time-range, or to reduce the window size")
    else:
        for w in range(num_hours +1 - window_size):
            
            total = Decimal('0.00')             #
            numst = Decimal('0.00')
            for t in range(1,window_size+1):
                for stock in stock_data.keys():
                    if stock_data[stock][w+t-1][1] !="absent" and stock_data[stock][w+t-1][2] != 'absent':
                        error =  stock_data[stock][w+t-1][1]-stock_data[stock][w+t-1][2]
                        if error.is_signed() == True:
                            error = error*Decimal('-1.00')
                        total = total + error
                        numst = numst + Decimal('1.00')
                    else:
                            error = 'ignore'
                    #print(str(w+t) + "|"+str(stock) +"|"+ str(stock_data[stock][w+t-1][1])+"  " +str(w+t) + "|"+str(stock) +"|"+ str(stock_data[stock][w+t-1][2])+"  " + str(error))

            try:
                avg_error = total/numst
                #a = decimal.Decimal(str(avg_error))
                rounded = avg_error.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
                outfile.write( str(w+1) +"|"+str(w+window_size) +"|"+ str(rounded) + '\n')
            except ZeroDivisionError:
                outfile.write( str(w+1) +"|"+str(w+window_size) +"|"+  "NA" + '\n')
        
if __name__ == '__main__':            
    window_path= sys.argv[1]
    actual_path = sys.argv[2]                             
    predicted_path = sys.argv[3]
    out_path = sys.argv[4]
    comparison(window_path,actual_path,predicted_path,out_path)