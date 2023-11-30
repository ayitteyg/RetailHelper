import csv
import os
import json
from datetime import date, datetime
#import pandas as pd
from dbtable import Database
import calendar
import random
from myFunc import roundup, roundup2
import xlsxwriter
from xlsxwriter.workbook import Workbook
import pathlib

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet



class backupdata:
    def save_backup(b):
        dt = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
        d =f'backup_file_'+ dt
        data_str = json.dumps([b])

        if not os.path.isdir("C:/Rhpr"):  
            os.makedirs("C:/Rhpr") 
          
            with open(f'C:/Rhpr/{d}.json', 'w') as file:
                data = file.write(data_str)
                file.close() 
        else:
            with open(f'C:/Rhpr/{d}.json', 'w') as file:
                data = file.write(data_str)
                file.close()



    def load_backup(self):
        with open('backup_data.json', 'r+') as file:
            data = json.load(file)

            company = json.loads(data[0]['backupdata'][0][0][0])
            products = json.loads(data[0]['backupdata'][0][1][0])
            purchases = json.loads(data[0]['backupdata'][0][2][0])
            adjustments = json.loads(data[0]['backupdata'][0][3][0])
            salessummary = json.loads(data[0]['backupdata'][0][4][0])
            salesitems = json.loads(data[0]['backupdata'][0][5][0])
            auth = json.loads(data[0]['backupdata'][0][6][0])

            d = [company, products,purchases,adjustments,salessummary, salesitems, auth]          
            return d


class jsonclass:
    def AddNewSalesJson(cartitems):
        if not os.path.exists('sales_data.json'):
            data_str = json.dumps([cartitems])
            with open('sales_data.json', 'w') as file:
                data = file.write(data_str)
                file.close()
        else:
            with open('sales_data.json', 'r+') as file:
                data = json.load(file)
                data.append(cartitems)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(data, file, indent=4)


    def iNumb():
        iNo= ""
        if not os.path.exists('basket.json'):
            iNo = 1
            #print(iNo)
            return iNo
        else:
            with open('basket.json', 'r+') as file:
                data = json.load(file)
                if data:          
                    iNo = max([i['iNo'] for i in data]) + 1
                else:
                    iNo = 1
                #print(iNo)
                return iNo


    def Addtobskt(itms):
        if not os.path.exists('basket.json'):
            data_str = json.dumps([itms])
            with open('basket.json', 'w') as file:
                data = file.write(data_str)
                
                
        else:
            with open('basket.json', 'r+') as file:
                data = json.load(file)
                data.append(itms)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(data, file, indent=4)


    def loadbskt(self):
        try:
            with open('basket.json', 'r+') as file:
                bskt = []
                data = json.load(file)       
                for i in data:
                    lst = [i['iNo'], i['items'][0], int(i['items'][1]), float(i['items'][2]), round(float(i['items'][3]),2)]
                    bskt.append(lst)
            #print(bskt)
        except:
            return None
        return bskt
    
    
    def addto_salesitems(dt,rct):
        a = jsonclass().loadbskt()
        salesitems = []
        for i in a:
            item = (dt,rct, i[1], i[2], i[3])
            salesitems.append(item)
        #print(salesitems)
        return salesitems


    def QtyIncrease(iNo):
        with open('basket.json', 'r+') as file:
            data = json.load(file)       
            for i in data:
                if i['iNo'] == iNo:
                    i['items'][1] = int(i['items'][1]) + 1
                    i['items'][3] = round(i['items'][1] * i['items'][2],2)
                    file.seek(0)  # rewind
                    json.dump(data, file, indent=4)
                    file.truncate()
            

    def QtyDecrease(iNo):
        with open('basket.json', 'r+') as file:
            data = json.load(file)       
            for i in data:
                if i['iNo'] == iNo and  i['items'][1] > 1:
                    i['items'][1] = i['items'][1] - 1
                    i['items'][3] = round(i['items'][1] * i['items'][2],2)
                    file.seek(0)  # rewind
                    json.dump(data, file, indent=4)
                    file.truncate()

    
    def clearJson():
        if os.path.exists("basket.json"):
            os.remove("basket.json")


    def deleteitem(iNo):
        with open('basket.json') as file:
            data = json.load(file)
            #print(data)
            for i in data:
                if i['iNo'] == iNo:
                    data.remove(i)
                    #print(data)
                    
        with open('basket.json', 'w') as data_file:
            data = json.dump(data, data_file, indent=4)                 


class salesdata:
    def receiptNo():
        rct = ""
        if not os.path.exists('sales_data.json'):
            rct = 1000
            #print(rct)
            return rct
        else:
            with open('sales_data.json', 'r+') as file:
                data = json.load(file)
                if data:          
                    rct = max([i['receipt#'] for i in data]) + 1
                else:
                    rct = 1000
                #print(rct)
            return rct


    def addtax(self,t):
        if not os.path.exists('tax.txt'):
            with open('tax.txt', 'w') as file:
                file.write(t)
        else:
            with open('tax.txt', 'w') as file:
                file.write(t)
    
    def getax(self):
        t = ""
        if not os.path.exists('tax.txt'):
            t=0.00
            return t
        else:
            with open('tax.txt', 'r+') as file:
                t = file.read()
                return t
                
            

    def todaysummary():
        dt = str(date.today())
        with open('sales_data.json', 'r+') as file:
            data = json.load(file)       
            for i in data:
                if i['date']==dt:
                    pass
                   # print(i['total'])
            total = sum([i['total'] for i in data if i['date']==dt])
            count = len([i for i in data if i['date']==dt ])
            #print(total)
            #print(count)
            return total,count
            

class db:

    def set_active_user(self,u):
        if not os.path.exists('user.txt'):
            with open('user.txt', 'w') as file:
                file.write(u)
        else:
            with open('user.txt', 'w') as file:
                file.write(u)
    

    def get_active_user(self):
        u = ""
        if not os.path.exists('user.txt'):
            u="user"
            return u
        else:
            with open('user.txt', 'r+') as file:
                u = file.read()
                return u



    def reset_json_file(self):
        data_str = json.dumps([])
        with open('sales_data.json', 'w') as file:
            data = file.write(data_str)
            file.close()
        


    def sales_stock_update(self,dt,rct):
        sales = jsonclass.addto_salesitems(dt=dt, rct=rct) #
        for i in sales: 
            Database().update_stock_qty(item=i[2], qty=i[3])


    def getAllProduct(self):
        allProduct = Database().get_all_data(table='products')
        #print(allProduct)
        return allProduct

    def getstockvalue(self):
        stockvalue = Database().get_stock_value()
        #print(stockvalue)
        return stockvalue
    
    def getusers(self):
        users = Database().get_users()
        #print(users)
        return users
    
    def getuser_detail(self,id):
        users = Database().get_user_detail(id=id)
        #print(users)
        return users

    def add_single_product(self,val):
        Database().insert_single_product(val=val)


    def add_new_stock(self,val):
        Database().add_to_purch(val=val)


    def add_to_adjustment_table(self,val):
        Database().add_to_adjst(val=val)    
    

    def add_new_user(self,val):
        Database().insert_new_user(val=val)
    

    def get_product_count(self):
        count = " Product Count: {:,.0f}".format(Database().get_product_count())
        return count


    def get_total_stock_value(self):
        total = "TOTAL STOCK VALUE GHS {:,.2f}".format(Database().get_total_stock_value()) 
        return total
    
    def update_product_price(self,id, p):
        Database().update_product_price(id=id, p=p)
    
    def update_users(self,a,b,c,d,e,f,g,h,id):
        Database().update_usertable(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, id=id)
    

    def delete_product_from_db(self, t, id):
        Database().delete_from_db(table=t, id=id)
    
    def delete_user_from_db(self, id):
        Database().delete_user_db(id=id)
    

    def add_to_salessummary(self,val):
        Database().insert_single_salessummary(val=val)

    
    def add_to_salesitems(self, dt, rct):
        lst = jsonclass.addto_salesitems(dt=dt, rct=rct)
        Database().add_to_salesitems(lst=lst)


    def get_monthlysummary(self,yr):
        d = [f'{calendar.month_abbr[int(i[0])]}: {"GHS {:,.2f}".format(i[1])}' for i in Database().monthlysummaries(yr=yr)]
        return d


    def get_max_month_sales(self,yr):
        d = Database().monthlysummaries(yr=yr)
        return d

    def get_sales_yrs(self):
        yrs = [i[0] for i in Database().get_years()][-5:]
        return yrs


    def average_monthly_sales(self):
        try:
            s = Database().monthlysummaries_all()
            lst = [i[0] for i in s]
            avg = sum(lst) / len(lst)
            avrg = "GHS {:,.2f}".format(avg)
        except:
            avrg = "GH 0.00"
        #print(avrg)
        return avrg


    def average_daily_sales(self):
        try:
            s = Database().daily_sales_all()
            lst = [i[0] for i in s]
            avg = sum(lst) / len(lst)
            avrg = "GHS {:,.2f}".format(avg)
        except:
            avrg= "GH 0.00"
        #print(avrg)
        return avrg


    def average_daily_customer(self):
        try:
            a = Database().dailycustomer()
            avgC = roundup2(sum([i[0] for i in a]) / len(a))
        except:
            avgC=0
        return avgC


    def max_daily_sales(self):
        s = Database().daily_sales_all()
        if not s == []:
            lst = [i[0] for i in s]
            m = max(lst)
            mx = "GHS {:,.2f}".format(m)
            #print(avrg)
            return mx


    def YTD(self):
        s = Database().year_to_date_sales(yr=str(date.today().year))
        s = Database().year_to_date_sales(yr=str(date.today().year))[0][0]
        ytd = "GHS {:,.2f}".format(s)
        #print(ytd)
        return ytd


class dbReport:
    def daily_sales_report(dt):
        r = Database().dailysalesreport(dt=dt)
        return r

    def monthly_sales_report(yr, mnt):
        r = Database().monthlydailysales(yr=yr, mnt=mnt)
        return r

    def yearly_sales_summary(yr):
        r = [(calendar.month_name[int(i[0])],round(i[1],2)) for i in Database().monthlysummaries(yr=yr)]
        return r



    def download_daily_sales_as_xlsx(p,dt):
        rpt = dbReport.daily_sales_report(dt=dt)
        col = ["No.", "Item", "qty", "Price", "Amount"]
        typ = "DAILY SALES REPORT"
        prd = str(dt)
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    def download_daily_sales_as_pdf(p,dt):
        rpt = dbReport.daily_sales_report(dt=dt)
        col = ["No.", "Item", "qty", "Price", "Amount"]
        typ = "DAILY SALES REPORT"
        prd = str(dt)
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass


    def download_monthly_sales_as_xlsx(p,yr,mnt):
        rpt = dbReport.monthly_sales_report(yr=yr, mnt=mnt)
        col = ["Date", "Sales"]
        typ = "MONTHLY SALES SUMMARY"
        prd = f'{yr}: {calendar.month_name[int(mnt)]}'
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    def download_monthly_sales_as_pdf(p,yr,mnt):
        rpt = dbReport.monthly_sales_report(yr=yr, mnt=mnt)
        col = ["Date", "Sales"]
        typ = "MONTHLY SALES SUMMARY"
        prd = f'{yr}: {calendar.month_name[int(mnt)]}'
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    
    def download_yearly_summary_as_xlsx(p,yr):
        rpt = dbReport.yearly_sales_summary(yr=yr)
        col = ["Month", "Sales"]
        typ = "YEARLY SALES SUMMARY"
        prd = f'{yr}'
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    def download_yearly_summary_as_pdf(p,yr):
        rpt = dbReport.yearly_sales_summary(yr=yr)
        col = ["Month", "Sales"]
        typ = "YEARLY SALES SUMMARY"
        prd = f'{yr}'
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass


    def download_stock_qty_as_xlsx(p):
        rpt = [(i[0], i[1], i[3]) for i in db().getstockvalue()] #stck_qty
        col = ["No", "Product", "qty on hand"]
        typ = "Stocks available"
        prd = f'{date.today()}'
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    def download_stock_qty_as_pdf(p):
        rpt = [(i[0], i[1], i[3]) for i in db().getstockvalue()] #stck_qty
        col = ["No", "Product", "qty on hand"]
        typ = "Stocks available"
        prd = f'{date.today()}'
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    
    def download_out_out_of_stocks_as_xlsx(p):
        rpt = [(i[0], i[1], i[3]) for i in db().getstockvalue() if i[3] < 1] #out of stcks_qty
        col = ["No", "Product", "qty on hand"]
        typ = "Stocks out"
        prd = f'{date.today()}'
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    def download_out_out_of_stocks_as_pdf(p):
        rpt = [(i[0], i[1], i[3]) for i in db().getstockvalue() if i[3] < 1] #out of stcks_qty
        col = ["No", "Product", "qty on hand"]
        typ = "Stocks out"
        prd = f'{date.today()}'
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass



    def download_stocks_valuation_as_xlsx(p):
        rpt = db().getstockvalue()
        col = ["No", "Product", "Price", "Qty", "Value"]
        typ = "Stocks valuation at sales"
        prd = f'{date.today()}'
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    def download_stocks_valuation_as_pdf(p):
        rpt = db().getstockvalue()
        col = ["No", "Product", "Price", "Qty", "Value"]
        typ = "Stocks valuation at sales"
        prd = f'{date.today()}'
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass
    
    
    def download_stocks_adjustments_as_xlsx(p):
        rpt = Database().stock_ajstments_report()
        col = ["Date", "Product", "Qty"]
        typ = "Stocks adjustments report"
        prd = f'{date.today()}'
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    def download_stocks_adjustments_as_pdf(p):
        rpt = Database().stock_ajstments_report()
        col = ["Date", "Product", "Qty"]
        typ = "Stocks adjustments report"
        prd = f'{date.today()}'
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass


    def download_stocks_received_as_xlsx(p):
        rpt = Database().stock_received_report()
        col = ["Date", "Product", "Qty"]
        typ = "Stocks Received report"
        prd = f'{date.today()}'
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    def download_stocks_received_as_pdf(p):
        rpt = Database().stock_received_report()
        col = ["Date", "Product", "Qty"]
        typ = "Stocks Received report"
        prd = f'{date.today()}'
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass



    def download_productsales_history_as_xlsx(p, k):
        rpt = Database().productsaleshistory(item=k)
        col = ["Date", "Product", "ReceiptNo", "Qty", "Price", "Amount"]
        typ = f"Product sales history"
        prd = f'{date.today()}'
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass


    def download_productsales_history_as_pdf(p, k):
        rpt = Database().productsaleshistory(item=k)
        col = ["Date", "Product", "ReceiptNo", "Qty", "Price", "Amount"]
        typ = f"Product sales history"
        prd = f'{date.today()}'
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass
    

    def download_top_selling_as_xlsx(p, k):
        d = Database().productsales()
        rpt = d[:int(k)]
        col = ["No", "Product",  "Qty sold"]
        typ = f"Top {k} moving product"
        prd = f'{date.today()}'
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass


    def download_top_selling_as_pdf(p, k):
        d = Database().productsales()
        rpt = d[:int(k)]
        col = ["No", "Product",  "Qty sold"]
        typ = f"Top {k} moving product"
        prd = f'{date.today()}'
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass

    
    def download_least_selling_as_xlsx(p, k):
        d = Database().productsales()
        rpt = d[len(d)-int(k):]
        col = ["No", "Product",  "Qty sold"]
        typ = f"Bottom {k} Non-moving product"
        prd = f'{date.today()}'
        xl().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass


    def download_least_selling_as_pdf(p, k):
        d = Database().productsales()
        rpt = d[len(d)-int(k):]
        col = ["No", "Product",  "Qty sold"]
        typ = f"Bottom {k} Non-moving product"
        prd = f'{date.today()}'
        pdf().generatereportsheet(rpt=rpt, col=col, typ=typ, prd=prd, p=p)
        pass


class xl:
    def generatereportsheet(self,rpt,col,typ,prd,p):
        workbook = xlsxwriter.Workbook(p)
        worksheet = workbook.add_worksheet()
        report = rpt 
        bus_name = Database().get_busines_profile()[0]

        #data_Font formatting
        dff = workbook.add_format(
            {'font_name': 'Courier New',
              'font_size':12
              }
            
            )
        
        #header_Font formatting
        hff = workbook.add_format(
            {'font_name': 'Courier New',
              'font_size':13,
              'bold':True,
              'align': 'center',
              }
            
            )
        

        # bold format
        font_bold = workbook.add_format()
        font_bold.set_bold()

        # underline format
        bb = workbook.add_format()
        bb.set_bottom(2)


        worksheet.merge_range("B3:H3", "Merged Range")
        worksheet.merge_range("B4:H4", "Merged Range")
        worksheet.merge_range("B5:H5", "Merged Range", bb)

        worksheet.write('B3', bus_name, hff)
        worksheet.write('B4', typ, hff)
        worksheet.write('B5', prd, hff)

        worksheet.set_column('D:D', 40)


        #headers
        col = col
        for col_num, data in enumerate(col, start=2):
            worksheet.write(7, col_num, data, hff)


        for i, row in enumerate(report, start=8):
            for j, value in enumerate(row, start=2):
                worksheet.write(i, j, value, dff)
        workbook.close()
        pass


class pdf:    
    def generatereportsheet(self,rpt,col,typ,prd,p):
        bus_name = Database().get_busines_profile()[0]
        doc = SimpleDocTemplate(
                filename=p,
                pagesize=A4,
                rightMargin=72, leftMargin=72,
                topMargin=72, bottomMargin=18,
                )
        spc = Spacer(1, 0.25*inch)
        styles = getSampleStyleSheet()


        flowables = []
        company_name = bus_name
        report_typ = typ
        report_dt = prd
        ln = f"{ '_' * 70}"

        h1 = Paragraph(company_name, style=styles["Normal"])
        h2 = Paragraph(report_typ, style=styles["Normal"])
        h3 = Paragraph(report_dt, style=styles["Normal"])
        L = Paragraph(ln, style=styles["Normal"])
        
        col = col
        data = rpt
        data.insert(0, col)
        tbl = Table(data)
    

        flowables.append(h1)
        flowables.append(h2)
        flowables.append(h3)
        flowables.append(L)
        flowables.append(spc)
        flowables.append(tbl)


        doc.build(flowables)


class dummy:
    def load_dummy(self):
        dummy_data = pathlib.Path(r"C:\Users\User\Desktop\retail_dummy.xlsx")
       # Database().reset_product_table()
       # Database().insert_bulk_product(f=dummy_data)
       # Database().insert_bulk_purchases(f=dummy_data)
       # Database().insert_bulk_adjustments(f=dummy_data)
       # Database().insert_bulk_salessummary(f=dummy_data)
       # Database().insert_bulk_salesitems(f=dummy_data)



