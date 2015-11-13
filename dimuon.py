from ROOT import TFile

f = TFile("testdata/events.root")
t = f.Get("events")
n = t.GetEntries()
print "Num. events = " + str(n)
