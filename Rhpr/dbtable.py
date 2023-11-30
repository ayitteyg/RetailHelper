import sqlite3
import os, json
import pandas as pd


class Database:
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        db = os.path.join(path, 'database.db')
        self.connect = sqlite3.connect(db)
        self.cur = self.connect.cursor()

    def createTables(self):
        c = self.cur
        conn = self.connect


        comp = """
                    CREATE TABLE if not exists company
                    (
                    name    CHAR(50) DEFAULT businessName NOT NULL,
                    address    CHAR(50) DEFAULT businessBox,
                    location    CHAR(50) DEFAULT businessLocation NOT NULL,
                    contact1    CHAR(13) DEFAULT contact1 NOT NULL,
                    contact2    CHAR(12) DEFAULT contact2,
                    email     CHAR(50) DEFAULT businessMail
                    ) 

                    """
        c.execute(comp)


        products = """
                    CREATE TABLE if not exists products
                    (productId INTEGER PRIMARY KEY AUTOINCREMENT,
                    productName    CHAR(50) NOT NULL,
                    productPrice   REAL     NOT NULL,
                    productQty     INT      NOT NULL,
                    productCat     CHAR(50)
                    ) 

                    """
        c.execute(products)

        purch = """
                    CREATE TABLE if not exists purchases
                    (productId INTEGER PRIMARY KEY AUTOINCREMENT,
                    purchdate DATE NOT NULL,
                    productName    CHAR(50) NOT NULL,
                    productQty     INT      NOT NULL,
                    productCat     CHAR(50)
                    ) 

                    """
        c.execute(purch)
        #print("purchases table created")

        
        adjst = """
                    CREATE TABLE if not exists adjustments
                    (productId INTEGER PRIMARY KEY AUTOINCREMENT,
                    adjstdate DATE NOT NULL,
                    productName    CHAR(50) NOT NULL,
                    productQty     INT      NOT NULL,
                    productCat     CHAR(50)
                    ) 

                    """
        c.execute(adjst)
        #print("adjustment table created")



        salessummary = """
                    CREATE TABLE if not exists salessummary
                    (salesId INTEGER PRIMARY KEY AUTOINCREMENT,
                    salesDate    DATE  NOT NULL,
                    salesRct   CHAR(10)     NOT NULL,
                    salesTotal     REAL      NOT NULL,
                    salesPerson     CHAR(50)  NOT NULL,
                    salesItem   INT NOT NULL
                    ) 

                    """
        c.execute(salessummary)
        #print("salessummary table created")


        salesitems = """
                    CREATE TABLE if not exists salesitems
                    (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    iDate    DATETIME NOT NULL,
                    iReceipt    CHAR(10) NOT NULL,
                    Item   CHAR(50) NOT NULL,
                    Qty   INT NOT NULL,
                    Price   REAL NOT NULL
                    ) 

                    """
        c.execute(salesitems)
        #print("salesitems table created")S

        
        auth = """
                    CREATE TABLE if not exists auth
                    (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fname    CHAR(100) NOT NULL,
                    username   CHAR(5) NOT NULL,
                    contact   CHAR(10) NOT NULL,
                    mail   CHAR(30) ,
                    pwd   CHAR(20) NOT NULL,
                    active  BOOLEAN DEFAULT 0 NOT NULL,
                    added DATE NOT NULL,
                    status CHAR(10) NOT NULL
                    ) 

                    """
        c.execute(auth)
        #print("auth table created")


        conn.commit()
        conn.close()


    def drop_table(self, table):
        cur = self.cur
        conn = self.connect
        query = f"""
               drop table if exists
               {table}               
               """
        cur.execute(query)
        conn.commit()
        conn.close()


    def drop_all_tables(self):
        cur = self.cur
        conn = self.connect
        a = """ drop table if exists company """
        cur.execute(a)

        b = """ drop table if exists products """
        cur.execute(b)
        
        c = """ drop table if exists purchases """
        cur.execute(c)

        d = """ drop table if exists adjustments """
        cur.execute(d)

        e = """ drop table if exists salessummary """
        cur.execute(e)

        f = """ drop table if exists salesitems """
        cur.execute(f)

        g = """ drop table if exists auth """
        cur.execute(g)

        conn.commit()
        

    def add_bulk_salessummary(self,lst):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into salessummary (salesDate,salesRct,salesTotal,salesPerson,salesItem) 
                values (?,?,?,?,?)
            """
        val = lst
        cur.executemany(q, val)
        conn.commit()
        conn.close()
    

    def add_bulk_salesitems(self,lst):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into salesitems (iDate,iReceipt,Item,Qty,Price) 
                values (?,?,?,?,?)
            """
        val = lst
        cur.executemany(q, val)
        conn.commit()
        conn.close()

    def add_bulk_product(self,lst):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into products (productName,productPrice,productQty,productCat) 
                values (?,?,?,?)
            """
        val = lst
        cur.executemany(q, val)
        conn.commit()
        conn.close()


    def add_business_profile(self, val):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into company (name,address,location,contact1,contact2,email) 
                values (?,?,?,?,?,?)
               
            """
        cur.execute(q,val)
        conn.commit()
        conn.close()


    def insert_bulk_salessummary(self,f):
        db = pd.read_excel(f, sheet_name='salessummary')
        db['salesDate'] = db['salesDate'].apply(lambda x: x.strftime("%Y-%m-%d"))
        db = db.fillna('None')
        lst = list(db.itertuples(index=False, name=None))
        #print(lst)
        self.add_bulk_salessummary(lst=lst)
    

    def insert_bulk_salesitems(self,f):
        db = pd.read_excel(f, sheet_name='salesitems')
        db['iDate'] = db['iDate'].apply(lambda x: x.strftime("%Y-%m-%d"))
        db = db.fillna('None')
        lst = list(db.itertuples(index=False, name=None))
        #print(lst)
        self.add_bulk_salesitems(lst=lst)


    def insert_bulk_purchases(self,f):
        db = pd.read_excel(f, sheet_name='purchases')
        db['purchdate'] = db['purchdate'].apply(lambda x: x.strftime("%Y-%m-%d"))
        db = db.fillna('None')
        lst = list(db.itertuples(index=False, name=None))
        #print(lst)
        self.add_bulk_purch(val=lst)


    def insert_bulk_adjustments(self,f):
        db = pd.read_excel(f, sheet_name='adjustments')
        db['adjstdate'] = db['adjstdate'].apply(lambda x: x.strftime("%Y-%m-%d"))
        db = db.fillna('None')
        lst = list(db.itertuples(index=False, name=None))
        #print(lst)
        self.add_bulk_adjst(val=lst)


    def add_bulk_purch(self, val):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into purchases (purchdate,productName,productQty) 
                values (?,?,?)
            """
        cur.executemany(q, val)
        conn.commit()
        conn.close()

  
    def add_bulk_adjst(self, val):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into adjustments (adjstdate,productName,productQty) 
                values (?,?,?)
            """
        cur.executemany(q, val)
        conn.commit()
        conn.close()


    def add_to_purch(self, val):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into purchases (purchdate,productName,productQty) 
                values (?,?,?)
            """
        cur.execute(q, val)
        conn.commit()
        conn.close()


    def add_to_adjst(self, val):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into adjustments (adjstdate,productName,productQty) 
                values (?,?,?)
            """
        cur.execute(q, val)
        conn.commit()
        conn.close()


    def insert_bulk_product(self,f):
        db = pd.read_excel(f, sheet_name='products')
        db = db.fillna('None')
        lst = list(db.itertuples(index=False, name=None))
        #print(lst)
        self.add_bulk_product(lst=lst)


    def insert_single_product(self, val):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into products (productName,productPrice,productQty,ProductCat) 
                values (?,?,?,?)
               
            """
        cur.execute(q,val)
        conn.commit()
        conn.close()


    def insert_single_salessummary(self, val):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into salessummary (salesDate,salesRct,salesTotal,salesPerson,salesItem) 
                values (?,?,?,?,?)
               
            """
        cur.execute(q,val)
        conn.commit()
        conn.close()


    def add_to_salesitems(self, lst):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into salesitems (iDate,iReceipt,Item,Qty,Price) 
                values (?,?,?,?,?)
            """
        val = lst
        cur.executemany(q, val)
        conn.commit()
        conn.close()


    def set_default_business_profile(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into company (name,address,location,contact1,contact2,email) 
                values ("Simple Business Apps Solutions","Box 111","Ofankor-Barrier","+233","+233","ayittey.og@gmail.com")
               
            """
        cur.execute(q)
        conn.commit()
        conn.close()


    def update_business_profile(self, fld, val):
        cur = self.cur
        conn = self.connect
        query = f""" 
                UPDATE company                
                SET 
                {fld} = "{val}"             
            """
        cur.execute(query)
        conn.commit()
        conn.close()


    def set_app_default_user(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into auth (fname,username,contact,mail,pwd,active,added,status) 
                values ("developer","rhpr","0549053295","ayittey.og@gmail.com","12345","True","2023-01-01","superuser")
               
            """
        cur.execute(q)
        conn.commit()
        conn.close()


    def insert_new_user(self, val):
        cur = self.cur
        conn = self.connect
        q = f"""
                insert into auth (fname,username,contact,mail,pwd,active,added,status) 
                values (?,?,?,?,?,?,?,?)
               
            """
        cur.execute(q,val)
        conn.commit()
        conn.close()


    def get_superusers(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT username, pwd  FROM auth WHERE (status="superuser"  AND active="True")           
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def get_busines_profile(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT *  FROM company              
           """
        cur.execute(q)
        db = cur.fetchall()[0]
        conn.close()
        return db


    def get_active_users(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT username, pwd  FROM auth WHERE active = "True"             
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def get_allusers(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT username, pwd  FROM auth            
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def get_users(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT id,fname,username,contact,mail,"*********",active,added,status  FROM auth              
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def get_user_detail(self,id):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT *  FROM auth WHERE id={id}             
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def get_all_data(self, table):
        cur = self.cur
        conn = self.connect
        cur.execute(
            f""" select * from {table}""")
        db = cur.fetchall()
        conn.close()
        return db
    

    def stock_ajstments_report(self):
        cur = self.cur
        conn = self.connect
        cur.execute(
            f""" select adjstdate, productName, productQty from adjustments
                 ORDER BY adjstdate DESC
            
            """)
        db = cur.fetchall()
        conn.close()
        return db


    def stock_received_report(self):
        cur = self.cur
        conn = self.connect
        cur.execute(
            f""" select purchdate, productName, productQty from purchases
                  ORDER BY purchdate DESC
            """)
        db = cur.fetchall()
        conn.close()
        return db


    def get_stock_value(self):
        cur = self.cur
        conn = self.connect
        cur.execute(
            f""" select productId, productName, round(productPrice,2), productQty, round(productPrice * productQty,2) from products""")
        db = cur.fetchall()[200:]
        conn.close()
        return db
    

    def get_product_count(self):
        cur = self.cur
        conn = self.connect
        cur.execute(
            f""" select count(*) from products""")
        db = cur.fetchall()[0][0]
        conn.close()
        return db
    

    def get_products(self):
        cur = self.cur
        conn = self.connect
        cur.execute(
            f""" select productName from products""")
        db = cur.fetchall()
        conn.close()
        return db


    def get_total_stock_value(self):
        cur = self.cur
        conn = self.connect
        cur.execute(
            f""" select coalesce(sum(productPrice * productQty),0)  from products""")
        db = cur.fetchall()[0][0]
        conn.close()
        return db
    

    def update_product_price(self, p, id):
        cur = self.cur
        conn = self.connect
        query = f""" 
                UPDATE products                
                SET productPrice = {p}
                WHERE productId = {id}
               
            """
        cur.execute(query)
        conn.commit()
        conn.close()
    

    def stock_adjst(self, item, qty):
        cur = self.cur
        conn = self.connect
        query = f""" 
                UPDATE products                
                SET productQty = productQty + {qty}
                WHERE productName = "{item}"
               
            """
        cur.execute(query)
        conn.commit()
        conn.close()
    

    def update_stock_qty(self, item, qty):
        cur = self.cur
        conn = self.connect
        query = f""" 
                UPDATE products                
                SET productQty = productQty - {qty}
                WHERE productName = "{item}"
               
            """
        cur.execute(query)
        conn.commit()
        conn.close()


    def update_usertable(self, a,b,c,d,e,f,g,h, id):
        cur = self.cur
        conn = self.connect
        query = f""" 
                UPDATE auth                
                SET 
                fname = "{a}",
                username = "{b}",
                contact = "{c}",
                mail = "{d}",
                pwd = "{e}",
                active = "{f}",
                added = "{g}",
                status = "{h}"
                WHERE Id = {id}
               
            """
        cur.execute(query)
        conn.commit()
        conn.close()
    

    def delete_user_db(self, id):
        cur = self.cur
        conn =  self.connect
        query = f""" delete FROM auth where Id = {id}"""
        cur.execute(query)
        conn.commit()
        conn.close()


    def price_print(self, id):
        cur = self.cur
        conn = self.connect
        cur.execute(
            f""" select productPrice from products where productId = {id}""")
        db = cur.fetchall()
        conn.close()
        return db
    

    def delete_from_db(self, table, id):
        cur = self.cur
        conn =  self.connect
        query = f""" delete FROM {table} where productId = {id}"""
        cur.execute(query)
        conn.commit()
        conn.close()
    

    def monthlysummaries(self, yr):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT * FROM 
                    (SELECT strftime('%m', salesDate) AS 'month', coalesce(sum(salesTotal),0) as m_sum 
                    FROM salessummary where strftime('%Y', salesDate) = "{yr}"
                    GROUP BY month) m 
                Where true
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def monthlysummaries2(self, yr):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT * FROM 
                    (SELECT strftime('%m', salesDate) AS 'month',  coalesce(sum(salesTotal),0) as m_sum, strftime('%Y-%m', salesDate) AS 'yrmnth'  
                    FROM salessummary where strftime('%Y', salesDate) = "{yr}"
                    GROUP BY month) m 
                Where true
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def get_years(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT DISTINCT (SELECT strftime('%Y', salesDate) AS 'yr') FROM salessummary              
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db
    

    def monthlysummaries_all(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT coalesce(sum(salesTotal),0), strftime('%Y-%m', salesDate) year_month
                FROM salessummary
                GROUP BY year_month
                ORDER BY year_month DESC
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def dailycustomer(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT coalesce(count(iReceipt),0),  iDate 
                FROM salesitems
                GROUP BY iDate
                
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def daily_sales_all(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT salesTotal FROM salessummary
                """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db
    

    def dailysales(self, mnth):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT * FROM 
                    (SELECT strftime('%d', salesDate) AS 'day', coalesce(sum(salesTotal),0) as d_sum 
                    FROM salessummary where strftime('%Y-%m', salesDate) = "{mnth}"
                    GROUP BY day) d
                Where true

            """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def year_to_date_sales(self,yr):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT coalesce(sum(salesTotal),0) as ytd FROM salessummary where strftime('%Y', salesDate) = "{yr}"
                """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def dailysalesreport(self,dt):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT Id,Item,Qty,Price, (Qty * Price)  FROM salesitems where iDate = "{dt}"
                """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def monthlydailysales(self,yr,mnt):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT  salesDate as d, sum(salesTotal) as s
                FROM salessummary
                WHERE (strftime('%Y', salesDate) = "{yr}" AND strftime('%m', salesDate) = "{mnt}")
                GROUP BY d
                              
           """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db


    def productsaleshistory(self,item):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT iDate,Item, iReceipt,Qty,Price, (Qty * Price)  FROM salesitems where Item = "{item}"
                """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db
    

    def saleshistory(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT iDate,Item,Qty,Price, (Qty * Price)  FROM salesitems
                """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db
    

    def productsales(self):
        cur = self.cur
        conn = self.connect
        q = f"""
                SELECT Id, Item, coalesce(sum(Qty),0)
                FROM salesitems
                GROUP BY Item
                ORDER BY Qty DESC


                """
        cur.execute(q)
        db = cur.fetchall()
        conn.close()
        return db
    

    def get_qty(self,i):
        cur = self.cur
        conn = self.connect
        cur.execute(
            f""" select productQty from products WHERE productName = "{i}" """)
        db = cur.fetchall()
        conn.close()
        return db
    

    def table_to_json(self):
        cur = self.cur
        conn = self.connect

        P = f""" SELECT json_object("company",
                json_group_array
                 (
                    json_object
                      (
                        'name', name, 
                        'address', address, 
                        'location', location,
                        'contact1', contact1,
                        'contact2', contact2,
                        'email', email
                        )
                 )
                ) result
             FROM company """   
        cur.execute(P)
        profile = cur.fetchall()[0]


        I = f""" SELECT json_object("products",
                json_group_array
                 (
                    json_object
                      (
                        'productId', productId, 
                        'productName', productName, 
                        'productPrice', productPrice,
                        'productQty', productQty
                        )
                 )
                ) result
             FROM products """       
        cur.execute(I)
        items = cur.fetchall()[0]

        
        ph = f""" SELECT json_object("purchases",
                json_group_array
                 (
                    json_object
                      (
                        'productId', productId, 
                        'purchdate', purchdate,
                        'productName', productName, 
                        'productQty', productQty
                        )
                 )
                ) result
             FROM purchases """       
        cur.execute(ph)
        purchases = cur.fetchall()[0]


        aj = f""" SELECT json_object("adjustments",
                json_group_array
                 (
                    json_object
                      (
                        'productId', productId, 
                        'adjstdate', adjstdate,
                        'productName', productName, 
                        'productQty', productQty
                        )
                 )
                ) result
             FROM adjustments """       
        cur.execute(aj)
        adjustments = cur.fetchall()[0]

        

        ss = f""" SELECT json_object("salessummary",
                json_group_array
                 (
                    json_object
                      (
                        'salesId', salesId, 
                        'salesDate', salesDate,
                        'salesRct', salesRct, 
                        'salesTotal', salesTotal,
                        'salesPerson', salesPerson,
                        'salesItem', salesItem
                        )
                 )
                ) result
             FROM salessummary """       
        cur.execute(ss)
        salessummary = cur.fetchall()[0]
 


        si = f""" SELECT json_object("salesitems",
                json_group_array
                 (
                    json_object
                      (
                        'Id', Id, 
                        'iDate', iDate,
                        'iReceipt', iReceipt, 
                        'Item', Item,
                        'Qty', Qty,
                        'Price', Price
                        )
                 )
                ) result
             FROM salesitems """       
        cur.execute(si)
        salesitems = cur.fetchall()[0]


        ath = f""" SELECT json_object("auth",
                json_group_array
                 (
                    json_object
                      (
                        'Id', Id, 
                        'fname', fname,
                        'contact', contact, 
                        'mail', mail,
                        'pwd', pwd,
                        'active', active,
                        'added', added,
                        'status', status
                        )
                 )
                ) result
             FROM auth """       
        cur.execute(ath)
        auth = cur.fetchall()[0]


        conn.close()
        return  profile, items, purchases, adjustments, salessummary, salesitems, auth
    

    def reset_databases(self):
        self.drop_all_tables()
        self.createTables()
        #self.set_app_default_user()
        #self.set_default_business_profile()
    

    def reset_product_table(self):
        c = self.cur
        conn = self.connect

        drop = """ drop table if exists products"""
        c.execute(drop)

        products = """
                    CREATE TABLE if not exists products
                    (productId INTEGER PRIMARY KEY AUTOINCREMENT,
                    productName    CHAR(50) NOT NULL,
                    productPrice   REAL     NOT NULL,
                    productQty     INT      NOT NULL,
                    productCat     CHAR(50)
                    ) 

                    """
        c.execute(products)
        conn.commit()
        conn.close()


   
    #next