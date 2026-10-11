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
 "cells": 42,
 "chains": 40,
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

## Amendment 6 (2.0.0_SA_COO~B1, 2026-10-11 ~15:0xZ): cell `FB-g-17` added (the canonical-bucket list is the registry's, not three hand lists)

The engagement of the canonical keys must be the registry's one value (the CTO's ADDENDA 4 and 7; the naming gate refuses a
typed bucket). `FB-g-16` renders `CANONICAL_PLATINUM_BUCKETS` (the destination classes' unique canonical buckets) into
`firm-config.mjs` and `loaders.py`; `FB-g-17` (worker `~40`, workstream `CANONLIST`) makes the router and the validator
import it. After it the act-4 flip is the one alias marker. Edge: after `FB-g-16`. Cells 16 -> 17, chains 14 -> 15.

## Amendment 7 (2.0.0_SA_COO~B1, 2026-10-11 ~15:5xZ): cells `FB-g-19` and `FB-g-20` added (act 3b, the readers' admission; CTO ADDENDA 8 and 9)

Row D1-S27 found the canonical bucket carrying no Allow and a fence admitting none of act 4's readers; the CTO ruled one
prerequisite act, 3b, with every row generated (ADDENDUM 8), after a generator cell (ADDENDUM 9). `FB-g-19`: the exemption
grammar's `prefix` takes a string or a list (the performance adapter reads two prefixes). `FB-g-20`: the module exposes a
scope's canonical ownership key, so the readers' identity grants are generated through `opal_name`. Workstream `FENCE3B`.
The act's remaining cells (the registry rows, the OAI allow in the shared-infra bucket policy, ten identity grants, the
executor's order and the pair) follow these two. Cells 17 -> 19, chains 15 -> 17.

## Amendment 8 (2.0.0_SA_COO~B1, 2026-10-11 ~14:5xZ): cell `FB-g-21` added (act 3b's carrier is a generated bucket-policy Allow; CTO ADDENDUM 10)

The CTO accepted a generated bucket-policy Allow beside each scoped Deny row, in place of nine identity-side applies
(ADDENDUM 10, msg 3922). `FB-g-21`: the module renders that Allow from the same row, accepts an exact object key in a row's
prefix list (the CTO's grain: the object ARN of the ownership key, never the prefix), and renders an Allow-only `grants` row for
the two principals the fence already admits by other means. `FB-g-22` (registry rows and the shared-infra wiring) follows its
merge. Cells 19 -> 20, chains 17 -> 18.

## Amendment 9 (2.0.0_SA_COO~B1, 2026-10-11 ~15:0xZ): cell `FB-g-22` added (act 3b's rows and the shared-infra wiring)

`FB-g-22` writes act 3b's permitted set into the registry (eight scoped rows, two `grants` rows) and wires the module's Allow
into the bucket policy file, replacing the performance adapter's three hand statements. It depends on `FB-g-21`'s merge.
The act that applies the policy (`FB-f-14`, staged) runs under the act 3b pair. Cells 20 -> 21, chains 18 -> 19.

## Amendment 10 (2.0.0_SA_COO~B1, 2026-10-11 ~15:1xZ): cell `FB-g-23` added (a write action on the fence side only; CTO ADDENDUM 11)

The exec-summary generator's put moves with act 4b. The CTO ruled (ADDENDUM 11, msg 3927) that the fence's scoped actions gain
`s3:PutObject` on the Deny side only, with the Allow identity-side in the writer's root. `FB-g-23` is the module and builder
change; act 4b's rows follow. Cells 21 -> 22, chains 19 -> 20.

## Amendment 11 (2.0.0_SA_COO~B1, 2026-10-11 ~15:3xZ): cell `FB-f-14` added (act 3b applied)

The act 3b pair is SIGNED in both halves (CTO msg 3932) and its cells `FB-g-19` to `FB-g-23` are merged and graded. `FB-f-14` is the
apply of the one bucket policy, issued to `0.7.0_AE_CloudOps~FB1`; the close simulation is the laptop lane's, cut by the issuer
as a crossbox ORDER. Cells 22 -> 23, chains 20 -> 21.

## Amendment 12 (2.0.0_SA_COO~B1, 2026-10-11 ~15:4xZ): cells `FB-g-24` and `FB-g-26` added (row D1-S29; CTO act-0 ADDENDUM 1)

The act-0 grant lacks `s3:DeleteObject`, and the two stale-advisor cleanups never read `delete_objects`' `Errors`
(D1-S29). The CTO ruled both: a narrow Delete grant on the exact prefixes the code deletes under (msg 3931, item 1), and
fail-loud on `Errors` at both sites (item 2). `FB-g-24`: the module exposes the per-class canonical directories, so the grant
is generated. `FB-g-26`: both scripts fail loud, with a unit test. The grant cell `FB-g-25` (bd-pipeline `iam.tf`) follows
`FB-g-24`'s merge. Cells 23 -> 25, chains 21 -> 23.

## Amendment 13 (2.0.0_SA_COO~B1, 2026-10-11 ~15:5xZ): cell `FB-g-25` added (the narrow Delete statement; row D1-S29)

`FB-g-24` (the module's per-class directories) and `FB-g-26` (fail loud on `Errors`) are merged and graded. `FB-g-25` writes the
one statement of the act-0 policy that grants `s3:DeleteObject` on the two advisor directories. Cells 25 -> 26, chains 23 -> 24.

## Amendment 14 (2.0.0_SA_COO~B1, 2026-10-11 ~15:5xZ): cell `FB-f-15` added (act 3b's close simulation, laptop lane)

`FB-f-14` applied the act 3b bucket policy (`0.7.0_AE_CloudOps~FB1`, @0acccf7d8e: 4 to 29 statements, `r4_act3b.py` 3 of 3).
`FB-f-15` is its second half: the IAM evaluation of nine admitted principals and two non-admitted roles against the live
policy, a read-only order for `0.7.0_AE_CloudOps~FBL` through a crossbox ORDER. Cells 26 -> 27, chains 24 -> 25.

## Amendment 15 (2.0.0_SA_COO~B1, 2026-10-11 ~16:0xZ): cells `FB-g-27` and `FB-g-28` added (act 3c and act 4b's identity side; CTO ADDENDUM 11)

The CTO's ADDENDUM 11 put the exec-summary generator's put on the fence's Deny side and its Allow identity-side. `FB-g-27`
writes the generator's scoped row into the registry (act 3c's rows; its apply is one more bucket-policy act, inert). `FB-g-28`
adds the narrow `s3:PutObject` policy in the exec-summary root (apply before 4b). Cells 27 -> 29, chains 25 -> 27.

## Amendment 16 (2.0.0_SA_COO~B1, 2026-10-11 ~16:1xZ): cell `FB-f-16` added (the act-0 Delete statement applied)

`FB-g-25` merged and graded (@555ba2e0f5, `r4_delgrant.py` 5 of 5); the act-0 addendum's two halves read SIGNED (CTO msg 3959).
`FB-f-16` applies the one statement to the one policy, issued to `0.7.0_AE_CloudOps~FB1`, before act 2. Cells 29 -> 30, chains 27 -> 28.

## Amendment 17 (2.0.0_SA_COO~B1, 2026-10-11 ~16:2xZ): cell `FB-g-29` added (the invocation census for act 4's widened sample)

The CTO's act 3b CTO half (msg 3932) widened act 4's sample to one real invocation per admitted principal. `FB-g-29` is the
read-only census of the smallest side-effect-free event per function (eight IRPT consumers and the validator). Cells 30 -> 31,
chains 28 -> 29.

## Amendment 18 (2.0.0_SA_COO~B1, 2026-10-11 ~16:2xZ): cells `FB-f-17` and `FB-f-18` added (act 3c and act 4b's identity policy applied)

The CTO signed act 3c and acts 4b/4c (msg 3974). `FB-f-17` applies the generator's fence row (one bucket policy); `FB-f-18`
applies the narrow put policy in the exec-summary root (`1 to add`). Both are inert until act 4b; both are issued to
`0.7.0_AE_CloudOps~FB1` after `FB-f-16`. Cells 31 -> 33, chains 29 -> 31.

## Amendment 19 (2.0.0_SA_COO~B1, 2026-10-11 ~16:4xZ): the four staged acts re-homed (cells `FB-f-9`, `FB-f-10`, `FB-f-11`, `FB-f-13`)

The four window acts cut in round 3 and parked at its close are re-homed to this decomposition by amendment (their `<decomp_doc>`
now names this file): act 2 (`FB-f-9` phase B, the producers' mode move), act 3 (`FB-f-10`, the delta copy), act 4 (`FB-f-11`, the
value flip and the eleven units) and acts 4b/4c (`FB-f-13` phases B and C). They stay `parked` until the issuer's GO; their order
is `ledger/WINDOW_RUNBOOK_ROUND4.md`. Cells 33 -> 37, chains 31 -> 35.

## Amendment 20 (2.0.0_SA_COO~B1, 2026-10-11 ~16:4xZ): cell `FB-g-32` added (the SEV1 SMS publisher census; c290)

Andrew's word: the one test text ARRIVED, so the fault is SNS's origination choice; the CTO ruled the form (AMENDMENT 5, msg
4005): every publisher that reaches the SEV1 SMS subscription sets `AWS.MM.SMS.OriginationNumber` from one Terraform-managed
value. `FB-g-32` is the read-only census (N printed). Cells 37 -> 38, chains 35 -> 36.

## Amendment 21 (2.0.0_SA_COO~B1, 2026-10-11 ~17:0xZ): cells `FB-g-30` and `FB-g-31` added (act 4's flip commit and the eight re-pins)

The act-4 pair's permitted set (COO half + ADDENDA 1 and 2, CTO half + ADDENDA 1 to 5) names two repository commits that no
earlier cell produced: the flip commit (one registry value and the regenerated targets) and the eight re-pins of the IRPT
consumers' staged `loaders.py`. Both are worker cells so the order's `<paths>` grants the generated targets' lanes. They are
STAGED (`parked`) for the window. Cells 38 -> 40, chains 36 -> 38.

## Amendment 22 (2.0.0_SA_COO~B1, 2026-10-11 ~17:2xZ): cell `FB-f-19` added (act 4's laptop leg) and `FB-f-11` re-faced

Act 4 is two executors under one pair: `FB-f-11` is now the dell1 leg (the eight IRPT consumers, the before and after
authorization sample, the first hour) and `FB-f-19` the laptop leg (router, guard, validator). Both are STAGED (`parked`) for the
window. Cells 40 -> 41, chains 38 -> 39.

## Amendment 23 (2.0.0_SA_COO~B1, 2026-10-11 ~17:3xZ): cell `FB-g-35` added (c290: the SMS default type)

The census (`FB-g-32`) read 54 publishers, 38 of them AWS services that cannot set a message attribute. The CTO withdrew the
per-publish form and ruled one attribute on the existing account preferences (AMENDMENT 6, msg 4021). `FB-g-35` writes it; its
apply is the laptop lane's. Cells 41 -> 42, chains 39 -> 40.
