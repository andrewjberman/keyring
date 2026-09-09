# NFRA_CLDGRPH round 5 -- L8 PACKET (PARTIAL; one of four orders terminal)

**Compiled by** `2.0.0_SA_COO~A` 2026-09-09 ~16:2xZ at the drain of TO-CG-E-3 (@`d3a03a7b7b`), on the `/drive`
obligation "terminal orders -> L8 compile NOW". **Handed to** `3.0.0_SA_CVO` for L9 as each section lands; the FINAL
packet and the ONE drain-end read to `1.0.0_SA_CTO` follow the last drain. **Round 5 is the recut on the CTO's round-4
analysis** (@`707ba2a4c9`: 7 of 8 REALIZED, FWD-7 NOT_REALIZED on the INSTRUCTION plane; PRD v0.5 rows S17-S20, R13):
the instruction and residue planes of the retirement, four cells, three chains (`de466829e0`).

## 1. THE FOUR ORDERS AT THIS WRITE

| order | cell | plane | slot | state at 16:2xZ |
|---|---|---|---|---|
| TO-CG-E-1 | CG-s-17 | INSTRUCTION (the route back) | `~2` on `wk-cldgrph-5-2` | executing: 14 carriers edited on the branch, no commit yet |
| TO-CG-E-2 | CG-s-18 | the four `:latest` producers | `~1` on `wk-cldgrph-5-1` | executing: the pin commit landed on the branch (@`87ed1cdd17`), the ledger's close in progress |
| **TO-CG-E-3** | **CG-s-19** | **RESIDUE (the local stores)** | `~3` | **TERMINAL, drained @`d3a03a7b7b`** (s.2) |
| TO-CG-E-4 | CG-s-20 | RESIDUE (the stitch graph) | `~3`, handed at 16:2xZ on `ab45a3337f` | executing |

## 2. TO-CG-E-3 (CG-s-19) -- the residual local stores, as the checker graded it

Instance `deliverables/0.9.0_WK_NFRA_CLDGRPH~3/NFRA_CLDGRPH.TO-CG-E-3.residual-local-stores-dispositioned.proof_of_spec.json`
@`7f3616c14b`; re-validated at the issuer's seat INSIDE the worktree with the six ids: rc 0, 0 violations, 4 of 4
surprises resolving; both commits authored by the worker; every touched path inside the grant (one tracked `.py`, the
deliverables folder, the channel, the face).

| id | verdict | deciding line | denominator |
|---|---|---|---|
| E3-AC1 | PASS by output | `DISPOSITIONS=4 of 4 RECORDED` / `P7_ROW_FILED=NFRA_CLDGRPH-W3-S6` / `DISPOSITION_PROBE_CONTROL=FIRED` | 4 artifacts, a 4-value closed vocabulary; the control caught 3 of 3 planted defects |
| E3-AC2 | PASS by output | `READERS=0 of 487 files` / `BUILDER_DECLARED=infra/aws/globgrph/kuzu_load.py` / both controls FIRED | 487 `.py` AST-walked over four tool homes, 0 parse failures; 3 prose + 1 docstring mention NOT counted |
| E3-AC3 | PASS by output | `STORES_PRESENT=4 of 4` / `STORE_BYTES_UNCHANGED=2 of 2` | re-run AFTER the manifest acts; the issuer's own `ls -la` agrees (9,224,192 B @06-12 09:55; 4,050,944 B @06-12 10:57) |
| E3-AC4 | PASS by output | `BUILDER_STAMPS_CLAIM=true` / `MANIFEST_CLAIM_FIELDS=2 of 2 staying store(s)` | the issuer read `kuzu_db._build_manifest.json`: `edge_count 2488`, `edge_count_claim merge_attempts`, `artifact_claim historical`; `kuzu_ac7.db` got a manifest that says it does not know its source |
| E3-AC5 | PASS by output | `OK: pre-commit gate clean for 7 of 7 file(s)` | 1 tracked edit + 6 deliverable scripts |
| E3-AC6 | RECORDED, no verdict | the record's s.5 | 4 of 4 artifacts, 3 of 3 reading questions |

**THE DISPOSITIONS** (the record `CG-s-19.residual-stores.result.md` @`85e33e98ee`): `kuzu_db` and `kuzu_ac7.db` =
`HOLD_PENDING_P7` (owner `3.0.0_SA_CVO`, the hold's author); `kuzu_load.py` = `KEEP_WITH_NAMED_READER`; the stale
`.kuzu_nessie_load.*.lock` = `RETIRE_WITH_TOMBSTONE` (owner `0.8.0_AE_CloudComp`). Nothing deleted, moved, rebuilt or
opened with an engine.

## 3. THE JUDGMENT CRITERION E3-AC6 -- what the CVO grades, and the gap the worker named itself

**Two clauses in FWD-7's accept, and this order meets only the READING one.** `READERS=0 of 487` is reachability:
no tool a user works with opens `kuzu_db` or `kuzu_ac7.db`. But `kuzu_db` is a second, older copy of THIS graph (its
own manifest: 1,166 nodes, built 2026-06-12 from `snapshots/20260612/graph-20260612.tar.gz`) and **it is still on
disk**. The EXISTENCE clause -- *no second, older copy anyone could still be reading from* -- is met by DELETION, not
by this record, and the deletion is one act wide (delete + tombstone) and gated on P7's author. **Row W3-S6 (ARMED,
`disarm_owner: 3.0.0_SA_CVO`) is the ask**; the CVO's re-statement or lift on the record is what releases it. This is
stated by the worker in its report and here so the CVO reads it before grading rather than after.

## 4. ROWS THIS ORDER ADDS TO THE CVO'S DESK (channel 122 -> 126 at the drain)

- **W3-S6** (OBSERVATION / ARMED, `3.0.0_SA_CVO`): the P7 re-statement ask -- the accept's "lifted or re-stated by its
  author" clause; the two stores held pending it.
- **W3-S7** (OBSERVATION / ARMED, `0.8.0_AE_CloudComp`): the S53 claim's writer AND consumer both live in
  `_provenance.py`, outside this order's `<paths>` -- the claim is stamped by the builder and carried by the manifests,
  but the shared provenance module that would REJECT on it was not in the grant; a next cut names it.
- **W3-S8** (OBSERVATION / ARMED, `0.8.0_AE_CloudComp`): an honest UNKNOWN card on `kuzu_ac7.db` SILENCES
  `format_provenance_header`'s `!! UNKNOWN VINTAGE` branch -- a manifest that says "I do not know" reads as a manifest
  to the header, so the warning a reader relied on is gone; the disclosure must key on the claim, not on presence.
- **W3-S9** (OBSERVATION / INERT): the stale lock's one-way hash cannot name its target (3,262 candidates, 0 matches);
  it is retired with a tombstone on that basis.

## 5. WHAT THIS PACKET DOES NOT CLAIM

No FWD graded; no row dispositioned; three orders open. Push state LOCAL (origin/CLOUD @`58adeff90c` by ls-remote at
13:0xZ this session; LD-0522). This seat is registered through the MCP client since 16:1xZ (PID 20528); the READ ack
on this packet is measurable by `get_delivery_state` from here on.

---

# ADDENDUM 1 -- 2026-09-09T16:31Z, appended by `2.0.0_SA_COO~A` at the TO-CG-E-2 drain (@`a302d9ebb8`)

## A1.1 TO-CG-E-2 (CG-s-18) IS TERMINAL -- two of four; 22 of 24 project orders

Instance `deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-E-2.four-latest-producers-pinned.proof_of_spec.json`
@`5eccbba025`, rc 0 on seven ids at the issuer's seat inside the worktree.

| id | verdict | deciding line | denominator |
|---|---|---|---|
| E2-AC1 | PASS by output | `PINNED_BY_DIGEST=7 of 7` (the issuer's own `describe-task-definition` on cse-producer: revision 2 on `@sha256:1b89853f...`) | 7 named families; nessie/trino printed out-of-population |
| E2-AC2 | PASS by output | `DIGEST_MATCHES_LOCAL=4 of 4` | the digest parsed from `serving.tf` at run time |
| E2-AC3 | PASS by output | `TARGETS_ON_PINNED_REVISION=3 of 3 declared launcher(s)` | the fourth family has NO launcher on any plane (W1-S28) |
| E2-AC4 | PASS by output | `LATEST_DIGEST_UNCHANGED=true` | bracketed from the order's first read |
| E2-AC5 | PASS by output | the entry's own `Status: CLOSED`, seven families in its Deploy line | 1 of 1 |
| E2-AC6 | PASS by output | `FMT_RC=0` on 4 of 4 files | see S64 |
| E2-AC7 | RECORDED, no verdict | the record's blast-radius reading | 5 of 5 questions |

## A1.2 THE THING THE FACE DID NOT SAY AND THE WORKER MEASURED -- for the CVO's E2-AC7 grade

**The apply set was TEN addresses, not four.** The three declared launchers reference `aws_ecs_task_definition.<x>.arn`
(revision-scoped) AND the three launcher roles' `ecs:RunTask` policies scope their `Resource` to the same revision-scoped
ARN (`comp_learns_producer.tf:131`). `-target` on the four task definitions alone would have applied green and left
three nightly launches failing AccessDenied from the next fire -- W1-S2's shape from round 4, recurring in the same
tree, caught the same way (the plan's address census, not the face's list). `Apply complete! Resources: 4 added,
6 changed, 4 destroyed`; post-apply targeted plan `No changes`; the unscoped plan a control by address list (14
addresses, 4 foreign, none applied). No image rebuilt, pushed or re-tagged; no launch provoked.

## A1.3 ROWS THIS ADDENDUM ADDS TO THE CVO'S DESK (channel 126 -> 131 at the drain, 133 with S64/S65)

- **W1-S27** (ARMED, `1.0.0_SA_CTO`): W1-S11 RECURRED -- the halt gate resolves its principal only from the
  session-keyed serial file, never `OPAL_AGENT_SERIAL`; rc 3 IDENTITY UNRESOLVED on the order's first call while the
  spine-v3 worker limb sits intact one function downstream. The CTO's design surface (analysis s.5).
- **W1-S28** (INERT): `globgrph-resource-summaries-producer` has NO launcher on any plane; a hand-run family (one
  13-minute session on 2026-07-18). Its pin is in force for whoever runs it next.
- **W1-S29** (ARMED, this seat) -- **DISARMED by S64**: the issuer's cut defect (a fmt bar on an unmeasured baseline);
  the worker's substance-vs-whitespace resolution accepted with its printed control.
- **W1-S30** (ARMED, this seat -- CARRIED NAMED): `serving.tf:11-16`'s header comment now describes a world that
  ended at 15:5xZ ("the four producers stay on `:latest` by design"); a comment edit in a file outside every round-5
  grant, lane `0.7.0_AE_CloudOps`.
- **W1-S31** (ARMED, this seat) -- **DISARMED by S65**: the slot folder collision, repaired in the same turn and
  verified byte-identical at the drain; the naming rule adopted for every future face; the gate gap (an in-grant
  overwrite of a tracked deliverable is invisible to every carrier) travels to L10 named beside W2-S18/S19/S20.

## A1.4 WHAT DID NOT CHANGE

E-1 (`~2`) and E-4 (`~3`) executing; no FWD graded; no row dispositioned. Push state LOCAL.

---

# ADDENDUM 2 -- 2026-09-09T16:55Z, appended by `2.0.0_SA_COO~A` at the TO-CG-E-4 drain (@`49fea6980a`)

## A2.1 TO-CG-E-4 (CG-s-20) IS TERMINAL -- three of four; 23 of 24 project orders

Instance `deliverables/0.9.0_WK_NFRA_CLDGRPH~3/NFRA_CLDGRPH.TO-CG-E-4.stitch-graph-home-decided.proof_of_spec.json`
@`aff8c7a102`, rc 0 on six ids at the issuer's seat inside the worktree.

| id | verdict | deciding line | denominator |
|---|---|---|---|
| E4-AC1 | PASS by output | `STITCH_HOME=JOIN_PROJECTION RECORDED` / `PRODUCER_READ=true` | 4 producer fields; 4 later-round cells with lanes; the control caught a planted thin reason |
| E4-AC2 | PASS by output | `REFUSAL_TEXTS_NAME_HOME=2 of 2` | the two `SystemExit` sites in `_stitch_freshness`; the nessie leg's raise printed out-of-scope |
| E4-AC3 | PASS by output | `BUILDER_STAMPS_CLAIM=true` / `MANIFEST_CLAIM_FIELDS=2 of 2` / store `UNCHANGED=True` | the issuer read the manifest: `edge_count_claim merge_attempts`, `artifact_claim interim_local_projection` |
| E4-AC4 | PASS by output | `PROJECTION_REBUILD_PATHS=0 of 3216` | AST nodes across both edited files; 1 comment + 1 docstring mention printed beside the zero |
| E4-AC5 | PASS by output | `OK: pre-commit gate clean for 16 of 16 file(s)` + the bounded `comp_debt.py` run (rc 1, the refusal naming the home) | see W3-S12, W3-S13 |
| E4-AC6 | RECORDED, no verdict | the record's s.4 | 4 of 4 questions + the deliberate-omissions clause |

## A2.2 THE DECISION, AND THE FINDING BENEATH IT -- for the CVO's E4-AC6 grade and the CTO's L10 read

**HOME = JOIN_PROJECTION** (owner `0.8.0_AE_CloudComp`). The one-line reason: the S3 stitch artifact's own marker
says `"producer": "stitch-local"` -- the estate already treats the cloud key as the destination and only the COMPUTE is
misplaced; declaring the local store canonical would ratify the workaround and retire the destination. Four
later-round cells are named with lanes, verbs and accepts (none cut here): **repair the producer** (`0.7.0_AE_CloudOps`);
extend the projection to carry the stitch source; repoint `comp-debt`'s second leg through the client; retire the local
store with a CG-s-19-shaped disposition (all `0.8.0_AE_CloudComp`).

⛔ **W3-S10 (ARMED, `0.8.0_AE_CloudComp`): the cloud stitch producer has NEVER succeeded.** `opal-stitch-produce`:
67 of 67 CodeBuild builds FAILED since 2026-07-07, 25 of 25 consecutive rule-initiated nightlies (`cron(0 3 * * ? *)`,
ENABLED, fires on time); the BUILD phase dies in ~30 s on `derive_stitch.py ... exit status 2`; `stitch-source/source.zip`
last pushed 2026-07-07. The issuer's own `list-builds-for-project` read 67. What IS in S3 was written by a laptop. **JOIN
was decided on a substrate that currently produces nothing**, which is why the first named cell is the repair.

⛔ **W3-S11 (ARMED, `0.8.0_AE_CloudComp`): the local stitch store's bytes were content-written 2026-08-27 02:32 with no
manifest rewrite** (Modify == Change; no build, since the builder rewrites the manifest); `node_count 3414 / edge_count
5329` describe the July bytes and no manifest describes the store on disk. The capable mutator is INFERRED as the
deleted `kuzu_cost_enrich.py` (it wrote both stores; the identification is marked inferred, the capability grounded).

- **W3-S12** (INERT): the face's expected bounded `comp-debt` run cannot show the stitch leg NOT refusing from any
  worktree (`STITCH_DB` is script-relative and the store is gitignored); from the main workspace it refuses STALE by
  mtime. The refusal itself was the exercised artifact.
- **W3-S13** (INERT): E-3 and E-4 both named `commit_gate_all.sh` in the same slot folder (the issuer's cut, the same
  defect as W1-S31/W2-S34); resolved as a UNION script gating all 16 `.py` of both orders, its header saying so.

## A2.3 WHAT DID NOT CHANGE

E-1 pass 2 (`~2`) executing on the issuer's ruling of W2-S30 (the classification generator on the population
authority). No FWD graded; no row dispositioned. Channel 137 at the drain. Push state LOCAL.
