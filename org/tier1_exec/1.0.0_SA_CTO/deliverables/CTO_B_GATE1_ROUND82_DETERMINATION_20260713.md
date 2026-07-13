# Gate-1 Determination — INF Advisor-of-Record, ROUND-8.2

**Gate:** gate-1 (CTO~B, go-live principal + never-widen). **Gate-2 is CVO~B's and does NOT route through me** (Andrew-direct, LD-0277).
**Delta reviewed:** `68be1809d..dbab19e4c` — DS's 10 round-8.2 commits.
**Determination date:** 2026-07-13. **Author:** `1.0.0_SA_CTO~B`.

---

## VERDICT

**ARCHITECTURE SOUND. ROUND-8.2 CLOSES F1–F10 + C_07 + the pin/pull window. GO-LIVE REMAINS WITHHELD on TWO new findings, both CONFIRMED BY EXERCISE.**

Neither new finding is an architecture blocker. Both are **MUST-FIX-BEFORE-GO**. Both are cheap. **Harm is NOT demonstrated for either** — and I am recording that plainly rather than inflating them, because the reason to fix them is structural, not empirical:

> **A GUARD WHOSE SOUNDNESS RESTS ON A PROPERTY OF THE PRODUCER IT EXISTS NOT TO TRUST IS NOT A GUARD.**

**Nothing served. Switch OFF. SERVE-HELD. Zero live impact throughout.**

**Neither fix requires a gold run, a backfill, or any re-derivation** — they are source-only and land SERVE-HELD. **Compatible with `[STOP]` b7bce51bd.** DS must NOT run a chain to validate them; the unit suites are the oracle.

---

## 1. WHAT ROUND-8.2 CLOSED (verified at the LINE, exercised where behavioural)

Suites: **64/64 pass** (`test_aor_resolution.py`).

| # | Finding | Closed at | Evidence |
|---|---|---|---|
| **F1 / R5** | switch-gated resolver entry; rollback fails OPEN | `orion-gold-dispatch.sh:430-453` | **De-multiplexed.** Chain entry is now **presence**-gated (`_aor_script_deployed`), never on the semantic switch — and injected into **all SEVEN chain literals** (`:445-452`), not just `CHAIN_COMPUTE`. A recovery run (`--chain incremental` / `gold-*`) now carries the resolver. |
| **F1 / R1** | the artifact could not say what it came from | `aor_resolution.py:648-699` | Key = **`(source_digest, fold_mode, code_digest)`** asserted at the chokepoint `load_resolution()`. The digest IS the thing; `as_of` retained for diagnosis, correctly NOT asserted. |
| **R1b** | `as_of` could be FABRICATED as wall-clock | `orion-gold-dispatch.sh:1396` | Unresolvable as-of now leaves the pin **UNSET → fails closed**, never a fabricated today. |
| **PIN/PULL** | pin named the bytes the pull was about to overwrite | `orion-gold-dispatch.sh:977-984` | **Re-pin fires INSIDE `run_chain`, AFTER `INF_API_SILVER_ACCOUNTS_V2` succeeds** (the failure branch `return`s at `:975` first), and before the resolver. **Both** broken branches closed — the same-day-rerun RAISE *and* the silent first-run-of-day yesterday-roster read. **The fix is the ORDERING, not the guard.** |
| **F2** | A_00 loader ignored the pin → NaN advisor_key | `INF_A_00:186`, `:302` | `verify_source_partition()` called; and A_00 **RAISES** on any absent account rather than serving it. |
| **F3** | readable-but-INCOMPLETE cache trusted verbatim | `aor_resolution.py:878-935` | Completeness oracle against the event ledger — the cache is used only when **CONSISTENT**, never merely because it READ. |
| **F4** | new hard-abort in the D-chain | 4 call-sites | `expect_nonempty=True` **DECLARED** at C_02:479 / D_00d:685 / D_02c:180 / D_04:3348. My RAISE ruling held. |
| **F5** | a blip on a rebuildable write killed the nightly | `aor_resolution.py:1137-1188` | Rebuildable writes isolated → log+continue. Correctly **NOT** applied to serving inputs. |
| **F6** | run-invariant S3 GET inside 32-worker loops | `aor_resolution.py:701-704` | Memoized — and **cached only AFTER every assertion passes**, so a frame that failed its identity checks can never be handed to a later caller. |
| **F7** | the deleted coverage detector | `aor_attribution_audit.py:142-153` | `coverage_drop` **re-established**. It was removed on "the coverage axis is owned elsewhere" and **nothing owned it**. |
| **F8** | append-only + fail-on-read = a PERMANENT outage | `aor_resolution.py:906-940` | Per-key `try/except` → skip, **alert**, and mark the basis **INCOMPLETE** so the detector reports **CANNOT-EVALUATE instead of greening**. All three legs. A naive skip would have traded a loud outage for a silent miss; DS closed both directions. |
| **F9** | NULL advisor_key on unresolvable accounts | `INF_A_00:274` etc. | Floored `absent='unknown'`. **(See NEW-A — the floor is HALF-BUILT.)** |
| **F10** | census evaded by a smuggled symbol | `test_aor_resolution.py:281-365` | The census **DECLARES ITSELF INCAPABLE** for the inline-re-derivation class, in its own docstring, and ships a **negative control proving it can fail**. That is the right call: a symbol-census that LOOKS like a data-flow census is exactly how C_07 walked past. |
| **C_07** | silently UN-FOLDED the AoR on the served view | `INF_C_07:164-199` | Override deleted on **BOTH** branches — the `combine_first` **and** the unconditional else-arm assign. The **BRANCH axis** I flagged is closed. Surgical: the IWM-orphan enrichment is retained. |
| **D_04:3307** | (base-CTO's RETRACTED ruling) | `INF_D_04:3324-3352` | **The documented fallback was correctly NOT cut.** The comment even distinguishes NON-EMPTY from TOTAL (*"a map covering 3 of 400 households passes that assertion"*). The B_00 lesson held. |

---

## 2. NEW FINDING A — the absent-floor protects the field a human SEES, not the field that SILENTLY DROPS THE ROW

**`aor_resolution.py:747-756` (`attach_advisor_key`). MED. MUST-FIX-BEFORE-GO. Harm NOT demonstrated.**

`attach_advisor_key` floors **`advisor_key`** on the absent set (`df.loc[~mask, advisor_key_col] = absent`) but writes **`rep_bucket` only on `mmask`** — so an absent account keeps `rep_bucket = <NA>`.

**And `INF_09:193` filters `window['rep_bucket'] == 'individual'` BEFORE grouping. The row does not appear as a visible null. It VANISHES from per-advisor NNA.**

**EXERCISED** (positive control passed — a *present* account does inherit its bucket, so the arm measures something real):

```
absent row: advisor_key IS floored (the VISIBLE field)   -> PASS  advisor_key='unknown'
absent row: rep_bucket  IS floored (the SILENT field)    -> FAIL  rep_bucket=<NA>
absent row SURVIVES the real INF_09:193 filter           -> FAIL  30.0 of 60.0 NNA silently vanishes
```

**THE COMMENTS ASSERT A PROTECTION THE CODE DOES NOT PROVIDE.** `INF_A_01:200-202` and `INF_C_07:277-279` both justify the floor *precisely* as protection against this drop — *"a <NA> advisor_key drags rep_bucket <NA> with it, and the downstream rep_bucket filter then drops the row SILENTLY."* **It does not floor rep_bucket.** A comment is a claim with no vintage and no test.

**Why harm is not demonstrated, stated honestly:** `INF_A_00` (which runs FIRST, in `CHAIN_GOLD_A`) **RAISES** on any absent account (`:302`), and the pin + digest assertion mean the consumers and the resolver provably read the same `accounts_v2` bytes — so the absent set should be structurally empty. **A_00 is sound. It is sound because it RAISES, not because of the floor.** `INF_A_01:203` and `INF_C_07:280` floor-and-CONTINUE, with no such raise — they are protected only by a property of the producer.

**RULING:**
1. **`INF_A_01` and `INF_C_07` get A_00's RAISE.** Same class, same grain, fail-closed. **Structure beats assertion.**
2. Floor `rep_bucket` alongside `advisor_key` in `attach_advisor_key` — to an explicit non-null sentinel, **NOT `'individual'`** (that would FABRICATE attribution, adding the row to per-advisor NNA: the C_07 sin). **AN EXCLUSION SHOULD BE A DECISION, NOT AN ARTIFACT OF `NaN != 'individual'`.**
3. `apply_resolution_fold` (`:784`, `absent=None`) is the movers-only path and must stay unfloored. **Do NOT blanket-fix it** — that is the B_00 hazard, and it would wipe every non-mover.

---

## 3. NEW FINDING B — the chokepoint asserts the COLUMN and serves the ROW

**`aor_resolution.py:661 / :675 / :691`. MED. MUST-FIX-BEFORE-GO. Harm NOT demonstrated.**

All three identity assertions read:

```python
sorted({str(v) for v in pd.Series(res[col]).dropna().unique()}) != [expected]  -> RAISE
```

**`.dropna()` removes the NULL-stamped rows from the COMPARISON. It does not remove them from the FRAME, which is returned to every consumer.** So **one** correctly-stamped row vouches for **N** unstamped rows carrying attribution.

**EXERCISED** (positive control passed — a fully-stamped frame PASSES, so the harness is not comparing garbage against itself):

```
POSITIVE CONTROL: fully-stamped resolution PASSES        -> PASS
poisoned resolution (1 stamped / 3 NULL) is REFUSED      -> FAIL  RETURNED 4 rows, 3 UNSTAMPED, carrying attribution
```

This is **base-CVO's R2 finding**, landed in CLAUDE.md last night and **still live at HEAD**. Today's producer stamps the three fields as loop-invariant scalars (`:326-328`) so it *cannot* emit a NULL — which is exactly the point: **the guard's entire job is policing artifacts it did not produce.** Its own sibling says so in the same file (`verify_source_partition:186` — *"'Usually agree, never assert' is precisely the posture that produced F1"*).

**RULING:** assert the ROW — `if res[c].isna().any(): raise` for all three columns.
**And exercise the fix for OVER-condemnation before it lands:** `isna().any()` on an EMPTY frame returns `False`, and `:606` already raises on `len(res)==0`, so the zero-mover OFF path cannot be wiped. **A fail-closed fix that fires on a legitimate zero is the disease it was sent to cure.**

---

## 4. WHAT GATE-1 DOES *NOT* SAY

- It does **not** clear gate-2. That is CVO~B's, independently (LD-0277), and F1 must be exercised **THROUGH THE DISPATCH**, not resolver-direct — the instrument gap that let C_07 through.
- It does **not** authorize the switch. Release order stands: CHANGE-3 silver deploy → round-8.2(+these two) → switch ON + sentinel-lift + FE promote → **V4 served-verify on the nightly (NEVER#4)**.
- It does **not** touch the phantom advisor / `canonical_nna` class. `[STOP]` b7bce51bd binds: **nobody re-derives.** The AoR go-live and the canonical_nna deletion class are **separate**, and the AoR fixes require no re-derivation.

---

## 5. THE TRAP I WAS SENT NOT TO REPEAT, AND WHETHER I DID

MSTR: *"your v2 compensation census PASSED its positive control — it reported 'C_07 flagged' — but the line it flagged was `:411`, not the defect at `:229`. The proven-RED case must be a proven-RED LINE."*

Both new findings above are anchored on the **defect LINE** (`:747-756`; `:661/:675/:691`), each **exercised**, each with a **positive control that passed** — so neither arm is a rigged pass. **And I still nearly repeated it in a different costume:** my first glob for the AoR scripts searched `data/inflection/` and returned **ZERO**. The real tree is `data/inf/`. A zero is the one result a pattern produces for reasons that have nothing to do with the estate. **I opened the commits instead of believing the zero.**

---

*Gate-1: SOUND, WITHHELD on §2 and §3. Nothing served; switch OFF; SERVE-HELD.*

---

# ADDENDUM — GATE-1 **CLEARED** at `59d70b95e` (2026-07-13)

Both withholds are closed. **141/141** on my own run, my own denominator.

**A** — `attach_advisor_key` floors **both** fields atomically. `rep_bucket` gets an explicit named bucket (`UNRESOLVED_REP_BUCKET='unresolved'`), so **the exclusion is a DECISION, not an artifact of `NaN != 'individual'`**. The row is **excluded from per-advisor rollups** (an unattributable row must never be served as an advisor's) but **REMAINS in the firm total** — so `sum(advisors) < firm_total` is **VISIBLE** rather than silently absorbed. Loud alarm naming accounts; hard RAISE on the incoherent shape (non-null `advisor_key` + null `rep_bucket`). **`apply_resolution_fold` still passes `absent=None`** — the movers-only landmine stays **unarmed**, pinned by test.

**B** — the **row-level assertion is FIRST** (`:671-699`), before the column comparisons (`:718+`). **The ordering IS the fix**: the column checks would PASS on a poisoned frame and the row check would never be reached. Over-condemnation exercised: `.isna().any()` on an EMPTY frame is False, so the legitimate **zero-mover OFF path still PASSES**.

## >> AND MY OWN FALSIFIER ASSERTED THE DEFECT. RECORDED, BECAUSE IT IS THE LESSON. <<

Re-running my morning falsifier against the fix, **arm A FAILED — and the failing assertion was MINE and it was WRONG**:

> *"the absent row SURVIVES the `INF_09:193` rep_bucket filter"*

**That demands an UNATTRIBUTABLE row be counted into a named advisor's NNA. It demands FABRICATED ATTRIBUTION** — the phantom-advisor sin in reverse. DS refused it explicitly (*"I am not fixing a silent drop by committing the phantom sin in reverse"*) and he was right.

**A TEST THAT ASSERTS THE DEFECT WILL DEFEND IT.** I had conflated *"the row must not silently vanish"* with *"the row must be counted as an advisor's."* **Only the first is true.** The property that matters is **DISCLOSURE, not INCLUSION**:

```
firm total 60.0 · sum over per-advisor 30.0 · VISIBLE RESIDUAL 30.0   <- disclosed, reconcilable
```

*Disclose the residual; never suppress it; never guess it.* **Three of us wrote a test that defended the bug it was written to catch today** (CVO~B's F2 arm encoding `absent=None`; her phantom arm rewarding the forbidden fix; this). It is not coincidence — **it is what happens when you write the assertion from the SHAPE OF THE DEFECT instead of from the PROPERTY YOU WANT.**

**And DS's dtype finding is the one none of the three gates saw:** `df[df['rep_bucket'] != 'routing']` **KEEPS** a `<NA>` row under `object` dtype and **DROPS** it under `string` dtype. **The fate of an unresolved row depended on a dtype nobody pinned.** Flooring makes it deterministic. He found it by measuring, not reasoning.

## WHAT GATE-1 CLEARING DOES *NOT* DO

- It does **not** clear gate-2 (CVO~B, independent, LD-0277). Her V4 served-verify is **NOT RUN — an EXPLICIT GAP, never a PASS** — and it is now structurally blocked: the dispatch is **held at the chokepoint**, so the nightly cannot run. **AoR go-live is serialized behind the hold-lift.**
- It does **not** authorize the switch. `AOR_FOLD_ACTIVE` stays **OFF**. The deploy it unblocks is **DELTA-0**.
- **The lift is gated on the coverage assertion — never on this gate, and never on any project's release being ready.** *"Lift it just for the V4"* is the most likely way the hold is defeated. It will not arrive looking like a destructive act; it will arrive looking like the last box on a form.

*Gate-1: CLEARED. Nothing served; switch OFF; the chain is held and verified held.*
