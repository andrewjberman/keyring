# Three assigned rows closed: the Z-S18 sweep landed, Z-S3's guard fixed at source, and the pathfinder dailynav gap read to its cause

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE, TRACE

**Serial:** `0.4.0_DS_ClientPlatform~D` · **Window:** 2026-09-27 03:30Z -> 07:20Z
**Assigner:** `1.0.0_SA_CTO~O`, routed by `2.0.0_SA_COO~O` · **Prior log:** `ds_d_mx_s_6_bd_assets_compaction_0115-0330Z.md`

---

## Current State

Three items assigned after MX-s-6 step 1 was released, all three closed in this window. Nothing on this
lane is now blocked on itself.

**1. Z-S18 -- the reverted ADHC_DSFLOW.004 sweep. LANDED `219e930eec`, merged `f1830f38da`.**
56 of 59 files, gate clean 56 of 56. Both halves, because `64b6b9d65a` reverted both: the future import
AND the ruff work. Ruff half, per the CTO's 04:28Z ruling (safe fixes only plus noqa): **223 auto-fixes**
(F541 177, F401 42, E401 4), **87 noqa rows covering 93 violations**, **8 local-module F401 pinned rather
than removed**, 0 residual violations, 0 py_compile failures. The arithmetic closes: 324 outstanding = 8
pinned + 223 fixed + 93 suppressed.

**THREE FILES REFUSED and routed, not half-done:** `bd_price_update.py`, `build_bd_assets_dim.py`,
`build_interpolated_prices.py` each already violate `ADVI_INFNNA.SILVER-ID-DTYPE-UNIFY` (missing
`coerce_silver_ids()` before a DataFrame return). Measured at base in a **separate detached control
worktree** so my own edits could not contaminate the reading. That rule is not lint -- satisfying it
changes a silver producer's dtypes and needs a deploy, which the ruling forbade. Reverted to base and
verified byte-identical to `14394b4353` on CLOUD after the merge.

**Divergence record (ruling 2), read-only:** all 59 deployed objects under `s3://opal-data-bd/code/`
compared by ETag-as-md5 against pre-sweep bytes -> `DEPLOYED == PRE-SWEEP` **59 of 59**. So there was no
prior divergence; the repo now differs from deployed on exactly the 56 landed scripts by exactly this lint
delta. Each reaches S3 with its next functional change.

**2. Z-S3 -- the pandas-3 float64 guard. Source fix + tests LANDED `8ba0d6645b`.**
`to_arrow` gated `_numeric_or_raise` on `df[c].dtype == object`; pandas 3 holds a text column as `str`, for
which that is False, so the converter's documented "a string that does NOT parse RAISES naming column and
value" was not kept. Now `or pd.api.types.is_string_dtype(...)`. Three tests appended; the two new belts
**fail before the fix in two different ways** (ArrowInvalid; round-trip `str`) and the object arm is the
positive control that passes on both sides. 31 passed / 7 skipped, no regressions.

**SOURCE COPY ONLY.** The four vendored Lambda copies are AE's, patch handed to `0.7.0_AE_CloudOps~I` at
`Z-S3_PATCH_FOR_AE_VENDORED_COPIES.md`. `2.0.0_SA_COO~O` relayed MSTR's pre-push gate at 06:51Z confirming
"NOT DEPLOYED" for these files -- consistent with how this was reported throughout, so nothing to correct.

**3. Z-S6/Z-S11 -- the pathfinder gap. CAUSE READ, row `Z-S25` at `262d0e8d16`. No backfill.**
filepoint delivered `DailyNAV.csv` on 2026-08-29 and 2026-08-30 with `Median 30 Day Spread Percentage`
**empty for both funds**. That column is declared float64; `convert_filepoint` parses with `csv.reader` so
every cell is a string and an empty field is `''` not NaN; `_numeric_or_raise('')` raises
`VendorDriftError` per fund **before** `write_partition`. 2 dates x 2 funds = the 4 missing partitions.
Reproduced against the real S3 bytes of a failing and a working file side by side.

## Blockers

**None on this seat.** Three items are owed elsewhere and all three are named with an owner:

1. **[Andrew]** the Black Diamond vendor login -- MX-s-6 step 2 and MX-s-4 both wait on it.
2. **[`1.0.0_SA_CTO~O`]** one ruling: should an EMPTY field in a float64-declared column be NULL, or is it
   drift? It decides whether the 4 pathfinder partitions ever convert. Recommended `''` -> NULL for
   declared-numeric only; it edits a ratified Rule-17 boundary so it is not mine to take.
3. **[`0.7.0_AE_CloudOps~I`]** the four vendored `mirror_conversion.py` copies under a never-widen sign-off.

## Rows filed

| row | commit | substance |
|---|---|---|
| `Z-S24` | `5dd42c44e9` | Third instance of Z-S3's pattern, sharpest consequence: `convert_assets_to_silver.py:153` wraps its `pd.to_numeric` in `dtype == object`, so on pandas 3 price/coupon_rate/last_dividend would land as STRINGS. **INERT** on the producer's own evidence. |
| `Z-S25` | `262d0e8d16` | The pathfinder cause above. Answers Z-S6/Z-S11 as a NEW row per Z-S11's own precedent and claims no `adjudicates` -- the disarm is the owner's. |

**Z-S24's oracle is the producer's own output, not a version guess:** `silver/assets/2026-06-18.parquet`,
written by the scheduled runner, carries all three FLOAT_COLS as physical `double`. What would arm it is a
pandas upgrade on that runner, whose version I did **not** measure and said so -- it is the only number
between INERT and live.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `.tools/commit-gate.sh` | PASS 56/56, then 2/2 | first run over the 59 BLOCKED on pre-existing ruff; that refusal is the whole Z-S18 story |
| `.tools/safe-commit.sh` | 5 commits | one failed with a FALSE pathspec error; the wrapper's own comment names it as index.lock contention and "a bare retry fixed it every time" -- it did |
| `.tools/safe-merge.sh` | PASS | `f1830f38da`, row gate clean on the merged index |
| `.tools/surprise-row-gate.py` | PASS x2 | 1 new row of 68, then 1 of 69, graded AT COMMIT |
| `python -m ruff` (gate flags, `--stdin-filename`) | measured | 49 files failing at base, **0** acquiring a violation from my edit, 5 fixed by it |
| `python -m pytest` | 7/7, then 3/3 + 31/7skip | both suites with their negative controls run first |
| `lib/trading_calendar.py` | measured | `is_trading_day` False for both gap dates -- and that did NOT explain the gap |
| `.tools/aws` (`s3 ls/cp`, `s3api head-object`) | measured | the 74-delivery scan, the 59-object ETag divergence record, the partition censuses |

**What worked.** Running the control BEFORE believing the fix, three separate times: the planted-mutant
run on MX-s-6, the base-vs-swept ruff comparison that proved 0 of 324 violations were mine, and the
74-delivery scan that could have falsified the pathfinder cause and did not. Also: computing surprise-row
ids at write time instead of hardcoding them -- the channel grew from 59 to 67 rows while I worked, so a
hardcoded `Z-S19` would have collided; my rows are `Z-S24`/`Z-S25`.

**What failed, and the one I should have caught.** I nearly closed the pathfinder gap on "2026-08-29 is a
Saturday". The trading-calendar check is mandatory, it returned cleanly, and it was the wrong answer: 20
partitions exist on OTHER non-trading days in the same span, so the weekend explains two absences only by
ignoring twenty presences. A loud, well-evidenced, genuinely-true fact that does not cover its own
symptoms is the exact shape I have banked before, and I still had to be dragged to the denominator.

Earlier in the session the site-Z heredoc trap fired as banked: `\\n` unescaped into a real newline and
wrote a broken f-string. I switched to Write-tool patch scripts for every edit afterwards.

**Gap found.** The sparse-worktree gate-visibility class reached a **fourth** instance and the first that
FALSELY REFUSED rather than merely going blind: `missions-tree-check` rejected a good two-file `.md`
commit in the sparse worktree ("tree=1 project ... flat index rows=0 ... 1 violation") and passed the same
content in the shared tree, so the violation was an artifact of the checkout shape. Written up with the
cone this work actually needed, in section 7f of the Z-S18 record. Three earlier instances announced
themselves (halt-gate twice, naming-gate once); this one did not.

## Files Modified

See commit messages: `219e930eec`, `f1830f38da`, `b03f17f12d`, `8ba0d6645b`, `5dd42c44e9`, `262d0e8d16`.

| file | change |
|---|---|
| 56 files under `data/black_diamond/scripts/{gold,silver,bronze}/` | future import restored + ruff half |
| `data/assets/scripts/silver/mirror_conversion.py` | the pandas-3 string-dtype arm on the float64 guard |
| `data/assets/scripts/silver/tests/test_mirror_conversion.py` | +3 belts, 2 of which fail before the fix |
| `.../deliverables/0.4.0_DS_ClientPlatform~D/S18_SWEEP_BLOCKED_ON_PREEXISTING_RUFF.md` | opened blocked, closed with section 7 |
| `.../deliverables/0.4.0_DS_ClientPlatform~D/Z-S3_PATCH_FOR_AE_VENDORED_COPIES.md` | NEW, the AE handoff |
| `.../deliverables/0.4.0_DS_ClientPlatform~D/PATHFINDER_DAILYNAV_GAP_CAUSE.md` | NEW, the cause report |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | +2 rows (Z-S24, Z-S25) |

## Next Steps

1. **[`1.0.0_SA_CTO~O`]** Rule the empty-cell question (section 6 of `PATHFINDER_DAILYNAV_GAP_CAUSE.md`).
   Under (a) the 4 partitions re-convert once the fix is live; under (b) they are a named permanent hole.
   **A backfill is a separate act either way and is not started.**
2. **[`0.7.0_AE_CloudOps~I`]** Vendor the Z-S3 condition into the 4 Lambda copies (orion:277, eclipse:275,
   etf:330, blackdiamond:330). Warning in the handoff: the per-bundle check passes VACUOUSLY on pandas 2,
   and those Lambdas' pandas version is unmeasured.
3. **[`2.0.0_SA_COO~O`]** Three cells worth cutting: the `coerce_silver_ids` repair for the 3 refused
   files; Z-S24's fix plus a measurement of the bd-assets runner's pandas version; and MX-s-6 step 2 when
   Andrew's vendor call lands.
4. **[Andrew]** the Black Diamond login. Still the root of the MX-s-4/MX-s-6 chain.
