from core.irc import Irc
from core.hooks import dispatch

class Bot(object): # don't inherit from Irc, keeps things flat :D
    '''Instantiates Irc, loops over `Irc.conn.iqueue` and sends data through 
       `dispatch()`. Pass True if using SSL/TLS.
    '''

    def __init__(self, server, nick, port=6667, ssl=False, channels=[]):
        self.channels = channels
        self.irc = Irc(server, nick, port, ssl)
        self._dispatch_events()

    def _dispatch_events(self):
        while True: # magic loop
            event = self.irc.events.get()
            dispatch(self, event)

