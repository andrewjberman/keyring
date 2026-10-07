# The CIX recency limb is ported into the tzero tripwire and proved against its own parent commit — built on a branch, deliberately not deployed — 0.7.0_AE_CloudOps~RV

**archetype:** MIXED (IMPLEMENT + VALIDATE)

**Date:** 2026-10-07
**Task Order:** `OPAL_BBGTML.TO-GUARD-4.tzero-tripwire-cix-recency-port` (`<risk>WORLD</risk>`)
**Status:** COMPLETE as the order defines it — built, proved and committed on a branch. **NOT MERGED**, which is the order's instruction, not an unfinished step.

---

## Objective

Close the hand-run half of gap 2 that my own row `OPAL_BBGTML-Z-S12` found in the previous
segment: `publish_to_portal.py:64` runs the **tzero** copy of the tripwire as the send gate, and
that copy lacked the per-series custom-CIX recency limb GUARD-3b put in the tplus1 copy. The CTO
ruled the smallest of the three routes my row offered (ADDENDUM 7 @`58e472b0b6`): port the limb,
nothing else.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `comp-read <tzero> --enumerate 'maxd\s*=\|rd_dates\s*=\|asof_ok\|expected_asof'` and the same on tplus1 | PASS | **This settled the order's STOP condition.** Banded output put tzero `:133-134` beside tplus1 `:212` and showed `asof_ok` is only consumed at the `maxd not in asof_ok` line — which is what distinguishes "resolves a different as-of" (stop) from "accepts a different set" (proceed). A plain grep would have returned the same lines without the CODE/DEF banding that made the consumption site obvious. |
| comp-read | `comp-read <tplus1> --for "exact line bounds of grade_cix_series and _check_cix_recency and the CIX_PREFIX constant"` | PASS | Gave the python-ast section map (`118-165`, `168-190`, `61-65`) that the extraction script sliced on. Extracting on measured bounds is why the ported limb came out byte-identical on the first run. |
| comp-read | `comp-read .tools/msys_argv_guard.py --for "how do I call msys_safe_run..."` | PASS | Surfaced the `msys_safe_run(cmd: list, **kwargs)` signature for the `git show` in the proof — the sanctioned route for a Python-spawned MSYS binary with a `<ref>:<path>` argument. |
| comp-which | — | SKIPPED | Non-application stated: no search was needed this segment. Every file, line bound and commit was already in hand from the GUARD-3 segment. |
| comp-pipescript / comp-iam / comp-blast / comp-estate | — | SKIPPED | Same non-application as the previous segment, and stated rather than skipped silently: no gold run, no `iam.tf`, no infra, no S3 code prefix. This cell edits one local Python file and deploys nothing at all. |

**What worked:** `comp-read --enumerate` turned the session's one genuine stop-or-go judgment into a
two-file line comparison instead of an argument. `comp-read --for`'s AST bounds made byte-identical
extraction possible.

**What failed:** nothing.

**Gap found:** none.

---

## Work Completed

### 1. The STOP condition, checked before any edit

The order's item 3 said to stop, file a row and report if the tzero copy resolves a different
as-of than the tplus1 copy grades against. **It does not, and the distinction is the substance of
this segment:**

```
tzero  :133-134   rd_dates = pd.to_datetime(rd["date"]) ; maxd = rd_dates.max().date()
tplus1 :212       maxd = pd.to_datetime(rd["date"]).max().date()
```

Same expression, same frame, same value — and the limb grades against `maxd`. What *does* differ is
`expected_asof()` (tzero expects the RUN DAY, tplus1 run day − 1 BDay), but that only builds the
ACCEPTANCE SET tested at `tzero :153` / `tplus1 :213`. A different check, untouched here. So:
proceed, no row.

### 2. The port, extracted not retyped

A one-shot script sliced the three pieces out of the merged tplus1 file on the AST bounds and
inserted them at tzero's own insertion points. An AST diff then **measured** the identity:
`CIX_PREFIX` (1 line), `grade_cix_series` (48), `_check_cix_recency` (23) — **all three
byte-identical**, and the call statement identical too (`tplus1 :221`, `tzero :245`). The only
textual difference is the 6-line call-site comment, which records the §1 distinction so the next
reader of this copy need not re-derive it.

### 3. The proof, five arms

`GUARD-4: PASS` exit 0. C1 the frozen pull → FAIL naming 7 of 13 at 2026-09-29 with the denominator
printed; C2 the re-pull → PASS 13/13; C3 SPX unaffected; C4 the negative control; C5 the arm that
closed row Z-S12's last open claim. Detail in
`deliverables/TO_GUARD_4_REPORT_TZERO_PORT_20261007.md`.

**C4 needed a control on its own control.** The arm requires the parent-commit copy to read PASS on
the frozen pull — but a mangled `git show` returns CLEAN-EMPTY on this device, and an empty module
would *also* read PASS, manufacturing precisely the result the arm wants to see. So the retrieved
bytes' git blob hash is asserted equal to `f4ee4cae0d…`, measured before the edit, before the module
is loaded.

**C5 closed a claim I had left open in my own row.** Z-S12 stated plainly that it had only *read*
tzero's existing as-of-scoped presence check and not exercised it. Exercised now: on the frozen pull
that check prints `all 5 model portfolios have a bar ON the as-of 2026-10-05` — it **passes** —
while 7 benchmark/ETF series are frozen, none of which is in `MODEL_INDEX_NAMES`. So it structurally
cannot see them, and the port is not redundant with it.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Extract the limb text from tplus1 rather than retype it | The order says "the same function body". This file has already diverged twice (the tzero/tplus1 split, and the presence check only one copy has); retyping is the mechanism of that divergence. Extraction also made the "which lines differ" report answer a measurement instead of a claim. |
| Proceed past item 3's STOP | The limb grades `maxd`, which both copies compute identically. `expected_asof()` differs but feeds only the acceptance set. Recorded in the cell commit so the reasoning is reviewable even if the report is not read. |
| Do NOT add the new bullet to the tzero module docstring | Item 2 says nothing else in the file changes. Named as a deliberate non-change in the report and offered as a one-line amendment, so it cannot be mistaken for an oversight. The consequence — tzero's docstring does not list this check — is stated rather than left for a reader to notice. |
| No surprise row this segment | The one thing that would have warranted one (a differing as-of) resolved to proceed on measurement. Filing a row anyway would be noise. |
| No NEVER-2 entry | Correct and deliberate: no deploy is being made. On site Z a NEVER-2 entry marks a working-tree edit going live; a branch in a linked worktree does not touch the shared working tree. Opening one would misrepresent a build as a deploy. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `integrations/bloomberg/pipeline/tzero/tools/bbg_pkl_tripwire.py` | the ported CIX recency limb, +87 lines, 238 → 325 | Yes — `d328b0d5fe` **on branch `rv-bbgtml-guard4` only** |
| `.../deliverables/guard4_tzero_tripwire_proof.py` | AC1 proof, 5 arms | Yes — `3b65362444` (branch) |
| `.../deliverables/TO_GUARD_4_REPORT_TZERO_PORT_20261007.md` | the order's single report | Yes — `3b65362444` (branch) |

**Nothing in the shared tree changed this segment.** Verified four ways: the shared tzero blob is
still the parent `f4ee4cae0d5707b26e46b3a5c535f5c9fc23d25a`; `rv-bbgtml-guard4` is not an ancestor
of CLOUD HEAD; the shared copy contains 0 occurrences of `grade_cix_series`; and
`git status --porcelain -- integrations/bloomberg/` is empty.

**Push state, MEASURED:** **LOCAL @`e9e43448dc`** — `git ls-remote origin CLOUD` read
`690206fc56` at 10:30Z. The branch is local-only and unpushed by design.

---

## Blockers

**None owed by this seat on this order.** The merge is not a blocker on me — it is Andrew's word,
which the CTO has put to him, and the order explicitly excludes the landing.

---

## Current State

Branch `rv-bbgtml-guard4` in worktree `C:/tmp/rv-guard4` (HEAD `3b65362444`) carries the tzero
tripwire with the per-series CIX limb byte-identical to the live tplus1 one, proved `GUARD-4: PASS`
exit 0 against both real pulls plus a parent-commit negative control. **Both are deliberately left
in place and the shared tree is untouched**, so the hand-run send path is still uncovered and
ADDENDUM 7's reading discipline is what covers it: nobody hand-runs `publish_to_portal.py` without
first running the **tplus1** tripwire on the same files and reading its exit code. The report is
delivered to `2.0.0_SA_COO~Z` (10:17:56Z).

---

## Next Steps

1. **[this seat] TO-GUARD-3 report 2** — the 11:00Z vehicle and 11:30Z checker live reads, then V1
   closed and the NEVER-2 ledger CLOSED. This is the only thing still owed by me today. A waiter is
   armed on both logs. If the 11:00Z fire repeats yesterday's DAPI failure (row `Z-S11`,
   `LastTaskResult 267014`), the tripwire arm is **NOT RUN**, never PASS.
2. **[Andrew, via `1.0.0_SA_CTO~Z`] The word that lets the tzero port merge** — until then the
   branch waits where section "Current State" names it.
3. **[`2.0.0_SA_COO~Z`] Flip `<status>` on TO-GUARD-4, and disposition `OPAL_BBGTML-Z-S12`** — its
   last unmeasured claim is now measured by proof arm C5.
4. **[`2.0.0_SA_COO~Z`, optional] The tzero docstring bullet** — one line, named in the report as a
   deliberate non-change; I did not take it unasked.
