# TCKT_VNEXT workstream F10 (FWD-6 commentary on the ticket; FWD-9 package route) -- L8 PACKET, rounds 1-4

**Compiled by** `2.0.0_SA_COO~V2` on 2026-10-09 ~03:4xZ, at /canonical-drive tick 3. **For** `3.0.0_SA_CVO` at L9, as a FILE. The one
message names this path and its hash. This is not the L10 slug: round 1's thread (FWD-1) is still open on TV-r-1, which is Alyssa's
own filing.

## 1. The workstream

- **Authority:** PRD ADDENDUM 1 @f8c019c28f (FWD-6, brought forward) and PRD v0.3 ADDENDUM 2 (FWD-9 / C-PACKAGE; CVO ratified-text half
  @8405844839).
- **Decomposition:** `decompositions/TCKT_VNEXT_DECOMP_F10.md`.
- **Contract:** the contract with NFRA_TRNSPT H6 is `deliverables/2.0.0_SA_COO~V2/FWD10_H6_H5_TICKET_WRITE_CONTRACT.md` v0.2
  @20784c5462.

`round-close-check.py --project TCKT_VNEXT --round <n> --workstream F10`:

| round | orders | verdict |
|---|---|---|
| 1 | 1 | MAY-CLOSE |
| 2 | 1 | MAY-CLOSE |
| 3 | 1 | MAY-CLOSE |
| 4 | 2 | MAY-CLOSE |

## 2. Terminal worker orders (every criterion MECHANICAL; issuer re-ran each one before the drain)

| order | cell | risk | instance (`deliverables/`) | issuer re-run | drained |
|---|---|---|---|---|---|
| TO-F10-l1 | F10-l-1 svc-commentary CREATE-only, draft fields, 08-12 tests (+AMENDMENT 1: firm clamp env) | WORLD | `0.9.0_WK_TCKT_VNEXT~3/TCKT_VNEXT.TO-F10-l1...proof_of_spec.json` | 4/4, 7/7, 4/4; suite 104 | @49c04cd4b2 |
| TO-F10-l2 | F10-l-2 household optional for svc-commentary | WORLD | `~3/TCKT_VNEXT.TO-F10-l2...` | 4/4; suite 108 | @38f57d2f57 |
| TO-F10-l3 | F10-l-3 C-PACKAGE route, principal EMPTY (+AMENDMENT 1: matrix pin 8->9) | WORLD | `~3/TCKT_VNEXT.TO-F10-l3...` | 4/4, 6/6; suite 118 | @da0471b901 |
| TO-F10-p2 | F10-p-2 portal shows draft + package refs | LOCAL | `~4/TCKT_VNEXT.TO-F10-p2...` | 3/3 bun, tsc rc 0 | @d3b33b2ff1 (workspace); portal 44c31b8e awaiting Andrew's DEV word |
| TO-F10-l4 | F10-l-4 BUILD_ONLY mode | LOCAL | `~5/TCKT_VNEXT.TO-F10-l4...` | PASS (fake-aws, negative control bites) | @d3b33b2ff1 |

## 3. The one JUDGMENT criterion for you -- TO-APPLY-F10 AC2 (WORLD, issuer cell F10-d-1, applier `0.7.0_AE_CloudOps~DELL2`)

The order is `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/task_orders/TCKT_VNEXT.TO-APPLY-F10.svc-commentary-code-env-and-mint-dell2.md`.
Its face still reads `pending`, because the applier has not flipped it. The ledger is CLOSED 4/4:
`org/critical_paths/change_management/20261009T0056Z_tckt-vnext-f10-d1-mint-20261009_deploy_completion.md`.

**AC2's words:** steps 5 and 6, which are the deployed bytes and env, plus leg M's positive arm and negative arms.

**The artifacts:**
- **Leg D:**
  - the plan is `deliverables/tckt_f10/F10-D1_plan_ticket_center.txt` (1/1/0);
  - live CodeSha256 is `RFRuryx..`;
  - the deployed `lambda_function.py` sha256 is `01534e2d...`. The issuer re-derived it from the live zip independently at ~01:1xZ.
  - `COMMENTARY_ALLOWED_FIRMS` is byte-exact;
  - the `package` route is live;
  - an unauthenticated POST gets 401;
  - ItemCount is 12, unchanged;
  - the replan is 0-diff.
- **Leg M:** `deliverables/tckt_f10/F10-M_arms_result.json` (@5c513af524), under COO-half AMENDMENT 2 @d6a493570d:
  - step 3, claims on the stored bytes: PASS;
  - step 4, create: 201, ticket TCK-20261009-a1052909;
  - steps 5a and 5b, no firm reach: PASS;
  - step 6: 400 naming the firm;
  - step 7, LIST: 403.

**Weigh these:**
- (a) Step 4 used a SYNTHETIC attachment pointer (`input_id` = sha256 of a TEST label). It proves the write path and the claims; it
  does not prove a real report's ids flow through. That is H6's live run (NFRA_TRNSPT) or TV-r-1.
- (b) Test ticket TCK-20261009-a1052909 is still OPEN. Only an Opal person can close it, and the ask is with the CTO.
- (c) The read grant reaches dell1 as well as dell2 (row D2-S9, for the CTO).

## 4. Rows this workstream raised

| row | state | owner |
|---|---|---|
| D2-W3-S1 | answered from code; confirmed live by step 4 | -- |
| D2-W3-S2 | resolved by W3-S3 | -- |
| D2-S6 | closed (CTO msg 1893) | -- |
| D2-S7 | fixed by TO-F10-l4 | -- |
| D2-S8 | the pair's reader gap; resolved by the laptop grant and amendments, ledger closed | -- |
| D2-S9 | open: dell1 reach | CTO |
| D2-S10 | the step-4/6 spec gap; resolved by AMENDMENT 2 | -- |

Full table: `deliverables/2.0.0_SA_COO~V2/ROW_DISPOSITIONS_R1_F10_20261009.md`.

## 5. Not in this packet

- **FWD-6's organic arm:** the drafter's first real draft. That is NFRA_TRNSPT H6; its Lambda role's read grant is H6's pair.
- **FWD-9's real run:** the package route's principal ships EMPTY until IRPT_ANLREQ's L5 binds it.
