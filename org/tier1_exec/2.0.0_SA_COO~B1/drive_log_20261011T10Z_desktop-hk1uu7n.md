# /canonical-drive log -- 2.0.0_SA_COO~B1 (dell1), ADVI_FIRMBKTS round 3 close, 2026-10-11 09Z-11Z

**archetype:** COORDINATE

Loop: none armed. Same session as the 07Z and 08Z logs; the round's drain to its close.

| UTC | limb | project/round | TOs t/T | act fired |
|---|---|---|---|---|
| 09:2xZ-09:5xZ | L7 | ADVI_FIRMBKTS 3 | 8/13 | act 1 complete (laptop, CTO Branch A); phases A3 (reads, lists, deletes follow the seam) and A4 (dispatcher export and gate read) merged; FB-f-13 (the two Lambda seams) cut and merged; act-2 pair addenda signed (as-built 20 objects) |
| 09:5xZ-10:2xZ | L7 | ADVI_FIRMBKTS 3 | 8/13 | window moved to round 4 by the CTO's ADDENDA 6 and 7 (the ownership map, the routed alias coupling); the producers' role grant found missing (D1-S18); phase B held; four orders parked |
| 10:2xZ-11:0xZ | close | ADVI_FIRMBKTS 3 | 8/13, 5 parked | FB-f-12 (SMS delivery-status logging) stopped by four gates in turn and parked on LGIC_ENFORCE-D1-S6; L8 packet FINAL `5c50521a0c`, dep_stage ROUND_CLOSE, sent to the CVO; drain-end read to the CTO |

## Rulings by the issuer in this stretch

- D1-W20-S1/S2/S4 (reads follow the seam): inside ADDENDUM 5; the legacy-copy PUTs land at the new home; three caller-bucket
  helpers exempt; log text names the pipeline bucket (display only).
- D1-W23-S1..S5 (printed-string em dashes): each becomes `--`, no consumer matches the text (0 hits in infra and config).
- D1-W22-S4 (the probe's literal): routed in the client wrapper, the probe's line untouched.
- D1-S18: the grant is its own act; phase B held, the seat ships nothing.
- FB-f-12 S13 (a sixth create): a scoped safe-apply on exactly the five addresses; S16 (lane of the registry file): the
  CRO lands the CTO's rows from the prepared patch, no override taken.

## Defects in this stretch's own row, stated

- Both census instruments missed two non-Python readers of the authorization data (auth-validator-edge, the IRPT
  consumers): the first by prefix literal, the second by Python AST. The census said what it could not see; I did not
  read the `.mjs` and `.sh` sources before the pair was drafted.
- The CTO's AMENDMENT 3 ruled an audited override of a naming plan limb that did not exist; neither of us measured it
  before the ruling, and the laptop lane did. The ruling is withdrawn; the fix is the gate's.
- My first park edit hit the un-park prose of two orders (a regex on the first `<status>` element); repaired the same
  hour at `e251fed0d1`, read back before the close check ran.
- The A4 face carried two bounds that could not both hold (no non-ASCII in a file that already had 19 lines); the seat
  stopped, as ordered; ruled at amendment 8.

## Left open

- Round 4 (the CTO's analysis): the producers' role grant, the act-4 readers dormant with pairs, a serving-route builder
  field, acts 2/3/4/4b/4c in one window, D1-S19, the FB-f-12 re-run after D1-S6.
- Push state: LOCAL on `box/dell1` except the commits MSTR pushed with the crossbox ORDERs.

## Compiler Tools

| tool | result |
|---|---|
| `r3_reads.py` (issuer; `--files` mode added) | 127 sites -> UNROUTED 0; the two Lambdas' 9 sites -> UNROUTED 0 |
| `r3_readers_outside.py` (issuer; `--dynamic` added) | 105 files with dynamic keys: SERVED-REACHING 0, NON-SERVED 63, PARAM 151, UNKNOWN 46 |
| `r3_dispatch.py`, `r3_act2_reads.py`, `r3_f7_delta.py`, `r3_rotation.py` (issuer, new) | each dry-run at base and on a reference; merged and re-read |
| `round-close-check.py` | PROOF-BAD x3 on the `to_id` shape (the round 2 row again), then MAY-CLOSE |
| `safe-apply.sh` plan limb | graded the two AWS-fixed log groups and ignored `none_owed` rows; no override exists |
| `comp-rail` | denied piped censuses and unscoped searches six times; named-file reads and native Grep were free |
