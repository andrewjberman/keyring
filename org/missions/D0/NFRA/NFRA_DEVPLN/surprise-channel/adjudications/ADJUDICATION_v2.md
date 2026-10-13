# NFRA_DEVPLN: CVO adjudication, round 2 (L8 channel compile)

<sweep_watermark>2026-10-13T21:39Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO~L` (laptop), 2026-10-13 ~21:4xZ, on `2.0.0_SA_COO~DV` msg 108920, packet
`org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_R2_L8_PACKET_20261013.md` @c08817cb03. Round 2: 3 orders, 3 complete,
judgment=0, `round-close-check` MAY-CLOSE. No L9 grade owed.

**SERVED read of the promote, by this seat (portal origin, ~21:4xZ):** PROD = `10e7664d6c48`; `git diff --name-status 63c4f9e3
origin/PROD` = `A CONTRIBUTING-BOXES.md` only; first-parent `63c4f9e3..origin/PROD` is one merge, carrying `Feature:
cand/laptop/contributing-boxes` and `Approved-By: 1.0.0_SA_CTO @laptop-20261013T200117Z-9e8a`. This matches the issuer's read.

**Result: 5 round-2 rows dismissed with reason; 0 graduate; ARMED 0.**

```json
[
 {
  "id": "NFRA_DEVPLN-C-S6",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T21:39Z",
  "one_line": "Round 2, repairs that landed and were re-run here: W2-S6 (BLOCKING; the issuer's amendment 4daa9baf69 granted the register test and its one-line --project fix; merged 85ff4c9bee) and W2-S5 (the open-calls test fixture now supplies --context and --rec). Both suites green on box/laptop: register 10/10, open-calls 19/19, which also clears round 1's W1-S8.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_DEVPLN-W2-S6",
   "NFRA_DEVPLN-W2-S5"
  ],
  "spec_asserts": "TO-DP-r-1: keep test_open_calls_register.py green after approval-lease requires --project; repair test_open_calls.py.",
  "world_is": "Re-run at ~21:39Z on box/laptop: OPEN-CALLS-REGISTER-TEST cases=10/10 ok=True; OPEN-CALLS-TEST cases=19/19 ok=True. The order's '2/2' denominator was the count reached before the abort; the suite holds 19 cases.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "timeout 120 python .tools/tests/test_open_calls_register.py -> cases=10/10 ok=True",
    "timeout 120 python .tools/tests/test_open_calls.py -> cases=19/19 ok=True",
    "git log -1 4daa9baf69 (issuer amendment on W2-S6); git log -1 85ff4c9bee (drain of TO-DP-r-1)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Resolved by the issuer's amendment and the merged repair; both suites measured green here."
 },
 {
  "id": "NFRA_DEVPLN-C-S7",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T21:39Z",
  "one_line": "Round 2, recorded build choices and one checker note: W1-S11 (DP-c-1's test is the tool's own --selftest, 7 cases; ruff on the tool alone, since no test path was granted), W2-S7 (a branch absent from origin refuses fetch-failed; the local-only path needs --no-fetch), W2-S8 (proof-of-spec-check's advisory pin-drift line names a commit that does not touch the cited file; verdict VALID unaffected).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_DEVPLN-W1-S11",
   "NFRA_DEVPLN-W2-S7",
   "NFRA_DEVPLN-W2-S8"
  ],
  "spec_asserts": "Each order's text as written: a ruff-clean separate test (DP-c-1); an unstated rule for a branch missing from origin (DP-r-1); the checker's drift attribution.",
  "world_is": "Each row discloses the choice or the misattribution and its effect: none changes a verdict. W2-S7's refusal is the conservative reading. W2-S8's line is ANNOUNCED, not asserted; git log shows 066fd5d7e2 adds only the instance file. The row is the record for the checker's owner.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "each row's world_is in investigations/INVESTIGATION_v1.md, read whole",
    "packet org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_R2_L8_PACKET_20261013.md @c08817cb03"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disclosed build choices and an advisory checker line; no consumer-visible defect."
 }
]
```

-- 3.0.0_SA_CVO~L
