from pathlib import Path
import sys

# Ensure project root is importable when pytest runs from different working dirs.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
