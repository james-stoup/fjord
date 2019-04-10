#!/usr/bin/env python

import logging
import random

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
#    - add favorite servers
#    - list of apps to kill if VPN drops

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
    Global_Connection_Status = 'Disconnected'
    
    def onStart(self):
        self.main_form = self.addForm("MAIN", MainForm, name='Fjord')
        self.con_form = self.addForm("CONNECTION_FORM", ConnectionForm, name='Connect/Disconnect')


# This form class defines the display that will be presented to the user.
#class MainForm(npyscreen.ActionForm, npyscreen.SplitForm, npyscreen.FormWithMenus):
class MainForm(npyscreen.ActionForm):
    def create(self):
        self.MyTitle = self.add(npyscreen.TitleText, name = "Welcome to Fjord", editable=False )
        self.ConnectionStatus = self.add(npyscreen.TitleText, name='Status:', value='Disconnected', editable=False, color='DANGER')

        self.nextrely += 1
        self.RealLoc = self.add(npyscreen.TitleText, name='Real Loc:', value='Home', editable=False)
        self.ProjLoc = self.add(npyscreen.TitleText, name='Proj Loc:', value='Home', editable=False)

        self.nextrely += 1
        self.nextrely += 1
        self.Settings = self.add(npyscreen.TitleText, name = 'Settings', editable=False)
        self.nextrely += 1

        # prevent editing once connected
        self.Country = self.add(npyscreen.TitleText, name='Country', value='France')
        self.City = self.add(npyscreen.TitleText, name='City', value='Paris')
        self.Protocol = self.add(npyscreen.TitleText, name = 'Protocol', value='UDP')

        self.Obfuscate = self.add(npyscreen.TitleText, name = 'Obfuscate', value='disabled')
        self.AutoConnect = self.add(npyscreen.TitleText, name = 'Auto Connect', value='disabled')
        self.DNS = self.add(npyscreen.TitleText, name = 'DNS', value='disabled')
        
        self.KillSwitch = self.add(npyscreen.TitleSelectOne, values=['Enabled', 'Disabled'], name = 'Kill Switch', max_height=3)

        self.nextrely += 1
        self.connectButton = self.add(npyscreen.Button, name='Connect', value_changed_callback=self.connectButtonPress)

        
    def connectButtonPress(self, widget):
        #npyscreen.notify_confirm('Button pressed!', title='Woot', wrap=True, wide=True, editw=1)

        logging.debug('CON STAT VAL: %s' % self.ConnectionStatus.value)

        # DEBUG - testing the limits
        # rand_num = random.randint(1,1001)
        # self.ConnectionStatus.set_value('CONNECTED - %s' % rand_num)

        if self.ConnectionStatus.value == 'Disconnected':
            self.ConnectionStatus.set_value('Connected')
        elif self.ConnectionStatus.value == 'Connected':
            self.ConnectionStatus.set_value('Disconnected')
             
        self.parentApp.switchForm('CONNECTION_FORM')
        
    def on_ok(self):
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.parentApp.setNextForm(None)

# END CLASS


# Go ahead and return to the main screen
class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        val = self.parent.parentApp.main_form.ConnectionStatus.value
        logging.debug('CONNECTION STATUS: %s' % val)

        # change the connection status
        # if self.parent.parentApp.main_form.ConnectionStatus.value == 'Connected':
        #     self.parent.parentApp.main_form.ConnectionStatus.set_value('Disconnected')
        #     logging.debug('  C -> D')

        # if self.parent.parentApp.main_form.ConnectionStatus.value == 'Disconnected':
        #     self.parent.parentApp.main_form.ConnectionStatus.set_value('Connected')
        #     logging.debug('  D -> C')

        # self.parent.parentApp.main_form.DISPLAY()
        self.parent.parentApp.switchForm('MAIN')

        
#class ConnectionForm(npyscreen.ActionForm, npyscreen.SplitForm, npyscreen.FormWithMenus):        
class ConnectionForm(npyscreen.FormBaseNew):
    """ The form used to display the connect/disconnct output """
    def create(self):
        logging.debug('connection form created')
        self.parentApp.setNextForm('MAIN')
        self.name = self.add(npyscreen.TitleText, name='Connecting To VPN', editable=False)

        # I can't make the exit button hidden because then it will explode, so I need to come
        # up with some way to force the user to view all the output before they return to main.
        self.exitButton = self.add(ExitButton, name="Exit", relx=-15, rely=-5, hidden=False)

        # change the connection status
        # if self.parentApp.main_form.ConnectionStatus.value == 'Connected':
        #     self.parentApp.main_form.ConnectionStatus.value = 'Disconnected'

        # if self.parentApp.main_form.ConnectionStatus.value == 'Disconnected':
        #     self.parentApp.main_form.ConnectionStatus.value = 'Connected'
            
    # def output_status(self):
    #     # print the output from nordvpn to here

    #     # once done, go ahead and enable the exit button
    #     self.exitButton.hidden=False

#class ConnectionForm(npyscreen.ActionForm, npyscreen.SplitForm, npyscreen.FormWithMenus):        
    # def on_ok(self):
    #     npyscreen.notify_confirm("Saved! Going back to main form", title="OK Pressed", wrap=True, wide=True, editw=1)
    #     self.parentApp.setNextForm('MAIN')

    # def on_cancel(self):
    #     npyscreen.notify_confirm("NOT Saved, going back to main form", title="OK Pressed", wrap=True, wide=True, editw=1)
    #     self.parentApp.setNextForm('MAIN') # Back to main form
# END CLASS


        
def main():
    """ Welcome to Fjord, a better way of using NordVPN """

    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    
    fjord = Fjord()
    fjord.run()
    



        
if __name__ == '__main__':
    main()
    # npyscreen.wrapper(Fjord().run())
