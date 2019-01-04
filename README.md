# spotireader
A python script, that monitors the dbus of Spotify and writes currently playing songs to a file, mainly for streaming purposes
<br>
"Spotireader" hooks to the DBus-Signal <i>PropertiesChanged</i> of <code>org.freedesktop.DBus.Properties</code> to monitor changes of
<code>org.mpris.MediaPlayer2.spotify</code> and writes song name and artist to a file
<br>
<h2><b>Dependencies</b></h2>
"Spotireader" depends on:
<ul>
<li>dbus</li>
<li>glib</li>
</ul>
Make sure you have these installed<br>

<br><b>For Archusers:</b><br>
<code>sudo pacman -S dbus glib2</code>
<br>
We also need some dependencies from [AUR](https://aur.archlinux.org) so go on and use your favorite AUR package manager (in my case <i>yay</i>)<br>
<code>yay -S python-dbus python-dbus-common python-gobject python-gobject2</code>
<br>that should be all
<br><br>

<h2><b>Setup</b></h2>
Pretty simple, download the spotireader.py, edit<br>
<code>SONG_FILE = "PATH"</code><br>
and set <b><i>PATH</i></b> to whatever file you want (<b>file</b> not directory).<br>
And youre ready to go, hookup Spotify and execute <i>spotireader.py</i>

<br>

<h2><b>User Extensions</b></h2>
If you have experience with Python or would like to play around, here is a JSON Representation of the <code>b</code> Parameter <sub><sup>(Dictionary)</sup></sub> 
of the <code>Handler</code> function:
<pre><code>{"Metadata": 
  {
  "mpris:trackid": "spotify:track:48Q3snZ8muPxDrZooxj3jB", 
  "mpris:length": 182000000, 
  "mpris:artUrl": "https://open.spotify.com/image/fd7d53574408812ff207362180d4c9b7e7c8eab0", 
  "xesam:album": "Inspiration", 
  "xesam:albumArtist": ["Unknown Brain"], 
  "xesam:artist": ["Unknown Brain"], 
  "xesam:autoRating": 0.58, 
  "xesam:discNumber": 1, 
  "xesam:title": "Inspiration", 
  "xesam:trackNumber": 1, 
  "xesam:url": 
  "https://open.spotify.com/track/48Q3snZ8muPxDrZooxj3jB"}, 
  "PlaybackStatus": "Playing"
  }
}
</code></pre>

<h2>Troubeshooting</h2><br>
Should you encounter any problems, feel free to open a new issue<br> i will do my best to help you resolve your problem
