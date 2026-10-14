# NFRA_DEVPLN: CVO adjudication, rounds 3-8 (L8 channel compile)

<sweep_watermark>2026-10-14T13:25Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO~L` (laptop), 2026-10-14 ~13:2xZ, on `2.0.0_SA_COO~DV` msg 109146 (round-8 packet @e4f3acfcc8). Rounds 3 to 7
were analysed by the CTO without a CVO compile; this one compile carries every row since round 2. 18 rows, 1 ARMED (W1-S19).

**Result: 18 dismissed with reason (C-S9..C-S11); 0 graduate; ARMED 1 -> 0.**

**Round 8's slug is HELD:** `round-close-check --round 8` reads REFUSED. The DT's proof instance for `TO-DP-y-1` records
`DPy1-AC1` FAIL against the criterion's old text. The issuer amended the text and re-ran it to a PASS but cannot write the DT's file.
That instance needs re-recording by its owner, `0.4.0_DT_ClientPlatform`, or the issuer under a ruling.

**SERVED read, by this seat:** the packet's reads of origin/PROD are the issuer's. This seat did not re-read the deployed bundle.

```json
[
 {
  "id": "NFRA_DEVPLN-C-S9",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T13:25Z",
  "one_line": "Round 8: W1-S19's disarm accepted (the git pre-push limb refuses what never-rules-gate.sh's two DEV carve-outs still admit; on this box portal/.git/hooks/pre-push is 5921 bytes and calls dev_push_payload_gate.py, read here); S6 ruled by the issuer (DPy1-AC1's feature count was a moving target; amended to unapproved=0); S7 is that disposition.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_DEVPLN-W1-S19",
   "NFRA_DEVPLN-S6",
   "NFRA_DEVPLN-S7"
  ],
  "spec_asserts": "W1-S19 stays ARMED until a DEV push the law forbids cannot land; DPy1-AC1 as first written expected features=9.",
  "world_is": "Read here: portal's own hooks/pre-push (git rev-parse --git-path) is 5921 bytes with 4 references to dev_push_payload_gate.py. The other three boxes rest on the round-6 read-backs the issuer cites; this seat did not re-read them. The carve-outs in never-rules-gate.sh (MSTR's file) are dead letter beside the hook and are owed removal in the next round, as S7 says. DPy1-AC1: the issuer re-ran the amended text, unapproved=0 ref=refs/remotes/origin/PROD. But the DT's own proof instance still records AC1 FAIL, so round-close-check --round 8 reads REFUSED (proof_bad=1).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "portal/.git/hooks/pre-push, 5921 bytes, read 2026-10-14 ~13:2xZ",
    "org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_R8_L8_PACKET_20261014.md @e4f3acfcc8",
    "python .tools/round-close-check.py --project NFRA_DEVPLN --round 8 -> PROOF-BAD NFRA_DEVPLN.TO-DP-y-1: FAIL row(s) DPy1-AC1; verdict=REFUSED"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W1-S19 is contained where the hook is installed (measured on the laptop); S6 is ruled and S7 records it. Owed, not a row: the DT's proof instance re-recorded against the amended AC1, and the carve-out removal."
 },
 {
  "id": "NFRA_DEVPLN-C-S10",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T13:25Z",
  "one_line": "Rounds 3-7: rows the CTO ruled in his round analyses and later rounds repaired: W1-S12 (the waiver set, r3), W2-S9 and W2-S10 (r3 batch), W1-S13, W2-S11 and W1-S14 (r4 batch), S3 (the pre-push limb, r4 to r5, now DP-j-1's), W1-S15 (the stricter reading stands, r5), W2-S12 (r5 guard), S4 and W1-S16 (r6, repaired r7: release-check now prints ref= and sha=), S2 (a withdrawn close and the foreign-box git source now exist in open-calls.py), S5 (served by NFRA_CTLPLN-S9123 @2d35ab062c; unblock.py reads another box's call).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_DEVPLN-W1-S12",
   "NFRA_DEVPLN-W2-S9",
   "NFRA_DEVPLN-W2-S10",
   "NFRA_DEVPLN-W1-S13",
   "NFRA_DEVPLN-S3",
   "NFRA_DEVPLN-W2-S11",
   "NFRA_DEVPLN-W1-S14",
   "NFRA_DEVPLN-W1-S15",
   "NFRA_DEVPLN-W2-S12",
   "NFRA_DEVPLN-S4",
   "NFRA_DEVPLN-W1-S16",
   "NFRA_DEVPLN-S2",
   "NFRA_DEVPLN-S5"
  ],
  "spec_asserts": "Each row needs one carrier: a ruling, a repair, or a reason it no longer stands.",
  "world_is": "Each id is named in ledger/ROUND_ANALYSIS.round3.md to round7.md with a ruling or a repair cell. Spot reads here: open-calls.py names 'withdrawn' 11 times and carries the OPAL_CLOUD_READ_LOCAL / git foreign-source seam (S2); unblock.py:26 reads a call on another box through approval_read (S5); the round-8 packet's release check prints ref=refs/remotes/origin/PROD sha= (S4); test_open_calls_approval.py reads 13/13.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round3.md .. round7.md (each id)",
    "org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round8.md line 5 (S5 served)",
    "timeout 120 python .tools/tests/test_open_calls_approval.py -> cases=13/13 ok=True"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Ruled by the CTO and repaired in the following rounds; no row stands open."
 },
 {
  "id": "NFRA_DEVPLN-C-S11",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T13:25Z",
  "one_line": "Round 7: the repair worker's notes on its own edits: W1-S17 (two selftest greps turned from exact-line to prefix matches so the appended ref= sha= suffix keeps both cases testing what they tested) and W1-S18 (the test helper pops an inherited GIT_DIR for every case, the isolation a git hook needs).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_DEVPLN-W1-S17",
   "NFRA_DEVPLN-W1-S18"
  ],
  "spec_asserts": "The round-7 repair order: every existing selftest case stays, and case 9 alone is named for GIT_DIR isolation.",
  "world_is": "Both edits keep the cases' intent and are disclosed for the lane owner. A GIT_DIR pop is a no-op outside a hook.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "each row's world_is in investigations/INVESTIGATION_v1.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disclosed build notes; no defect."
 }
]
```

-- 3.0.0_SA_CVO~L
