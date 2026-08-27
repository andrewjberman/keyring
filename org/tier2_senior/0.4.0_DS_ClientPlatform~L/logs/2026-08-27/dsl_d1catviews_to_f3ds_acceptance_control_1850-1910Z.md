# Session — `0.4.0_DS_ClientPlatform~L` — D1_CATVIEWS TO-F3-DS ACCEPTANCE CONTROL

**Serial:** `0.4.0_DS_ClientPlatform~L` (site Z, lane inbox `org/mcp/inbox/0.4.0_DS_ClientPlatform/~L/`)
**Window:** 2026-08-27 ~18:50Z – ~19:10Z
**Project:** `D1_CATVIEWS` ONLY (Rule 27). Spawned by `0.0.0_AB_MSTR~Z` msg 9634; lane ruled by
`1.0.0_SA_CTO~Z`, seated by `2.0.0_SA_COO~Z` — **and the TO-record half of that seating is absent;
see Blockers.**
**Archetype:** ACCEPTANCE CONTROL (independent second seat) + one REACHABILITY observation.

---

## Objective

Author the acceptance control for `D1_CATVIEWS.TO-F3-DS`, which `0.4.0_DS_ClientPlatform~Z` built and
proved @`3e88e10511` and correctly refused to accept themselves. The TO and `mdpf_category_registry.py:992`
(COO ruling 72258 s.3(d)) both require that the repair seat not author the control. `0.0.0_AB_MSTR~Z`
named the failure mode to avoid in the spawn: **a second seat confirming via the FIRST seat's method is
repetition, not corroboration** — so the deliverable is not "agreement", it is *a different instrument,
named, with the difference exhibited*.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `to-check.py` | `--all --assignee '0.4.0_DS_ClientPlatform~L'` | RUN, rc=0. **`total=0 projects=0 scanned=2132 unresolved_serials=0`.** This is the instrument that MEASURED the seating gap in Blockers — and `unresolved_serials=0` is the load-bearing field: it discriminates a genuine absence from the known `SEATED:`-prose notation defect. |
| `.tools/commit-gate.sh` | on `crosswalk_keyspace_import_control.py` | RUN, rc=0. py_compile + ds-precommit + ruff py39 clean over 1 file; "no unguarded strict-utf8 log reads". |
| `comp-pulse diff` (risk reflex, via `safe-commit.sh`) | `diff <2 paths>` days=7 top=8 | RUN, **REFLEX CLEAN as a MEASURED result**. DENOMINATOR: 2 files against 1351 danger nodes; danger map 18.9h old — the vintage the verdict is scoped to. |
| `.tools/safe-commit.sh` | `--author … -F <msgfile> -- <2 paths>` | RUN, rc=0 → `ac6fd85dbb`. `[msg-verify] MATCH len=5633`. |
| `ruff` / `py_compile` | run **directly**, not through the gate wrapper | rc=0 / "All checks passed!". Deliberately decomposed — see F3-4. |

## Work Completed

### 1. The control — `data/mdpf/scripts/gold/tests/crosswalk_keyspace_import_control.py`

Nine arms across three planes, `rc=0`, **9 of 9 behaved as predicted**. Subject materialised from an
immutable commit-ish and sha256-verified before any arm runs (`git archive --format=tar <PIN>` as the
recorded BUILDER; `git show <PIN>:<path>` as the content oracle) — the TO's "pin the CONTENTS *and* the
BUILDER".

### 2. The instrument, and the arm that proves it differs

| | Author `~Z` | This seat |
|---|---|---|
| subject | working tree | tree materialised from `3e88e10511`, sha256-verified |
| plane | in-process | out-of-process, fresh subprocess per arm |
| domain | the **function** (`_check_crosswalk_keyspace(<hand-built list>)`) | the **wiring** (`:613` over the real `MEMBERS`) |

**B1 ⊕ B2 exhibits it rather than asserting it.** Delete the one import-time call at `:613`, keep the
bad member: my `import` goes **clean** (rc=0); the author's AC1 command, run **verbatim**, still
**raises** (rc=1). Their command calls the function directly, so the call site is invisible to it.
**All four of their PASS rows are invariant to whether the guard is wired.** The wiring *is* present —
measured at `:613`, column 1, module scope — so this describes what their evidence is evidence *of*,
not a contradiction of their result.

### 3. Which arms move across the repair (B3)

Applied the `:992` control's own lesson. Against pre-repair parent `d37e12809a`: **A1 (import clean)
and A3 (SMA resolve) are GREEN**, so neither can evidence that this repair landed; the author's AC1
gives `AttributeError`. **Only A2 and B1 move.** The landed-vs-unlanded verdict rests on those two.

### 4. The four criteria

- **F3-1 PASS** (A2) — specimen bound into `MEMBERS` at module scope, subprocess `import` → rc=1,
  refusal **localised** to `"ABSENT from the crosswalk canonical keyspace"` and naming
  `opal_conservative_growth`, not merely "something raised".
- **F3-2 PASS** (A1) — rc=0. **9 model-class members of 15 registered; keyspace 11 model_keys; 0
  outside.** The guard runs at import, so a clean import *is* the negative arm.
- **F3-3 PASS** (A3) — `opal_div_sma -> divz`, `opal_growth_sma -> pfoe`; 2 of 2 map rows.
- **F3-4 PASS, and declared a re-run** — self_test rc=0 (captured before any pipe), 0 `^FAIL` lines,
  1950 bytes, py_compile rc=0, ruff py39 clean, two runs byte-identical. Run on the pin with the gate
  decomposed, **but that is thinner independence than Planes A/B and I did not dress it up.**

## Decisions Made

1. **Score the IMPORT, not the function.** F3-1 says "RAISES at import"; the only way to measure that
   clause is to mutate the module and let the import fail. Chose out-of-process so no arm shares an
   interpreter with an already-imported module.
2. **Mutators fail closed and loud.** Anchor not found exactly N times → `SystemExit`, because an arm
   whose mutation silently no-ops tests nothing while printing green.
3. **Did not edit the TO to seat myself.** Surfaced instead. `<issued_to>` is the issuer's field.
4. **Did not widen scope** to the `off_crosswalk` axis, the three existing raises, or the build pin —
   all named out of scope, and I agree with the cut.
5. **Recorded the reachability observation as OBSERVATION / INERT rather than a defect.** The guard is
   correct, correctly placed, and correctly wired; what I measured is what it is evidence *of*.

## Files Modified

| Path | Change |
|---|---|
| `data/mdpf/scripts/gold/tests/crosswalk_keyspace_import_control.py` | NEW — the control, 9 arms |
| `org/tier2_senior/0.4.0_DS_ClientPlatform~L/deliverables/D1_CATVIEWS.TO-F3-DS_ACCEPTANCE_CONTROL_20260827.md` | NEW — the acceptance record |

Commit `ac6fd85dbb`, 2 files, 575 insertions. **No file authored by `~Z` was touched.**

## Briefs Written

`D1_CATVIEWS.TO-F3-DS_ACCEPTANCE_CONTROL_20260827.md` — the acceptance verdict, the instrument
declaration, the F3-4 honesty clause, the reachability observation, and the seating gap.

## Blockers

**One, not mine to clear, and it did not block the work.** `1.0.0_SA_CTO~Z` named it and
`0.0.0_AB_MSTR~Z` relayed it in msg 9634: this lane must be seated in the **TO record**, not only in a
spawn message.

```
to-check.py --all --assignee '0.4.0_DS_ClientPlatform~L'
  total=0  projects=0  scanned=2132  unresolved_serials=0
TO-F3-DS:7   <issued_to>0.4.0_DS_ClientPlatform~Z</issued_to>
```

**`unresolved_serials=0` discriminates:** this is a genuine absence, *not* the known `SEATED:`-prose
notation defect that makes lane seats read zero while holding live work. The TO names the control
**role** but no serial. I executed rather than blocking, and did not work around it by editing the TO —
**that write is `2.0.0_SA_COO~Z`'s act.** My read: `<issued_to>` should keep naming `~Z` as build
assignee; what is missing is a record of the control seat, and its shape is the issuer's call.

## Current State

**TO-F3-DS is ACCEPTED on F3-1/F3-2/F3-3 by an independent instrument, and on F3-4 by an admittedly
near-duplicate one.** Delivered to `2.0.0_SA_COO~Z` (msg 9692) cc `1.0.0_SA_CTO~Z` (9693),
`3.0.0_SA_CVO~Z` (9694), `0.0.0_AB_MSTR~Z` (9695) — **4 DELIVERED / 0 QUEUED / 0 REFUSED, denominator 4.**

**Push state, measured and perishable:** `ac6fd85dbb` **LOCAL**, read `2026-08-27T19:08:39Z` against
`origin/SITEZ=53944935b3de2265b084b7e6acd0e6329df06590`, negative control fires (NOT on `origin/CLOUD`).
`0.0.0_AB_MSTR~Z` integrates; this seat does not push.

⚠ **My own earlier push-state claim aged inside 35 minutes and I caught it only because I re-read.**
At 18:56:01Z `origin/SITEZ` was `2098e27abe`; at 19:08:08Z it was `53944935b3`. The four build commits
re-read ON ORIGIN against the new ref. **This is the exact decay msg 9634 warned about, observed on my
own claim rather than someone else's.**

⚠ **And a control-design error I made and corrected in-session, recorded because it is the class this
whole deliverable is about:** my first push-state negative control asked whether `2098e27abe` was an
ancestor of `ac6fd85dbb`. It **is**, by construction — my commit sits on top of it — so that control
**could not fail**. It printed "did NOT fire (unexpected)" and I replaced it with `ac6fd85dbb` vs
`origin/CLOUD`, which fires. *A control that cannot fail is not a control, and I wrote one in the same
session in which I certified someone else's control design.*

Nothing is held by me and nothing is owed to me.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Close TO-F3-DS, or return REWORK against named evidence. The seating write is
   also theirs.
2. **[`0.0.0_AB_MSTR~Z`]** Push `ac6fd85dbb` when integrating.
3. **[`3.0.0_SA_CVO~Z`]** The reachability OBSERVATION below, if the channel wants it carried further.

## Surprise-channel items — OBSERVATION / INERT, filed to `3.0.0_SA_CVO~Z` cc `2.0.0_SA_COO~Z`

**The guard's `raise` is unreachable over the real `MEMBERS` at this pin — and this is not a defect.**
`_model_members()`:279 **derives** every model-class `member_id` from `e.model_key`, and the guard then
tests that value against the set it was drawn from. Measured three ways:

- **C1** `{model-class member_ids} == {cohort_class=='model' model_keys}` → **True**, 0 unmatched each way.
- **C3** `asset_category="models"` set at **exactly 1 site of 2** `asset_category=` assignments;
  `ALTERNATIVE/INSURANCE/CLIENT_MEMBERS` all empty tuples.
- **C2** rename a crosswalk `model_key` → the registered member **silently renames with it**, still 9,
  guard silent. **The guard cannot detect drift: drift needs two independent sources and there is one.**

So the invariant held 9/9 **by construction**, not by convention. The TO's premise *"enforced by
NOTHING"* is exactly right about **enforcement**; the reason it was true is **derivation**. That
**relocates** the risk rather than reducing it: the `opal_conservative_growth` specimen cannot be
registered by any code path in this module today, and becomes registrable the moment `_model_members()`
stops deriving. **The guard is a tripwire on a door that is currently welded shut — and it is on the
right door.** Placing it before the hazard is the correct order; the alternative is the "first violation
is also the first test" failure the TO exists to end. Recorded as what the guard is evidence of; **no
widening proposed and no action taken.**
