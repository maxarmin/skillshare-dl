'''
setup.py
for skillshare-dl
'''
import os
import shutil
try:
	user_id = os.geteuid()

except AttributeError:
	# Running Windows...
	"This script does not support Windows at the moment, sorry. Exiting..."
	exit()

if user_id != 0:
	print("This script needs to be run as root! Exiting...")
	exit()

print("------------skillshare-dl setup/installer------------")
print("This script is going to install all the neccessary dependencies",
"and tools needed to run skillshare-dl. Keep in mind: ",
"This tool has only been tested on Linux using Chrome 77(at the time of writing)",
", so if you want to ensure that the script is working properly just set up a VM ",
"with Ubuntu and Chrome.\n")
choice = input("Are you sure you want to proceed? [y/Y/n/N]: ").lower().strip()
if choice != 'y':
	print("Exiting...")
	exit()

linux_flag = 0
mac_flag = 0
windows_flag = 0

linux_flag = input("Are you using Linux? [y/Y/n/N]: ").lower().strip()
if linux_flag == 'y':
	linux_flag = 1
else:
	linux_flag = 0
	mac_flag = input("Are you using macOS? [y/Y/n/N]: ").lower().strip()
	if mac_flag == 'y':
		mac_flag = 1
	else:
		mac_flag = 0
		windows_flag = input("Are you using Windows? [y/Y/n/N]: ").lower().strip()
		if windows_flag == 'y':
			windows_flag = 1
			print("Not yet supported, sorry.")
			exit()
		else:
			windows_flag = 0


#print("\nLinux: {}\nmacOS: {}\nWindows: {}\n".format(linux_flag, mac_flag, windows_flag))

if linux_flag == 1:
	print("The following tools are needed:")
	print("- Chrome/Chromium\n- Python 3 (preferably 3.7)\n- Selenium")
	print("- browsermob-proxy\n- Chrome WebDriver\n- pip/pip3")

	chrome_installed_flag = input("Is Chrome or Chromium installed and running the latest version? [y/Y/n/N]: ").lower().strip()
	if chrome_installed_flag == 'n':
		print("Installing Chrome now...")
		os.system('wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - ')
		os.system('sudo echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list')
		os.system('sudo apt-get update')
		os.system('sudo apt-get install google-chrome-stable')
	else:
		print("Chrome already installed, skipping!")

	print("Installing Python 3...")
	os.system("apt-get install python3")

	print("Installing Selenium...")
	os.system('python3 -m pip install selenium')

	print("Installing browsermob-proxy...")
	os.system("python3 -m pip install browsermob-proxy")

	print("Downloading the browsermob-proxy binary...")
	os.system("mkdir /usr/local/bin/skillshare-dl/")
	os.system("wget https://github.com/lightbody/browsermob-proxy/releases/download/browsermob-proxy-2.1.4/browsermob-proxy-2.1.4-bin.zip")
	print("Moving it to /usr/local/bin/skillshare-dl/ ...")
	os.system("unzip browsermob-proxy-2.1.4-bin.zip")
	os.system("cp browsermob-proxy-2.1.4/bin/browsermob-proxy /usr/local/bin/skillshare-dl/")

	print("Downloading the ChromeDriver for Chrome 77...")
	os.system("wget https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_linux64.zip")
	os.system("unzip chromedriver_linux64.zip")
	print("Moving it to /usr/bin/ ...")
	os.system("cp chromedriver /usr/bin/")

	os.remove("chromedriver")
	os.remove("chromedriver_linux64.zip")
	os.remove("browsermob-proxy-2.1.4-bin.zip")
	shutil.rmtree("browsermob-proxy-2.1.4")
'''
Mac:
install brew by running:
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew install wget

wget https://dl.google.com/mac/stable/GGRO/googlechrome.dmg
open ~/Downloads/googlechrome.dmg
wait until the image has been opened
sudo cp -r /Volumes/Google\ Chrome/Google\ Chrome.app /Applications/
'''