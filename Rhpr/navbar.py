import flet
from flet import *
from functools import partial
from myFunc import show_date
import time



#side bar class
class ModernNavBar(UserControl):
    def __init__(self, username, user, page):
        self.username = username
        self.user = user
        super().__init__()
        self.page = page

        

    #highlight row on hover
    def highlight(self, e):
        if e.data == 'true':
            e.control.bgcolor = "white10"
            e.control.update()

            #change icon/text color on hover
            e.control.content.controls[0].icon_color = "white"
            e.control.content.controls[1].color = "white"
            e.control.content.update()

        else:
            e.control.bgcolor = None
            e.control.content.controls[1].color = "white54"
            e.control.update()

            #revert text color on hover
            e.control.content.controls[0].icon_color = "#F1E356"
            e.control.content.controls[1].color = "#F1E356"
            e.control.content.update()

    def UserData(self, initials:str, name:str, desc:str):
        #
        return Container(
            content=
            
            Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor="bluegrey900",
                        alignment=alignment.center,
                        content=Text(
                            value=initials,
                            size=10,
                            weight="bold",
                            color="white",
                        ),
                    ),

                    Column(
                        spacing=1,
                        alignment = "center",
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                weight="bold",
                                color="white",
                                #include animation effect here
                                opacity=1,
                                animate_opacity=200 #speed of animation 

                            ),

                            Text(
                                value=desc,
                                size=9,
                                weight="w400",
                                color="white54",
                                #include animation effect here
                                opacity=1,
                                animate_opacity=200 #speed of animation 

                            )
                        ]
                    ),
                ]
            )
        )

    #navigation click
    def on_nav_click(self, e):
        name = e.control.content.controls[1].value
        #print(name) 
        if name == "Logout":
            self.page.go("/login")
        
        if name == "Products":
            #self.page.go("/productpage")
            self.page.go("/authaccessproduct")
        
        if name == "Dashboard":
            self.page.go("/dashboardpage")
        
        if name == "Report":
            self.page.go("/reportpage")
        
        if name == "users":
            self.page.go("/authaccessuser")
        
        if name == "settings":
            self.page.go("/authaccesssettings")



    def ContainedIcon(self, icon_name:str,  text:str):

        return Container(
            #set dimensions
            width=180,
            height=45,
            border_radius=10,
            on_click=self.on_nav_click,
            on_hover=lambda e: self.highlight(e),


            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color="#F1E356",
                        style=ButtonStyle(
                            shape={
                                "":RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"":"transparent"},

                        ),
                        
                        
                    ),

                    Text(
                        value=text,
                        color="#F1E356",
                        size=11,
                        opacity=1,
                        animate_opacity=20,
                        
                    
                    )
                ]
            ),
        )


    #animating the sidebar
    def AnimateSidebar(self, e):
        #check the current width of the container
        if self.controls[0].width != 62:

            #iterate over the rows in the container and set opacity to zero
            #firt the postion of the Text()
            for item in (
                self.controls[0] #content of the container
                .content.controls[0] #now at the UserData container
                .content.controls[1] #now at the Text of the UserData controls
                .controls[:] #all items in there
            ):
                item.opacity= 0 
                item.update()
            
            #reducing opacity of the sidebar items
            for item in self.controls[0].content.controls[3:]:
                if isinstance(item, Container):
                    item.content.controls[1].opacity = 0
                    item.content.update()

            #minize the container's width        
            time.sleep(0.2)
            self.controls[0].width = 62
            self.controls[0].update()

        #revert back    
        else:            
            self.controls[0].width = 180
            self.controls[0].update()
            time.sleep(0.2)
            
            for item in self.controls[0].content.controls[0].content.controls[1].controls[:]:
                item.opacity= 1
                item.update()

            for item in self.controls[0].content.controls[3:]:
                if isinstance(item, Container):
                    item.content.controls[1].opacity = 1
                    item.content.update()
        pass


    def build(self):
        return Container(

            #define the dimensions and characteristics of the returned container
            width=180,
            #height=580,
            #height=600,
            padding=padding.only(top=10),
            #border_radius=10,
            alignment=alignment.center,
            content=
                Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment="center",

                    controls=[
                   
                    #add sidebar icons/content hers
                    self.UserData("RHpr ",self.username, self.user),


                    #manage sidebar colapsible
                    Container(
                        width=24,
                        height=24,
                        bgcolor="bluegrey800",
                        
                        #border_radius=8,
                        on_click=self.AnimateSidebar,
                        content=Icon(icons.ARROW_BACK_ROUNDED, color="White"),
                    ),


                    #add a divider
                    Divider(height=5, color='transparent'),
                    self.ContainedIcon(icons.SELL_ROUNDED, "Pos"),
                    self.ContainedIcon(icons.DASHBOARD_ROUNDED, "Dashboard"),
                    self.ContainedIcon(icons.PRODUCTION_QUANTITY_LIMITS_ROUNDED, "Products"),
                    self.ContainedIcon(icons.PIE_CHART_OUTLINE_SHARP, "Report"),
                    self.ContainedIcon(icons.VERIFIED_USER_ROUNDED, "users"),
                    self.ContainedIcon(icons.SETTINGS_APPLICATIONS_ROUNDED, "settings"),
                    Divider(height=5, color="white24"),
                    self.ContainedIcon(icons.LOGOUT_ROUNDED, "Logout"),
                    ]
                ),

        )       




