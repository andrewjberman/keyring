"""R-40 precondition 4, the CTO's acceptance verbatim (COO~X's discriminator): an
in-memory build_crosswalk THROUGH add_security's own path on the CURRENT inputs
prints MEASURED 194 (today's signed shape) BEFORE any registration is added,
194 + N after N fake registrations, and a negative control with the universe
argument withheld reads 36.

READ-ONLY: one S3 list + one get of the retained universe/v1 input (ambient
credentials), no put, no Bloomberg call. Run from the worktree root:
  PYTHONPATH="$(pwd)" python org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_EXPERIENCE/CLOSER_POOL_ONE_PUT_20260924/acceptance_precondition_4.py
"""
import json
import sys

from lib.research.identity import add_security, crosswalk

AS_OF = sys.argv[1] if len(sys.argv) > 1 else "2026-09-24"
N = 3

universe, source = add_security._identity_universe(None)
rows, reg_path = crosswalk.load_registrations()
print("universe %s names=%d; registrations %s rows=%d" % (source, len(universe.get("names") or []), reg_path, len(rows)))

before = add_security._build_document(AS_OF, list(rows), reg_path, universe, source)
print("ARM before-any-registration  MEASURED=%d records=%d registered=%d universe_registered=%d"
      % (before["denominators"]["MEASURED"], before["denominators"]["records"],
         before["denominators"]["registered"], before["denominators"].get("universe_registered", 0)))

fake_rows = list(rows)
for i in range(1, N + 1):
    root = "FAKE%d" % i
    fake_rows.append({
        "folder": None, "bloomberg": "%s US" % root, "resolution": "MEASURED",
        "security_key": "%s_US_Equity" % root,
        "identity": {"bloomberg_security": "%s US Equity" % root, "name": "%s CORP" % root,
                     "exchange": "US", "lei": None, "cik": None, "sec_id": None,
                     "source": None, "registered_at": "%sT00:00Z" % AS_OF, "field_errors": {}},
        "exchange_finding": "AGREES: id token 'US' == Bloomberg EXCH_CODE 'US'",
        "registered_at": "%sT00:00Z" % AS_OF, "raw_source": None,
    })
after = add_security._build_document(AS_OF, fake_rows, reg_path, universe, source)
print("ARM after-%d-fake-registrations MEASURED=%d records=%d registered=%d"
      % (N, after["denominators"]["MEASURED"], after["denominators"]["records"], after["denominators"]["registered"]))

negative = add_security._build_document(AS_OF, list(rows), reg_path, None, None)
print("NEGATIVE universe-withheld       MEASURED=%d records=%d registered=%d"
      % (negative["denominators"]["MEASURED"], negative["denominators"]["records"], negative["denominators"]["registered"]))

ok = (after["denominators"]["MEASURED"] == before["denominators"]["MEASURED"] + N
      and negative["denominators"]["MEASURED"] < before["denominators"]["MEASURED"])
print("VERDICT %s: before=%d after=%d (+%d) negative=%d"
      % ("PASS" if ok else "FAIL", before["denominators"]["MEASURED"], after["denominators"]["MEASURED"], N,
         negative["denominators"]["MEASURED"]))
print(json.dumps({"as_of": AS_OF, "universe_source": source, "before": before["denominators"],
                  "after": after["denominators"], "negative": negative["denominators"]}, indent=1))
sys.exit(0 if ok else 1)
