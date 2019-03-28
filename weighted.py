import csv
w_avg=[]
first = 6970.6
second = 6968.6
third = 6834.9
with open('FTSECSV.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        averaged = float("{0:.2f}".format(0.7*first+0.2*second+0.1*third))
        print(row[0]+ "nextday:")
        print (averaged)
        w_avg.append(averaged)
        third = second
        second = first
        first=float((row[1]).replace(",",""))
with open('weightedFTSE.txt','w') as f:
    for item in w_avg:
        f.write("%s\n" % item)
        
        
        
        
