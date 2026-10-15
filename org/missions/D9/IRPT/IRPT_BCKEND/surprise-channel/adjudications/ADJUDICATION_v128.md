# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PN, the Scope account feed and the one-account limit lifted)

<sweep_watermark>2026-10-15T17:54Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T17:54Z, on msg 8509 (the shared packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL1_PJ2_PJ3_PN1_DRAIN_END_20261015.md` @9ac52f5198; this file grades ~PN r1). Two orders, complete. IB-pr-586 (the Scope account feed, risk LOCAL) merged @7b150e672a and was amended twice: `data/inf/manual_api/pull_inflection_scope_account_returns.py`, its test, and `data/inf/scripts/gold/orion-gold-dispatch.sh`. IB-pr-587 (the household lift, risk WORLD by path) merged @50c41a28c2: `infra/aws/lambda/investor-reporting/performance/orion_account_mapping.py` and two tests. Re-run here at HEAD: IB223-1-AC1..AC3 and IB223-2-AC1..AC3, 6 of 6 PASS (exit 0 each). `round-close-check --round 1 --workstream "~PN"`: orders=2, proofs 2 of 2 ok, verdict=MAY-CLOSE.

**(3) "The Scope feed is built": repository only, nothing deployed. Read live here.**
- The feed script is NOT on the runner's code paths. `s3://opal-data-inf/code/manual_api/pull_inflection_scope_account_returns.py` and `code/gold/pull_inflection_scope_account_returns.py` both return 404.
- The chain catalog the runner executes, `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh`, still reads LastModified 2026-08-30T14:03:13Z (113,320 bytes). The repository copy changed at the merge (2026-10-15T17:08Z), and the S3 object did not.
- `irpt-performance-adapter` (which packages `orion_account_mapping.py`) was last modified 2026-10-13T12:51:39Z. Its deployed `orion_account_mapping.py` equals the pre-merge bytes (`50c41a28c2^1`) and differs from HEAD.

The apply is IB-pr-596 (pending) and waits on IB-pr-594 (the daily factor).

**Apply-time checks, and one packet claim that does not hold as written.** The packet says worker rows W429-S2 to S7 are "apply-time checks, listed in the apply order". IB-pr-596's text names W429-S2 and W429-S3 by id, but not S4 to S7. Two of the unnamed ones matter at apply:
- **W429-S4:** the feed imports `lib/` and the INF_B_00 builder by path, and the chain syncs only four `code/` prefixes, so the feed may fail to import on the runner.
- **W429-S5:** a persistent 429 stops the run, but a partial bronze key is then skipped forever by the absent-first rule.

Recommend (P1, to the issuer) that IB-pr-596 name W429-S4..S7 or show where its text covers them before the apply is cut final. Held also: `D2-W430-S3` (ARMED, `~P2`). `orion_selected.py` line 11 still states the mapping refuses any multi-account household, which the lift made untrue; a stale guard comment beside a live consumer guard.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S36",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T17:54:00Z",
  "one_line": "~PN r1. Scope account feed and household lift built, repository only; nothing deployed, read live: the feed script is absent from code/manual_api and code/gold (404), the runner's catalog code/gold/orion-gold-dispatch.sh is unchanged since 2026-08-30 while the repo copy changed, and irpt-performance-adapter (2026-10-13) carries the pre-merge orion_account_mapping.py. 6 of 6 criteria PASS re-run. The packet says W429-S2..S7 are listed in the apply order; IB-pr-596 names S2 and S3 only, and S4 (imports outside the synced prefixes) and S5 (a partial key skipped forever after a 429 stop) matter at apply. Dismissed (5): D2-W429-S1, -S2, -S3, -S6, D2-W430-S1 (readings or apply-time checks named in IB-pr-596). Held: D2-W429-S4, -S5, -S7, D2-W430-S2 (the RECORD FACE reached the worker, as W431-S1 and W432-S1: a dispatch defect for ~P2), D2-W430-S3 (stale guard comment).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W429-S1",
   "IRPT_BCKEND-D2-W429-S2",
   "IRPT_BCKEND-D2-W429-S3",
   "IRPT_BCKEND-D2-W429-S6",
   "IRPT_BCKEND-D2-W430-S1"
  ],
  "spec_asserts": "Signed pair (b) addendum 1 (the Scope feed: one call per household, calcGrossOfFees false, fee_basis NET, ABSENT never a zero); CLAUDE.md rule 22a (deployed bytes against the build input).",
  "world_is": "The Scope feed and the household lift exist in the repository only. The runner, the S3 catalog and the performance adapter still run the old bytes. Before the apply: IB-pr-594, and the apply order must cover the runner import path (W429-S4) and partial-key handling after a throttle stop (W429-S5).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T17:4xZ of the invocations in IB-pr-586 and IB-pr-587: IB223-1-AC1..3, IB223-2-AC1..3 PASS, exit 0 each; round-close-check ~PN round 1 MAY-CLOSE",
    "git diff --name-only 7b150e672a^1 7b150e672a and 50c41a28c2^1 50c41a28c2 (product paths listed above)",
    "aws s3api head-object opal-data-inf code/gold/orion-gold-dispatch.sh: 2026-08-30T14:03:13Z 113320; code/manual_api|code/gold/pull_inflection_scope_account_returns.py: 404",
    "aws lambda get-function irpt-performance-adapter: LastModified 2026-10-13T12:51:39Z; deployed orion_account_mapping.py equal to 50c41a28c2^1, differs from HEAD",
    "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-596.apply-scope-account-feed.md: status pending; names W429-S2 and W429-S3",
    "investigation rows D2-W429-S1..S7, D2-W430-S1..S3",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_PL1_PJ2_PJ3_PN1_DRAIN_END_20261015.md @9ac52f5198 (msg 8509)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Readings and apply-time checks the apply order names. The unnamed apply-time risks and the stale guard comment are held."
 }
]
```
