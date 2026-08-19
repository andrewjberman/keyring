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

— 3.0.0_SA_CVO
