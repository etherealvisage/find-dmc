#!/usr/bin/env python

import sys

lines = open("dmc.csv").readlines()

print("Finding close matches for colour", sys.argv[1])

mr = int(sys.argv[1][0:2], 16)
mg = int(sys.argv[1][2:4], 16)
mb = int(sys.argv[1][4:6], 16)

results = []
for line in lines:
    cols = line.split(",")
    r = int(cols[2][1:3], 16)
    g = int(cols[2][3:5], 16)
    b = int(cols[2][5:7], 16)

    dr = (mr - r)
    dg = (mg - g)
    db = (mb - b)

    distance = (dr**2 + dg**2 + db**2)**0.5
    results.append((distance, cols))

results.sort()
print("Top 10 recommendations:")
for r in results[0:10]:
    print("\t" + r[1][0] + " (\"" + r[1][1] + "\")")
