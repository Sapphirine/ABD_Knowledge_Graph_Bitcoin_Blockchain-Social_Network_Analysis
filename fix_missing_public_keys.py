#   preprocessing: input pubkeys from 'coinbase' are given in raw data, sometimes, as (None), these can be fixed by using the output pubkey
#  

from operator import itemgetter
import array as ar
def fix_missing_public_keys(rows):

    #handle missing pubkeys          
    rows.sort(key=itemgetter(1,2,0))
    prev_row = rows[0]
    
    for i in range(1, len(rows)):
        row = rows[i]
        if prev_row[3] == 0 and row[0] == 1 and row[1] == prev_row[1] and row[2] == prev_row[2]: # if missing, type==output and matching input key
            rows[i-1] = ar.array('L', map(int, [prev_row[0], prev_row[6], prev_row[2], row[3], prev_row[4], prev_row[5]]))   
        else:
            rows[i-1] = ar.array('L', map(int, [prev_row[0], prev_row[6], prev_row[2], prev_row[3], prev_row[4], prev_row[5]]))
        prev_row = row
        if i % 1000000 == 0:
            print "Progress: fix public keys, percent complete: " + str(float(i)/len(rows))
            
    ##### row specification:
    rows[i] = ar.array('L', map(int, [prev_row[0], prev_row[6], prev_row[2], prev_row[3], prev_row[4], prev_row[5]]))    
    return rows;