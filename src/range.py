import sys
import model
import numpy as np
import csv

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

"""if "-c" in opts:
    print(" ".join(arg.capitalize() for arg in args))
elif "-u" in opts:
    print(" ".join(arg.upper() for arg in args))
elif "-l" in opts:
    print(" ".join(arg.lower() for arg in args))
else:
    raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")"""

try:
    start = int(args[0])
    end = int(args[1])
except ValueError:
    raise SystemExit(f"Provide a positive integer")
finally:
    if len(args) != 2:
        raise SystemExit(f"Provide min and max")

x = []
y = []

for i in range(start, end):
    sequencer = model.Collatz(i)
    result = sequencer.sequence()
    x.append(result[0])
    y.append(result[1])

with open('results.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['number', 'trials'])
    for i in range(len(x)):
        writer.writerow([x[i],y[i]])