import gevent

from core.irc import Irc

if __name__ == '__main__':

    bot = lambda : Irc('irc.voxinfinitus.net', 'Kaa_', 6697, True, ['#voxinfinitus','#landfill'], False)
    #another_bot = lambda : Irc('irc.freenode.net', 'Kaa_', 6667, False, ['#landfill'])
    
    jobs = [gevent.spawn(bot)]
    gevent.joinall(jobs)
