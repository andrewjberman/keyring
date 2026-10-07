# 0.7.0_AE_CloudOps~S -- MDPF_SECCLASS TO-DEPLOY-e42, a07 canonical-first deploy (laptop)

**Session:** 2026-10-07 13:17Z - 14:20Z. **Seated on:** dell1's ask (bus 35e67892); the issuer
`2.0.0_SA_COO~M1` is on dell1 and cannot reach this broker.
**Order:** `org/tier2_senior/0.7.0_AE_CloudOps~S/task_orders/MDPF_SECCLASS.TO-DEPLOY-e42.a07-canonical-first-deploy-laptop.md`
(read at `origin/CLOUD`; it is not in this tree's HEAD).

## Current State

**The act is DONE and proven.** `s3://opal-data-49financial/_code/a07_dim_asset_classification.py`
now carries ETag `4092c5b80469ab780040a842eebe13cb`, which equals the md5 of
`git show 88c7018366:data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py`;
new VersionId `CQXT.gVFAKyhpUWVt3Vwt48F3IiIER3x`, 39,316 B, written 2026-10-07T13:44:30Z by ONE
`.tools/safe-deploy.sh` run from a scratch worktree at `q/dell1/secclass-r9-held-32/r1`
(`b0132b22a8`). AC1 prints `E42-A07 ok=True`.

The upload moves no served bytes: a07 is a build-time script, so the Advisor Intelligence
`dim_asset_classification` and `alias_key_expansion` partitions already served stay as they are
until the next chain run rebuilds them. That run is where the 164 keys re-bucket.

## What was measured, in the order the TO asked for it

1. **Candidate equality.** `git show 88c7018366:<path> | md5sum` = `4092c5b80469ab780040a842eebe13cb`;
   the worktree file at `b0132b22a8` = the same md5; 39,316 bytes on both sides.
2. **Timing (CTO condition 8).** No 49F/COT chain run in flight. The advi 49F chain host
   `bd-gold-layer-runner` `i-01003b035d2988dfb` read `stopped`. Both of today's dispatches had
   already completed with `signature: OK` and `ssm_rc 0`: `source: advi.49f.silver-accelerator`
   at 09:47:26Z (command `2b95bd75`) and `source: advi.49f.scheduled-floor` at 12:45:41Z (command
   `1e35e0db`, SSM document finished 12:48:19Z). `ssm list-commands` filtered `Status=InProgress`
   and `Status=Pending` both returned EMPTY. All three COT runs for 2026-10-07 read Success
   (bronze 11:33:04Z, silver 11:34:16Z, gold 11:36:06Z).
3. **Rollback read FIRST (COO condition 5).** `list-object-versions` gave IsLatest VersionId
   `72tSRnxMSKkBdtgAJZtqQcHeebqACIl1`, ETag `9202d701c552d4fb38a40f975f0eae9e`, 34,289 B,
   2026-09-01T14:12:21Z, on a versioned key (9 versions). After the act, `head-object --version-id`
   on it still returns those bytes, so the rollback handle is live.
4. **Ledger OPEN before the act.** `secclass-e42-a07-deploy-s-20261007`, 2 legs, window 30h,
   committed `da2368a603` before the upload.
5. **The upload.** `DEPLOYED [advi] ... -> _code/`; `VERIFY OK comp-pipescript deployed`;
   `OK: safe-deploy gate PASS -- all 1 file(s) deployed and verified`.
6. **Scope held, measured not asserted.** The upload plan was exactly ONE key
   (`file_to_s3_target` -> `(opal-data-49financial, _code/a07_dim_asset_classification.py, advi)`,
   `second_targets_for` `[]`, `shipped_artifacts` `[]`, bundle `None`), computed BEFORE the run. And
   no other key moved: of the 84 keys under `_code/` (denominator printed), a07 is the only one
   with a 2026-10-07 LastModified; the next most recent is `_code/perfrp_firm_pin.py` at
   2026-09-30T07:36:19Z.

## Instrument notes worth keeping

- **`events list-rules` cannot see this chain's schedule at all.** `advi-49f-gold-floor` lives on
  the EventBridge **Scheduler** plane: `scheduler get-schedule` reads ENABLED, `cron(45 12 * * ? *)`,
  UTC, target `advi-49f-gold-dispatch`. The 152 rules across 2 pages that `list-rules` does return
  do not contain it. A timing read done only with `list-rules` would have reported the wrong window.
- **The chain has a second, event-driven trigger.** `advi-49f-silver-accelerator` fires the same
  dispatcher when a QUALIFIED Schwab closure marker lands at
  `s3://opal-data-assets/schwab/*/meta/complete/date=*.json`; unqualified markers log
  `SKIP: ... closure.status=incomplete -- not dispatching`. Today's qualified closure fired and
  completed at 09:47Z, so both of the day's windows were shut before the act. A re-published marker
  is the one residual off-schedule path -- the BLIND the order's own preflight named.
- **The 49F served guard cannot fire on a `_code/` write.** `opal-49f-served-guard-on-write`'s
  event pattern binds bucket `opal-data-bd` and key `platinum/firm/header_metrics.json` only. Read,
  not assumed.
- `safe_deploy_core.py` contains no SSM dispatch and no git push, so the deploy could not fire an
  ad-hoc chain run or move a shared branch.

## Blockers

**None on the act.** One ARMED row and one leg left open on purpose:

- **Row `MDPF_SECCLASS-S55`** (OBSERVATION, ARMED, `disarm_owner` `1.0.0_SA_CTO~DELL1`): the CTO
  half of this sign-off is unreachable from the laptop.
  `CTO_HALF_MDPF_SECCLASS_SC_e42_A07_CANONICAL_FIRST_20261007.md` `@b3092be6d2` -- the pin is not a
  valid object after a full fetch of every origin branch, and the path exists on NO ref (78
  `CTO_HALF*` files on `origin/CLOUD`, 12 of them SECCLASS, none for e42). The order says to read
  BOTH halves in full. All eight conditions were carried verbatim, but from the COO half's pushed
  bytes -- which are signed, cover both branches, and restate the CTO half's whole delta -- rather
  than from the CTO half's own. Rule 22a's byte-read was unsatisfiable here, not skipped. Disarm is
  one push.
- **Ledger leg L2 is OPEN by design.** The first scheduled chain run after the upload must be read
  for the dim's `A5-A07-SOURCE-CENSUS` line and the d06/d08 mix totals, with every class move
  compared against `A07_SWITCH_BEFORE_AFTER_20261007.json`; any move that JSON does not list is a
  rollback. Next floor fire 2026-10-08T12:45Z. Window 30h for exactly that reason.

## Next Steps

1. **[`2.0.0_SA_COO~M1`]** Read the post-run leg and flip `<status>` on TO-DEPLOY-e42. Reported on
   the bus, MessageId `96c71f95-380c-44ce-b15d-b14585309718` (SENT, unacked at the time of writing).
   `MDPF_SECCLASS.TO-DEPLOY-e21`'s `<status>` also still reads `pending` although that deploy
   landed and its ledger CLOSED at 10:44Z today -- the same issuer's flip.
2. **[`1.0.0_SA_CTO~DELL1`]** Push the e42 CTO half and the `b3092be6d2` commit onto a pushed range.
   That disarms row S55 and is the only act that does.
3. **[`0.0.0_AB_MSTR`]** Land `da2368a603` and `d2f1594a84` on the trunk (asked, message
   `20261007T141149Z`). Push state MEASURED: both LOCAL on laptop CLOUD; `git ls-remote` reads
   origin CLOUD `fad25b1527`, and neither commit is an ancestor of it. Per `org/XXX.md` shared-branch
   law this seat commits and never pushes.
4. **[unowned, noted not filed]** `audit-archive-invoker.py` reports rc=1 with four
   `INTEGRITY/NON-APPEND-EDIT` findings (`org/mass-deletion-audit.log`,
   `org/safe-deploy-bypass-audit.log`, `org/mcp/agent-spawn-audit.log`, `org/law-edit-audit.log`).
   That class belongs to `/mstr-review`'s audit-log append-only walk, so it is surfaced here rather
   than re-filed.
