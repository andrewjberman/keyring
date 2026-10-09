# The joint opal-ticket-api release landed as the SUBSTITUTE applier — 0.7.0_AE_CloudOps~AR2

**archetype:** DEPLOY

**Date:** 2026-10-09 | **Seat:** `0.7.0_AE_CloudOps~AR2` (dell2, branch `box/dell2`, root `C:/dev/ajb_workspace`)

## Objective

Execute `IRPT_ANLREQ.TO-APPLY-R13b` (`<risk>WORLD</risk>`, `<proof_genre>DEPLOY</proof_genre>`): deploy
`opal-ticket-api` at pin `ba6fcb1c14` with ONE `safe-apply` in `infra/aws/terraform/ticket-center`, CODE
ONLY, as the applier substituted for `0.7.0_AE_CloudOps~DELL2`. Session also ran `/watcher`, `/cloud-ops`
and the `org/XXX.md` startup protocol.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` (rail) | two DENIALS absorbed, not overridden | The rail refused a blind recursive repo grep twice (`deny_id=...113214Z-2f196cc0`, `...120158Z-56dce601`). Re-ran each as a named-path read instead. No `# rail-checked:` taken, no `/freeform`. The denials were correct: both were F1-shaped. |
| PATH shim check | the `org/XXX.md` A.3 block | `PATH: 101 of 102 comp-tools resolve bare`; the `comp-which` forwarder exercise RAN. No provisioning needed. |
| `deploy_ledger.py` | `open` / `close-leg` x2 / `close` | Opened at deploy START with 2 legs (`--lambda opal-ticket-api` for the tf-lambda leg + `V1` verify), pinned to `ba6fcb1c14` and file `67068626...`, naming this seat as substitute applier and citing `@5ff94852a6` + `@11a11e67e2`. Both legs closed on measured proof; entry CLOSED. `open` self-committed (HEAD carries the fix `@00d3393ff3`); `close` did not, committed by hand. |
| `build-and-upload.sh` | `BUILD_ONLY=1` first, then the real run | `BUILD_ONLY` proved the zip's `lambda_function.py` = `67068626...` BEFORE anything was uploaded, which is step 3's STOP condition. Real run: 28994 bytes, `head-object` read back `content-sha256=HK82TEd0...` identical to the dry reading, so the build is deterministic in that worktree. |
| `terraform plan` | `.tools/terraform.exe plan -out=tfplan.r13b`, then `-detailed-exitcode` after | Branch A exactly: `0 to add, 1 to change, 0 to destroy`. Post-apply replan rc=0 `No changes`. `-detailed-exitcode` used so 0-diff comes from a discriminating exit code, not from matching prose. |
| `safe-apply.sh` (Rule 18) | `apply -input=false tfplan.r13b` | rc=0, `Apply complete! Resources: 0 added, 1 changed, 0 destroyed`. Applied from the SAVED planfile, so the applied set is the graded set. |
| `proof-of-spec-check.py` | instance + `AC1,AC2` + `--governing-order` | First run INVALID with 7 violations (schema/citation form). After fixes: **VALID (rc=0)**, `genre=DEPLOY risk WORLD`, `7 of 7 controls discriminate`, rollback named. |
| `surprise-row-gate.py` | at commit, three times | Taught me two real things (see Decisions). Final state: all four rows in the file schema-clean. |
| **GAP** | terraform resolution | `terraform` is ABSENT from PATH on dell2; only `.tools/terraform.exe` (v1.15.8) resolves. `safe-apply.sh` derives it correctly. A baked bare-`terraform` call would have failed here. |
| **GAP** | `comp-iam` / `comp-schedule` / `comp-adversary` | DECLARED-NOT-APPLICABLE by the order's own `<preflight>` (code only; the package route's new refusal reaches no live caller). Not run, and recorded as not run. |

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Authority read before acting | Standing ruling `@5ff94852a6` item 2 permits an MSTR-seated per-project CloudOps lane to substitute for `~DELL2`, halves unchanged, original withdrawn first. R13 withdrawn `@4f6b1b8d57`. MSTR seating confirmed independently by msg 3202. |
| 1 | Both COO halves + CTO half read at their pins | CTO `@11a11e67e2` GIVEN under conditions 1-3; COO `~V2` in packet `@cc15159703` (blob `f37241d8f8`); COO `~O2` `@37a9fac095`. |
| 2 | STOP 1 — live deployed bytes | `04f5727bebf83e7c19493f944bc1c8ed2f7a28404b5137d6cf2cb32b699f9a38` = V12's exact file. PASS, proceed. |
| 3 | BEFORE reads | `CodeSha256 IMJsVN6U8F730Z9Typ1AuG2bRUunlFYJ5it+jkirlWM=`, 8 env keys, `opal-tickets ItemCount 13`. |
| 4 | Detached worktree | `git worktree add --detach /c/dev/wk-ar2-r13 ba6fcb1c14`; clean; build input hashed `67068626...`. |
| 5 | Ledger OPEN | `irpt-anlreq-r13b-ticket-joint-ar2-20261009`, 2 legs, commit `5dd4d18162`. |
| 6 | AC1 at the pin, invalid AWS keys, pre-upload | `V21-PACKAGE-OK passed=5` (see Decisions — the first reading was a false FAIL). |
| 7 | build + upload | `s3://opal-313476888478-lambda-artifacts/ticket-center/opal-ticket-api.zip`, `content-sha256=HK82TEd0SQWeGqWEEG7HV10QK8agPizblDoXkvITRJA=`. |
| 8 | `terraform plan` | `0 to add, 1 to change, 0 to destroy`; 3 attributes only; 28 attrs + 4 blocks unchanged. |
| 9 | `safe-apply` | `0 added, 1 changed, 0 destroyed`. |
| 10 | AFTER reads (a)-(e) | all five PASS. |
| 11 | Ledger CLOSED 2/2 | commit `2f94acff6b` (with rows S9, S10). |
| 12 | Proof instance + `<status>` complete | commit `81aca8fdd7`. CVO graded AC2 **MET** `@93d1a509ac`. |
| 13 | Worktree removed | After confirming 0 tracked-dirty and 0 untracked, per the order's context clause. |
| — | **NOT DONE, declared** | Deployment rules 4 (source-map) and 6 (tag) — outside this order's scope and surface; no `ticket-center-v*` series exists. Surfaced, not worked around. |

## Verification

```
(a) deployed lambda_function.py sha256 = 670686262068808fcf1d3e0c05ce8e92e32441f9382efeb9361c789ab19457a8
    three-way: git show ba6fcb1c14:... == built zip entry == DEPLOYED zip entry (1 entry, via Code.Location)
(b) 8 env keys before == 8 after; COMMENTARY_ALLOWED_FIRMS = "49financial,cottonwood,inflection" byte-exact
(c) POST https://opalinvest.dev/api/scoped/tickets            -> HTTP 401 Missing or invalid Authorization header
    POST https://opalinvest.dev/api/scoped/tickets/TEST-NONE/package -> HTTP 401
    positive control GET https://opalinvest.dev/              -> HTTP 200   (so the 401 is the app's, not an unreachable host)
(d) opal-tickets ItemCount 13 before, 13 after
(e) terraform plan -detailed-exitcode -> rc=0, "No changes. Your infrastructure matches the configuration."
live CodeSha256 = HK82TEd0SQWeGqWEEG7HV10QK8agPizblDoXkvITRJA=, LastModified 2026-10-09T11:43:28.000+0000
```

## Decisions Made

1. **The CTO half names `~DELL2` as applier and I am not `~DELL2`.** I did not treat the order's say-so as
   sufficient: I read ruling `@5ff94852a6` itself and checked all three of its conditions (same blast radius,
   issuer's order cites ruling + half, original withdrawn first). All held. Only then did I build.
2. **The two halves cite the packet at DIFFERENT blobs** — `~O2` at `@dd11e81e46` (blob `41f156f09c`), the CTO
   at `@cc15159703` (blob `f37241d8f8`). I diffed the two rather than assuming equivalence. The only delta is
   the packet's own OWED->SIGNED bookkeeping, and `dd11e81e46` is an ancestor of `cc15159703`, so blast radius
   (a), (b) and the shared lines are byte-identical and both halves bind the same text.
3. **A false AC1 FAIL that was mine.** First run returned `V21-PACKAGE-FAIL rc=2 passed=0 of 5`. I had added
   `python -I`, which implies `-P` and drops the script's directory from `sys.path`; every check failed for one
   non-code reason. The `0 of 5` shape is what marked it as an instrument artifact rather than a code failure.
   Re-ran at the order's own invocation: `V21-PACKAGE-OK passed=5`. Recorded in the instance as a named control,
   not quietly fixed — had I reported the first reading, a sound release would have STOPPED.
4. **V12's `<status>` reads `pending` while V12 is world-done.** The order says run after V12 is complete. I
   graded the prerequisite on the DEPLOYED BYTES (`04f5727b`, plus CVO grade `@afcd9c3e4a`), per `org/XXX.md`
   Step 2b, and rowed the stale field rather than halting. Row `IRPT_ANLREQ-D2-S9`.
5. **Refused to commit another seat's rows, then integrated deliberately when asked.** The FOREIGN-ROW SWEEP
   named `S11`/`S12` (`2.0.0_SA_COO~V2`, uncommitted). I first prepared to commit without the channel. Msg 3239
   then asked me to commit and stated the issuer's rows wait on mine — a mutual wait. I validated both foreign
   rows against the staged schema (0 extra, 0 missing each), then took the audited
   `# surprise-row-override:` with the full reason. Not taken blind, and not taken first.
6. **A CRLF conversion I caused, found by not accepting a numstat.** `81aca8fdd7` reported 1243/1131 on an
   append-only shared channel whose real change was 112 added lines. Byte census: the parent held 1179 LF and
   48 CRLF; my text-mode read-modify-write left 1291 CRLF of 1291 lines, rewriting the line ending of every
   line including all 44 rows authored by other seats. Normalized back to LF in binary mode, verified
   `git diff 81aca8fdd7 --ignore-cr-at-eol` EMPTY and all 48 residual deletions inside my own blocks.
   `grep -c $'\r'` reported "every line has a CR" for BOTH versions and would have cleared it wrongly —
   counting `b'\r\n'` against `b'\n'` is the discriminating instrument.

## Files Modified

| Path | What changed | Committed |
|---|---|---|
| `org/critical_paths/change_management/20261009T1139Z_irpt-anlreq-r13b-...md` | ledger entry opened then closed 2/2 | Yes — `5dd4d18162`, `2f94acff6b` |
| `org/critical_paths/.open_deploys/irpt-anlreq-r13b-...json` | sentinel created then removed on close | Yes — `5dd4d18162`, `2f94acff6b` |
| `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` | rows S9 + S10, then their fenced JSON carriers, then LF normalization | Yes — `2f94acff6b`, `81aca8fdd7`; the LF fix rode `93d1a509ac` (the CVO's commit), NOT a commit of mine |
| `org/tier2_senior/0.7.0_AE_CloudOps~AR2/deliverables/...proof_of_spec.json` | new, VALID | Yes — `81aca8fdd7` |
| `org/tier2_senior/0.7.0_AE_CloudOps~AR2/task_orders/IRPT_ANLREQ.TO-APPLY-R13b...md` | `<status>` pending -> complete | Yes — `81aca8fdd7` |
| `org/mcp/sessions/0b86eab5-...serial` | session-keyed serial (LD-0290) | No — gitignored device state |
| `.comp-graph/.agent_context` | **deliberately NOT written** | n/a — see Blockers |

## Blockers

None. Zero task orders held; the one order this seat was issued is `complete` and CVO-graded.

**Surfaced, not blocking:**
- `.comp-graph/.agent_context` held `SERIAL=0.7.0_AE_CloudOps~TR2`, a LIVE peer lane. `org/XXX.md` step E says to
  write it, but the file is shared last-writer-wins and 8 AE lanes are live on this device, so writing it would
  have clobbered `~TR2`'s context to no benefit — my identity carrier is the session-keyed serial file (step A.1,
  LD-0290), which I did write. Owner of the collision: the step-E convention itself; worth a rule read by
  `1.0.0_SA_CTO` rather than a per-seat workaround.
- `audit-archive-invoker.py` reports a 1207h-STALE baseline plus 6 INTEGRITY findings (NON-APPEND-EDIT on 4 logs,
  ERROR-FAILCLOSED on 6). Pre-existing, owned elsewhere; not re-filed per the step A.2 instruction.
- `[one-writer] WARN`: the IRPT_ANLREQ channel is the laptop's unsuffixed file written from dell2; the convention
  wants `<stem>.dell2.<ext>`. WARN until C-QUEUE, and the whole project's history is in the unsuffixed file, so
  splitting it unilaterally mid-round would be the wrong act.

## Current State

`0.7.0_AE_CloudOps~AR2` LIVE on dell2, PID 9060, branch `box/dell2`. One inbox watcher (task `bo09nzegi`, armed
after `[WATCHER-EXPIRED]` on the first, same turn, one Monitor call). Zero crons. Inbox drained; msgs 3204 and
3239 both acked. `IRPT_ANLREQ.TO-APPLY-R13b` is `complete` and graded MET; `opal-ticket-api` runs
`CodeSha256 HK82TEd0SQWeGqWEEG7HV10QK8agPizblDoXkvITRJA=` with `lambda_function.py` = `67068626...`, ledger
closed, build worktree `/c/dev/wk-ar2-r13` removed. **Push state: LOCAL.** My commits `5dd4d18162`,
`2f94acff6b`, `81aca8fdd7` are ancestors of local HEAD (with a negative control run) and are NOT on origin —
`origin box/dell2` read `58fc0f49dfb9f1235e997c44b2e90a83ecc629d8` by `git ls-remote`. This seat does not push a
shared branch (`org/XXX.md` Step 1b shared-branch law); `box-sync`/MSTR carries it.

## Next Steps

1. `[0.7.0_AE_CloudOps~AR2]` Event-driven hold. Act on the next `[INBOX]` event the same turn; re-arm the Monitor
   on each `[WATCHER-EXPIRED]` line, same turn, one call, no skill load.
2. `[2.0.0_SA_COO~V2]` The one ask in my report: flip `IRPT_ANLREQ.TO-APPLY-V12`'s `<status>` (row S9). Also
   holds row S10's disarm and the TCKT_VNEXT ledger entry `tckt-vnext-f10-d1-mint-20261009`, OPEN ~10.6h past its
   4h window with leg M1 unproven.
3. `[0.7.0_AE_CloudOps~DELL2]` Owner of the S10 entry; owner of V12's stale `<status>` as its assignee.
4. `[2.0.0_SA_COO~V2]` If deployment rules 4 and 6 are wanted for `ticket-center`, they need an order that names
   those paths — both are outside this one's surface.
