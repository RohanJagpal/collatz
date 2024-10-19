import sys
import model
import csv
from statistics import stdev

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

try:
    start = int(args[0])
    end = int(args[1])
    incr = int(args[2])
except ValueError:
    raise SystemExit(f"Provide a positive integer")
finally:
    if len(args) != 3:
        raise SystemExit(f"Provide min, max and increment")

n = []
trials = []

for i in range(start, end+1):
    sequencer = model.Collatz(i)
    result = sequencer.sequence()
    n.append(result[0])
    trials.append(result[1])

maxs = []
stdevs = []

for i in range(1,len(trials)//incr):
    stdevs.append(i*incr)
    stdevs.append(stdev(trials[start:i*incr]))

with open('stdevs.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['max', 'stdevs'])
    for i in range(len(maxs)):
        writer.writerow([n[maxs],stdevs[i]])