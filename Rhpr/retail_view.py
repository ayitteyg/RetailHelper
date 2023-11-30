from flet import *
from retail_templates import *


#create app view here

def views_handler(page):
    return{

        #home view
        "/login":View("/login", [ApplicationLogin(page)] ),
        "/authaccessproduct":View("/authaccessproduct", [authaccessproduct()] ),
        "/authaccessuser":View("/authaccessuser", [authaccessuser()] ),
        "/authaccesssettings":View("/authaccesssettings", [authaccesssettings()] ),
        "/appsettings":View("/appsettings", [Appsettings()] ),
        "/useraccess":View("/useraccess", [useraccess()] ),
        "/homepage":View("/homepage", [ApplicationBody()] ),
        "/productpage":View("/productpage", [Productpage()] ),
        "/dashboardpage":View("/dashboardpage", [dashboardpage()] ),
        "/reportpage":View("/reportpage", [reportpage()] ),





    }
