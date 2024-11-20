from __future__ import unicode_literals

import locale
import time
from datetime import datetime
import urllib.request, urllib.parse, urllib.error

from kodi_six import xbmc, xbmcgui

DATE_FORMAT = "%Y-%m-%d %H:%M:00"


def log(x):
    xbmc.log(repr(x), xbmc.LOGERROR)


def escape(value):
    try:
        value = value.decode()
    except:
        pass
    try:
        value = value.encode()
    except:
        pass
    return urllib.parse.quote_plus(value)


def get_format():
    dateFormat = xbmc.getRegion('datelong').replace('%-','%')
    timeFormat = xbmc.getRegion('time').replace('%H%H', '%H').replace('%I%I', '%I')
    timeFormat = timeFormat.replace(":%S", "")
    return "{}, {}".format(dateFormat, timeFormat)


def extract_date(dateLabel, timeLabel):
    date = xbmc.getInfoLabel(dateLabel)
    #get localized mounth names, when kodi has wrong translation opposite to locale
    mounths_kodi=[]
    mounths_locale=[]
    for i in range(21,33):
        mounths_kodi.append(xbmc.getLocalizedString(i))
        
    for i in range(1,13):
        mounth_loc_name= datetime(1900, i, 1).strftime('%B')
        mounths_locale.append(mounth_loc_name)

    for i in range(0,12):
        date=date.replace(mounths_kodi[i],mounths_locale[i])
    log(date)

    timeString = xbmc.getInfoLabel(timeLabel)
    fullDate = "{}, {}".format(date, timeString)

    # https://bugs.python.org/issue27400
    try:
        parsedDate = datetime.strptime(fullDate, fullFormat)
    except TypeError:
        parsedDate = datetime(*(time.strptime(fullDate, fullFormat)[0:6]))
    
    return datetime.strftime(parsedDate, DATE_FORMAT)


def get_language():
    try:
        language = xbmc.getLanguage(xbmc.ISO_639_1, True)
        log("Language: " + language)
        languageParts = language.split("-")

        return "{}_{}.UTF-8".format(languageParts[0], languageParts[1])
    except:
        return ""


try:
    log("get_language: "+get_language())
    usedLocale = locale.setlocale(locale.LC_TIME, get_language())
except:
    usedLocale = locale.setlocale(locale.LC_TIME, "")
log("Used locale: " + usedLocale)

fullFormat = get_format()

channel = escape(xbmc.getInfoLabel("ListItem.ChannelName"))
title = escape(xbmc.getInfoLabel("ListItem.Label"))

try:
    start = extract_date("ListItem.StartDate", "ListItem.StartTime")
    stop = extract_date("ListItem.EndDate", "ListItem.EndTime")
    log(start)
    log(stop)
    try:
        cmd = "PlayMedia(plugin://plugin.video.iptv.recorder/record_epg/%s/%s/%s/%s)" % (channel,
                                                                                        title,
                                                                                        start,
                                                                                        stop)
        xbmc.executebuiltin(cmd)

        message = "{}: {} ({} to {})'".format(xbmc.getInfoLabel("ListItem.ChannelName"), xbmc.getInfoLabel("ListItem.Label"), start, stop)
        xbmcgui.Dialog().notification("IPTV Recorder - Scheduled record", message, xbmcgui.NOTIFICATION_INFO, 10000, sound=False)
    except:
        xbmcgui.Dialog().notification("IPTV Recorder", "Could not schedule recording", xbmcgui.NOTIFICATION_WARNING)
except Exception as e:
    xbmcgui.Dialog().notification("IPTV Recorder", "Error parsing dates", xbmcgui.NOTIFICATION_ERROR)
    log("IPTV Recorder: Error parsing dates ({})".format(e))
