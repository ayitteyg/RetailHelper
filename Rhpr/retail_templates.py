from flet import *
import flet as ft
from navbar import ModernNavBar
from myFunc import show_date, roundup
from datahandler import jsonclass, salesdata, db, dbReport, backupdata
from dbtable import Database
from datetime import date
import math
import calendar
import pathlib, os
from rprint import salesreceipt


#login class
class ApplicationLogin(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    

        self.username = TextField(label='Username', 
                border_radius=10,
                icon = ft.icons.PERSON,
                border=border.only(bottom=BorderSide(2,"BLue")))

        self.pwd = TextField(label='Password', 
                border_radius=10,
                password=True,
                can_reveal_password=True,
                icon=ft.icons.KEY,
                border=border.only(bottom=BorderSide(2,"BLue")))
        
        self.readme = readme()
        self.showpreadme = AlertDialog(modal=False, content=self.readme)



    def sign_in_submit(self, e):
        self.page.close_banner()
        #print("clicked")
        code = f"{self.username.value}:{self.pwd.value}"
        auth = [f"{k[0]}:{k[1]}" for k in Database().get_active_users()]

        #print(auth)
        #print(code)
        
        
        if code in auth:
            self.page.go("/homepage")
            db().set_active_user(u=self.username.value)

    
        else:
            msg = Banner(
                bgcolor="Amber", leading=Icon(icons.WARNING_ROUNDED),
                content=Text(value="Wrong credentials, either password or username is incorrect, Acess Denied"),
                actions=[
                    TextButton("Dismiss", on_click=self.close_banner)],
                ) 
            
            self.page.banner = msg
            msg.open = True
            self.update()
            self.page.update()
            self.page.close_banner()

       

    def close_banner(self,e):
        self.page.banner.open = False
        self.update()
        self.page.update()    
        



    def show_readme(self,e):
        self.page.dialog = self.showpreadme
        self.showpreadme.open = True
        self.update()
        self.page.update()



    def build(self):
        return Container(
                content=Column(
                    spacing=10,

                    controls=[
                    ApplicationBar(),    
                  
                   #Container( 
                       #alignment="center",
                   #    height = 80,
                   #    width = 130,
                   #    on_click=self.show_readme,
                   #     content=Row(
                   #         controls=[
                   #             Text(value="READ ME"),
                   #             Image("images/rdme3.png", width=50, height=80)
                   #         ]
                   #     )                       
                   #     ),


                    Row(alignment="center",
                        controls=[Image("images/lgin.jpg", width=100, height=130)]),

                    Row(alignment="center",
                        controls=[self.username]),
                    
                    Row(alignment="center",
                        controls=[self.pwd]),

                    Row(
                        alignment="center",       
                        controls=[
                            ElevatedButton(
                            text="LOG IN",
                            on_click=self.sign_in_submit),                        
                            ]),
                    Row(
                        alignment='center',
                        height=100,
                        controls=[Text(''),]),



                     Container(
                        height=180,
                        alignment=alignment.bottom_center,
                        #bgcolor="Red",
                        
                       content=None

                       #content=(
                            #ApplicationButtonBar()
                        
                        #)
                        ),


                    ]

                )
            )
          

#authenticate access
class authaccessproduct(UserControl):
    def __init__(self):
        super().__init__()
      

        self.pwd = TextField(label='Password', 
                border_radius=10,
                password=True,
                can_reveal_password=True,
                icon=ft.icons.KEY,
                border=border.only(bottom=BorderSide(2,"BLue")))
        

    def go_home(self,e):
        self.page.go(f"/homepage")
        #self.exit_banner_if_any()


    def sign_in_submit(self, e):
        self.page.close_banner()
        code = str(self.pwd.value)
        #print(code)
        
        auth = [k[1] for k in Database().get_superusers()]

        
        if code not in auth:
            msg = Banner(
                bgcolor="Amber", leading=Icon(icons.WARNING_ROUNDED),
                content=Text(value="Wrong code, Acess Denied"),
                 actions=[
                    TextButton("Dismiss", on_click=self.close_banner)],
                ) 
            
            self.page.banner = msg
            msg.open = True
            self.update()
            self.page.update()

        else:
            self.page.go("/productpage")
            #self.exit_banner_if_any()
            

        return code

    def exit_banner_if_any(self):
        if self.page.banner.open == True:
            self.page.banner.open = False
        self.update()
        self.page.update()
 

    def close_banner(self,e):
        self.page.banner.open = False
        self.update()
        self.page.update()



    def build(self):
        return Container(
                content=Column(
                    spacing=20,

                    controls=[
                    Container(
                        alignment=alignment.center,
                        #expand=True,
                        height=60,
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        bgcolor="#065080",

                        content = Row(
                            alignment="center",
                             controls =[
                                IconButton(icon=icons.KEY_OFF_ROUNDED, icon_color="White"),
                                Text(value="PASSWORD", font_family="Poppins Bold", size=18, color="Amber"),
                                #Text(value=""),
                                
                             ]),
                        ), 

                    Row(alignment="center",
                        controls=[Image("images/access1.png", width=100, height=130)]),

                    
                    Row(alignment="center",
                        controls=[self.pwd]),

                    Row(
                        alignment="center",       
                        controls=[
                            ElevatedButton(
                            text="Enter",
                            on_click=self.sign_in_submit),

                            IconButton(icon=icons.HOME_OUTLINED, icon_color="Black", on_click=self.go_home),                        
                            ]
                            
                            
                            ),
                   
                    ]

                )
            )


class authaccessuser(UserControl):
    def __init__(self):
        super().__init__()
      

        self.pwd = TextField(label='Password', 
                border_radius=10,
                password=True,
                can_reveal_password=True,
                icon=ft.icons.KEY,
                border=border.only(bottom=BorderSide(2,"BLue")))
        

    def go_home(self,e):

        self.page.go(f"/homepage")
        #self.exit_banner_if_any()


    def sign_in_submit(self, e):
        self.page.close_banner()
        code = str(self.pwd.value)
        #print(code)
        
        auth = [k[1] for k in Database().get_superusers()]

        if code not in auth:
            msg = Banner(
                bgcolor="Amber", leading=Icon(icons.WARNING_ROUNDED),
                content=Text(value="Wrong code, Acess Denied"),
                 actions=[
                    TextButton("Dismiss", on_click=self.close_banner)],
                ) 
            
            self.page.banner = msg
            msg.open = True
            self.update()
            self.page.update()

        else:
            self.page.go("/useraccess")
            #self.exit_banner_if_any()
            

        return code

    def exit_banner_if_any(self):
        if self.page.banner.open == True:
            self.page.banner.open = False
        self.update()
        self.page.update()
 

    def close_banner(self,e):
        self.page.banner.open = False
        self.update()
        self.page.update()



    def build(self):
        return Container(
                content=Column(
                    spacing=20,

                    controls=[
                    Container(
                        alignment=alignment.center,
                        #expand=True,
                        height=60,
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        bgcolor="#065080",

                        content = Row(
                            alignment="center",
                             controls =[
                                IconButton(icon=icons.KEY_OFF_ROUNDED, icon_color="White"),
                                Text(value="PASSWORD", font_family="Poppins Bold", size=18, color="Amber"),
                                #Text(value=""),
                                
                             ]),
                        ), 

                    Row(alignment="center",
                        controls=[Image("images/access1.png", width=100, height=130)]),

                    
                    Row(alignment="center",
                        controls=[self.pwd]),

                    Row(
                        alignment="center",       
                        controls=[
                            ElevatedButton(
                            text="Enter",
                            on_click=self.sign_in_submit),

                            IconButton(icon=icons.HOME_OUTLINED, icon_color="Black", on_click=self.go_home),                        
                            ]
                            
                            
                            ),
                   
                    ]

                )
            )


class authaccesssettings(UserControl):
    def __init__(self):
        super().__init__()
      

        self.pwd = TextField(label='Password', 
                border_radius=10,
                password=True,
                can_reveal_password=True,
                icon=ft.icons.KEY,
                border=border.only(bottom=BorderSide(2,"BLue")))
        

    def go_home(self,e):

        self.page.go(f"/homepage")
        #self.exit_banner_if_any()


    def sign_in_submit(self, e):
        self.page.close_banner()
        code = str(self.pwd.value)
        #print(code)
        
        auth = [k[1] for k in Database().get_superusers()]

        if code not in auth:
            msg = Banner(
                bgcolor="Amber", leading=Icon(icons.WARNING_ROUNDED),
                content=Text(value="Wrong code, Acess Denied"),
                 actions=[
                    TextButton("Dismiss", on_click=self.close_banner)],
                ) 
            
            self.page.banner = msg
            msg.open = True
            self.update()
            self.page.update()

        else:
            self.page.go("/appsettings")
            pass
            

        return code

    def exit_banner_if_any(self):
        if self.page.banner.open == True:
            self.page.banner.open = False
        self.update()
        self.page.update()
 

    def close_banner(self,e):
        self.page.banner.open = False
        self.update()
        self.page.update()



    def build(self):
        return Container(
                content=Column(
                    spacing=20,

                    controls=[
                    Container(
                        alignment=alignment.center,
                        #expand=True,
                        height=60,
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        bgcolor="#065080",

                        content = Row(
                            alignment="center",
                             controls =[
                                IconButton(icon=icons.KEY_OFF_ROUNDED, icon_color="White"),
                                Text(value="PASSWORD", font_family="Poppins Bold", size=18, color="Amber"),
                                #Text(value=""),
                                
                             ]),
                        ), 

                    Row(alignment="center",
                        controls=[Image("images/access1.png", width=100, height=130)]),

                    
                    Row(alignment="center",
                        controls=[self.pwd]),

                    Row(
                        alignment="center",       
                        controls=[
                            ElevatedButton(
                            text="Enter",
                            on_click=self.sign_in_submit),

                            IconButton(icon=icons.HOME_OUTLINED, icon_color="Black", on_click=self.go_home),                        
                            ]
                            
                            
                            ),
                   
                    ]

                )
            )


class Appsettings(UserControl):
    def __init__(self):
        super().__init__()

        try:
            self.a =  Database().get_all_data(table="company")[0]
        except:
            self.a = "Bussiness name"

        self.taxcontainer = Column(spacing=1, height=80, width=100)
        self.tax = AlertDialog(modal=False, title=Text(value="Tax update", size=15), content=self.taxcontainer)


        self.profile = Bprofile()
        self.showprofile = AlertDialog(modal=False, content=self.profile)

        self.profileUpdate = Column(spacing=10, height=450, width=350)
        self.profileUpdateForm = AlertDialog(modal=False, title="", content=self.profileUpdate)
       

        self.pick_files_dialog = FilePicker(on_result=self.pick_files_result)
        self.selected_files = Text()


        self.confirm_reset = AlertDialog(
                modal=True,
                title=Text("Please confirm"),
                content=Text("Do you really want to reset databases? This action Initializes the app"),
                actions=[
                    TextButton("Yes", on_click=self.yes_reset),
                    TextButton("No", on_click=self.close_reset_confirm),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=self.close_reset_confirm)
                


        self.confirm_backup = AlertDialog(
                modal=False,
                title=Text("Please confirm"),
                content=Text("Backup / Restore data?"),
                actions=[
                    TextButton("Create Backup", on_click=self.yes_backup),
                    TextButton("Restore Backup", on_click=self.yes_restore_backup, on_hover="", disabled=True),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=self.close_confirm_backup)
        
       
        self.opt = RadioGroup(content=Column(alignment="SpaceBetween",
            controls=[
                Radio(value="yes", label="Clear All existing Product & price list"),
                Radio(value="no", label="Add to existing Product & price list"),
                 ]), 
                 #on_change=radiogroup_changed
                 )
        
        self.confirm_upload = AlertDialog(
                modal=False,
                title=Text("Product Price List upload"),
                content= Column(
                        height=240,
                    controls=[
                        Text("This might require ADMIN assistance!!", color="Red", font_family="Poppins Bold"),
                        Text("1. Save product price list and initial quantites as .xlsx file"),
                        Text("2. Select file to upload"),
                        Text("3. You can later update at the product section"),
                        Text(value=""),
                        Text(value="CHOOSE OPTION", color="#641E16", size=12),
                        self.opt,                        
                        ]
                     ), 
                actions=[
                    TextButton(text="upload", on_click=lambda e: self.pick_files_dialog.pick_files()),
                    #self.Txtbutt,
                      ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=self.close_confirm_backup)
        
        
        self.confirm_upload.actions.append(self.pick_files_dialog)
        

    def taxupdate(self,e):
        self.taxcontainer.controls.clear()
        v = salesdata().getax()
        t = TextField(label="tax",border_radius=8, icon=icons.PASSWORD_OUTLINED, on_submit=self.add_tax, value=v)
        self.taxcontainer.controls.append(t)
       
        self.page.dialog = self.tax
        self.tax.open = True
        self.page.update()
        #pass


    def add_tax(self,e):
        t = e.control.value
        
        salesdata().addtax(t=t)
        #print("action here")

        msg = SnackBar(content=Text(f"Tax value updated"), action="OK", bgcolor="#065080")
        self.page.snack_bar = msg
        msg.open = True

        self.page.dialog.open = False
        self.update()
        self.page.update()

    def change_date(self,e):
        print(self.date_picker.value)


    def pick_files_result(self, e: FilePickerResultEvent):
        self.page.close_banner()
        ff = (", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!")
        f = pathlib.Path(ff)
        opt = self.opt.value
        print(opt)

        if opt == "yes":
            Database().reset_product_table()
            Database().insert_bulk_product(f=f)

            
            msg = SnackBar(content=Text(f"product price list file uploading..."), action="", bgcolor="#065080")
            self.page.snack_bar = msg
            msg.open = True
            self.close_confirm_upload(e=e)
        
        if opt == "no":
            Database().insert_bulk_product(f=f)

            msg = SnackBar(content=Text(f"product price list file uploading..."), action="", bgcolor="#065080",)
            self.page.snack_bar = msg
            msg.open = True
            self.close_confirm_upload(e=e)

        
        if opt == None:
            
            msg = Banner(
                bgcolor="Amber", leading=Icon(icons.WARNING_ROUNDED),
                content=Text(value="No option choosen, Upload CANCELLED"),
                actions=[
                    TextButton("Ok", on_click=self.close_banner)],
                ) 
            
            self.page.banner = msg
            msg.open = True
            self.update()
            self.page.update()


    def close_banner(self,e):
        self.page.banner.open = False
        self.update()
        self.page.update()  
       

    def open_reset_confirm(self,e):
        self.page.dialog = self.confirm_reset
        self.confirm_reset.open = True
        self.update()
        self.page.update()

    
    def open_backup_confirm(self,e):
        self.page.dialog = self.confirm_backup
        self.confirm_backup.open = True
        self.update()
        self.page.update()


    def open_upload_confirm(self,e):
        self.page.dialog = self.confirm_upload
        self.confirm_upload.open = True
        self.update()
        self.page.update()


    def close_reset_confirm(self,e):
        self.confirm_reset.open = False
        self.update()
        self.page.update()
    

    def close_confirm_backup(self,e):
        self.confirm_backup.open = False
        self.update()
        self.page.update()
    

    def close_confirm_upload(self,e):
        self.confirm_upload.open = False
        self.update()
        self.page.update()



    def yes_reset(self,e):
        Database().reset_databases()
        Database().set_app_default_user()
        Database().set_default_business_profile()
        db().reset_json_file()

        msg = SnackBar(content=Text(f"Databases Resetted"), action="App has been initialized!!", bgcolor="#065080")
        self.page.snack_bar = msg
        msg.open = True
        self.close_reset_confirm(e=e)
        pass


    def yes_backup(self,e):
        backupdata.save_backup(b={"backup_data": Database().table_to_json()})
        msg = SnackBar(content=Text(f"Backup data at: C:/Rhpr "), action="Back up file created on local disk")
        self.page.snack_bar = msg
        msg.open = True
        self.close_confirm_backup(e=e)
        pass


    def yes_restore_backup(self,e):
        msg = SnackBar(content=Text(f"Backup Restore "), action="")
        self.page.snack_bar = msg
        msg.open = True
        self.close_confirm_backup(e=e)
        pass

    
    def yes_upload(self,e):
        opt = self.opt.value
        print(opt)
        msg = SnackBar(content=Text(f"product price list file uploading..."), action="", bgcolor="#065080")
        self.page.snack_bar = msg
        msg.open = True
        self.close_confirm_upload(e=e)
        pass

 

    def go_home(self,e):
        self.page.go(f"/homepage")
        #self.exit_banner_if_any()

    def view_profile(self,e):
        self.page.dialog = self.showprofile
        self.showprofile.open = True
        self.page.update()


    def updateProfile(self,e):
        self.profileUpdate.controls.clear()
        #print("selected")
        
        name = self.a[0]
        box =  self.a[1]
        loc =  self.a[2]
        cont1 =  self.a[3]
        cont2 =  self.a[4]
        email =  self.a[5]

        n = TextField(label="name",border_radius=8, icon=icons.BUSINESS, value=f"{name}", on_submit=self.profile_update)
        b =TextField(label="address",border_radius=8, icon=icons.BUSINESS_CENTER_ROUNDED, value=f"{box}", on_submit=self.profile_update)
        l =TextField(label="location",border_radius=8, icon=icons.GPP_GOOD_ROUNDED, value=f"{loc}", on_submit=self.profile_update)
        c1 =TextField(label="Contact1",border_radius=8, icon=icons.CALL, value=f"{cont1}", on_submit=self.profile_update)
        c2 = TextField(label="Contact2",border_radius=8, icon=icons.CALL, value=f"{cont2}", on_submit=self.profile_update)
        m = TextField(label="email",border_radius=8, icon=icons.MAIL_OUTLINE_ROUNDED, value=f"{email}", on_submit=self.profile_update)
        
       
        self.profileUpdate.controls.append(n)
        self.profileUpdate.controls.append(b)
        self.profileUpdate.controls.append(l)
        self.profileUpdate.controls.append(c1)
        self.profileUpdate.controls.append(c2)
        self.profileUpdate.controls.append(m)
        

        #open qty dialog
        self.page.dialog = self.profileUpdateForm
        self.profileUpdateForm.open = True
        self.page.update()
        pass
    

    def profile_update(self,e):
        fld = e.control.label
        val = e.control.value
        #print(fld, val)
        Database().update_business_profile(fld = fld, val=val)

        self.page.dialog.open = False
        self.update()
        self.page.update()


    
    def sign_in_submit(self, e):
        self.page.close_banner()
        code = str(self.pwd.value)
        #print(code)
        
        auth = [k[1] for k in Database().get_superusers()]

        if code not in auth:
            msg = Banner(
                bgcolor="Amber", leading=Icon(icons.WARNING_ROUNDED),
                content=Text(value="Wrong code, Acess Denied"),
                 actions=[
                    TextButton("Dismiss", on_click=self.close_banner)],
                ) 
            
            self.page.banner = msg
            msg.open = True
            self.update()
            self.page.update()

        else:
            #self.page.go("/useraccess")
            pass
            

        return code

    def exit_banner_if_any(self):
        if self.page.banner.open == True:
            self.page.banner.open = False
        self.update()
        self.page.update()
 
    def close_banner(self,e):
        self.page.banner.open = False
        self.update()
        self.page.update()

    def highlight_link(self,e):
        e.control.style.color = ft.colors.BLUE
        e.control.update()


    def build(self):
        return Container(
                content=Column(
                    spacing=20,
                    horizontal_alignment=CrossAxisAlignment.CENTER,

                    controls=[
                    Container(
                        alignment=alignment.center,
                        #expand=True,
                        height=60,
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        bgcolor="#065080",

                        content = Row(
                            alignment="center",
                             controls =[
                                #IconButton(icon=icons.SETTINGS_APPLICATIONS_OUTLINED, icon_color="White"),
                                Text(value="SETTINGS", font_family="Poppins Bold", size=18, color="Amber"),
                                #Text(value=""),
                                
                             ]),
                        ), 

                    Row(alignment="center",
                        controls=[Image("images/settings.png", width=80, height=100)]),

                    Row(alignment="center",
                        controls=[
                            Image("images/prfl.png", width=40, height=40),
                            Text(spans=[TextSpan(text="Profile", on_click=self.view_profile)]),
                            Text(spans=[TextSpan(text="Edit", on_click=self.updateProfile)]),
                        ]
                    ),

                    Row(alignment="center",
                        controls=[
                            Image("images/rstdata.png", width=40, height=40),
                            Text(spans=[TextSpan(text="Initialize", on_click=self.open_reset_confirm)]),
                            Text(value=""),
                        ]
                    ),


                    Row(alignment="center",
                        controls=[
                            Image("images/bckup.png", width=40, height=40),
                            Text(spans=[TextSpan(text="Backup", on_click=self.open_backup_confirm)]),
                            Text(value=""),
                        ]
                    ),



                    Row(alignment="center",
                        controls=[
                            Image("images/uploadf.png", width=40, height=40),
                            Text(spans=[TextSpan(text="Upload", on_click=self.open_upload_confirm)]),
                            Text(value=""),
                        ]
                    ),

                    Row(alignment="center",
                        controls=[
                            Image("images/tax.png", width=30, height=30),
                            Text(spans=[TextSpan(text="Update Tax", on_click=self.taxupdate)]),
                            Text(value=""),
                        ]
                    ),



                    Text(
                        disabled=False,
                        spans=[
                            TextSpan(
                                "Home",
                                TextStyle(decoration=TextDecoration.UNDERLINE),
                                #url="https://google.com",
                                on_enter= self.highlight_link,
                                on_click=self.go_home,
                                ),
                                
                                ]),

                    #IconButton(icon=icons.HOME_OUTLINED, icon_color="Black", on_click=self.go_home),  
                    

                    ]

                )
            )


class useraccess(UserControl):
    def __init__(self):
        super().__init__()
       
        self.userid = Text()

        self.updatefield = TextField(label='Full Name', 
                border_radius=5,
                #icon = ft.icons.PERSON,
                height=40,
                width=210,
                border=border.only(bottom=BorderSide(1,"BLue")))


        self.fname = TextField(label='Full Name', 
                border_radius=10,
                icon = ft.icons.PERSON,
                height=50,
                border=border.only(bottom=BorderSide(1,"BLue")))
        
        self.username = TextField(label='User Name', 
                border_radius=10,
                height=50,
                icon = ft.icons.PERSON,
                border=border.only(bottom=BorderSide(1,"BLue")))
        

        self.contact = TextField(label='Contact', 
                border_radius=10,
                height=50,
                icon = ft.icons.PHONE_CALLBACK,
                border=border.only(bottom=BorderSide(1,"BLue")))


        self.mail = TextField(label='Mail', 
                border_radius=10,
                height=50,
                value="user@gmail",
                icon = ft.icons.MAIL_OUTLINE_ROUNDED,
                suffix_text=".com",
                border=border.only(bottom=BorderSide(1,"BLue")))


        self.pwd = TextField(label='Password', 
                border_radius=10,
                height=50,
                password=True,
                can_reveal_password=True,
                icon=ft.icons.KEY,
                border=border.only(bottom=BorderSide(1,"BLue")))
        
        self.active = TextField(label='active', 
                border_radius=10,
                height=50,
                value="False",
                icon=ft.icons.PERSON,
                border=border.only(bottom=BorderSide(1,"BLue")))

        self.added = TextField(label='Date Added', 
                border_radius=10,
                height=50,
                icon = ft.icons.TODAY_ROUNDED,
                value=str(date.today()),
                read_only=True,
                border=border.only(bottom=BorderSide(1,"BLue")))
        

        self.status = RadioGroup(content=Row(alignment="SpaceBetween",
            controls=[
                Radio(value="superuser", label="superuser"),
                Radio(value="user", label="user"),
                 ]), 
                 #on_change=radiogroup_changed
                 )



        self.submit = ElevatedButton(
                            text="Add",
                            on_click=self.add_new_submit,
                            )

        self.updt = ElevatedButton(
                            text="Update",
                            on_click=self.update_user_submit,
                            )

        self.userformcontainer = Column(spacing=10, height=480, width=400, horizontal_alignment=CrossAxisAlignment.CENTER)
        self.userform = AlertDialog(modal=False, title=Text(value="Add User", size=15), content=self.userformcontainer)

        self.userformUpdatecontainer = Column(width=900, height=150,horizontal_alignment=CrossAxisAlignment.CENTER)
        self.R1 = Row(alignment="center", width=900)
        self.R2 = Row(alignment="center", width=900)
        self.userformUpdate = AlertDialog(modal=False,  content=self.userformUpdatecontainer)
        self.usertableContanier = Column(height=500, scroll="auto", spacing=0)


    def usertable_updating(self, userdb):
        self.usertable = Container( 
            alignment=alignment.center,
            content=DataTable(
                vertical_lines=ft.border.BorderSide(1, "Grey"),
                horizontal_lines=ft.border.BorderSide(1, "Grey"),
                sort_column_index=3,
                #sort_ascending=False,
                heading_row_color=ft.colors.BLACK12,
                width=1200,
                border_radius=5,
                heading_row_height=50,
                data_row_max_height=40,
                #show_checkbox_column=True,
                data_row_color={"hovered": "0x30FF0000"},  
                column_spacing=50,
                columns=[
                    DataColumn(Text("User id"),numeric=True),
                    DataColumn(Text("Full Name"),),
                    DataColumn(Text("User Name"),),
                    DataColumn(Text("Contact"),),
                    DataColumn(Text("Mail"),),
                    DataColumn(Text("Password"),),
                    DataColumn(Text("Active"),),
                    DataColumn(Text("Date Added"),),
                    DataColumn(Text("Access Status"),),
                    ],
                 rows = []                  
                ))  


        k = [
                DataRow(cells=[
                            DataCell(Text(l[0], color="black"),),
                                        #on_double_tap=self.updateOnDoubleTap, show_edit_icon=True),
                            DataCell(Text(l[1]),),
                            DataCell(Text(l[2]),),
                            DataCell(Text(l[3]),),
                            DataCell(Text(l[4]),),
                            DataCell(Text(l[5]),),
                            DataCell(Text(l[6]),),
                            DataCell(Text(l[7]),),
                            DataCell(Text(l[8]),),
                           
                            ],                      
                            on_select_changed=self.updateUser,
                            on_long_press= self.deleteUser,
                            
                            ) 
                            for l in userdb]
        for i in k:
            self.usertable.content.rows.append(i)
        self.usertableContanier.controls.append(self.usertable)
        return self.usertableContanier


    def on_update_refresh(self):
        #clear table and update
        table = self.usertable_updating(userdb=db().getusers())
        table.controls.clear()
        self.usertable_updating(userdb=db().getusers())

        msg = SnackBar(content=Text(
            f"Updated!              "), 
            action="Ok")
        self.page.snack_bar = msg
        msg.open = True

        self.update()
        self.page.update()


    def show_userform(self,e):
        self.userformcontainer.controls.clear()
        lst = [self.fname, self.username, self.contact, self.mail, self.pwd, self.active, self.added, self.status, self.submit]

        for i in lst:
            self.userformcontainer.controls.append(i) 
        self.page.dialog = self.userform
        self.userform.open=True
        self.update()
        self.page.update()


    def updateUser(self,e):
        self.fldupdtclear()

        id = int(e.control.cells[0].content.value)
        #print(id)
        usr = db().getuser_detail(id=id)[0]
        self.userid.value = usr[0]

        
        lst = [self.fldupdt(l="Full Name", v=usr[1]),self.fldupdt(l="User Name", v=usr[2]),
               self.fldupdt(l="Contact", v=usr[3]),self.fldupdt(l="Mail", v=usr[4]),
               self.fldupdt(l="Password", v=usr[5]),self.fldupdt(l="Active", v=usr[6]),
               self.fldupdt(l="Date Added", v=usr[7]),self.fldupdt(l="Access Status", v=usr[8])]


        self.userformUpdatecontainer.controls.append(Text(value=f"userid:{self.userid.value}"))

        for i in lst[:4]:
            self.R1.controls.append(i)
        self.userformUpdatecontainer.controls.append(self.R1)

        for i in lst[4:]:
            self.R2.controls.append(i)
        self.userformUpdatecontainer.controls.append(self.R2)

        self.userformUpdatecontainer.controls.append(self.updt)  

        self.page.dialog = self.userformUpdate
        self.userformUpdate.open=True
        self.update()
        self.page.update()


    def deleteUser(self,e):
        id = int(e.control.cells[0].content.value)
        db().delete_user_from_db(id=id)
        self.on_update_refresh()


    def fldupdtclear(self):
        self.R1.controls.clear()
        self.R2.controls.clear()
        self.userformUpdatecontainer.controls.clear()
        self.userformcontainer.controls.clear()
        self.update()
        self.page.update()


    def fldupdt(self,l,v):
        fld = TextField(label=l, 
                border_radius=5,
                value=v,
                height=40,
                width=210,
                border=border.only(bottom=BorderSide(1,"BLue")))
        
        if l=="Password":
            fld.password=True
            fld.can_reveal_password=False

        return fld


    def go_home(self,e):
        self.page.go(f"/homepage")


    def add_new_submit(self,e):
        new = (self.fname.value, self.username.value, self.contact.value, self.mail.value, 
               self.pwd.value, self.active.value, self.added.value, self.status.value)
        
        empty = len([i for i in new if i=="" or i==None])
        #print(new)
       
        if empty > 0:
            msg = Banner(
                bgcolor="Amber", leading=Icon(icons.WARNING_ROUNDED),
                content=Text(value="Some fields are empty"),
                 actions=[
                    TextButton("Ok", on_click=self.close_banner)],
                ) 
            
            self.page.banner = msg
            msg.open = True
            self.update()
            self.page.update()

        else:
            self.fldupdtclear()
            self.page.dialog.open=False
            self.update()
            self.page.update()
            

            #add to database and refresh
            db().add_new_user(val=new)
            self.on_update_refresh()
                          

    def update_user_submit(self,e):
        #print("hello")
        id = self.userid.value
        #print(id)

        L1 = self.R1.controls
        L2 = self.R2.controls
        R = [L1[0].value, L1[1].value, L1[2].value, L1[3].value, L2[0].value, L2[1].value, L2[2].value, L2[3].value]
        #print(R)
        db().update_users(a=R[0], b=R[1], c=R[2], d=R[3], e=R[4], f=R[5], g=R[6], h=R[7], id=id)
        self.page.dialog.open=False
        self.on_update_refresh()
        
        pass


    def close_banner(self,e):
        self.page.banner.open = False
        self.update()
        self.page.update()



    def build(self):
        return Container(
                alignment=alignment.center,

                content=Column(
                    spacing=0,

                    controls=[
                    # topbar 
                    Container(
                        alignment=alignment.center,
                        #expand=True,
                        height=60,
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        bgcolor="#065080",

                        content = Row(
                            alignment="SpaceBetween",
                             controls =[
                                IconButton(icon=icons.HOME_OUTLINED, icon_color="White", on_click=self.go_home),

                                Row(alignment="center",
                                    controls=[
                                        IconButton(icon=icons.ADD, icon_color="White", on_click=self.show_userform),
                                        Text(value="USERS", font_family="Poppins Bold", size=18, color="Amber"),
                                    ]
                                ),

                                Text(value=""),
                                
                             ]),
                        ), 

                    #note
                    Container(
                        alignment=alignment.center,
                        border_radius=border_radius.only(bottom_left=15, bottom_right=15),
                        bgcolor="#064080",

                        content=Column(
                            height=80, horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Text(
                                    size=16, font_family="SF Pro Bold", color="Amber",
                                    value=" ** Long Press User id to PERMANENTLY DELETE A USER, note: This action is irrevisible, if not certain, you can temporaly put Active to FALSE",
                                    ),

                                Text(
                                    size=13, font_family="Poppins Bold", color="White",
                                    value=" ** Click On User Details to Update",
                                    ),
                            ]
                          ),
                    ),

                    #display users datatables
                    Container(
                            alignment=alignment.center,
                        content=Column(
                            scroll="auto",
                            spacing = 0,
                            #controls=[]
                            controls=[self.usertable_updating(userdb = db().getusers())]
                        )
                    ),

                   
                    ]

                )
            )


#appbar class
class ApplicationBar(UserControl):
    def __init__(self):
        super().__init__()

        self.readme = readme()
        self.showpreadme = AlertDialog(modal=False, content=self.readme)

    def show_readme(self,e):
        self.page.dialog = self.showpreadme
        self.showpreadme.open = True
        self.update()
        self.page.update()
    
    def build(self):
        return Container(
            
            alignment=alignment.center,

            height=70,
            border_radius=border_radius.only(top_left=15, top_right=15),
            bgcolor="#065080",
            content=Row(

                alignment="SpaceBetween",

                controls=[
                    Row(
                        controls=[
                            Icon(icons.HOME_ROUNDED, color="white"),
                            Text(value=str(show_date()), color="white")
                        ]),
                   
                     Icon(icons.SHOPPING_BASKET, color="white", size=50),
                        
                    Container( 
                       #alignment="center",
                       height = 60,
                       width = 200,
                       on_click=self.show_readme,
                        content=Row(
                            controls=[
                                Icon(icons.READ_MORE_OUTLINED, color="white", size=40),
                                Text(value="READ ME    ", color="Amber"),
                                
                            ]
                        ),                       
                        ),
            ]),
          )


#bottonbar
class ApplicationButtonBar(UserControl):
    def __init__(self):
        super().__init__()
    
    def build(self):
        return Container(
            
            alignment=alignment.center,

            height=280,
            border_radius=border_radius.only(bottom_left=20, bottom_right=20),
            bgcolor="#065080",
            content=Row(

                #alignment="SpaceBetween",

                controls=[                 
                    
            ]),
          )


#page button
class PageFooter(UserControl):
    def __init__(self):
        super().__init__()
        self.p = Database().get_all_data(table="company")[0]
    
    def build(self):
        return Container(
            
            alignment=alignment.center,

            height=80,
            border_radius=border_radius.only(bottom_left=20, bottom_right=20),
            #bgcolor="#065080",
            content=Row(

                alignment="center",

                controls=[                 
                    Text(value=self.p[0], color="#FFC300", font_family="Poppins LightItalic", size=20),
                    #Text(value=self.p[0]),
            ]),
          )


#nav side
class navside(UserControl):
    def __init__(self):
        super().__init__()

        self.username = "Logged in"
        self.user = ""

    def build(self):
        return Container(
            height=520,
            width=150,
            bgcolor="#065080",

            content=ModernNavBar(username=self.username, user=self.user, page=None),
        )


#retail section
class addPayment(UserControl):
    def __init__(self):
        super().__init__()

       
        self.rct = salesdata.receiptNo()
        try:
            self.bskt_item =jsonclass().loadbskt()
            self.subT = sum([float(l[4]) for l in self.bskt_item])
            self.Tx = float(salesdata().getax())
            self.vat = round(self.subT * (self.Tx /100),2)
            self.amnt = "GHS {:,.2f}".format(self.subT + self.vat) #0.00
        
        except:
             self.amnt = "GHS {:,.2f}".format(0)


        
    def get_pay_change(self,e):
        self.controls[0].content.content.content.controls[2].controls.clear()
        pamnt = e.control.value
        #print(pamnt)

        #check if pay
        if pamnt == "":
            pamnt = 0
   
        chng0 = float(pamnt) - sum([float(l[4]) for l in self.bskt_item])
        chng = "GHS {:,.2f}".format(chng0)
        
        #append change icon and change amount again
        c = self.controls[0].content.content.content.controls[2].controls
        c.append(Image(src="images/chng.jpg", width=50, height=55))
        c.append(Text(value=chng, size=18, color="blue"))

        self.update()  
        self.page.update()


    def close_banner(self,e):
        self.page.banner.open = False
        self.update()
        self.page.update()


    def exitpay(self,e):
        self.page.dialog.open = False
        self.update()
        self.page.update()


    def save_exitpay(self,e):
        self.page.close_banner()

        pamnt = self.controls[0].content.content.content.controls[1].controls[1].value
        if pamnt == "":
            pamnt = 0
        chng = float(pamnt) - sum([float(l[4]) for l in self.bskt_item])
        #print(type(chng))

        if chng < 0:
            msg = Banner(
                bgcolor="Amber", leading=Icon(icons.WARNING_ROUNDED),
                content=Text(value="Payment Amount insufficient"),
                 actions=[
                    TextButton("Ok", on_click=self.close_banner)],
                ) 
            
            self.page.banner = msg
            msg.open = True
            self.update()
            self.page.update()

        else:

            self.page.dialog.open = False
            msg = SnackBar(content=Text(
                f"Saved!              Receipt#: {self.rct}"), 
                action="Next", bgcolor="#065080")
            self.page.snack_bar = msg
            msg.open = True

            if self.page.banner == True:
                self.page.banner = False
            self.update()
            self.page.update()

        #saves sales and clear basket
        bskt_item = jsonclass().loadbskt()
        dt = str(date.today())
        rct = self.rct
        total = sum([float(l[4]) for l in bskt_item])
        cshr = db().get_active_user()
        items = [i for i in bskt_item]
        cartitems = {'date':dt, 'receipt#':rct, 'total':total, 'cashier':cshr, 'items':items}
        jsonclass.AddNewSalesJson(cartitems=cartitems) 
        #print(cartitems)

        #add sales to database
        val = (date.today(), rct, total, cshr, len(items))
        db().add_to_salessummary(val=val)
        
        #add to salesitem database
        db().add_to_salesitems(dt=str(date.today()), rct=rct)

        b = jsonclass.addto_salesitems(dt=str(date.today()), rct=rct)
        r = [items,pamnt,chng,total,rct,cshr]
        salesreceipt().generate_receipt(receipt=r)
        #salesreceipt().print_receipt()
        
        #print(r)

        #update stock quantities
        db().sales_stock_update(dt=str(date.today()), rct=rct)

        #now reset / clear basket
        jsonclass.clearJson() 

        #updating controls and page
        pg = self.page.views[2].controls[0] #ApplicationBody class
        bdy = pg.controls[0].content.controls[1].content.controls #page body
        tdysm = bdy[2].controls[0].controls[1] #todaysummary class
        #print(tdysm)

        tdysm.controls.clear()
        tdysm.controls.append(todaySummary())


        crtsmry = bdy[2].controls[1].controls[1].content.controls[0].content #container for basket summary
        #crtsmry.controls.clear()
        #print(crtsmry)
        crtsmry.controls[0].content.controls[0].controls[1].content.value = 0
        crtsmry.controls[0].content.controls[1].controls[0].value = f"GHS 0.00"

        datatbl = bdy[2].controls[1].controls[1].content.controls[1].content.controls[0].content #container for basket items / datatables
        datatbl.rows = []

        
        #print (bdy[1].controls[1].controls[1].content.controls[1].content.controls[0].content)
        #print(crtitms)
        pg.update()
        


    def build(self):
        return Container(
            height=400,
            #width=320,
            #bgcolor="Green",

            content= Container(
                    alignment=alignment.center,
                    #height=90,
                    width=450,
                    border_radius=12,
                    #border=border.all(1,"#ebebeb"),
                    bgcolor="#065080",
                    content= Container(
                        border_radius=12,
                        bgcolor="White",
                        content = Column(
                            controls=[
                                #------------summary
                                 Row(
                                 controls=[
                                 Image(src="images/bskt4.jpg"),
                                 Column(
                                    alignment=CrossAxisAlignment.CENTER,
                                        spacing=1,
                                    controls=[
                                        Row(
                                            controls=[Text(value="SubTotal  ", font_family="Poppins Regular", color="Blue250"),
                                            Text(value=f"{self.subT}", font_family="Poppins Regular", size=14),]
                                        ),

                                        Row(
                                            controls=[Text(value=f"Tax({self.Tx}%)", font_family="Poppins Regular", color="Blue250"),
                                            Text(value=f"{self.vat}", font_family="Poppins Regular", size=13),]
                                        ),

                                        Row(
                                            controls=[Text(value="Total      ", font_family="Poppins Regular", color="Blue250"),
                                            Text(value=f"{self.amnt}", font_family="Poppins Semibold", size=15),]
                                        ),
                                    
                                    Row(
                                        controls=[Icon(icons.PEOPLE_ROUNDED),
                                            Text(value="   Receipt# :"),
                                            Text(value=self.rct)
                                        ]
                                    )])
                                   ]),

                                #----------
                                Row(
                                    alignment="center",
                                    controls=[
                                        Icon(icons.PAYMENT_ROUNDED),
                                        TextField(
                                            label="Amount", prefix_text="GHS: ",
                                            on_submit=self.get_pay_change)
                                    ]
                                ),
                                Row( 
                                    alignment="center",
                                    controls=[
                                        Image(src="images/chng.jpg", width=50, height=55),
                                        #Text(value=f"Change: {self.chng}")
                                    ]),

                                 Row( 
                                    alignment="center",
                                    controls=[
                                       TextButton(
                                           text="SAVE",
                                           on_click=self.save_exitpay
                                           ),

                                        TextButton(
                                           #Icon(icons.CLOSE_OUTLINED, color="Amber"), 
                                           text="Exit",
                                           on_click=self.exitpay
                                           ),
                                    ]),
                            ]
                        ),                         
                    )
                ))


#retail button action
class retailAction(UserControl):
    def __init__(self):
        super().__init__()

        self.taxcontainer = Column(spacing=1, height=80, width=100)
        self.tax = AlertDialog(modal=False, title=Text(value="Tax: update at settings", size=15), content=self.taxcontainer)

        #self.paycontainer = addPayment()
        self.paycontainer = Column(spacing=1, height=450, width=450)
        self.pay = AlertDialog(modal=True, title=Text(value="Add Payment", size=15), content=self.paycontainer)



    def on_hover(self,e):
        e.control.bgcolor="#065080" if e.data == "true" else "White"
        e.control.content.controls[1].color="white" if e.data == "true" else "Black"
        e.control.update()
    

    def taxupdate(self,e):
        self.taxcontainer.controls.clear()
        v = salesdata().getax()
        t = TextField(label="tax",border_radius=8, icon=icons.PASSWORD_OUTLINED, on_submit=self.add_tax, value=v, read_only=True)
        self.taxcontainer.controls.append(t)
       
        self.page.dialog = self.tax
        self.tax.open = True
        self.page.update()
        #pass


    def add_tax(self,e):
        t = e.control.value
        
        salesdata().addtax(t=t)
        #print("action here")

        msg = SnackBar(content=Text(f"Tax value updated"), action="OK", bgcolor="#065080")
        self.page.snack_bar = msg
        msg.open = True

        self.page.dialog.open = False
        self.update()
        self.page.update()


    def paycart(self,e):
        self.page.close_banner()

        if not os.path.exists('basket.json'):
            msg = Banner(
                bgcolor="Amber", leading=Icon(icons.WARNING_ROUNDED),
                content=Text(value="No cart items found!"),
                 actions=[
                    TextButton("Ok", on_click=self.close_banner)],
                ) 
            
            self.page.banner = msg
            msg.open = True
            self.update()
            self.page.update()
        else:
            self.paycontainer.controls = []
            self.paycontainer.controls.append(addPayment())
            self.page.dialog = self.pay
            self.pay.open = True
            self.page.update()
        

    def close_banner(self,e):
        self.page.banner.open = False
        self.update()
        self.page.update()

    def build(self):
        return Container(
            alignment=alignment.center,
            height=80,
            width=650,
            #bgcolor="Yellow",

            content=Row(
                alignment="SpaceBetween",
                controls=[
                    Container(
                        width=120,
                        height=40,
                        alignment=alignment.center,
                        border=border.all(1,"#ebebeb"),
                        border_radius=10,
                        #bgcolor="Green350",
                        on_hover= self.on_hover,
                        on_click = self.paycart,
                        content=Row(
                            alignment="center",
                            controls=[
                                Icon(icons.PAYMENT_ROUNDED),
                                Text(value="Payment"),
                                ]
                        )),

                    
                    Container(
                        width=120,
                        height=40,
                        alignment=alignment.center,
                        border=border.all(1,"#ebebeb"),
                        border_radius=10,
                        #bgcolor="Green350",
                        on_hover= self.on_hover,
                        on_click = self.taxupdate,
                        content=Row(
                            alignment="center",
                            controls=[
                                Icon(icons.UPDATE_ROUNDED),
                                Text(value="VAT")
                                ]
                        )),

                        

                        

                ]
            ),
        )


#dashboard
class todaySummary(UserControl):
    def __init__(self):
        super().__init__()

        T = salesdata.todaysummary()[0]
        C = salesdata.todaysummary()[1]

        self.total = "GHS {:,.2f}".format(T)
        self.count = C
        

    def build(self):
        return Column(
            controls=[
                  
            Container(
            height=100,
            width=360,
            #bgcolor="Green",

            content= Container(
                    alignment=alignment.bottom_right,
                    height=90,
                    width=280,
                    border_radius=12,
                    #border=border.all(1,"#ebebeb"),
                    #bgcolor="#065080",
                    content= Container(
                        alignment=alignment.center,
                        height=80,
                        width=270,
                        border=border.all(1,"#ebebeb"),
                        border_radius=12,
                        bgcolor="White",
                        content = Row(
                             controls=[
                                 Image(src="images/bskt2.jpg"),

                                 Column(
                                    alignment=CrossAxisAlignment.CENTER,
                                        spacing=1,
                                    controls=[
                                    Text(value="  Sales Today", font_family="Poppins Regular", color="Blue250"),
                                    Text(value=f"  {self.total}", font_family="Poppins Semibold", size=20),
                                    Row(
                                        controls=[
                                            Icon(icons.PEOPLE_ROUNDED),
                                            Text(value="   Sales Count |"),
                                            Text(value=f'{self.count}')
                                        ]
                                    )])
                                   ]
                        )
                          
                    )
                ))

            ]
        )
    
  
#cart summary
class cartsummary(UserControl):
     def __init__(self, qty, val):
        super().__init__()
        self.qty = qty
        self.val = val


     def build(self):
         return Container(
             height=60,
             width=400,

             content=Row(
                 alignment="SpaceBetween",
                 controls=[
                     Row(
                         controls=[
                           Image(src="images/bskt.jpg"),
                           Container(
                               alignment = alignment.center,
                               height=35,
                               width=35,
                               bgcolor="bluegrey100",
                               border_radius=15,
                               
                               content=Text(
                                 value=f"{self.qty}",
                                 size=25,
                                 color="Blue",  
                                 font_family="Poppins ExtraBold", 
                                 )
                           ),                           
                         ]                       
                     ),


                     Row(
                         controls=[
                             Text(
                                 value=f"GHS {self.val}",
                                 font_family="Poppins Bold", 
                                 color="Blue", 
                                 size=18,
                                 )
                         ]
                     ),
                 ]
             )
         )   


class display_product(UserControl):
    def __init__(self):
        super().__init__()

    
    def build(self):
        return Container(
            height=360, width=300, alignment="center",
            content=Image(src="images/product.jpg", height=300, width=250)
        )


#app bodyclass
class ApplicationBody(UserControl):

    def __init__(self):
        super().__init__()

        self.pwdcontainer = Column(spacing=1, height=80, width=100)
        self.pwd = AlertDialog(modal=False, title=Text(value="Confirm Password", size=15), content=self.pwdcontainer)
        
        p = Database().get_all_data(table='products')
        self.products = [{"name":i[1] , "price":round(i[2],2), "qty":i[3]} for i in p]
        
        
        self.q = 0
        self.v = 0.00

        self.today_summary = Column()
        self.cartsummarycontainer = Row(alignment="SpaceBetween")
        self.resultdata = ListView()
        self.SearchResultContanier = Column(height=500, scroll="auto", spacing=0, width=300)
        self.CartContanier = Column(height=360, scroll="auto", spacing=0, controls=[todaySummary()])
        self.cart = Column(spacing=10, height=180, width=300)
        self.addQty = AlertDialog(title=Text(value="add to cart", size=15, color="Amber_400"), content=self.cart)
        self.bskt = []

        #display product image
        self.SearchResultContanier.controls.append(Image(src="images/logo.png", height=300, width=250))

        self.cartitem = Container( 
            alignment=alignment.center,
            content=DataTable(
                #vertical_lines=ft.border.BorderSide(1, "Grey"),
                #horizontal_lines=ft.border.BorderSide(1, "Grey"),
                #sort_column_index=0,
                sort_ascending=True,
                heading_row_color=ft.colors.BLACK12,
                width=600,
                border_radius=5,
                heading_row_height=30,
                data_row_max_height=40,
                #show_checkbox_column=True,
                data_row_color={"hovered": "0x30FF0000"},  
                column_spacing=50,
                columns=[
                    DataColumn(Text("iNo"),numeric=True),
                    DataColumn(Text("item")),
                    DataColumn(Text("qty"),numeric=True),
                    DataColumn(Text("price"),numeric=True),
                    DataColumn(Text("cost"),numeric=True),
                    ],
                 rows = []                  
                ))   


        self.cartsummary = Container(
             height=60,
             width=600,             
             content=Row(
                 #alignment="SpaceBetween",
                 controls=[
                     Row(
                         alignment="SpaceBetween",
                    controls=[
                    Image(src="images/bskt.jpg"),
                    Container(
                        alignment = alignment.center,
                        height=50,
                        width=53,
                        bgcolor="bluegrey100",
                        border_radius=15,
                        
                        content=Text(
                            value=f"{self.q}",
                            size=20,
                            color="Blue",  
                            font_family="Poppins ExtraBold", 
                            )),]                       
                        ),
                     Row(
                        alignment="start",
                    controls=[
                        #Image(src="images/cash.jpg"),
                        Text(
                            value=f"GHS {self.v}",
                            font_family="Poppins Bold", 
                            color="Blue", 
                            size=15,
                            )]
                      ),

                     Container(
                        width=200,
                        height=40,
                        alignment=alignment.center,
                        border=border.all(1,"#ebebeb"),
                        border_radius=10,
                        #bgcolor="#FFE4C4",
                        #on_hover= self.on_clear_hover,
                        on_click = self.ClearCart,
                        content=Row(
                            alignment="center",
                            controls=[
                                Icon(icons.DELETE_ROUNDED),
                                Text(value="Clear Cart"),
                                ]
                        )),                     
                      ]))
    

    def show_access_dlg(self,e):
        self.pwdcontainer.controls.clear()
        u = db().get_active_user()
        p = TextField(label=f"{u}",border_radius=8, icon=icons.PASSWORD_OUTLINED, on_submit=self.confirm_code, password=True)
        self.pwdcontainer.controls.append(p)
       
        #open qty dialog
        self.page.dialog = self.pwd
        self.pwd.open = True
        self.page.update()
        pass
    

    def toggle_menu(self,e):
        menu = self.controls[0].content.controls[1].content.controls[0]
        space = self.controls[0].content.controls[1].content.controls[1]

        #user = menu.content.controls[0].content.controls[0].content.controls[0].content.controls[1]
        #print(user)

        if menu.visible == False:
            menu.visible = True
            space.visible = False
        else:
            menu.visible = False
            space.visible = True

        self.update()
        self.page.update()



    def on_break(self,e):
        self.controls[0].content.controls[1].visible = False
        self.update()
        self.page.update()


    def confirm_code(self,e):
        c = e.control.value
        auth = [k[1] for k in Database().get_active_users()]
        

        if c in auth:
            self.controls[0].content.controls[1].visible = True
            self.update()
            self.page.update()

            #print(self.controls[0].content.controls[1])

        self.page.dialog.open = False
        self.update()
        self.page.update()


    def on_clear_hover(self,e):
        e.control.bgcolor="#FFE4C4" if e.data == "true" else "#065080"
        e.control.content.controls[1].color="white" if e.data == "true" else "Black"
        e.control.update()


    def clearingCart(self):
        self.cartitem.content.rows=[]
        self.cartsummary.content.controls[0].controls[1].content.value = 0
        self.cartsummary.content.controls[1].controls[0].value = "GHS 0.0"
        jsonclass.clearJson()
        self.update()
        self.page.update()


    def ClearCart(self,e):
        self.clearingCart()
       

    def updateOnDoubleTap(self, e):
        #print(e.control.content.value)
        iNo = e.control.content.value
        jsonclass.deleteitem(iNo=iNo)
        self.updating_cart()
        

    def IncreaseCartQty(self,e):
        #print(e.control.cells[0].content.value)
        iNo = e.control.cells[0].content.value
        jsonclass.QtyIncrease(iNo=iNo)
        self.add_update_cart(bskt_item = jsonclass().loadbskt())
        

    def DecreaseCartQty(self,e):
        #print(e.control.cells[0].content.value)
        iNo = e.control.cells[0].content.value
        jsonclass.QtyDecrease(iNo=iNo)
        self.add_update_cart(bskt_item = jsonclass().loadbskt())


    def add_update_cart(self, bskt_item):
        try:
            cart = self.CartContanier.controls # set container to a variable
            bsktContainer = self.cart.controls # 
            bsktContainer.clear() 
            self.cartsummarycontainer.controls.clear()
            self.cartitem.content.rows=[]
            cart.clear()
            k = [
                DataRow(cells=[DataCell(Text(l[0], color="White"),
                                        on_double_tap=self.updateOnDoubleTap, show_edit_icon=True),
                            DataCell(Text(l[1]),),
                            DataCell(Text(l[2]),
                                    ),
                            DataCell(Text(l[3])),
                            DataCell(Text(l[4])),
                            ],                      
                            on_select_changed=self.IncreaseCartQty,
                            on_long_press=self.DecreaseCartQty,
                            #on_double_tap=lambda e: print(dir(e.id)),
                            #on_long_press=lambda e: print('delete'),
                            
                            ) 
                            for l in bskt_item]
            for i in k:
                self.cartitem.content.rows.append(i)
                
            q = sum([int(l[2]) for l in bskt_item])
            v1 = sum([(l[4]) for l in bskt_item])  
            v = "GHS {:,.2f}".format(v1) 
            cart.append(self.cartitem) 

        #move todays_summary_dashboard up
            self.today_summary.controls.clear()
            self.today_summary.controls.append(todaySummary())

        # get and update cartsummary     
            self.cartsummarycontainer.controls.append(self.cartsummary)
            self.cartsummarycontainer.controls[0].content.controls[0].controls[1].content.value = q
            self.cartsummarycontainer.controls[0].content.controls[1].controls[0].value = f"{v}"

            if self.addQty.open == True:
                self.addQty.open = False

            self.update()
            self.page.update()
        except:
            return None


    def updating_cart(self):
        self.add_update_cart(bskt_item = jsonclass().loadbskt())


    def add_to_cart(self,item,p):
        item = item
        p = float(p)
        #print(self.cart.controls)
        qty = int(self.cart.controls[1].value)
        #print(qty)
        lst = [item, qty, p, round(p*qty,2)]
        #print(lst)

        #json detail
        iNo = jsonclass.iNumb()
        items = [item, qty, p, round(p*qty,2)]
        itms = {'iNo': iNo, 'items':items}
        jsonclass.Addtobskt(itms=itms)
        self.add_update_cart(bskt_item = jsonclass().loadbskt())
        

    def selected_product(self,e):
         self.cart.controls.clear() 
         item = e.control.text
         for i in self.products:
             if i['name'].lower() == item.lower():
                 p = round(i['price'],2)
                 q = i['qty']
                 #print(i['price'])
                 #print(p)
         
         # set product cart info
         prc = TextField(label=item,border_radius=8, read_only=True, icon=icons.MONETIZATION_ON, prefix_text=f"GHS: {p}")
         qty = TextField(label=f"qty_on_hand:  {q}",border_radius=8,icon=icons.PRODUCTION_QUANTITY_LIMITS_ROUNDED, on_submit=lambda e: self.add_to_cart(item,p))
         self.cart.controls.append(prc)
         self.cart.controls.append(qty)
         self.update()

        #open qty dialog
         self.page.dialog = self.addQty
         self.addQty.open = True
         self.update()
         self.page.update()
         

    def on_product_search(self,e): #search product and append result
        self.SearchResultContanier.controls.clear()
        srch = e.control.value
        #print(srch) #debugging

        #searching product
        if not srch == "":
            self.SearchResultContanier.controls.clear()
            for item in self.products:
               #print(item["name"])
                if srch.lower() in item['name'].lower():
                    #print(item['name'])
                    fnd = TextButton(text=item['name'], on_click= self.selected_product)
                    self.SearchResultContanier.controls.append(fnd)                
            self.update()
        else:
            #print("Empty") 
            self.SearchResultContanier.controls.clear()   
            self.SearchResultContanier.controls.append(Image(src="images/logo.png", height=300, width=250))
            self.update()


    def build(self):
        return Container(
            padding=padding.only(top=1),
            expand=True,
            height=700,
            #border_radius=10,
            #width=1200,
            #bgcolor="Green",
            content= Column(
                spacing=0,

                controls=[
                    Container(
                        #bgcolor="#065080",
                        content= Column(
                             horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[

                                Container(        
                                    alignment=alignment.center,
                                    height=70,
                                    border_radius=border_radius.only(top_left=15, top_right=15),
                                    bgcolor="#065080",
                                    content=Row(
                                        alignment="SpaceBetween",
                                        controls=[
                                            Row(
                                                controls=[
                                                    Container(
                                                        width=100,
                                                        height=40,
                                                        alignment=alignment.center,
                                                        on_click=self.toggle_menu,
                                                        content=Icon(icons.MENU, color="white"),
                                                    ),
                                                   
                                                    Text(value=str(show_date()), color="white")
                                                ]),

                                            Container(
                                                on_click=self.show_access_dlg,
                                                content=Icon(icons.SHOPPING_BASKET, color="white", size=50),
                                            ),

                                            Container(
                                                #visible=False,
                                                on_click=self.on_break,
                                                content=Row(
                                                    controls=[
                                                        Icon(icons.LOGOUT_OUTLINED, color="white"),
                                                        Text(value=f"break / pause   ", color="Amber"),

                                                        

                                                ]
                                            ),
                                            ),
                                            
                                            
                                            ]),
                                        ),

                                 #ApplicationBar(),
                                 #Text(value="user", color="Amber"),
                            ]
                            
                        )
                    ),

                    Container(
                        visible=True,
                        height=520,
                        

                        content=Row(
                            alignment = "SpaceBetween",

                            controls=[                              
                                #navside
                                Container(
                                    visible=False,
                                    content=navside(),
                                ),
                                
                                Container(
                                    visible=True,
                                    width=200,
                                ),

                               #retail section                            

                                Column(
                                    alignment=CrossAxisAlignment.CENTER,
                                    spacing=0,
                        
                                    controls=[

                                        Row(
                                           width=950,
                                           alignment="SpaceBetween", 
                                         controls=[
                                             retailAction(),
                                             self.today_summary,

                                        ]),        
                                       
                                        
                                        Row(
                                            alignment="SpaceBetween",
                                            controls=[  
                                            
                                            Column(
                                                spacing=0,
                                                controls=[

                                                   Container(
                                                       height=60,
                                                       width=350,
                                                       #bgcolor="Black",
                                                            content=TextField(label='Search Product', 
                                                            border_radius=10,
                                                            #icon = icons.SEARCH_ROUNDED,
                                                            border=border.all(1,"#ebebeb"),
                                                            on_change= self.on_product_search)
                                                   ),
                                                   Container(
                                                       height=360,
                                                       width=350,
                                                       border_radius=7,
                                                       border=border.all(1,"#ebebeb"),
                                                       #bgcolor="Green",
                                                       content=self.SearchResultContanier
                                                   ),                                                
                                                 
                                                 ]),


                                             Container(
                                                 #bgcolor="Amber",
                                                 width=800,
                                                 height=420,
                                                 content=Column(
                                                        spacing=0,
                                                        controls=[

                                                        Container(
                                                            alignment=alignment.center, 
                                                            height=60,
                                                            width=800,
                                                            #bgcolor="Black",
                                                            content= self.cartsummarycontainer
                                                        ),

                                                        

                                                        Container(
                                                            height=360,
                                                            width=700,
                                                            border_radius=7,
                                                            border=border.all(1,"#ebebeb"),
                                                            #bgcolor="Green",
                                                            content=self.CartContanier
                                                        ),                                                
                                                        

                                                        

                                                        ]),
                                             ),
                                            ]
                                            ),
                                    ]
                                    
                                ),
                            ]
                        )),

                    Container(
                        content= None
                        #PageFooter()
                        ),
             
                ]
            )
            
            
            
          )


#product page
class Productpage(UserControl):
    def __init__(self):
        super().__init__()


        self.pick_files_dialog = FilePicker(on_result=self.pick_files_result)
        self.selected_files = Text()
        
        self.selectfile = Column(
            controls=[
                ft.ElevatedButton(
                    "Bulk product load",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda e: self.pick_files_dialog.pick_files(
                        allow_multiple=True
                        ),               
                ),
                self.selected_files,
            ])

        self.searchproduct =  TextField(label="Search Product", icon=icons.SEARCH_ROUNDED, on_change=self.on_product_search)
        self.productcount = Text(value=db().get_product_count(), color="Blue", size=15)
        self.stockvalue = Text(value=db().get_total_stock_value(), color="#065080", size=18) 


        self.ProductUpdateContent = Column(spacing=10, height=250, width=400)
        self.ProductUpdate = AlertDialog(title=Text(value="Product Update", size=15, color="#17202A"), content=self.ProductUpdateContent)

        self.stocktableContanier = Column(height=500, scroll="auto", spacing=0)
        #self.productid = TextField(label="Productid", read_only=True, prefix_text="ProductId:" , value=2)
        self.productname = TextField(label="Productname", read_only=False, prefix_text="Product:  " )
        self.productprice = TextField(label="Productprice", read_only=False, prefix_text="GHS:  ", value=0.0)
        self.productqty = TextField(label="Productqty", read_only=False, prefix_text="Qty:  ", value=0)
        #self.productcat = TextField(label="Productcategory", read_only=False, prefix_text="Productcategory:")
        self.savbut = ElevatedButton(text="AddNew Product", on_click=self.save_new_product) 

        self.productForm = Column(
            scroll="auto", spacing=30,
            controls=[
                #self.productid,
                self.productname,
                self.productprice,
                self.productqty,
                self.savbut,])
        

        self.selectfile.controls.append(self.pick_files_dialog)

    



    #dialog modal
        self.confirm_action =AlertDialog(
                modal=True,
                title=Text("Please confirm!!!", size=13),
                content=ft.Text("This action requires data processing and need admin guidance"),
                actions=[
                    ft.TextButton("Delete", on_click=self.close_dlg),
                    ft.TextButton("Discard", on_click=self.close_dlg),
                ],
                actions_alignment=MainAxisAlignment.END,
                on_dismiss=lambda e: print("Modal dialog dismissed!"),
                )
    
    def close_dlg(self,e):
        self.page.dialog = self.confirm_action
        self.confirm_action.open = False
        self.page.update()


    def open_confirm_dlg_modal(self,e):
        self.page.dialog = self.confirm_action
        self.confirm_action.open = True
        self.update()
        self.page.update() 




    def pick_files_result(self, e: FilePickerResultEvent):
        self.selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )
        self.selected_files.update()
        print(self.selected_files.value)



    def close_banner(self,e):
        self.page.banner.open = False
        self.update()
        self.page.update()


    def on_product_search(self,e): #search product and append result
        srch = e.control.value
        #print(srch) #debugging
        self.stocktable.content.rows.clear()

        data = db().getstockvalue()
        #print(data)
        for l in data:
            #print(item["name"])
            if srch.lower() in l[1].lower():
                fnd = DataRow(cells=[DataCell(Text(l[0], color="black"),),
                                              
                                              #on_tap=self.updateOnDoubleTap, show_edit_icon=True),
                                    DataCell(Text(l[1]),),
                                    DataCell(Text(round(l[2],2)),
                                            ),
                                    DataCell(Text(int(l[3]))),
                                    DataCell(Text("{:,.2f}".format(l[4]))), 
                                    ],                      
                                    on_select_changed=self.updateProduct,
                                    on_long_press= self.deleteProduct,
                                    
                                    ) 
        
                self.stocktable.content.rows.append(fnd)
        self.update()
        self.page.update()

 
    def stocktable_updating(self, productdb):
        self.stocktable = Container( 
            alignment=alignment.center,
            content=DataTable(
                #vertical_lines=ft.border.BorderSide(1, "Grey"),
                #horizontal_lines=ft.border.BorderSide(1, "Grey"),
                sort_column_index=3,
                sort_ascending=False,
                heading_row_color=ft.colors.BLACK12,
                width=850,
                border_radius=5,
                heading_row_height=50,
                data_row_max_height=40,
                #show_checkbox_column=True,
                data_row_color={"hovered": "0x30FF0000"},  
                column_spacing=50,
                columns=[
                    DataColumn(Text("id"),numeric=True),
                    DataColumn(Text("Product"),
                               on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),),
                    DataColumn(Text("Price"),numeric=True),
                    DataColumn(Text("QtyOnHand"),numeric=True,
                               on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),),
                    DataColumn(Text("Value GHS"),numeric=True),
                    ],
                 rows = []                  
                ))  


        #productdb = db().getstockvalue()
        k = [
                DataRow(cells=[DataCell(Text(l[0], color="black"),),
                                        #on_double_tap=self.updateOnDoubleTap, show_edit_icon=True),
                            DataCell(Text(l[1]),),
                            DataCell(Text(round(l[2],2)),
                                    ),
                            DataCell(Text(int(l[3]))),
                            DataCell(Text("{:,.2f}".format(l[4]))), 
                            ],                      
                            on_select_changed=self.updateProduct,
                            on_long_press= self.deleteProduct,
                            
                            ) 
                            for l in productdb]
        for i in k:
            self.stocktable.content.rows.append(i)
        self.stocktableContanier.controls.append(self.stocktable)
        return self.stocktableContanier



    def deleteProduct(self,e):
        id = int(e.control.cells[0].content.value)
        #print(id)
        db().delete_product_from_db(t="products", id=id)
        self.on_update_refresh()
        pass

    
        
    def updateProduct(self,e):
        #print("selected")
        self.ProductUpdateContent.controls.clear()

        id = e.control.cells[0].content.value
        prdt = e.control.cells[1].content.value

        id = TextField(label=f"{id}",border_radius=8, read_only=True, icon=icons.NUMBERS_ROUNDED, prefix_text=f"{prdt}")
        prc =TextField(label="New Price",border_radius=8,icon=icons.PRICE_CHANGE, on_submit= lambda e: self.change_price(id,e))
        stck =TextField(label= "+ New Stock Qty", value=0, border_radius=8,icon=icons.SHOPPING_BASKET, on_submit= lambda e: self.add_new_stock(id,e))
        adjt =TextField(label= "+/- Stock Adjusted", value=0,border_radius=8,icon=icons.SHOPPING_BASKET, on_submit= lambda e: self.stock_adjustment(id,e))
       
        self.ProductUpdateContent.controls.append(id)
        self.ProductUpdateContent.controls.append(prc)
        self.ProductUpdateContent.controls.append(stck)
        self.ProductUpdateContent.controls.append(adjt)

        #open qty dialog
        self.page.dialog = self.ProductUpdate
        self.ProductUpdate.open = True
        self.page.update()
        pass



    def add_new_stock(self, id, e):
        #id = int(id.label)
        qty = int(e.control.value)
        prdt = id.prefix_text
        dt = str(date.today())
        val = (dt, prdt, qty)
        #print(val)

        self.close_updateform()
        #add to purchases db and update product stock
        db().add_new_stock(val=val)
        Database().stock_adjst(item=prdt , qty=qty)
        self.on_update_refresh()
        pass



    def stock_adjustment(self, id, e):
        #id = int(id.label)
        qty = int(e.control.value)
        prdt = id.prefix_text
        dt = str(date.today())
        val = (dt, prdt, qty)
        #print(val)

        self.close_updateform()
        #add to adjustment db and update product stock
        db().add_to_adjustment_table(val=val)
        Database().stock_adjst(item=prdt , qty=qty)
        self.on_update_refresh()
        pass



    def change_price(self, id, e):
        id = int(id.label)
        new_price = float(e.control.value)
        #print(id, new_price)
        
        self.close_updateform()

        #update price in db
        db().update_product_price(id=id, p=new_price)
        self.on_update_refresh()


    def close_updateform(self):
        if self.ProductUpdate.open == True:
            self.ProductUpdate.open = False
        self.update()
        self.page.update()


    def on_update_refresh(self):
        #clear table and update
        table = self.stocktable_updating(productdb=db().getstockvalue())
        table.controls.clear()
        self.stocktable_updating(productdb=db().getstockvalue())

        msg = SnackBar(content=Text(
            f"Updated!              "), 
            action="Ok")
        self.page.snack_bar = msg
        msg.open = True

        self.update_stock_summary()
        self.update()
        self.page.update()


    def update_stock_summary(self):
        self.productcount.value = ""
        self.stockvalue.value = ""

        self.productcount.value = db().get_product_count()
        self.stockvalue.value = db().get_total_stock_value() 

        self.update()
        self.page.update()


    def save_new_product(self,e):
        self.page.close_banner()
        if self.productname.value == "":
            msg = Banner(
                bgcolor="Amber", leading=Icon(icons.WARNING_ROUNDED),
                content=Text(value="Product field is empty"),
                 actions=[
                    TextButton("Ok", on_click=self.close_banner)],
                ) 
            
            self.page.banner = msg
            msg.open = True
            self.update()
            self.page.update()

        else:
             #clear & update
            new_product = (self.productname.value,float(self.productprice.value),int(self.productqty.value), "None") 
            db().add_single_product(val=new_product)
            table = self.stocktable_updating(productdb=db().getstockvalue())
            table.controls.clear()
            self.stocktable_updating(productdb=db().getstockvalue())

            msg = SnackBar(content=Text(
                f"Product              "), 
                action="Ok")
            self.page.snack_bar = msg
            msg.open = True

            if self.page.banner == True:
                self.page.banner = False
            
            self.productname.value = ""
            self.productprice.value = 0.0
            self.productqty.value = 0

            self.update_stock_summary()
            self.update()
            self.page.update()
        
        
    def on_hover(self,e):
        e.control.bgcolor="#065080" if e.data == "true" else "White"
        e.control.content.controls[1].color="white" if e.data == "true" else "Black"
        e.control.update()
    

    def go_home(self, e):
        #print("clicked")
        self.page.go("/homepage")
        
    

    def build(self):
        return Container(
            #alignment=alignment.center,
            expand=True,
            content=Column(
                controls=[
                    #topbar
                    Container(
                        alignment=alignment.center,
                        #expand=True,
                        height=50,
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        bgcolor="#065080",

                        content = Row(
                            alignment="SpaceBetween",
                             controls =[
                                IconButton(icon=icons.HOME_ROUNDED, on_click=self.go_home, icon_color="White"),
                                Text(value="PRODUCT / STOCK VALUE", font_family="Poppins Bold", size=18, color="Amber"),
                                Tooltip(
                                message="IF NECESSARY TO DELETE, Long Press on the Product Item to DELETE, KINDLY NOTE: This action is IRREVERSIBLE",
                                content=Text("Delete Product", color="White"),
                                padding=20,
                                border_radius=10,
                                text_style=ft.TextStyle(size=13, color="Amber")),
                                Text(value=""),

                             ]),
                    ),


                    #main content
                    Container(
                        alignment=alignment.top_center,
                        #expand=True,
                        height=600,
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        #bgcolor="green",

                        content = Row(
                            
                             controls =[
                                #product session
                                Container(
                                    width=350,
                                    alignment=alignment.top_center,
                                    border=border.all(1,"#065080"),
                                    #bgcolor="red",
                                    content=Column(
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                height=120,
                                                content=Image(src="images/product2.jpg"),
                                            ),
                                            Container(
                                                 height=400,
                                                 alignment=alignment.center,
                                                 padding = padding.all(10),
                                                 content=Column(
                                                     controls=[
                                                         Row(
                                                             wrap = True,
                                                             controls=[
                                                                 
                                                                #self.selectfile,

                                                             ]
                                                         ),
                                                        
                                                        Container(
                                                            alignment=alignment.center,
                                                            content= self.productForm
                                                        ),
                                                     ]
                                                 )
                                            ),
                                            
                                        ]
                                    )
                                ),
                                
                                #stock session
                                Container(
                                    alignment = alignment.top_center,
                                    width = 900,
                                    #bgcolor="Amber",
                                    content=Column(
                                             alignment=CrossAxisAlignment.CENTER,
                                         controls=[
                                            #search stock
                                            Container(
                                                alignment=alignment.center,
                                                height = 80,
                                                width = 850,                                              
                                                #expand=True,
                                                    content = Row(
                                                        alignment = "SpaceBetween",

                                                        controls=[                                                          
                                                           self.searchproduct,
                                                           self.productcount,
                                                           self.stockvalue,

                                                        ]
                                                    )

                                                    
                                             ),
                                            
                                            #display stock datatables
                                            Container(
                                                  alignment=alignment.center,
                                                content=Column(
                                                    scroll="auto",
                                                    spacing = 0,
                                                    controls=[self.stocktable_updating(productdb = db().getstockvalue())]
                                                )
                                            ),
                                            
                                            #stock summary
                                            Container(),
                                        ]
                                    )
                                       
                                ),
                             ]),
                    ),
                    
                    
                ]
            )
        )


#top dashboard
class topdashboard(UserControl):
    def __init__(self, summary, value):
        super().__init__()

        self.summary = summary
        self.value = value    

    def build(self):
        return Container(
                        width=250,
                        height=115,
                        alignment=alignment.center,
                        border=border.all(1,"#ebebeb"),
                        border_radius=10,
                        padding=padding.only(left=15, top=12),

                        content= Column(spacing=10,
                                height=110,
                                width=250,
                                controls=[
                                    Icon(icons.BAR_CHART_ROUNDED),
                                    Text(value=self.summary, font_family="Poppins Semibold", size=12, color="#C70039"),
                                    Text(value=self.value, size=15, color="Black", font_family="Poppins Bold"),
                                    ])                     
                        
                        )


class charttopdashboard(UserControl):
    def __init__(self, yr, on_year_click):
        super().__init__()

        self.on_year_click = on_year_click
        self.yr = yr    

    def on_hover(self,e):
        e.control.bgcolor="#7488b3" if e.data == "true" else "White"
        e.control.content.controls[1].color="white" if e.data == "true" else "Black"
        e.control.update()

    def build(self):
        return Container(
            width=130,
            height=40,
            alignment=alignment.center,
            border=border.all(1,"#ebebeb"),
            border_radius=10,
            on_hover= self.on_hover,
            on_click=self.on_year_click,
            padding=padding.only(top=10),

            content=Row(
                alignment="center",
                controls=[
                    Icon(icons.DASHBOARD_ROUNDED),
                    Text(value=self.yr),
                    ])
        )

     
#dashboars summary
class dashboardpage(UserControl):
    def __init__(self):
        super().__init__()

        self.monthlysummary = Column(spacing=10,
                                    height=500,
                                    width=250,
                                    scroll="auto",
                                    )

        self.monthlychart = Column(spacing=10,
                                    height=300,
                                    width=900,
                                    scroll="auto",
                                    )
        
        self.topmoving = Column(spacing=10,
                                    height=500,
                                    width=400,
                                    scroll="auto",
                                    )

        self.yrs = Row(alignment="center")
        #run load monthly summary function
        self.load_monthly_summary(yr=str(date.today().year))


        #top dashboard summary
        self.monthlysalesavg = topdashboard(summary="Average Monthly Sales", value= db().average_monthly_sales())
        self.dailysalesavg = topdashboard(summary="Average Daily Sales", value= db().average_daily_sales())
        self.ytd = topdashboard(summary="Year To Date (YTD)", value= db().YTD())
        self.dailycountavg = topdashboard(summary="Average Daily Customers", value= db().average_daily_customer())
        
    

        #choosen year
        yr = db().get_sales_yrs()
        yrs = [charttopdashboard(yr=i, on_year_click=self.on_year_click) for i in yr]
        for i in yrs:
            self.yrs.controls.append(i)

        
        
        #adding chart
        #self.monthlychart.controls.append(saleschart(yr=str(date.today().year)))


        #report download
        self.sales_report = reportdownload()


    def load_monthly_summary(self, yr):
        #summary = db().get_monthlysummary(yr=yr)
        summary = Database().monthlysummaries2(yr=yr)
        for s in summary:
            self.monthlysummary.controls.append(
                        Container(
                        
                        border=border.all(1,"#ebebeb"),
                        border_radius=5,
                        bgcolor="White",
                        on_click = self.show_daily_sales,
                        on_hover= self.on_hover,
                        content= Column(
                            controls=[
                                Text(value=s, visible=False),
                                Text(value=f'{calendar.month_abbr[int(s[0])]}: {"GHS {:,.2f}".format(s[1])}', color="#3F4D5B"),
                            ]
                             
                        ) 
                        
                        #Text(value=f'{calendar.month_abbr[int(s[0])]}: {"GHS {:,.2f}".format(s[1])}', color="#3F4D5B")
                    ))

        


    def on_year_click(self,e):
        yr = e.control.content.controls[1].value
        #print(yr)
        self.monthlysummary.controls.clear()
        self.monthlychart.controls.clear()

        #reload
        self.load_monthly_summary(yr=yr)
        self.monthlychart.controls.append(saleschart_bar(yr=yr))
        self.update()
        pass

    def show_daily_sales(self,e):
        s = e.control.content.controls[0].value
        v = e.control.content.controls[1].value

        #print(s)
        #print(v)
        mnth_name = calendar.month_abbr[int(s[0])]
        #print(s[2])
        #print(mnth_name)

        #clear chart
        self.monthlychart.controls.clear()
        #print("cleared")

        #load daily sales chart
        self.monthlychart.controls.append(saleschart_daily_bar(mnth=s[2], mnth_name=mnth_name))
        self.update()
        pass

    def on_hover(self,e):
        e.control.bgcolor="#641E16" if e.data == "true" else "White"
        e.control.content.controls[1].color= "White" if e.data == "true" else "Black"
        e.control.update()


    def go_home(self, e):
        #print("clicked")
        self.page.go("/homepage")


    def build(self):
        return Container(

            expand=True,
            content=Column(
                spacing=0,

                controls=[
                    #topbar
                    Container(
                        alignment=alignment.center,
                        #expand=True,
                        height=50,
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        bgcolor="#065080",

                        content = Row(
                                alignment="SpaceBetween",
                             controls =[
                                IconButton(icon=icons.HOME_ROUNDED, on_click=self.go_home, icon_color="White"),
                                Text(value="SALES SUMMARY / DASHBOARD", font_family="Poppins Bold", size=18, color="White"),
                                Text(value=""),

                             ]),
                        ),
                        
                         
                        
                       #top dashboard summary 
                    Container(
                           
                            alignment=alignment.center,
                            #expand=True,
                            height=100,
                            border_radius=border_radius.only(bottom_left=10, bottom_right=10),
                            #bgcolor= "Yellow",#065080",

                                content = Row(
                                    #alignment="center",

                                    controls =[
                                        Image(src="images/dshbrd1.png", width=250),
                                        self.monthlysalesavg,
                                        self.dailysalesavg,
                                        self.ytd,
                                        self.dailycountavg,
                                        #self.dailycountavg,
                                        
                                    ]),


                       ),
                        #divider
                    Container(
                            alignment=alignment.center,
                            #expand=True,
                            height=10,
                            border_radius=border_radius.only(bottom_left=10, bottom_right=10),
                            bgcolor="#065080",

                            content = Row(
                                controls =[
                                    
                                ]),
                            ),

                       #middle dashboard summary 
                    Row(
                           alignment="SpaceEvenly",
                           spacing=0,
                           controls=[
                               
                               #month summary
                               Container(
                                    alignment= alignment.center,
                                    width=250,
                                    height=470,
                                    bgcolor="#34495E",
                                    border_radius=border_radius.only(top_left=15, top_right=15),
                                    border=border.all(1,"#05204d"),
                                    padding=padding.only(left=15, top=10),

                                    content = Column(

                                        controls=[
                                            Text(
                                                value="Monthly sales summary",
                                                size=15, color="Yellow", font_family="Poppins Bold"
                                                ),
                                            self.monthlysummary
                                        ]

                                             
                                        
                                    )
                               ),

                               #chart
                                Container(
                                    #bgcolor="#85C1E9",  
                                    #height=300,
                                    width=1000,  
                                    content=Column(
                                        controls=[

                                             Container(
                                                height=80,
                                                width=1000,
                                                bgcolor="#1B4F72",
                                                alignment=alignment.center,
                                                border_radius=border_radius.only(bottom_left=10, bottom_right=10),
                                                border=border.all(1,"#ebebeb"),

                                                content=Text(value="SALES TREND, values in thousands (,000) ",
                                                             size=18, font_family="Poppins Bold", color="AMBER")
                                                #content=None,
                                            ),

                                            Divider(height=9, thickness=3),

                                            self.yrs,

                                            Column(
                                            controls=[

                                                    #Text(value="Sales Trend"),
                                                    Container( 
                                                                                    
                                                        content=self.monthlychart 
                                                    ),

                                                    
                                                ]),  

                                                                                
                                        ]
                                    )
                                ),
                               
                           ]
                       ),

                    Container(
                            alignment=alignment.center,
                            #expand=True,
                            height=120,
                            border_radius=border_radius.only(bottom_left=15, bottom_right=15),
                            bgcolor="#065080",

                            content = Row(
                                controls =[
                                    
                                ]),
                            ),



                        
                        ]
                 ),
        )



class saleschart(UserControl):
    def __init__(self, yr):
        super().__init__()
        self.yr = yr


        self.mnth_sum = db().get_max_month_sales(yr=self.yr)
        try:
            self.max_mnth = math.ceil(max([i[1] for i in self.mnth_sum]) * 1.2)
        except:
            self.max_mnth = 1000 #default monthly highest sales



    def build(self):
        data_1 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(int(i[0]), round(i[1],2)) for i in self.mnth_sum
            ],
            stroke_width=2,
            color="Black",
            curved=True,
            stroke_cap_round=True,
            )
        ]

    
        chart = ft.LineChart(
            data_series=data_1,
            border=ft.border.all(2, ft.colors.with_opacity(0.1, ft.colors.ON_SURFACE)),
            horizontal_grid_lines=ft.ChartGridLines(
                interval=1, color=ft.colors.with_opacity(0.1, ft.colors.ON_SURFACE), width=2
            ),
            vertical_grid_lines=ft.ChartGridLines(
                interval=1, color=ft.colors.with_opacity(0.1, ft.colors.ON_SURFACE), width=2
            ),
            left_axis=ft.ChartAxis(
                labels=[
                   
                    
                ],


                labels_size=40,
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=i,
                        label=ft.Container(
                            ft.Text(
                                value=calendar.month_abbr[i],
                                size=12,
                                weight=ft.FontWeight.NORMAL,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ) for i in range(1,13)
                    
                    
                ],
                labels_size=32,
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.WHITE),
            min_y=0,
            max_y=self.max_mnth,
            min_x=1,
            max_x=12,
            animate=5000,
            expand=True,
        )
        
        return chart


class saleschart_bar(UserControl):
    def __init__(self, yr):
        super().__init__()
        self.yr = yr
        
        self.db = db().get_max_month_sales(yr=self.yr)
        try:
            self.max_mnth = roundup(max([int(i[1]) for i in self.db]) * 1.2) * 1000
            
        except:
            self.max_mnth = 500000
        #print(self.max_mnth)

    def build(self):      
        chart = ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x= int(i[0]),
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=i[1],
                        width=25,
                        color=ft.colors.AMBER,
                        tooltip="GHS {:,.2f}".format(i[1]),
                        border_radius=0,
                    ),
                ],
            ) for i in self.db
            ],

        border=ft.border.all(1, ft.colors.GREY_400),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text(f"Monthly summary ({self.yr})"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=int(i[0]), label=ft.Container(ft.Text(f"{calendar.month_abbr[int(i[0])]}", size=11), padding=10)
                ) for i in self.db

            ],
            labels_size=40,
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
            max_y=self.max_mnth,
            interactive=True,
            expand=True,
        )
      
        return chart


class saleschart_daily_bar(UserControl):
    def __init__(self, mnth, mnth_name):
        super().__init__()
        self.mnth = mnth
        self.mnth_name = mnth_name

        self.db = Database().dailysales(mnth=self.mnth)
        self.max_mnth = math.ceil(max([i[1] for i in self.db]) * 1.2) 
        #print(self.db)
        #print(self.max_mnth)
        



    def build(self):      
        chart = ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x= int(i[0]),
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=i[1],
                        width=10,
                        color=ft.colors.AMBER,
                        tooltip="GHS {:,.2f}".format(i[1]),
                        border_radius=0,
                    ),
                ],
            ) for i in self.db
            ],

        border=ft.border.all(1, ft.colors.GREY_400),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text(f"Daily Sales ({self.mnth_name})"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=int(i[0]), label=ft.Container(ft.Text(f"{i[0]}", size=11), padding=10)
                ) for i in self.db

            ],
            labels_size=40,
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
            max_y=self.max_mnth,
            interactive=True,
            expand=True,
        )
      
        return chart

        
class reportdownload(UserControl):
    def __init__(self):
        super().__init__()

        
        self.cnt = None
        #self.dlg = AlertDialog(title=Text(value=self.rpt, size=15, color="Amber_400"), content=self.cnt)

    def sales_report_summary(self,e):
        opt = e.control.value
        #print(opt)

        if opt == "Daily":
            self.cnt = reportdailySales()
        
        if opt == "Monthly":
            self.cnt = reportmonthlySales()
        
        if opt == "Period":
            self.cnt = reportperiodSales()
        
        if opt == "Year":
            self.cnt = reportyearlySummary()


        #dlg = AlertDialog(title=Text(value=self.rpt, size=15, color="Amber_400"), content=self.cnt)
        dlg = AlertDialog(content=self.cnt)

        #open report dialog
        self.page.dialog = dlg
        dlg.open = True
        self.update()
        self.page.update()
        

    def stock_report_summary(self,e):
        opt = e.control.value
        #print(opt)

        if opt == "stock qty":
            self.cnt = stockquantity()
        
        if opt == "out of stock":
            self.cnt = outofstocks()
        
        if opt == "stock valuation":
            self.cnt = stocksvaluation()
        

        if opt == "stock adjustments":
            self.cnt = stocksadjustments()
        

        if opt == "stock received":
            self.cnt = stocksreceived()
        


        #dlg = AlertDialog(title=Text(value=self.rpt, size=15, color="Amber_400"), content=self.cnt)
        dlg = AlertDialog(content=self.cnt)

        #open report dialog
        self.page.dialog = dlg
        dlg.open = True
        self.update()
        self.page.update()
     

    def product_report_summary(self,e):
        opt = e.control.value
        #print(opt)

        if opt == "sales history":
            self.cnt = productsaleshistory()
        
        if opt == "top":
            self.cnt = topmovingproduct()
        
        if opt == "bottom":
            self.cnt = bottomnonmovingproduct()
        


        #dlg = AlertDialog(title=Text(value=self.rpt, size=15, color="Amber_400"), content=self.cnt)
        dlg = AlertDialog(content=self.cnt)

        #open report dialog
        self.page.dialog = dlg
        dlg.open = True
        self.update()
        self.page.update()
     
   

    def build(self):
        sales =  Container(
            width=200,
            height=60,
            alignment=alignment.center,
            padding = padding.only(top=5),
            bgcolor = "White",
            border=border.all(1,"Black"),
            border_radius=8,

            content=Column(
               # spacing=0,
                controls=[
                     #Text(value=""),
                     Dropdown(
                         label="Sales report",
                        on_change=self.sales_report_summary,
                        options=[
                            dropdown.Option("Daily"),
                            dropdown.Option("Monthly"),
                            #dropdown.Option("Period"),
                            dropdown.Option("Year"),
                        ],
                        width=200,
                        height=50,
                        border_width=0.5,
                        border_color = "White",
                        #autofocus=True,
                        #bgcolor="Blue",
                        #focused_bgcolor="White",
                        color="Black",
                        #focused_border_color="Amber"
                        
                        )

                ]
               

            )

        )


        stocks =  Container(
            width=200,
            height=60,
            alignment=alignment.center,
            padding = padding.only(top=5),
            bgcolor = "White",
            border=border.all(1,"Black"),
            border_radius=8,

            content=Column(
               # spacing=0,
                controls=[
                     #Text(value=""),
                     Dropdown(
                        label="Stocks report",
                        on_change=self.stock_report_summary,
                        options=[
                            dropdown.Option("stock qty"),
                            dropdown.Option("out of stock"),
                            dropdown.Option("stock valuation"),
                            dropdown.Option("stock adjustments"),
                            dropdown.Option("stock received"),
                        ],
                        width=200,
                        height=50,
                        border_width=0.5,
                        border_color = "White",
                        #autofocus=True,
                        #bgcolor="White",
                        #focused_bgcolor="White",
                        color="Black",
                        #focused_border_color="Amber"
                        
                        )

                ]
               

            )

        )


        products =  Container(
            width=200,
            height=60,
            alignment=alignment.center,
            padding = padding.only(top=5),
            bgcolor = "White",
            border=border.all(1,"Black"),
            border_radius=8,

            content=Column(
               # spacing=0,
                controls=[
                     #Text(value=""),
                     Dropdown(
                         label="product report",
                        on_change=self.product_report_summary,
                        options=[
                            dropdown.Option("sales history"),
                            dropdown.Option("top"),
                            dropdown.Option("bottom"),
                        ],
                        width=200,
                        height=50,
                        border_width=0.5,
                        border_color = "White",
                        #autofocus=True,
                        #bgcolor="White",
                        #focused_bgcolor="White",
                        color="Black",
                        #focused_border_color="Amber"
                        
                        )

                ]
               

            )

        )


        return Row(
            alignment="center",
            controls=[
                sales,
                stocks,
                products,
            ]
        )


class reportdailySales(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdate = TextField(label="Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()))


        self.typ = "Daily sales"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdate,  arg2=None, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdate,  arg2=None, typ=self.typ)
       

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=15, 
                     height=200, 
                     width=300,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdate,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt


class reportmonthlySales(UserControl):
    def __init__(self):
        super().__init__()

        self.rptyr = TextField(label="Year",border_radius=8,icon=icons.CALENDAR_VIEW_MONTH, value=str(date.today().year))
        self.rptmnth = TextField(label="Month",border_radius=8,icon=icons.CALENDAR_VIEW_MONTH, value=str(date.today().month))

        self.typ = "Monthly sales"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptyr,  arg2=self.rptmnth, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptyr,  arg2=self.rptmnth, typ=self.typ)

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=10, 
                     height=230, 
                     width=300,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),


                        self.rptyr,
                        self.rptmnth,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt


class reportperiodSales(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdt1 = TextField(label="Start Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()))
        self.rptdt2 = TextField(label="End Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()))


        self.typ="Period sales"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdt1,  arg2=self.rptdt2, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdt1,  arg2=self.rptdt2, typ=self.typ)

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=10, 
                     height=230, 
                     width=300,
                controls=[

                         Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdt1,
                        self.rptdt2,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt


class reportyearlySummary(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdate = TextField(label="Year",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today().year))


        self.typ = "Yearly summary"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdate,  arg2=None, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdate,  arg2=None, typ=self.typ)
       

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=15, 
                     height=200, 
                     width=300,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdate,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt


class reportpage(UserControl):
    def __init__(self):
        super().__init__()


        self.sales_report = reportdownload()
 

        self.show = Container(
                        
                        height=150,
                        visible=False,
                        content=Row(
                            alignment="center",
                            controls=[

                                self.sales_report
                                
                            ]
                        ))

        self.pwdcontainer = Column(spacing=1, height=80, width=100)
        self.pwd = AlertDialog(modal=True, title=Text(value="passcode", size=15), content=self.pwdcontainer)

        
    
    def show_access_dlg(self,e):
        self.pwdcontainer.controls.clear()
        p = TextField(label="code",border_radius=8, icon=icons.PASSWORD_OUTLINED, on_submit=self.confirm_code)
        self.pwdcontainer.controls.append(p)
       
        #open qty dialog
        self.page.dialog = self.pwd
        self.pwd.open = True
        self.page.update()
        pass


    def confirm_code(self,e):
        c = e.control.value

        auth = [k[1] for k in Database().get_superusers()]

        if c in auth:
            self.show.visible = True
            self.update()
            self.page.update()

        self.page.dialog.open = False
        self.update()
        self.page.update()



    def go_home(self, e):
        #print("clicked")
        self.page.go("/dashboardpage")

    def build(self):
        
        pg = Column(
            controls=[
                #topbar
                    Container(
                        alignment=alignment.center,
                        #expand=True,
                        height=50,
                        border_radius=border_radius.only(top_left=15, top_right=15),
                        bgcolor="#065080",

                        content = Row(
                            alignment="SpaceBetween",
                             controls =[
                                IconButton(icon=icons.ARROW_BACK_OUTLINED, on_click=self.go_home, icon_color="White"),
                                Text(value="SUMMARY REPORT", font_family="Poppins Bold", size=18, color="Amber"),
                                Text(value=""),
                                
                             ]),
                        ),

                    #save as section
                    self.show,
                    #Container(
                        
                    #    height=150,
                    #    visible=False,
                    #    content=Row(
                    #        alignment="center",
                    #        controls=[

                    #            self.sales_report
                                
                    #        ]
                    #    )),

                    #divider
                    Container(
                           
                            #expand=True,
                            height=10,
                            border_radius=border_radius.only(bottom_left=10, bottom_right=10),
                            bgcolor="#065080",

                            content = Row(
                                controls =[
                                    
                                ]),
                            ),


                                     
                    
                    Divider(height=2, thickness=1),

                    #report summary
                    Column(
                        alignment= CrossAxisAlignment.CENTER,
                        width=1000,
                        height=500,

                        controls=[
                            Container(
                                on_click=self.show_access_dlg,
                                
                                content=Image(src="images/salesrpt.png", width=1000, height=400)
                            )
                            
                        ]

                    )

            ]
        )
       
        return pg


class saveas(UserControl):
    def __init__(self, saveas, ext, arg1, arg2, typ):
        super().__init__()

        self.ext = ext
        self.saveas = saveas
        self.arg1 = arg1
        self.arg2 = arg2
        self.typ = typ
        
        self.save_files_dialog = FilePicker(on_result=self.save_file_result)
        self.save_file_path = Text()



        self.file_to_save = Row(
                controls=[
                    ft.ElevatedButton(
                        f".{self.saveas}",
                        #icon=icons.UPLOAD_FILE,
                        Image(src=f"images/{self.ext}.png", width=20, height=20),
                        on_click=lambda e: self.save_files_dialog.save_file(
                            file_name="", allowed_extensions=["xlsx","pdf"]),               
                    ),
                    self.save_file_path,
                ])

        self.file_to_save.controls.append(self.save_files_dialog)


    # Save file dialog
    def save_file_result(self, e: FilePickerResultEvent):
        ext = f".{self.saveas}"
        if e.path:
            #print(e.path)
            flname =  f"{e.path}{ext}"

            #check file extension
            #print(pathlib.Path(path).suffix)
            if pathlib.Path(flname).suffix == ".xlsx":
                if self.typ == "Daily sales":
                    #print("downloading daily sales report...")
                    dbReport.download_daily_sales_as_xlsx(p=flname, dt=self.arg1.value)

                if self.typ == "Monthly sales":
                    print("downloading Monthly sales report...")
                    dbReport.download_monthly_sales_as_xlsx(p=flname, yr=self.arg1.value, mnt=self.arg2.value)

                if self.typ == "Period sales":
                    print("downloading Period sales report...")

                if self.typ == "Yearly summary":
                    print("downloading Yearly sales report...")
                    dbReport.download_yearly_summary_as_xlsx(p=flname, yr=self.arg1.value)
               

                #stock session
                if self.typ == "Stock Qty":
                    print("downloading stock qty report...")
                    dbReport.download_stock_qty_as_xlsx(p=flname)
                
                if self.typ == "Out of Stocks":
                    print("downloading out of stock report...")
                    dbReport.download_out_out_of_stocks_as_xlsx(p=flname)
                
                if self.typ == "Stocks Valuation":
                    print("downloading stock valuation report...")
                    dbReport.download_stocks_valuation_as_xlsx(p=flname)
                
                if self.typ == "Stocks adjustments":
                    print("downloading stock adjustments report...")
                    dbReport.download_stocks_adjustments_as_xlsx(p=flname)
                
                if self.typ == "Stocks Received":
                    print("downloading stock Received report...")
                    dbReport.download_stocks_received_as_xlsx(p=flname)



                #product session
                if self.typ == "Product Sales History":
                    print("downloading  saleshistory report...")
                    dbReport.download_productsales_history_as_xlsx(p=flname, k=self.arg2.value)


                if self.typ == "Top Moving Product":
                    print("downloading Top moving report...")
                    dbReport.download_top_selling_as_xlsx(p=flname, k=int(self.arg2.value))


                if self.typ == "Non Moving Product":
                    print("downloading Bottom nonmoving report...")
                    dbReport.download_least_selling_as_xlsx(p=flname, k=int(self.arg2.value))



        if pathlib.Path(flname).suffix == ".pdf":
            if self.typ == "Daily sales":
                #print("downloading daily sales report...")
                dbReport.download_daily_sales_as_pdf(p=flname, dt=self.arg1.value)
            
            if self.typ == "Monthly sales":
                print("downloading Monthly sales report...")
                dbReport.download_monthly_sales_as_pdf(p=flname, yr=self.arg1.value, mnt=self.arg2.value)

            if self.typ == "Period sales":
                    print("downloading Period sales report...")

            if self.typ == "Yearly summary":
                print("downloading Yearly sales report...")
                dbReport.download_yearly_summary_as_pdf(p=flname, yr=self.arg1.value)
            

            #stock session
            if self.typ == "Stock Qty":
                print("downloading stock qty report...")
                dbReport.download_stock_qty_as_pdf(p=flname)
            
            if self.typ == "Out of Stocks":
                print("downloading out of stock report...")
                dbReport.download_out_out_of_stocks_as_pdf(p=flname)
            
            if self.typ == "Stocks Valuation":
                print("downloading stock valuation report...")
                dbReport.download_stocks_valuation_as_pdf(p=flname)
            
            if self.typ == "Stocks adjustments":
                print("downloading stock adjustments report...")
                dbReport.download_stocks_adjustments_as_pdf(p=flname)
            
            if self.typ == "Stocks Received":
                print("downloading stock Received report...")
                dbReport.download_stocks_received_as_pdf(p=flname)






            #product session
            if self.typ == "Product Sales History":
                print("downloading  saleshistory report...")
                dbReport.download_productsales_history_as_pdf(p=flname, k=self.arg2.value)


            if self.typ == "Top Moving Product":
                print("downloading Top moving report...")
                dbReport.download_top_selling_as_pdf(p=flname, k=int(self.arg2.value))


            if self.typ == "Non Moving Product":
                print("downloading Bottom nonmoving report...")
                dbReport.download_least_selling_as_pdf(p=flname, k=int(self.arg2.value))



        #self.save_file_path.value = e.path if e.path else "Cancelled!"
        #print(self.page.dialog)
        self.page.dialog.open = False
        self.page.update()

        self.save_file_path.update()


    def generate_report(self,e):
        dt = self.arg1.value
        print(dt)
        

    def build(self):

        return Container(
                        width=100,
                        height=40,
                        alignment=alignment.center,
                        border_radius=10,
                        on_click = lambda e: self.save_files_dialog,
                        #on_click = self.generate_report,
                        content=Row(
                            alignment="center",
                            controls=[
                                self.file_to_save,
                            ]
                            
                        ))



class stockquantity(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdate = TextField(label="Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()), read_only="True")


        self.typ = "Stock Qty"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdate,  arg2=None, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdate,  arg2=None, typ=self.typ)
       

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=15, 
                     height=200, 
                     width=300,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdate,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt



class outofstocks(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdate = TextField(label="Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()), read_only="True")


        self.typ = "Out of Stocks"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdate,  arg2=None, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdate,  arg2=None, typ=self.typ)
       

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=15, 
                     height=200, 
                     width=300,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdate,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt



class stocksvaluation(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdate = TextField(label="Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()), read_only="True")


        self.typ = "Stocks Valuation"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdate,  arg2=None, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdate,  arg2=None, typ=self.typ)
       

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=15, 
                     height=200, 
                     width=300,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdate,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt



class stocksadjustments(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdate = TextField(label="Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()), read_only="True")


        self.typ = "Stocks adjustments"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdate,  arg2=None, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdate,  arg2=None, typ=self.typ)
       

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=15, 
                     height=200, 
                     width=300,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdate,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt


class stocksreceived(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdate = TextField(label="Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()), read_only="True")


        self.typ = "Stocks Received"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdate,  arg2=None, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdate,  arg2=None, typ=self.typ)
       

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=15, 
                     height=200, 
                     width=300,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdate,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt


class productsaleshistory(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdate = TextField(label="Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()), read_only="True")
        self.prdt = Dropdown(label="Product", height=50, width=320, border_width=0.5, dense=True, text_size=12)

        self.typ = "Product Sales History"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdate,  arg2=self.prdt, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdate,  arg2=self.prdt, typ=self.typ)
       
        
        a = [i[0].upper() for i in Database().get_products() if i[0] != ""]
        self.prdt.options = [dropdown.Option(str(i)) for i in a]


    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=15, 
                     height=250, 
                     width=350,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdate,
                        Row(
                            controls=[
                                Icon(icons.PRODUCTION_QUANTITY_LIMITS_ROUNDED),
                                self.prdt,
                            ]
                        ),
                        
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt


class topmovingproduct(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdate = TextField(label="Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()), read_only="True")
        self.input = TextField(label="Top?: Input",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=5)

        self.typ = "Top Moving Product"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdate,  arg2=self.input, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdate,  arg2=self.input, typ=self.typ)
       

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=15, 
                     height=250, 
                     width=300,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdate,
                        self.input,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt


class bottomnonmovingproduct(UserControl):
    def __init__(self):
        super().__init__()

        self.rptdate = TextField(label="Date",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=str(date.today()), read_only="True")
        self.input = TextField(label="Bottom?: Input",border_radius=8,icon=icons.CALENDAR_VIEW_DAY_ROUNDED, value=5)

        self.typ = "Non Moving Product"
        self.xlsave = saveas(saveas="xlsx", ext='asxl', arg1=self.rptdate,  arg2=self.input, typ=self.typ)
        self.pdfsave = saveas(saveas="pdf", ext='aspdf',arg1=self.rptdate,  arg2=self.input, typ=self.typ)
       

    def go_to_reportpage(self, e):
        #print("clicked")
        self.page.go("/reportpage")


    def build(self):     
        cnt = Column(
                     spacing=15, 
                     height=250, 
                     width=300,
                controls=[

                        Container(
                            width=300,
                            height=30,
                            alignment=alignment.center,
                            content=Text(value=self.typ, size=14, font_family="Poppins Bold")
                        ),

                        self.rptdate,
                        self.input,
                        Row(
                            alignment="center",
                            controls=[
                                self.xlsave,
                                self.pdfsave,
                            ]
                        )

                         ]     
                     )
        return cnt


class Bprofile(UserControl):
    def __init__(self):
        super().__init__()

        try:
            self.a =  Database().get_all_data(table="company")[0]
        except:
            self.a = "Bussiness name"
        
    def dialog_dismiss(self):
        self.page.dialog.open = False
        self.update()
        self.page.update()
    


    def build(self):
        prfl = Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            #leading=ft.Icon(ft.icons.BUSINESS_CENTER_ROUNDED),
                            #title=ft.Text("Bussines Profile"),
                            subtitle= Column(
                                controls=[
                                    Row(
                                        controls=[
                                            Icon(icons.BUSINESS),
                                            Text(value="Business Name:  ", font_family="Poppins Bold", color="#641E16"),
                                            Text(value=self.a[0]),
                                        ]
                                    ),
                                    Row(
                                        controls=[
                                            Icon(icons.LOCATION_CITY_ROUNDED),
                                            Text(value="Address:  ", font_family="Poppins Bold", color="#641E16"),
                                            Text(value=self.a[1]),
                                        ]
                                    ),
                                    Row(
                                        controls=[
                                            Icon(icons.MAP_ROUNDED),
                                            Text(value="Location:", font_family="Poppins Bold", color="#641E16"),
                                            Text(value=self.a[2]),
                                        ]
                                    ),
                                    Row(
                                        controls=[
                                            Icon(icons.PHONE_CALLBACK_ROUNDED),
                                            Text(value="Contacts:", font_family="Poppins Bold", color="#641E16"),
                                            Text(value=self.a[3]),
                                            Text(value=self.a[4]),
                                        ]
                                    ),
                                    Row(
                                        controls=[
                                            Icon(icons.MAIL_OUTLINE_ROUNDED),
                                            Text(value="Mailing:", font_family="Poppins Bold", color="#641E16"),
                                            Text(value=self.a[5]),
                                        ]
                                    ),
                                ]

                            ),
                        ),
                       
                    ]
                ),
                width=450,
                height=250,
                padding=10,
            )
        )
        return prfl


class readme(UserControl):
    def __init__(self):
        super().__init__()

        try:
            self.a =  Database().get_all_data(table="company")[0]
        except:
            self.a = "Bussiness name"
        
    def dialog_dismiss(self):
        self.page.dialog.open = False
        self.update()
        self.page.update()
    


    def build(self):
        rdme = Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading= Image(src="images/rdme1.png"),
                            title=ft.Text("Retail Helper (Rhpr_0.1)"),
                            subtitle= Column(
                                controls=[                                   
                                    Row(
                                        controls=[
                                            Icon(icons.CHECK),
                                            Text(value="Rhpr is designed for small to medium scale business")
                                        ]),
                                    
                                    Row(
                                        controls=[
                                            Icon(icons.CHECK),
                                            Text(value="App usually has dummy data for Demo purposes")
                                        ]),
                                    
                                    Row(
                                        controls=[
                                            Icon(icons.CHECK),
                                            Text(value="Stand alone App with no internet connection required")
                                        ]),
                                    
                                    Row(
                                        controls=[
                                            Icon(icons.CHECK),
                                            Text(value="You can always create a backup of your data unto your PC or external source")
                                        ]),
                                    
                                    Row(
                                        controls=[
                                            Icon(icons.CHECK),
                                            Text(value="Default Login: username-:rhpr  passwords-:12345")
                                        ]),
                                    
                                    Row(
                                        controls=[
                                            Icon(icons.CHECK),
                                            Text(value="After review with dummy data, go to settings, edit business profile and initialize app for use")
                                        ]),

                                    Row(
                                        controls=[
                                            Icon(icons.PERSON),
                                            Text(value="Developer: George"),
                                            Icon(icons.PHONE),
                                            Text(value="Contact: +233549053295"),
                                            Icon(icons.MAIL),
                                            Text(value="email: ayittey.og@gmail.com"),
                                        ]),
                                   
                                    
                                ]

                            ),
                        ),
                       
                    ]
                ),
                width=800,
                height=350,
                padding=10,
            )
        )
        return rdme


#next page
