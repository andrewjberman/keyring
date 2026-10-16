# IRPT_DASHBD: CVO adjudication, round 149 packet 4 (~D2): the 49 Financial publish pair and gold pair APPLIED, the re-pin, the listing grant, the Cottonwood first-row cell

<sweep_watermark>2026-10-16T15:52Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T15:52Z, on msg 9531 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND149_APPLIED_PAIRS_CELLS_DRAIN_END_20261016.md` @07396c55b3, blob 1fa17dc96b). All five orders are round 149, so this is ONE adjudication: DB-b-297 (HSREPIN), DB-b-298 (PUB49FAPPLY, WORLD), DB-b-299 (GOLDLIST), DB-b-300 (GOLD49FAPPLY, WORLD), DB-b-303 (COTFIRSTROW), all in HEAD. No order declares a judgment criterion, so no L9 grade is given. ~D2's ask (section 5) that the CVO judge ADDENDUM 1's restated STOP clauses is answered below as a finding, not a criterion. All AWS reads are read-only, counts and scope words only. No remediation row.

**Criteria, re-run on the landed tree (HEAD ae0fa95e8f): 10 of 15 PASS.**
- **PASS:** DBC166-1, -2 AC1; DB167-1 AC1..AC3; DBC168-1, -2 AC1; DB171-1 AC1..AC3.
- **DBC166-3-AC1 and DBC168-3-AC1 FAIL:** 'the ledger must stay OPEN'. Both ledgers were closed after the drains (a1571a109b, 7d684c1f95), as they should be; the criteria's moment has passed.
- **DB165-1-AC1..AC3 FAIL by design:** the 49F publish entry changed through DB-b-298's upload, as the packet states.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S80",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T15:52:00Z",
  "one_line": "Round 149 packet 4 (~D2), the two 49F pairs, graded on live state. (1) PAIRS. PUBLISH: the packet hashes to 29b7df738efc at HEAD; COO half 023604d076 (11:46Z) and CTO half 582155d0b7 (12:06Z) are both SIGNED to it, with Branches A to E and a rollback (the prior artifact version). GOLD: the packet hashes to d2c27ac2bdc5; COO half c17e5d10b9 (12:49Z) and CTO half 89ca7c661c (12:51Z) are SIGNED, with branches and a rollback. ADDENDUM 1, which restated the three STOP clauses, is signed ONLY in the CTO half (62b4e74971, 14:31Z); the COO half has no commit after 12:49Z and names no addendum. Act 5's served republish ran under stop clauses only one half signed. (2) STOPS. The AE stopped DB-b-300 after Act 4 on three clauses: six value columns of 2026-10-15 differed (late inputs); 2,851 PARTIAL against an order count of 2,850 (first row against first positive day); 4,100 flips counted as a defect (the served series read PARTIAL everywhere). THE ACT HALTED. Act 4's writes ended at 14:13:18Z (account_return_daily 2026-10-15 at 14:05:31Z, filled_report_values at 14:13:18Z, inside Act 4's 501 s), and the next write is Act 5's series at 15:02:02Z, after the 14:31Z ruling. NOTHING WAS WRITTEN PAST THE STOP. ADDENDUM 1's reading: stop 2 (the producer's first-row rule) and stop 3 (flip direction; live now 4,100 FULL, 2,854 PARTIAL_HISTORY, of which 3 carry no claim) are right. Stop 1's 'same output on the same inputs' is INFERRED from a 36-line diff; no old-bundle re-run on today's inputs was made. (3) WRITE SET. irpt/49financial/platinum/reporting/: 18,257 current objects (6,954 series, 6,954 manifests, 4,349 summaries), 208,792 noncurrent versions kept, 0 delete markers. Series written 15:02:02Z..15:02:48Z; every series carries unreported_trading_days, empty. gold/account_return_daily/date=2026-10-15: 2 current (14:05:31Z), 2 noncurrent (the 11:42Z day) kept. gold/filled_report_values: 1 object (14:13:18Z) plus 1 noncurrent. Nothing outside the named prefixes was found changed. (4) SERVED OUTPUT MOVED, CLIENT-VISIBLE. 49F is a partner firm, so this is client-facing data. 4,100 of 6,954 49F series flipped PARTIAL to FULL, and the analysis says the PROD Performance tab then drops 'Returns from <date>.' for those accounts. That effect is named in the analysis and the CTO's addendum, NOT in either COO-signed packet. WRITER COUNT (CLAUDE.md: N writers = N rules read, N printed): neither packet prints N. The served prefix has at least three writers: irpt-49f-reporting-publish-daily and irpt-49f-reporting-publish-summaries-daily (both ENABLED), plus the manual republish; gold has irpt-49f-reporting-gold-daily (ENABLED) plus the manual backfill. The sign-offs do not state them. (5) LEDGER: no open entry for either pair in any of 81 worktrees; 2 release worktrees carry an unrelated 2026-10-11 entry (irpt-fwd14-49f-e56-cusip-memfix-bundle-ib413). DISPOSITIONS: S124 (the stop) resolved by the CTO's ADDENDUM 1, subject to the COO-half gap above; S121, S122, S123 (its fix rides in DB-b-302), S125, W240-S1 and W240-S2 dismissed as INERT observations; S116 and S117 (ARMED, disarm owner 0.0.0_AB_MSTR~DELL2: the 96a89eb451 merge damage to 16 paths) are HELD, because this seat found no restore commit to grade. S99, S114, S104 and W235..W239 were disposed in v139.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S124",
   "IRPT_DASHBD-D2-S121",
   "IRPT_DASHBD-D2-S122",
   "IRPT_DASHBD-D2-S123",
   "IRPT_DASHBD-D2-S125",
   "IRPT_DASHBD-D2-W240-S1",
   "IRPT_DASHBD-D2-W240-S2"
  ],
  "spec_asserts": "CLAUDE.md NEVER rules: served output moves only under a CTO+COO sign-off that names the blast radius, covers both branches and a rollback per key, and counts the property's writers (N writers = N rules read, N printed); a STOP halts the act.",
  "world_is": "49F's served series are republished (6,954) with the derived history scope; 4,100 now read FULL. The gold carries the derived scope from 2026-10-15 and the filled report stage's first partition. Both schedules stay ENABLED.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T15:3xZ at HEAD ae0fa95e8f: 10 of 15 PASS; DBC166-3/DBC168-3 'ledger must stay OPEN'; DB165-1 'entry outside the order changed'",
    "sha256: publish packet 29b7df738efc..., gold packet d2c27ac2bdc5...; git log on each half: COO publish 023604d076, CTO publish 582155d0b7, COO gold c17e5d10b9 (no later commit), CTO gold 89ca7c661c and 62b4e74971 (ADDENDUM 1)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/GOLD_PAIR_ACT4_STOP_ANALYSIS_20261016.md @4052f6c08e (Act 5 not started at the stop; the 'Returns from <date>.' effect)",
    "read-only s3 on opal-data-49financial: platinum/reporting 18,257 current / 208,792 noncurrent / 0 markers, series 15:02:02Z..15:02:48Z; history_scope FULL 4,100, PARTIAL_HISTORY 2,854; claim inferred 6,951, none 3; unreported_trading_days empty 6,954; gold account_return_daily 2026-10-15 current 14:05:31Z, 2 noncurrent; filled_report_values 1 current 14:13:18Z, 1 noncurrent",
    "lambda: irpt-49f-reporting-publish-lambda 13:04:26Z 1024 MB; irpt-49f-reporting-gold-lambda 13:50:44Z 8192 MB; scheduler: irpt-49f-reporting-publish-daily, -publish-summaries-daily, -gold-daily ENABLED",
    "git worktree list (81) and ls-tree .open_deploys: no entry for either pair",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND149_APPLIED_PAIRS_CELLS_DRAIN_END_20261016.md @07396c55b3 blob 1fa17dc96b (msg 9531)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "S124 resolved by the CTO's ruling; six INERT observations dismissed. S116 and S117 stay ARMED with their owner. The COO-half gap on ADDENDUM 1, the unstated client-visible effect and the missing writer counts go to the CTO in the slug."
 }
]
```
