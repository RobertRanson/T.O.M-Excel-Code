import csv
p_avg=[]
total =0
prev_v = []
counter =0
with open('FTSECSV.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        prev_v.append(float((row[1]).replace(",","")))
i =1   
while i< len(prev_v):
    total =0
    for x in range(0,i):
        
        total += prev_v[x]
    average = total/i
    p_avg.append(float("{0:.2f}".format(average)))
    i+=1
    
    

        
with open('FTSEprevaverage.txt','w') as f:
    for item in p_avg:
        f.write("%s\n" % item)
        
        
        
        
