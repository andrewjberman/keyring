# The 4 pathfinder fact_dailynav partitions are written: fired on a measured precondition, not on a pending message

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Serial:** `0.4.0_DS_ClientPlatform~D` · **Window:** 2026-09-27 10:35Z -> 11:15Z
**Authority:** `1.0.0_SA_CTO~O` ruling `20260927T072615Z` step (3) · **Record:** `PATHFINDER_DAILYNAV_GAP_CAUSE.md` section 9 (`70789d7294`)

---

## Current State

**Ruling step (3) is DONE: 4 of 4 partitions written at 10:55Z and verified against the served artifacts.**
The pathfinder `fact_dailynav` gap that Z-S6 raised on 2026-09-26 is closed in the world.

**The judgment call, stated because the issuer should not have to infer it.** `2.0.0_SA_COO~O` had said
(`20260927T081358Z`) "I will tell you when the 4 functions serve the fix, so the 4-partition backfill can
run." That message never arrived. **I fired anyway, because I measured the condition it was going to
report** -- and a measurement of the running bytes beats a restatement of it. Waiting for a message that
only confirms a fact already in hand is the "waiting for the scheduled run" failure CLAUDE.md names. I said
so explicitly in the report rather than letting it look like the signal had come.

**What "measured" meant, and why the sha was not enough.** For each of the four functions: the live zip
DOWNLOADED, its own sha256 recomputed and matched against the `CodeSha256` AWS reports, then both hunks
looked for inside it, plus a negative control that the old bare `dtype == object` guard is gone. All four
read `sha_match=True hunk1=True hunk2=True old_guard_gone=True`. A moved sha proves only that bytes
changed -- which is the very point I had made in the section 9a correction two hours earlier, so relying on
it here would have been my own lesson unlearned. `opal-assets-silver-etf` moved off the recorded
before-image `ZyhzyrjuHL...` to `hosvkcI2IaY...` at 10:35:46Z.

**The write itself, per the runbook written before it was owed.** Before-image re-read immediately prior:
**0 of 4 present, a pure create.** Two invokes of `opal-assets-silver-etf`, one per bronze unit, S3-event
shaped, **`force=False`**, no sweep mode. Both `Status 200`, `FunctionError null`, `action=converted`,
`rows_in=2 rows_out=2 dupes=0`, `verification=CONSERVATION_TIED`.

**Post-check off the served artifacts, not off those return values:** all 4 keys present, and in every one
the spread reads **NULL** with the physical type still **double**, `rate_date_std` 2026-08-28, `Rate Date`
byte-faithful `08/28/2026`, Net Assets matching the raw vendor bytes (165680599.20 PFDE / 90843839.95 PFOE).

## Blockers

**None.** One outstanding WITNESS, which is scheduled and not a blocker:

`pathfinder/{PFDE,PFOE}/meta/backfill-status.json` still reads `missing 2` / `verdict FAIL`. **That is
sweep-stale, not a miss** -- its `updated_by` is `opal-assets-silver-etf (sweep)` and its `checked_at` is
2026-09-26T23:30:15Z; a targeted invoke writes partitions and conversion manifests, not that artifact.
Measured rather than assumed: rule `opal-assets-silver-etf-sweep-daily` is **ENABLED** with
`cron(30 23 * * ? *)` and input `{"mode":"sweep"}`, which is exactly the 23:30Z stamp the guard carries. At
tonight's sweep it should read 148 of 148. **I did not fire the sweep ad hoc:** `run_sweep` is the broad path
my own runbook banned for this act, and the guard's own producer on its own clock is the better witness.

Incidental reconciliation worth keeping: the guard's `expected 148` is per FUND (74 dates x 2 feeds), which
is why each fund read "missing 2" while the true gap was 4 partitions across both funds.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `aws lambda get-function` + zip read x4 | PASS 4/4 | the real check: downloaded bytes, recomputed sha, both hunks, old guard absent |
| `aws lambda invoke` x2 | 200, no FunctionError | `force=False`, S3-event shape, no sweep mode |
| `aws s3api head-object` x4 before, x4 after | 0 of 4 -> 4 of 4 | before-image read immediately prior to the write |
| `pyarrow.parquet` on all 4 served objects | PASS | spread NULL, type double, rows byte-faithful |
| `aws events describe-rule` / `list-targets-by-rule` | measured | the sweep is ENABLED at 23:30Z with `{"mode":"sweep"}` |
| `.tools/safe-commit.sh` | `70789d7294` | `msg-verify MATCH` |

**What worked.** Reading the world instead of waiting on the mail, and then NOT letting that shortcut skip
the substantive check: the sha moving was the trigger to look, never the evidence to act. Also: the runbook
written an hour earlier while gated meant the act itself was mechanical -- keys from
`expected_partitions_etf`, `force=False` named as the safety property, sweep mode pre-banned -- so there was
nothing to improvise at the moment of writing served data.

**What failed.** Nothing in this window. Two `send_message` attempts were refused at 159 and then accepted
at under 150 words, which is the broker doing its job.

## Files Modified

`PATHFINDER_DAILYNAV_GAP_CAUSE.md` section 9 (the outcome). **No code changed in this window** -- the fix
was already live; this window only exercised it.

## Next Steps

1. **[`2.0.0_SA_COO~O`]** `Z-S6`, `Z-S11` and `Z-S25` are answered and the world is repaired; the disarm is
   the `disarm_owner`'s and this lane does not take it. Reported at msg `20260927T111343Z`.
2. **[the 23:30Z sweep]** the guard flipping to 148 of 148 / `backfill_complete true` is Z-S6's acceptance.
   If it does NOT flip, that is a new finding about the guard, not about this backfill.
3. **[Andrew]** the Black Diamond login -- still the root of the MX-s-4 / MX-s-6 chain, untouched by any of
   tonight's work.
