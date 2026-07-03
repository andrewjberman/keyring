"""comp-debt signal engines -- each emits grounding_lib.Signal objects for fuse.py.

REUSE adapters (call/adopt existing substrate, never fork):
  duplicates.py  -- CALLs debtscan/dup_scan.run_scan (the DONE comp-dups signal)
  graph.py       -- comp-kuzu/comp-blast no-consumer + the 14-class FP-suppression overlay
  usage.py       -- agent_telemetry/ + comp-which-rail.log tool-coldness

NEW signals (genuinely new-build):
  git_heat.py    -- last-touch + last-reference over N days
  tf_drift.py    -- comp-iam reconcile + live-aws (ground-on-LIVE)
  cloudtrail.py  -- CW invocation-metrics (15mo) + CloudTrail cross-confirm

Every signal returns INFERRED symptoms; a signal is CONFIRMED only with its own live/source
confirm leg (Rule 22). fuse.py applies the dormant_guard + the >=2-CONFIRMED AC2 bar.
"""
from __future__ import annotations
