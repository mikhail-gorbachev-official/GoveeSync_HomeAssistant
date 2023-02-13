# GoveeSync
This code will allow you to use Govee internal UDP api to control your device as well as sync what is on the screen. <strong>You need to install the below libs before running</strong>:<br>
pip install wmi<br>
pip install pywin32

# Constants
Update the device IP of the device you want to control on line 21.

# Testing / Searching for devices
Download UDPReceiver.py and UDPSender.py
<ol>
<li>Start CMD prompt, navigate to the folder where you downloaded the above files. Then type: python UDPReceiver.py<br>This should start a UDP multicast listener on port 4002</li>
<li>Once the listener is started open another CMD prompt. Navigate to the folder, and type: python UDPSender.py<br>This should output any Govee devices found to the shell.</li>
</ol>

# Supported Commands

To turn the device on/off:<br>
GoveeInternalControl("On")<br>
GoveeInternalControl("Off")<br>
<br>
To set the brightness:<br>
GoveeInternalControl("BrightLevel",100) #1-100% expressed as an integer<br>
GoveeInternalControl("BrightLevel",50) #1-100% expressed as an integer<br>
GoveeInternalControl("BrightLevel",10) #1-100% expressed as an integer<br>
<br>
To change the color:<br>
GoveeInternalControl("Color",color=(0,255,0)) #Color expressed as a RGB tuple<br>
GoveeInternalControl("Color",color=(255,0,0)) #Color expressed as a RGB tuple<br>
<br>
To go into game mode where the screen will sync to the device:<br>
<strong>Do note: in this mode the code will attempt to lock onto the window that is in focus.<br><br>There is a box size constant you can mess around with if you want to and see if you get better results.<br><br>This mode essentially works by creating a square in the center of the app's window. We sample a pixel at each of the four corners of the square, get the color values, then average those 4 color values together. that averaged out value is then sent to the Govee lights over UDP api.</strong><br>
<br>
GameTime()


