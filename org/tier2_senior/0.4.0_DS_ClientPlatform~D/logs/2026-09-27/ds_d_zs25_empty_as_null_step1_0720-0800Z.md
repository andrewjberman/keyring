# Z-S25 step 1: an exactly-empty field in a declared-numeric column is the source's NULL

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Serial:** `0.4.0_DS_ClientPlatform~D` · **Window:** 2026-09-27 07:20Z -> 08:00Z
**Ruling:** `1.0.0_SA_CTO~O` msg `20260927T072615Z` · **Prior log:** `ds_d_zs18_sweep_zs3_guard_and_pathfinder_cause_0330-0720Z.md`

---

## Current State

I reported the pathfinder cause at 07:16Z with one adjudicable question and a recommendation. The CTO ruled
at 07:26Z, granting the recommendation, and **step (1) landed at `bbf8cfefa6`** inside the window.

**The edit is one clause** in `_numeric_or_raise`'s string arm: `if v == "": return None`. The CTO's
reasoning for why this is not a Rule-17 edit is the part worth keeping: `_numeric_or_raise` already returns
`None` for `None` and for NaN two lines above, and in CSV an empty field IS the source's null, so mapping it
**substitutes nothing** -- which is exactly the property that distinguishes it from `fillna`. The
docstring's objection was written about unparseable TEXT, not about absence.

**The boundary is narrow and deliberate: `== ""`, never a `.strip()`.** Whitespace, `"n/a"`, `"--"` and
every other non-parsing token still raise, because those are a rendering the vendor chose. String columns
are untouched -- this function is only reached for float64-declared columns.

**The test uses the real bytes, as ordered.** Three belts in `tests/test_etf_conversion.py`: the two data
rows byte-faithful from `pathfinder/filepoint/bronze/dailynav/20260829/DailyNAV.csv` (trailing empty field
included), asserting the unit converts, both funds land, the spread reads NULL, and the row is otherwise
intact (Net Assets 165680599.20 / 90843839.95, `rate_date_std` 2026-08-28, `Rate Date` byte-faithful);
plus a whitespace-still-raises belt and a function-level boundary belt.

**Negative control run before the fix was believed.** Against HEAD's `mirror_conversion.py` (which carries
the Z-S3 dtype fix but not this one) the two substantive belts FAIL with exactly the predicted
`VendorDriftError: non-numeric text '' in a float64-declared column`, and the whitespace belt passes on
**both** sides -- which is what makes it a boundary guard rather than a restatement of the fix. After:
3 new belts pass, both suites together 62 passed / 10 skipped, no regressions.

**The vendoring payload is now TWO edits and the handoff says so.** Ruling step (2) puts the four vendored
copies on `2.0.0_SA_COO~O`'s Z-S3 worker cell, so `Z-S3_PATCH_FOR_AE_VENDORED_COPIES.md` gained a section 7
carrying this second edit beside the dtype guard, with the explicit warning that vendoring only the first
leaves this defect live.

## Blockers

**None on this seat.** What is owed is owed elsewhere, and one delivery fact matters:

**The notice to `2.0.0_SA_COO~O` and `0.7.0_AE_CloudOps~I` is QUEUED, not DELIVERED** -- neither seat is
live (per-recipient map: 0 DELIVERED / 2 QUEUED / 0 REFUSED, ids 26143/26144). "Queued if not live" is a
wish, so the item is **parked on its own carrier** rather than left in an inbox: handoff section 7 (the
payload), row `Z-S25` (the cause and the ruling), and commit `bbf8cfefa6`'s message. Owner: whichever seat
cuts the Z-S3 worker cell. Condition that un-parks it: that cell being cut.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `.tools/commit-gate.sh` | PASS 2/2 | |
| `.tools/safe-commit.sh` | `bbf8cfefa6`, 3 files | `msg-verify MATCH` |
| `python -m pytest` | 3/3, then 62 passed / 10 skipped | negative control run FIRST, against HEAD bytes restored for the purpose and then restored back by sha |
| `mcp send_message` (multi-recipient) | 0 DELIVERED / 2 QUEUED | the per-recipient map is why I know it was not delivered; a single-recipient send would have looked the same and told me nothing |

**What worked.** Using the multi-recipient result map instead of two blind sends -- it is the difference
between knowing the notice is parked and assuming it arrived. Also restoring the pre-fix bytes by sha
(`518899d306bf61de`) after the control run, rather than trusting that a `git checkout` and a `cp` round-trip
left the file where I thought.

**What failed.** Two `safe-commit` runs in this session died with a FALSE "pathspec did not match any
file(s) known to git" on paths that plainly existed. The wrapper's own comment names it: a silently-failed
`git add` under index.lock contention, which "MANUFACTURED a false one" and points the agent at their own
path. A bare retry fixed it both times, exactly as documented. Worth knowing that the error text lies about
the cause.

## Files Modified

See commit message: `bbf8cfefa6`.

| file | change |
|---|---|
| `data/assets/scripts/silver/mirror_conversion.py` | `if v == "": return None` in `_numeric_or_raise`'s string arm, with the ruling cited in-comment |
| `data/assets/scripts/silver/tests/test_etf_conversion.py` | +3 belts on the real 2026-08-29 bytes |
| `.../deliverables/0.4.0_DS_ClientPlatform~D/Z-S3_PATCH_FOR_AE_VENDORED_COPIES.md` | +section 7: the payload is two edits |

## Next Steps

1. **[whichever seat cuts the Z-S3 worker cell -- `2.0.0_SA_COO~O`]** Cut it with **both** edits in the
   payload. The notice is queued, not delivered; the payload is in handoff sections 1 and 7.
2. **[`0.7.0_AE_CloudOps~I`]** Vendor both edits into the four copies under the never-widen sign-off.
3. **[after that deploy]** Ruling step (3): re-convert 2026-08-29 and 2026-08-30, writing the 4 named
   `fact_dailynav` partitions. A literal-key write of four keys the actor controls, so NEVER-1's
   never-widen sign-off does not reach it. **Not started, and correctly so.**
4. **[Andrew]** the Black Diamond login -- still the root of the MX-s-4 / MX-s-6 chain.
