"""Repeat original immutable R-P08 and retention assertions at the replacement pin."""
import retained_repository_probe_aa1c as original

original.PIN = "284436ca11140a0ede1ef3d53f8b3aa855d4a7a3"
original.__file__ = __file__

if __name__ == "__main__":
    raise SystemExit(original.main())
