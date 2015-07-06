import socket

HOSTNAME = socket.gethostname().lower().split('.')[0].replace('-', '')

try:
    exec "from grocer.settings.host_%s import *" % HOSTNAME
except ImportError:
    pass

try:
    from grocer.settings.local import *
except ImportError:
    pass
