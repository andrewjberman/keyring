# IRPT_DASHBD: CVO adjudication, round 134 (workstream F-SHIP, ~F2): the per-row business-date claim (19th column), contract 0.5.0, with J1 and J2; the Inflection snapshot finding

<sweep_watermark>2026-10-16T16:34Z</sweep_watermark>

L8 compile, L9 grades and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T16:34Z, on msg 9595 and ~F2's correction msg 9623 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R134_F.md` @e1af2c8476, blob ac5ba87ddf). One order, TO-DB-f-2001, merged in ONE drain be82803a49, in HEAD. Re-run on trunk (HEAD 2a4139a74f): DBF134-1-AC1, AC2, AC3 PASS. The figure-bearing samples (org/mcp/drive_ticks/R134_SAMPLE_*_20ROWS.json) are untracked and git-ignored; nothing below carries a client value. All AWS reads are read-only, counts only. No remediation row.

**L9 -- DBF134-1-J1: PASS** (Inflection, 20 of 20), by natural key over Complete rows.
- **Uniqueness and source blocks:** each sampled key is unique in its own partition, and every source block equals the live row.
- **Every contract field re-derives,** 20 of 20, including business_date_claim. The rolled line (row 12) reads 'inferred'; the 19 measured lines read 'measured'.
- **Census, scoped:** this seat's census covered the 20 sampled partitions plus 5 seeded others, 25 of 155: 31,306,140 Complete rows, 167,449 in 77,073 non-unique keys.
- **Census, latest snapshot:** re-scoped per msg 9623 to the LATEST snapshot alone (date=2026-10-16): 1,336,782 Complete rows, 6,566 in 3,017 non-unique keys. This equals ~F2's R135 figures exactly.
- **Not comparable:** ~F2's packet printed totals only, not per-partition counts, so a per-partition comparison could not be made.

**L9 -- DBF134-1-J2: PASS** (49 Financial, 20 of 20).
- **Census, full:** 573 partitions, 3,354,885 rows, 21,236 in 10,027 non-unique keys, equal to ~F2's.
- **Uniqueness and source blocks:** 20 of 20 keys are unique in partition, and every source block equals the live row.
- **Every field re-derives,** 20 of 20, including the claim. The rolled line (row 4) reads 'inferred', and the UNMAPPED_BY_TABLE line is counted, not dropped.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S81",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T16:34:00Z",
  "one_line": "Round 134 F-SHIP (~F2): AC1..AC3 PASS. L9 DBF134-1-J1 PASS, 20 of 20 (Inflection). L9 DBF134-1-J2 PASS, 20 of 20 (49F). THE CLAIM COLUMN answers v142: business_date_claim is the 19th column on all three producers, and the rolled lines read inferred and the measured lines measured, in both samples. Contract 0.5.0 (business_date now 'inferred' with business_date_claim as its per-row claim; schema hash 58790f62fe63c9ca -> ac652e2f71b18427) landed in ONE drain with the three producers and their tests (be82803a49): one drain met. ROUND 132's stale AC3 proof (v142) is REFRESHED: round-close --round 132 now reads proof_ok=1, MAY-CLOSE. ROUND 133 (TO-DB-f-1901, contract 0.4.2, S6 RULED_INTERNAL) is complete with no L8 packet in ~F2's folder, and a packet is owed for it (CTO msg 8841: a packet at every drain). THE INFLECTION SNAPSHOT FINDING (msg 9623), tested here. Each fact_transactions partition is a CUMULATIVE snapshot, not a day's transactions. The latest (2026-10-16) holds 1,336,782 Complete rows with transDates from 2020-06-03 to 2026-10-15; all 1,336,580 Complete ids of 2026-10-15 recur in it. The PRODUCER is pure and does NOT de-duplicate: normalize_trn on one seeded account gives 2,640 rows from the latest snapshot alone (equal to the account's 2,640 Complete source rows) and 5,280 from the latest plus the previous snapshot unioned. A wiring that unions partitions would emit every transaction once per snapshot, about 140 times over the table. The B-IN adapter's flows_of has the same exposure: it sums flows over whatever frame it is given, and it has no production caller today. NEITHER IS WIRED. The rule the wiring must carry is ONE snapshot, the latest, per run; it should be a criterion of the release pair. CORRECTION TO v140, v142 AND THIS GRADE'S SCOPED CENSUS: those Inflection duplicate totals summed partitions as if disjoint, so they are snapshot-weighted (about 140 copies of each transaction), not transaction counts. 1,036,824 rows in 477,446 keys (v140) and 134,332 in 61,844 (v142) count (snapshot, key) pairs. The per-row grades stand, because each sampled row's key was unique within its own snapshot. The transaction-level figure is the latest snapshot's: 6,566 rows in 3,017 non-unique keys of 1,336,782. Dismissed (2): D2-W2001-S1 (the class test does not collect in a sparse worktree), D2-W2001-S2 (a channel folder not materialised).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W2001-S1",
   "IRPT_DASHBD-D2-W2001-S2",
   "IRPT_DASHBD-D2-C-S75",
   "IRPT_DASHBD-D2-C-S79"
  ],
  "spec_asserts": "Spine L9; CTO msg 9193 (natural key, unique within the row's own partition); CTO msg 9498 ruling 1 (per-row business-date claim); CTO msg 8735 (one drain); a denominator's scope must equal the claim's population (rule 24 (i)).",
  "world_is": "Contract 0.5.0 and three producers on trunk, unwired and unserved. Inflection's silver is a daily cumulative snapshot, and the producer emits whatever frame it is handed without de-duplication.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T16:xxZ at HEAD 2a4139a74f: DBF134-1-AC1, AC2, AC3 PASS",
    "J2 grader: 49F 573 partitions, 3,354,885 rows, 21,236 in 10,027 non-unique keys; 20 of 20 unique and matching every field incl. business_date_claim; row 4 rolled",
    "J1 grader: 25 of 155 partitions, 31,306,140 Complete rows, 167,449 in 77,073 non-unique keys; 20 of 20 unique and matching every field incl. business_date_claim; row 12 rolled",
    "snapshot test (read-only): latest 2026-10-16 1,336,782 Complete rows, transDate 2020-06-03..2026-10-15; 1,336,580 of 1,336,580 previous-day Complete ids present; latest non-unique 6,566 rows in 3,017 keys; producer normalize_trn on one account: 2,640 (latest) vs 5,280 (latest + previous)",
    "git diff be82803a49^1 be82803a49: contract 0.5.0 and account_transaction*.py plus their tests in one merge; contract schema_hash ac652e2f71b18427..., 19 columns",
    "round-close-check --round 132 --workstream ~F2: proof_ok=1, MAY-CLOSE; --round 133: TO-DB-f-1901 complete, no L8_PACKET_R133 in deliverables/2.0.0_SA_COO~F2",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R134_F.md @e1af2c8476 blob ac5ba87ddf (msgs 9595, 9623)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two INERT worker rows. C-S75 and C-S79 are cited to correct their snapshot-weighted Inflection census totals; their grades stand. The one-snapshot rule for the wiring and the owed round-133 packet go to the CTO in the slug."
 }
]
```
