import sys
import model

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

try:
    number = int(args[0])
except ValueError:
    raise SystemExit(f"Provide a positive integer")
finally:
    if len(args) > 1:
        raise SystemExit(f"Only 1 number permitted")

sequencer = model.Collatz(number)
result = sequencer.sequence()
print(f"\n\033[92m===RESULT===\n\u001b[37mInitial number: {str(result[0])}\nTrials to complete: {str(result[1])}\n\033[94m===FINISHED===\u001b[37m")