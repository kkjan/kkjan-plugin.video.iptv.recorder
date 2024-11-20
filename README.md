# IPTV Recorder
## plugin.video.iptv.recorder

Kodi addon for recording streams from the IPTV Simple Client pvr plugin or xmltv/m3u files.

Adding recording from the IPTV Simple Client is possible and has been done but it is too hard for most people to build for their devices.

This addon is an easily extensible python addon that should work with any device.

You will need a version of ffmpeg for your device. 

https://ffmpeg.org/

Android builds are here: https://github.com/WritingMinds/ffmpeg-android/releases/latest

On Android this addon will copy ffmpeg to the /data/data folder so it can run. (Not work on Adroid 10 and latest)

This addon support Windows scheduller (on Windows system), cron (on linux system) , "Cron For Kodi addon" (must be installed https://kodi.tv/addons/nexus/service.cronxbmc/) and internal kodi system for starting recording.

This addon is primary tested on RPi4 and libreelec.

### Quick Start

* Install this addon via my repo. 
[https://github.com/kkjan/kkjan-kodi-repo/blob/main/kkjan.kkjanius.sk/kkjan.kkjanius.sk-0.2.0.zip](https://github.com/kkjan/kkjan-kodi-repo/blob/main/kkjan.kkjanius.sk/kkjan.kkjanius.sk-0.2.0.zip)
* Download ffmpeg for your device
* Point to the ffmpeg exe in Settings.
* Select folder for recording.
* Make sure IPTV Simple Client is enabled and works or point to your xmltv/m3u in Settings\Data.
* Go into the addon \ Channel Groups and find a program to Record.

