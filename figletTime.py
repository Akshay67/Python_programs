from datetime import datetime
import pyfiglet

now = datetime.now()
current_time = now.strftime("%H:%M")
ascii_banner = pyfiglet.figlet_format(current_time)
print(ascii_banner)

