# LGIC_CANON -- remediations (compile ordered by the CTO's closure plan)

<sweep_watermark>2026-09-21T17:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01 ~09:1xZ. Trigger: 1.0.0_SA_CTO 103630 and 103656 (RULINGS batches 71 and 74). The channel held 1 undispositioned row of 58 (S29); it is graduated here, open with its owner. All 30 task orders read terminal. Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_FIRMBKTS_LGIC_CANON_COMPILE_20261001.md (co-committed).

```json
[
  {
    "id": "LGIC_CANON-S29",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "02_DOCTRINE.md's generated naming section is stale and cannot be re-rendered safely: a ruled correction was written by hand inside the generated markers on 2026-09-20 while the schema source still carries the retired text, so a --write silently reverts the ruling. The check has been red for ten days, so it no longer tells anyone when the section drifts for a new reason.",
    "evidence": [
      "python infra/logic/render_naming_section.py --check at CLOUD HEAD (this seat, 2026-10-01 09:0xZ): rc=1, 'CHECK: STALE -- 3 failure(s)': the NAMING_SCHEMA.json stamp reads v1.10 sha256:043bb490... against a live file hashing sha256:0a5d5ba3... (v1.12); the scopes.json stamp differs; the section differs from a fresh render at section line 4 (156 lines against 154)",
      "infra/logic/02_DOCTRINE.md:224 at HEAD (this seat): the hand-written line 'claim: **PRESENT** -- landed by LN-g-1 ... grade() consults it' is still there",
      "the schema's live hash has moved again since the row was filed (the row read sha256:2c8834a9...), so the section is now two schema edits behind",
      "investigation row LGIC_CANON-S29 (4.0.0_SA_CRO, 2026-09-21): --write produced a 3+/5- diff that reverted the 2026-09-20 correction",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_FIRMBKTS_LGIC_CANON_COMPILE_20261001.md (co-committed)"
    ],
    "remedy": "P1, as the row states it: move the 2026-09-20 correction into its source (the legacy-served-paths claim text in org/standards/NAMING_SCHEMA.json), run --write, and confirm the re-render keeps the corrected line and changes only the stamps; then --check reads CURRENT. Until then nobody runs --write on that file. The row's two open measurements (whether grade() reads that schema field; the schema edit's lane) are the owner's first reads.",
    "owner": "4.0.0_SA_CRO",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "4.0.0_SA_CRO",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "4.0.0_SA_CRO",
      "at": "2026-10-07T15:08Z"
    },
    "closed": true
  }
]
```
