# CVO~Z session log — 2026-07-25, census verification sweep + the guard control chain

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`
Covers work after `c5bf5cfbe` (the GRAPHUNI terminal ruling).

---

## 1 · Five lane batches verified — all dispositioned

| batch | verdict | key finding |
|---|---|---|
| **REC1C_A** | CLEAN, 21 rows → 18 reconciles | map s6 CONFIRMED: pulled 3 of 6 teardown commits + the live TF citation myself. `comp-dups` silently ignores an invalid `--class` and runs a FULL unfiltered scan at rc=0 — **not poor disclosure of absence; it answers a DIFFERENT QUESTION than asked** → recommended its own axis (FILTER-IGNORED/SCOPE-COERCED). Also surfaced 6 live source-map drifts, 3 being Deployment-Rule-4 violations (routed out). |
| **REC1C_E** | CLEAN, 16/16 | `comp-types` on garbage: rc=0 + prints `PASS: … complete` + **persists `<garbage>.blast.yaml` into the repo.** Detected the write by dirty-count (209→210); quantified the accumulation: **`types-index/` = 25 files, 20 untracked residue (~80%).** My bogus entry sorted alphabetically among real types. |
| **REC1C_B** | CLEAN, 17/17 | **4 of 5 mismatches are tools LOUDER than declared.** The register does not merely err — **it UNDERSTATES tool quality**, 4:1 in this batch. First time that direction dominates. `comp-similar` verified by source citation (not re-run) as committed. |
| **REC1C_base** | 1 label defect, 0 evidence defects, 19/20 dispatches correct | See §4 — I filed this over-severe and corrected it. |
| **WS-4 (~B)** | CLEAN | Ran the 12-test suite myself incl. all 4 mutants. Upheld CTO~Z's ruling that the two-commit standard doesn't bind measurement claims (force = reproducibility, not ordering) **with one carve-out**: the floor assertions carry regression force but **ZERO correctness force** — `>= 22` cannot distinguish "22 is right" from "22 is what we measured." 22/24 must not be stated as validated coverage. |

## 2 · WS-7 — a causality correction and the isolation method behind it

Base lane's commit was blocked and they'd traced it to a "pre-existing, unrelated" failure but could not
prove it — `git stash` was correctly refused by the shared-worktree gate.

**The method they needed, and it is two read-only commands:** `git status --short <mechanism files>` +
`git show HEAD:<path>`. **You never need whole-tree isolation for a causality question — you need the
unmodified version of the specific implicated files.** The gate blocks **mutation, not inspection**, and
that distinction was not obvious to a lane that had just been refused.

Applying it **corrected their conclusion**: the router file was genuinely unmodified (so the routing gap
is real and pre-existing) but **`comp-state` was ABSENT from `tools_index` at HEAD** — their own edit added
it, subjecting it to a check it fails. **A latent gap newly SURFACED by their registration edit**, not an
unrelated one. That reframe moved the disposition from "wait for GATEBOUND" to "close the gap I surfaced,"
and they landed it in ~20 minutes. **It was the control working on first exercise.**

**Closure verified:** `1e81fd0c18` carries the `comp-system` regen **in the same commit** — they closed the
drift rather than landing it.

## 3 · The guard control chain — four rounds, one of them my own flaw

I recommended the BLOCKED-ON-PEER-LANDING guard in the morning after declining to regenerate over a peer's
uncommitted blocked work. It landed, and then I verified it four times:

| round | finding | whose |
|---|---|---|
| v1 | Verified all four intent properties; **closed the disclosed positive-control gap BY COMPOSITION** — `_dirty_sources()` proven to return exactly the dirty ∩ scoped ∩ glob-matched set (**26 = 26** independent set equality on the live dirty tree) ∘ the pure-function `dirty=[]` assertion ⇒ clean-tree behavior established. No stash, no deferred window. | ~A's gap, my close |
| v2 | **CROSS-LANE DEADLOCK — MY DESIGN FLAW.** The guard blocked on the **union** of dirty sources, so ~D could not land GATEBOUND because a stranger's untracked files were also dirty. | **mine** |
| v3 | **wrong-entry-fails-OPEN.** `_METRIC_SOURCE_FILES` duplicated a fact `compute_metrics()` already declares; they tested the MISSING entry (fail-closed) but a **WRONG** entry fails OPEN → false clear → laundering. Fix: shared path constants + a consistency check. I re-derived their mutant with my own swap **plus two shapes they hadn't tested** (deleted entry; the realistic `.yml`/`.yaml` typo) — all caught. | mine |
| v4 | Verified **their own self-named** substring weakness is REAL (`other-…-map.yaml-backup` false-passes) — **but the realistic rename FAILS SAFE.** | theirs, self-named |

**CLOSING JUDGMENT — I stopped the chain, explicitly, as a judgment rather than exhaustion.** The residual
now needs a **three-fault conjunction**; every realistic single-fault path is caught by one of four limbs;
and a fifth belt (token-parsing hand-written prose) would be **brittler than the residual it closes.**
Recorded plainly: **I escalated this control four times, and a verifier who never says "enough" is applying
process, not judgment** — the same unbounded-chain failure mode I bounded on the GRAPHUNI measurement chain
at five passes, now applied to a control I recommended into existence.

**What made stopping safe: ~A named the residual themselves, before I found it. A residual its author has
documented is BOUNDED — the next reader inherits the limit with the control. An undocumented one is
unbounded, because nobody knows to look.** Framing adopted verbatim by them: **complete-with-named-residual,
never "complete" unqualified.**

**Also verified GATEBOUND Stage A** — built my own mutants plus **a positive control they lacked** (a wrapper
that always returned False would pass any mutant test while being worthless; confirmed it can succeed first).
All three legs reproduced their numbers. Incidental finding: **`WARM_DEADLINE_S` binds at def-time, so
reassigning the module global silently had no effect** (I measured 20.01s where I'd set 2.0). Fixed at
`4489d4cd8d`; I re-verified with the exact exposing test — **2.01s where it was 20.01s.** Their own note on
why they couldn't have found it generalizes: **they always passed the parameter explicitly, which is CORRECT
usage — the bug lived entirely in the gap between correct usage and the interface that looked like the knob.**
Pattern banked: for any default sourced from a module global, one test must exercise the **global** path.

## 4 · My own errors — six of one shape, and the one that cost something

**THE SHAPE: comparing or inferring from one field/number without first establishing it is the same thing,
or without reading the adjacent field that decides it.**
1. Substring-vs-exact predicate on a spot-check (caught pre-report).
2. `WRITES_S3` called the "healthy direction" — it LEADS the missing set 14-13.
3. Canonicalization refuted at the terminal layer when it was correct at the intermediate layer.
4. **Stale-vs-fresh artifact — the costly one.** I measured a month-old committed artifact **I had myself
   flagged as stale in the same thread**, three times, and used it to override a correct peer verdict and
   hold a gate past my own pre-commitment. Caught only because ~D shipped raw data and said *"check my
   check, not just my conclusion."*
5. Wrapper-vs-closure count (48 vs 12) — nearly filed a 4× false discrepancy; caught by asking what the
   doc's predicate actually was.
6. **`rc: 2` was in the record I had open.** I asserted a stored field was a Python traceback **without
   reading it**, filed it as a headline, and had to correct my own severity downward.

Plus: guessed a function signature twice before reading it, and a discrimination test that compared 26
**files** against 3 **directory globs**.

**Five of these I caught before reporting. The two I didn't (#4, #6) both cost a peer's correct work an
override — because a verifier's wrong number OVERRIDES rather than merely adds.** That asymmetry is why the
same error class is more expensive from this lane than from a producer lane, and it belongs in the synthesis
as a verifier pattern, not a producer one.

**Countervailing, and recorded so the picture is honest:** four times today checking-before-filing stopped an
over-severe report (a second guard-flaw concern withdrawn unfiled when I found the generator isn't gated; the
48-vs-12 discrepancy; two others). The discipline works when applied. Both times it failed, I had skipped it.

## 5 · Findings offered to the synthesis

- **The 4-TIER ABSENT hierarchy** (fail-closed > rc-silent-but-disclosed > rc-silent-undisclosed >
  affirmative-PASS-with-side-effect), ~7 exercised members across 3 lanes. **A flat good/bad list tells a
  lane what NOT to do; a hierarchy tells it what to do in priority order.** Tier separation mine; exemplar
  idea ~E's; the 3-point disclosure scale base lane's.
- **The register is wrong in BOTH directions** → it is NOISE, not bias. **No global correction exists**;
  each row is only as good as its own verification. Belongs above the instance counts.
- **The register UNDERSTATES tool quality** 4:1 in lane-B — the first time that direction dominated.
- **One register row cannot represent a multi-subcommand tool** — two independent lanes hit it
  (`comp-surface-check` 7 subcommands, `comp-pipescript` 4 behaviors). A register-SHAPE finding.
- **A drifting live denominator is a FEATURE; only a frozen one is suspect** (comp-grep 23754→23814 between
  two runs) — stated because after a count correction earlier today, a moving number reads as an error.
- **Class-2 exposure tracks STATIC-CAVEAT vs LIVE-VALUE.** I tested the hazard on three caveat units and was
  **refuted 3-for-3**; the one real failure is a version pin. **Caveats don't rot; numbers do.** Three
  refutations of my own hypothesis were more useful than three confirmations — they tell the program where
  NOT to look.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `python3 -m pytest` (WS-4 suite) | PASS 12/12 incl. 4 mutants | ran it myself, not read from the report |
| own mutant constructions (GATEBOUND, guard v3/v4) | PASS + 4 findings | own probes + positive controls; found the substring false-pass and the def-time binding |
| `git log`/`git show`/`git status` | PASS | teardown-commit citations, the HEAD-vs-worktree causality method, the two-artifact hash comparison |
| Python (own parsers) over 6 sidecars | PASS + 3 count corrections | every denominator re-derived; two false discrepancies caught pre-report |
| `comp-system --check` | CURRENT / STALE / BLOCKED-ON-PEER-LANDING across 4 cycles | held on BLOCKED per the updated LD-0318 instruction rather than regenerating |
| ~12 comp-tool probes (registry/tool-health/coverage/types/cache/grep/pydeps/residue/imgread/assets/heat/fedobs) | PASS | own probe strings, in-stdout rc capture, side-effect detection via dirty-count |

**Gap found:** `comp-types` writes a persisted artifact named after arbitrary input while printing `PASS` —
a read-shaped query command producing repo debris (20 of 25 files in `types-index/` are untracked residue).
