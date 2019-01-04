import dbus
import dbus.mainloop.glib
import glib
SONG_FILE = "PATH"

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

session_bus = dbus.SessionBus()
spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")

spotify_properties = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")

cursong = None
artist = None

def Handler(sender,b,c):
    global cursong,artist
    if 'xesam:title' in b["Metadata"]:
        song = b["Metadata"]["xesam:title"]
        if song != cursong:
            cursong = song
            artistUpdated = False
            if 'xesam:artist' in b["Metadata"]:
                artistUpdated = True
                artist = ", ".join(b["Metadata"]["xesam:artist"])
                print("Playing {} by {}".format(cursong, artist))
            with open(SONG_FILE, "w") as file:
                if artistUpdated:
                    file.write("{} - {}".format(artist, cursong))
                else:
                    file.write("{}".format(cursong))
                file.close()

spotify_properties.connect_to_signal("PropertiesChanged", Handler)

mainloop = glib.MainLoop()
mainloop.run()
