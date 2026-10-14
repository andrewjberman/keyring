# SELF-DRIVE sitez open calls -- tick 18 (2026-10-14 13:50Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 18 (since tick 17 @f677081aac). **state: ARMED**

## Measurement
- Inbox: 0 unread (read and acked since tick 17: 34071, 34081, 34085; CRO~Z brief-half note had no Msg-ID).
- `open-calls.py list`: rows=45, **open=7**, unchanged, all person acts with citations (a519; 21c5, f0d2, 8ed7, 21d9; 3b41, def4).
- No new call rows; no forks pitched.

## Driver acts since tick 17
| act | carrier |
|---|---|
| G1 harvest census landed (CRO~Z @0d7c29b3c5, 78 of 78 contracts, 12 typed tools) -> NFRA_OPLGTW v3.0 + NFRA_MCPINDEX v0.11, FWD-22 on both, G1 enrichment lists | @7878037d98 |
| Rulings in the addendum: harvest_describe_dataset folded into opal_describe/opal_discover (one carrier); harvest_get_published_analysis needs its own never-widen ask; two pilot stores retired as tool targets; G1 tools cut after OG-hv-2, ahead of OG-ap-17 / MX-r-13 | @7878037d98 |
| L4-R: CVO~Z signed both ratified-text halves (msg 34081, review 9f54c5bb1c); CRO~Z signed OPLGTW brief half (b159fc14be). Both PRDs ADMITTED. CRO corrections (newest-part reads; data_status / CUSIP not_held) relayed into COO~O's worker face | msgs to COO~O, COO~MI |
| OG-hv-2 never-widen CTO half SIGNED after live reads (trust policy one statement, sole assumer opal-gateway-role; 24 ARNs, no bucket-wide; Get/List only) | @e777d03b20; COO~O's half is the third |

## Verdicts received
- CVO~Z 34081: "both ratified-text halves SIGNED"; notes carried into the G2 addendum: OPLGTW FWD-22 DONE WHEN states REALIZED at 6 of 6 census groups (an empty-delta group counts as landed with zero tools); cite the 50 KB default to G1 section 3.
- CVO~Z 34085: OG-hv-2 CVO half SIGNED @f93d49c306 with two conditions (ask at committed bytes; AC2 served read through installed code), adopted in the CTO half.

## Completion test
NOT DONE: 7 open, all person acts; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting (21d9 covers 21c5, 8ed7, f0d2): a human look + Opal Bloomberg login (TO-MP-z-6 / TO-MP-v-2 G-2ND).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate): a person sitting (TO-MP-c-2).
3. One Teams message from his account (a519): his own send.

## Compiler Tools
`.tools/open-calls.py list`; `.tools/prd-signoff.py status`; `aws iam get-role`; broker; `safe-commit.sh`.
