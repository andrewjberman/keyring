# IRPT_DASHBD: CVO adjudication, round 136 (workstream F-SHIP, ~F2): the 49 Financial gold handler emits the transaction day; L9 DBF136-1-J1 and DBF136-1-J2; S6 as finally ruled; round 135 owes a packet

<sweep_watermark>2026-10-16T22:45Z</sweep_watermark>

L8 compile, L9 grades and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T22:45Z, on msg 9937 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R136_F.md` @7a83fc36e1). Orders TO-DB-f-2201, 2202 and 2203, all complete.

**Mechanical criteria, re-run on trunk (HEAD 6b6c16b492):** all seven PASS.
- DBF136-1-AC1, AC2, AC3.
- DBF136-2-AC1, AC2.
- DBF136-3-AC1, AC2.

**The figure files:**
- They are untracked and git-ignored. Their sha256 prefixes and byte counts equal the packet's: J1 da1e316f9320b42f (25,890 bytes) and J2 09c3cba8dbae5cd8 (31,767 bytes).
- The committed hashed forms also match: ee9848707ea98dde and 8c5c6d22551f58c5.
- Nothing below carries a client value. All AWS reads were read-only.

No remediation row.

**L9 -- DBF136-1-J1: PASS** (Inflection, 20 of 20), graded by natural key within the ONE newest snapshot (date=2026-10-16).
- **Census of that snapshot (this seat's):** 1,521,297 rows, of which 1,336,782 are Complete. Complete rows in non-unique keys: 6,566, in 3,017 keys. Every figure equals the packet's, per status included.
- **Uniqueness and source blocks:** 20 of 20 sampled keys are unique, and every source block equals the live row.
- **Re-derivation:** every one of the 19 columns re-derives from contract 0.5.1, 20 of 20. That includes business_date_claim: 19 rows read measured and 1 rolled row reads inferred.
- **The landed launcher's own plan (run by this seat, no emit):** 1,336,781 rows out, 1 OFFSET_OF_REVERSED. It printed "S6: 96 of 96".

**L9 -- DBF136-1-J2: PASS** (49 Financial, 20 of 20).
- **Census, full:** 573 partitions, 3,354,885 rows; 21,236 rows in 10,027 non-unique keys. This equals the packet's.
- **Rows:** 20 of 20 keys are unique in their partition. Every field and the claim re-derive, with 1 rolled row reading inferred.

**(1) One snapshot per run (v144's trap):**
- **In code:** the trap is closed. `INF_G_01` reads only the newest date= partition not after the run day.
- **Shown on one sampled account:** the producer emits 646 rows. The newest snapshot holds 646 Complete lines. The newest two snapshots together hold 1,292, which a union would emit.
- **Limit:** this is code on trunk; it is not wired or deployed.

**(2) S6:**
- **The premise is outdated.** msg 9649's EXTERNAL ruling was itself WITHDRAWN by msg 9669 (ADDENDUM 2 of the round-134 analysis @5d8adf5722).
- **The final ruling:** both legs are INTERNAL, as a reinvestment.
- **Contract 0.5.1 matches it in its three places:**
  - `s6_ruling`: pin 5d8adf5722, with withdrawn_pins 1881c0fc01 and a5475b2fdd, and the 96-event counts.
  - `s6_status`: RULED_INTERNAL_REINVESTMENT. The exact value "RULED_INTERNAL" appears 0 times.
  - `source_mapping[184]` and `[185]`: INTERNAL.
- **The producer agrees:** its output holds 96 "Dividend Paid from Cash" rows and 96 "Income Paid" rows, all INTERNAL.
- **So the 96 do not read EXTERNAL,** and they should not.

**(3) Round 135 owes a packet.**
- Its three orders, DB-f-2101, 2102 and 2103, are complete, not direct acts, and carry 0 judgment.
- No L8_PACKET_R135_F.md exists, and no slug has been sent for that round.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S83",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T22:45:00Z",
  "one_line": "Round 136 F-SHIP (~F2): 7 mechanical PASS. L9 DBF136-1-J1 PASS, 20 of 20 (Inflection, newest snapshot: 1,521,297 rows, 1,336,782 Complete, 6,566 in 3,017 non-unique keys). L9 DBF136-1-J2 PASS, 20 of 20 (49F, 573 partitions). One snapshot per run shown on one account: 646 out = 646 in the snapshot (two-snapshot union 1,292). S6 final is INTERNAL (msg 9669 withdrew 9649); contract 0.5.1 and producer agree, 96 and 96 INTERNAL. Round 135 owes a packet.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-C-S82"],
  "spec_asserts": "DBF136-1-J1 / J2 (TO-DB-f-2201): 20 sampled producer rows per firm against the source by natural key, 19 columns incl. business_date_claim, J1 from the ONE newest Orion snapshot with its census printed and the S6 'N of 96'. CTO msg 9669 (@5d8adf5722): Dividend Paid from Cash and Income Paid both INTERNAL, s6_status RULED_INTERNAL_REINVESTMENT, release criterion 96 of 96 equal-amount lines.",
  "world_is": "J1 20 of 20 unique and every field equal; snapshot census equals the packet's. J2 20 of 20; full census equals the packet's. Landed INF_G_01 plan on date=2026-10-16: rows_out 1,336,781, S6 96 of 96, producer S6 rows 96 + 96 all INTERNAL; one account 646 out vs 646 Complete in the snapshot vs 1,292 over the newest two. Contract 0.5.1: s6_ruling pin 5d8adf5722, s6_status RULED_INTERNAL_REINVESTMENT, [184]/[185] INTERNAL. Round 135 (DB-f-2101..2103, complete, 0 judgment, not direct acts) has no L8 packet.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_handler.py|p136_tf.py|p136_sourcemap.py . <id> -> 7 of 7 PASS at 6b6c16b492",
    "sha256 org/mcp/drive_ticks/J1_SAMPLE_INFLECTION_R136.json da1e316f9320b42f, J2_SAMPLE_49F_R136.json 09c3cba8dbae5cd8 (untracked, git-ignored)",
    "CVO grader (read-only S3 GETs) over orion/inflection/silver/fact_transactions/date=2026-10-16 and schwab/08335338/silver/fact_trn/ (573 partitions); counts and field names only",
    "data/inf/scripts/gold/INF_G_01.account_transaction_gold.py newest_partition/read_snapshot/plan/s6_report run read-only by this seat (no emit)",
    "org/mcp/inbox/2.0.0_SA_COO/~F2/read/20261016T165945Z_1.0.0_SA_CTO_DELL2__DECISION__S6_final__my_EXTERNAL_ruling_.md (Msg-ID 9669)",
    "org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json @6b6c16b492 contract_version 0.5.1",
    "python -I .tools/round-close-check.py --project IRPT_DASHBD --round 135 -> MAY-CLOSE, judgment=0; no L8_PACKET_R135_F.md under deliverables/2.0.0_SA_COO~F2/"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Both judgments pass on unique natural keys. The S6 contract carriers that v145 named stale are now aligned with the final ruling (msg 9669). The one-snapshot trap is closed in code. The round-135 packet is owed by 2.0.0_SA_COO~F2; it is not a defect in this round's content. The 49F handler has not yet read a real fact_trn partition; per the packet that waits on the signed dry run."
 }
]
```
