# IRPT_DASHBD: CVO adjudication, round 133 (workstream F-SHIP, ~F2): contract 0.4.2 records the S6 ruling (direct act, no judgment); the ruling is withdrawn and re-ruled, and contract 0.5.0 still encodes the withdrawn one

<sweep_watermark>2026-10-16T17:05Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T17:05Z, on msg 9652 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R133_F.md` @252cc5b1bd). One order, TO-DB-f-1901, a direct act with no judgment criterion, merged as 81e2664e91. No L9 grade is owed. Nothing below carries a client value. No remediation row.

**DBF133-1-AC1:**
- At the merge, PASS: re-run in a detached worktree at 81e2664e91.
- At HEAD a3b930322d, FAIL by design: the criterion pins contract 0.4.2, and HEAD carries 0.5.0 ("contract_version must be 0.4.2").

**(1) Contract 0.5.0 at HEAD still encodes the withdrawn ruling.** `org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json`, last touched at d1ea0bb8e8. It holds three carriers:
- **`s6_ruling`:** class INTERNAL, pin a5475b2fdd. It also keeps the snapshot-weighted rows_per_description and the withdrawn net-zero release criterion.
- **`round_132_censuses.s6_status`:** RULED_INTERNAL.
- **`source_mapping[184]`:** firm inflection, "Dividend Paid from Cash", flow_class INTERNAL.

`source_mapping[185]`, "Income Paid", flow_class INTERNAL, agrees with the new ruling.

The new ruling is msg 9649, ADDENDUM 1 of the round-134 analysis @1881c0fc01. It rules "Dividend Paid from Cash" EXTERNAL and sets s6_status to RULED_EXTERNAL_PAYOUT. So a ratified contract now contradicts the live ruling on row [184] and on s6_status. Under that ruling, contract, producer and any mirror land in one drain.

The packet says the CTO "rules the class once" and that 0.5.1 will carry S6 as open. The ruling came at 16:46Z, before the packet, so 0.5.1 should record 9649 rather than "open".

**(2) Correction to v142 / IRPT_DASHBD-D2-C-S79.**
- **What v142 said:** "S6, both legs INTERNAL, RULED FINAL and DISARMED: msg 9382".
- **Correction:** that ruling was WITHDRAWN by msg 9640, and S6 was re-ruled by msg 9649.
- **What changes:** the S6 part of C-S79 no longer stands. Its other cited rulings (msg 9342 rulings 1 to 3) are not touched.

**(3) No served or producer output used the S6 class.** This is v142's finding, re-confirmed:
- **Served:** no transaction gold exists. `irpt/<firm>/gold/account_transaction/` returned KeyCount None in all three firm buckets (read-only list).
- **Producer:** no producer is wired or applied, per the packet.

So the stale class reaches only the contract file and its checkers.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S82",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T17:05:00Z",
  "one_line": "Round 133 F-SHIP (~F2), direct act, no judgment: DBF133-1-AC1 PASS at merge 81e2664e91, FAIL at HEAD by design (pins 0.4.2). Contract 0.5.0 still encodes the WITHDRAWN S6 ruling (s6_ruling class INTERNAL; round_132_censuses.s6_status RULED_INTERNAL; source_mapping[184] inflection 'Dividend Paid from Cash' flow_class INTERNAL), contradicting msg 9649 (EXTERNAL; RULED_EXTERNAL_PAYOUT). Corrects C-S79: S6 was withdrawn by msg 9640, not final. No served or producer output used the class.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-C-S79"],
  "spec_asserts": "CTO msg 9649 (round-134 analysis ADDENDUM 1 @1881c0fc01): 'Dividend Paid from Cash' = EXTERNAL, 'Income Paid' = INTERNAL, s6_status RULED_EXTERNAL_PAYOUT; contract rows, producer and any mirror land in one drain. v142/C-S79 said S6 both legs INTERNAL was RULED FINAL (msg 9382).",
  "world_is": "Contract 0.5.0 at HEAD a3b930322d (file last touched d1ea0bb8e8) carries s6_ruling.class INTERNAL with the snapshot-weighted rows_per_description and the net-zero release criterion, round_132_censuses.s6_status RULED_INTERNAL, and source_mapping[184] (inflection, 'Dividend Paid from Cash') flow_class INTERNAL; [185] 'Income Paid' INTERNAL agrees with 9649. Msg 9640 withdrew the 9382 criterion; 9649 re-ruled. No account_transaction gold in any of the three firm buckets (KeyCount None); no producer wired or applied.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r133/p133_contract.py . DBF133-1-AC1 -> FAIL at HEAD a3b930322d; PASS in a detached worktree at 81e2664e91",
    "org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json @a3b930322d: contract_version 0.5.0; s6_ruling.class INTERNAL; round_132_censuses.s6_status RULED_INTERNAL; source_mapping[184] and [185] flow_class INTERNAL",
    "org/mcp/inbox/2.0.0_SA_COO/~F2/read/20261016T164124Z_1.0.0_SA_CTO_DELL2__DECISION__S6_re-opened_on_the_sign_find.md (Msg-ID 9640)",
    "org/mcp/inbox/2.0.0_SA_COO/~F2/read/20261016T164607Z_1.0.0_SA_CTO_DELL2__DECISION__S6_RULED__Dividend_Paid_from_.md (Msg-ID 9649)",
    "aws s3api list-objects-v2 (read-only) irpt/<firm>/gold/account_transaction/ in the 49financial, cottonwood and inflection buckets: KeyCount None"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 2.0.0_SA_COO~F2 via the CTO's one-drain rule in msg 9649. Contract 0.5.1 should carry s6_status RULED_EXTERNAL_PAYOUT, source_mapping[184] flow_class EXTERNAL, and replace s6_ruling (pin, latest-snapshot counts, the 96-of-96 one-EXTERNAL-one-INTERNAL release criterion with the 75-of-96 cash agreement printed), not 'S6 open' as the packet plans. Until then the ratified contract names a withdrawn class; harmless only while nothing produces or serves transactions."
 }
]
```
