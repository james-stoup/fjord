#!/usr/bin/env python

import npyscreen


print('welcome to fjord')


#openvpn nl308.nordvpn.com.tcp.ovpn

### TO DO ###
#
#   Features
# 
#    - continuously running app in terminal
#    - shows connection status + stats
#    - shows what country you are really in
#    - shows what country the internet thinks you are in
#    - supports all of the options that the official app has
#    - allows you to save a configuration
#    - relies on openvpn
#    - shows map of world in ascii (if we are feeling frisky)
#    - tab complete country/city combos
#    - list explanation of what the damn options mean
#    - h key shows/hides help
#    - 

#  GUI
#
#    * should change colors based on if we are connected or not
#    * label showing projected location
#    * label showing real location
#    * show list of countries
#    * show cities per country
#    * show map of cities (maybe)
#    * offer to save configurations
#    * randomize connecting point
#    * maybe also show connection speed?

# for use with NordVPN Version 2.2.0-2


# during main loop we should just call 'nordvpn status' and change the background
# color of the main display to red or green depending on the status
# Status: Disconnected




# Primary class
class Fjord(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name='Fjord')


# This form class defines the display that will be presented to the user.
class MainForm(npyscreen.Form):
    def create(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        
        self.MyTitle = self.add(npyscreen.TitleText, name = "Welcome to Fjord", editable=False )
        self.ConnectionStatus = self.add(npyscreen.TitleText, name='Status:', value='Disconnected', editable=False, color='DANGER')

        self.nextrely += 1
        self.RealLoc = self.add(npyscreen.TitleText, name='Real Loc:', value='Home', editable=False)
        self.ProjLoc = self.add(npyscreen.TitleText, name='Proj Loc:', value='Home', editable=False)

        self.nextrely += 1
        self.MyColor = self.add(npyscreen.TitleText, name='Color', value='BLUE')
        self.MyName = self.add(npyscreen.TitleText, name='Name', value='Bob')
        
        
    def afterEditing(self):
        self.parentApp.setNextForm(None)

        
def main():
    """ Welcome to Fjord, a better way of using NordVPN """
    



        
if __name__ == '__main__':
    fjord = Fjord()
    fjord.run()
    
