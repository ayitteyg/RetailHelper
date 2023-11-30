import flet
from flet import *
from retail_view import views_handler
from dbtable import Database



def main(page:Page):
    page.spacing=0
    #page.window_title_bar_hidden = True
    page.window_frameless = True
    page.window_title_bar_buttons_hidden = True
    page.bgcolor = colors.TRANSPARENT
    page.window_bgcolor = colors.TRANSPARENT
    page.padding = 5
    page.auto_scroll = True
    page.window_min_width = 1380
    page.window_progress_bar = 0.1

    
    
    Database().createTables()
    #Database().set_default_business_profile()
    #Database().set_app_default_user()

    page.fonts = {
    "SF Pro Bold":"fonts/SFProText-Bold.ttf",
    "SF Pro Heavy":"fonts/SFProText-Heavy.ttf",
    "SF Pro HeavyItalic":"fonts/SFProText-HeavyItalic.ttf",
    "SF Pro Light":"fonts/SFProText-Light.ttf",
    "SF Pro Medium":"fonts/SFProText-Medium.ttf",
    "SF Pro Regular":"fonts/SFProText-Regular.ttf",
    "SF Pro Semibold":"fonts/SFProText-Semibold.ttf",
    "SF Pro SemiboldItalic":"fonts/SFProText-SemiboldItalic.ttf",
    
    
    "Poppins ThinItalic":"fonts/poppins/Poppins-ThinItalic.ttf",
    "Poppins Thin":"fonts/poppins/Poppins-Thin.ttf",
    "Poppins Semibold":"fonts/poppins/Poppins-Semibold.ttf",
    "Poppins SemiboldItalic":"fonts/poppins/Poppins-SemiboldItalic.ttf",
    "Poppins Regular":"fonts/poppins/Poppins-Regular.ttf",
    "Poppins MediumItalic":"fonts/poppins/Poppins-MediumItalic.ttf",
    "Poppins Medium":"fonts/poppins/Poppins-Medium.ttf",
    "Poppins LightItalic":"fonts/poppins/Poppins-LightItalic.ttf",
    "Poppins Light":"fonts/poppins/Poppins-Light.ttf",
    "Poppins Italic":"fonts/poppins/Poppins-Italic.ttf",
    "Poppins ExtraLightItalic":"fonts/poppins/Poppins-ExtraLightItalic.ttf",
    "Poppins ExtraLight":"fonts/poppins/Poppins-ExtraLight.ttf",
    "Poppins ExtraBold":"fonts/poppins/Poppins-ExtraBold.ttf",
    "Poppins ExtraBoldItalic":"fonts/poppins/Poppins-ExtraBoldItalic.ttf",
    "Poppins BoldItalic":"fonts/poppins/Poppins-BoldItalic.ttf",
    "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf",
    "Poppins BlackItalic":"fonts/poppins/Poppins-BlackItalic.ttf",
    "Poppins Black":"fonts/poppins/Poppins-Black.ttf",
  }

    def route_change(route):
        #print(page.route)
        #clear current page and append new url
        page.views.clear
        page.views.append(
            views_handler(page)[page.route]
        )
        pass


    page.on_route_change = route_change
    page.go("/login")
    page.update()

    print(page.views[0].controls)
flet.app(target=main, assets_dir="assets")
#flet.app(main, view=AppView.WEB_BROWSER, assets_dir="assets")