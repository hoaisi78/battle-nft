import abi
import checklp
import buyToken
import threading
import time
from web3 import Web3
k = 0

def main():
    global k
    tokenbuy = ""    #Contract Address of Token we want to buy      
    count = 0.025
    minlp = 0.5  #min lp snip
    gaslimit = 4000000
    gasgwei = 0.3
    mode = 1     ## mode =  1: shushiswap, mode = 2 camelot, mode = 3 zyber, mode = 4 ailenfi
    private_key=[]
    sender_address = [] ## list wallet, ['w1','w2','']
    process= []
    while True:
        try:
            if(mode == 1):
                k = k + 1
                print("Checking Lp....... " + str(k))
                resultcheck  = checklp.checkLptokenShushi(address=tokenbuy)
                if(resultcheck!='0x0000000000000000000000000000000000000000'):
                    lpbalance = checklp.checklpEth(resultcheck)
                    if lpbalance > minlp:
                        for u in range(len(sender_address)):
                            t = threading.Thread(target=buyToken.buyTokenShushi, args = (sender_address[u], private_key[u], tokenbuy, count, gaslimit,gasgwei))
                            t.daemon = True   
                            t.start()  
                            process.append(t)  
                        for i in process:
                            i.join()
                    else:
                        continue
                    return
                else:
                    continue
            elif mode == 2:
                k = k + 1
                print("Checking Lp....... " + str(k))
                resultcheck  = checklp.checkLptokenCamelot(address=tokenbuy)
                if(resultcheck!='0x0000000000000000000000000000000000000000'):
                    lpbalance = checklp.checklpEth(resultcheck)
                    if lpbalance > minlp:
                        for u in range(len(sender_address)):
                            t = threading.Thread(target=buyToken.buyTokencamelot, args = (sender_address[u], private_key[u], tokenbuy, count, gaslimit,gasgwei))
                            t.daemon = True   
                            t.start()  
                            process.append(t)  
                        for i in process:
                            i.join()
                    else:
                        continue
                    return
                else:
                    continue
            elif mode == 3:
                k = k + 1
                print("Checking Lp....... " + str(k))
                resultcheck  = checklp.checkLptokenzyber(address=tokenbuy)
                
                if(resultcheck!='0x0000000000000000000000000000000000000000'):
                    lpbalance = checklp.checklpEth(resultcheck)
                    if lpbalance > minlp:
                        for u in range(len(sender_address)):
                            t = threading.Thread(target=buyToken.buyTokenZyber, args = (sender_address[u], private_key[u], tokenbuy, count, gaslimit,gasgwei))
   
                            t.daemon = True   
                            t.start()  
                            process.append(t)  
                        for i in process:
                            i.join()
                    # t = threading.Thread(target=buyToken.buyToken, args = (address,privatekey,tokenbuy,count,gas))
                    # txhash =buyToken.buyTokenZyber(address=address,private=privatekey,count=count,gas=gas,tokenBuy=tokenbuy)
                    # print(txhash)
                    else:
                        continue
                    return
                else:
                    continue
            
            elif mode == 4:
                k = k + 1
                print("Checking Lp....... " + str(k))
                resultcheck  = checklp.checkLptokenailen(address=tokenbuy)
                
                if(resultcheck!='0x0000000000000000000000000000000000000000'):
                    lpbalance = checklp.checklpEth(resultcheck)
                    if lpbalance > minlp:
                        for u in range(len(sender_address)):
                            t = threading.Thread(target=buyToken.buyTokenAilen, args = (sender_address[u], private_key[u], tokenbuy, count, gaslimit,gasgwei))
   
                            t.daemon = True   
                            t.start()  
                            process.append(t)  
                        for i in process:
                            i.join()
                    else:
                        continue
                    # t = threading.Thread(target=buyToken.buyToken, args = (address,privatekey,tokenbuy,count,gas))
                    # txhash =buyToken.buyTokenZyber(address=address,private=privatekey,count=count,gas=gas,tokenBuy=tokenbuy)
                    # print(txhash)
                    return
                else:
                    continue
        
        
        except Exception as e:
            print("Error", e)
            continue
            
main()
    


