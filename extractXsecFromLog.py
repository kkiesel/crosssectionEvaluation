#!/usr/bin/env python2

import glob
import tarfile
import collections

path = "done/crab_*/results/cmsRun_*.log.tar.gz*"

out = {}
for fname in glob.glob(path):
    dSet = fname.split("/")[-3][5:]
    f = tarfile.open(fname)
    for member in f.getmembers():
        if "stdout" not in member.name: continue
        m = f.extractfile(member)
        selLines = [ l for l in m.readlines() if l.startswith("After filter: final cross section")]
        if not len(selLines): continue
        line = selLines[0]
        vals = line.split(" = ")[1].split()
        if dSet not in out: out[dSet] = []
        out[dSet].append( (vals[0], vals[2]) )


print "# dataset    cross section (pb)    uncertainty (pb)"
sortedOut = collections.OrderedDict(sorted(out.items(), key=lambda t:t[0]))
for k,v in sortedOut.iteritems():
    for x in v:
        print "{:<60}".format(k), float(x[0]), float(x[1])
