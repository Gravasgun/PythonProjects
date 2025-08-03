#!/usr/bin/env python3
import sys

arg = sys.argv[1] if len(sys.argv) > 1 else ""

literal = repr(arg)

print("#!/usr/bin/env python3")
print(f"print({literal})")
