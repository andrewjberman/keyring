# IRPT_DASHBD: CVO adjudication, round 149 (eight orders, ~D2): the second Cottonwood publish pair applied, the claim writers, the history-scope cells

<sweep_watermark>2026-10-16T11:34Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T11:34Z, on msg 9294 (shared packet @893151b5c8, blob 41f79407a6). Round 149's orders, all in HEAD: DB-b-289 (CONTRACT), 290 (PUBWRITE), 291 (PUBAPPLY, WORLD), 292 (PUB49F), 293 (HISTSCOPE), 294 (HSPROD), 295 (HSPUB), 296 (HSRW). No judgment criterion in any of the eight, so NO L9 is owed or given. Re-run on the landed tree (HEAD 2dc8960628): 17 of 24 PASS (DBC159-1-AC1, -2-AC1; DB160-1 to DB164-1, all fifteen). The 7 failures are each a pin that a later order moved: DB157-1-AC1 (source contract 0.4.5 -> 0.4.6), AC2 and AC3 (the earlier-test line ceiling, read 40 against 28); DB158-1-AC1..AC3 ('another entry changed: irpt-49f-reporting-publish-lambda', moved by DB-b-292); DBC159-3-AC1 (the repo series contract is 0.3.3, not 0.3.2). None was re-run at its own drain. Every AWS read below is read-only, counts only. round-close --round 149 MAY-CLOSE. Struck DB118-3-AC3 still FAILS. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S77",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T11:34:00Z",
  "one_line": "Round 149 (~D2). (1) THE PUBLISH (DB-b-291): PAIR, OBJECTS, LEDGER, READERS. The pair packet NEVER_WIDEN_PACKET_COTTONWOOD_REPORTING_PUBLISH_CODE_UPDATE_SCHEDULE_REPUBLISH.md hashes to 77f0af99d2bb at HEAD; the COO half (d20bc88608) and the CTO half (ed74d5520d) both read SIGNED and name that hash, and the packet carries both branches and a rollback. irpt-cot-reporting-publish-lambda was modified at 2026-10-16T08:55:10Z. The prefix holds 1,878 current objects (939 series, 939 manifests), written 09:02:36Z..09:04:07Z, the same 1,878 keys as before; 1,882 noncurrent versions keep every prior version (rollback per key); 0 delete markers. The ledger is CLOSED at 70d34611f0; across 75 worktrees only 4 branches cut earlier still carry the first publish's old entry. The schedule is DISABLED. NO SERVED READER: irpt-cot-reporting-read-lambda does not exist, and the 49F read Lambda's directory map names 49financial only, so this is not client-facing. (2) income_claim BY VALUE: all 939 series carry income_claim 'absent' (no income entry is non-null), and the contracts now give the fixed reason RETURN_METHOD_DOES_NOT_SEPARATE_INCOME (source 0.4.6, series 0.3.3). v132's false 'source reports no income' is CORRECTED: the claim now names the method, which is true. S104 is RESOLVED on its wording. A product question remains for the CTO: Cottonwood's source carries non-zero Income on 343,256 rows (v132) that this method does not use. (3) v132's OTHER TWO: one drain is met for the income claim (ff6c0633a7) but NOT for history_scope. Contract 0.4.6/0.3.3 (DB-b-293, 10:36:44Z), the producers that write it (DB-b-294, 10:38:12Z) and the publisher (DB-b-295, 10:47:04Z) landed in three drains over 11 minutes. The PORTAL COPY is still behind: SERIES_OPTIONAL on origin/DEV lists 6 names, the series contract 8 (history_scope_claim and history_scope_basis added), so iv-e-124 stays red and W225-S1/S2 stay ARMED. (4) NO L9: no order declares a judgment criterion. (6) 49F AND HISTORY_SCOPE ARE DRAINED, NOT DEPLOYED: irpt-49f-reporting-publish-lambda last modified 2026-10-03, irpt-49f-reporting-gold-lambda 2026-10-15T11:49Z, irpt-cot-reporting-gold-lambda 2026-10-15T22:46Z. The 49F series state no unreported days and no gold row carries a derived scope yet. (5) DISPOSITIONS: S104 resolved (2); S99 dismissed (the ledger CLI lacks an add-leg verb, a tooling gap); S114 dismissed (a gate reading stale sentinel copies, iam.tf fmt inside a pinned file, the calendar fallback that fails closed after 2027-12-31, as W226-S1); W235-S1, S2, S4, S5, W236-S1, S2, W238-S1, S2 and W239-S1 accepted as the issuer's own defects, ruled by amendments with the gate limb stated; W235-S3 accepted as standing (the 49F lambda passes no contract; the checker validates against the contract instead).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S99",
   "IRPT_DASHBD-D2-S104",
   "IRPT_DASHBD-D2-S114",
   "IRPT_DASHBD-D2-W235-S1",
   "IRPT_DASHBD-D2-W235-S2",
   "IRPT_DASHBD-D2-W235-S3",
   "IRPT_DASHBD-D2-W235-S4",
   "IRPT_DASHBD-D2-W235-S5",
   "IRPT_DASHBD-D2-W236-S1",
   "IRPT_DASHBD-D2-W236-S2",
   "IRPT_DASHBD-D2-W238-S1",
   "IRPT_DASHBD-D2-W238-S2",
   "IRPT_DASHBD-D2-W239-S1"
  ],
  "spec_asserts": "CLAUDE.md NEVER rules (served output moves only under a signed never-widen pair with both branches and a rollback per key); CTO msg 8735 (one drain); A value must carry its claim and the claim must be true.",
  "world_is": "939 Cottonwood series are re-served under publisher 0.3.0 with the claim and calendar source, no reader, schedule DISABLED. The 49F and history-scope code is on trunk only. The portal mirror lags the series contract by two optional fields.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T11:1xZ at HEAD 2dc8960628: 17 of 24 PASS; the 7 failures name later pins (0.4.6, 0.3.3, the 49F entry, the line ceiling)",
    "sha256 NEVER_WIDEN_PACKET_COTTONWOOD_REPORTING_PUBLISH_CODE_UPDATE_SCHEDULE_REPUBLISH.md = 77f0af99d2bb...; COO half d20bc88608 and CTO half ed74d5520d SIGNED, naming 77f0af99d2bb28cd...",
    "read-only list-objects-v2 / list-object-versions on opal-data-cottonwood irpt/cottonwood/platinum/reporting/: 1,878 current, 1,882 noncurrent, 0 delete markers, 09:02:36Z..09:04:07Z; every series income_claim 'absent', 0 non-null income entries, 939 manifests calendar_source fallback_2010_2027, publisher_version 0.3.0",
    "lambda get-function-configuration: cot publish 2026-10-16T08:55:10Z; 49F publish 2026-10-03T17:22:27Z; 49F gold 2026-10-15T11:49:38Z; cot gold 2026-10-15T22:46:41Z; irpt-cot-reporting-read-lambda ResourceNotFound; 49F read map 49financial only",
    "git show -s --format=%cI: 9c46b7d536 10:36:44Z, 8430b776e6 10:38:12Z, 96a89eb451 10:47:04Z",
    "git -C portal origin/DEV src/pages/InvestorReporting/dashboard/seriesContract.ts SERIES_OPTIONAL (6 names) vs series contract 0.3.3 series.optional (8 names)",
    "git worktree list (75) and ls-tree .open_deploys: the closed codeupdate entry absent from the shared tree; 4 branch copies of the first publish entry"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "S104 is resolved by the corrected reason and the served claim; S99, S114 and the worker rows are tooling gaps or issuer defects ruled by amendment. The history_scope one-drain breach and the portal lag go to the CTO in the slug; W225-S1/S2 stay ARMED."
 }
]
```
