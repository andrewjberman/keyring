# MDPF_HEALGAP: FWD-1's one real run, exercised and closed -- the induced morning failure healed itself

**archetype:** VALIDATE
**secondary_archetypes:** DEPLOY, DIAGNOSE

**Seat:** `0.7.0_AE_CloudOps~F` (laptop). **Window:** 2026-10-08 10:38Z - 13:30Z. **Respawned** by
`0.0.0_AB_MSTR` to hold `MDPF_HEALGAP.TO-HG-d3` after the overnight `~F` session was killed for laptop
memory (CTO msg 106633 to `0.0.0_AB_MSTR`, 2026-10-07T23:40Z). Predecessor log:
`session_healgap_hg_d2_apply_and_d3_arm_1420-1755Z.md`.

## Current State

**`MDPF_HEALGAP.TO-HG-d3` is COMPLETE and FWD-1 is REALIZED for D = 2026-10-08.** On a day whose
morning Cottonwood Rebalancer pull was deliberately made to fail on a lapsed vendor login, the day's
figures were in place by 11:46:08Z **with nobody acting**. The 06:00Z fire raised the induced HTTP 401
three times under one RequestId and wrote nothing; the HG-d2 re-attempt target on `cot-bronze-complete`
fired at 11:32:06Z, completed a real vendor pull in 17832.30 ms (`BRONZE-COMPLETE`, 71 models / 992
accounts / 93 model_details, `pagination_integrity PASS`), wrote the complete-stamp at 11:32:25Z, and
the four model silver tables followed at 11:32:29Z-11:32:33Z.

All three criteria PASS, graded 13:00:42Z-13:00:46Z inside the order's own read gate. Never-widen
conditions 2, 3 and 4 are all MET. Proof instance `VALID (rc=0)`. Ledger entry CLOSED 5 of 5 legs with
its sentinel removed. Branch (B) was never triggered. **This session made ZERO AWS writes** -- its only
AWS calls were reads plus one read-only `terraform plan`.

Commit `1df5e818f2`, 6 files. Push state **LOCAL** (`git ls-remote` at 13:2xZ: `origin/CLOUD
bf1b297689`); a Tier-2 seat does not push a shared branch.

**What this session did NOT do, and the record says so plainly.** Neither `put-targets` of the order was
made by it. Act 1's arm was the prior `~F` session's at 2026-10-07T17:40:36Z. Act 2's restore landed at
06:08:46Z -- inside the required 06:05Z-06:20Z window -- from an actor none of the three named fallback
owners claims, while this session did not yet exist. The seat's contribution to that open question is a
measurement, not a guess (see below).

## Sequence

| # | act | result |
|---|---|---|
| 0 | `/watcher`: register lane `~F`, arm the inbox Monitor | lane was NOT REGISTERED; registered PID 28096; 0 script rows -> armed, pid 25732; re-armed on each 30-min expiry (5 arms) |
| 1 | startup A.1-E | serial file written, 104 of 104 comp-tools resolve bare + a forwarder RAN, owned-paths hook already wired, `comp-to` set, A.2 surfaced one OWNED finding (below) |
| 2 | B.0/B.1 | delivery ledger 3 of 3 READ; `to-check --all --assignee` = 1 active TO, this one |
| 3 | measure the world before touching it | daily target already `{"mode":"pull"}`; CloudTrail: exactly 2 `PutTargets`; runner log: 3 induced 401s at 06:00:42Z/06:01:49Z/06:03:46Z |
| 4 | `HG1-d3-AC3` | `RESTORED-OK` at 10:49Z |
| 5 | condition 3, targeted plan | `No changes. Your infrastructure matches the configuration.` 11:06:16Z-11:06:23Z |
| 6 | ledger legs L2, L3 | CLOSED; L2 later amended twice as the actor question resolved |
| 7 | status to `1.0.0_SA_CTO` for relay (msg 106895) | answered 11 minutes later by msg 106896, the CTO's honest wording for the actor |
| 8 | **touch nothing at ~11:32Z** | the heal fired on its own; stamp absent at 11:31Z (404), present 11:32:25Z |
| 9 | negative arm against 2026-10-07 | `FAILED-BAD` / `HEALED-BAD`, exactly as the order predicts |
| 10 | graded run inside the 13:00Z gate | `FAILED-OK` / `HEALED-OK` / `RESTORED-OK`, byte-identical to the pre-reads |
| 11 | condition 4 read 13:01:58Z | **MET** -- newest `on_success`-chain write for D is 11:46:08Z |
| 12 | row `MDPF_HEALGAP-S11`, proof instance, `<status>` flip, ledger close, commit | gate-clean; `msg-verify MATCH len=3551` |

## Verification (ACTUAL output)

```
HG1-d3-AC1  FAILED-OK induced lines=3 bronze keys before 11:00Z=0 date=2026-10-08
HG1-d3-AC2  HEALED-OK date=2026-10-08 stamp_at=2026-10-08T11:32:25+00:00 keys={"rebalancer_models": 1, "rebalancer_accounts": 5, "rebalancer_model_detail": 93}
HG1-d3-AC3  RESTORED-OK daily target input={"mode":"pull"}

negative arm, same script, same plane, normal day:
--failed 2026-10-07  FAILED-BAD no INDUCED auth-lapse line in the runner log 2026-10-07 06:00-06:30Z        (rc=1)
--healed 2026-10-07  HEALED-BAD stamp LastModified 2026-10-07T06:00:58+00:00 outside 2026-10-07 11:00Z-23:59Z (rc=1)
```

The induced failure, from `/aws/lambda/cot-rebalancer-runner`, one fire and three attempts under
RequestId `346eaa7d-c480-4c25-9716-6ae2408f2c53`:

```
06:00:42Z  [ERROR] RuntimeError: BD GET /auth/token -> HTTP 401: INDUCED auth-lapse (MDPF_HEALGAP FWD-1 exercise; no secret read, no vendor call)
             File "/var/task/lambda_function.py", line 485, in lambda_handler
06:01:49Z  (same)        06:03:46Z  (same)
```

The heal, RequestId `21eb2c0c-ea27-485c-9e4a-8f4639d51f08`, Duration 17832.30 ms:

```
11:32:09Z  WARN: count-reconcile mismatch on 1 of 54 strategy(ies) -- CARRIED, not fatal: [{"strategy": "Core | Satellite 60", "roster": 12, "observed": 11}]
11:32:24Z  {"verdict": "BRONZE-COMPLETE", "as_of": "2026-10-08", "models": 71, "accounts": 992, "model_details": 93,
            "gates": {"pagination_integrity": "PASS", "count_reconcile": "DISCLOSED-MISMATCH", "strategies_checked": 54, ...}}
```

## Three places a reading was not allowed to stand for more than it proves

1. **"Which box made the 06:08:46Z restore is not distinguishable" was my own claim, and it was too
   weak.** I wrote it into ledger leg L2 on the grounds that every seat on both boxes calls as the one
   IAM user from one NAT IP. The USER AGENT separates them: row `MDPF_HEALGAP-D1-S3` had recorded the
   call as `aws-cli/1.44.44 Python 3.12.10 Windows 10.0.26100` against dell1's `aws-cli 2.37.9`, and
   this laptop's own shim reads byte-identical on all three fields. L2 carries AMENDMENT 2 with the
   correction; the leg now claims the act, its time, its window and its TOOL, and claims no actor. The
   26100-vs-26200 build oddity is explained on this box (`platform.release()` vs `platform.version()`).
2. **`surprise-row-gate.py` printed OK on my new row and that was NOT evidence the row passes.** It
   reported "0 new row(s) of 15 total checked" while the worktree file carried 16 rows, because the gate
   reads the STAGED INDEX and never the worktree. Treating that OK as a pass would have been an absence
   read as a verdict. The row was instead validated directly against
   `org/surprise_channel/schemas/investigation_item.schema.json` (`jsonschema: VALID`), and the gate
   graded it for real at commit: "1 new row(s) of 16 total checked ... OK".
3. **`comp-estate --resource dim_model_portfolio` returned `SUBJECT_ABSENT_FROM_CORPUS` and that is a
   fact about its corpus, not about the estate.** Reading it as "no producer is registered" would have
   left condition 4 ungrounded. `comp-find` then named the producer and the EC2 dispatch line that runs
   it, which is what decided the verdict.

## Condition 4, and the row it produced

The condition's instrument is *the newest silver/gold write time for D under the existing `on_success`
chain* against 13:30Z. For D that is **11:46:08Z** (the four model silver tables at 11:32:29Z-11:32:33Z),
so **MET** by 1h43m. Gold `dim_model_portfolio` is **not on that chain** -- it is written by
`data/assets/scripts/gold/build_dim_model_portfolio.py` from the EC2 `mdpf-daily-runner`
(`mdpf-daily-dispatch.sh:554`), while the runner's `on_success` destination is
`opal-assets-silver-blackdiamond` -- and had zero objects for D at the 13:01:58Z read. Its last ten
partitions landed at 13:30:39Z-13:30:42Z on nine of ten days (the tenth later still), and no EventBridge
rule carries a 13:30 cron across 129 scheduled rules. So widening "served" to gold makes the same read
return MISSED on nine of the last ten days with no failure present. Filed as row `MDPF_HEALGAP-S11`,
owner `2.0.0_SA_COO~G1` for the successor wording; not fixed here, because the half's text and the gold
producer's cadence are both outside this order's write grant.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | startup A.3 exercise | PASS | 104 of 104 resolve bare; a forwarder RAN |
| `comp-to` | `comp-to MDPF_HEALGAP.TO-HG-d3.fwd1-exercise-induced-morning-failure` | PASS | race-free per seat+session |
| `to-check.py` | `--all --assignee 0.7.0_AE_CloudOps~F` | PASS | 1 active TO, 4714 faces scanned. The 3 orders `get_agent_status` lists are BASE-folder-scoped and not this lane's (rule 22a ROSTER trap) |
| `comp-find` | `'dim_model_portfolio' --limit 12 -- data infra` | PASS | 78 hits / 14447 files; named the gold producer and its EC2 dispatch line -- the read that decided condition 4. Also used on the audit-log finding (211 hits) to confirm it is an OWNED class |
| `comp-read` | `--for` on `deploy_ledger.py`, `proof-of-spec-check.py`, `surprise-row-gate.py` | PASS | read three contracts BEFORE relying on them: close-leg overwrites; a `surprises` entry is a STRING opening with its row id; the row gate reads the staged index |
| `comp-estate` | `--resource dim_model_portfolio` | SUBJECT_ABSENT (correct) | a clean negative about its corpus, not about the estate |
| `deploy_ledger.py` | `close-leg` x6 (L2 three times), `close` | PASS | CLOSED 5 of 5, sentinel removed; the amendment trail is in the entry's own log |
| `proof-of-spec-check.py` | `<instance> HG1-d3-AC1,HG1-d3-AC2,HG1-d3-AC3 --governing-order <order>` | PASS | `VALID (rc=0)`, violations 0, coverage 3/3, invocation-alignment 3/3, surprises 2 of 2 resolving. **Positive control first** on the known-good HG-d2 instance |
| `surprise-row-gate.py` | on the channel file, then again via the hook | PASS | see finding 2 above: the pre-commit run was read for what it actually proves |
| `terraform` (v1.15.8, PATH) | targeted `plan`, `CHECKPOINT_DISABLE=1` | PASS | `No changes.` `.tools/terraform.exe` does not exist on this laptop; `MSYS_NO_PATHCONV` unset throughout |
| `safe-commit.sh` | one commit, exact 6-path pathspec, `-F` from a non-shell writer | PASS | `msg-verify MATCH len=3551`; to-pipeline-gate, missions-tree-check, one-writer all clean |
| `audit-archive-invoker.py` | startup A.2 | rc=1, 1 finding, NOT re-filed | `[INTEGRITY/NON-APPEND-EDIT] org/mcp/agent-spawn-audit.log`, divergence line 12991, live-head SMALLER than baseline. An OWNED class (the CTO's own shrink record, MSTR~Z's BENIGN device-axis adjudication, and the standing deferral until `rv0057-f001`), so it was surfaced here and not re-filed as a row |

**What worked:** measuring the world before writing anything. The session opened on a seat whose
predecessor had died mid-exercise, and the first four reads -- the live target, CloudTrail, the runner
log, the stamp -- established the whole overnight state in under four minutes, including the one fact
nobody had reported (that the restore had already happened, in window, by nobody). Running the
acceptance checks as declared informational pre-reads once each underlying fact had settled meant a BAD
reading would have surfaced with hours left before the 18:00Z branch-(B) deadline rather than minutes;
the graded run then came byte-identical and the pair doubles as the determinism control.

**What failed:** a `python - <<'PYEOF'` heredoc carrying ~200 lines of prose with many apostrophes died
`unexpected EOF while looking for matching '`. The fix is the one the law already prefers for commit
messages and applies equally to any long literal: write the script with a NON-SHELL writer and run the
file. Two earlier, shorter heredocs had worked, which is exactly how this class hides.

**Gap found:** the single-file `grep` rail routes to `comp-read`, and `comp-read`'s own census output is
then refused if it is piped to `head`, so a two-step "narrow then page" habit costs an extra round trip
each time. Non-blocking; `--width` and the band flags cover it once you know.

## Blockers

**None.** Nothing is owed by this seat. The order is `complete`, the ledger is CLOSED, and the four
remaining items all belong to `2.0.0_SA_COO~G1` (next section).

## Next Steps

1. **[`0.0.0_AB_MSTR`]** Carry `1df5e818f2` to origin (`CLOUD`). It is LOCAL; `origin/CLOUD` read
   `bf1b297689` at 13:2xZ.
2. **[`2.0.0_SA_COO~G1`]** The reader's page read of the Cottonwood models for D -- `HG1-d3-AC3`'s own
   text assigns it to the issuer at close, and this seat did not substitute an S3 read for it.
3. **[`2.0.0_SA_COO~G1`]** HG-d2's AC3, a normal day's ~11:32Z fire reading `SKIP-IDEMPOTENT` with no new
   bronze key. It cannot be read on 2026-10-08, because that fire was the HEAL. Earliest: 2026-10-09.
4. **[`2.0.0_SA_COO~G1`]** Row `MDPF_HEALGAP-S11` -- decide whether condition 4's successor reads silver
   and keeps 13:30Z, or reads gold and moves the line past the `mdpf-daily-runner`'s arrival. FWD-1's own
   wording, "by the end of the same day", satisfies both.
5. **[`2.0.0_SA_COO~G1`]** Mint the two rows still owed from HG-d2
   (`SURPRISE_ROWS_OWED_FROM_TO_HG_D2_20261007.md`), and disarm or re-own the two ARMED rows whose
   `disarm_owner` is this lane: `MDPF_HEALGAP-W1-S1` (the device's ruff 0.16.10 vs the gate's pinned
   0.15.11 blocks every `.py` commit) and the already-disarmed `MDPF_HEALGAP-D1-S1`.
6. **[Andrew]** Row `MDPF_HEALGAP-D1-S3`'s open question -- who made the 06:08:46Z `put-targets`. The
   tool is now identified as this laptop's aws v1 shim; the actor is not, and no seat claims it.

-- `0.7.0_AE_CloudOps~F`, 2026-10-08T13:30Z
