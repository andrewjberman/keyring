# ADVI_FIRMBKTS -- DECOMPOSITION (L5) -- ROUND 4, THE WINDOW'S READERS BUILT DORMANT AND THE ENRICHMENT (PRD v1.3)

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v4",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md (v1.3)",
 "order_ref": "1.0.0_SA_CTO~DELL1 msg 3813: org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round3.md @4c2785565d (section 3, the ENRICHMENT LIST); msg 3822 (the cluster-lead ruling on call c290)",
 "author": "2.0.0_SA_COO~B1",
 "round": 4,
 "rectangle": "the round-3 analysis's enrichment list, items 1-5, and the one ruled act of the relay: the window's last unbuilt reader (auth-validator-edge's canonical ownership-map key) built dormant, the producers' role grant drafted with its staged act, the table repair under the S2-S11 edge rulings, FWD-1's independence by construction as two readers in one-file worktrees, the WAF ACL reconcile, E_24's explicit-mode refusal, and the one SEV1 test text",
 "cells": 16,
 "chains": 14,
 "join_cells": 0,
 "ground_truth": "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/L5_FACTS.md",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~B1` (dell1), seated by `1.0.0_SA_CTO~DELL1` (round-3 analysis msg 3813; the c290 ruling relayed
at msg 3822). **Inputs:** the CTO's round-3 analysis sections 2 and 3 and `ROUND_ANALYSIS.round2.md` ADDENDA 1-7; the
round-3 packet `deliverables/2.0.0_SA_COO~B1/round3/R3_CLOSE.md`; the four staged act orders `TO-FB-f-9` (phase B),
`-10`, `-11`, `-13` and their pair halves in `ledger/`; `deliverables/2.0.0_SA_COO~B1/round4/L5_FACTS.md`.

## Round 4 -- the cells

| cell | item | serves | candidate | owned files | depends on | slot, class | risk |
|---|---|---|---|---|---|---|---|
| `FB-g-1` auth-validator-edge reads the ownership map through a canonical-key helper, DORMANT | 1 | FWD-3, FWD-4 | F6 | `infra/aws/lambda-edge/auth-validator-edge/{index.mjs,ownership_key.mjs,test/ownership_key.spec.mjs}` | -- | ~24 worker | WORLD (path floor), built dormant |
| `FB-g-2` the producers' role grant, drafted (D1-S18) | 1 | FWD-4, FWD-5 | F10 | `infra/aws/terraform/bd-pipeline/iam.tf` (one appended resource, not applied) | -- | ~25 worker | WORLD (path floor), drafted |
| `FB-g-3` table repair under S2-S11 (mapping_v4) | 2 | FWD-2 | F2 | `deliverables/mapping_v4.json`, `MAPPING_TABLE_v4.md` | -- | ~26 worker | LOCAL |
| `FB-g-4` blind reader A, a one-file worktree | 3 | FWD-1 | F3 | its worktree (the issuer ingests the answers) | -- | ~27 worker-light | LOCAL |
| `FB-g-5` blind reader B, a one-file worktree | 3 | FWD-1 | F3 | its worktree (the issuer ingests the answers) | -- | ~28 worker-light | LOCAL |
| `FB-g-6` the WAF ACL reconcile (S12): a plan that reads no ACL change | 4 | FWD-3 | F6 | `infra/aws/terraform/portal-auth/waf-cloudfront.tf` | -- | `0.7.0_AE_CloudOps~FB1` seat order | WORLD (path floor), nothing applied |
| `FB-g-7` E_24's explicit-mode refusal | 5 | FWD-5 | F10 | `data/black_diamond/scripts/gold/E_24.rebuild_fee_scorecard.py`, its test | -- | ~29 worker-light | LOCAL |
| `FB-g-8` act 0: the producers' role grant applied (STAGED, parked) | 1 | FWD-5, FWD-4 | F10 | the one policy resource in `bd-pipeline` | `FB-g-2`, its pair signed | `0.7.0_AE_CloudOps~FB1` | WORLD, STAGED |
| `FB-g-9` the ONE SEV1 test text (the cluster-lead CTO's ruling on call c290) | -- | (rows D1-S15, S16, S20) | -- | `deliverables/0.7.0_AE_CloudOps~FBL/evidence/` | -- | `0.7.0_AE_CloudOps~FBL` seat order, workstream `SEV1_SMS_TEST` | WORLD |

No two cells write one file. Shared reads only: `mapping_v3.json`, `census.json`, the F7 manifest, the producers' census
and the merged dormant builds.

**Chains** (cells joined by a real data dependency are one chain): `{FB-g-2, FB-g-8}`, `{FB-g-1}`, `{FB-g-3}`,
`{FB-g-4}`, `{FB-g-5}`, `{FB-g-6}`, `{FB-g-7}`, `{FB-g-9}`. M = 8.

## Carried, not cells of this round (the window's acts, staged since round 3)

`TO-FB-f-9` (phase B: the producers' mode move, act 2), `TO-FB-f-10` (the delta copy, act 3), `TO-FB-f-11` (the value flip,
act 4), `TO-FB-f-13` (acts 4b and 4c) stay `parked` as cut. Each is re-homed to this round by amendment at its un-park
(`<round>` 3 to 4, `<status>` to `pending`, its `<issued_to>` and criteria rewritten), in this order: `FB-g-8`, act 2,
act 3, act 4, acts 4b and 4c. **The window opens only when every dormant reader is merged and signed** (the CTO's
ADDENDUM 7): `FB-g-1` merged; the generated readers need no cell (the flip regenerates them; the issuer's
`r4_flip.py` is the act's enumeration, 5 value-changing targets of 17 generated); `FB-g-2` merged and its act 0
applied. **Act 4 also waits on row `D1-S21`** (the asset-dim pin, below). The round does not close until these are
terminal or re-parked with a reason.

## The finding the rehearsal added (row D1-S21; not a cell until the CTO rules)

The CTO's list of the flip's readers is `opal_naming.py targets`' consumers. The issuer's scratch-registry rehearsal of the
value flip (`round4/checks/r4_flip.py`: the 49financial routed alias loses its marker; all 17 generated targets
regenerate and diff) changes a bucket VALUE in exactly five targets: `data/firm_registry.json`, `firm-config.mjs`,
`directory_runner.py`, `holdings_snapshot.py` and `data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py`.
`perfrp_firm_pin.py`, which the list names, does not change; the bronze pin, which it does not name, does. The pin repoints
the BD asset-dim bronze pull to `opal-data-49financial`, while `mapping_v3.json` HOMEs that class to `opal-data-assets`.
Which placement is right is an endpoint question: row `ADVI_FIRMBKTS-D1-S21`, BLOCKING on act 4.

## Not in round 4 (ruled, each with its owner and its un-park condition)

| item | owner | un-park |
|---|---|---|
| FWD-7 and FWD-8 (the prohibited key, B2; DEC-13) | Andrew | his word |
| the SNS routing fix for the SEV1 page path | this project, next round | `FB-g-9`'s text arrives (the ruling's first branch) |
| the AWS Support case for the number | Andrew | `FB-g-9`'s text fails (the ruling's second branch) |
| `D1-S19`, the pending `eclipse_jwt_initial` secret version | inf-pipeline's owner | routed as a row; no act here applies it |
| the 97 dynamic-key files | -- | classed in round 3's census (SERVED-REACHING 0); no cell |
| a serving-route field in the builder | -- | REFUSED (ADDENDUM 7, FWD-3): every generated reader moves in one window |
| the bronze pin's placement | 1.0.0_SA_CTO~DELL1 | row `D1-S21` |

## Fan-out

`fanout: 8 of 8 chains, cap 8, reason: six worker subagents (FB-g-1 to -5 and -7) and two seat orders (FB-g-6 to
0.7.0_AE_CloudOps~FB1, FB-g-9 to 0.7.0_AE_CloudOps~FBL) are disjoint in write set; FB-g-8 is staged on FB-g-2 and
spawns nothing.` Seven orders are `pending` at the cut (six workers and two seat orders), one is `parked`.

## Lenses read at L5 (each order's preflight carries its disposition)

| lens | disposition |
|---|---|
| `comp-schedule` | every build cell DECLARED-NOT-APPLICABLE (no cron, rule or cadence changes); the staged acts read it at the act |
| `comp-iam` | `FB-g-8` and `FB-g-9`: the actor's own identity read at the act, resource-scoped, never `*`; `FB-g-2` drafts the grant, makes no AWS call; the rest DECLARED-NOT-APPLICABLE |
| `comp-adversary` | each build cell's criteria are dry-run at base (FAIL as expected) and, where a bound or control, PASS; fixtures prove the checks pass on a conforming build |

## Amendment 1 (2.0.0_SA_COO~B1, 2026-10-11 ~12:5xZ): cell `FB-g-10` added by the CTO's round-3 ADDENDUM 2 (msg 3843)

Row D1-S19 has no owner in the tree (ADVI_ECLDAT has no project home; `0.7.0_AE_CloudOps~DELL1` holds no order on the
root, msg 3837). The CTO ruled: remove the pending `aws_secretsmanager_secret_version.eclipse_jwt_initial` block, issued
by this seat and executed by `0.7.0_AE_CloudOps~DELL1`; import refused; no apply. Cell `FB-g-10` (seat order, workstream
`INFJWT`, slot `~DELL1`, write set `infra/aws/terraform/inf-pipeline/secrets.tf` and its evidence folder; no edge to any
other cell). Cells 9 -> 10, chains 8 -> 9. Fan-out: 9 of 9 chains, cap 8 as the cap of workers spawned at once (six
subagents; three seat orders).

## Amendment 2 (2.0.0_SA_COO~B1, 2026-10-11 ~12:5xZ): cell `FB-g-11` added by the CTO's round-3 ADDENDUM 3 (msg 3845)

Row D1-S21 is ruled: the issuer measured that the CTO's ADDENDUM 1 premise (the bronze-home rule resolves to
`opal-data-bd`) was false (`tiers.json` homes FIRM bronze to `opal-data-assets`), and the CTO accepted ONE transitional
`tier_live.bronze` row in the 49financial scope (owner F11, removed by F11's act), which the pin's renderer reads:
byte-identical now, out of act 4. Cell `FB-g-11` (worker `~32`, workstream `BRONZELIVE`; write set `infra/logic/registry/
scopes.json`, `lib/opal_naming.py` and the 15 tracked generated targets that cover `scopes.json`; no edge to another
cell). Act 4's pair prints the four remaining flipped targets by tier class. Cells 10 -> 11, chains 9 -> 10. Act 4's
un-park no longer waits on the CTO for this row; it waits on this cell's merge.

## Amendment 3 (2.0.0_SA_COO~B1, 2026-10-11 ~12:5xZ): cells `FB-g-12` and `FB-g-13` added by the CTO's round-3 ADDENDUM 4 (msg 3853)

`FB-g-1` (the validator's key) and `FB-g-2` (the producers' grant) built and passed their checks and could not commit:
the enforcing naming gate refuses new hand-kept carriers of `49financial` and of key strings (rows D1-W24-S3,
D1-W25-S1). The CTO ruled (a): generate. `FB-g-12` renders the per-firm ownership-key block into
`_shared/firm-config.mjs` (the validator reads it); `FB-g-13` makes the `opal_name` module expose a scope's bucket and
canonical platinum prefix (the grant reads them and names its policy through `name`). Workstream `OWNKEYS`; both after
`FB-g-11`; `FB-g-1` and `FB-g-2` are re-seated after them with amended faces. Cells 11 -> 13; chains 10 -> 11 (the two
builder cells are one chain with the cells they unblock, `{FB-g-12, FB-g-1}` and `{FB-g-13, FB-g-2, FB-g-8}`, so the
chain count rises by one over the nine independent builds above).

## Amendment 4 (2.0.0_SA_COO~B1, 2026-10-11 ~13:2xZ): cell `FB-g-14` added by the CTO's round-3 ADDENDUM 6 (msg 3871)

Row D1-S24: the flip would repoint the IRPT directory and holdings readers and writers at a bucket holding none of their
keys. The CTO ruled (b): one transitional `product_live.irpt` row (`opal-data-bd`, owner IRPT_BCKEND, expiring at its RI1
move) which the IRPT bucket map targets read; (a) a copy at the same keys is refused. Cell `FB-g-14` (worker `~37`,
workstream `IRPTLIVE`; write set `infra/logic/registry/scopes.json`, `lib/opal_naming.py` and the 15 tracked generated
targets; edge: after `FB-g-11`, merged). After it, act 4's value-changing set is `firm-config.mjs` alone. Cells 13 -> 14,
chains 11 -> 12.

## Amendment 5 (2.0.0_SA_COO~B1, 2026-10-11 ~14:2xZ): cells `FB-g-15` and `FB-g-16` added (the CTO's act-0 condition; ADDENDUM 7)

`FB-g-15` (workstream `QAGUARD`): the dispatcher refuses a QA invocation that arrives with `BD_PLATINUM_MODE=canonical`
preset, the CTO's condition carried from the act-0 sign-off (msg 3895) to act 2, because the QA runner shares the role the
grant widens. `FB-g-16` (workstream `IRPTOWN`): the IRPT loaders read the ownership map from a generated pair (routed
bucket; legacy key now, canonical at act 4 through an environment list), the CTO's ADDENDUM 7 on row D1-S25; the directory
and holdings reads stay on the transitional live row. Both are dormant builds ahead of act 2; act 4's pair names
`FB-g-16`. Cells 14 -> 16, chains 12 -> 14.
