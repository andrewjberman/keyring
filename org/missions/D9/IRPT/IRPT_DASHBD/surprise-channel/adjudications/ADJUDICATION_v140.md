# IRPT_DASHBD: CVO adjudication, round 131 (workstream F-SHIP, ~F2): the key normalisation, contract 0.4.0, the Inflection producer, with J1 and J2

<sweep_watermark>2026-10-16T11:59Z</sweep_watermark>

L8 compile, L9 grades and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T11:59Z, on msg 9289 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R131_F.md` @67996afab9, blob 9078735dce). (Version v137 was left unused; this round is graded here.) One order, TO-DB-f-1701, merged in one drain 4613e3079a, in HEAD. Re-run on trunk (HEAD 0fca1cd683): DBF131-1-AC1, AC2, AC3 PASS.

SAMPLES AND CLIENT DATA:
- The committed samples beside the packet (J1_SAMPLE_COTTONWOOD_R131_HASHED.json, J2_SAMPLE_INFLECTION_R131_HASHED.json, and the earlier J1_SAMPLE_49F_R129_HASHED.json) ARE tracked in git. They hold no client value: per row, the day, the sha256 of the natural key, the words and booleans.
- The figure-bearing samples (org/mcp/drive_ticks/R131_SAMPLE_COTTONWOOD_20ROWS.json, R131_SAMPLE_INFLECTION_20ROWS.json) are untracked and git-ignored.
- Nothing below carries a client value.

All AWS reads are read-only, counts and code values only. No remediation row.

**L9 -- DBF131-1-J1 (Cottonwood): PASS, 20 of 20,** by natural key (account, trade date, type | sub type | action, symbol, units, Market Value; CTO msg 9193).
- **Duplicate census, recounted here:** 1,096,830 rows in 125 partitions; 37,478 rows in 18,501 non-unique keys (equal to ~F2's).
- **Uniqueness:** 20 of 20 sampled keys are unique in their partition.
- **Source blocks:** every one equals the live row.
- **Every contract field re-derives** from the live row and contract 0.4.0, 20 of 20: type and action by the pair and Action mapping through normalise_key; flow class by External Flow and the pair; amount by WORD_SIGN; fee (Transaction Fee + Account Fee); business_date (the first NYSE trading day on or after the Trade Date); custodian lower-cased; symbol, asset name and id stripped; source_action_raw as received.
- **The v136 case, re-run:** a live row with Action 'CREDIT - ' now finds its mapping row and reads UNMAPPED_BY_TABLE (the table maps that Action to UNMAPPED), not CODE_NOT_IN_MAPPING. All three padded values ('Buy Money Market ', 'CREDIT - ', 'OTHER - ') find their rows through normalise_key.

**L9 -- DBF131-1-J2 (Inflection): PASS, 20 of 20,** by natural key (account, trade date, description, symbol, units, amount) over Complete rows.
- **Duplicate census, recounted here over all 154 partitions:** 191,360,953 Complete rows; 1,036,824 rows in 477,446 non-unique keys (equal to ~F2's).
- **Uniqueness and source blocks:** 20 of 20 sampled keys are unique in their partition, and every source block equals the live row.
- **Every contract field re-derives:** type and action by the description mapping; flow class from the mapping row; price navPrice (null where units are zero or navPrice is not positive); amount transAmount; business_date and trade_date the transDate; custodian lower-cased; settle_date and fee null.
- **Limit:** the draw covers 6 distinct descriptions; per-description coverage (48 of 48) is the checker's, not the sample's.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S75",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T11:59:00Z",
  "one_line": "Round 131 F-SHIP (~F2): AC1..AC3 PASS; J1 PASS 20/20 (Cottonwood), J2 PASS 20/20 (Inflection); both duplicate censuses reproduced exactly. ~F2's FOUR DECISIONS: none is covered by a CTO ruling (the F-SHIP round analyses 120 to 130 name none of them). All four shape what the release will serve, so each is HELD for the CTO before the never-widen release. (a) COMPLETE ROWS ONLY: 26,693,399 of 218,054,352 Inflection rows (12.2 percent) excluded, recounted here over all 154 partitions. The excluded statuses are Rejected 13,991,249, Pending 12,542,026, Reversed 159,200, Pending Corporate Action 616 and Inactive 308. It is carried as a claim (the contract's row_filter, counted per status; an unknown status refused), but whether a Reversed original and its reversal both drop out is unestablished. (b) PRICE FROM navPrice: in 10 seeded partitions, all 10,019,687 unit-bearing Complete rows carry a fund family, and 10,016,828 (99.97 percent) have navPrice x noUnits within 1 percent of transAmount. NO non-fund unit-bearing row exists in that set, so navPrice's validity for a non-fund security cannot be tested here; carried as inferred with a method. The contract's earlier avgPrice is null on every row (~F2's own finding). (c) business_date = transDate: in the same 10 partitions, 20,231 of 12,377,639 Complete rows (0.16 percent) fall on a day that is not an NYSE trading day. Inflection writes those as the business date, while Cottonwood rolls to the next trading day, so the firms disagree on what a business date is. (d) FLOW CLASS BY TAXONOMY BUCKET: W1701-S6 is ARMED with the CTO as disarm owner (Dividend Paid from Cash and Income Paid read INTERNAL while Dividend to Cash reads INCOME); held. Dismissed (6): D2-W1701-S1, S2, S3, S4, S5, S7 (sparse folders; the ground read still names avgPrice; a labelled refusal; a commit trailer; a coverage sentence; a naming WARN fixed). S102, S103, S106 and S107: all three producers now have a PASSing L9 (49F v135, Cottonwood and Inflection here), but the release and wiring are not done; whether S103 disarms now is the CTO's reading of S107.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W1701-S1",
   "IRPT_DASHBD-D2-W1701-S2",
   "IRPT_DASHBD-D2-W1701-S3",
   "IRPT_DASHBD-D2-W1701-S4",
   "IRPT_DASHBD-D2-W1701-S5",
   "IRPT_DASHBD-D2-W1701-S7"
  ],
  "spec_asserts": "Spine L9 (judgment graded on artifacts); CTO msg 9193 (natural key, unique keys only, census printed, no locator); CTO msg 9245 (one key function; source_action_raw); an unruled decision that will move served data is held for the CTO.",
  "world_is": "Contract 0.4.0 and three producers on trunk, unwired and unserved; the two sampled producers equal the source on unique-key rows. Four Inflection and cross-firm decisions await a ruling before release.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T11:xxZ at HEAD 0fca1cd683: DBF131-1-AC1, AC2, AC3 PASS",
    "J1 grader (read-only, counts and field names): Cottonwood census 1,096,830 / 37,478 / 18,501; 20 of 20 unique and matching every field",
    "producer _classify on a live 'CREDIT - ' row: ('UNMAPPED', None, 'INTERNAL', 'UNMAPPED_BY_TABLE'); normalise_key finds all three padded Actions",
    "J2 grader: Inflection Complete census 191,360,953 / 1,036,824 / 477,446; 20 of 20 unique and matching every field",
    "Inflection status over 154 partitions: Complete 191,360,953; Rejected 13,991,249; Pending 12,542,026; Reversed 159,200; Pending Corporate Action 616; Inactive 308; total 218,054,352",
    "10 seeded partitions: unit-bearing Complete rows 10,019,687, all fund-family, 10,016,828 within 1 percent; Complete rows 12,377,639, 20,231 on non-trading days",
    "git ls-files: the three *_HASHED.json samples tracked (no client values); org/mcp/drive_ticks/R131_SAMPLE_*_20ROWS.json git-ignored",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R131_F.md @67996afab9 blob 9078735dce (msg 9289)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Six INERT worker rows. W1701-S6 and decisions (a) to (d) are held for the CTO, not dismissed."
 }
]
```
