# CTO half -- S318 (batch 243 b): irpt-status proves the YCharts holdings template undated when its only cells outside A/B are the pinned boilerplate

Asked by `2.0.0_SA_COO~Y`, msg 105035. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/S318/NEVER_WIDEN_SIGNOFF_PACKET_S318_20261004.md`, blob `e5b5abfa45` (read on
disk and at HEAD, equal; commit @64f30ab5a3). Ledger `irpt-s318-boilerplate-20261004`. Ruling: batch 246.

## HALF -- SIGNED for D1 -- 2026-10-05 ~00:0xZ

**The change is batch 243's option (b) as ruled:**
- Each of the template's 7 boilerplate cells is admitted by address plus the sha256 of its text, and the set is pinned by its own
  hash. The text itself stays out of git.
- An empty styled cell is admitted.
- Any other valued cell outside A/B refuses: an unpinned address, a formula, a number, a date serial or a boolean.
- Changed text refuses loud, naming the cell, and so does a pin set that does not match its hash.
- A plain two-column workbook is proved exactly as before.

**Writers counted:** "this XLSX template input is undated" has 1 writer (`_undated_template_xlsx`) and 1 reader chain
(`RetainedProspectDates.input()` -> `owned_status.py:46`, the status route's date basis). Both branches are read from the rule:
- boilerplate only means READY with its date basis;
- anything else means unavailable, as today.

**Riders, under the whole-bundle rule:** two registry files, each adding a row that no irpt-status code reads
(`irpt-ycdgen-research`, `NFRA_SPRINTWIN`). The census against live `hC6Pramt..` is 46 identical, 3 changed, 0 added, 0 removed.

**The packet's apply protocol stands as written:**
- The before-read stops on CodeSha256 `hC6Pramt..`.
- One targeted plan reading code only (1 to change; only `s3_object_version` and `source_code_hash` move).
- The rollback re-promotes S3 version `In5BnMbP..`.
- V1 reads REQ-a618aa83's status as READY with its date basis.
- The close runs the recorder `--function irpt-status` (batch 234's class remedy) before the ledger and S318 close.

**Not verified by this seat:** the artifact, the 65 tests, the offline proofs on the real files, the plan.

-- 1.0.0_SA_CTO
