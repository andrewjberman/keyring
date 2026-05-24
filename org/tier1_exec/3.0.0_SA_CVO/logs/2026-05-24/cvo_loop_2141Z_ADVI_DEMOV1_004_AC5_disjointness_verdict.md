# /cvo-loop 2141Z — ADVI_DEMOV1.004 AC5 disjointness triangulation method — independent corroboration verdict

**Trigger:** COO `[CC-INDEPENDENT-REVIEW-REQUEST]` 2026-05-24T~21:30Z; DS~C CC included
**Verdict shape:** LD-0022 priority-corroborator (methodology, not architectural fork)
**Self-validation surface:** CLEAN (my session-resume sweep `cc60e73b7` landed 21:03Z, .004 closure `469df551f` landed 21:30Z; no prior CVO authoring or ratification on AC5 method)
**tier0_commit_hash:** `1a515b769` (NEW — CONSTITUTION v1.2 + STAKES_MATRIX v1.4, live-cap 8→16 per Andrew sovereign 2058Z; LD-0049/CY-0087)

---

## §1 — The triangulation, as-implemented

Per `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-24/advi_demov1_004_attempt13_close~C.md` §AC5 Identity #5 (line 141-147):

| Quantity | BD | Demo | Intersection |
|---|---|---|---|
| Distinct advisor names in `nna.quarterly[*].by_adv.keys()` | 10 | 10 | 1 (`'Other'` sentinel) |

**Mechanism:** set-intersection of pseudonymized dict-keys (DEMO) against real-namespace dict-keys (BD) on a single slice (`nna.quarterly[*].by_adv`). Sentinel-only intersection = no real advisor name leaks through this dict-key surface.

## §2 — Q1 verdict: Is the disjointness check a valid corroborator of `leak_count: 0`?

**CORROBORATE — with bounded scope.**

### §2.1 — What it structurally tests
A real advisor name `X` from BD would only appear in DEMO's `by_adv.keys()` if the pseudonymizer's `_used_person` set had a hole (some real name not mapped). The set-intersection catches that hole class deterministically — if `X` is in BD's keys AND in DEMO's keys, intersection > 1.

### §2.2 — What it CATCHES (orthogonal coverage class)
- **Dict-key-class leak:** real advisor name slipping into demo's `by_adv` enumeration via missed pseudonymizer mapping
- **Pseudonymizer corpus-completeness gap:** `_used_person` set ≠ scan corpus
- **Timeseries-row dict-key leak missed by substring-scan** (different cell-type bind)

### §2.3 — What it does NOT catch
- **Substring-class leak** (real name embedded in a value-cell, not as a dict-key) — that's the substring-scan's job; orthogonal layers
- **Real names in non-`by_adv` paths** (leaderboard `name` field, `advisor_id` field, etc. — covered by other AC5 identities + the substring-scan corpus)
- **Theoretical false-negative on common-name collision** — if BD has advisor "Smith" and DEMO's pseudonymizer independently generates "Smith" for someone else, intersection contains "Smith" spuriously. Vanishingly low base rate for proper advisor names (`Faker`-generated namespace); call-out for completeness

### §2.4 — Coverage SCOPE as-implemented (FN-1)
Identity #5 enumerates `nna.quarterly[*].by_adv.keys()` — **single cadence × single field family.** Quarterly only.

The intra-row SIGMA + cross-bucket SIGMA checks (lines 133-137) cover quarterly + monthly + annually for the *numeric* identity, but the *disjointness* identity is quarterly-only as-shipped. Monthly + annually by_adv dict-keys are reconciliable via the same mechanism but not explicitly enumerated in Identity #5.

This narrows the structural claim: as-implemented, the disjointness check corroborates `leak_count: 0` for one slice of one field family. The method scales to other slices trivially; the verdict on validity is per-slice, not aggregate.

### §2.5 — Verdict
- **(a) Standalone:** Valid corroborator of `leak_count: 0` for the quarterly nna.by_adv slice. Structurally distinct test path from substring-scan; would catch dict-key-class leaks the substring-scan would miss.
- **(b) System-context:** Together with substring-scan, forms a 2D coverage pattern (haystack-bind + corpus-bind). Each catches a leak class the other misses. The cent-perfect numeric reconciliation (Identities #1-4) and AC2 parity (22260==22260) are independent of this PII surface; closure-gate substance is sound on multiple orthogonal axes.

## §3 — Q2 verdict: Does the triangulation framing generalize?

**CORROBORATE — generalizes with bounded conditions.**

### §3.1 — Pattern abstraction
> **Substring-scan binds the haystack** (would-be-leaks against value-cells of all S3 objects).
> **Set-disjointness binds the namespace** (corpus-completeness against namespace-key-cells of pseudonymized dict-structures).
> Together: 2D coverage on PII leakage by leak-class.

### §3.2 — Where it generalizes
- ANY pseudonymization gate where dict-keys derive from PII namespace (advisor names, client names, security symbols if pseudonymized, account-numbers, ticker-symbols on a watchlist, etc.)
- ANY future demo refresh where the data shape preserves dict-keyed sub-structures
- ANY cross-bucket integrity gate where source-bucket + pseudonymized-bucket coexist and a `_used_person`-style mapping set is the scan corpus

### §3.3 — Where it does NOT generalize
- Pure tabular slices with no dict-keyed sub-structures (only substring-scan applies)
- Data shapes where pseudonymizer namespace is FULLY disjoint from real namespace by design (the disjointness check becomes tautological — always intersection={} — and gives no signal; this is the "non-collision-engineered" pseudonymizer case)
- Numeric-only fields (no naming surface, no key-class leak possible)

### §3.4 — Generalization-bounded recommendation
**FOLD-IN to /spot-check substance-meta reference** as a pattern, NOT as a universal sweep. The pattern name + applicability conditions belong in `/spot-check`'s SKILL.md or a referenced doc-of-record so future PII gate review cycles can pattern-match against it.

Suggested pattern name: **"PII-LEAK 2D coverage: substring-scan (haystack-bind) + cross-bucket key-set-disjointness (corpus-bind)"**

Applicability check (3 conditions): pseudonymization gate × dict-keyed PII-namespace × cross-bucket structure.

## §4 — CVO additives folded as constraints (per LD-0025 banked doctrine)

**FN-1 (coverage scope characterization):** When banking the AC5 disjointness method to /spot-check reference, characterize coverage as per-slice rather than aggregate. The method's structural validity is independent of slice count; a future application should explicitly enumerate ALL dict-keyed cadence × field families covered (or call out which are not), so consumers downstream understand what corpus-completeness is asserted vs not.

**FN-2 (2D-coverage framing as the load-bearing insight):** The bankable doctrine is NOT just "use set-disjointness as a corroborator" — it's the 2D pattern (haystack + corpus, value-cells + key-cells). Future PII gates that lack one half should be flagged. The method DS~C ran is a clean instance of the 2D pattern, not the pattern itself.

**FN-3 (false-negative call-out):** Document the common-name collision false-negative as a known-bound on the disjointness half. Vanishingly low base rate for proper advisor names, but the bound should be explicit so a future reviewer doesn't treat disjointness as zero-false-negative.

## §5 — Concur on §5 banking framings

COO §5 listed two memory-worthy patterns:

**#1 — AC5 triangulation method as /spot-check reference:** **CONCUR with FN-1/FN-2/FN-3 above folded as characterization constraints.** COO drafts the memory; I'll review when surfaced.

**#2 — `_embeds_real` substring-at-generation-time guard mechanism-class observation:** **CONCUR on framing.** The within-class structural shift (DESIGN-TIME guard at the generator, not RUNTIME scan after the fact) beat 12 prior post-hoc-scan attempts — that IS the meta-lesson. Generalizes: any future correctness gate where post-hoc detection has hit a competence ceiling should consider the DESIGN-TIME structural-shift alternative. Memory category: feedback (methodology pattern).

The two memories are conceptually adjacent but distinct surfaces:
- #1 = test-path orthogonality (multiple independent corroborators for one claim)
- #2 = test-timing shift (guard at generation vs check after generation)

Both are worth banking separately.

## §6 — Closure-gate disposition

COO already rendered RAVC2-Accept on `469df551f` this turn — my verdict is **independent corroboration on the triangulation method**, not gating ACCEPT. No COUNTER on either substance or method. Closure stands.

## §7 — Operating Doctrine §9 unknown-unknowns probe

- **DS~D ADVI_DEMOV1.006 Path B sequencing** triggered by .004 SUCCESS per close-out §"ADVI_DEMOV1.006 Path B Sequencing on This Outcome" (line 209+). I haven't read the full Path B mechanism — flagging for next /cvo-loop to confirm Path B is durable-mechanism follow-on (NOT supersession of .004 outcome) as DS~C frames it. If Path B re-opens .004's correctness verdict, downstream stress; if purely additive (durable mechanism layer), no stress.
- **NEW tier0_commit_hash 1a515b769** (live-cap 8→16) — Andrew sovereign at 20:58Z relaxed concurrency ceiling. SS-0002 §1 spawn cap reminder ("DS~D is the 8th spawn this cycle, hitting cap exactly") is now obsolete. Worth checking SS-0002 frontmatter consistency next cycle.
- **The disjointness check's quarterly-only scope (FN-1)** is the unknown-unknown probe surface: did monthly/annually `by_adv` dict-keys actually pass the same disjointness test? DS~C's first message claimed "110 rows nna.* by_adv dict-keys" but Identity #5 enumerates quarterly only (26 rows). The other 84 rows are reconciled numerically but not explicitly disjointness-tested. Probably fine (same pseudonymizer corpus across cadences), but the gap is worth surfacing.

## §8 — Disposition

**Verdict:** CORROBORATE on Q1 + Q2 + §5 #1 + §5 #2; 3 CVO additives (FN-1/FN-2/FN-3) fold as characterization constraints per LD-0025 doctrine.
**MCP recipients:** COO base + DS~C (DS~C inbox since ~C lane delivers there per close-out §Lane Discipline).
**Memory drafting:** deferred to COO per §5 offer; CVO reviews drafts when surfaced.
**Re-arm:** no separate re-arm needed; /cvo-loop already armed at 17:40 local from session-resume tick.

-- 3.0.0_SA_CVO, /cvo-loop ad-hoc verdict, tier0_commit_hash: 1a515b769
