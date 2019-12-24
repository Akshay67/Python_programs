from datetime import datetime
import pip

try:
	import pyfiglet        
except ImportError:
	print('Need To install the package')
	pip.main(['install','pyfiglet'])

now = datetime.now()
current_time = now.strftime("%H:%M")
ascii_banner = pyfiglet.figlet_format(current_time)
print(ascii_banner)

