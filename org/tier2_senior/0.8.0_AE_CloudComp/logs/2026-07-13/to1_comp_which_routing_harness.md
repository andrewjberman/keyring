# NFRA_COMPASSURANCE.TO-1 — the comp-which routing-quality harness

**archetype:** VALIDATE
**Agent:** `0.8.0_AE_CloudComp~Z` (~Z lane, NFRA-only, THIS TASK ONLY)
**Issued by:** `2.0.0_SA_COO~Z` · **Session:** 2026-07-13 21:15Z–
**TO:** `org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_COMPASSURANCE.TO-1.generated-routing-harness.md`
**Deliverable:** `.tools/comp-which-routing-test.py` (REPLACED) + a FROZEN cohort + a blob-pinned baseline.

---

## What this TO was, in one line

We had **no honest coverage number** for `comp-which` — the router CLAUDE.md Rule 21 makes mandatory for every
search in the fabric. Every downstream TO (abstain, top-k, catalog) is graded against the number this harness
produces. **If the number flatters us, every gate built on it is decorative.**

---

## THE HEADLINE — TWO NAMED METRICS. **NOT AN ERROR BAR. DO NOT AVERAGE THEM.**

```
SUBJECT   .tools/comp-which @ 52d008f4c   blob 673176ddd68d   (the TO's named vintage)
COHORT    FROZEN + MATERIALIZED from a rail-log snapshot captured BEFORE my first probe

  34%  "Of EVERYTHING comp-which is ASKED, what has no catalog vocabulary?"
       (includes HUD-injected glob patterns — comp-tool-hud.sh:291)

  29%  "Of NATURAL-LANGUAGE QUESTIONS AGENTS ASKED, what has none?"
       <<< THE COVERAGE HOLE PROPER. What the metric actually claims to mean. >>>

  Cohort C (catalog-derived — the FLOOR, explicitly NOT the headline) = 18.2%
  ==> the catalog-probe design we killed STILL understates the hole by 1.59x
      even on the reading most hostile to the finding.
```

**These answer two different questions.** They are not bounds on each other and there is **no true value in
between**. A reader will average a bracket — so it is not presented as one.

**And the globs are not noise: they are a CORRECT ABSTAIN, MISCOUNTED AS A HOLE.** `**/*COMPASSURANCE*` *has* a
right answer — `comp-glob`. A glob scoring zero on the curated rules and falling through to the primitive is
**the fallback working exactly as designed**. Counting it as a coverage hole **scores a SUCCESS as a FAILURE**.
(COO~Z's ruling; my AC14 measurement, his interpretation.)

Label-free, no ground truth, nothing to argue about — **a denominator nobody on this project authored, because
agents wrote it, not us.**

### ⚠️ THE CORRECTION SEQUENCE IS MONOTONIC. 1.59x IS NOT A FLOOR.

```
  2.40x  ->  1.87x  ->  1.84x  ->  1.59x
```

**Every single correction moved the same way: the effect shrank.** I framed that as *"the finding survived every
check."* COO~Z reframed it correctly, and it is the sharpest methodological point of the night:

> **A random error process corrects in BOTH directions. A MONOTONIC sequence of corrections is the signature of
> a SYSTEMATIC BIAS that is still only partly uncovered.**
>
> **RESIDUAL RISK, STATED IN THE DIRECTION IT IS LIKELY TO BE WRONG: further contamination, if found, is
> LIKELIER TO SHRINK THIS THAN TO GROW IT.**

**A FOURTH CONTAMINANT IS CONFIRMED AND IS NOT REMOVED.** I dumped 25 random zero-scoring strings and read them:

```
  "phhpk cpeaj djfkc"      <- generated gibberish — an agent's own probe
  "banana bread recipe"    <- an off-domain control probe
```

**My exact-token strip list cannot catch these — GENERATED gibberish is unpredictable by construction, which is
the entire point of generating it.** 2 in 25 (~8%); **n=25 is not a point estimate and I do not quote it as
one.** They score zero *legitimately*. They are not coverage gaps.

> **Every contaminant in this project was found by READING THE STRINGS. Not one was found by reading the
> aggregate.** My `ROUTE-` inheritance, COO~Z's filter, my `[:6]` slice, the globs, and now these — **all five
> were invisible in the summary statistic and obvious in the raw rows.**

**The finding survives anyway, and that is the only reason to trust it: 18.2% vs 29.0% = 1.59x, on the reading
most hostile to it, after four attempts to kill it — three of them by its own authors.**

---

## THE POST FINDING — and the part of it I got WRONG, first

PRE/POST, both blob-pinned, both through the non-polluting mirror:

```
  PRE   52d008f4c (argmax)          gibberish 2/40 get a tool   rc=0 always   NO warning banner
  POST  c52f83612 (abstain+top-3)   gibberish 2/40 get a menu   rc=1          WARNING BANNER PRESENT
```

### ⚠️ WHAT I CLAIMED, AND WHY IT WAS FALSE — this is the most important entry in this log

I reported to COO~Z that **"the abstain is CORRECT and INVISIBLE — an agent reads stdout, an agent does not
read `$?`."** It made a clean story. **It was wrong.**

The abstain **is** in stdout, and it is prominent:

```
  !! NO CURATED RULE MATCHED THIS QUESTION (every score is below the vetted band).
     These are FUZZY GUESSES, not a routing decision. If none of the descriptions
     above answer your question, THE CATALOG DOES NOT COVER IT -- do not pick one.
```

**I never saw it, because my grounding command sliced the output with `out.splitlines()[:6]`.** I printed the
first six lines, and then reasoned about *"what an agent sees"* from the slice.

> ## A TRUNCATED SCAN IS NOT A NEGATIVE RESULT — INCLUDING WHEN IT IS YOUR OWN OUTPUT, AND ESPECIALLY WHEN IT AGREES WITH YOU.
>
> This is the **third** time tonight I truncated a scan and reasoned from it as complete (the `head` that let
> me delete a gate's symbol; the tag-census regex that presupposed its own answer; and now a `[:6]` slice).
> **I committed it in the argument I was most confident about.** *Knowing a failure mode by name does not
> immunize you against writing it.*

### WHAT ACTUALLY SURVIVES — two real contract divergences, both REPORTED, neither adjudicated by me

1. **PRD §3.1 gap.** §3.1 says NO FIT prints `MATCHES: none` + `VERDICT: NO FIT`. The binary prints
   **`MATCHES (top 3 of 41)`** — a ranked, scored, described menu — **ABOVE** the warning. A scored menu
   first and *"do not pick one"* second is a **mixed signal**. *The exit code is not the contract; **the
   output is the contract**.* (That sentence survives; the "invisible" framing does not.)

2. **PRD C-3 gap — THE SUBJUNCTIVE SURVIVED THE FIX** (found by COO~Z; I confirmed it on execution evidence).
   C-3 requires NO FIT to **ACTUALLY RUN** comp-grep/comp-glob — *"no subjunctive."* It does not.
   **Zero execution evidence** — no `matches=`, no `files=`, no `scanned=`:

   ```
   the original defect:  "No tool fit? it WOULD RUN comp-grep -- never a dead-end."   a promise, never kept
   the shipped fix:      "or search directly:  comp-grep 'smbhbrej'"                  a suggestion, never run
   ```

   > **IT CHANGED GRAMMATICAL MOOD AND NOT EPISTEMIC STATUS.** *"it would run"* became *"you could run"* —
   > **and neither of them runs.** C-3 was written specifically to kill that sentence, and a differently-worded
   > version of the same sentence shipped inside the fix.

   Whether printing beats auto-running a slow grep is a **genuine design question** — but it is a **decision**,
   and right now it is an **unremarked divergence from the contract.**

**The harness now measures FOUR signals separately** (`rc` / warning banner / menu / did-the-fallback-actually-run)
**and convicts on only ONE** — an *unguarded* misroute (a menu with no abstain on either channel). The two
contract gaps are **reported, never convicted on**: they are TO-2's call, not the harness's. **Binary untouched.**

---

## Findings surfaced (all measured, none inferred)

| # | Finding | Status |
|---|---|---|
| 1 | **The harness eats its own denominator.** `comp-which` `_log_rail`s on EVERY invocation (`:792-805`, no suppress flag, `WS` from `__file__`). Cohort R is `count==1` singletons — probing them re-injects each, making them duplicates, **ejecting them from the next run's cohort.** AC5 was killing AC8. Proven by exercise (6310→6311). | **FIXED** via a byte-identical scratch-WS mirror. COO~Z ratified. |
| 2 | **The OLD harness was the polluter.** Its `self_route_verdicts()` feeds every tool its own `use_case` through the LIVE binary against the REAL workspace. Fingerprint (strings existing ONLY in that file): `"could the AdvisorsTab leak a client SSN to the browser?"` ×39, `"which directories are dead and safe to delete?"` ×41 → **it ran ≥41 times.** CTO~Z measured the total at **87.6%** of the log. **And it is wired into a FAIL-CLOSED COMMIT GATE, so it re-pollutes on every commit, forever.** | **FLAGGED, NOT FIXED** (TO-2/TO-4). Behaviour preserved verbatim. |
| 3 | **`--route-only` is not side-effect-free.** It guards `_run_primitive()` only; `_log_rail` still fires. The HUD's PreToolUse hook (`comp-tool-hud.sh:291`) passes the agent's **raw search query** — so every HUD nudge injects a search *pattern*, not a question, into the log. | Reported (AC14). |
| 4 | **A SIXTH tool count.** `completeness` reports **42 registered**. Tally is now 46 RULES / 66 manifest / 63 footer / ~30 CLAUDE.md / 41 top-k header / 42 registered. | TO-4's. Reported, not reconciled. |
| 5 | **Malformed rail rows.** 128 `<unparseable>` + ~100 shell-fragment "tags" (`"===`, `-rln`, `MSYS_NO_PATHCONV=1`). `_log_rail` strips newlines from `q` but **not from `term`/`intent`** — multi-line commands spill across lines. Every line-based parser mis-reads them. | Reported. Cohort R unaffected (cannot match the ROUTE tag). |
| 6 | **`DENY` = 449 rows** — a whole tag class nobody had named. | Surfaced by the mandatory tag tally. |

---

## MY OWN ERRORS — on the record, because a self-report that omits them is worthless

1. **I BLOCKED EVERY AGENT'S COMMITS IN THIS WORKTREE.** My rewrite deleted `self_route_verdicts()`; a
   **repo-wide, fail-closed** commit gate (`manifest_check_cli.py`) loads this file as module `cwrt` and calls
   it. `--force` does not bypass it. **Restored as a documented PUBLIC CONTRACT; verified by EXERCISING the
   gate** (`completeness` → PASS over 42 tools), not by reading a symbol.

2. **The instrument that failed me was my own, and it failed the exact rule I had quoted twice that hour.**
   I ran a reverse-dependency grep to clear myself **and piped it through `head`.** 10 lines printed, the
   consumer sat below the cut, and I read a **truncated output as a complete negative result.** Re-run
   properly: **7 consumers, not 2.**
   > **A TRUNCATED SCAN IS NOT A NEGATIVE RESULT. Print the denominator of every scan you reason from —
   > *including the one you ran to prove yourself safe.***

   `comp-blast` is genuinely blind to `.tools/` (PRD F-5 — no comp-tool *could* have warned me). **I refused
   to let that launder the operator error.** They are two findings; merging them buries the one I can fix.

3. **A pass over an empty set is not a pass.** `commit_gate_runner.py` printed `OK: pre-commit gate clean for
   0 file(s)` — it never reached the manifest-check family. Had I stopped there I'd have declared "unblocked"
   off a gate that ran over nothing.

4. **My own tag census had COO~Z's bug and I missed it for the same reason.** My regex was
   `ROUTE-[A-Z-]+|RUN-[A-Z]+`. It tallied **8,159 of 10,518 lines and I never asked what the other 2,359
   were.** I wrote a regex that presupposed the answer, then read its output as an enumeration. The 1,487
   bare-`ROUTE` rows were sitting in my complement the whole time.

5. **My pollution check was wrong twice.**
   - **v1 (count delta)** — confounded by concurrency; reported `+2 POLLUTED` over rows that were not mine.
     *It fired correctly for the wrong reason, which is its own kind of lie.*
   - **v2 (attribution by probe string)** — still wrong, **in the accusing direction**: my probe set is drawn
     **from** the log, so a concurrent agent asking one of those questions is byte-identical to me writing it.
   - **v3 (a positive alibi)** — every route I issue lands in the **mirror's** log; 713 issued, **713
     captured, all accounted for.** Immune to concurrency because it never looks at the shared file.
     > **AN ALIBI BEATS A DENIAL.** Prove where your writes went; do not merely fail to find them elsewhere.

6. **I measured my own exit code with an `echo` in between.** Reported `HARNESS EXIT: 0` when the harness had
   exited 2. **I measured the echo's `$?`.** Fixed.

7. **My posterior-floor mechanism guess was WRONG.** I predicted `top == 0` would never fire. The abstain
   *does* fire (rc=1), so it is not keyed that way. **I got the SHAPE right (a guard the live path does not
   reach) and the MECHANISM wrong, and I am not letting the right shape launder the wrong mechanism.**

8. **I OVERSTATED THE POST FINDING AND SHIPPED IT TO MY COO.** I claimed the abstain was *invisible* to
   agents. **It is not — the warning banner is in stdout.** I had sliced stdout to 6 lines (`[:6]`) and
   reasoned about "what an agent sees" from the slice, **and I did not quote the part of my own evidence that
   refuted my own claim.** That is selecting the evidence that supports the conclusion — the exact trap I had
   caught in someone else's work an hour earlier.
   > **THREE TRUNCATION ERRORS IN ONE SESSION** — `head` (blocked the worktree), a census regex that
   > presupposed its answer (missed 2,359 lines), and `[:6]` (manufactured a false headline). **The tool is
   > different every time. The error is identical every time.** *A truncated scan is not a negative result.*

   COO~Z caught it, and disclosed that he had made **my** `echo`/`$?` error **sixty seconds after reading my
   warning about it.** Neither of us was careless. **Knowing a failure mode by name does not immunize you
   against writing it — which is precisely why these belong in a GATE and a TO, not in a lesson.**

---

## Compiler Tools

**MANDATORY SECTION.** Every `<run>` in the TO's `<compiler_tools_mandate>`, with observed output and an
explicit pass/fail against `<expect>`.

| Phase | Tool + command | Expected | Observed | Verdict |
|---|---|---|---|---|
| 0 | `wc -l org/mcp/comp-which-rail.log` ; `grep -cE 'ROUTE-'` | ~10,514 lines / 6,308 ROUTE | **10,518 / 6,309** | **MISMATCH → re-derived, as `<if_mismatch>` demands.** Log is append-live. I did NOT reuse COO~Z's numbers. |
| 1 | `comp-which "how fresh is the platinum mdpf aggregate"` | rc=0 + a single confident route | rc=0 → `comp-platinum page` (CLAUDE.md's own table says `comp-freshness`) | **PASS** — baseline captured. TO-2/TO-3 had not landed *yet*. **NOTE: COO~Z later RETRACTED this mandate — the string is a real rail-log question and running it live ejects it from the singleton cohort. Disclosed; it is in the printed strip list.** |
| 1 | `python -c "...graph-call-manifest.yaml..."` | 66 entries / 66 use_case / 38 tools | **66 / 66 / 38** | **PASS** — re-verified, did not trust the TO. |
| 1 | `comp-blast comp-which` | **NOT-FOUND** (expected to fail to find) | `NOT-FOUND: no graph node matches 'comp-which'` | **PASS (as designed).** The compiler graph does not model the compiler tools — **PRD F-5, and it is the reason nothing could warn me about finding #1 in "my own errors" above.** |
| 2 | `python .tools/comp-which-routing-test.py` | per-cohort n / zero-rate / denominator; R=HEADLINE; C=NOT-HEADLINE; recall@3 | All emitted. R bracketed [33.1–33.8%]; C labelled SELF-CONSISTENCY; recall@3 = 80.3% (PRE) / 90.9% (POST) | **PASS** |
| 2 | **MUTATION TEST** — force every score to 0, then to 9 | harness FAILS LOUDLY both ways | `mutant_all_zero → DETECTED: YES` ; `mutant_all_nine → DETECTED: YES` ; scorer restored | **PASS — demonstrated, not asserted.** |
| 2 | Positive + gibberish controls, **each in isolation** | positive > 0 ; gibberish 100% zero | positive = **5** ; gibberish **40/40 zero at RULES** | **PASS** |
| 2 | **r[1] anti-control** (my addition) | reproduce the known space-count bug ON PURPOSE | gibberish scores **33 via `r[1]`**, **0 via `r[0]`** | **PASS** — proves the harness is attached to the *real* scorer. *A control that cannot detect the bug it was written for is a decoration.* |
| 3 | Re-run + commit the baseline artifact | a committed, dated, blob-pinned baseline | `comp-which-routing-baseline.json` + `comp-which-routing-cohort.frozen.json` | **PASS** |
| — | `comp-which` (the rail, for my own searches) | — | Used where a comp-tool fit. Raw greps into `.tools/` carried inline `# rail-checked:` markers — **comp-blast is structurally blind to `.tools/` (F-5), which is the documented reason no comp-tool fits a `.tools/` reverse-dependency search.** | Logged |
| — | `manifest_check_cli.py completeness` | the gate I broke must pass | `PASS: routable + placement + self-routes + existence, over 42 registered tool(s)` rc=0 | **PASS — exercised, not config-read.** |

**Gap found in the compiler toolchain:** `comp-blast` cannot see `.tools/*`. **A worker deleted a function
with a live fail-closed-gate consumer and every instrument we own said it was safe.** That is PRD **F-5 /
Q3** exercised in anger, by the worker, against himself. It is the strongest evidence yet for modelling the
compiler tools in the compiler graph.

---

## Deliverables

- `.tools/comp-which-routing-test.py` — replaced. 3 cohorts, 2 layers, 5 self-controls, mutation test,
  frozen-cohort mode, blob-pinned subject, positive-alibi pollution proof. **Exit 0 / 1 / 2 distinguishes
  "all good" / "the SUBJECT is broken" / "the INSTRUMENT is broken."**
- `org/modules/graph/comp-which-routing-cohort.frozen.json` — the **materialized** cohort (actual probe
  strings, not a recipe). TO-2/TO-3 **re-run against this list; they do not re-derive it.**
- `org/modules/graph/comp-which-routing-baseline.json` — the blob-pinned PRE baseline.

## Blockers

**NONE.** Nothing of mine is blocked.

## Next

1. **[COO~Z]** rule on the two-layer abstain gap (rc=1 vs stdout). **It is TO-2's, not mine.**
2. **[TO-2/TO-4]** the commit-gate polluter (`self_route_verdicts` → 87.6% of the log, re-injected every commit).
3. **[me]** standing by inside the fence. **No comp-which binary edits. No spawns. Zero crons.**
