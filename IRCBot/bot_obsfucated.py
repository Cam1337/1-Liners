import socket, sys, itertools

chan = "#test"
gr = "Hi :)"

irc = lambda h,p,b,s=socket.socket(),bot=lambda q,o=lambda s,t,d:[s.write("PRIVMSG {0} :{1}\r\n".format(t,d)),s.flush()],z=lambda s,d:[s.write("{0}\r\n".format(d)),s.flush()],start=lambda s,h,p,r,b:[s.connect((h,p)),r(s,"NICK "+b[0]),r(s,"USER {0} {1} *** : {2}\r\n".format(b[1],h,b[2]))],on_ping=lambda s,d,r,m:[r(s,"PONG {0}".format(d[1]))],on_001=lambda s,d,r,m:[r(s,"JOIN "+chan),m(s,chan,gr)],gfunc=lambda fcs,st:[fcs[i].get(st[i],None) for i in fcs.keys() if i<len(st)],ex=lambda st,q,gfs,gf,r,m: [sys.stdout.write(repr(st)+"\n"),[i(q,st,r,m) for i in gf(gfs,st) if i!=None]]:[[ex(q.readline().split(),q,{1:{"001":on_001},0:{"PING":on_ping}},gfunc,z,o) for i in itertools.cycle([0])]],:bot([s.connect((h,p)),s.send("NICK {3}\r\nUSER {0} {1} *** : .{2}\r\n".format(b[1],h,b[2],b[0])),s.makefile("r+w+b")][-1])
        

irc("ip",6667, ["TestBot","TestBotI","TestBotR"])