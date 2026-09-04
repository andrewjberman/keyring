# Session W, 2026-09-04 20:30-22:00Z -- NFRA_OUTSET round 1: TO-OS-s-6 and TO-OS-s-7, two cloud audits

**archetype:** VALIDATE

**Seat:** `0.7.0_AE_CloudOps~W` (dedicated NFRA_OUTSET lane, first session of this serial)
**Issuer:** `2.0.0_SA_COO` · **Orders:** `NFRA_OUTSET.TO-OS-s-6`, `NFRA_OUTSET.TO-OS-s-7`
**Repo:** HEAD `14f26b5eff` on `CLOUD` · **Push state (MEASURED via `git ls-remote origin CLOUD`):** LOCAL; origin/CLOUD @`fa82d6b93c`.

---

## Current State

Both orders executed to their acceptance clauses. `TO-OS-s-7` is complete and flipped. `TO-OS-s-6` is
executed but **NOT flipped**: its only mechanical criterion cannot pass as cut, which is a CUT DEFECT
belonging to the issuer, filed as `NFRA_OUTSET-S1` and reported rather than worked around.

**OS-s-6 -- who can call the federated transport.** Target fixed from the producer, not assumed:
`.tools/_trino_fed.py:31-36,84` gives cluster `opal-globgrph`, task-def `globgrph-trino`, log group
`/ecs/globgrph/trino`, and the requirement `ecs:RunTask` + `logs:GetLogEvents`. Live task-def ARN
`arn:aws:ecs:us-east-1:313476888478:task-definition/globgrph-trino:6`. APPLIED census refreshed BEFORE use
(2026-09-04T21:18:31Z; 224 roles / 1 group / 7 users). Role plane: 1 holder of `ecs:RunTask`
(`lambda-execution-role`), 3 of `logs:GetLogEvents`, 1 explicit Deny. **The cell's real question settled:
a worker subagent holds no cloud identity and does not need one -- it inherits the box's ambient
credentials, which resolve to `user/Andrew_Berman`, a member of `AdministratorAccessOpalCapital` carrying
`AdministratorAccess` (`*`/`*`). So a worker subagent CAN call the transport, holding `*` on `*`.** The
report host is UNREADABLE -- a PRD-s.3 design object, not a provisioned resource.

**OS-s-7 -- the code_heat parquet's cadence and owner.** Cadence read from the PRODUCER, as the face
demanded: `infra/aws/terraform/globgrph/item2a.tf:404-409` records the `GLOBGRPH_CODEHEAT_ENABLED` flag
REVERTED 2026-07-16 per CTO TO-2 ruling 033933Z, making the producer host-bound ("DEV-BOX CADENCE").
Corroborated on a different instrument: 142 live EventBridge rules, 5 name-matching, **0 firing the
code_heat producer** while four sibling producers on the same federation do carry nightly crons.
**There is no cadence and there is no owner** -- Glue `Owner` is null, no rule owns it, the deleted flag
was its former carrier, and the substrate card's `0.7.0_AE_CloudOps~X` owns the CARD ROW of a *different*
(Iceberg) object. Last write 2026-07-16T03:40:46Z, **50.7 days**, while the other side of the federated
join refreshes nightly.

---

## What I Did

1. `/watcher` -- lane `~W` was NOT REGISTERED and had no watcher; registered (PID 5984), armed the
   persistent inbox Monitor (task `bi7wil5n2`, `parent-tied: pid 1695612`), confirmed `running`, read and
   READ-acked the COO's GO (msg 94278).
2. `org/XXX.md` Step 1b A-F. B.0 delivery ledger: 1 row, READ 1/1. B.1 `to-check --all --assignee`:
   **2 active TOs, both mine**, 2,315 faces scanned, 0 parse errors, 0 unresolved serials.
3. Read both order faces whole, then executed OS-s-6 and OS-s-7.
4. Wrote 2 result documents, 2 `proof_of_spec` instances (both **VALID rc=0**), and minted the project's
   `INVESTIGATION_v1.md` with 3 rows (3/3 schema-valid).

## Blockers

**Two, both the issuer's cut, neither mine.**

1. `O6-AC1`'s `<invocation>` is `python .tools/comp-iam --help`, but `.tools/comp-iam` is a `#!/bin/bash`
   forwarder -- rc=1, `SyntaxError`, 0 matches for its own `<expect>` string `usage`. `comp-iam --help`
   (the instrument the estate runs) gives rc=0 and 1 match. Since a mechanical criterion's pass "is
   decided by the MATCH and never by your opinion", I did not substitute the working invocation.
   `TO-OS-s-6` stays `pending` until the issuer amends the cut. Row `NFRA_OUTSET-S1`.
2. **Systemic, found by the gate refusing my commit rather than by reading code:** 16 of this project's
   17 faces name their `proof_of_spec` instance by the SHORT stem, while
   `.tools/to-pipeline-gate.py:1261-1270` globs the FULL face stem. An assignee obeying its own face
   writes a file the gate cannot see, and the gate's message ("NO proof-of-spec instance was found
   beside it") points at the assignee rather than at the cut. `TO-OS-s-1` alone carries the correct
   form. Resolved for my two orders by writing both instances under the full stem -- same granted
   folder, the name the mechanism requires -- and recorded in both result docs so no reader is misled.
   The other 15 faces are the issuer's to amend. Row `NFRA_OUTSET-S4`.

## Next Steps

1. Issuer amends `O6-AC1`'s invocation to `comp-iam --help`; this seat re-runs it and flips `TO-OS-s-6`.
2. Issuer routes `NFRA_OUTSET-S2` (comp-find content mode dead) and `NFRA_OUTSET-S3` (third
   simulate false-deny mode) to their owning surfaces -- both are outside this order's `<paths>` grant.
3. `3.0.0_SA_CVO` grades the 4 judgment criteria at L9. No verdict was written on any of them.

---

## Two measurement errors of my own, named

1. **I read an rc that was not the one I wanted.** My first `O6-AC1` run printed `RC=0` -- the rc of a
   trailing `head`, not of `python`. Re-measured with the rc captured before any pipe: rc=1. The defect
   verdict was unchanged, but the wrong number pointed the *exonerating* way. It recurred once more on
   the first proof-of-spec validation (`RC_S6=0` while the tool printed `INVALID (rc=1)`), so I captured
   rc before the pipe on every subsequent check.
2. **I supplied a resource ARN at the wrong grain and nearly believed the result.** `logs:GetLogEvents`
   simulated against a log-STREAM-grain ARN returned `implicitDeny` for a principal holding `*`/`*`. I
   caught it only because that deny is impossible on its face. Against a narrowly-scoped principal it
   would have read as a clean true negative. That became `NFRA_OUTSET-S3`.

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-iam` | `comp-iam refresh-census` | rc=0. APPLIED census at 2026-09-04T21:18:31Z, account 313476888478, 224 roles / 1 group / 7 users. Run BEFORE any APPLIED use per the 24h-TTL trap. Its own `managed_policies_resolved: false` established the 137-role UNRESOLVED partition. **Gap found:** the artifact enumerates roles only -- the 7 users and 1 group are counted in `summary` and detailed nowhere, so the identity that every seat and worker actually uses is invisible to it. That gap is the whole OS-s-6 answer and I had to leave the tool to find it. |
| `comp-iam` | `comp-iam --help` | rc=0, prints `usage` + 17 subcommands. Used as the control proving `O6-AC1`'s intent is satisfiable while its literal invocation is not. |
| `comp-read` | `comp-read <PRD> --for 'federated transport / trino task-def / code_heat / OS-s-6 / OS-s-7 / P2 / P3'` | 270 lines, 37 sections, 37 qualifiers (27 near the queried regions). Surfaced s.7 rows and the s.3 report-host description at :180-183 that grounds the UNREADABLE verdict. |
| `comp-read` | `comp-read .tools/comp-heat --for 'how does comp-heat call the federated transport...'` | 415 lines, 13 sections via python-ast. `cmd_federated` at :348-360 routed me to `.tools/_trino_fed.py` -- the read that fixed the correct object instead of auditing `comp-heat` itself. |
| `comp-read` | `comp-read org/modules/graph/comp_iam_census.py --for 'where is the census written, TTL, vintage'` | 230 lines, 7 sections. Established the vintage/TTL semantics and the "uncovered, never absent" rule for managed policies. |
| `comp-read` | `comp-read .tools/proof-of-spec-check.py --enumerate 'judgment'` | 13 whole-value hits / 0 substring; DOCSTRING=1 COMMENT=1 DEF=0 CODE=11. Gave the canonical judgment-row form (`UNVERIFIABLE-BY-INSTRUMENT` + `status_reason`) at :1083-1084 and the refusal at :86-87. |
| `comp-find` | `comp-find 'trino'`, `'RunTask'`, `'code_heat'`, `'NFRA_OUTSET' --limit 5` | **rc=124 on every content-mode call, zero bytes stdout AND stderr, including the positive control.** NO MEASUREMENT obtained. **Gap found -> `NFRA_OUTSET-S2`:** a timed-out comp-find is byte-identical to a clean zero-hit search and suppresses the printed denominator Rule 21 depends on. Searches completed with native `Grep` (Rule 21 carve-out); no finding rests on a comp-find content result. |
| `comp-find` | `comp-find --hidden iam_live_census` | Returned promptly with a proper header and the correct "A count over a path that is not there is not a zero -- it is NO MEASUREMENT" error. The contrast localises S2 to CONTENT mode, not to the rail or the shims. |
| `comp-to` | `comp-to NFRA_OUTSET.TO-OS-s-6` | rc=0, session TO_ID set race-free per seat+session. |
| `surprise-row-gate` / `jsonschema` | validate 3 rows against `investigation_item.schema.json` | 3/3 SCHEMA VALID. |
| `proof-of-spec-check` | both instances, criterion lists pinned | Both **VALID (rc=0)**, violations=0, after a first pass that correctly refused them for a missing `controls.determinism` and `controls/mutant.status`. |

**AE role minimums -- truthful non-application.** `comp-pipescript deployed` / `postdeps`: N/A, no gold
run was triggered. `comp-iam gaps`: N/A, no `iam.tf` was changed. `comp-blast`: N/A, no infra change --
both orders are READ-ONLY audits and nothing on AWS was created, modified or deleted.
