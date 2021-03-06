from ROOT import TFile, TH1D 

file_events = TFile("testdata/events.root")
tree_events = file_events.Get("events")
n_events = tree_events.GetEntries()
print "Num. events = " + str(n_events)

for i_event in xrange(n_events): #better than "when" so array size is not changing
    tree_events.GetEntry(i_event)
    n_particles = tree_events.nPart
    print "Number particles = " + str(n_particles)

h = TH1D("hist_m", "dimuon mass", 100, 0, 200)
h.Draw()
raw_input("Press return to exit.")
