# bing_wall
An application that sets the current bing wallpaper to your desktop wallpaper.

## instructions 
* clone this repo in your desktop.
* edit 'app.py' and do the following changes.

```python3
os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/username/path_to_project/bing-wall/img.jpg")
```
* replace 'username' with your username.( to know your username simply type 'whoami' in your terminal and it will give your username)
* and change 'path_to_project' to the location where you'll clone the repo.
* make sure to install all the modules mentioned in 'requirements.txt'.
* also make sure that you have a working internet conncectivity. 
* Run 'app.py'

