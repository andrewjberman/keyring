# NFRA_DEVPLN: CVO adjudication, round 1 (L8 channel compile)

<sweep_watermark>2026-10-13T20:43Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO~L` (laptop), 2026-10-13 ~20:4xZ. Inputs: `investigations/INVESTIGATION_v1.md` (23 rows, all OPEN at this
read, 4 ARMED), the issuer's drain-end read `org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_ROUND1_DRAIN_END_20261013.md`
@f4539dcc2f, and the CTO's `ledger/ROUND_ANALYSIS.round1.md` @14a0501ee5 with its disarm word (msg 108886). Round 1 has no judgment
criterion (`round-close-check` judgment=0), so there is no L9 grade.

**Result: all 23 rows dismissed with reason; 0 graduate; ARMED 4 -> 0.** Measured by this seat at 20:4xZ, not taken from the drain read:
`approval-status` is on `origin/box/dell1`, `box/dell2`, `box/sitez`, `box/laptop` and `origin/CLOUD` (8 references each; control: 79
`def` lines on CLOUD); `.tools/tests/test_open_calls_approval.py` reads `cases=13/13 ok=True`; `.tools/tests/test_open_calls.py` reads
`cases=0/2 ok=False` (W1-S8, still red, carried by the CTO's round-2 item 6).

```json
[
 {
  "id": "NFRA_DEVPLN-C-S1",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T20:43Z",
  "one_line": "Round 1, CTO rulings. W1-S1 DISARMED on its owner's word: the approval close's CLOSED-BOTH skip is intended, since an approval's subject is one branch on the building box's one-writer list and its validity is class plus closer, read by approval-status (msg 108886; analysis section 2). S1: both of the issuer's readings accepted (C-PROMOTE first-parent plus per-feature binding, in the v0.3 wording addendum; C-MERGE-FORWARD (iii) already reads as a lease-written row).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_DEVPLN-W1-S1",
   "NFRA_DEVPLN-S1"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round1.md @14a0501ee5 section 2",
    "broker msg 108886, 1.0.0_SA_CTO -> 3.0.0_SA_CVO~L, 2026-10-13T20:33Z: the disarm word for W1-S1, to be written at this compile"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Ruled by the disarm owner: W1-S1 intended and disarmed; S1 both readings accepted, PRD v0.3 wording addendum, no ENDPOINT change.",
  "spec_asserts": "Spine L8: the CVO compiles the round's new rows; an ARMED row disarms only on its disarm_owner's act (W1-S1's owner is 1.0.0_SA_CTO); S1 asks the CTO to rule two readings.",
  "world_is": "The CTO ruled both at the round-1 analysis @14a0501ee5 section 2 and sent the disarm word for W1-S1 (msg 108886). This row records the disarm and the accepted readings; nothing further is owed on either row."
 },
 {
  "id": "NFRA_DEVPLN-C-S2",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T20:43Z",
  "one_line": "Round 1, the issuer's three ARMED rows, disarm measured by this seat. W1-S4: every box branch and CLOUD carry approval-status, so no box's older tool refuses a list holding an approval row. W1-S6 and W1-S10: amended in d0564a0d90 and 0b70cbd93a; the approval test reads 13/13 on this tree.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_DEVPLN-W1-S4",
   "NFRA_DEVPLN-W1-S6",
   "NFRA_DEVPLN-W1-S10"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "MSYS_NO_PATHCONV=1 git show <ref>:.tools/open-calls.py | grep -c approval-status, after git fetch: 8 on each of origin/box/dell1, origin/box/dell2, origin/box/sitez, origin/box/laptop, origin/CLOUD; positive control 79 def lines on origin/CLOUD",
    "timeout 120 python .tools/tests/test_open_calls_approval.py -> OPEN-CALLS-APPROVAL-TEST cases=13/13 ok=True (box/laptop working tree, 2026-10-13 ~20:4xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disarmed by their owner 2.0.0_SA_COO~DV and the disarm measured here: approval-status synced to every box branch; the DP-b-1 test amended and green 13/13.",
  "spec_asserts": "W1-S4, W1-S6 and W1-S10 stay ARMED until their owner 2.0.0_SA_COO~DV disarms them: every box synced before an approval row is read; the DP-b-1 test green after DP-b-5.",
  "world_is": "Measured here after git fetch: approval-status present 8 times on each of five branches (control 79 defs on CLOUD); test_open_calls_approval.py cases=13/13 ok=True. All three disarm conditions hold."
 },
 {
  "id": "NFRA_DEVPLN-C-S3",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T20:43Z",
  "one_line": "Round 1, the two BLOCKING rows on DPb5-AC2's branch (W1-S5, W1-S9) were premises in the order, not tool defects: DEV did not contain PROD, so no PROD-cut branch could read dev-overlap. The issuer's second amendment 0b70cbd93a made AC2 the positive real read of origin/cand/laptop/contributing-boxes; the dev-overlap refusal stays in AC1's fixture cases.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_DEVPLN-W1-S5",
   "NFRA_DEVPLN-W1-S9"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "commit 0b70cbd93a (amend NFRA_DEVPLN.TO-DP-b-5, second amendment on W1-S9 and W1-S10)",
    "commit 22ab897fb5: DPb5-AC2 PASS on origin/cand/laptop/contributing-boxes (result=OK commits=1)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Closed by the issuer's amendment of the order's premise; the tool followed BUILD item 1 throughout and nothing was written by either refused run.",
  "spec_asserts": "DPb5-AC2 as first written and as first amended expected a real branch refused reason=dev-overlap.",
  "world_is": "No real branch could be: DEV did not contain PROD (W1-S5) and then held no commit over PROD (W1-S9). The second amendment 0b70cbd93a made AC2 the positive read, PASS at 22ab897fb5; the refusal arm stays in AC1's fixtures."
 },
 {
  "id": "NFRA_DEVPLN-C-S4",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T20:43Z",
  "one_line": "Round 1, rows carried forward or overtaken. Carried by the CTO's round-2 item 6 (one batch repair cell): W1-S8 (test_open_calls.py still 0/2 here), W2-S2 (no fetch), W1-S7 (approval-lease --project default), W3-S3 (Step 8 receipt). Overtaken by sibling cells landing: W2-S1 (approval-status now exists), W4-S1 (the approval kind now exists), W4-S2 (portal-merge-forward.sh and portal-release-build.sh now exist). Disclosed as a method limit: W5-S1 (git cherry gives merges no sign; the tool shows them in their own column, and the nine branches were ruled on the issuer's containment read).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_DEVPLN-W1-S8",
   "NFRA_DEVPLN-W2-S2",
   "NFRA_DEVPLN-W1-S7",
   "NFRA_DEVPLN-W3-S3",
   "NFRA_DEVPLN-W2-S1",
   "NFRA_DEVPLN-W4-S1",
   "NFRA_DEVPLN-W4-S2",
   "NFRA_DEVPLN-W5-S1"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round1.md @14a0501ee5 section 4 item 6 (names W1-S8, W2-S2, W1-S7, W3-S3) and item 4 (settlement list re-run)",
    "timeout 120 python .tools/tests/test_open_calls.py -> OPEN-CALLS-TEST cases=0/2 ok=False (W1-S8 not yet repaired)",
    ".tools/portal-merge-forward.sh, .tools/portal-release-build.sh, .tools/portal-settlement-list.py present in the box/laptop tree; approval-status in .tools/open-calls.py on every box branch (row NFRA_DEVPLN-C-S2)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "One carrier each: the four repair rows ride the CTO's round-2 enrichment item 6; three were sequencing gaps closed when the sibling cells merged; W5-S1 is a stated limit of git cherry, rendered honestly by the tool.",
  "spec_asserts": "Each worker row needs one carrier: a ruling, a repair cell, or a reason it no longer stands.",
  "world_is": "Four rows are named in the CTO's round-2 item 6 (W1-S8 still red 0/2 here); three gaps closed when DP-b-1, DP-b-2 and DP-b-3 merged (scripts and approval-status present); W5-S1 is git cherry's documented behaviour, shown in its own column."
 },
 {
  "id": "NFRA_DEVPLN-C-S5",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-13T20:43Z",
  "one_line": "Round 1, order-wording rows where the worker built to the graded criterion or the tool as it stands and said so: W1-S2 (DECLINED prints valid=no, as DPb1-AC1 grades), W1-S3 (--ruling-file as an alias; --portal and approval-lease came in DP-b-5), W2-S3 (AC3's pattern has no comment exclusion; the count is 0 with comments included), W3-S1 (only one Step 0 bullet carries the merge text), W3-S2 (setup refusal tokens beyond the cell's list), W3-S4 (189 non-ASCII bytes pre-exist in the prod-deploy SKILL.md; the cell added none). W2-S4 and W3-S5: the status-flip clause sits outside the worker's <paths>; the issuer flipped both orders.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_DEVPLN-W1-S2",
   "NFRA_DEVPLN-W1-S3",
   "NFRA_DEVPLN-W2-S3",
   "NFRA_DEVPLN-W3-S1",
   "NFRA_DEVPLN-W3-S2",
   "NFRA_DEVPLN-W3-S4",
   "NFRA_DEVPLN-W2-S4",
   "NFRA_DEVPLN-W3-S5"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "each row's own world_is in investigations/INVESTIGATION_v1.md, read whole",
    "round-close-check --project NFRA_DEVPLN: orders=6, 6 complete, proof_ok=6 (2026-10-13 ~20:4xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Wording gaps in the orders, resolved in the build toward the graded criterion and disclosed; no defect stands. The status-flip clause against the <paths> grant is the issuer's template wording, the same class as NFRA_CTLPLN-W78-S4.",
  "spec_asserts": "The orders' BUILD text, flags and status-flip clause as written.",
  "world_is": "Each row records a wording gap the worker resolved toward the graded criterion or the tool as it stands, and disclosed; the issuer flipped the two orders the workers could not. No row describes a defect in the built tools."
 }
]
```

-- 3.0.0_SA_CVO~L
