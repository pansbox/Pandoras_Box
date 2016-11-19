import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Pans Wizard'
EXCLUDES       = [ADDON_ID, 'repository.Pans Wizard' 'plugin.video.GenieTv' 'repository.GenieTv']
# Text File with build info in it.
BUILDFILE      = 'http://genietvcunts.co.uk/PansBox/wiz/Text/Builds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://genietvcunts.co.uk/PansBox/wiz/Text/apkfile.txt'

# Dont need to edit just here for icons stored locally
HOME           = xbmc.translatePath('special://home/')
PLUGIN         = os.path.join(HOME,     'addons',    ADDON_ID)
ART            = os.path.join(PLUGIN,   'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONMAINT      = 'http://genietvcunts.co.uk/PansBox/wiz/art/test.png'
ICONBUILDS     = 'http://genietvcunts.co.uk/PansBox/wiz/art/test.png'
ICONCONTACT    = 'http://genietvcunts.co.uk/PansBox/wiz/art/test.png'
ICONSAVE       = 'http://genietvcunts.co.uk/PansBox/wiz/art/test.png'
ICONTRAKT      = 'http://genietvcunts.co.uk/PansBox/wiz/art/test.png'
ICONREAL       = 'http://genietvcunts.co.uk/PansBox/wiz/art/test.png'
ICONLOGIN      = 'http://genietvcunts.co.uk/PansBox/wiz/art/test.png'
ICONAPK        = 'http://genietvcunts.co.uk/PansBox/wiz/art/test.png'
ICONSETTINGS   = 'http://genietvcunts.co.uk/PansBox/wiz/art/test.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'                                                                    

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'gold'
COLOR2         = 'silver'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][[COLOR '+COLOR2+']Pans Wizard[/COLOR]][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'    
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'                                          
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'                                          
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]' 
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]' 

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'                                                                    
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Pans Wizard.\nContact us at http://Pans Wizardmediapro.com'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'                                                                    
# Url to wizard version
WIZARDFILE     = 'http://genietvcunts.co.uk/PansBox/wiz/Text/Builds.txt'                          
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'                                                                    
# Addon ID for the repository
REPOID         = 'repository.aftermathwizard'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'http://Pans Wizardmediapro.com/files/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'http://Pans Wizardmediapro.com/'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://genietvcunts.co.uk/PansBox/wiz/Text/notification.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font14'
HEADERMESSAGE  = 'Pans Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = 'Font13'
# Background for Notification Window
BACKGROUND     = 'http://genietvcunts.co.uk/PansBox/wiz/art/test.png'
#########################################################