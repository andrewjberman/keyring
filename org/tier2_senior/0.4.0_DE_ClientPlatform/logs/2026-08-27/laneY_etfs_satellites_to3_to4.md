# 0.4.0_DE_ClientPlatform~Y -- ETFS_SATELLITES TO-3 then TO-4 (D4, site Z)

**Date:** 2026-08-27 · **Serial:** `0.4.0_DE_ClientPlatform~Y` · **Archetype:** BUILD
**Project:** `ETFS_SATELLITES` (D4) -- ONE project, Rule 27 · **Session:** launch -> TO-3 + TO-4 delivered

---

## Mandate

ANDREW-DIRECT D4 via `0.0.0_AB_MSTR~Z` (msg 9353): DE lane for ETFS_SATELLITES ONLY. **TO-3 then
TO-4. DO NOT COLLAPSE THEM.** The named hazard: a mode axis shipped without its firm gate renders
the satellites pill for EVERY FIRM -- a client-facing multi-tenant exposure that ships green
(typecheck passes, build passes, panel renders, and the defect is *who can see it*).

**Held the split.** Two TOs, separate commits, gate second. `1.0.0_SA_CTO~Z` independently verified
mid-build that all three `modesFor` occurrences in `portal/src` were comments naming TO-4 -- zero
implementation (msg 20260827T180557Z).

---

## Delivered

| # | commit | what |
|---|---|---|
| 1 | portal `7ebe38b0` | **TO-3** -- the `satellites` mode axis + panels. 9 files, +1378/-35. |
| 2 | workspace `1c601792ba` | TO-3 proof-of-spec, `rc=0 VALID`. |
| 3 | portal `705bb9df` | TO-3 addendum -- COO's SAT-a-4 ruling pinned into the registry seam. |
| 4 | portal `375bbc9a` | TO-3 fix -- the exercise's pre-change rev. See "What went wrong". |
| 5 | portal `797c4f8d` | **TO-4** -- the firm gate, `modesFor(firm)`. 4 files, +428/-9. |
| 6 | workspace `ae79205cb6` | TO-4 proof-of-spec, `rc=0 VALID` + this log. |
| 7 | portal `685cca05` | POST-ACCEPTANCE FIX: 23 non-ASCII chars I introduced + the expiring-baseline defect recurring. |
| 8 | portal `f74a8a13` | POST-ACCEPTANCE FIX: `getPositioningData`'s "No auth required" comment, FALSE at the served plane. 1 of 47 occurrences measured; the other 46 explicitly NOT cleared. |

**Push state, re-measured 20260827T191413Z (is-ancestor vs `ls-remote`; NEG-CTL vs `origin/PROD` =
NO, so the oracle discriminates): ALL EIGHT COMMITS ON ORIGIN.** portal @`origin/DEV f74a8a13`,
unpushed=0; workspace @`origin/SITEZ 86607cde`. ⚠ **This claim is PERISHABLE and ages the moment the
integrator runs** -- an earlier line in this log read LOCAL and was correct when written, then
expired inside 90 seconds. `0.0.0_AB_MSTR~Z` is the integrator and pushes. Portal main worktree on
**DEV** throughout (Rule 19, `branch --show-current`).

---

## The finding: the TO's EIGHT mode-keyed sites were NINE of TWENTY

TO-3 §1 had already corrected cell `SAT-b-1` from SIX sites to EIGHT, and stated the lesson --
*"an oracle checking six cannot see a seventh site missed."* Re-derived against my own tree the
count is **20**: 9 declaration-layer, 11 consumer-layer, **15 SILENT** before this change.

> **ALL EIGHT OF THE TO'S SITES ARE IN `bookSet.ts` + `gridConfig.ts`. NOT ONE IS IN A CONSUMER.**

`Positioning.tsx`, `PositioningSummary.tsx` and `HoldingsTab.tsx` each carried independent
`mode === 'etfs'` branches binding `'satellites'` to the MODELS arm. Sharpest: `Positioning.tsx:99`
`const isEtfs = mode === 'etfs'` -- a two-valued boolean over a three-valued axis, fanning out to
**seven** consumption points from one line.

**Three were not merely missing but actively wrong:**

- `capabilitiesFor` -- the ternary gave any new mode the MODELS branch = **all four TRUE**, against
  `SAT-d-3` declaring all FALSE. *A cell contradicted by a default is not a cell.*
- `subCategoryHoldings` + `hasSubCategorySource` -- the attribution feed is models-only and
  model-keyed, so satellites missed on every book and **Asset Sub-Categories rendered EMPTY while
  `hasSubCategorySource` read TRUE** -- the panel's own placeholder never fired.
- the header trigger -- satellites rendered plain text *only because* `hasModelKeyNotes()` returns
  false for a non-model code. Right output, wrong reason, one key collision from opening a MODEL's
  notes from a SATELLITE's header.

**Fix is a mechanism, not a patch:** every mode-keyed decision is now a `Record<PositioningMode, X>`
so the compiler *asks*; `POSITIONING_MODES` is derived from `MODE_LABELS`' keys, which retires the
array-literal hazard rather than exercising it. CTO recorded that as better than the criterion asked
for and did not ask for their version back.

**Design:** `satelliteAdapter.ts` synthesises a satellite-keyed payload from the already-served
models payload -- build-ladder rung 2, the rung `etfAdapter.ts` stands on. The panels are untouched
on the models and ETFS paths, which makes `SAT-inv-4` true by construction rather than by test.

**Membership is NOT declared in the portal.** The nine members are TO-2's deliverable (DS lane) and
that TO is the primary carrier; a second copy here would diverge from minute one, and a hand-copied
list cannot carry the IS-A vs HOLDS-A rule that keeps it correct. `SATELLITE_REGISTRY` ships EMPTY
with a **declared** pending state that renders a stated notice.

---

## TO-4: `null` is not a firm

The decomp read *"Cottonwood + Opal see three pills; every other firm sees two."* CVO's F2 record
caught the uncovered member before a line was written: `AuthContext.tsx:354` sets `firmId: null`
when `/auth/me` FAILS -- an authenticated session whose firm is UNKNOWN, not absent.

`modesFor` is TOTAL over `firms ∪ {null}`, and **null fails CLOSED** to the two-pill set, mirroring
`isPathAllowedForFirm`'s `?? false`. Failing open would make *"break /auth/me"* the way to see
another firm's mode.

**The tamper arm is the load-bearing control.** `usePersistentToggle` validates every read against
the allowed set it is *given*, and `Positioning.tsx` gives it `visibleModes` -- so a denied viewer
hand-editing sessionStorage to `'satellites'` has it rejected and the key cleared. Passing the
DECLARED set there would have hidden the pill and left the mode reachable: a gate with a hole
behind it. **The wiring is asserted, not assumed.**

**CTO's amendment (18:19Z), surfaced UP by DS~W:** the bronze artifact carries
`hierarchy.firmId = 4175` -- the MODEL's owning firm, the same constant on all nine, so a gate on it
gates nothing or everything and typechecks cleanly. This gate reads the auth plane only; a leg
sweeps all six satellites-path files for a `hierarchy` access in CODE (comments excluded on purpose
-- the code NAMES the trap): **0 hits over 6 files**.

**Rendered, both arms:** `firmId=49financial` -> MODELS | ETFS. `firmId=cottonwood` -> MODELS |
ETFS | SATELLITES.

---

## What went wrong, and what it cost

1. **My own TO-3 commit broke my own TO-3 evidence script.** The exercise resolved its pre-change
   modules from `SAT_BEFORE_REV || 'HEAD'` -- correct exactly while uncommitted, wrong the instant
   `7ebe38b0` landed, because HEAD then *contains* the change. It died at import rather than going
   green off a self-comparison, but that was luck of the import graph, not design. **A default that
   is right only until your own commit lands is a control with an expiry date on it.** Fixed at
   `375bbc9a` by resolving the rev from the repository. Found by re-running the older exercise as a
   regression check while building TO-4 -- nothing else would have reported it.
2. **Two of my own controls did not discriminate on first run**, and both were fixed at the SOURCE
   rather than at the assertion: `ARTIFACT_KEYS_ARE_BOOKS` was a guard no mode could ever trip (a
   guard that cannot fire is not a guard -- REMOVED, the real protection named in a comment), and
   the `portfolioNamesFor` control compared a value to itself (re-pointed at `'LT'`, which the
   models alias map actually renames).
3. **I ACKed broker id `9354` from a GUESSED id.** The CTO message file carries no Msg-ID line and I
   inferred "next after 9353". The broker refused it (already ACKed) so no true recipient's
   write-once slot was consumed -- but guessing an id can forge the one delivery signal an orphan
   cannot forge. Recorded against my own lane.
4. **A copy defect a grep could not see:** the page description rendered `Opal Satellites -- each a
   weighted blend`, where this codebase's ASCII stand-in for an em-dash in *comments* reads as two
   stray hyphens in *page copy*. Caught by reading the screenshot; reworded.
5. **A stale normative line.** After wiring the gate, the comment above the toggle still said
   `POSITIONING_MODES is the allowed set` -- true of the mechanism, false about the value. Fixed the
   line, then read the line.
6. **I skipped XXX.md Step 1b A.2 at load** (ran A.1, A.3, B, C; not the audit-archive-invoker).
   **The step is non-blocking by design, so skipping it is SILENT** -- nothing failed, nothing
   flagged it, and I would have gone the whole session without noticing had `0.0.0_AB_MSTR~Z` not
   broadcast an edit to that exact step at 19:19Z. Run late; findings are the expected benign class.
   **A mandated step whose omission produces no signal is one an agent can believe it performed.**
7. **I introduced 23 non-ASCII characters** against CLAUDE.md's ASCII rule -- into two files that
   were at ZERO, and into three I authored that each carry the line *"No non-ASCII in this file"*.
   **A file asserting its own compliance is what stops the next reader checking.** Fixed @`685cca05`,
   bounded to what I caused (the pre-existing 17 lines in three other files measured identical to
   baseline and left untouched, so the diff still shows which were mine).
8. ⛔ **I SHIPPED THE EXPIRING-BASELINE DEFECT A SECOND TIME, IN THE FILE I WROTE TO FIX THE FIRST.**
   TO-4's AC5 leg read `git diff HEAD` -- "TO-4's diff" only while TO-4 was uncommitted. Same class
   as #1, committed an hour after I banked the lesson from it. **Knowing it did not transfer to the
   next instance; only resolving the ref from the repository does.** `0.0.0_AB_MSTR~Z` places it
   with their own ceiling defect and CTO's cause-keyed guard: **three seats, three surfaces, one
   shape -- a control pinned to a value the fix itself moves.**

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `tsc -b` | `./node_modules/.bin/tsc -b --force` | rc=0 throughout. Never bare `tsc --noEmit` (root tsconfig is `files:[]` + references, so the bare form compiles an empty set). **Insufficient by design** -- all 15 silent sites compiled clean while returning the models answer. |
| `eslint` | changed tree + both exercise scripts | rc=0, zero findings. |
| `satellites-mode-axis-exercise.mjs` | `bun --tsconfig-override=tsconfig.app.json ...` | **30/30**, each silent leg paired with a pre-change control REQUIRED to fail. |
| `satellites-firm-gate-exercise.mjs` | same | **24/24**, every allow-leg paired with a deny-leg; tamper exercised; gate shown able to discriminate. One leg failed first run and was RIGHT to. |
| `/frontend-dev` ui-smoke | `node scripts/ui-smoke.mjs positioning ... [--firm X] [--fixtures f.json]` | 6 screenshots READ. Found the copy defect; confirmed capability ABSENCE and both gate arms. |
| DOM text dump | one-off playwright read | The Yield row was CLIPPED by the panel's sticky footer -- read as a VALUE (3 / 3.40) rather than inferred from a partial glyph. |
| `comp-transform ternary-audit` | `Positioning`, `PositioningSummary`, `bookSet` | ⛔ **MEASURED NOTHING.** "No string-literal union types found in file or types.ts" -- `PositioningMode` lives in `shared/bookSet.ts`, outside its file+types.ts scope; `bookSet` is not a component. A scoped instrument returning a silent clean for a plane outside its scope. **Reported, not counted as a pass.** |
| `comp-blast` | `comp-blast capabilitiesFor` | NOT-FOUND over a printed 20,779-node denominator; the tool itself says this is not a "nothing breaks" clear. Auto-Rule 6 discharged by a direct census of the two call sites. |
| `proof-of-spec-check.py` | TO-3 and TO-4 instances, rc read without a pipe | Both `rc=0 VALID`. TO-3 first run returned `rc=2 TOOL-ERROR` (not a verdict) -- `controls.mutant` was a string where the schema wants an object. |
| `safe-commit.sh` | per-invocation `GIT_COMMITTER_*`, `-F <msgfile>` | 8 commits, all msg-verify MATCH. First portal attempt refused `rc=128` (unknown committer identity in the shared checkout); nothing left staged. The risk-reflex HOLD on `HoldingsTab.tsx` was READ before proceeding. |
| `audit-archive-invoker.py` (XXX.md A.2) | `python .tools/audit-archive-invoker.py` | ⚠ **SKIPPED AT MY LOAD, run late at 19:20Z.** 18 findings, baseline 2026-08-20T042433Z, snapshot=not-due. **EXPECTED on this device and NOT chased** — `1.0.0_SA_CTO~Z` closed it as the named A.2 gate at 19:22Z: it is `rv0057-f001`, a migration mid-flight, and it ends on its own when the 238 files move (laptop-side). Direction discriminator holds: **8 of 8 shrank, 0 grew, 0 unchanged**, 1.46x–23.81x, median 5.94 — reproduces `0.4.0_DS_ClientPlatform~L`'s figures on a fresh run. ⛔ **DID NOT `mkdir org/audit/archive/<device>/`** — that silences the findings by making the tool believe we are post-migration and compare against an EMPTY chain. The remaining findings are ABSENCE, a shape the direction discriminator does not address; routed to the note's owner, not chased. **COUNT RECONCILED with `3.0.0_SA_CVO~Z` (they read 13, I read 18): the tool's own header says 18 = 5 `COVERAGE` + 13 `INTEGRITY`, and `INTEGRITY` 13 = 8 `NON-APPEND-EDIT` + 5 `ERROR-FAILCLOSED`. CVO scoped to the INTEGRITY class; I counted every printed line. The `COVERAGE` and `ERROR-FAILCLOSED` file sets are IDENTICAL, so it is FIVE absent FILES producing TEN lines — my earlier "10 absence findings" was line-correct and invited reading it as ten files.** Neither count was wrong; they had different denominators. |

---

## Open / routed, not performed

- ⛔ **The PROD promote must carry TO-3 AND TO-4 TOGETHER.** TO-3 alone on PROD is an ungated
  declared set -- every firm sees the pill. DT lane, Andrew's word.
- **TO-4's AE limb (deploy) is NOT seated on me** and there is no AE seat on this fabric. Routed,
  not performed.
- **Wiring `SATELLITE_REGISTRY` to TO-2's published registry** is blocked on COO's SAT-a-4 delivery
  form: not a build-time constant, `vintage()` must resolve the data's as-of at READ TIME, and the
  staleness arm must be re-exercised THROUGH the chosen carrier. Ruling pinned into the seam at
  `705bb9df`.
- `SAT-b-5` (whether a 0-account satellite renders) is a COO/DE display decision, not one of TO-3's
  cells. Untouched -- it must not be resolved by accident of the predicate.
