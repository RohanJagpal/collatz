import sys
import model
import csv

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

try:
    start = int(args[0])
    end = int(args[1])
except ValueError:
    raise SystemExit(f"Provide a positive integer")
finally:
    if len(args) != 2:
        raise SystemExit(f"Provide min and max")

n = []
trials = []

for i in range(start, end):
    sequencer = model.Collatz(i)
    result = sequencer.sequence()
    n.append(result[0])
    trials.append(result[1])

with open('results.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['number', 'trials'])
    for i in range(len(n)):
        writer.writerow([n[i],trials[i]])