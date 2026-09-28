# 0.6.2_AE_PartnerETL~S -- 2026-09-27 1910Z to 2026-09-28 1410Z -- TO-IB-s158 closed, Andrew-direct answered and verified

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

Delta since the prior log (`logs/2026-09-27/session_0.6.2_AE_PartnerETL~S_1745-1910Z_...md` @`eae7625ed3`).

## What happened in this window

**1. AC1 amended by the issuer; the order flipped complete.** I had refused `IBS158-AC1` as originally
written -- it demanded the quoted failing line per day from the box's own log, and no carrier holds those
bytes. `2.0.0_SA_COO~P` amended AC1 @`9fa6a3c5d8` to grade the cause at the grain the carriers allow, then
asked (102038) for a re-run and a flip. Re-ran all three criteria: AC1 `CAUSE-NAMED`, AC2 and AC3 re-read
on the live plane. Order flipped `complete` @`fe23038617`. **No evidence was changed to satisfy the new
bar** -- the same `failed_days` rows, the same ABSENT causes and the same three-carrier absence proof now
pass because the ISSUER moved the bar, which is their call and not the executor's.

**2. The flip was REFUSED first, and the refusal was a real finding.** `to-pipeline-gate.py`'s
complete-flip limb could not find my proof-of-spec instance. The TO's `<proof_of_spec>` block declares a
FLAT seat path; for a TREE order (`*/task-orders/`) the gate globs
`<project>/deliverables/<serial>/<FULL-TO-FILENAME-STEM>.proof_of_spec.json`. A VALID instance was sitting
at the declared path and the gate could never see it. Moved it to the gate's grammar, matching this
project's 12 pre-existing instances; `git mv`, recorded as a 79% rename, no divergent duplicate. Row
`IRPT_BCKEND-S167`.

**3. Validating STANDALONE passed two stale pins that the gate's own binding rejected.** Running
`proof-of-spec-check` bare returned VALID; running it the way `check_complete_flip` does
(`--governing-order`) returned INVALID on two `PENDING-THIS-COMMIT` rows that were already tracked at HEAD
(the CCX class). Re-pinned both to `eae7625ed3`. **A bare validation is not the validation the flip is
graded by.**

**4. Andrew-direct 102057, relayed by `4.0.0_SA_CRO`: three status questions.** Answered and recorded
@`294bba53ed` (record: `deliverables/ANDREW_DIRECT_20260927_1957Z_IRPT_BCKEND_S158_THREE_STATUS_QUESTIONS.md`,
quoting verbatim with channel and time). Answering Q1 required reading the trigger Lambda's source, which
**falsified a claim I had already committed**: I had written that the 09-28 07:30 ET run would be the
cold-boot test exercising the new log-on-failure branch. It would not. `Lever A` skips the mint entirely
while the capture probes positive-live and is younger than `MAX_SESSION_AGE_DAYS` (env unset -> default 7).
Corrected in place in both the deliverable and the proof-of-spec; row `IRPT_BCKEND-S168` filed against my
own prior assertion.

**5. The prediction was then MEASURED, not left as a projection.** After the 07:30 ET run I read the
Lambda's own CloudWatch log: `Lever A: cot cookie POSITIVE-live (probe positive
(captured_at=2026-09-27T18:42:27.162Z, age 0.7d <= 7d)) -> SKIP OIDC-login mint, direct bronze-run`. Both
limbs held. Verification appended and committed @`7350eb3859`; relayed to the CRO for Andrew.

**6. Purge and reboot traffic handled.** Acked 102321 (S19 purge, froze my git writes), 102337 (freeze
narrowed to pushes only -- which never bound this lane, since seats do not push CLOUD), 102352 (the reboot
checkpoint sequence). Flagged to `2.0.0_SA_COO~M` a consequence nobody had named: the rewrite changes commit
hashes, and proof-of-spec instances pin artifacts BY HASH, so post-rewrite they can read UNRESOLVED-HERE or
resolve against a commit that no longer carries what the row claims. IRPT_BCKEND alone has 13+ committed
instances.

## Deployment Sequence + Verification (AE role-specific)

No new deploy in this window. The window's only live-plane acts were READS plus one sanctioned document
fire, all covered by the ledger closed in the prior window
(`irpt-bcknd-s158-cot-session-autologin`, CLOSED 5/5 legs).

Verification output, pasted as read:

```
=== IBS158-AC1 (amended invocation, verbatim from the TO at HEAD) ===
CAUSE-NAMED

=== IBS158-AC2 (re-run, live plane) ===
  7 './run-bd-auto-login.sh > $LOG_FILE 2>&1 || EXIT_CODE=$?'
  8 'tail -25 $LOG_FILE || true'
 10 'exit $EXIT_CODE'
captures exit code without set -e aborting: True
uploads the log                          : True
exits with the captured code             : True

=== IBS158-AC3 (re-run, live plane) ===
1790534547.771        (= 2026-09-27T18:42:27.771Z)

=== 09-28 07:30 ET run, from the Lambda's own log ===
Lever A: cot cookie POSITIVE-live (probe positive (captured_at=2026-09-27T18:42:27.162Z, age 0.7d <= 7d))
         -> SKIP OIDC-login mint, direct bronze-run
SSM RunCommand sent: dd4f49e2-b12e-43c3-b6d6-554ce6c1b341 document=opal-cot-bronze-run attempt=1
bronze dd4f49e2 Success 11:30:32Z | silver 8961c6d4 Success 11:31:49Z | gold e619c14a Success 11:33:30Z
AWSCURRENT UNCHANGED 9da4e781-7f11-4cf0-b2dd-2980e56db1db (created 2026-09-27T18:42:27.771Z)
```

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `proof-of-spec-check.py` | `<instance> IBS158-AC1,AC2,AC3 --governing-order <TO>` | PASS eventually, after catching two REAL defects. Bare run said VALID; the `--governing-order` run (how the gate calls it) said INVALID on two stale `PENDING-THIS-COMMIT` pins. Also caught `decomp_ref.owned_cells` is not a schema property and that my AC3 `invocation` had a second command appended -- the recorded invocation must be the criterion's VERBATIM, extra legs belong in `output_evidence`. |
| `to-pipeline-gate.py` (fired on me) | via `safe-commit` on the flip | REFUSED the flip: "NO proof-of-spec instance was found beside it". Correct, and the most useful gate hit of the window -- see `IRPT_BCKEND-S167`. |
| `comp-blast` | `comp-blast opal-cot-bd-session-fetch` (prior window, cited) | PARTIAL by its own admission: `PRESENT_WITH_ZERO_RESULTS`, "no EXTRACTED edge -- NOT provably zero". Did NOT clear the blast radius; the live `describe-rule` did. |
| `safe-commit.sh` | 3 commits this window | PASS, with two instructive refusals: an `index.lock` collision with another seat, and a MERGE-IN-PROGRESS refusal ("NOTHING WAS STAGED BY THIS RUN") while another seat drained. Waited both out rather than forcing; the second cleared on its own. |
| raw `aws` reads | `ssm list-commands`, `logs get-log-events`, `secretsmanager list-secret-version-ids` | PASS, with one near-miss logged below. |

**What worked:** running the validator under the GATE'S binding rather than bare. The two pins it caught
would have shipped as a silently-wrong record.

**What failed:** `aws ssm list-commands --instance-id ... --max-items 14` did NOT return today's bronze
invocation, which briefly read as "no bronze ran" and appeared to contradict my own prediction. The command
existed the whole time -- `--max-items` interacts with pagination and dropped the row. A targeted
`list-command-invocations --command-id` returned it as Success. This is CLAUDE.md rule 22a's paginated
`list-*` trap in its exact shape: **the instrument was wrong, not the world.**

**Gap found:** the tree-order `<proof_of_spec>` grammar and `to-pipeline-gate.py` disagree on where an
instance lives (`S167`). Any tree order written with the flat path cannot be flipped. Raised to the issuer;
not adjudicated here.

**Role minimums, declared honestly:** `comp-pipescript deployed` / `postdeps` were NOT run this window and
were not applicable -- this lane triggered no gold run. The 09-27 gold run fired from the session-fetch
Success via the `cot-session-complete` rule, and the 09-28 gold run fired from the scheduler's own chain;
neither was an ad-hoc dispatch by this seat. `comp-iam gaps` not applicable -- no `iam.tf` change.

## Blockers

None BLOCKED. One HELD, evidence-cited: the FAILURE branch of the new log-on-failure step is UNEXERCISED
because nothing has failed since it landed, and per the Lever-A age bound the next expected
`opal-cot-bd-session-fetch` is about **2026-10-04 07:30 ET** (or sooner on a negative probe). ABSENT is not
EXERCISED-AGAINST; this is a wait on a real event, not a blocker on a seat.

## Current State (for a reader with zero prior context)

- **`IRPT_BCKEND.TO-IB-s158` is `complete`** @`fe23038617`, verified with `git show HEAD:<to>` plus a
  negative control. 3/3 criteria PASS against AC1 as amended @`9fa6a3c5d8`.
- **Instance (canonical, gate-findable):**
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.6.2_AE_PartnerETL~S/IRPT_BCKEND.TO-IB-s158.cot-bd-session-autologin.proof_of_spec.json`
  -- VALID rc=0 under `--governing-order`.
- **Deliverable:** `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_S158_CAUSE_20260927.json`.
- **Andrew-direct record:** `.../deliverables/ANDREW_DIRECT_20260927_1957Z_IRPT_BCKEND_S158_THREE_STATUS_QUESTIONS.md`
  (carries the VERIFIED section added @`7350eb3859`).
- **Live infra:** SSM document `opal-cot-bd-session-fetch` is at **version 5** (applied
  2026-09-27T18:37:47.998Z) and uploads its wrapper log to
  `s3://opal-data-cot/logs/cot-exporter/session-fetch/` on the FAILURE branch as well as on success.
  Name unchanged, still exits non-zero on failure, so `cot-session-complete` still fires on Success only.
- **Live session:** `blackdiamond/cot/session` AWSCURRENT `9da4e781-7f11-4cf0-b2dd-2980e56db1db`, created
  2026-09-27T18:42:27.771Z. The 09-28 chain ran green unattended on the Lever-A skip.
- **Box:** `i-0643a5bee8a8feabf` (cot-exporter), `running` at last read; `ec2-auto-shutdown-enforcer` stops
  it at `IDLE_CEILING_HOURS=3.0`. `/tmp` is **tmpfs** -- nothing written there survives a stop.
- **Deploy ledger:** `irpt-bcknd-s158-cot-session-autologin` CLOSED, all 5 legs proven (L4 closed as
  VACATED: no cause was named, so nothing was deployed to the box).
- **Open rows, none mine to close:** `IRPT_BCKEND-S165` (the box carries NO in-run login retry -- the
  standing risk to unattended reliability) and `S166` (the running login script has no build input in the
  cot tree), both ARMED with `disarm_owner 1.0.0_SA_CTO`. `S164`, `S167`, `S168` GRADUATED/INERT.
- **Purge state at time of writing:** local HEAD `95ec2ca2dc` != origin/CLOUD `9c432e014a` (645 ahead / 419
  behind); all five of my commits still resolve, so the S19 rewrite has NOT landed. **Every hash in this
  log will be rewritten by it.**
- **Also held, not started:** `org/tier2_senior/0.6.2_AE_PartnerETL/task_orders/AUTH_SELFHEAL.TO-A1.cookie-riding-consumer-inventory.md`,
  `pending` since 2026-08-31, different project and issuer, outside this session's dispatch.

## Next Steps

1. **[0.6.2_AE_PartnerETL~S, me]** After `0.0.0_AB_MSTR` posts the S19 purge CLOSE: re-measure this log's
   and the handoff's hashes (the rewrite invalidates them), then send the one-line READY-FOR-REBOOT to
   `0.0.0_AB_MSTR` per Phase C of
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_140xZ_FABRIC_REBOOT_CHECKPOINT_SEQUENCE.md`.
   Holding the READY line until then deliberately -- citing pre-rewrite hashes would be citing hashes that
   no longer exist.
2. **[1.0.0_SA_CTO]** `IRPT_BCKEND-S165`: the cot box has no in-run login retry. This is the highest-value
   remaining fix for unattended reliability and needs a newer `bd_49f_auto_login.js` box-deploy, which was
   outside TO-IB-s158's grant.
3. **[2.0.0_SA_COO~P]** `IRPT_BCKEND-S167`: fix the `<proof_of_spec>` path grammar in the tree-order
   template, or every tree order written with the flat path will be refused at its flip.
4. **[0.0.0_AB_MSTR]** post-rewrite, the round's proof-of-spec artifact pins need a re-resolve sweep --
   flagged to `2.0.0_SA_COO~M`, not owned here.
