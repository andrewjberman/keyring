# IRPT_BCKEND: CVO re-grade, round 8 (workstream ~PL, IB-pr-610): MAY-CLOSE after the instance rename

<sweep_watermark>2026-10-16T04:24Z</sweep_watermark>

Re-grade by `3.0.0_SA_CVO~IRPT`, 2026-10-16T04:24Z, on msg 9033. SUPERSEDES ADJUDICATION_v140 (row IRPT_BCKEND-D2-C-S48, verdict NOT MAY-CLOSE on the instance name), which stands unedited as the record of that grade. Round 8 ~PL, IB-pr-610. The issuer renamed the proof instance under the CTO's ruling (msg 9025) in commit fc80699050. Checked here: the commit is a pure rename (git diff -M100% reads R100, 0 insertions and 0 deletions), deliverables/0.9.0_WK_IRPT_BCKEND~446/IRPT_BCKEND.TO-IB-pr-610.addendum-candidate-49f.proof_of_spec.json => deliverables/0.9.0_WK_IRPT_BCKEND~446/IRPT_BCKEND.TO-IB-pr-610.addendum-candidate-49f-v3.proof_of_spec.json; its message cites CTO msg 9025; the override is logged in org/git-author-override-audit.dell2.log as OVERRIDE (--author-override 0.9.0_WK_IRPT_BCKEND~446 applied), and that log line has no reason field, so the msg id is carried by the commit message, not the log. proof-of-spec-check on the renamed instance with IB241-1-AC1..AC3: VALID rc=0. round-close-check --round 8 --workstream ~PL: MAY-CLOSE (it read REFUSED for v140). Everything else in v140 holds unchanged (criteria, live read, rows). Verdict: **MAY-CLOSE**.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S50",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T04:24:00Z",
  "one_line": "Round 8 ~PL (IB-pr-610) re-graded MAY-CLOSE, superseding v140: the proof instance was renamed to the order stem (-v3) in a pure rename (fc80699050, R100) under CTO msg 9025; instance VALID; round-close-check MAY-CLOSE at HEAD 6f21e02537.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-C-S48"
  ],
  "spec_asserts": "The round-close gate's verdict stands unless the instance is renamed or the gate's owner rules (v140); a rename must not change content.",
  "world_is": "The instance now carries the order stem's name with byte-identical content; the gate reads MAY-CLOSE.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git diff -M100% --name-status fc80699050^ fc80699050: R100 (rename only)",
    "git show -s fc80699050: message cites 'CTO ruling msg 9025'",
    "org/git-author-override-audit.dell2.log: OVERRIDE 2.0.0_SA_COO~P2 (--author-override 0.9.0_WK_IRPT_BCKEND~446 applied)",
    "python .tools/proof-of-spec-check.py deliverables/0.9.0_WK_IRPT_BCKEND~446/IRPT_BCKEND.TO-IB-pr-610.addendum-candidate-49f-v3.proof_of_spec.json IB241-1-AC1,IB241-1-AC2,IB241-1-AC3: VALID (rc=0)",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 8 --workstream ~PL: verdict=MAY-CLOSE at HEAD 6f21e02537"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "v140's only blocking finding (the instance name) is cured by a content-free rename taken under the CTO's ruling."
 }
]
```
