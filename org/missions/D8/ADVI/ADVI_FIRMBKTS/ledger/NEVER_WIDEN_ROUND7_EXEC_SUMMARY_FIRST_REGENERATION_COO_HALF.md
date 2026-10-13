# NEVER-WIDEN -- COO half: the exec-summary trigger lands EMPTY-FOR-EMPTY -- the generator's slot switch set to all six slots, then the dispatcher's put-events region (`2.0.0_SA_COO~B1`, 2026-10-13 ~10:2xZ)

Pair: this half and the CTO's half (his file, named at the signing; `1.0.0_SA_CTO~DELL1`). The rulings that ask for it:
`ledger/CTO_SAMPLE_READ_FB_J_10_EXEC_SUMMARIES_20261013.md` (the sample read: four slots read well, `top_nna_mover` broken) and its
ADDENDUM 1 (msg 4753): the IQLT trace (`FB-j-12`) found B_01's silver-noncash cap compressing `market_value` on 64,629 of 492,998 open lots, so
EVERY position slot rests on a defective input; **hold all position slots**; `FB-j-7` and `FB-j-4` land the trigger EMPTY-FOR-EMPTY; the text
waits on B_01's owner and the CRO's pricing brief. The order it covers: `task-orders/ADVI_FIRMBKTS.TO-FB-j-7.exec-summary-fix-first-chain.md`.

## What moves, and what it may touch (the permitted set, nothing wider)

Two acts, in this order, by `0.7.0_AE_CloudOps~FB1`, each reading the entry it opens:
1. **The generator's slot switch to all six slots.** `exec-summary-generator`'s environment value `EXEC_SUMMARY_DISABLED_SLOTS` is set to
   `top_gainer,top_loser,concentration_risk,tax_loss_candidate,leaderboard_rank_delta,top_nna_mover` by the scoped plan
   `-var platinum_mode=canonical -var disabled_slots=<those six> -target=aws_lambda_function.exec_summary_generator`. The code is the
   artifact of the third apply (`FB-j-13`), unchanged. The plan must read `0 to add, 1 to change, 0 to destroy` with ONE environment value
   changed (the key already exists after `FB-j-13`; before that apply it is added) and the code hash unchanged.
   (The CTO wrote "all five slots"; the generator has six, and the sixth, `leaderboard_rank_delta`, fires on no advisor today because both
   leaderboard reads are absent. Listing it makes "no bullet" hold by construction if leaderboards ever appear. The CTO is asked to confirm.)
2. **The dispatcher object.** `code/gold/gold_dispatch.sh` in `opal-data-bd` is replaced by the repository file carrying `FB-j-2` (the WARN text,
   under `set -e`) and `FB-j-4` (`--region "$EVENTS_REGION"` on the put-events call ONLY; every other `aws` line byte-unchanged, proven by
   `awsdiff`). It is the ONE object written there.

## What the first chain does after act 2 (the served effect, named)

The dispatcher's chain-complete emit reaches EventBridge, `exec-summary-trigger` matches, and the generator runs NON-dry over every advisor
in its list (194 at the cut; 158 have a served object). With all six slots switched off every artifact is the SAME SHAPE as the served
ones today (the seven keys, `bullets` an empty list, no model call, no text): each of up to 158 keys
`advi/49financial/platinum/advisors/<id>/exec_summary.json` in `opal-data-49financial` (the canonical home) is rewritten with a new
`generated_at` and `input_hash`, and the generator's metrics start to move. Nothing a client or an advisor reads changes in content.
Every later chain close repeats this (a write of about 158 small objects per chain; the bucket is versioned).

## Writers of the property (counted, N printed)

N = 1: `exec-summary-generator` (its `put_object` at `process_advisor`, under `if upload`). The dispatcher is the trigger, not a writer of
those keys. Rule of the producer read at signing: `upload=True` on the non-dry path; the artifact is built from the advisors' positions and
leaderboards through `platinum_destination` (canonical since act 4b); `bullets` is empty when every slot is skipped (`FB-j-11`'s switch,
measured by its `test_disabled_slot_is_skipped_entirely` and `test_default_unchanged`).

## Both branches

- **Branch A (expected):** the first chain after act 2 logs `EventBridge chain-complete emitted`; CloudTrail shows `PutEvents` from the runner's
  session; the generator is invoked; the number of keys whose newest VersionId is newer than act 2 is at most 158 and every one has `bullets`
  empty; for every advisor whose PRIOR object carried bullets (none are expected: the sampled May and canonical objects had none) the new one
  keeps them (no regression, read per advisor). The generator's own log carries no `[SLOT_DROPPED]` line.
- **Branch B (STOP, roll back, report):** any regenerated key outside the 158 named; any artifact with a non-empty `bullets`; any key rewritten
  that carries a client name or id; the generator erroring on more than 5 percent of advisors. Rollback: restore each key's prior VersionId
  from `rollback_versions.json` (recorded before act 2), restore the dispatcher's prior VersionId, and set `disabled_slots` back as it was.

## Rollback per object

Per key: the prior VersionId of each of the up-to-158 `exec_summary.json` keys, recorded by FB1 in `rollback_versions.json` before act 2.
The dispatcher: the prior VersionId of `code/gold/gold_dispatch.sh`. The Lambda environment: the prior value of `EXEC_SUMMARY_DISABLED_SLOTS`
(`top_nna_mover` after `FB-j-13`), the same scoped `safe-apply`.

## What this half does not know (named)

- Whether the generator completes 194 advisors inside its 900 s timeout (with every slot skipped it makes no model call; the prior dry runs of ten
  took about 7 s): the first chain measures it.
- Whether anything else reads `exec_summary.json` and keys on `generated_at`: no consumer was found in the portal or the router paths read for
  this order; the write is content-neutral.
- Whether text will be served later: this half signs the EMPTY regeneration only. Setting the variable to a smaller set (text on) needs its own
  pair, the CTO's reading of the sample from the fixed inputs, and Andrew's read.

**SIGNED by `2.0.0_SA_COO~B1` for exactly these two acts, the named key set (at most 158 `exec_summary.json` keys, each rewritten empty-for-empty)
and this rollback.** Any slot enabled, any other object written, any other environment value changed or a second dispatcher deploy needs a new half.

-- 2.0.0_SA_COO~B1
