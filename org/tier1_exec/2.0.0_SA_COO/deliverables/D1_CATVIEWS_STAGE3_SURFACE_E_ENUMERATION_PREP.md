# D1_CATVIEWS stage 3 — surface (e) PRODUCER RESOLUTION: enumeration prep

**Owner:** `2.0.0_SA_COO` (stage-3 decomp owner). **Status:** PREP, not the decomp. Captured so the
measurement is not re-derived.
**Why (e) first:** it is the surface Andrew's word and the 15/85 incident actually named, and the PRD
declares its population by example (*"`build_cottonwood_mdpf_slice.py` … **and their siblings across
firms**"*) rather than by enumeration. **An unenumerated "and siblings" is the thing stage 3 exists to close.**

---

## 1. Two instrument classes, denominators printed

| # | Instrument | Scope | Denominator | Verdict |
|---|---|---|---|---|
| I1 | `comp-find -i` on the **named tokens** (`CANONICAL_KEY`, `INCOME_NON_MODEL_NAMES`, `PENDING_RULING`) | `data/` | **44 hits / 1,086 files** | **FLOOR ONLY** — see §2 |
| I2 | **SHAPE pass** — module-level `UPPER_CASE` name-map literals, filtered to vocabulary-shaped names | `data/{mdpf,assets/gold,cot,inf,black_diamond}/scripts` | **457 .py scanned → 54 files carry one** | the real population |

⛔ **I1 IS A FLOOR AND IT ALREADY CONTAINS A FALSE POSITIVE.**
`data/black_diamond/scripts/silver/inject_scoped_overrides.py:55` —
`CANONICAL_KEY = "silver/prices/canonical_prices.parquet"`. **Same token, entirely different meaning: an S3
key string, not a vocabulary map.** A census keyed on the token would have counted it as a hand vocabulary.

**I1 found the vocabulary in 3 Cottonwood files** (`build_cottonwood_mdpf_slice.py` defines it;
`build_cottonwood_mdpf_pair.py` and `build_cottonwood_interpolated_backfill.py` import it). **Read alone,
I1 says the hand vocabulary is Cottonwood-only. That reading is wrong.**

---

## 2. The "siblings across firms" are REAL but the PRD's axis is MISNAMED

The siblings are **not primarily per-FIRM.** I2 found the same *shape* — a hardcoded model-name→key or
key→display map — across **three different axes**:

| axis | instances |
|---|---|
| **per-FIRM (live)** | `build_cottonwood_mdpf_slice.py` — `CANONICAL_KEY` (the one the PRD names) |
| **per-VINTAGE (backfill/legacy)** | `build_legacy_compat_emit.py` `ECLIPSE_NAME_TO_KEY` · `build_mdpf_count_backfill_pre0518.py` `LEGACY_NAME_TO_MODEL_KEY` · `build_mdpf_process_backfill.py` `MODELNAME_TO_KEY` · `build_mdpf_v0_bandaid_backfill.py` `MODEL_SERIES_TO_KEY` — **FOUR** |
| **per-SERVED-ARTIFACT** | `dim_mdpf_aum_metrics.py` + `dim_mdpf_aum_timeseries.py` — `SERVED_MODEL_NAME` in **both**; plus `INFLECTION_MODEL_KEYS`, `ROSTER_MODEL_NAME` |

**This matters for the cell:** a cell scoped to *"per-firm hand vocabularies"* would enumerate **one** and
miss six. **The axis is HARDCODED-MODEL-VOCABULARY, and FIRM is only one of its three values.**

---

## 3. ⛔ A DIVERGENCE I ALMOST FILED AS A DEFECT — AND IT IS BY DESIGN

`SERVED_MODEL_NAME` exists in **two** builders with **different content**:

| file | entries | sha |
|---|---|---|
| `dim_mdpf_aum_metrics.py` | **7** (the 5 archetypes **+ `opal_blend_5050_int_ltc`, `opal_blend_5050_st_int`) | `3ba967413f043478` |
| `dim_mdpf_aum_timeseries.py` | **5** (the archetypes only) | `54a315efe96b00a3` |

**Every structural signal said "one logical producer, two independently-editable homes"** — the class
CLAUDE.md names, where *"a filename-resolved check … reads CLEAN where two copies have silently diverged."*

⛔ **IT IS NOT THAT. BOTH FILES DOCUMENT THE DIFFERENCE AT THE DEFINITION SITE:**
- `dim_mdpf_aum_timeseries.py:59` — *"5 CORE models only (served aum-timeseries by_model = these exact 5;
  NO SMA, NO blend)"*, **verified against the served sample.**
- `dim_mdpf_aum_metrics.py:80-83` — *"the string the legacy aum-metrics.json emits (verified against the
  served sample) … Deliberately NOT the crosswalk display_name … SMAs are absent by design."*

**Each set matches ITS OWN served artifact. Two artifacts genuinely carry different model sets.**

**THE SAVE, AND THE LESSON: STRUCTURAL SIMILARITY IS NOT EVIDENCE OF A DEFECT.** The shape pass is what
*found* the pair; only **reading the definition site** resolved it. Had I filed on the sha difference I
would have manufactured a two-homes incident out of two correct files — on a taxonomy surface Andrew has
just asked to have "figured out," which is exactly where a false finding costs the most.

---

## 4. THE REAL FINDING, which the false one was standing in front of

⛔ **NEITHER BUILDER READS THE RATIFIED REGISTRY. BOTH HARDCODE.**

`mdpf_category_registry.py:100-106` declares `PRIMARY_MODEL_KEYS` — the five archetypes, ratified 08-19.
`dim_mdpf_aum_timeseries.py`'s five keys **are exactly that tuple**. It arrived there **by hand, verified
against a served sample — not by reading the registry.** Neither file references `PRIMARY_MODEL_KEYS`.

**So the alignment is CURRENTLY TRUE AND STRUCTURALLY UNGUARANTEED.** If a sixth Primary archetype is ever
ruled, the registry gains it and **these two files do not** — silently, because each was verified against
a *served sample* that would itself be stale.

**THAT IS SURFACE (e) EXACTLY — *"resolve membership THROUGH the one registry."* The registry is BUILT and
these consumers do not consume it.** The 15/85 hand-map fix is the interim form of the same gap on a
different producer.

---

## 5. Carried into the decomp

- **(e) is bigger than the PRD framed** and its axis is **hardcoded-model-vocabulary**, not per-firm. Cells
  must cover the **vintage** and **served-artifact** values, not just the firm one.
- **A cell for the registry-consumption gap** (§4) — distinct from the hand-vocabulary cell: one is *"the
  map is by hand,"* the other is *"a correct map is not sourced from the ratified one."*
- **Boundary, declared:** the four **backfill/legacy** vocabularies are per-vintage and may be legitimately
  frozen — a backfill of historical data SHOULD use the vocabulary of its era. **Do not reflexively route
  them for registry consumption; that could be the wrong remedy.** Their disposition is a cell, not an
  assumption.
- ⛔ **Do NOT re-open** the stored 5-enum or the ruled Primary/Custom partition (PRD s.8.2, boundary (g)).
