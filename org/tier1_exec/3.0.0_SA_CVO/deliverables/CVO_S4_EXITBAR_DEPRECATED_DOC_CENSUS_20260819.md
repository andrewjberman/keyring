# §4 EXIT-BAR CENSUS — "no conflicting or deprecated documentation" in the ontology tree

**Author:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Assignment:** NFRA_WORLDMODEL P1 Tranche 1 §4 exit bar (`@df64992815`), CVO verification axis —
CRO-confirmed 194546Z. Gate authority: Andrew-direct `@1044c49f2e`.
**Tree searched, named:** `infra/system/ontology/` — **89 files** (39 `.md`, 27 `.yaml`/`.json`,
23 other). *A clean 404 in the wrong tree is the failure mode this canon has already suffered; every
verdict below names its tree.*

**Pass 1 scope:** the DEPRECATED-TERM axis — estate renames/retirements with known dates, swept
against the tree. Six terms, **96 raw occurrences, 3 real findings.** The gap between 96 and 3 is the
point: a raw grep reports 96 hits and buries the 3.

---

## Method + why the not-defects are half the deliverable

Every occurrence classified against one question: **does this file USE the deprecated name as current,
or does it RECORD it?** A changelog entry, a dated ledger row, and a census capture of a real AWS
resource name are all *correct* — rewriting them would falsify the record. Only current-use is a
defect.

---

## FINDINGS

### F1 — NEW, not in the T-list. `LAYER_FIELD_ANATOMY.md` carries the retired segment name as a live field value.

- `LAYER_FIELD_ANATOMY.md:422` — segment-id enumeration: `partner-data`, `market-intelligence`,
  `interactive-products`, `access-delivery`, **`estate-infrastructure`**
- `LAYER_FIELD_ANATOMY.md:438` — a count row keyed **`estate-infrastructure`** → `sys-estate-ops-platform`, 6

**RENAMED `andrew-infrastructure` 2026-08-12** (Andrew-direct, CRO terminal — *"the audience is the
discriminator"*), and `SYSTEM_DEFINITIONS.yaml:141` already carries the new name correctly.

**T4/F-C scopes the SERVED LADDER DOC only.** This is a different file and it is not on the tranche's
target list — so it would have survived Tranche 1 unchanged.

**The instructive part:** `LAYER_FIELD_ANATOMY.md` is one of the **two files CRO cited as ALREADY
CARRYING the union-find correction** (`:312-313`). **A file corrected on one axis is not a corrected
file.** Any sweep keyed on "which files are fixed" rather than "which claims are fixed" will skip it,
because it is already on the fixed list.

### F2 — NEW, and the sharpest one. A LIVE vocabulary defines its own terms by the behavior of a RETIRED instrument.

`L0B_CHANGE_TYPE_VOCABULARY.md` anchors two change-type definitions to `comp-surface-check`:

- `:118` — *"a versioned source and an invocation input (`comp-surface-check scan`'s graph snapshot: a
  node vanishing is …)"*
- `:150` — `| EMPTY | the referenced thing exists with zero content | comp-surface-check {} case
  (distinct from ABSENT — different code paths, measured) |`

**`comp-surface-check` was RETIRED 2026-08-06** (Andrew-direct: *"I want comp-surface-check retired. i
do not like that tool"*) — binary, registry rows, comp-which route, S3 publish leg, portal CI leg and
pre-commit hook all removed together.

This is **not** a historical citation. It is a **definitional anchor in a live vocabulary**: the
ABSENT-vs-EMPTY distinction is *defined by* what a tool that no longer exists used to do. Nobody can
re-derive it, and the parenthetical *"different code paths, measured"* points at code that is gone.

⛔ **Remedy is RE-ANCHOR, not delete.** The distinction itself is correct and load-bearing — the
estate leans on it constantly (a clean 404 vs a well-formed zero is the difference between absence and
emptiness, and mis-reading it has produced false ABSENT verdicts in this very canon). **Re-anchor it to
a live instrument** (`comp-find`'s MEASURED-ZERO output states exactly this distinction and is
current), keeping the semantics unchanged.

### F3 — NEW, and it changes how F-anything in `10_census/` should be read: the census has NO IN-TREE VINTAGE, and the fold made a stale seed read FRESH.

`worldmodel/10_census/` holds live-shaped AWS state (`instances.json` carries `"state": "stopped"`
per instance; `iam_roles.json`, `re_us-east-1.json` carry ARNs and tags). **Measured:**

- **No in-tree vintage declaration.** No README, no manifest, no as-of header in
  `10_census/` (`cards/ instruments/ parity/ scripts/`).
- **`git log` on the instruments returns `6096e11d95`, dated 2026-08-19** — the *fold* commit
  (`fold(NFRA_WORLDMODEL -> infra/system/ontology/worldmodel)`), i.e. **the date it MOVED, not the
  date it was CAPTURED.**

The census is declared a **SEED + DIFF BASE, 07-31 vintage, never a live read** — **but that
declaration lives OUTSIDE this tree** (the P0 census scoring log). **So a reader inside the ontology
tree has no in-artifact way to learn it, and the freshest available signal — git — says today.**

**This is a staleness signal that now reads FRESH because a move rewrote its apparent age**, which is
worse than an obviously old file: an obviously old file gets checked.

**And it invalidates the confident half of my own census.** 80 of my 96 raw occurrences are
`m365-mcp-gateway` inside `10_census/instruments/`. I classified them NOT-DEFECTS because they are AWS
*physical* resource names in a dated seed — **but I knew the seed date from a memory file, not from the
artifact.** A reader without that context reaches one of two wrong conclusions: that the census is
current AWS state, or that 80 stale names need fixing. **Until the vintage is declared in-tree, both
readings are unfounded — including mine.**

**Recommend:** an in-tree as-of declaration for `10_census/` (capture date + SEED/DIFF-BASE status +
"never a live read"). One file. It converts 80 ambiguous occurrences into 80 correctly-framed ones and
is a precondition for anyone auditing this subtree after me.

### F4 — CONFIRMS T4 / F-C independently (not a new finding)

`C0_C1_C2_C3_C4_SYSTEM_LAYERS.md:12` and `:28` carry `estate-infrastructure` as a current C4 segment
name. Already on the tranche as T4, owner = my slot. Reported so the census is complete, not because it
is new.

### F5 — LOW. Provenance citation that reads as an instruction.

`L0B_CHANGE_TYPE_VOCABULARY.md:86` — *"the pointer inventory is measured, not assumed (`comp-grep` over
23,853 files, positive-controlled for …)"*. **Correct as provenance** — it names the instrument that
performed a past measurement, and rewriting it would falsify the method record. The only risk is a
reader taking it as current guidance when nothing routes to `comp-grep` since 08-07. **A parenthetical
`(now comp-find)` removes the trap without touching the provenance.** Optional.

---

## NOT DEFECTS — with the reason each survives

| Occurrences | Where | Why it is CORRECT |
|---|---|---|
| **80** `m365-mcp-gateway` | `10_census/instruments/*.json`, `cards/S3_BUCKET_DECK.md:205` | These are **AWS PHYSICAL resource names** — `m365-mcp-gateway-role`, `-profile`, `-waf`, `-alb-sg`, the ALB listener-rule ARN. The 08-14 rename was **logical** (service → `opal-gateway`); the AWS resources were not recreated. **Rewriting them would falsify the census and break the join to live AWS.** *(Framing depends on F3 landing.)* |
| **2** `comp-semantic-estates` | `SYSTEM_DEFINITIONS.yaml:24`; `worldmodel/00_framework/CANON_ALIGNMENT.md:19` | Both **record the rename**. The changelog entry explicitly explains that real-world dashed names *"are unchanged on disk and remain reachable"* — a deliberate, reasoned reference. |
| **2** `estate-infrastructure` | `worldmodel/20_rulings/RULINGS_LEDGER.jsonl:47,68` | **Dated ledger rows, ts 2026-07-30** — predating the 08-12 rename. An immutable record of what a thing was called when the ruling was made. **Rewriting history to match a later name is the defect, not the fix.** |
| **2** `estate-infrastructure` | `SYSTEM_DEFINITIONS.yaml:18,141` | `:18` is the changelog entry **recording** the rename; `:141` uses `andrew-infrastructure` as current **and cites the old name as its provenance.** Exactly right. |
| **0** `comp-glob` | — | Clean. |

---

## Verdict on this pass, and what it does NOT cover

**Pass 1 (deprecated-term axis): 3 actionable findings + 1 confirmation + 1 optional.** Two of the
three (F1, F2) are outside the tranche's target list and would have survived Tranche 1; **F3 is a
precondition for auditing `10_census/` at all.**

⛔ **THIS IS A FLOOR, NOT THE EXIT BAR.** The bar is *"no conflicting or deprecated documentation
remains"* and this pass swept **one axis with six known terms.** It does not cover:

- **conflicting** (as opposed to deprecated) content — two live docs asserting different things, which
  is the F-A/union-find class and needs a claim-level comparison, not a term sweep;
- deprecated terms **I did not think to list** — my sweep is bounded by my own recall of estate
  renames, and *that is precisely the blindness the T11 delta-map predicts*;
- stale **version pins** and **hand-typed counts** (T2/T5's axis), swept separately;
- the `worldmodel/` subtree's own internal consistency post-fold.

**The honest denominator of this pass is 6 terms, not "the deprecated class."** A second pass should
derive its term list from a source rather than from me — the naming-act entries in
`SYSTEM_DEFINITIONS.yaml`'s changelog are themselves an enumeration of renames, which makes the term
list **derivable instead of recalled.** That is the same *gate-derived-denominator* fix I pressed on
O2, applied to my own instrument.

---

# PASS 2 — derived term list (CRO-approved 195537Z)

**Method:** 17 changelog entries parsed from `SYSTEM_DEFINITIONS.yaml`; **5** carry a
RENAME / RETIRE / DEPRECATE / SUPERSEDE token; the retired-CONCEPT list falls out of them —
`Territory` (retired v2.0), `attribution` (retired vertical v1.4), `find-insure-serving` → `insurance`,
`value-parity` → `ops-internal`, `contract_record` (retired sense v1.7).
**Swept: 136 raw occurrences. Result: ZERO NEW DEFECTS.**

All 136 fall into three correct classes:

- **(a) AWS PHYSICAL resource names** in `10_census/instruments/` — IAM roles `opal-cot-value-parity`,
  `opal-inf-value-parity`; Lambda `yang-generate-holdings-attribution`. *(Pass 1's F3 fix landed
  between passes and made this class **derivable by the next reader** instead of trusted from my
  memory — the fix paying off on the very next pass.)*
- **(b) Entries RECORDING the retirement** — best specimen `LAYER_FIELD_ANATOMY.md:391`:
  `count_checksum: 29 # 27 - attribution (RETIRED 07-30) + etf-reports + ceo-digest + ticketing`,
  the retirement shown as arithmetic.
- **(c) A DIFFERENT LIVE SENSE of the same word** — `SYSTEM_DEFINITIONS.yaml:459` uses *attribution*
  for an INF served-field definition, unrelated to the retired vertical.

## The yield: recall improved, and PRECISION is the binding constraint

Deriving the list made the sweep **complete**. It did nothing for the thing that decides each verdict,
which is **SENSE** — and measured across the derived list, **every retired term has at least one live,
unrelated sense in the same tree.**

**`territory` is the specimen.** Retired as a classification axis at v2.0. **34 occurrences: one is
the doctrine phrase "map, not the territory"; ~30 are a live, load-bearing GRAPHLEARNS concept** —
*"territory predicate"*, *"residue = declared territory − produced nodes, derived not guessed"*,
*"territory=0 read as a measurement"*. Current, valuable, unrelated to the retired enum.

⛔ **THEREFORE THE §4 BAR IS NOT TERM-CHECKABLE.** *"No conflicting or deprecated documentation"*
requires per-occurrence sense adjudication, and **no completeness improvement to the term list changes
that.**

## Finding against a PROPOSED mechanism (§3 candidate (b), the digit/term lint)

**A naive deprecated-term lint would fire ~30 false positives on `territory` alone**, against a
concept the tree depends on. **A lint at that false-positive rate does not get tightened — it gets
ignored**, and an ignored gate is worse than none because it reads as coverage. If (b) proceeds it
must be **sense-aware**, or scope-limited to terms with no live homonym — which on this evidence may
be an empty set. *Not a design proposal: a measurement that falsifies the naive form before it is
built.*

## One adjudication question — surfaced, not decided

`territory` was **retired as a term** at v2.0 and is **simultaneously the core noun of a live concept**
in the same tree. Either (i) a one-word-two-things collision needing adjudication, or (ii) two
legitimately distinct senses where the retirement bound only the classification axis. **The changelog
retired a term and did not say which SENSES it bound** — which is what leaves it open. A Rule-24
naming call at CRO's seat or Andrew's, not mine. If (i), the GRAPHLEARNS material needs a different
noun; if (ii), the retirement entry should say so, so the next sweep — human or lint — does not
re-raise it.

## Both passes: what remains

The **CONFLICTING** half of the bar (two live docs asserting different things — the F-A/union-find
class) is **untouched by both passes**. It needs claim-level comparison, not term sweeping, and it is
where the bar actually lives. Proposed cut, for CRO: key it off the registry's **CITED-source pairs**
— where a doc restates a value a named source computes, compare them — so the pass has a derivable
denominator the way pass 2 did, rather than resting on free-text reading.

— 3.0.0_SA_CVO
