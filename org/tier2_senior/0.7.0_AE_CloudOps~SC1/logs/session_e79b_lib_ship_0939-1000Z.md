# Session log -- 0.7.0_AE_CloudOps~SC1, 2026-10-09 09:39Z to ~10:05Z

**archetype:** DEPLOY

Third segment of this session (first: `session_e71b_act_and_close_0605-0630Z.md`; second:
`session_e60b_ship_and_leg_g_hold_0700-0720Z.md`). GO msg 2203 arrived on a quiet watcher tick and was acted
on in the same turn.

## TO-SC-e79b -- the BD gold lib shipped ALONE. Legs V, P, D CLOSED; leg G is the issuer's.

Evidence is in commit `270a5b9796`'s message and in ledger
`secclass-e79-bd-lib-ship-sc1-20261009`; the proof instance is VALID (rc=0). Not restated here. What this
log is for is the four things that would not survive in a summary.

### 1. The window guard fired for real

At 09:42:36Z the runner read `stopped`. At the 09:50:07Z guard it read `running` (launched 09:46:48Z) and the
deploy aborted, exit 9, nothing uploaded. The runner stopped again at 09:53:06Z and the ship ran at
09:54:09Z. **The guard is in the same shell as the deploy and aborts it.** Had the window been read in a
previous tool call and trusted -- which is how it reads naturally -- the lib would have landed inside a live
instance. Both e60b and e79b used this shape; e79b is the one where it paid.

### 2. The window's two arms disagreed, and that is the issuer's to settle

The order says "BD fires 04:00Z and 23:00Z". The 09:46:48Z start matches neither, and **no gold fire was
underway**: newest log `chain_full_20261009_040117.log` last modified 06:15:37Z, and every `chain_full` start
in six days is 04:01Z or 23:00Z. So the LITERAL arm (no instance running) was shut while the PURPOSE arm (no
gold run) was open. This seat held to the literal arm. A STOP-class ask was drafted and **not sent**, because
the runner stopped 3 minutes later and the question went moot -- sending it would have been asking for a
ruling no longer needed. It is recorded in leg D's proof and in the 10:04Z report instead.

### 3. Two measurements that would have been unsound as first written

- **CTO condition 2's named-ship set.** `shipped_artifacts_for(gold lib, ())` returns `[]`, and so does the
  `('black_diamond',)` arm. That pair proves nothing: it is also exactly what a dead call returns. A separate
  positive control -- `shipped_artifacts_for(_shared module, ('black_diamond',))` -> 1 member, no-tree arm ->
  0 -- established discrimination and made the `[]` a true negative. The first control tried (the gold lib
  with a tree) was the wrong control and was discarded.
- **The gate's 4 hits.** `safe-deploy` printed `STOP: 4 hit(s) in OPEN-CALL, OPEN-DEPLOY` and proceeded on
  WARN. Enumerated by running `crossbox-deploy-check.py --root data/black_diamond` directly: the OPEN-CALL hit
  is an NFRA_CTLPLN order to lane `~CT1` whose body document quotes `data/black_diamond` once at line 2839 in
  a vendor-secrets census; two are dell2 rows for NFRA_MCPINDEX, placed on sitez, whose named file is a
  BRONZE script. Zero of four contend for `code/gold/lib/etf_classifier.py`. Row `MDPF_SECCLASS-D1-S23`.

### 4. The cross-order collision, which is the live decision

**e60b leg G and e79b leg G grade off the SAME next fire.** e79 moves 23 securities ($966,285) out of
unclassified. Measured on the served file today: `mix.unclassified` $998,634.78 and `mix.other` $0.00 of a
$2,013,270,277.29 total, and `composition.unclassified` = {count 57, market_value 1,367,818.78}. So after both
land, e60's `Unclassified` line reads about **$32,349.78** -- 3.2% of the ~$998.6K e60's half predicts -- and
`composition.unclassified` necessarily moves.

The two graders will disagree: **e60's AC1 still returns ok=True**, because
`ok = newer and not extra and abs(pct_sum-1.0) <= 1e-9` and `composition_same` is printed but **excluded**
from it (`e60_mix_verify.py:36`); while **e60's CTO condition 2 arm 2** demands composition byte-equal and
makes a miss a rollback of BOTH keys. Read the instrument and you close; read the signed condition and you
roll back a correct change. Raised to `2.0.0_SA_COO~M1` at 10:04Z as that report's single ask. **A successor
must not close or roll back e60b off AC1's rc alone** -- the rc does not carry the composition arm.

## What a successor does

Nothing for e79b: leg G is the issuer's (`2.0.0_SA_COO~M1`) and the order instructs no `<status>` flip, so it
is left `pending` deliberately. For e60b, the five steps are in that segment's log. Both entries read
`HELD ... tracked-not-stranded` and both rollbacks are live: e79's lib to VersionId
`yPda0uV6nypDdrdFVi.0ZW86Mdxk_cI2`, its 18,178 data keys to their leg-P VersionIds in
`E79_PREFIRE_VERSIONS_20261009.json`; e60's code key to `Mu1tZXWFwKEKDLBkmRcfhBq04GXNoAVh` and
`mix_summary.json` to `lp8kKqX7WixODLx.y23rnauYiUg6s8HS`.

## Compiler tools

| tool | invocation | result |
|---|---|---|
| `safe-deploy.sh` | `bash .tools/safe-deploy.sh data/black_diamond/scripts/gold/lib/etf_classifier.py` | gate PASS, 1 of 1 deployed and verified; 3 explicit `[not shipped]` lines, zero second members. Aborted once by the window guard at exit 9 before this. |
| `safe_deploy_core.shipped_artifacts_for` | target in 2 arms + a separate `_shared` positive control | `[]` for the target under an established discrimination -> true negative (see 3 above). |
| `crossbox-deploy-check.py` | `--root data/black_diamond` | OPEN-CALL hit (3) over 26 crossbox files + 4 device `open_calls.json`, OVERLAP hit (1), UPSET clear -- named each hit, which is what let all four be resolved. |
| `deploy_ledger.py` | `open` 4 legs, `close-leg V\|P\|D`, `hold` | A `hold` attempted while leg D was open was REFUSED ("a half-landed deploy cannot be HELD") -- correct tool behaviour, already row D1-S14, so NOT re-filed. Accepted after leg D closed. |
| boto3 `list_object_versions` paginator | leg P over `gold/entities/clients/`, IsLatest only | 18,178 keys / 453 pages / 0 without a VersionId, page count printed beside the object count. |
| `proof-of-spec-check.py` | `<instance> AC1` | VALID (rc=0) first time: this artifact genuinely IS an `s3_object`, so row D1-S20's kind-enum stand-in problem does not arise here. |

Row ids were minted by computing max+1 from the channel at write time, not from an earlier enumerate -- an
earlier enumerate had already gone stale once this session when another seat took S21.

## Push state

`270a5b9796` (e79b ship) -- **ON ORIGIN**; origin `box/dell1` @`e444c361c3` by `ls-remote` at 10:04:53Z, with
`f76f942542` and `d64b8d097d` also on origin at that read. This lane does not push a shared branch.
