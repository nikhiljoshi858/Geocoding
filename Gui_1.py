# Name: Nikhil Joshi    Class: D7A      Roll no. 25
# Name: Sahil Rajpal    Class: D7A      Roll no. 50
# Name: Srivatsan Iyengar   Class: D7A  Roll no. 28
# Python mini Project: Contacting Google APIs (Geocoding) and Navigation
from tkinter import *
import tkinter.messagebox
import gmplot
import urllib.request, urllib.error, urllib.parse
import json
import ssl
def show_location():
    api_key = False
    # Since we don't have an API key we use a different
    # website to contact the Google APIs
    # If you have any valid Google API key then set api_key = True and enter the key as parameter

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    parms = dict()
    parms['address']=address.get()
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")
    headers = dict(uh.getheaders())

    try:
        js=json.loads(data)
    except:
        js = None

    if js is None or 'status' not in js or js['status'] != 'OK':
        print("==========Falied to retrieve==========")
        quit()

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    tkinter.messagebox.showinfo("Show", ("Latitude is :",lat,"\nLongitude is :",lng))
    gmap=gmplot.GoogleMapPlotter(lat,lng,17)
    gmap.coloricon = 'http://www.googlemapsmarkers.com/v1/%s/'
    gmap.marker(lat,lng,'blue')
    gmap.draw('geojson.html')
    location = js['results'][0]['formatted_address']

master = Tk()
master.title("Calculate latitude and longitude")
Label(master, text='Enter Location').grid(row=0)
address = Entry(master)
address.grid(row=0, column=1)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_location).grid(row=3, column=1, sticky=W, pady=4)
"""
display= StringVar()
label = Label( master, textvariable = display, relief=RAISED )
display.set(address)
label.grid()
"""
mainloop()