# NFRA_DEBTSCAN TO-D2X — DS lane composition follow-up (inf / cot / mdpf), UNKNOWN-VINTAGE caveat lift

**Lane:** DS (0.4.0_DS_ClientPlatform) | **Driver:** COO [DRIVE] GO 20260612T192948Z
**Run:** 2026-06-12 ~19:30–20:05Z | **Posture:** READ-ONLY (zero mutations; Rule 13 untouched)
**Predecessor:** `2026-06-12_D2_composition_ds.md` (bd legs FRESH; inf/cot/mdpf filed UNKNOWN-VINTAGE)
**Unblocked by:** NFRA_DEBTSCAN.TOOL-01 (AE 0.6 `b5050f6b2`) — `comp-pipescript deployed --firm {inf,cot,mdpf}`
**Binding doctrine:** freshness-bound; CVO ≥0.8 precision gate before promoting above ADVISORY.

---

## 1. Headline

The **freshness/UNKNOWN-VINTAGE caveat is LIFTED** for inf/cot/mdpf — TOOL-01's `deployed --firm`
gives real per-tree S3 vintage (all MATCH except the 3 already-filed mdpf MISSING). **D2-DS-01 confirmed CLOSED.**

But lifting the vintage caveat exposed a **different, honest coverage gap**: the *other two* D2
composition subcommands (`io` column-gaps and `postdeps`) were **never extended past bd/inf** the way
`deployed` was. So the cot/mdpf composition legs are now **vintage-KNOWN but tool-UNCOVERED** — I am
replacing the vintage caveat with an accurate tool-coverage caveat, not a blanket "CLEAN everywhere."
This is the same enumeration-gap class TOOL-01 fixed for `deployed`, now found in `io` + `postdeps`.

A naive re-run reports "0 column gaps, all trees CLEAN." That is **false for cot/mdpf** — the io
detector silently returns "Unknown script" for scripts it has no graph for, which a GAP-grep counts as
"no gap." Verified by header inspection (`--pipeline cot-gold` prints `[bd-gold]`) + Unknown-script
accounting.

---

## 2. Provenance / freshness header (vintage caveat LIFTED)

| Tree | Freshness source (TOOL-01) | Result | Vintage |
|---|---|---|---|
| inf-gold (+silver) | `comp-pipescript deployed --firm inf` → s3://opal-data-inf | **61 MATCH / 0 STALE / 0 MISSING** | FRESH (known) |
| cot (gold+silver+bronze) | `comp-pipescript deployed --firm cot` → s3://opal-data-cot | **47 MATCH / 0 STALE / 0 MISSING** | FRESH (known) |
| mdpf | `comp-pipescript deployed --firm mdpf` → s3://opal-data-mdpf | **15 MATCH / 0 STALE / 3 MISSING_ON_S3** | known (3 stranded — see below) |

mdpf 3 MISSING_ON_S3 = `build_mdpf_inflection_history_from_spine.py`, `build_mdpf_wsc_inflection_nonmodel_backfill.py`,
`patch_mdpf_per_date_partitions.py` (all `backfill/` layer). **Already filed = TOOL-01-F01** (ledger
`2026-06-12_TOOL01_completion_ae06.md`), owner AE; stranded-deploy candidate (dual mdpf S3 layout). Not
re-filed here; counted as a known staleness finding, not a column-gap FP.

---

## 3. Family: comp-pipescript io — COLUMN GAPS ($0-metric class)

Swept per-script with **honest Unknown-script accounting** (an "Unknown script" return = the io graph
has no manifest for that script → UNCOVERED, NOT clean):

| Tree | Total IDs | Genuinely analyzed | Column gaps | Uncovered (Unknown) | Leg verdict |
|---|---|---|---|---|---|
| inf-gold | 47 | **46** | **0** | 1 | CLEAN (real inf graph) |
| cot-gold | 43 | 28† | 0† | 15 | **UNCOVERED** (see D2X-DS-02) |
| mdpf | 18 | **0** | 0 | **18** | **UNCOVERED** (no mdpf io graph) |

† cot's "28 analyzed" is misleading: `comp-pipescript io --pipeline cot-gold` **falls back to the
bd-gold 29-ID canonical graph** (manifest header prints `[bd-gold]`; valid-ID list = bd's A_00…D_04).
So those 28 manifests describe **bd scripts**, not cot's; the 15 cot-specific scripts (E_*, gldinc_p1_shadow,
validate_sl_nightly_gate, diag_gold_silver_recon, gold_prof, runner-telemetry, validate_platinum_consistency)
return "Unknown script." Genuine cot-script column-gap coverage ≈ **0**. Confirmed across
`--pipeline {cot-gold,cot,all,mdpf}` — all return Unknown for cot/mdpf-specific IDs.

**inf column-gap result: CLEAN (46/47 analyzed, 0 gaps).** cot/mdpf: not assessable with current tooling.

---

## 4. Family: comp-pipescript postdeps (missing post-step class: $22M phantom-override)

`comp-pipescript postdeps` hardcodes the bd config (`pipeline_cli.py:2321` →
`data/black_diamond/scripts/gold/gold_pipeline_deps.yaml`). It **does not read** inf's
`data/inf/scripts/gold/orion_pipeline_deps.yaml` or cot's `data/cot/scripts/gold/gold_pipeline_deps.yaml`.
So the tool's postdeps view for inf/cot is structurally bd-only (= D2X-DS-01). Read the inf/cot configs
directly instead:

| Tree | Deps config | Guards present | Gap |
|---|---|---|---|
| inf | `orion_pipeline_deps.yaml` | B_03→C_00 (AUAGAP.002) | canonical_prices→inject ABSENT — **MOOT** (inf inject is v1 stub no-op; see FP below) |
| cot | `gold_pipeline_deps.yaml` | build_canonical_prices_v2→inject (+ dim_advisor_office preconds, B_00 hybrid_price_fill precond) | **fork-shadow orphan** (D2X-DS-03) + **missing B_03→C_00** (D2X-DS-04 candidate) |
| mdpf | (none) | — | N/A — no deps config; mdpf is backfill/feeders shape |

---

## 5. Findings ledger {id, class, finding, verdict, owner}

### D2X-DS-01 [tooling-debt] — `comp-pipescript postdeps` is bd-only — **REAL**
Hardcoded to the bd yaml (`pipeline_cli.py:2321`); blind to inf/cot deps configs that exist on disk.
Same enumeration-gap class as the now-fixed D2-DS-01 (`deployed` bd-only). Owner: CTO/AE (tool extension —
`--firm`/config-discovery for postdeps). Severity: ADVISORY (no live data impact; coverage blind spot).

### D2X-DS-02 [tooling-debt] — `comp-pipescript io` has no cot/mdpf column-gap graph — **REAL**
io builds graphs for bd (29 canonical IDs) + inf only. `--pipeline cot-gold` silently falls back to the
bd graph; mdpf has no io graph at all (0/18). cot/mdpf gold scripts cannot be column-gap-analyzed →
the $0-metric detector (geo_drill / fee_earning_aua class) is structurally blind on those trees. Sibling
of D2X-DS-01. Owner: CTO/AE (tool — add cot/mdpf io graphs, mirroring TOOL-01's deployed extension).
Severity: ADVISORY. **Material:** it falsifies any "cot/mdpf 0 column gaps CLEAN" claim (incl. this
sweep's naive first pass + the predecessor ledger's cot leg).

### D2X-DS-03 [config fork-shadow] — cot deps config carries a bd orphan guard — **REAL (low-sev)**
cot `gold_pipeline_deps.yaml` declares `build_canonical_prices_v2.py → inject_scoped_overrides.py`
[BLOCKING] with bd's **verbatim** incident text ("2026-04-06 BNP PARIBAS SA override wiped, +$22M
phantom value in **Delaney** account" — Delaney is a *bd* account). But cot has **no
`inject_scoped_overrides.py`** anywhere under `data/cot/scripts/` and **no `price_overrides.json`** → the
guard references a script that doesn't exist in the cot tree = bd→cot fork-shadow orphan (dead config).
Matches the known bd→cot fork-shadow class (`memory/feedback_bd_cot_fork_validate_config_stale_shadow`,
NFRA_COT_TOOLING `6bc1f1ce3`). Owner: DS (cot config cleanup — remove or replace with a real cot stanza).
Severity: ADVISORY (cot nightly runs fine; not live-breaking — orphan/dead, not active).

### D2X-DS-04 [config gap] — cot missing the B_03→C_00 AUAGAP guard — **CANDIDATE**
Both bd and inf deps configs carry the `B_03.account_gains → C_00.canonical_performance` [BLOCKING]
guard (AUAGAP.002: a partial rerun stopping at B_03 leaves canonical_performance stale). cot's config
**omits it**, despite cot having both `B_03.account_gains.py` and `C_00.canonical_performance.py`
deployed (MATCH). Latent same-class risk IF cot's dispatch can do partial reruns. **Not promoted** —
needs cot-lane confirmation that cot C_00 consumes B_03's account_gains output (io can't verify: no cot
graph) and that cot supports partial reruns. Owner: DS (cot, confirm-then-add). Severity: ADVISORY.

### Verified-FP (suppressed with reason) — inf canonical_prices→inject guard absence
inf `orion_pipeline_deps.yaml` lacks a `build_canonical_prices→inject_scoped_overrides` guard, which
would be the $22M class — BUT inf `inject_scoped_overrides.py` is an explicit **v1 stub** ("no manual
overrides for Inflection v1… exits 0 so the auto-chain"), and inf has no overrides to wipe. The guard is
correctly absent (nothing to protect). **FP — suppressed.** (Verify-before-promote caught this.)

---

## 6. Precision sample (CVO gate)

| Candidate | Surfaced | Verdict | Promoted |
|---|---|---|---|
| D2X-DS-01 postdeps bd-only | 1 | REAL (tooling-debt) | 1 |
| D2X-DS-02 io no cot/mdpf graph | 1 | REAL (tooling-debt) | 1 |
| D2X-DS-03 cot fork-shadow orphan guard | 1 | REAL (config-debt, low-sev) | 1 |
| D2X-DS-04 cot missing B_03→C_00 guard | 1 | CANDIDATE (needs cot-lane confirm) | 0 (advisory) |
| inf inject-guard-absence | 1 | FP (inf inject = v1 stub no-op) | 0 (suppressed) |
| **Total** | **5** | **3 REAL / 1 candidate / 1 FP** | **3** |

**Promoted-set precision = 3/3 = 1.00** (≥0.80 gate PASS). **Suppression accuracy = 1/1.** All findings
filed ADVISORY pending CVO §3 adjudication before any non-ADVISORY promotion.

---

## 7. Verdict

- **Freshness/UNKNOWN-VINTAGE caveat: LIFTED.** inf/cot/mdpf vintage is now bound (TOOL-01 `--firm`);
  all MATCH except the 3 already-owned mdpf MISSING (TOOL-01-F01). D2-DS-01 CLOSED-confirmed.
- **inf composition: genuinely CLEAN** — 46/47 io-analyzed, 0 column gaps; postdeps guard (B_03→C_00)
  present; the one absent guard is a verified-FP (stub).
- **cot/mdpf composition: NOT clean-claimable with current tooling** — `io` has no cot/mdpf graph and
  `postdeps` is bd-only. The honest result is tool-UNCOVERED, surfaced as 2 tooling-debt findings
  (D2X-DS-01/-02) + 1 cot config fork-shadow (D2X-DS-03) + 1 candidate (D2X-DS-04). Zero *confirmed*
  composition bugs in cot/mdpf — but zero confirmed-clean either, until io/postdeps gain cot/mdpf graphs.

**Net:** the vintage axis closed; the coverage axis opened. Recommend a TOOL-02-class follow-on
(extend `io` + `postdeps` to cot/mdpf, mirroring TOOL-01's `deployed` extension) so the cot/mdpf
composition legs become assessable rather than perpetually tool-blind.

---

## CVO Precision Adjudication — 3.0.0_SA_CVO, 2026-06-12 ~20:00Z

- **D2X-DS-01 REAL** — verified: `cmd_postdeps` hardcodes the bd deps file (`pipeline_cli.py:2321`), structurally bd-only.
- **D2X-DS-02 REAL** — empirically reproduced: `comp-pipescript io B_03 --pipeline cot-gold` prints header `[bd-gold]` — silent fallback to the bd graph. The honesty-catch framing (cot/mdpf = tool-UNCOVERED, not clean) is exactly right and carries into the ledger as doctrine.
- **D2X-DS-03 REAL — REGRADED UP (SEV3→SEV2) and reframed:** verification escalated it. `data/cot/scripts/silver/inject_scoped_overrides.py` is MISSING (repo + `opal-data-cot/code/silver/`), while cot's `build_canonical_prices_v2.py` declares it an ENFORCED auto-chain (`:495-500` fail-closed `FileNotFoundError` — correctly prevents the silent-wipe $22M class, citing its own Delaney/BNP postmortem) **and S_00 is DISPATCHED** (`data/cot/scripts/gold/gold_dispatch.sh:78`) **and DEPLOYED** (S3 06-11). Net: not orphan config-debt — a latent hard-crash on first cot S_00 dispatch. Missing piece = the cot fork of inject_scoped_overrides.py (cot's `aua_overrides.json` RC6 exclusions exist and want a consumer). Owner: DS cot-lane; recommend pairing with the TOOL-02 follow-on.
- **D2X-DS-04** — stays CANDIDATE pending cot-lane confirm (correct handling, outside the precision denominator).
- **FP suppression (inf inject = v1 stub no-op)** — accepted on DS's documented reasoning.

**Precision: promoted 3/3 = 1.00 ≥ 0.80 — PASS. D2X families promote non-ADVISORY.** (An upward severity regrade is not a precision miss — the finding was real and conservatively filed.)

— 3.0.0_SA_CVO
