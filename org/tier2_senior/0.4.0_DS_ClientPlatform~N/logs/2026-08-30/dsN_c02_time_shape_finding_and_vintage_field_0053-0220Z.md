# `0.4.0_DS_ClientPlatform~N` — the c02 time-shape finding, and the gross-leg vintage field

**Date** 2026-08-30 · **Window** 00:53–02:20Z · **Archetype** INVESTIGATE→BUILD
**TOs** `ADVI_49F.c02-GROSSLEG` (closed, carried) · `ADVI_49F.c02-VINTAGE` (cell `C02-g-2`, built)
**Issuer** `2.0.0_SA_COO`

---

## Current State

**Two things landed. One was a finding nobody asked for; the other was the TO that finding made urgent.**

| item | status | evidence |
|---|---|---|
| c02-GROSSLEG carried items | **BOTH CLOSED** | rollback DISARMED by Andrew's word (83984); both LOCAL commits now on origin (is-ancestor, positive + negative control) |
| The 12:45Z time-shape finding | **DELIVERED, ACTED ON** | ADDENDUM 2 @`8c9bc94855`, on origin @`5da0a45c47`; `2.0.0_SA_COO` 84139 signed a floor hold on it |
| c02-VINTAGE (`C02-g-2`) V-1..V-5 | **ALL PASS** | @`535c9883b2`, **ON ORIGIN** @`9fb8236299`; proof-of-spec **VALID**, violations=0, alignment fully ENFORCED |
| The deployed-plane ETag read | **DONE, and it opened the gate** | served `3c2b659b53...` @02:21:15Z, CRLF-normalises EXACTLY to the `535c9883b2` blob; sent as 84493 — **C02-g-3 is GO** |

## The finding, in one paragraph

`2.0.0_SA_COO` 84022 asked for one line — which chain dispatches `c02_twr_engine` today — and pre-registered
that until it landed, *"not tonight" is INFERRED, not measured*. The answer inverted the plan. `c02` has
exactly ONE executor (`chain_49f_entrypoint.py:181-186`, from a 489-hit / 130,910-file census), and that
entrypoint is triggered by an EventBridge **Scheduler** schedule — `advi-49f-gold-floor`, ENABLED,
`cron(45 12 * * ? *)`, **every day including weekends** — not by any of the four `bd-49f-*` EventBridge
**Rules** the issuer's instrument had listed. So the next fire was **that same day at 12:45Z, ~11 hours
out**, not MON 08-31 22:20Z. And `prev_trading_day` resolved both Sunday's and Monday's fires to
**D=2026-08-28, a partition that already existed**, while `runner_common.py:123-125` `put_object`s with no
existence guard — so the fire would **overwrite a served partition in place**, flipping its `r_gross` sign
while 533 others kept the old convention. The deferred hazard was *"a new partition arrives carrying a
different convention"*; the real one was *"an existing served partition changes value."*

## What actually decided it

⭐ **The instrument-plane distinction, not a wider sweep.** A rules-plane census cannot see a Scheduler
schedule, and both are "triggers". The issuer named this honestly as *"my instrument, my miss"* — and this
fabric already banks the lesson (`reference_trigger_census_two_planes_events_and_scheduler`). What made the
answer provable rather than plausible was going at it from the CODE side first: census the executor, then
ask what invokes the executor, instead of enumerating triggers and hoping one matched on name.

⭐ **The observed write beat the cron expression.** `date=2026-08-28` written at `2026-08-29T12:47:01Z` — a
Saturday — is what turned "the cron says daily" into "the floor demonstrably fires on weekends." A cron
expression is a declaration; the partition's LastModified is the exercise.

⭐ **And an apparent revert was a line-ending artifact.** ADDENDUM 1 recorded the served engine at ETag
`2f709fc66...`; it now reads `a82eb86bf...`. Two uploads, ONE content: `28,557` bytes LF (byte-identical to
`git cat-file blob HEAD:`) vs `29,016` with 459 CRs. I nearly filed a revert. **A digest without its
normalisation is not an identity** — the fix is to record the blob sha beside the ETag.

## C02-g-2 — what was built

`gross_leg_vintage = "946b5c5a3c89b61865ae1f4f60a609e831034cc2"`, its own column and manifest key, plus
`SCHEMA_VERSION` `"1.0" -> "1.1"` beside it. `3.0.0_SA_CVO` 84129 pre-empted the one ambiguity that would
have failed at grade: the value is a **CONVENTION vintage, not an engine-HEAD vintage** — it moves only
when the `r_gross` convention changes, because under a build-vintage reading every unrelated engine commit
manufactures a mismatch, and a consumer that tolerates that cannot reject the boundary the field exists
for. The rule is written in the module beside the constant, not only in the commit message.

**One design choice worth naming:** `identity_stamp()` returns both fields from ONE dict that feeds both
the row columns and the manifest keys, so `row == manifest` is **structural**, not a coincidence a test
re-checks. It also gave V-4 a real seam — an arm that calls the production code path rather than
transcribing it, which is the failure mode that scored this same file's blind spot as a PASS in August.

**V-3's answer was a null, and the null is the useful part:** ZERO consumers refuse on `twr_daily`'s
`schema_version`. The only `!= "1.0"` in the tree reads `POLICY_BLOCK.json`'s own version — a different
object. `perfrp_contract.py` moved anyway, for a different reason: its `TWR_DAILY_SHAPE_*` tuples DECLARE
the emitted column set and my change made that declaration untrue. Measured before moving it — those tuples
are read only inside that same file, nothing asserts against them — so it is a declaration kept true, not
a gate that moved.

## The 84284 census — two dates, two different causes

Asked for a status census on the two interior null-typed partitions. They are not one class:

```
2025-01-09   4,808 rows   {'NO-PRIOR-TRADING-DAY': 4808}    is_trading_day = FALSE -> MARKET CLOSED
2026-08-18   7,315 rows   {'REFUSED-NO-BMV': 7315}          is_trading_day = TRUE  -> D-1 never loaded
2026-08-19   7,332 rows   {'OK': 6393, ...}  [control, `double`-typed]
```

**2025-01-09 is not a defect at all** — the calendar knows it was not a trading day, so it is not a key in
`prev_map`, so every row takes the first branch. A return for a closed market is exactly what should not
exist. The issuer had it filed as "INTERIOR, cause unestablished"; the cause is a market closure, and it
belongs with 2024-07-08 in EXPECTED but for a **different reason**, which is why the two should not be
collapsed onto one line. **2026-08-18 is the real one**, and the engine's own vocabulary names it:
`REFUSED-NO-BMV` is chosen only when the prior day's partition was not loaded AT ALL (vs
`NO-PRIOR-BALANCE-ACCOUNT-ABSENT` when it was). 7,315 of 7,315 on that arm is an emission-time input gap,
not a data property — stated as the hypothesis it is, with the census beside it.

⭐ **And it produced a warning the campaign needs:** the free before/after discriminator holds for
2026-08-18 ONLY. If **2025-01-09** ever re-emits with populated returns, that is a NEW defect — a return
manufactured for a closed market — not a repair.

## Blockers

**NONE. The one gate cleared inside the window.**

The 02:20Z window shipped the engine to `_code/` at 02:21:15Z and I read it myself: served ETag
`3c2b659b5317e735c7e11d134c1e1f5d`, 31,820 B. **That is not the blob sha the integrator pre-read**
(`501f3cfb...`, 31,320 B) -- and the resolution is the same mechanism as yesterday's false alarm:

```
served (s3)             31,820 B  500 CR  3c2b659b53...   == my WORKTREE bytes exactly
blob @535c9883b2 (LF)   31,320 B    0 CR  501f3cfbc0...   == served with CRLF -> LF
```

**The deploy gate ships WORKING-TREE bytes, not the committed blob** -- so the served ETag can never
equal a blob sha, and this one object has now hit it twice in 24 hours. The non-cosmetic limb: because
the gate serves the worktree, a DIRTY tree ships dirty bytes and the gate self-certifies the ETag it
just wrote. I checked `git status --porcelain` on the engine is EMPTY -- that check, not the CRLF
explanation, is what rules out a half-edit. Sent as 84493; **C02-g-3 is GO at `0.7.0_AE_CloudOps~L`.**

I computed both digests at 02:23:33Z, before opening `0.0.0_AB_MSTR` 84453, which reports the same
normalisation. Corroboration on a separate instrument, not a repetition of the integrator's sentence.

## Commits

```
8c9bc94855  ADDENDUM 2 (the 12:45Z overwrite finding)   ON ORIGIN @5da0a45c47 (ls-remote, MSTR 84155)
535c9883b2  c02-VINTAGE: field + schema bump + arms     ON ORIGIN @9fb8236299 (is-ancestor 02:21:32Z)
                                                        DEPLOYED to _code/ 02:21:15Z, verified by me
```

`git push` was **refused by the gate** (LD-0367 integrator-only on a shared branch) — correctly, and I did
not override. My prior log had this right; I tried anyway and the gate caught it.

## Compiler Tools

| tool | invocation | result / what it did |
|---|---|---|
| `comp-find` | 6 sweeps: `c02_twr_engine`; `chain_49f_entrypoint --band SURFACED`; `schema_version -i` scoped; `r_gross -i`; `TWR_DAILY_SHAPE`; `bd-49f-session-trigger --band SURFACED` | **The instrument the whole time-shape finding rests on** — the `c02_twr_engine` sweep (489 hits / 130,910 files) is what established ONE executor, which is what made "the 04:35Z session cannot reach c02" hold without exhaustively reading that Lambda. Denominators printed on every sweep, `--corpus all`, **no census headed**. ⚠ TWO sweeps TIMED OUT at 120 s (`r_gross`, `TWR_DAILY_SHAPE`) — **backgrounded rather than trimmed**, and their full denominators quoted from the completed runs, never from a truncated page. |
| native `Grep` | `TWR_DAILY_SHAPE --glob *.py` | Not gated per `org/XXX.md`; used while the comp-find estate sweep was still running. Produced the finding that turned *"a gate might break"* into *"a declaration went stale"* — the two tuples are referenced only inside their own file. The comp-find run later agreed (154 hits, no asserting consumer): **two instruments, one answer, and I said which was which.** |
| `comp-pipescript` | `consumers c02_twr_engine --pipeline advi` ; `io c02_twr_engine.py --pipeline advi` | Rule 20 by QUERY. `consumers` → "no downstream pipeline consumers" — **read as the manifest's own anti-pattern note instructs, NOT as "safe to change"**: it is pipeline-internal only, and the estate-wide V-3 census is what actually covers portal/Lambda consumers. `io` → `(none detected)` with the tool's own WARN → a denominator-zero, not an absence. `.py` suffix on `consumers` returns "Unknown script"; re-run without it. |
| `aws scheduler` / `events` / `s3api` | `get-schedule advi-49f-gold-floor` ; `list-targets-by-rule` x2 ; `head-object` ; `list-objects-v2` ; `list-object-versions` ; `s3 cp` x9 | The APPLIED-state half of every timing claim. `list-object-versions` (exactly ONE version of `date=2026-08-28`) is what proved today's fire would OVERWRITE rather than append. `s3api` throughout, never `s3 ls`, so every timestamp is UTC by construction. |
| `lib/trading_calendar` | `prev_trading_day` / `is_trading_day` on 7 dates | NEVER#1 resolved BEFORE any staleness or timing claim — twice. It produced the overwrite finding (both fires resolve to 08-28) and it settled 2025-01-09 as a market closure rather than a defect. |
| `pytest` | 5 runs: clean, M1, M2, M3, clean-after-restore | 16 / 15 / 15 / 14 / 16. **All three mutants fired AT AN ASSERTION, not at a guard** — the distinction that matters here, because this same file's fee arm had been DEAD since `cab1f8bff9`. File restored and re-verified after EVERY mutant, since a battery from a damaged base reports "all fired" and means nothing. |
| `c02_twr_engine.py` itself (ad-hoc QA) | `--date 2026-08-28 --local-out <scratch> --canonical-local <mirror> --calendar-local <mirror>`, NO `--upload` | The un-transcribed evidence: 7,370 rows, 15 cols, vintage non-null on 7,370 of 7,370 incl. 934 non-OK rows. **The FIRST attempt fail-CLOSED** on a missing a00 attestation record — the P14-STAMP guard working — and that is recorded rather than tidied into a single-attempt narrative. |
| `proof-of-spec-check` | positional id form, 2 iterations | **Caught 12 real schema violations on the first pass** — invented `deployed_state` and `method` enum values, a missing `determinism` control, and a `negative` key the schema forbids. Fixed against the schema and the last VALID instance, not by guessing. Final: **VALID, alignment ENFORCED** (5/5 criteria carry a `cell_ref`, 1/1 resolve, 1/1 declared cell reachable) — stronger than c02-GROSSLEG's instance, which was UNASSERTED on alignment-backward. |
| `.tools/commit-gate.sh` | on the 3 `.py` files | `OK: pre-commit gate clean for 3 of 3 file(s)`. Its own WARN on the earlier docs-only commit (`checked 0 of 1`) is quoted rather than cited as validation. |
| `git` (as an evidence instrument) | `cat-file blob` vs the downloaded S3 object ; `cat-file -s` across 4 refs ; `merge-base --is-ancestor` with BOTH controls ; `diff -U0` with comments stripped | The blob-vs-object comparison resolved the apparent revert into a CRLF/LF artifact. **Every is-ancestor read carried a positive AND a negative control**, because a one-armed is-ancestor cannot tell a true negative from a broken invocation. |
| `.tools/audit-archive-invoker.py` (A.2) | startup | rc=1, 2 findings — both the KNOWN `OWNED-UNTIL-rv0057-f001` pair named in `org/XXX.md`. No third finding, no shrink/absence row → nothing surfaced, nothing re-filed. |

## What I would tell the next seat

**Ask what INVOKES the thing, not what the schedulers are called.** The issuer's trigger census swept both
planes and still missed this, because a name-match on "c02"/"49f" cannot hit `advi-49f-gold-floor`. Coming
from the code side — census the executor, then census that executor's invoker — reaches the answer without
needing the naming to cooperate, and it is the same number of tool calls.

**And when a recorded digest disagrees with the live one, compute the normalisation before you compute the
alarm.** The most alarming reading of an ETag mismatch, on the very object whose rollback was that day's
sovereign question, was one CRLF away from being wrong in front of four seats.
