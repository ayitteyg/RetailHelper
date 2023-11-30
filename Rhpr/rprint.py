import os
import datetime
from dbtable import Database
from datahandler import salesdata
#os.startfile("sales_data.txt", "print")

class salesreceipt:

    def item(self,x):
        if len(x) < 35:
            k = 35 - len(x)
            i = x+(" "*k)
            #print(len(i))
            return i
        else:
            return x

    def generate_receipt(self, receipt):

        l = "-"*65
        m = "*"*65
        tbs = "\t\t\t\t\t"
        sp = "\n"
        dt = datetime.datetime.now().strftime("%A, %B %d")
        B = Database().get_busines_profile()
        it = "item"

        r = receipt
        user = r[-1]
        rct = r[-2] #r[]
        subtotal = "{:,.2f}".format(r[3])
        T = float(salesdata().getax())
        tax = "{:,.2f}".format(r[3]*(T/100))
        total = "{:,.2f}".format(r[3] + (r[3]*(T/100)))
        chng = "{:,.2f}".format(r[2])
        paid = "{:,.2f}".format(int(r[1]))

        #print(user,rct,subtotal,total,chng,paid)



        header = ["\t\t\t\tCASH RECEIPT",m,f"\t\t{B[0]}", f"\t\t{B[2]}", f"\t\t{B[3]}",m,
                        f"Date: {dt}", f"Sales Person: {user}",f"Receipt# : {rct}",l,
                        f"No.\t{self.item(it)}\tqty\tGhc:"]

        
        data = [f"{i[0]}\t{self.item(i[1])}\t{i[2]}\t{i[4]}" for i in r[0]] 
                

        summary = [f"{tbs}subtotal:\t{subtotal}",
                    f"{tbs}tax(17.5%):\t{tax}",
                      f"{tbs}total:\t\t{total}",
                        f"{tbs}paid:\t\t{paid}",
                          f"{tbs}change:\t\t{chng}",l] 

        fotter = "\t\t\t*THANK YOU!* PLEASE DO VISIT AGAIN.."

        if not os.path.exists('receipt_data.txt'):
            with open('receipt_data.txt', 'w') as file:
                for line in header:
                    file.write(line+"\n")
                for line in data:
                    file.write(line+"\n")               
                file.write(sp)
                file.write(l)
                file.write("\n")
                for line in summary:
                    file.write(line+"\n")
                file.write(fotter)
            file.close()
        else:
            with open('receipt_data.txt', 'w') as file:
                for line in header:
                    file.write(line+"\n")
                for line in data:
                    file.write(line+"\n")
                file.write(sp)
                file.write(l)
                file.write("\n")
                for line in summary:
                    file.write(line+"\n")
                file.write(fotter)
            file.close()


    def print_receipt(self):
        os.startfile("receipt_data.txt", "print")
 

