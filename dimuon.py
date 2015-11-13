from ROOT import TFile

f = TFile("testdata/events.root")
t = f.Get("events")
n = t.GetEntries()
print "Num. events = " + str(n)

for i in xrange(n): #better than "when" so array size is not changing
    t.GetEntry(i)
    n2 = t.nPart
    print "Number particles = " + str(n2)
