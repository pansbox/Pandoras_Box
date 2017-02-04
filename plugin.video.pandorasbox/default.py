# -*- coding: cp1252 -*-

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import urlparse
import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs,traceback,cookielib,urlparse,httplib,time
import urlresolver
import time
import cloudflare,client,googleplus,cleantitle

Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
CAT=Decode('LnBocA==')
Base_Pand = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv'))
addon_id='plugin.video.pandorasbox'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Pandoras Box"
VERSION = "1.0.1"
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.pandorasbox/')
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/Pandora\'sBox/'
if not os.path.exists(ADDON_DATA):
    os.makedirs(ADDON_DATA)
watched = ADDON_DATA + 'watched.txt'
if not os.path.exists(watched):
    open(watched,'w+')
favourites = ADDON_DATA + 'favourites.txt'
watched_read = open(watched).read()
if not os.path.exists(favourites):
    open(favourites,'w+')
favourites_read = open(favourites).read()
IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'

ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))



def Home_Menu():
    
    addDirPand2('[COLOR darkgoldenrod][I]Open Pandora\'s Box[/I][/COLOR]','',400,'https://s32.postimg.org/ov9s6ipf9/icon.png',ART + 'fanart.jpg','','')
    addDirPand2('[COLOR darkgoldenrod][I]Search[/I][/COLOR]','',1,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png',ART + 'fanart.jpg','','')
    addDirPand2('[COLOR darkgoldenrod][I]Favourites[/I][/COLOR]','',12,'http://icons.iconarchive.com/icons/colorflow/colorflow_1/256/32-Favorites-icon.png',ART + 'fanart.jpg','','')

    xbmcplugin.setContent(addon_handle, 'movies')
		
def Search_Menu():
	addDirPand2('[COLOR darkgoldenrod][I]Search Pandoras Films[/I][/COLOR]','',424,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png',ART + 'fanart.jpg','','')
	addDirPand2('[COLOR darkgoldenrod][I]Search Pandoras TV[/I][/COLOR]','',425,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png',ART + 'fanart.jpg','','')

        xbmcplugin.setContent(addon_handle, 'movies')

	
def Pandoras_Box():

    html=OPEN_URL(Base_Pand +Decode('c3BvbmdlbWFpbi5waHA='))
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart,mode in match:
            addDirPand2(name,url,mode,img,fanart,desc,'')

    xbmcplugin.setContent(addon_handle, 'movies')
			
			
def Pandora_Menu(url):
        
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,desc,background,name in match:
            Watched = re.compile('url="(.+?)"\n').findall(str(watched_read))
            for item in Watched:
                if item == url:
                    name =('[COLORblue]*[/COLOR]'+name).replace('[COLORblue]*[/COLOR][COLORblue]*[/COLOR]','[COLORred]*[/COLOR]')
            if not 'http' in url:
                if 'list' in url:
                    addDirPand2(name,url,13,iconimage,background,desc,'')
                else:
                    url = 'plugin://plugin.video.youtube/play/?video_id='+ url
                    addDirPand(name,url,401,iconimage,background,desc,'')
            else:
                addDirPand(name,url,401,iconimage,background,desc,'')
            xbmcplugin.setContent(addon_handle, 'movies')			
            xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def Youtube_Playlist(url):			
    url = 'https://www.youtube.com/playlist?'+url
    xbmc.log('###################################'+url)
    HTML = OPEN_URL(url)
    block_set = re.compile('<tr class="pl-video yt-uix-tile(.+?)</tr>',re.DOTALL).findall(HTML)
    for block in block_set:
        image = re.compile('data-thumb="(.+?)"').findall(str(block))
        for image in image:
            image = image
        name = re.compile('data-title="(.+?)"').findall(str(block))
        for name in name:
        	name = (name).replace('&quot;','').replace('&#39;','\'').replace('&amp;','&')
        duration = re.compile('<div class="timestamp"><span aria-label=".+?">(.+?)</span>').findall(str(block))
        for duration in duration:
            duration = duration
        url = re.compile('data-video-ids="(.+?)"').findall(str(block))
        for url in url:
            url = url
        if 'elete' in name:
            pass
        elif 'rivate vid' in name:
            pass
        else:
            addDirPand('[COLORred]'+str(duration)+'[/COLOR] : '+str(name),'plugin://plugin.video.youtube/play/?video_id='+str(url),401,str(image),'','','' )

                    
			
def Search_Pandoras_Films():
    
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) # what you type in
    Search_Title = Search_Name.lower()
    filenames = ['hey1080p','hey3D','hey','480p','720p','1080p','mova', 'movb', 'movc', 'movd', 'move', 'movf', 'movg', 'movh', 'movi', 'movj', 'movk', 'movl', 'movm', 'movn', 'movo', 'movp', 'movq', 'movr', 'movs', 'movt', 'movu', 'movv', 'movw', 'movx', 'movy', 'movz','720paction','720padventure','720panimation','720pcomedy','720pcrime','720pdocumentary','720pdrama','720pfamily','720pfantasy','720phorror','720pmystery','720promance','720psci-Fi','720psport','720pthriller','720pwestern','1080paction','1080padventure','1080panimation','1080pcomedy','1080pcrime','1080pdocumentary','1080pdrama','1080pfamily','1080pfantasy','1080phorror','1080pmystery','1080promance','1080psci-Fi','1080psport','1080pthriller','1080pwestern','top10action','top10animation','top10biography','top10comedy','top10crime','top10documentary','top10drama','top10family','top10fantasy','top10horror','top10music','top10mystery','top10romance','top10sci-fi','top10sport','top10thriller','top10western']
    for file_Name in filenames:
        search_URL = Base_Pand + file_Name + CAT
        HTML = OPEN_URL(search_URL)
        if HTML != 'Opened':
            match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML)
            for url,iconimage,desc,fanart,name in match:
                if Search_Name in name.lower():
                    Watched = re.compile('url="(.+?)"\n').findall(str(watched_read))
                    for item in Watched:
                        if item == url:
                            name = '[COLORblue]*[/COLOR]'+name
                    if not 'http' in url:
                        if 'list' in url:
                            addDirPand2(name,url,13,iconimage,background,desc,'')
                        else:
                            url = 'plugin://plugin.video.youtube/play/?video_id='+ url
                            addDirPand(name,url,401,iconimage,background,desc,'')
                    else:
                        addDirPand(name,url,401,iconimage,background,desc,'')
                    xbmcplugin.setContent(addon_handle, 'movies')
                    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
				
				
def Search_Pandoras_TV():
    
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) # what you type in
    Search_Title = Search_Name.lower()
    filenames = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for file_Name in filenames:
        search_URL2 = Base_Pand + file_Name + CAT
        HTML = OPEN_URL(search_URL2)
        if HTML != 'Opened':
            match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(HTML)
            for name,desc,url,img,fanart,mode in match:
                if Search_Name in name.lower():
                    Watched = re.compile('url="(.+?)"\n').findall(str(watched_read))
                    for item in Watched:
                        if item == url:
                            name =('[COLORblue]*[/COLOR]'+name).replace('[COLORblue]*[/COLOR][COLORblue]*[/COLOR]','[COLORred]*[/COLOR]')
                    if not 'http' in url:
                        if 'list' in url:
                            addDirPand2(name,url,13,iconimage,background,desc,'')
                        else:
                            url = 'plugin://plugin.video.youtube/play/?video_id='+ url
                            addDirPand(name,url,401,iconimage,background,desc,'')
                    else:
                        addDirPand2(name,url,mode,img,fanart,desc,'')
					
                    xbmcplugin.setContent(addon_handle, 'movies')
                    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

			
def open_Menu(url):

    html=OPEN_URL(url)
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart,mode in match:
        Watched = re.compile('url="(.+?)"\n').findall(str(watched_read))
        for item in Watched:
            if item == url:
                name =('[COLORblue]*[/COLOR]'+name).replace('[COLORblue]*[/COLOR][COLORblue]*[/COLOR]','[COLORred]*[/COLOR]')
        addDirPand2(name,url,mode,img,fanart,desc,'')

        xbmcplugin.setContent(addon_handle, 'movies')
        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def Write_Favourite(name,url,mode,iconimage,fanart,description):
    print_text_file = open(favourites,"a")
    print_text_file.write('url="'+str(url)+'">name="'+str(name)+'"'+'>mode="'+str(mode)+'">image="'+str(iconimage)+'">fanart="'+str(fanart)+'">description="'+str(description)+'"<END>\n')
    print_text_file.close

def Read_Favourite():
    Fav = open(favourites).read()
    Fav_Regex = re.compile('url="(.+?)">name="(.+?)">mode="(.+?)">image="(.+?)">fanart="(.+?)">description="(.+?)"<END>').findall(Fav)
    for url,name,mode,image,fanart,description in Fav_Regex:
        if not mode == '401':
            addDirPand2(name,url,mode,image,fanart,description,name,'')
            setView('Movies', 'INFO')
        elif mode == '401':
            addDirPand(name,url,mode,image,fanart,description,name,'')
            setView('Movies', 'INFO')
    if len(Fav_Regex)<=0:
        addDirPand2('[COLORblue][B]You need to add favourites first[B][/COLOR]','','','','','','')			
			
def addDirPand(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
        fav_mode = mode
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from Pandora\'s Favorites','XBMC.RunPlugin(%s?mode=10056&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in favourites_read:
                contextMenu.append(('Add to Pandora\'s Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDirPand2(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
        fav_mode = mode
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from Pandora\'s Favorites','XBMC.RunPlugin(%s?mode=10056&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in favourites_read:
                contextMenu.append(('Add to Pandora\'s Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
		
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2: 
                params=sys.argv[2] 
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}    
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
params=get_params()
url=None
name=None
iconimage=None
mode=None
description=None
extra=None
fav_mode=None

try:
    fav_mode=int(params["fav_mode"])
except:
    pass
	
try:
    extra=urllib.unquote_plus(params["extra"])
except:
    pass

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)

def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 
 
def Resolve_Dizi(url):
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass



def Resolve(url): 
    print_text_file = open(watched,"a")
    print_text_file.write('url="'+url+'"\n')
    print_text_file.close
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('LOADING','Opening %s Now'%(name))
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve() 
    if dp.iscanceled(): 
        print "[COLORblue]STREAM CANCELLED[/COLOR]" # need to get this part working    
        dialog = xbmcgui.Dialog()
        if dialog.yesno("[B]CANCELLED[/B]", '[B]Was There A Problem[/B]','', "",'Yes','No'):
            dialog.ok("Message Send", "Your Message Has Been Sent")
        else:
	         return
    else:
        try: play.play(url)
        except: pass
        try: ADDON.resolve_url(url) 
        except: pass 
        dp.close()

def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = ''
    link = ''
    try: 
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    except: pass
    if link != '':
        return link
    else:
        link = 'Opened'
        return link

def setView(content, viewType):
	if content:
	    xbmcplugin.setContent(int(sys.argv[1]), content)


if mode == None     : Home_Menu()
elif mode == 1 		: Search_Menu()
elif mode == 10 	: Resolve_Dizi(url)
elif mode == 11		: Write_Favourite(name,url,fav_mode,iconimage,fanart,description)
elif mode == 12 	: Read_Favourite()
elif mode == 13 	: Youtube_Playlist(url)
elif mode == 400 	: Pandoras_Box()
elif mode == 401    : Resolve(url)
elif mode == 423 	: open_Menu(url)
elif mode == 424 	: Search_Pandoras_Films()
elif mode == 425 	: Search_Pandoras_TV()
elif mode == 426 	: Pandora_Menu(url)
elif mode == 427 	: addDirPand(name,url,mode,iconimage,fanart,description,extra)

xbmcplugin.endOfDirectory(int(sys.argv[1]))