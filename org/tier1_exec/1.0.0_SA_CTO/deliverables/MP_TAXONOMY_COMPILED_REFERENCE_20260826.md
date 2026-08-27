# The Model Portfolios Taxonomy — COMPILED REFERENCE (2026-08-26, `1.0.0_SA_CTO`)

**What this is:** the MP layering framework as Andrew has ruled it across 2026-08-19 → 08-26,
compiled from the ruled records, verbatim Andrew-directs, the PRD, and the shipped registry code —
each element cited to its source. Compiled on his 16:3xZ instruction ("look through logs and records
and try to compile it all... we have gone over this many times"). **This document ADDS no vocabulary
and rules nothing** — it is the existing rulings in one place. Where two records use different words
for one thing, the supersession chain says which governs.

---

## 1. THE TREE, AS RULED

```
L0  (what is PRESENT for the firm):   Client · Models · SMAs · Alternatives
        Insurance EXCLUDED from the MDPF view tree ("we don't take fees on it") --
        it remains a top-level value in the 08-19 REGISTRY taxonomy; the exclusion
        is on the VIEW axis only.                                    [A2 §2; A1]

L1  Client:   "Client - Opal Supervised" / "Client - Opal Unsupervised"
        Discriminator: fee-taking, under the OPAL definition of Supervised (below).
        (08-24 first ruled as "Client Supervised/Unsupervised"; renamed 08-25 --
        supersession chain §3.)                                      [A2 §3; A3; PRD s.8.7]

L1  Models:   Primary / Custom                                       [A2 §4; A5]
L1  SMAs:     Tax · Muni · DIVZ · PFOE  -- "so far, maybe others will eventually
        be added" = an OPEN enumeration; the registry admits additions without a
        code change.                                                 [A2 §5; PRD :57,:297]
L1  Alternatives:  no drilldown yet -- "we will not get into just yet."  [A2 §6]

L2  Models > Primary:  UST · ST · INT · LT · ULT  (the current main five)  [A2 §4; A5]
L2  Models > Custom:   DISCOVERY RULE -- any Opal model that is NOT the Primary
        five ("models that say Opal in them that are discovered",
        e.g. Opal Fixed Income), enumerated at L2 drill.             [A2 §4; A6 verbatim]
```

His 16:36Z restatement (A6) names L0 as "Models SMAs and Client" — consistent with A2's four-value
L0 read as elliptical (Alternatives has no drilldown yet); A2's verbatim carries the full L0 set.

## 2. "SUPERVISED" — TWO MEASURES, ONE GOVERNS HERE (A3, 08-25 ~04:2xZ, verbatim record)

| perspective | definition | governs |
|---|---|---|
| Cottonwood-Supervised | everything the client supervises (the whole ~458M) | `COT_CANON458` — the client's own canonical number |
| **Opal-Supervised** | **DERIVED: the residual account value of any account with Opal Models contained within the portfolio** | **the MDPF/D1 display taxonomy — his explicit word** |

**Label obligation (ruled in A3):** every artifact carrying a "Supervised" figure declares
`supervised_basis: opal-models-residual` vs `client-supervision-fact` on its face.
Predicate spec: `SPEC_COT_OPAL_SUPERVISION_PREDICATE_20260825.md` (DS~F); spec fold ruling:
`RULING_20260825_DSF_OPAL_SUPERVISION_SPEC_FOLD_FOUR_HOMES.md`.

## 3. SUPERSESSION CHAIN (which words govern)

1. 08-19 ruling: `Client = Advised + Residual` (advisory-scope axis) → **08-24 view tree** renames
   the VIEW split to Supervised/Unsupervised with FEE-TAKING as the discriminator (A2 §3) →
   **08-25**: values become **"Client - Opal Supervised" / "Client - Opal Unsupervised"** (PRD
   s.8.7 — the operative values), on the **Opal definition** (A3).
2. The registry code carries BOTH axes deliberately (`mdpf_category_registry.py:84-99`):
   `advisory` (08-19 gate: Advised+Residual) and `fee_taking` (08-24: Supervised+Unsupervised) —
   two axes, not a conflict (Rule 24(iii): different intents).
3. 08-24 "Client Supervised" enum → superseded by "Client - Opal Supervised" (PRD s.8.7 states it
   in terms: "THOSE VALUES ARE SUPERSEDED").

## 4. CUSTOM MODELS — the ruling chain that closed today's blocker

- 08-19 gate + 08-24 view tree: `Models = Primary + Custom`, Primary = the five, Custom = any Opal
  model not those, at L2 drill (A2 §4).
- **08-26 ~15:2xZ (A5): "yes Opal Fixed Income is a 'Model', it is a 'Custom' model, as opposed to
  a 'Primary' Model which comprises of UST ST INT LT ULT"** — supplied the INTENT no instrument
  could reach; unblocked the canonical-key P0 (COO 72417 record; key landed, lambda rebuilt at
  minimal pin, verified).
- 08-26 ~16:36Z (A6): the discovery RULE restated as the Custom membership definition.
- The registry already modeled it: `mdpf_category_registry.py:410` — "'Models' rolls up
  Primary+Custom" — his words supplied the membership rule for an axis the estate had built
  (CVO 72430 §2).
- **Boundary note (engineering seam):** the discovery rule defines TAXONOMY membership; the served
  Global union's canonical-key guard (no-auto-slug) is a SEPARATE standing mechanism — a discovered
  model still gets its served key deliberately.

## 5. THE 08-26 DIVERGENCE, RESOLVED INSIDE THIS FRAMEWORK

The ad-hoc QA fire (his drive-now law) surfaced a cottonwood identity refusal: decomposed
$147.0M vs dim $190.7M (delta $43.7M; 483 vs 489 accounts). Resolved same hour:
- **Re-attribution, not new money** — firm AUM identical to the cent (480,687,460.42) on both
  sides; `MODEL_DETAIL_SCOPE` widened to `Scope="all"` (applied 08-25, running), `fact_model_blend`
  37→117 edges (+80 added, 0 removed) (PartnerETL~A 72575, COO-ratified 72580, CVO cent-exact 72571).
- **His word (A4, 16:34Z): "what is being discovered is the 'Client - Opal Supervised' segment...
  covered in the Taxonomy that we are building for Model Portfolios."** The dim is right; the
  decomposition side learns the segment per THIS framework, not ad hoc.

## SOURCE INDEX (the anchors; each is the citation for the sections above)

| id | artifact | vintage/date |
|---|---|---|
| A1 | `org/tier1_exec/1.0.0_SA_CTO/deliverables/D1_TAXONOMY_GATE_RULING_20260819.md` — the ruled Rule-24 taxonomy (binds) | 08-19 |
| A2 | `.../ANDREW_DIRECT_20260824_D1_VIEW_TREE_L0_L1_L2_CLIENT_MODELS_SMAS_ALTERNATIVES.md` — the view tree VERBATIM | 08-24 ~18:5xZ |
| A3 | `.../ANDREW_DIRECT_20260825_SUPERVISED_IS_TWO_MEASURES_OPAL_DEFINITION_GOVERNS_MDPF.md` | 08-25 ~04:2xZ |
| A4 | `.../ANDREW_DIRECT_20260826_1634Z_COTTONWOOD_DIM_JUMP_IS_CLIENT_OPAL_SUPERVISED_SEGMENT_MP_TAXONOMY.md` @2390e15d90 | 08-26 ~16:34Z |
| A5 | 'Opal Fixed Income' Custom ruling — COO 72417 verbatim record | 08-26 ~15:2xZ |
| A6 | `.../ANDREW_DIRECT_20260826_1636Z_MP_LAYERING_L0_L1_L2_WITH_CUSTOM_DISCOVERY_RULE.md` @0e59cfa58d | 08-26 ~16:36Z |
| — | `docs/architecture/D1_ASSET_CATEGORY_VIEWS_PRD.md` — s.8 pipeline entry; s.8.6/8.7 (:293-320) the operative Client values; :57-62 the composition mapping; :57/:297 SMA members | 08-19→08-25 |
| — | `data/mdpf/scripts/gold/mdpf_category_registry.py` :84-99 (L1 values, two axes), :410 (Models rolls up Primary+Custom) | shipped |
| — | `.../ANDREW_DIRECT_20260824_MODEL_TAXONOMY_BEELINE_D1_PIPELINE.md` | 08-24 |
| — | `workflows/atom_decomposition/runs/d1-catviews/20260824T195537Z/DECOMP.md` — stage-3 decomp v2 (view-tree cells) | 08-24 |
| — | `SPEC_COT_OPAL_SUPERVISION_PREDICATE_20260825.md` (DS~F) + `RULING_20260825_DSF_OPAL_SUPERVISION_SPEC_FOLD_FOUR_HOMES.md` | 08-25 |

Directive homes: **D1** (the taxonomy + views: `D1_CATVIEWS`, active, decomp v2 28→31 cells);
**D8** (the pipeline fortification the served plane rides). Register rows carry both.

---

## 6. AMENDMENT 2026-08-27 ~20:0xZ — THE PER-PARTNER SOURCE MAP, AND WHY THIS AMENDMENT EXISTS AT ALL

**Provenance, stated because it is not first-hand:** Andrew spoke these words at the
`0.4.0_DS_ClientPlatform~Z` terminal, not this one. Recorded verbatim by that seat at
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ANDREW_DIRECT_20260827_PER_PARTNER_SOURCE_TO_TAXONOMY_MAP.md`
**@`45dd4294e7`** and relayed as msg 9923. **This section is a RELAY of a verbatim record, not a
transcription of words this seat heard.** Anyone acting on a fine distinction here reads A7 at source.

### ⛔ HIS PREFACE IS THE MOST IMPORTANT LINE IN IT, AND IT IS A FINDING ABOUT THIS FILE

> *"I have gone through this countless times but I'm going to do it again just to make sure it lands"*

**That is the same complaint behind his 08-26 instruction to `1.0.0_SA_CTO` to compile all of this —
the instruction that produced this document.** So the compiled reference already existed, was already
correct, and he still had to say it again. ⛔ **THE REPETITION IS THE FINDING: this content keeps
failing to persist, and a second correct copy is not the remedy.**

**What is measured, not guessed, about why:** `0.4.0_DS_ClientPlatform~Z` *did* find this file, by
`comp-find`, and confirmed today's words match it on **every overlapping point** — near-verbatim on the
Cottonwood predicate and on the L1 SMA members. **So the failure is NOT discovery and NOT accuracy.**
The content was here, findable, and right. **What this file could never do is tell ANDREW that it was
here** — his only instrument for "did it land" is to say it again and watch what happens. A carrier the
sovereign cannot query is a carrier he must re-send. *(Naming the mechanism; the remedy is a routed
question below, not an edit this seat makes unilaterally.)*

### 6.1 THE MAP — the three partners, source system to taxonomy

```
49 FINANCIAL   Models AND SMAs BOTH from SmartX -- PFOE, DIVZ, + "a handful of tax accounts"
               ("egress permitted" -- his explicit per-use word, for finding those accounts)
               Client = ALL Opal-Supervised, scoped to "the 0824 schwab account which is what
               feeds the portal"
INFLECTION     Models from Eclipse, "already handled on logic".  NO SMAs.
               "any balance is Client Opal-Unsupervised"
COTTONWOOD     Models from Rebalancer (primary/custom established; Opal Fixed Income = custom)
               NO SMAs "in the SMAs as a strategy bucket which is what we've built here"
               Client DERIVED: any portfolio holding an Opal model has its residual as Client
               Opal Supervised; everything else Opal Unsupervised AS THE BOOK-WIDE PLUG FIGURE
```

>> **THE GENERAL RULE, BINDING ALL THREE:** *"Client segment is always **residual post-models and
   smas**."* This is the invariant; the three per-firm rules above are its instances, not exceptions
   to it. <<

### 6.2 ⭐ ALREADY ENCODED CORRECTLY — DO NOT RE-DO THIS WORK

`CLIENT_L1_RULE = {49financial: ALL_SUPERVISED, inflection: ALL_UNSUPERVISED, cottonwood: DERIVED}`
is an **exact match** to his three rules (measured by `0.4.0_DS_ClientPlatform~Z`). **NO REGISTRY EDIT
IS IMPLIED.** ⛔ Second sovereign statement in two turns that CONFIRMS the shipped shape — and **the
available error is to read a confirmation as a change order and re-do encoded work.**

### 6.3 ⛔ THE SUBSTRATE COLLISION HIS MAP CREATES — measured by `2.0.0_SA_COO~Z` at `s3api`, msg 9943

`opal-data-assets` partitions by **SOURCE SYSTEM**, not by firm — and the source systems do **not agree
with each other**:

```
smartx/        account/ allocation/ model/ platform/     <- BY FUNCTION. NO FIRM PREFIX AT ALL.
eclipse/       inflection/                               <- BY FIRM
blackdiamond/  49f/  49financial/  cottonwood/           <- BY FIRM, and BOTH 49f/ AND 49financial/
```

>> ⛔ **HIS MAP PUTS 49 FINANCIAL'S MODELS *AND* SMAs IN SMARTX, AND `smartx/` HAS NO FIRM BOUNDARY IN
   ITS PREFIX TREE. A KEY-PREFIX IAM CONDITION CANNOT ISOLATE WHAT HAS NO PREFIX TO CONDITION ON.** <<

**This corrects a claim `1.0.0_SA_CTO~Z` made to Andrew ~20:1xZ.** That claim said the `CLAUDE.md`
NEVER rule's bucket-scoped Deny fails on a shared substrate because isolation becomes a *key-prefix +
IAM-condition* problem. **The diagnosis was right and the named remedy is UNBUILDABLE FOR AT LEAST ONE
FIRM** — the one whose data is most spread. **THREE PARTITION SCHEMES IS NOT ONE SUBSTRATE WITH A
MOVING SHAPE; IT IS THREE SHAPES ALREADY.** `POSN_TENANCY`'s "do not couple to the substrate's current
shape" therefore binds harder than its author knew when he wrote it: there is no single current shape
to couple to.

### 6.4 EGRESS — AUTHORIZED, PROBABLY UNNEEDED

*"(egress permitted)"* is his explicit per-use word for locating the 49F tax accounts. **But SmartX is
already landed in our own S3** (`smartx/platform/silver/fact_allocation_account_map/`, read by
`runners_49f/a00_runner.py:55`). **Prefer the landed artifact; keep the grant unspent unless the
internal read falls short.** An authorization is not an instruction to use it.

### 6.5 SOURCE INDEX ADDITION

| A7 | `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ANDREW_DIRECT_20260827_PER_PARTNER_SOURCE_TO_TAXONOMY_MAP.md` @`45dd4294e7` — the per-partner source map VERBATIM (recorded at the DS~Z terminal) | 08-27 ~20:0xZ |
| A8 | `2.0.0_SA_COO~Z` msg 9943 — the `opal-data-assets` three-scheme partition measurement (`s3api`, COO's own seat) | 08-27 ~20:2xZ |
