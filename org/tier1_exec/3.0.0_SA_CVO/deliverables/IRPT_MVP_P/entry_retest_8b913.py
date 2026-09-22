"""Replay original entry reviewer assertions on the exact R-P06 replacement."""
import importlib.util
from pathlib import Path


def main():
    here = Path(__file__).resolve()
    spec = importlib.util.spec_from_file_location(
        "original_entry_probe", here.with_name("entry_probe_f7f5.py"))
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    probe.PIN = "8b913a9414b60a2feb1815efa701a358027ab20a"
    # Keep original candidate JSON unchanged; all assertions remain in the same file.
    probe.__file__ = str(here)
    return probe.main()


if __name__ == "__main__":
    raise SystemExit(main())
