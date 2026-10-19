# 3.0.0_SA_CVO~IRPT -- session 2026-10-17 01:10Z to 2026-10-19 23:20Z (dell2): disarm rulings, one sample L9, one compile

**archetype:** VALIDATE

Continues `../2026-10-17/session_CVO-IRPT_1845Z-0110Z.md`. The session was offline from about 10-17 15:00Z to 10-19
12:49Z; at resume the watcher was re-armed (one script row), delivery state since 10-17 06:40Z showed 1 of 1 READ,
and no IRPT adjudication or drain packet had landed from any seat in the gap.

## Work (7 adjudications)

| project | adj | commit | ruling |
|---|---|---|---|
| IRPT_DASHBD | v150 | 10ad24dff6 | W2605-S1 DISARMED: the live function never imports the producer (0 of 16 files); the fix ships with the new handler |
| IRPT_DASHBD | v151 | 01b80cd784 | W1901-S2 DISARMED (amendment a real fix, 56/56); S103/S107 held: Cottonwood's only L9 was on contract 0.4.0 |
| IRPT_DASHBD | v152 | 493a6120b6 | Cottonwood sample on 0.5.1 PASS 20/20; S103/S107 DISARMED (all three firms L9 on 0.5.1); sample had no criterion id |
| IRPT_DASHBD | v153 | 7c54f649a6 | S136 DISARMED: 10-19 fire, 0 FILLED_CATCHUP_LIST_FAILED in its whole log, listing grant live (simulator) |
| IRPT_DASHBD | v154 | b48dfc10d2 | B-IN r132 MAY-CLOSE: 863 = manifest, 795 + 68, 0 unaccounted; boundary measure and chain check untestable (chain earliest 2027-06-10) |
| IRPT_ANLREQ | v28 | 5d44b1e04b | W301-S1/W302-S1 DISARMED: 156 and 26 counted independently; all 17 class changes ordered |
| IRPT_ANLREQ | v29 | bf638c2b19 | S216 DISARMED: producer ran COMPLETE on the real pre-price-pages layout, 17 price elements NOT_IN_THIS_VERSION |

## MCP traffic

Received and acked: 10325, 10333, 10335, 10364, 10677, 10694, 10915, 11060. Sent: one slug per adjudication above.

## Compiler Tools

| tool | result | note |
|---|---|---|
| criterion and test re-runs on trunk | PASS | every row |
| CloudWatch log read of one invocation, whole stream, with a positive control | PASS | v153 |
| `aws iam simulate-principal-policy` with a neighbouring-prefix negative | PASS | v153 |
| producer run against a historical layout from git | PASS | v29 |

What worked: refusing a disarm until the condition held for every firm (v151 -> v152); counting pinned values
independently rather than accepting the code's new output (v28).
Gap found: a sample graded outside any task order has no criterion id the round gate can count (v152).

## Current State

- Watcher re-armed on each expiry; inbox empty at 23:18Z. Zero crons.
- Push state: origin box/dell2 reads 7d1955a98f (ls-remote 23:18Z); v29 LOCAL at that read.

## Blockers

None in this lane.

## Next Steps

- [Andrew] v143's 49F Performance-page change: approve or roll back (COO half signed after the act).
- [2.0.0_SA_COO~G2] W303-S1/S2, W308-S1/S2/S3 and the INERT observations in the next IRPT_ANLREQ L8 compile.
- [3.0.0_SA_CVO~IRPT] Compile and slug every new IRPT L8 packet.

-- 3.0.0_SA_CVO~IRPT
