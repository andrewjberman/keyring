# MDPF_HEALGAP: HG-d2 applied and complete, HG-d3's FWD-1 exercise armed for 2026-10-08

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

**Seat:** `0.7.0_AE_CloudOps~F` (laptop). **Window:** 2026-10-07 14:20Z - 17:55Z. **Re-seated** on a
dell1 seat ask (bus 7d37b4bc) for `MDPF_HEALGAP.TO-HG-d2`; the prior `~F` session of this day held
`TO-HG-d1` (log `session_healgap_hg_d1_deploy_0945-1125Z.md`).

## Current State

**`MDPF_HEALGAP.TO-HG-d2` is COMPLETE.** `cot-bronze-complete` now carries a second target,
`cot-rebalancer-runner-reattempt`, invoking `cot-rebalancer-runner` with `{"mode":"pull"}` beside its
unchanged `CotSilverOnBronzeComplete` target, and the runner's resource policy carries statement
`AllowEventBridgeInvokeReattempt` for `events.amazonaws.com` from `rule/cot-bronze-complete`. So a day
whose 06:00Z Cottonwood Rebalancer pull fails on a lapsed login is pulled again at ~11:32Z the same
day, with nobody acting. Live reads: `HG1-d2-AC1 WIRED-OK`, `HG1-d2-AC2 UNCHANGED-OK`, targeted
re-plan `No changes.`, and `terraform state list` carrying
`aws_cloudwatch_event_target.cot_rebalancer_reattempt` and
`aws_lambda_permission.cot_rebalancer_reattempt`. Proof instance `VALID (rc=0)`, violations 0,
coverage 2/2. The order's `<status>` is flipped to `complete`.

**`MDPF_HEALGAP.TO-HG-d3` is IN FLIGHT, acts 0 and 1 done.** `cot-rebalancer-runner-daily`'s single
target has carried Input `{"mode":"pull","induce":"auth-lapse"}` since 2026-10-07T17:40:36Z (same Id
`cot-rebalancer-runner-daily`, same Arn, `length(Targets)=1`), so the 2026-10-08 06:00Z fire will
raise an induced HTTP 401 before any secret read or vendor call. The `cot-bronze-complete` re-attempt
input was verified UNTOUCHED at `{"mode":"pull"}` in the same read, so D's ~11:32Z fire is a real pull
and the heal is a real heal.

**Where the work ran.** The shared laptop tree was 419 commits behind `origin/CLOUD` and
`0.0.0_AB_MSTR` is not merging it while seats work in it, so the terraform acts ran in linked worktree
`/c/tmp/wk-healgap-d2` (branch `wk-healgap-d2`, created at `origin/CLOUD 8798e5f484`), authorized by
`0.0.0_AB_MSTR` via CTO relay msg 106398 under CLAUDE.md 14b. The applied `.tf` bytes are sha256
`0105df425f85c088d9b32d7ef8260f27d74ef71d2788821c338e85d2d032922a`, identical to the ratified blob at
the GO commit `dff3c744f1`. All ledger work ran in the shared tree, where the live entries are.

**Device fact worth carrying:** `.tools/terraform.exe` does NOT exist on this laptop. `terraform`
resolves on PATH at v1.15.8, and `safe-apply.sh`'s own fallback chain (override -> sibling -> PATH ->
fail loud) resolved the same binary. This is the exact case `/cloud-ops` warns about.

## Deployment Sequence

| # | act | result |
|---|---|---|
| 0 | act-0 SKIP probe: one `RequestResponse` invoke of `cot-rebalancer-runner`, `{"mode":"pull"}` | `{"verdict": "SKIP-IDEMPOTENT", "as_of": "2026-10-07"}` |
| 1 | `deploy_ledger.py open` + leg L1 | entry `20261007T1621Z_mdpf-healgap-hg-t2-reattempt-apply-20261007`, 5 legs, 8h window |
| 2 | targeted `terraform plan`, `CHECKPOINT_DISABLE=1` | `Plan: 2 to add, 0 to change, 0 to destroy.` |
| 3 | `.tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply` + same two `-target`s | 16:47:12Z-16:47:53Z; landing proven by re-plan + state list |
| 4 | `record-terraform-deploy.sh opal-assets --plan hgd2.tfplan` | rc=2 REFUSED by design, nothing written |
| 5 | `deploy_ledger.py close` + exact-pathspec commit | all 5 legs proven, sentinel removed |
| 6 | AC1 / AC2, run again after the close commit | `WIRED-OK` / `UNCHANGED-OK` |

## Verification (ACTUAL output)

Act-0 probe, 2026-10-07T16:15:36Z, RequestId `6fe29f10-fadc-4f05-9070-95b68cc7f072`, StatusCode 200,
no `FunctionError`:

```
{"verdict": "SKIP-IDEMPOTENT", "as_of": "2026-10-07"}
START RequestId: 6fe29f10-fadc-4f05-9070-95b68cc7f072 Version: $LATEST
cot-rebalancer-runner invoked 2026-10-07T16:15:36Z firm=cottonwood bucket=opal-data-assets date=2026-10-07
{"verdict": "SKIP-IDEMPOTENT", "as_of": "2026-10-07"}
REPORT ... Duration: 94.43 ms  Billed Duration: 648 ms  Memory Size: 512 MB  Max Memory Used: 98 MB  Init Duration: 553.41 ms
```

Bronze `blackdiamond/cottonwood/bronze/rebalancer_{models,accounts,model_detail}/2026-10-07/`:
BEFORE `1/5/91 = 97`, AFTER `1/5/91 = 97`. Newest `model_detail` key `LastModified
2026-10-07T06:00:56Z`. Stamp `meta/2026-10-07-complete.json` unchanged, 11679 B @ `06:00:58Z`.

Acceptance, both run twice (immediately after the apply, and again after the ledger-close commit as
the order's act 4 directs), byte-identical:

```
WIRED-OK target=cot-rebalancer-runner-reattempt input=pull other_targets=CotSilverOnBronzeComplete policy_sid=AllowEventBridgeInvokeReattempt
UNCHANGED-OK code=HG-t-1 build retry=2 age=21600 on_success=opal-assets-silver-blackdiamond daily=cron(0 6 * * ? *) input=pull
```

Base arm, measured on the laptop at ~16:09Z BEFORE the apply, matching the order's dell1 base:
`WIRED-BAD runner targets on cot-bronze-complete=0 (want 1); all=['CotSilverOnBronzeComplete']` with
AC2 already `UNCHANGED-OK`, so the base separated the two criteria exactly as the order predicted.

HG-d3 act 1, pre-read 17:38:11Z / put 17:40:36Z / read-back 17:41:52Z:

```
PRE:  {"Id":"cot-rebalancer-runner-daily","Arn":"...:function:cot-rebalancer-runner","Input":"{\"mode\":\"pull\"}"}  length(Targets)=1  State=ENABLED  cron(0 6 * * ? *)
PUT:  {"FailedEntryCount": 0, "FailedEntries": []}
POST: {"Id":"cot-rebalancer-runner-daily","Arn":"...:function:cot-rebalancer-runner","Input":"{\"mode\":\"pull\",\"induce\":\"auth-lapse\"}"}  length(Targets)=1
SEP:  cot-bronze-complete -> CotSilverOnBronzeComplete {"mode":"silver-run"} ; cot-rebalancer-runner-reattempt {"mode":"pull"}   (untouched)
```

## Three places a tool's output was NOT allowed to stand in for evidence

1. **The apply's resource-count line was never read.** The captured stdout tail ended inside the root
   outputs block and cut it off. It is quoted nowhere in the ledger, the report or the proof instance;
   the landing is measured by a 0-diff re-plan and `terraform state list` instead. An unread line is
   not evidence.
2. **No HALTGT pass is cited.** `safe-apply`'s checkpoint ran and did not block, but per ADHC_HALTGT /
   LD-0267 it reads only unread files directly under `inbox/<serial>/`, so this seat's live inbox
   Monitor moves every message first and a `~lane` seat is unhaltable. The gate cannot witness this
   seat; its silence is recorded as uninformative.
3. **`record-terraform-deploy.sh` was run, not skipped, and it refused.** rc=2, `stamped 0 of 15 rows
   under opal-assets: (none)`, nothing written. The resolver was read before being trusted:
   `record-deploy-scope.py applied_addresses()` admits an address only when `change.actions`
   intersects `{create, update}`, and this plan carries
   `module.cot_rebalancer_runner.aws_lambda_function.this` with `actions=no-op`. Forcing the
   `--function` form would have overwritten a correct source-map row with this apply's timestamp.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | `comp-which "how do I grep the repo"` (startup A.3 exercise) | PASS | 104 of 104 comp-tools resolve bare; a forwarder RAN |
| `comp-to` | `comp-to MDPF_HEALGAP.TO-HG-d2.apply-reattempt-target` | PASS | session TO_ID set race-free per seat+session |
| `to-check.py` | `--all --assignee 0.7.0_AE_CloudOps~F` | PASS | `0 active TOs`, 4539 faces scanned -- correct, the order lived only on the dell1 branch at that moment |
| `deploy_ledger.py` | `open` / `close-leg` x5 / `close`, slug `mdpf-healgap-hg-t2-reattempt-apply-20261007`; then `open` + `close-leg L1` for `...hg-d3-fwd1-exercise-20261008` | PASS | row S6 confirmed: at `close` another seat's entry + sentinel were also modified in the shared tree; kept out of both commits by exact pathspec |
| `record-terraform-deploy.sh` / `record-deploy-scope.py` | `opal-assets --plan hgd2.tfplan` | FAIL-CLOSED (correct) | rc=2 empty deployment set; see rows 1-2 of the owed file |
| `safe-apply.sh` | `-chdir=infra/aws/terraform/opal-assets apply -auto-approve` + two `-target`s | PASS | `MSYS_NO_PATHCONV` kept unset, per row 3 of the HG-d1 owed rows |
| `safe-commit.sh` | 4 commits, exact pathspec each, `-F` message files written by a non-shell writer | PASS | `msg-verify MATCH` on every one |
| `proof-of-spec-check.py` | `<instance> HG1-d2-AC1,HG1-d2-AC2 --governing-order <order>` | PASS | `VALID (rc=0)`, violations 0, alignment ENFORCE clean, `invocation-alignment` 2/2 |
| `terraform` (v1.15.8, PATH) | `init` / `plan` / `show -json` / `state list`, `CHECKPOINT_DISABLE=1` | PASS | `init` reused the shared provider cache -- nothing downloaded, which also keeps the act inside Andrew's download-tier rule |

**What worked:** grading the preconditions from git blobs on the dell1 branch BEFORE the trunk merge
meant that when r12 landed, only one ancestry read stood between the GO and the plan. Running the
recorder's own `--dry-run` resolver rather than assuming its behaviour turned a guess into a measured
refusal.

**What failed:** the first act-0 invoke exited rc=255 at CLI argument parsing -- `aws-cli/1.44.44` has
no `--cli-binary-format`, a v2-only flag. No API call was made, so the order's one-invoke budget was
intact, but the fix was to read `aws lambda invoke help` on THIS box rather than carry a v2 habit onto
a v1 shim. Separately, `--plan` passed as a repo-root-relative path doubles the prefix and
`terraform show` reports `Failed to read the given file as a state or plan file`, which the recorder
surfaces with the same wording it uses for a legitimate refusal.

**Gap found:** `record-terraform-deploy.sh`'s verdict line cannot distinguish "a path mistake" from
"a correct empty-set refusal" -- the same diagnostic-ambiguity shape as row 3 of the HG-d1 rows, where
a path fault was reported as a naming BLOCK. Both are in the owed-rows file for the issuer to mint.

## MCP traffic

8 messages handled. Significant: msg 106398 (CTO relay of `0.0.0_AB_MSTR`'s YES to the linked-worktree
route -- the decision that unblocked the apply); msg 106420 (the issuer asking whether the apply was
in progress or refused, answered with the measured result); msg 106443 (the issuer's instruction to
write/validate/flip/publish d2's proof, plus the `TO-HG-d3` GO); msg 106485 (the CTO's RULING naming a
four-deep fallback chain for tomorrow's restore and asking `0.0.0_AB_MSTR` to keep this session up
overnight). Sent: two asks to `0.0.0_AB_MSTR` about the trunk, and three reports via `1.0.0_SA_CTO`
for relay to the issuer, which cannot reach this inbox from dell1.

## Files Modified

See commit messages: `1ad97815f3`, `a536d4b391`, `04f05c1e31`, `f2cce52172`. Beyond those, the only
edit was `<status>pending</status>` -> `<status>complete</status>` in
`org/missions/D8/MDPF/MDPF_HEALGAP/task-orders/MDPF_HEALGAP.TO-HG-d2.apply-reattempt-target.md`.

| commit | tree | push state (`git ls-remote` at 17:5xZ, `origin/CLOUD ead69f1ddd`) |
|---|---|---|
| `1ad97815f3` | shared `CLOUD` | on origin |
| `a536d4b391` | shared `CLOUD` | on origin |
| `f2cce52172` | shared `CLOUD` | LOCAL |
| `04f05c1e31` | `wk-healgap-d2` | LOCAL -- drain asked of `0.0.0_AB_MSTR` |

## Blockers

**None.** Nothing is owed by this seat that it can act on now. The two remaining d3 obligations are
TIME-GATED, not blocked: the restore window opens at 06:05Z on 2026-10-08, and AC1/AC2 cannot be read
before 13:00Z. This is the qualified-wait case -- the exercise exists to observe a scheduled 06:00Z
fire, so firing anything ad hoc would destroy the discriminator the wait produces.

## Next Steps

1. **[`0.7.0_AE_CloudOps~F`] Restore `cot-rebalancer-runner-daily`'s target Input to `{"mode":"pull"}`
   between 06:05Z and 06:20Z on 2026-10-08**, then `HG1-d3-AC3` (`RESTORED-OK`) and a targeted
   `terraform plan` on `aws_cloudwatch_event_target.cot_rebalancer_runner_daily` reading no change
   (CTO half `@b05cdf04c1` condition 3). A 06:03Z wake (`bz7atx9un`) and an idempotent fail-safe
   (`bv5miebw8`, which performs only the order's second `put-targets` and only if a read shows the
   induce still live) are armed in-session; neither survives this session ending, which is why the
   CTO ruled the fallback chain in msg 106485. Pre-staged payload:
   `<scratchpad>/hg_d3/targets_restore.json`.
2. **[`0.7.0_AE_CloudOps~F`] Touch NOTHING at ~11:32Z on 2026-10-08** -- the heal must happen with
   nobody acting. Then after 13:00Z run `HG1-d3-AC1` (`FAILED-OK`) and `HG1-d3-AC2` (`HEALED-OK`), and
   record whether the served Cottonwood figures for D were in place by 13:30Z (condition 4, MET or
   MISSED). A `HEALED-BAD` after 18:00Z triggers branch (B): ONE `{"mode":"pull"}` invoke for D,
   recorded, and FWD-1 grades NOT REALIZED for D.
3. **[`0.0.0_AB_MSTR`] Drain branch `wk-healgap-d2`** (commit `04f05c1e31`: d2's proof instance,
   report, owed rows and the `complete` flip), and carry `f2cce52172` to origin.
4. **[`2.0.0_SA_COO~G1`] Mint the two rows** in
   `deliverables/0.7.0_AE_CloudOps~F/SURPRISE_ROWS_OWED_FROM_TO_HG_D2_20261007.md` -- act 4's recorder
   is inapplicable to a wiring-only apply, and a 0-diff plan still lists the function address.
5. **[`2.0.0_SA_COO~G1`] AC3 of both d2 halves** -- the next normal day's ~11:32Z fire read as
   `SKIP-IDEMPOTENT` with no new bronze key. It is the issuer's read by both halves' own text and is
   NOT among this order's criteria. Note it collides with the d3 exercise: on 2026-10-08 the ~11:32Z
   fire is the HEAL, not a skip, so AC3's normal-day read is 2026-10-09 or later.
6. **[`1.0.0_SA_CTO~DELL1`] FWD-3** -- rule whether a historical source exists for the 11 missing
   model-detail days (2026-08-31 to 09-10) or restate the outcome; row `MDPF_HEALGAP-S2`. Andrew's
   ACT 2 answer was no refill (`@e5fb41862f`).

-- `0.7.0_AE_CloudOps~F`, 2026-10-07T17:55Z
