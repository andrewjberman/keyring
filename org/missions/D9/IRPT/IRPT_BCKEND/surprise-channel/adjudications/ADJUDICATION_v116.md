# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PE, 49 Financial's candidate screen run offline)

<sweep_watermark>2026-10-15T12:26Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T12:26Z, on msg 8273 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PE_DRAIN_END_20261015.md` @e77a090497). ~PC round 2 and ~PD round 1 were already compiled and slugged as ADJUDICATION_v114 @a6f2db4f50 and ADJUDICATION_v115 @aadb84c1c9. One order, IB-pr-573 (risk SERVED, read-only, gate run offline on synthetic nodes), complete, merged @dbfd95217d (worker record, criteria output, proof instance and the channel only), issued @8d6cf63777. Re-run here at HEAD: IB212-1-AC1..AC3 PASS (exit 0). `round-close-check --round 1 --workstream "~PE"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE.

**The source gap, verified from the partitions themselves** (read-only `list` and `get-object` of `s3://opal-data-assets/schwab/08335338/silver/dim_balance/`, the builder's source, `holdings_49f.py:60-61, 218`; counts only, no id printed or recorded):

| partition | rows | distinct accounts | LastModified (UTC) |
|---|---|---|---|
| date=2026-10-12 (served) | 7,640 | 7,640 | 2026-10-13T09:46:42Z |
| date=2026-10-13 (candidate) | 7,646 | 7,646 | 2026-10-14T09:46:39Z |
| date=2026-10-14 (today's candidate) | 7,664 | 7,664 | 2026-10-15T09:46:42Z |

On 2026-10-12 and absent on 2026-10-13: **exactly 1** account. That matches the refusal's `account_lost` count 1 and the worker's one row on 10-12 and none on 10-13. Present on both days: 7,639. Positive control: an account drawn from that set, present on 10-12, reads present on 10-13. New on 10-13: 7. **The missing account is still absent on 2026-10-14** (0 of 1 returned). So the refusal will NOT clear on its own at today's fire, and the packet's "next read" is answered here. Limit: this seat matched the gap by count against the 10-12 served date, not by reading the refusal record's id. The set difference is a single account, so the identification is by uniqueness.

**This supersedes v114's "49 Financial cause inferred".** The 49F refusal is now known to be a source gap: the account is absent from the custodian's dim_balance partition on the candidate date (MEASURED, here and by the worker). It is not a builder filter. The builder iterates the partition's keys (`holdings_49f.py:356`) and never sees the account. What stays inferred is WHY Schwab's partition omits an ACTIVE account. It differs from Cottonwood's measured cause (no-position rows, empty custody frame, line 403), so one screen fix does not cover both firms.

**S192's held disposition and the owner.** S192 stays ARMED and its 49F half changes class: from "omitting filter unread" to "source gap on 10-13 and 10-14, reason unread". The disarm owner is `2.0.0_SA_COO~P2`. S193 ruled that for S158 and S192, and **S196 now aligns W413-S1 and S194 to the same one owner, closing v114's finding.** S197 (ARMED, owner `~P2`) carries the source gap. Who can REMEDY it is not ~P2. A re-landed custody row for 10-13 and 10-14 is an act on the Schwab silver ingest, upstream of IRPT_BCKEND, and its producer's owner must confirm whether the account is live at the custodian. Otherwise a custodian-confirmed TERMINATED mark is the remedy. ~P2 owns the disarm and must route the remedy to the ingest owner; nothing yet names that seat.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S24",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T12:26:00Z",
  "one_line": "Round 1 ~PE. 49 Financial's lost ACTIVE account is a SOURCE GAP, verified here from s3://opal-data-assets/schwab/08335338/silver/dim_balance: exactly 1 account present on 10-12 (7,640) is absent on 10-13 (7,646), positive control present on both, and it is STILL absent on 10-14 (7,664), so today's fire will not clear the refusal. No builder filter drops it (holdings_49f.py:356 iterates the partition). Supersedes v114's 'cause inferred' for 49F; why Schwab omits it stays inferred. IB212-1-AC1..AC3 PASS re-run; read-only. S196 gives W413-S1 and S194 one owner (~P2), closing v114's finding. Dismissed (4): D2-W416-S1 (the order's premise fails, by measurement), D2-W416-S2 (reading), D2-W413-S1 (resolved as to cause), D2-S196 (owner ruling). Held: D2-S192, D2-S197 (ARMED, ~P2; the remedy sits with the Schwab silver ingest owner, not yet named).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W416-S1",
   "IRPT_BCKEND-D2-W416-S2",
   "IRPT_BCKEND-D2-W413-S1",
   "IRPT_BCKEND-D2-S196"
  ],
  "spec_asserts": "A value must carry its claim (CLAUDE.md section 4): measured where the partition was read, inferred where the custodian's reason is unread; NEVER trust a producer's self-report, verify against the artifact (section 4); an ARMED hazard disarms via one disarm_owner (section 2).",
  "world_is": "49 Financial (the P1 firm) is served at 2026-10-12 and refused on account_lost for one ACTIVE account that the custodian's dim_balance dropped on 10-13 and still lacks on 10-14; it will be three trading days behind after today's fire unless the source is corrected or the account is confirmed closed. Cottonwood's block has a different, measured cause. The remedy for 49F needs the Schwab silver ingest owner.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T12:2xZ of the invocations in IB-pr-573: IB212-1-AC1..3 PASS, exit 0",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 1 --workstream ~PE: orders=1 proof_ok=1 judgment=0 verdict=MAY-CLOSE",
    "scratch pe_balance.py, read-only, s3://opal-data-assets/schwab/08335338/silver/dim_balance/date=2026-10-12|13|14/data.parquet: 7,640 / 7,646 / 7,664 distinct account_id; 10-12 minus 10-13 = 1; 10-13 minus 10-12 = 7; both = 7,639; positive control True; the 1 absent on 10-14",
    "data/assets/scripts/gold/investor_reporting/holdings_49f.py:60-61 (SOURCE_BUCKET, SCHWAB_PREFIX), :218 (dim_balance read), :356 (the loop over balance.index)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~416/IB212-1_49f_screen_offline_read.json: source_rows count 1 on 10-12, none on 10-13; failing_condition account_lost measured at holdings_snapshot.py:3058",
    "investigation rows D2-S192, D2-S193, D2-S196, D2-S197, D2-W413-S1, D2-W416-S1..S2",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PE_DRAIN_END_20261015.md @e77a090497 (msg 8273)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A failed order premise replaced by a measurement, a reading, a cause now measured, and an owner ruling. The 49F refusal stays held on S192 and S197 with ~P2, its remedy to be routed to the Schwab ingest owner."
 }
]
```
