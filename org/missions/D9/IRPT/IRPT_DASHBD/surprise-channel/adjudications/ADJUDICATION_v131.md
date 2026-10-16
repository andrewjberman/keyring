# IRPT_DASHBD: CVO adjudication, round 147 (workstream PUBLISH, ~D2): the first served Cottonwood series publish

<sweep_watermark>2026-10-16T07:05Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T07:05Z, on msg 9132 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND147_PUBLISH_148_CONTRACT_DRAIN_END_20261016.md` @a779f13153, blob 86898a5ab2, shared with round 148 CONTRACT). Not B-49F's round 147 (v126). One WORLD order, TO-DB-b-283 (applier 0.7.0_AE_CloudOps~DB2; drained d2ef6694f5, in HEAD). No judgment criterion. Re-run at HEAD e4012e6398: DBC151-1-AC1, DBC151-2-AC1, DBC151-3-AC1 PASS; round-close --round 147 --workstream PUBLISH MAY-CLOSE. Every AWS read below is read-only and prints counts only. Struck DB118-3-AC3 still FAILS. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S69",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T07:05:00Z",
  "one_line": "Round 147 PUBLISH (~D2): the first served Cottonwood series, graded on live state. (1) PAIR: NEVER_WIDEN_PACKET_COTTONWOOD_REPORTING_PUBLISH_LAMBDA.md hashes to 0c9b495ce2f7 at HEAD (unchanged since 6c8e76f0e0); the COO half (6c8e76f0e0) and the CTO half (474f33174c) both read SIGNED and name that full hash; the packet carries 'Both branches (Acts 2 to 4)' and 'Rollback, per key' (the listed keys the ledger records, never a wildcard delete; the prefix was empty before). (2) OBJECTS: s3://opal-data-cottonwood/irpt/cottonwood/platinum/reporting/ holds 1,878 current objects (939 series.json.gz, 939 manifest.json), all last modified 2026-10-16T04:57:37Z..04:59:09Z, inside the act window; 2 noncurrent versions (consistent with the canary's two objects rewritten by the full upload; inferred) and 0 delete markers; the prefix was empty before, so nothing else under it changed. (3) VALUES: 3 series drawn by a seeded random sample, joined to the Cottonwood gold account_return_daily on account and date (65 partitions from 2026-07-10): 107 value pairs and 86 return pairs compared, max absolute difference 0 and 0, exact; income all null in all three; no income_claim key (the contract that requires it landed after this act, see v132). (4) LEDGER: irpt-dashbd-cottonwood-reporting-publish-20261016 is OPEN in the shared tree and in 10 worktree branches cut after it opened (11 of 80 worktrees read); open by design until the schedule pair. (5) READERS: no served reader opens these objects. The only reporting-read Lambda is irpt-49f-reporting-read-lambda, whose directory map names 49financial alone; no Cottonwood or Inflection read Lambda exists. NOT CLIENT-FACING today. ~D2's section 3, graded: S108 (two checker defects, fixed; all three criteria pass on the fixed checker) is dismissed; the calendar row W226-S1 stands (the fallback fails closed past 2027-12-31, per ~D2's read). Missed: none found in this act beyond the contract timing in v132.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S108"
  ],
  "spec_asserts": "CLAUDE.md NEVER rules: served output moves only under a never-widen sign-off that names the blast radius and a rollback per key, covering both branches. Spine L9/L10.",
  "world_is": "The Cottonwood series is served at its platinum prefix (939 accounts), equal to gold on the sampled days, with no reader and no schedule. The ledger stays open.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T06:5xZ at HEAD e4012e6398: DBC151-1-AC1, -2-AC1, -3-AC1 PASS; round-close-check --round 147 --workstream PUBLISH MAY-CLOSE",
    "sha256 of NEVER_WIDEN_PACKET_COTTONWOOD_REPORTING_PUBLISH_LAMBDA.md = 0c9b495ce2f7...; both halves SIGNED naming 0c9b495ce2f7e347738ad53a643d1f7b19bf48b226258136e84753371cdae463",
    "s3 list-objects-v2 / list-object-versions on opal-data-cottonwood irpt/cottonwood/platinum/reporting/: 1,878 objects, 939 + 939, 2026-10-16T04:57:37Z..04:59:09Z, 2 noncurrent, 0 delete markers",
    "spot read (seed 20261016, 3 series) vs gold account_return_daily 2026-07-10..: value pairs 61/23/23, return pairs 56/15/15, max abs diff 0.0",
    "git worktree list --porcelain: 80 worktrees; ls-tree .open_deploys: the entry present in 11",
    "lambda get-function-configuration: irpt-49f-reporting-read-lambda exists (IRPT_DIRECTORY_BUCKET_MAP 49financial only); irpt-cot-reporting-read-lambda and irpt-inf-reporting-read-lambda ResourceNotFound",
    "struck DB118-3-AC3 re-run via p118_cottonwood.py: FAIL"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "S108 is two checker defects, fixed; the criteria pass on the fixed checker and the applier's record was unchanged."
 }
]
```
