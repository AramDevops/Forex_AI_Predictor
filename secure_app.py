"""
@author: Nasr Akram

"""
import API
import time
import apps
from PIL import Image
import streamlit as st
from hydralit import HydraApp
import hydralit_components as hc



#Only need to set these here as we are add controls outside of Hydralit, to customise a run Hydralit!
st.set_page_config(page_title='Forex Multitool',page_icon="🐙",layout='wide',initial_sidebar_state='auto',)



if __name__ == '__main__':

    #---ONLY HERE TO SHOW OPTIONS WITH HYDRALIT - NOT REQUIRED, use Hydralit constructor parameters.

    hydralit_navbar = 'Use Hydralit Navbar',True
    sticky_navbar = 'Use Sticky Navbar',True
    animate_navbar = 'Use Animated Navbar',True
    hide_st = 'Hide Streamlit Markers',True

    over_theme = {'txc_inactive': '#FFFFFF'}
    #this is the host application, we add children to it and that's it!
    app = HydraApp(
        title='Forex MultiTool',
        favicon="🐙",
        hide_streamlit_markers=hide_st,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        banner_spacing=[5,30,60,30,5],
        use_navbar=hydralit_navbar, 
        navbar_sticky=sticky_navbar,
        navbar_animation=animate_navbar,
        navbar_theme=over_theme
    )

    #Home button will be in the middle of the nav list now
    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)

    #add all your application classes here
    app.add_app("AI V1", icon="📚", app=apps.CheatApp(title="AI V1"))
    app.add_app("Future options 1...",icon="⌨", app=apps.WalshApp(title="Future options 1..."))
    app.add_app("Sequency (Secure)",icon="🔊🔒", app=apps.WalshAppSecure(title="Sequency (Secure)"))
    app.add_app("AI V2", icon="🛰️", app=apps.SolarMach(title="AI V2"))
    app.add_app("Future options 3...", icon="⌨", app=apps.SpacyNLP(title="Future options 3..."))
    app.add_app("Future options 2...", icon="⌨", app=apps.UberNYC(title="Future options 2..."))
    app.add_app("AI V2", icon="🛰️", app=apps.SolarMach(title="AI V2"))
    app.add_app("Forex Tools", icon="⏲️", app=apps.LoaderTestApp(title="Forex Tools"))
    app.add_app("Cookie Cutter", icon="🍪", app=apps.CookieCutterApp(title="Cookie Cutter"))

    #we have added a sign-up app to demonstrate the ability to run an unsecure app
    #only 1 unsecure app is allowed
    app.add_app("Signup", icon="🛰️", app=apps.SignUpApp(title='Signup'), is_unsecure=True)

    #we want to have secure access for this HydraApp, so we provide a login application
    #optional logout label, can be blank for something nicer!
    app.add_app("Login", apps.LoginApp(title='Login'),is_login=True)

    #specify a custom loading app for a custom transition between apps, this includes a nice custom spinner
    app.add_loader_app(apps.MyLoadingApp(delay=0))

    #we can inject a method to be called everytime a user logs out
    #---------------------------------------------------------------------
    # @app.logout_callback
    # def mylogout_cb():
    #     print('I was called from Hydralit at logout!')
    #---------------------------------------------------------------------

    #we can inject a method to be called everytime a user logs in
    #---------------------------------------------------------------------
    # @app.login_callback
    # def mylogin_cb():
    #     print('I was called from Hydralit at login!')
    #---------------------------------------------------------------------

    #if we want to auto login a guest but still have a secure app, we can assign a guest account and go straight in
    #app.enable_guest_access()

    #check user access level to determine what should be shown on the menu
    user_access_level, username = app.check_access()

    # If the menu is cluttered, just rearrange it into sections!
    # completely optional, but if you have too many entries, you can make it nicer by using accordian menus
    if user_access_level > 1:
        complex_nav = {
            'Home': ['Home'],
            'Forex Tools': ['Forex Tools'],
            'AI Predicter 🏆': ['AI V1',"AI V2"],
            'Future options 1... 🔥': ["Future options 1...","Sequency (Secure)"],
            'Future options 2...': ["Future options 2..."],
            'NLP': ["Future options 3..."],
            'Cookie Cutter': ['Cookie Cutter']
        }
    elif user_access_level == 1:
        complex_nav = {
            'Home': ['Home'],
            'Forex Tools': ['Forex Tools'],
            'AI Predicter 🔥': ['AI V1',"AI V2"],
            'Future options 1... 🔥': ["Future options 1..."],
            'Future options 2...': ["Future options 2..."],
            'NLP': ["Future options 3..."],
            'Cookie Cutter': ['Cookie Cutter']
        }
    else:
        complex_nav = {
            'Home': ['Home'],
        }


    #and finally just the entire app and all the children.
    app.run(complex_nav)


    #print user movements and current login details used by Hydralit
    #---------------------------------------------------------------------
    # user_access_level, username = app.check_access()
    # prev_app, curr_app = app.get_nav_transition()
    # print(prev_app,'- >', curr_app)
    # print(int(user_access_level),'- >', username)
    # print('Other Nav after: ',app.session_state.other_nav_app)
    #---------------------------------------------------------------------

