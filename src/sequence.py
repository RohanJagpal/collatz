import sys
from .model import Collatz

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
    float(args[1])
except ValueError:
    raise SystemExit(f"Provide a positive real")
finally:
    if len(args) > 2:
        raise SystemExit(f"Only 1 number permitted")

number = args[1]

sequencer = Collatz(number)
sequencer.sequence()