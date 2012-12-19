import socket, sys, itertools

class Infinite(object):
    def __init__(self):
        self.t = [1,2,3,4]
    def __iter__(self):
        for i in self.t:
            self.t.append(5)
            yield i


z = Infinite()
a = lambda t: t + [0]
for i in a([1]):
    print i
def p(s):
    print s

#print [[i,a(t)] for i in t]
 

irc = lambda h,p,b,s=socket.socket(),\
    bot=lambda\
        sock,\
        msg=lambda s,t,d:[s.write("PRIVMSG {0} :{1}\r\n".format(t,d)),s.flush()],\
        raw=lambda s,d:[s.write("{0}\r\n".format(d)),s.flush()],\
        start=lambda s,h,p,r,b:[s.connect((h,p)),r(s,"NICK "+b[0]),r(s,"USER {0} {1} *** : {2}\r\n".format(b[1],h,b[2]))],\
        on_ping=lambda s,d,r,m: [r(s,"PONG {0}".format(d[1]))],\
        on_001=lambda s,d,r,m: [r(s,"JOIN #test"),m(s,"#test","Hi from TESTBOT")],\
        on_say=lambda s,d,r,m: [m(s,"#test"," ".join(d[4:]))],\
        gfunc=lambda fcs,st:[fcs[i].get(st[i],None) for i in fcs.keys() if i < len(st)],\
        ex=lambda st,sock,gfs,gf,r,m: [sys.stdout.write(repr(st)+"\n"),[i(sock,st,r,m) for i in gf(gfs,st) if i != None]],\
        :[[ex(sock.readline().split(),sock,{1:{"001":on_001},0:{"PING":on_ping},3:{":!echo":on_say}},gfunc,raw,msg) for i in itertools.cycle([0])]],\
    :bot([s.connect((h,p)),s.send("NICK {3}\r\nUSER {0} {1} *** : .{2}\r\n".format(b[1],h,b[2],b[0])),s.makefile("r+w+b")][-1])
        


irc("199.48.69.234",6667, ["TestBot","TestBotI","TestBotR"])