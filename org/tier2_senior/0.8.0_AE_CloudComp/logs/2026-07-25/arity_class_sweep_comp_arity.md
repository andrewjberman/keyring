# The arity-class sweep: comp-arity, instance 2, and four self-inflicted false-positive classes -- 0.8.0_AE_CloudComp~D

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

Window: ~1828Z -> ~1905Z (follows `pathfix_p1_arity_regression_and_dead_rail_fallback.md`).
1 commit (`57bfd483a`, pushed), 3 MCP messages handled, 0 deploys.

---

## Current State

**CTO~Z's arity-sweep dispatch (182805Z) is CLOSED. `57bfd483a`, pushed.**

**THE ANSWER: there is no instance three in first-party code.**
```
org/  0 | org/modules/graph/  0 | data/  0 | .tools/  0 | infra/aws/lambda/  0
                                                    (MISMATCH + MULTI-ARITY, vendored excluded)
```
The class had exactly two instances. Both are now fixed.

**Built `.tools/comp-arity`** -- an AST sweep for unpack-arity mismatches: a tuple-unpacking call
site whose arity disagrees with the actual return arity of the repo-defined function it calls.
Registered in `excluded_not_graph_use_cases` + `comp-coverage-map.yaml` `meta_tools[]`.

**Instance 2 FIXED** (`tests/test_failure_class_hardening.py:39,52`).
`pii_cli._derive_pseudonymized_fields` has returned 3 since `@2094d30c9b` (2026-07-11); those
sites unpacked 2 for 14 days. **Grounded before claimed** -- "too many values to unpack" is the
SYMPTOM of an arity mismatch, not proof of one, so I read the def (3 returns, all 3-tuples) and
the production site (`:205` unpacks 3) before calling it the same class.
Asserted on the third value: `masking_live` is the REACHABILITY of the serve-time hashing gate.
Assertion is `is not None`, **not** `is False` -- today it IS False (masking retired 2026-04-15
Andrew; handled honestly by the caller, **not a defect**) and pinning that would fail the day
masking is restored. `None` is the dangerous state: if the gate parser breaks, `masking_live`
silently becomes None, the caller fails safe, and nobody learns the parser died.

**Andrew-direct prohibition ACKED, compliance GROUNDED not asserted:**
`git log --author=CloudComp~D -- .../sovereign_held.py` -> EMPTY; `git status` on it -> clean.
`comp-arity` contains no governance/hold predicate (grep for held|sovereign|governance|forbidden
-> no matches). Its only filter is `--include-vendored`, a third-party relevance filter over code
we do not own, not a hold over code we do.

---

## >> FOUR FALSE-POSITIVE CLASSES, ALL IN MY OWN TOOL, ALL CONFIDENT, NONE ERRORED <<

I only reached "0" by disbelieving my own instrument four times. Each is recorded at its site in
the source rather than quietly fixed.

1. **BASENAME COLLISION -> A CROSS-FIRM FALSE POSITIVE.** Keyed the index by basename, so
   `data/black_diamond/.../C_06.client_mix_timeseries.py` (returns 8) and
   `data/cot/.../C_06.client_mix_timeseries.py` (returns 4) collided. cot's def overwrote bd's,
   and the tool reported bd's **correct** 8-unpack as a MISMATCH against cot's arity.
   **The instrument committed a bd<->cot conflation -- exactly what firm separation exists to
   prevent -- and emitted it as a finding against a gold script, on the night of a bd ruling.**
   Caught by grounding ONE finding instead of trusting the count.
2. **METHOD CALLS RESOLVED BY NAME -> ~200 FALSE POSITIVES.** `year, month, day =
   match.groups()` is stdlib `re.Match.groups()`; the resolver matched `groups` against a
   same-named repo function. **Every** first-party "finding" in `infra/aws/lambda` was this.
3. **VENDORED TREES CROSS-RESOLVING.** Several Lambda layers each bundle their own
   scipy/pydantic/sklearn, so same-named functions from different COPIES resolve into each other.
4. **THE SWEEP DIED MID-SCOPE AND PRINTED NOTHING.** `os.walk` enumerates a path `open()` cannot
   read (Windows MAX_PATH, a ~150-char filename under `org/threads/`). FileNotFoundError killed
   the run and produced EMPTY output for that scope -- **indistinguishable from "0 findings" in a
   summary table.** And I guarded ONE of the TWO identical read sites first, so it crashed again:
   **I updated some call sites of a changed contract and not all of them, inside the tool that
   sweeps for exactly that.**

**~200 confident findings -> 0.** Reporting run one would have handed the gate ~200 non-defects
in Lambda code plus a cross-firm claim.

**The generalisable lesson, and it is the same one as the `grep -c` catch in the prior window:**
a positive control proves a tool can FIND; it can never prove a tool is not INVENTING. Defect 1
was invisible to every positive control I had, because the tool was finding something that was
not there. **That asymmetry is why the negative control is now permanent.**

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-arity` (new) | `--self-test` | PASS 3/3 | POSITIVE: pre-`@0e8ea80` -> finds exactly 5 sites at lines 74/79/87/95/103, independently re-derived. DISCRIMINATING: HEAD -> 0. NEGATIVE: bd/cot collision -> 0 false MISMATCH. |
| `comp-arity` | 5 scopes | PASS | 0 MISMATCH / 0 MULTI-ARITY first-party estate-wide. |
| `comp-grep` | `def load_static_tables` | PASS | Found the 2 same-basename defs that exposed false-positive class 1. |
| `comp-glob` | `**/comp-coverage-map.yaml` | PASS | Located the registration surface (via the shim landed earlier today). |
| `.tools/commit-gate.sh` | on `comp-arity` | **FAIL x2, correctly** | Caught (a) `VENDORED_SKIPPED` with no module-level binding -- a latent NameError that worked only by call order; (b) a ruff multi-import. **A gate finding that gets silently fixed teaches nobody**, so both are recorded in-source. |
| `comp-manifest-check` | registration invariant | **BLOCKED, correctly** | Refused an unregistered `comp-*`. Its own text is the session's thesis: *"a tool nobody can find is indistinguishable from a tool that was never built."* |
| `comp-system` | regenerate 06 | PASS | Required by the BLOCKED-ON-PEER-LANDING guard this lane helped build -- the guard fired on my own commit and worked. |

**What worked:** grounding a single finding rather than triaging a count -- that is what exposed
the bd/cot conflation. And the estate's gates: three separate gates (commit-gate, manifest-check,
comp-system) each refused this commit for a *different real reason*, and each refusal improved it.

**What failed:** my own tool, four ways (above).

**Gap found:** `comp-arity` is registered as EXCLUDED rather than routable, following the
comp-residue precedent (full registration without curated comp-which vocabulary just manufactures
a BLOCKED self-route finding). **That is a DEBT, not a resting place** -- it is the same shape as
the Rule-21 dead-fallback break fixed at `@8ec16dff7` four hours ago. Flagged to CTO~Z with a
recommended curated-vocabulary follow-up.

---

## Blockers

**None.**

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** SURFACED, NOT TOUCHED: `.tools/comp-grep` ships a literal
   `--include-held` flag (`:76`) gating a `sovereign-held guard (GG1)` (`:115`, `:122`) -- the
   pattern Andrew's 185538Z ruling prohibits by name, inside the estate's sanctioned search
   primitive, so its denominator is the denominator of everything found through the rail. Guard
   is LOUD (prints `held_note`), so reduced-but-announced, not silent. **Not touched: not
   dispatched, and I cannot tell from outside whether its guard is purely governance or has a
   second non-governance limb fused in -- the `sovereign_held.py` lesson exactly.** If dispatched
   I will SPLIT-then-verify, never rip.
2. **[1.0.0_SA_CTO~Z]** `comp-arity` routable-registration debt (item above).
3. **[1.0.0_SA_CTO]** bd cluster + `sovereign_held.py` -- STOP standing, untouched.
4. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
