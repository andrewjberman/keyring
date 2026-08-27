# Session — `0.4.0_DS_ClientPlatform~W` — ETFS_SATELLITES TO-1 + TO-2

**Serial:** `0.4.0_DS_ClientPlatform~W` (lane ~W, seated this session)
**Window:** 2026-08-27 17:37Z – 18:05Z
**Directive:** D4 (SITEZ) · **Project:** `ETFS_SATELLITES` ONLY (Rule 27)
**Archetype:** BUILD-TO-SPEC (two TOs, one round, spec frozen)
**Branch:** SITEZ · **Device:** site Z

---

## Objective

Build `ETFS_SATELLITES.TO-1` (weights from `rebalancer_model_detail`, name→book resolution,
the vintage policy) and `ETFS_SATELLITES.TO-2` (the declared membership registry, nine members,
drift detector) against the cut @`d5b1139e9f` and the decomp @`936b9ae1e9` or later.

Nine acceptance criteria: `SAT-TO1-AC1..AC4`, `SAT-TO2-AC1..AC5`.

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | `comp-which "where is rebalancer_model_detail read or parsed in this estate"` | NEAR-TIE across 3 tools, no silent guess. Routed me to `comp-find`, which is what actually answered. |
| `comp-find` | `comp-find 'rebalancer_model_detail' --files` | **THE HIGH-VALUE RUN.** DENOMINATOR 210 hits / 27,216 files. The `[DEF]` band named the existing silver converter `rebalancer_conversion.py` + `rebalancer_schemas.py` — build-ladder rung 2, and `rebalancer_schemas.py` turned out to carry two documented bytes-vs-PRD deltas I would otherwise have rediscovered by failing. |
| `comp-estate` | `comp-estate --resource rebalancer_model_detail` | **NO CHAIN REFERENCES IT.** A true negative, consistent with `data/assets/**` sitting outside `PIPELINE_MAP`. |
| `comp-pipescript io` | `comp-pipescript io satellites_weights.py --pipeline cot-gold` | **UNKNOWN SCRIPT — and the POSITIVE CONTROL is what makes that readable.** The same invocation on the established sibling `build_dim_model_portfolio.py` returns the SAME "Unknown script in tree". So `data/assets/**` gold scripts are **not in comp-pipescript's DAG at all**; the verdict is a SCOPE fact about the tool, not a defect in my module. Surfaced (item 4). |
| `.tools/commit-gate.sh` | on the 3 `.py` files | **PASS, rc=0 captured BEFORE any pipe.** First run BLOCKED on two unused imports (`Iterable`, `Sequence` in `satellites_weights.py`); fixed, re-run clean. |
| `pytest` | `python -m pytest data/assets/scripts/gold/tests/test_satellites.py` | **24 passed, rc=0 captured before any pipe.** 23 offline + 1 live-S3 `integration`. |
| `proof-of-spec-check.py` | positional, both instances, rc read without a pipe | See "Proof instances" below. |

---

## Work Completed

### 1. `data/assets/scripts/gold/satellites_registry.py` — the DECLARED registry (TO-2)

Nine members, `REGISTRY_VERSION`, `REGISTRY_CLAIM = 'held'`, an **unfilled maintainer slot**
flagged as an open call at Andrew and explicitly **not a build gate**, the exclusions recorded
with their (different) reasons, the `SAT-b-5` render decision as its own constant with its own
claim, and the build-time drift oracle.

**Placement reasoning, not taste:** membership is a BUSINESS filter, and `rebalancer_schemas.py`
already records the rule for this exact feed — *"`is_opal` is a BUSINESS filter, so it belongs at
GOLD (WS-3), never at silver."* `data/assets/**` is also deliberately outside
`safe_deploy_core.PIPELINE_MAP`, so nothing here auto-deploys on push.

**No monitor, no alarm, no checker, nothing scheduled.** `drift_report` / `assert_no_drift` are
functions a test calls. The moratorium is respected by construction.

### 2. `data/assets/scripts/gold/satellites_weights.py` — the derivation (TO-1)

`hierarchy.children[].relativeAllocation` → per-satellite `{book, weight}`, the declared
name→book map, and the vintage policy. **Writes nothing** — it derives; it does not publish.

### 3. `data/assets/scripts/gold/tests/test_satellites.py` + fixtures

24 tests over all nine criteria. Fixtures are TRIMMED from the measured bronze bytes and carry a
`_fixture_provenance` block (source key, LastModified, byte count, what was trimmed). **All 65
roster rows retained** so the denominator survives the trim.

### 4. The measured picture

```
ROSTER  2026-08-27  pageCount=1  totalResultCount=65  len(pagedResults)=65   FULL COVERAGE
NINE    15[3] 30[4] 40[18] 50[83] 60[81] 70[39] 80[65] 90[0] 98[11]   <- every bracket matches the TO
WEIGHTS 15=ST 1.0 | 30=INT .25/ST .75 | 40=INT .5/ST .5 | 50=INT .75/ST .25 | 60=INT 1.0
        70=CG .5/INT .5 | 80=CG 1.0 | 90=LTA 1.0 | 98=LTA 1.0      all sum to 1.0000
```

---

## Decisions Made

1. **Read BRONZE, not the silver sibling** — `rebalancer_conversion.py` already lands
   `relative_allocation`, which is the build-ladder answer for a normal derivation. `SAT-a-1`'s
   oracle requires **the artifact's own bytes as the exhibit**, and a silver table is a derived
   copy, so reusing it would move the evidence one hop from the thing the oracle names. Recorded
   in the module so nobody "fixes" it later.

2. **Declared my own name→book map rather than importing the MDPF crosswalk.**
   `build_cottonwood_mdpf_slice.py:152-157` already carries these exact prefixed names, and it
   independently corroborates Andrew's `Opal Conservative Growth → LT` ruling. But its values are
   MDPF slugs — a **different vocabulary** from Positioning book codes. Bridging two vocabularies
   through one map arms a latent collision the first time either side adds a key. **Cited as
   evidence, not taken as a dependency.**

3. **`SAT-b-5`: `Opal Satellite 90` RENDERS.** Decided and stated as its own constant with its own
   `held` claim, separable from membership (Rule 24(iii) — folding display into the membership
   enum is exactly how a 0-account book gets decided by accident). Two citable reasons: account
   count never enters the composition arithmetic (90 resolves identically to the 11-account 98),
   and `bookSet.ts` already ruled this shape — *"DECLARED ORDER IS THE FLOOR … every declared book
   always renders."* Marked ratifiable so the maintainer can overturn it deliberately.

4. **Freshness basis = trading-day frontier, selected BY MEASUREMENT.** See Blockers/Findings §2.

---

## Findings

### 1. The `Opal ` prefix silently defeats the portal alias map — found, closed, guarded

`portal/src/lib/modelPortfolioColors.ts` `CANONICAL_MODEL_NAME` is keyed **without** the prefix
(`'Short-Term'`, `'Long-Term Aggressive'`). **Every constituent name in these artifacts carries
it** (`'Opal Short-Term'`). `resolveCanonicalModelName` returns an unknown string **verbatim by
design**, so routing these names through it yields a plausible non-book key and **no error** —
an empty join that reads as *"this satellite has no weights"* rather than *"the key did not
match."* That is precisely the silence `SAT-a-2` is written against. The map is declared against
the artifact's actual name form, and a test asserts the unprefixed keys are ABSENT so it cannot
be "simplified" back to the portal's key form without failing.

### 2. NEVER#1 resolved by measurement, and the measurement CORRECTED my working assumption

I did not assume the cadence. Measured against the live bucket: **2026-08-22 (Saturday) and
2026-08-23 (Sunday) BOTH carry the full detail artifact** — 8002 bytes each, `LastModified`
~06:00Z via `s3api` (UTC; the decomp's "~02:00Z" is the same instant in ET). **This feed lands
every calendar day, weekends included.**

That measurement is what SELECTS the basis. A calendar-day check would alarm on a Saturday for a
feed whose business content cannot have changed. The trading-day frontier is correct on both arms
with **no special case**: on Saturday `expected_last_trading_day` returns FRIDAY, so Friday's data
reads FRESH — *Friday IS Monday's answer*, mechanically. `freshness_basis` rides on the face of
every result so no consumer has to guess which clock produced the verdict.

### 3. The trailing-number mutant is WORSE than the TO stated — a third row, measured

The TO named the `Core | Satellite 98` (9) vs `Opal Satellite 98` (11) collision. Running the
mutant predicate rather than describing it found **`Passive 98`** — a book from an unrelated
family entirely. Rows ending `98` are three, not two. Only the anchored canonical form separates
all three, and that is now asserted as a set intersection rather than left as prose.

### 4. Three guessed constants failed their own tests, and that is the record

My first test run had **3 failures, all mine** — `constituent_rows == 14` (it is **13**: five
members carry one child, four carry two) and the two-element trailing-`98` set. Each was a
number I wrote from expectation instead of measuring. They are recorded here because the
corrected values in the deliverable now read as if they were always measured, and they were not.

---

## Files Modified

| path | state |
|---|---|
| `data/assets/scripts/gold/satellites_registry.py` | NEW |
| `data/assets/scripts/gold/satellites_weights.py` | NEW |
| `data/assets/scripts/gold/tests/test_satellites.py` | NEW |
| `data/assets/scripts/gold/tests/fixtures/satellites/roster_2026-08-27.json` | NEW (trimmed, provenance on face) |
| `data/assets/scripts/gold/tests/fixtures/satellites/detail_2026-08-27.json` | NEW (trimmed, provenance on face) |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ETFS_SATELLITES.TO-1_PROOF_OF_SPEC.json` | NEW |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ETFS_SATELLITES.TO-2_PROOF_OF_SPEC.json` | NEW |

---

## Blockers

**None.** Nothing in either TO was blocked, and nothing was waited on.

⚠ **One DEPENDENCY that is not a blocker: `SAT-a-4` (delivery form) is `2.0.0_SA_COO~Z`'s unmade
call.** TO-1 §4 says *"do not pick the form yourself; if it is unmade when you need it, ask, do
not assume."* I did not need it: the derivation is written **indifferent to the carrier** — it
returns a value, it does not choose a delivery mechanism. **But it constrains whoever picks:** a
build-time constant would carry the vintage of the BUILD rather than of the data, so `vintage()`
would be measuring the wrong clock while still returning FRESH. That residual is stated in the
module and in the proof instance, and the staleness arm must be re-exercised at that boundary.

---

## Current State

Both TOs BUILT. 24 of 24 tests pass including the live-bytes arm. Both proof instances written
and validated. Commits are LOCAL — `0.0.0_AB_MSTR~Z` is the integrator and pushes.

Nothing is owed to me and nothing is held by me.

---

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** `SAT-a-4` — the delivery form, with the build-time-constant caveat above.
2. **[Andrew, via `2.0.0_SA_COO~Z`]** the registry MAINTAINER NAME — a shipping condition, **not a
   build gate**, and it must not be relayed as one.
3. **[`0.4.0_DE_ClientPlatform~Y`]** surprise item 2 below reaches their TO-4 surface directly.

---

## Surprise-channel items — filed to `3.0.0_SA_CVO~Z`, cc `2.0.0_SA_COO~Z`

1. **OBSERVATION / INERT — TO-2 §7's routed `components[]` question is ANSWERED by measurement.**
   §7 asks whether `hierarchy.components[]` is *unused or unpopulated* ("`list[0]` — empty on
   every model read"), noting those take different remedies. **It is NEITHER.** It is empty on the
   **root Strategy node** and **populated on the depth-1 Model children** — 16 to 20 security
   leaves each across all nine satellites. Corroborated by an independent instrument:
   `data/assets/scripts/silver/rebalancer_schemas.py:19-24` documents exactly this shape
   (*"'Opal Satellite 70' (Strategy) has children=[…] and components=[]; 'Opal Conservative
   Growth' (Model) has children=[] and components=[15 leaves]"*). The "universally empty" reading
   came from looking only at the root. No action taken; the question is closed, not opened.

2. **OBSERVATION / INERT — but it lands on `0.4.0_DE_ClientPlatform~Y`'s TO-4 surface, so it is
   filed promptly.** The bronze detail artifact **does** carry a `firmId` — `hierarchy.firmId =
   4175` on all nine satellites. `SAT-c-1`'s "ZERO firm-id references" is about the **Positioning
   directory**, and remains true. ⛔ **This is NOT the viewer-firm source `modesFor(firm)` needs,
   and its danger is that it looks like one:** it is the model's OWNING firm, it is the SAME
   constant 4175 across all nine, and a gate wired to it would gate nothing or gate everything
   while typechecking cleanly. Surfacing it so it is dismissed deliberately rather than found and
   trusted. **No action taken and none proposed** — TO-4 is not my lane.

3. **OBSERVATION / INERT.** The decomp records the partition landing "~02:00Z"; measured via
   `s3api` (UTC) it is ~06:00Z. Same instant, different zone — not a discrepancy, but the vintage
   policy states its basis explicitly so the two never get compared as if they were one clock.

4. **OBSERVATION / INERT — a tool-scope gap, for `1.0.0_SA_CTO~Z`.** The DS compiler-tools mandate
   requires `comp-pipescript io <script> --pipeline <tree>` for *every gold script touched*.
   `data/assets/**` gold scripts are **not in any comp-pipescript tree** — established with a
   positive control (the established sibling `build_dim_model_portfolio.py` returns the same
   "Unknown script"). The mandate is therefore **unsatisfiable for this directory**, which is
   consistent with `data/assets/**` being deliberately outside `PIPELINE_MAP`. No action taken.

-- `0.4.0_DS_ClientPlatform~W`
