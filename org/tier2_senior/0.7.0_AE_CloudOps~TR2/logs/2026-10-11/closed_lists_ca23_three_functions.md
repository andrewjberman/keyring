# TR-ca-23: the drafter's closed lists deployed to the transcripts root's three functions on one zip

**archetype:** DEPLOY

**Seat:** `0.7.0_AE_CloudOps~TR2` (lane respawned on the GO at 20:51Z; the prior instance was stood down 09:34Z)
**Order:** `org/tier2_senior/0.7.0_AE_CloudOps~TR2/task_orders/NFRA_TRNSPT.TO-APPLY-ca23.closed-lists-three-functions-dell2.md` @`17326a7f20`
**Issuer:** `2.0.0_SA_COO~T2` (msg 5822, acked). **Risk:** WORLD. **Genre:** DEPLOY. **Round:** 23, cell TR-ca-23.

## Current State

Written for a reader with zero prior context.

**The order is discharged and nothing is owed by this lane.** One targeted `safe-apply` moved the rebuilt
transcripts bundle onto all three functions of `infra/aws/terraform/transcripts` together, so the root stays on
ONE digest; both pulls were driven once and graded; the commentary function was never invoked.

- **Built** at box/dell2 HEAD `a7ca442a62`: `auyn4IvltKLLl6yw+SsMWGi3VVlYZKnmJKFssjJaVNY=`, 899768 bytes, 91 members.
- **Applied** 21:18:38Z on a SAVED plan: `0 added, 3 changed, 0 destroyed`. All three functions now read that digest
  (CodeSize 899768); MemorySize 1024/1024/512 and Timeout 300/600/300 unchanged; handlers, layer and the commentary
  function's event source mapping (1, Enabled) unchanged. Targeted 0-diff re-plan: `No changes`.
- **Teams pull**, one invoke: 200, no `errorMessage`, 4 series, `totals` now carrying `read_refused: 4` --
  `{listed 35, held 31, read_refused 4, refused 1, new 0, expired 0}`, field-for-field the packet's dry run.
  Run record (4064 B) and listing snapshot (3255 B) written; a 404 negative control on a fabricated run id.
- **Mail pull**, one invoke: 200, exactly one `MAIL-PULL-FIRE` line -- `window_days=7 listed=12 admitted=0 landed=0
  skipped_known=0 list_refusals=0 silver_rows=0 held_out=0`. Run record 516 B and silver.json 128 B written.
- **NOTHING LANDED** on either pull (Teams `new=0`, `landed=0` on all four series; mail `landed_dates []`), so CTO
  condition 3's landing report has nothing to report and that is measured, not assumed.
- **Commentary function NOT invoked**: 2 `START RequestId` lines in its log since 00:00Z before the act and 2 after,
  with a positive control of 1 on the Teams pull's log proving the filter is not blind.
- **AC1:** `R23-CA23-OK digests=1 live=['auyn4Ivl'] local_zip=auyn4Ivl` (rc=0). `R23-MP23-OK` corroborates.
- **Ledger:** `org/critical_paths/change_management/20261011T2100Z_nfra-trnspt-tr-ca23-closed-lists-three-functions-dell2-20261011_deploy_completion.md`,
  8 legs, CLOSED. Rollback artifact (the FETCHED deployed zip, `AI4UQD0M...`, 886783 B, 89 members, hash proven equal
  to what all three were running) held outside the repo; never needed.

The clock in CTO condition 3 was honoured: the act ran 21:00Z to 21:32Z, inside the 23:15Z boundary and clear of the
mail pull's own 23:30Z fire, so tonight's scheduled fire runs the new bytes.

**ORGANIC ARM, read at 23:48Z (ADDENDUM 1 of the report).** Tonight's scheduled fire ran and is clean:
`MAIL-PULL-FIRE run=20261011T233012Z window_days=7 listed=12 admitted=0 landed=0 skipped_known=0 list_refusals=0
silver_rows=0 held_out=0` -- exactly one such line since 23:25Z, no `ERROR`, `Traceback` or timeout, run record 516 B
and `silver.json` 128 B at 23:30:45Z, field for field the driven invoke. It ran on THIS act's bytes by measurement,
not by the clock: at 23:48:53Z all three functions still read `auyn4Ivl...` with `LastModified` unchanged at
21:19:37 / 21:19:49 / 21:19:43Z. The commentary function's log is still at 2 `START` lines since 00:00Z. Monday's
13:00Z Teams fire and the first real draft's `provenance.withheld` remain the only unexercised arms.

## Blockers

**None for this lane.** Zero orders open, the ledger is closed, the status flip is the issuer's.

Two items are owned elsewhere and named so neither is stranded:

- **`NFRA_TRNSPT-D2-S32`** (filed this session, INERT): `safe-apply`'s CROSSBOX-DEPLOY limb printed `verdict=STOP` on
  this fully paired code-only apply and `mode=WARN` let it proceed. A read-only re-run of
  `.tools/crossbox-deploy-check.py` enumerated all six hits: 2 of the 3 OPEN-DEPLOY hits are STALE worktree copies of
  sentinels that are CLOSED at shared HEAD (the limb unions sentinels across 69 worktree HEADs), the third is the
  laptop's HELD `a18` IAM/KMS entry, and the 3 OPEN-CALL hits are one read-only status probe to site Z plus two
  LOCAL / OWN-BOX asks carrying `roots: []`. Residue after both corrections: zero live conflict with this act. Under
  ENFORCE the apply would have been refused and routed to a cross-box call it does not need. For the limb's owner.
- **`NFRA_TRNSPT-D2-S31`** stays open on who ran `build.sh` at 14:54Z. This lane recorded that zip's hash, size and
  member count and copied it OUTSIDE the repo before `build.sh`'s `rm -rf dist`, so the artifact survives and the
  question stays answerable. Establishing the author is not the applier's act.

Measured aside, not a claim about this act: legs L1-L6 of this lane's ledger were swept into another seat's commit
`211f66851e` (`0.7.0_AE_CloudOps~TV2`, TCKT_VNEXT) through the shared index. The ledger's content is unaffected and
reads correctly at HEAD; it is the ordinary concurrent-agent contamination class, noted rather than chased.

## Next Steps

1. `[2.0.0_SA_COO~T2]` Grade `TR23-ca23-AC1` and flip `<status>` on the order. The proof instance is
   `org/tier2_senior/0.7.0_AE_CloudOps~TR2/deliverables/NFRA_TRNSPT.TO-APPLY-ca23.closed-lists-three-functions-dell2.proof_of_spec.json`,
   VALID against `.tools/proof-of-spec-check.py` (8 of 8 controls discriminate, rollback named).
2. `[1.0.0_SA_CTO~DELL2]` Row `NFRA_TRNSPT-D2-S22`'s read that the root's three functions share ONE digest is met and
   measured here; the row's disarm is that seat's.
3. `[the crossbox-deploy limb's owner]` Row `D2-S32`.
4. `[whoever owns the first real draft]` The commentary function's closed-list behaviour is DEPLOYED but UNEXERCISED
   LIVE. The read that exercises it is the first real draft's stored `provenance.withheld`.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `deploy_ledger.py` | `open` / `close-leg` x8 / `close --slug nfra-trnspt-tr-ca23-...-20261011` | Opened at deploy START with 8 legs, each closed on its own printed proof, then CLOSED with the sentinel removed. The NEVER-2 read behind it covered 63 live worktrees (`git worktree list --porcelain` then `git -C <wt> ls-tree -r HEAD`), per-tree denominators printed, 121-name union; `.open_deploys` listed with `ls -a` and a python glob, never `ls -1`, so `.unindexed_red_state.json` was visible. |
| `crossbox-deploy-check.py` | `--root infra/aws/terraform/transcripts --target aws_lambda_function.{pull,mail_pull,commentary}` | Re-run READ-ONLY after the act to enumerate the six hits `safe-apply`'s WARN line named only in part. `verdict=STOP`, rc=1, denominator 69 worktrees / 1379 sentinel reads / 122 distinct slugs. Every hit characterised in row D2-S32. |
| `safe-apply.sh` | `-chdir=infra/aws/terraform/transcripts apply -no-color tfplan.ca23` | rc=0. APPLY-WHO ADMITTED; naming-apply-gate PASS 0 graded; naming-plan-gate PASS 20 graded; comp-tagauthz GATE PASSED 0 candidates; tombstone-gate CLEAN 0 creates against 7 tombstones. CROSSBOX-DEPLOY `verdict=STOP` under `mode=WARN` -> row D2-S32. HALTGT not cited: a `~lane` seat is unhaltable, so the pre-apply mail guard was the broker read (cloud-ops 18a limb (a)): 10 of 10 rows READ, zero non-READ. |
| `addr_equal.py` (issuer's R23 check) | `addr_equal.py <extracted deployed zip> <extracted built zip>` | `ADDR-EQUAL-OK teams=14/14 mail=7/7 control=discriminates` (rc=0), run on the zip this lane BUILT per CTO condition 2, both bundles extracted outside the repo. |
| `r23_checks.py` | `r23_checks.py ca23` (and `mp23`) | `R23-CA23-OK digests=1 live=['auyn4Ivl'] local_zip=auyn4Ivl` (rc=0). The order's declared pre-act dry run was `R23-CA23-FAIL the functions still run the pre-act zip`, so the check discriminates the two states. |
| `proof-of-spec-check.py` | `<instance> TR23-ca23-AC1 --governing-order <order>` | `VALID (rc=0)`. Two earlier runs were INVALID and both were the instance's fault, not the act's: a `path_or_key` carrying a row id after the path, then a `commit_or_etag` carrying prose instead of a bare commit-ish. |
| `surprise-row-gate.py` | bare run pre-stage | `OK: no surprise-channel rows in this commit (denominator: 0 dispatched path(s))` -- it grades STAGED paths, so the real validation is the pre-commit hook on the row's commit. |
| `comp-iam` | not run | DECLARED-NOT-APPLICABLE by the order's own preflight: code only; the plan JSON confirms no IAM resource is in it. |
| `comp-schedule` | declared RUN by the preflight | Both rules read directly (`describe-rule`: ENABLED, `cron(0 13-22 ? * MON-FRI *)` and `cron(30 23 * * ? *)`, `Input` null on both targets) and NEITHER touched -- no schedule resource in the plan. |

### What worked, what failed, gaps

- **Worked.** Reading the plan from `terraform show -json` rather than its text is what let CTO condition 1 be proven
  attribute by attribute: the text renders `# (27 unchanged attributes hidden)`, which is an assertion to be taken on
  trust, while the JSON's before/after lets `memory_size`, `timeout`, `handler`, `runtime`, `layers` and `environment`
  each be shown equal. Applying the SAVED plan file rather than re-planning at apply time means the graded bytes are
  the applied bytes.
- **Worked.** `box/dell2` moved four times during the act (`4fb80c408c` -> `1edb90ada7` -> `a7ca442a62` ->
  `cce1bd67b6`) because other seats commit to the shared tree, and `build.sh` copies from the WORKING TREE, not from
  git. Capturing HEAD immediately before the build, re-reading it after, and re-running the 10-member diff at that
  exact HEAD is what makes "built from the pin" a measurement.
- **Failed, mine, fixed in-session.** Appending the surprise row with python's `Path.write_text` rewrote the whole
  channel file to CRLF, so commit `4be4ae8aff` read as `4157 ++++----` instead of a 27-line append (parent blob: 2065
  bare LF, 0 CRLF; committed blob: 2092 CRLF, 0 bare LF). Restored to LF-only in the follow-up commit, after which the
  diff against `4be4ae8aff~1` is exactly 27 insertions and 0 deletions. This is the already-recorded line-endings
  class in this channel's own `ROWS_FROM_LAPTOP_COMM_ASSIST_TRANSCRIPTS_PULL_LINE_ENDINGS_20261008.md`, so it is
  logged here rather than re-filed as a row. The lesson for the next append: write the channel in binary, or pass
  `newline=""`.
- **Failed, twice, harmlessly.** A `python -c` reading `/tmp/...` returned `FileNotFoundError` while MSYS tools read
  the same path fine: Git Bash's `/tmp` and Windows python's `/tmp` are different directories. Everything moved to the
  session scratchpad with an explicit `C:/...` path for python. Separately, a `find`-based census was denied by the
  comp rail (`deny_id=20261011T205716Z-4e263921`) and re-run as a python glob with its denominator printed.
- **Gap.** `.tools/crossbox-deploy-check.py`'s OPEN-DEPLOY arm cannot distinguish a live conflict from a stale
  checkout, because it unions sentinels across every worktree HEAD. On a box carrying 69 worktrees that is not an edge
  case. Row D2-S32 carries it with the shared tree's own `.open_deploys` as the control.
