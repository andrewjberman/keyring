"""Hardening fixture (CTO~Z follow-on 20260725T094941Z): float version -- Python renders 1.10 as '1.1',
so the version text cannot round-trip. Must render ASSUMPTION naming the type+value, never PASS or FAIL."""
SCHEMA_VERSION = 1.10
