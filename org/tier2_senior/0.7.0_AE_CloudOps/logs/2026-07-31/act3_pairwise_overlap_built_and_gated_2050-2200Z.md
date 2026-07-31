# Act 3 pairwise overlap built into comp-blast -- and the metric was wrong three times before it was right

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Serial:** `0.7.0_AE_CloudOps` (base) · **Window:** 2026-07-31T20:50Z -> 22:00Z · **Branch:** CLOUD
**Commits (1 substantive):** `727e5dfb1d`

---

## Summary

Andrew-direct: build the "compare"/pairing functionality into `comp-blast`. Shipped `--compare`
(pair mode) and `--overlap-sweep` (population mode) — the **COMPUTE** and **PROPOSE** halves of act 3.
**ASSESS stays with a human**, which is the control and not a workflow nicety: this is the one
mechanism in the program whose failure is irreversible, because what it proposes is deletion.

---

## What was built

```
comp-blast <A> --compare <B>
comp-blast --overlap-sweep [--population PREFIX] [--min-score] [--min-mass] [--grain] [--head]
```

**The metric is specificity-weighted overlap, not raw overlap, and that was measured before it was
designed.** Over 42 cot gold scripts (25 with consumers, 151 distinct consumers), **six consumer
nodes were each shared by 19 of the 25 producers.** A shared hub is what a pipeline looks like, not
what a duplicate looks like — raw Jaccard emits nearly every pair. Each shared consumer is weighted
`idf = ln(N/df)`, so a consumer written by 112 of 333 producers contributes ~0 while one shared by
exactly two carries the signal.

**Raw Jaccard is still printed beside the weighted score, deliberately.** A reader seeing `0.865`
next to `0.679` watches the hub effect work; a single corrected number would hide it.

**The relation verb is kept.** The graph types every edge (WRITES_S3 / READS_S3 / CALLS / TRIGGERS /
FETCHES) and the default render discards it — P4 of the dial pass. For duplication that distinction
IS the question: two producers **writing** one sink is a single-writer conflict; two scripts
**calling** one helper is ordinary reuse. Shared write targets are surfaced separately.

---

## Deployment Sequence + Verification (AE role addition)

**No AWS deploy.** Repo-side tooling under `org/modules/graph/` — no Terraform/Lambda/EC2 leg, no
`safe-apply`, no deploy-completion ledger opened.

**Verification is the exercised behaviour, actual output:**

```
=== PAIR MODE ===
  gold:A_01.advisor_assignments
  gold:A_02.fee_rate_history
    blast sizes: 48 / 49   shared: 45   union: 52
    jaccard(raw) 0.865   WEIGHTED 0.754   mass 87.15   containment 0.938
    shared BY VERB: READS_S3=9, WRITES_S3=36
    !! SHARED WRITE TARGETS (36) -- 2+ producers writing one sink:
       s3:gold/artifacts/clients_tab.json   (shared by 112 of 333 producers estate-wide)

=== MUTANT 1: strip specificity weighting (idf -> 1.0) ===
  FAILED test_hub_overlap_scores_below_specific_overlap
  FAILED test_ratio_alone_ranks_thin_evidence_at_the_top      2 failed, 6 passed  -> restored green

=== MUTANT 2: disable write-verb separation ===
  FAILED test_write_targets_are_separated_from_reads_and_calls  1 failed, 7 passed -> restored green

=== all four blast suites ===            27 passed in 27.69s
=== exit codes still disjoint ===        phantom 4 / usage 1 / sweep-clean 0
=== Rule 14 commit gate ===              OK: pre-commit gate clean for 2 file(s)
```

---

## Three defects in my own metric, each found by RUNNING it

1. **A ratio needs a magnitude beside it.** The first sweep ranked, at a **perfect 1.000**, pairs of
   functions whose entire blast radius was one shared `log` call. `wi/wu` is scale-free and cannot
   tell "identical" from "standing on a single edge." Added `shared_mass` (absolute summed idf) as a
   second floor; a candidate must clear both.
2. **Scope is not reference.** idf computed inside a 5-node selector made a 112-of-333 hub look
   *rare*, because everything in view shared it. Specificity is an **estate** property — `--population`
   now chooses which pairs are SCORED, while idf always derives from the full grain-matched set.
3. **A denominator that did not belong to its numerator.** With df estate-wide and the slice size
   printed beside it, the tool rendered `shared by 33 of 5 producers`. Caught in my own output, on
   the exact axis I spent the prior window catching elsewhere.

Plus a `NameError` from renaming a parameter and not its two uses — it **failed loud**, which is the
right way to fail, and is why the render is exercised rather than reasoned about.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-blast --compare` | pair mode, new | PASS | exercised on a 48/49-consumer pair |
| `comp-blast --overlap-sweep` | sweep, new | PASS | 1891 pairs scored in 3.3s over 333 producers |
| `comp-blast` (baseline forms) | phantom/usage/clean | PASS | exit codes still disjoint after the new surface |
| `commit-gate.sh` | 2 .py files | PASS | Rule 14, all checks passed |
| `comp-surface-check` / `comp-pulse` | via safe-commit | PASS | no critical surface; reflex clean, measured |

**What worked:** measuring the hub distribution BEFORE choosing a metric. Every design decision here
was made against data — the weighting, the mass floor, and the grain default each exist because a
run produced garbage first.

**What failed:** my own first metric, three times (above). Nothing external failed this window.

**Gap found:** `--all-producers` remains unreachable behind the positional guard. I exempted
`--overlap-sweep` and deliberately did NOT exempt `--all-producers` — it is a separately reported
defect with its own owner, and widening a guard on someone else's behalf is how a scope creeps.

---

## Files Modified

See commit message: `727e5dfb1d`.

| File | Why |
|---|---|
| `org/modules/graph/cli.py` | overlap metric block + `--compare`/`--overlap-sweep`/`--population`/`--min-score`/`--min-mass`/`--grain`/`--head`; `_require_query` exemption for sweep |
| `org/modules/graph/tests/test_blast_overlap_pairwise.py` | NEW gate, 8 tests, mutant-verified twice |

---

## Blockers

**None.** The work was authorized directly by Andrew (~1732Z, "continue identifying how to build in
'compare' or pairing functionality") and COO ruled at 175531Z that it continues under the hard pause,
since a general pause does not silently cancel a specific direct instruction and pairing predates it.

---

## Current State (handoff surface — zero prior context assumed)

- **Pairwise overlap is LIVE in `comp-blast` at `@727e5dfb1d`.** Two modes; both read-only; both
  emit candidates headed `CANDIDATES FOR HUMAN ASSESSMENT, NOT FINDINGS`.
- **The prohibition is honoured structurally, not by disclaimer:** no name, path, or vertical signal
  is computed anywhere — not weighted low, not computed-and-hidden. Only graph edges. `--population`
  is an ADDRESS prefix (a namespace), never a name match.
- **Defaults:** `--min-score 0.30`, `--min-mass 1.0`, `--grain script`, `--head 15`. Every
  suppression prints its count; an empty result explicitly states it is not evidence the estate has
  no duplication.
- **OPEN QUESTION FOR A HUMAN, and it is the interesting one:** on the full `gold:` population at
  `--min-score 0.70 --min-mass 3.0`, **174 of 1891 pairs clear.** That is either a genuinely
  high-duplication surface (many gold scripts do write the same portal artifacts) or the defaults are
  still too loose. **The tool must not answer this** — it is exactly the assessment step reserved for
  a human, and tuning the threshold until the count looks comfortable would be fitting the instrument
  to the desired answer.
- **Not built, deliberately:** no sameness inference, no deletion proposal, no alarm/monitor/pager
  (the moratorium binds hardest where a duplication finding feels most alertable).
- **Regime:** Andrew hard pause on new ESTATE starts. Zero crons. Lane tree clean. Nothing applied
  to AWS this window or the last.

---

## Next Steps

1. **[Andrew]** The 174-of-1891 question above — is that surface real, or are the defaults loose?
   It is an assessment call and the tool is built not to make it.
2. **[0.7.0_AE_CloudOps]** Remaining dial fixes in order: the UnicodeEncodeError itself (the earlier
   fix made the crash SAFE, not absent), `--direction up` inverting `--check-consumers`, the
   substring `matches[0]` ambiguity, the FETCHES upstream gap.
3. **[0.7.0_AE_CloudOps]** Read the DIAL record when P8 + synthesis land (workflow `wonf5bipn`);
   route findings — a read-only fleet's proposals must not become edits without routing.
4. **[2.0.0_SA_COO]** Act 3 v1 first artifact is the candidate list; the mechanism now exists to
   produce it against any bounded population on request.

---

## MCP traffic

None sent this window. Prior window's threads (COO act-3 sequencing 172542Z, hard pause 175531Z,
DIALED-TOOL-FLOW relay 174134Z) remain the governing context; no new dispatches required.
