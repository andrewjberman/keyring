# 0.4.0_DE_ClientPlatform~D — ADVI_PERFRP.TO-R1-DE re-seat, 16:00–18:15Z

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, DIAGNOSE

Seat re-armed after the fabric shutdown killed the predecessor mid-round (CTO D2-D3 ledger row 10,
COO 78243). Scope: ADVI_PERFRP.TO-R1-DE only.

**Commits (all under this lane's author line):**

| repo | hash | what |
|---|---|---|
| portal | `481a31c5` | merge `origin/DEV` into DEV — the one conflict was two ADDITIVE flags |
| portal | `2b8f7987` | PRF-d-1 / AC2: CSV export wired — the projection was written, exercised, wired to nothing |
| portal | `9957410e` | PRF-d-1: Manage Table MOUNTED — the second built-but-never-wired control |
| workspace | `2813c8d8c4` | AC2 → PASS + the PRF-d-1 caller census artifact |
| workspace | `c7f6ae7c17` | AC8 reason retired, status HELD |
| workspace | `537de2bf75` | AC10 → PASS on all three limbs |
| workspace | `a7924a327d` | AC10 mask spec: issuer baseline clause + `baseline` harness command |

**Push state, measured by `ls-remote` at this seat, not from any message:**
`origin/DEV` = `9957410e` = portal local HEAD (CI "Build & Validate" conclusion **success**, run
33194560122). `origin/CLOUD` = `537de2bf75`; `a7924a327d` LOCAL, rides the next window.

---

## What happened

**The seat's work had been stranded three days.** Six portal commits sat local. The predecessor
(and I, initially) mis-diagnosed why. I read `portal/.git/hooks/pre-push`, correctly enumerated its
three limbs, found no integrator clause, and reported the gate did not exist. It does —
`.tools/hooks/never-rules-gate.sh:509-559`, the **harness** PreToolUse layer, invisible from inside
`portal/.git/`. COO had already accepted my correction and was about to write it into a drive log;
I retracted before it landed (78289). **I read one plane correctly and let "not in this layer"
become "not on this surface."**

**Merge conflict, resolved as a UNION not a choice.** `scripts/ui-smoke.mjs`: HEAD added
`--clicktext`, `origin/DEV` added `--pick` (ETFS_SATELLITES). Both authors wrote "ADDITIVE" in
their own comments. Taking either side would have **silently deleted a peer's instrument and passed
every gate** — a missing step-flag is not an error, the reducer just never emits it.

**Two defects, one shape — "build-but-never-wire".** `PerfrpCsvExport` + `perfrpTableToCsvRows`:
built, suite leg L26 **green over the projection**, and **zero production callers** — a green suite
certifying an export no reader could reach. Then the same census found `PerfrpManageTable` +
`usePerfrpColumnVisibility` in the same state. Both mounted; `csvFilenameStem` is now a **required**
prop, so a table without an export is un-typecheckable (control: TS2741).

**AC2's stated wait had gone stale in the favourable direction, on this lane's own commits.**
"CSV cannot be evaluated over 0 tables" was true when written; tables landed 08-25 (`67caa6ad`,
`cad72c82`) and nothing re-read the row. Second instance of the class COO named in 71722 §4.

---

## Instrument defects found in my own work (the useful half)

1. **The caller census, first run, would have published four false gaps.** I excluded the defining
   module to avoid counting definitions — which also excluded **intra-module composition**, so it
   reported 0 call sites for four controls I had *just read on a render*. Had it shipped, the four
   false gaps would have discounted the two true ones. *A census that cannot see composition
   measures file boundaries, not wiring.*
2. **A zero is not a verdict.** Two controls had 0 uses and take **opposite** verdicts:
   `PerfrpTable` = real gap (nothing else serves it); `PerfrpPeriodUnavailable` = **dead code**, the
   behaviour is served inline at `AdvisorBookClientDetail.tsx:189` (exercised: Period 1Y swaps the
   Fee Summary panel for the honest notice — AC7 working live).
3. **AC10 run 1: a FALSE CONFESSION I nearly filed against myself.** 528 differing px on both
   protected tabs. Cropped and **looked**: a paper-plane nav icon present pre, absent post — that is
   `@18fd5b38`, `0.3.0_DT_TradingOperations` removing Submit-a-Request. **A peer's commit in shared
   chrome.** The report one step away was "my change moved the protected tabs." *A false confession
   is as damaging as a false pass and is the direction nobody audits — a seat reporting failure
   against itself reads as rigorous and gets filed.* **Both halves of a FAIL are measurements: the
   fact AND the attribution.**
4. **A pinned ref decays as a baseline.** The spec pinned `d43b88c5`; `d43b88c5..3cfa7e8a` holds 40
   commits from 6 seats. The spec's own §2 **warned** about exactly this mis-attribution and the
   warning did not save the run — *a warning is not a mechanism*. Sound baseline is the
   **relationship**: `481a31c5^2` = `57701d5c`, window = 9 commits, 9 of 9 mine, and `18fd5b38` is an
   *ancestor* of the base — excluded by construction. Re-run: **PASS, 0 px** both tabs.
5. **A silent wrong click reads as a successful one.** `--click "1Y"` printed `CLICKED: 1Y`, rc=0,
   and hit the **Assets Overview** window toggle, not the Performance Controls period. Only the
   `--clicktext '1Y#1'` re-run is evidence.
6. **A downscaled screenshot is not an instrument for reading a digit.** I briefly read the unserved
   denominator as "8 of 8"; it is "6 of 8". Confirmed by the derivation (`accountRoster.ts`
   untouched), not by the pixels.

---

## Near-miss worth naming (COO 78581 asked for it here)

⛔ **A JUNCTION IS A PATH THAT LIES ABOUT ITS OWN EXTENT.** I junctioned `portal/node_modules` into a
temporary worktree, then reached for `rm -rf /c/ac10pre/node_modules` — which would have deleted
**through the junction into the real `portal/node_modules`**. The permission guard refused the
recursive delete; that refusal is the control that held. Correct removal is `rmdir` (Windows does not
follow a junction on rmdir). Verified after: 308 entries intact.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `bun run typecheck` | `tsc -b --noEmit`, 5 runs | PASS | never bare `tsc --noEmit` (portal CLAUDE.md) |
| typecheck **positive control** | injected `const x: number = "str"` | PASS | rc=2 TS2322 → restore sha256-identical → rc=0. A `tsc -b` green means nothing un-controlled |
| `perfrp-contract-exercise.mjs` | under **bun** | 35/35 | refuses under node (partial run ≠ verdict). L25 refused my dirty tree first — the leg working |
| `proof-of-spec-check.py` | positional, 13 criteria | VALID rc=0 | schema REFUSED my invented `controls` keys (rc=1); I moved the census rather than widening the schema |
| `ac10_closure.py` | `. ` | PASS | 80/78/2/78 — the spec's printed 69/67 is **stale** |
| `ac10_maskcheck.py derive` | n=5 × 2 tabs | PASS | 20/20 pairs, bbox byte-identical to declared |
| `ac10_maskcheck.py compare` | pre→post | PASS | 0 px outside mask, both tabs |
| `ac10_maskcheck.py baseline` | **new**, 3 arms | PASS | valid / foreign-author refusal / non-merge refusal all fire |
| `/frontend-dev` ui-smoke | 14 captures | PASS | every render READ; colour law clean |
| `ruff` (commit-gate) | via safe-commit | FAIL→PASS | caught F811 duplicate `os` + E741 `l`; both real, fixed |

**What worked:** the exercise suite's dirty-tree refusal and the schema's `additionalProperties:
false` both stopped me doing the wrong thing. **What failed:** my census's first form. **Gap found:**
`safe-commit.sh` cannot express a merge commit (`git commit --only` → rc=128 during a merge) — ruled
by CTO 78389 (interim form accepted; `--merge` limb to `0.8.0_AE_CloudComp` post-campaign).

---

## Current State

ADVI_PERFRP.TO-R1-DE: instance **VALID rc=0, 6 PASS / 7 UNCOMPUTABLE** at
`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/ADVI_PERFRP.TO-R1-DE_PROOF_OF_SPEC.json`
(BASE folder — the TO's declared `~D` path does not resolve; held INERT per 71400, the checker
discriminates loudly). PASS: AC1, AC2, AC7, AC9, AC10, AC13.

All portal work published at `origin/DEV @9957410e`, CI green, main worktree on DEV, tree clean.
Temporary pre-state worktree unregistered from git; the directory `C:\ac10pre` remains on disk
(recursive delete needs Andrew's word).

**Remaining 7, split honestly:** AC3/4/5/6/11 are **genuine producer waits** — verified, not assumed:
no PERFRP b-series commit since 2026-08-25 and `PERFRP_AVAILABLE_LEAVES` is still an empty Set, so no
leaf has reached the render path. AC8 HELD: `KNOWN-NOT-HELD` is declared in the taxonomy and
**unreachable** (`rosterCellsFor` assigns `position_only: NO_SOURCE` unconditionally) — a fourth
variant of the family, at the *taxonomy* grain; its SI-label clause is blocked on the **instrument**
(a screenshot cannot show a `title` attribute) and cannot move the row either way. AC12 waits on a
final render.

## Blockers

**None BLOCKING.** Every open criterion is a producer wait owned by the DS PERFRP lane (b-series
leaves), evidence cited above. Portal DEV publication is the integrator's by design, not a stall.

## Next Steps

- [`0.4.0_DS_ClientPlatform` PERFRP lane] the b-series leaves; the first one landing unblocks
  AC3/4/5/6/11/12 and is **one edit** here (`PERFRP_AVAILABLE_LEAVES`).
- [`2.0.0_SA_COO`] seat is **release-eligible** on reversible terms (re-seat on the first b-series
  leaf); the richer Manage Table picker is a named open gap for next round.
- [`0.4.0_DE_ClientPlatform~D`] if kept: the SI-label DOM attribute read — sharper than the
  screenshot oracle, but it moves no status.
- [Andrew] `C:\ac10pre` cleanup (recursive delete).
