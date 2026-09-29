# The cot login retry goes live, and the run that was supposed to prove it never logged in — 0.6.2_AE_PartnerETL~S

**Date:** 2026-09-29
**Task Order:** IRPT_BCKEND.TO-IB-m21-212 Part 2 (COMPLETE)
**Status:** COMPLETE
**archetype:** DEPLOY

Delta log. The prior entry (`session_0520Z-0850Z_...`) covers 211 and 212 Part 1.

---

## Objective

Land Part 2 on the issuer's GO: deploy the ported cot login script and its env file as one act under a ledger,
verify the running path, and close V2 on the first real run. Four amendments and one CTO ruling arrived during
the window and changed V2's definition twice.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open --slug cot-login-retry-s165-m-20260929 --leg A1..V2`, then `close-leg` x4, `hold`, `hold --release`, `close` | PASS | The `hold` verb is the one that mattered: when V2 turned out to be ungated, HELD with a named external gate and a reread date read as KNOWN-HELD instead of aging into a false RED. Nothing else in the estate would have expressed that honestly. |
| naming-gate.py | `--diff <staged .js> --post-from-index` | PASS | `WARN 7 graded` rc=0, zero REFUSE, against `REFUSE 15` before group C. This is the measurement amendment 2 required and the only proof that the port passes with no waiver. |
| proof-of-spec-check.py | `<instance> IBM21-212-AC1 --governing-order <TO>` | PASS | VALID rc=0: 0 violations, alignment 1/1 both directions, 3 of 3 surprises resolving, invocation 1/1, 6 of 6 artifacts resolved, 2 of them CONTENT-resolved off `introduces`. |
| surprise-row-gate.py | inside each `safe-commit` run | PASS (after a routed refusal) | Refused once on a CO-WORKER's row (`class: BLOCKER`, not in the ratified enum) riding the shared append-only channel. Routed to its author rather than overridden; that seat fixed it at `b88b92c57b`. |
| safe-commit.sh / safe-merge.sh | per commit / per drain | PASS | Three audited lane overrides on `.gitattributes`, each committed ALONE with its authority stated. |
| comp-read | `.tools/naming-gate.py --for "per-path exemption..."` (prior window) | PASS | Still the basis for group C's design: it is what established that `js_literals` has no builder-call skip. |
| aws events describe-rule | `--name cot-session-complete` | PASS | Not a compiler tool, but the load-bearing read of the window: it predicted the chain re-run BEFORE the login fired. |

**What worked:** `deploy_ledger.py hold` and `aws events describe-rule`. The first kept an honest ledger state
through a 2-hour gate; the second turned a side effect into a prediction instead of a surprise.

**What failed:** nothing returned a wrong answer. My own V1 read-back command was under-specified — it printed a
`grep -c` COUNT of the config lines where the acceptance checker greps for the LINES. The issuer caught it at
10:2xZ, not me, and that is the honest attribution.

**Gap found:** same as the prior window and now twice as costly — nothing answers "what will this gate refuse,
and what is the lawful escape". Add to it: nothing surfaces "what EventBridge rules key on the document I am
about to invoke". I got that by hand from `describe-rule`; a `comp-blast <ssm-document>` that walked
document → rule → target would have shown the chain re-run in one call.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Open the ledger BEFORE any upload | `ad0f36789b`, 4 legs declared |
| 2 | Capture the rollback baseline from S3 | env 1200 B md5 `9b55e03c…`, **verified byte-identical to the box copy the GO names**; .js 35049 B ETag `28dd27a0…` |
| 3 | A1: upload BLOB bytes, both files | ETags `7d37465b…` / `8e879af5…` = the blob md5s; 0 CR verified before upload |
| 4 | A2: S3 → box pull | SSM `deeb49bb` Success rc=0, `PULL-OK` |
| 5 | V1: a SEPARATE read-only command | running md5s exact, `CR_COUNT=0`, 4 of 4 config lines, `NODE-CHECK-OK` on the box's node |
| 6 | 11:30:32Z scheduled trigger | **SKIPPED the login** — Lever A, cookie age 1.7d ≤ 7d — ran bronze/silver/gold instead |
| 7 | HOLD the ledger | external gate named as Lever A, reread 2026-10-05 |
| 8 | Amendment 4 + CTO egress ruling | V2 re-scoped to ONE forced login |
| 9 | V2: one forced `opal-cot-bd-session-fetch` | SSM `edb17c3d` Success rc=0; session advanced |
| 10 | Close V2, release the hold, CLOSE the ledger | all 4 legs proven, sentinel removed |
| 11 | `r21_s165_retry_live.py` | `RETRY-LIVE 7d37465ba68e` rc=0 |
| 12 | proof-of-spec + `complete` flip + drain | `0e01f2b642`, drained `ad703ba12e` |

---

## Verification

**The session advanced** — measured on `blackdiamond/cot/session` before and after, reading `captured_at` and
the device cookie NAME only, never a cookie value:

```
captured_at_before = 2026-09-27T18:42:27.162Z
captured_at_after  = 2026-09-29T11:53:43.537Z
```

**The box's own log exercises all three hunk groups.** This is the part that matters, because a deploy that is
merely PRESENT proves nothing about the code path:

```
[bd-auto-login] partner=cot (creds/session/relay -> blackdiamond/cot/*)     <- group C: required firm id
[bd-auto-login] login attempt 1/3                                          <- group A: only in the port
[bd-auto-login] device-trust: bd_DeviceRegistration injected               <- group C: env-sourced cookie name
[bd-auto-login] step 2..4: state=MFA_OTP  -> OTP adapter (gateway)
[bd-auto-login] step 5: state=LOGGED_IN
[bd-auto-login] OK: fresh session written to SM (blackdiamond/cot/session)  <- group B: rewrapped persist
[orchestrator] cot BD auto-login exit rc=0
```

**Not exercised, and the log says so rather than implying coverage:** attempt 1 succeeded, so the retry's
FAILURE branch never fired. Its recovery is proven only by the local harness (7 of 7 arms). ABSENT is not
EXERCISED-AGAINST. The next real discriminator is a genuine transient failure, or the 2026-10-05 scheduled mint.

**The knock-on, predicted then observed:** `cot-session-complete` is ENABLED and keys on exactly
`document-name: opal-cot-bd-session-fetch` + `status: Success`, target the trigger Lambda. So the login re-ran
the chain: bronze `c683e7b5` Success, silver `c590b10f` Success, gold `b332fd76`. Measured before firing,
flagged on the broker, and today's first chain had already completed at 11:32Z, so nothing collided.

---

## Decisions Made

1. **Verified the egress authorization instead of accepting the relay.** A vendor sign-in is a CLAUDE.md hard
   stop without Andrew's word. I printed the Andrew-direct's bytes at the cited commit (`4c330ce53c`) rather
   than grepping for the quote, and — because that record says the word "lapses when this `1.0.0_SA_CTO`
   session ends" — I checked the CTO was LIVE (last seen 3s) before firing. Its written scope list enumerates
   COO lanes and their worker subagents and does not name my serial; I did **not** adjudicate that narrower,
   per the surface-don't-adjudicate rule, because the CTO ruled on this exact call (102764) and the issuer
   relayed it naming both.
2. **Invoked the SSM document directly, having established there is no force mode.** The trigger Lambda's
   modes are session-check / bronze-run / silver-run / gold-run / session-refresh, and only a non-live cookie
   makes Lever A fall through. Faking that condition by touching the session secret was never an option, so
   the faithful path was the document the Lambda itself dispatches, with the Lambda's own 1800s timeout and no
   parameters. Named in the ledger as a deliberate Lever-A bypass.
3. **Kept V1's verification in a separate command from A2's deploy**, so the proof is an independent read and
   not the deploying command's self-report.
4. **HELD the ledger rather than let it age.** The deploy was fully landed but UNEXERCISED; OPEN would have
   gone RED at 6h and implied a half-landed deploy, which was false. HELD with a named gate and a reread date
   says the true thing.
5. **Did not take the surprise-row override** when a co-worker's malformed row blocked my commit. The override
   would have landed a schema violation under my author line; routing it cost one message and they fixed it.
6. **Fixed the env line-ending hazard before leg A1, not after.** The working copy carried 35 CR while the blob
   was LF, and A1 uploads for a file the box SOURCES WITH BASH.

---

## Files Modified

| File | Commit | What |
|------|--------|------|
| `org/critical_paths/change_management/20260929T0931Z_cot-login-retry-s165-m-20260929_deploy_completion.md` | `ad0f36789b` → `0e01f2b642` | the ledger: opened, 4 legs closed, held, released, CLOSED |
| `org/critical_paths/.open_deploys/cot-login-retry-s165-m-20260929.json` | `ad0f36789b` → `0e01f2b642` | sentinel, created at open and removed at close |
| `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S165_RETRY_DEPLOY_20260929.json` | `c7f2e91e6d`, `d7044697f9`, `0e01f2b642` | the read-back JSON; `command_id` repointed after the issuer's AC1 read |
| `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.6.2_AE_PartnerETL~S/IRPT_BCKEND.TO-IB-m21-212....proof_of_spec.json` | `0e01f2b642` | instance, VALID rc=0 |
| `org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-m21-212....md` | `0e01f2b642` | `<status>` → complete |
| `.gitattributes` | `626033ace0`, `2a4c589512` | `*.env text eol=lf`, then a bare-CR repair to its own comment |
| `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` | `b88b92c57b` | row S202 (swept into a co-worker's commit by the shared-channel race; duplicates the issuer's S201) |

**S3 objects written:** `s3://opal-313476888478-lambda-artifacts/ec2/bd-cot-auto-login/bd_49f_auto_login.js`
(VersionId `WZpnhv6I66AqZYUzsS.d3BVAoU37OMKD`) and `.../secret-ids.env` (VersionId
`lbA4Qva2uA1d67GDfkNpF6SNijwuTsoc`). **Box changed:** `/opt/bd-cot-auto-login/` both files, on
`i-0643a5bee8a8feabf`.

**Drains to CLOUD:** `5110c2688e`, `722de3baa2`, `ad703ba12e`.
**Push state:** LOCAL. `origin/CLOUD` read `15655f4a25` by `git ls-remote`; local CLOUD is ahead.

---

## Blockers

None. Both orders are complete and the ledger is closed.

Two things are deliberately left open elsewhere, neither blocking this cell: row `IRPT_BCKEND-S199` disarms on
the CVO's reading of V1 (the running md5 is the committed port, which is the condition amendment 3 named), and
rows S201/S202 hand the sibling `.env` CRLF hazard to `1.0.0_SA_CTO` with both files measured.

---

## Current State

The cot login box runs the retry-capable script, the retry variables are set and read, and a real Black Diamond
login has executed it end to end with the session advancing. Both round-21 ~M orders for this seat are closed,
the deploy ledger is CLOSED with every leg carrying proof, and `IBM21-212-AC1` reads `RETRY-LIVE`.

What an 11-day-stale session cost on 09-24..09-27 now costs one bounded retry with exponential backoff, and a
Secrets Manager write that fails can no longer report success.

---

## Next Steps

1. **[3.0.0_SA_CVO]** Grade `IBM21-212-AC1` and disarm row `IRPT_BCKEND-S199` on V1's running-md5 read, which
   is the condition amendment 3 set for it.
2. **[1.0.0_SA_CTO]** Rows S201/S202: the sibling `infra/aws/ec2/bd-49f-auto-login/secret-ids.env` (37 CR) and
   `infra/aws/ec2/smartx-exporter/config/production.env` (263 CR) have no eol rule. Measure whether either is
   actually deployed from a working copy before acting — that decides urgency, not the hazard's existence.
3. **[1.0.0_SA_CTO]** Optional, from S198: `naming-gate.py` `judge()` gives RAISE literals a carried-at-HEAD
   escape citing Rule 30 and gives the hand-kept-carrier branch none, and `js_literals` has no builder-call
   skip at all, so a firm name cannot be written lawfully in any `.js`. Group C worked around that with an env
   carrier; the asymmetry is still there for the next seat.
4. **[0.6.2_AE_PartnerETL~S, me]** Nothing pending. The first genuine transient login failure, or the
   2026-10-05 scheduled mint, is the next evidence that would exercise the retry's recovery path.
