# MDPF_REMED.W2-1 — R-9..R-12 consumer census (1900–2050Z)

**archetype:** TRACE

**Agent:** `0.8.0_AE_CloudComp` (base) · **TO:** `MDPF_REMED.W2-1.shape-contract-consumer-census`
@e745552a63 · **Project:** MDPF_CANPLAT
**Deliverable:** `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/MDPF_R9_R12_CONSUMER_CENSUS_20260807.md`
**Register (PRD):** `docs/architecture/MDPF_REMEDIATION_REGISTER.md` @e5e932caf6 §2c

---

## Current State

The census COO's four rows each named as their closing condition is delivered. **Nothing moved** — no
served field renamed, relocated or retired; no gold/silver script modified; `route_bindings.yaml`
untouched.

| row | verdict |
|---|---|
| **R-9** `last_updated` | **0 rendering consumers** (1 hit / 288 portal component files, and it is a comment saying *do not use it*). One **disabled** reader; one **live passthrough** into the served response shape. |
| **R-10** `inflection_non_model_aua` | **0 portal-source consumers** (0 SURFACED / 1,260 files, **positive-controlled**). Three internal-instrument readers. |
| **R-11** five global-only fields | **ALREADY CLOSED by ADOPTION on 2026-08-05** — two days before the register became the PRD. |
| **R-12** pair-model blindness | **CONFIRMED: 14 pairs served, 12 generated, 8 live keys invisible by construction.** |

### The three findings worth reading

**1. R-9 was already ruled by Andrew, one layer down.** `ModelPortfolios.tsx:563-572` records the
MDPF_CADENCE FE-label fix (Andrew-sovereign 2026-06-08): the display was deliberately switched off
`metricsData.last_updated` onto `as_of_last` because *"the process timestamp misleads (renders
'today') when the spine has advanced but MDPF hasn't re-sampled."* R-9 asks whether to relocate a
field whose display use was already rejected **on exactly the grounds R-9 states**.
⚠ And the cost is not "nothing breaks": the one reader degrades **silently in the wrong direction** —
`data.last_updated || data.generated_at || new Date().toISOString()` falls through to **the client's
own clock**, so a stale as-of would render as *now*. Fix the fallback before the field moves.

**2. R-11 closed itself, by adoption rather than deletion.** The population was 6 (the five, plus
R-10's field, which the register correctly splits out) and was stable 07-27 → 08-03. On 08-05 all
four scopes gained all five: global 5/5 and every firm 0/5 on 08-03; 5/5 everywhere on 08-05. The
fields are now uniform, therefore canonical, therefore nothing to retire. **The row described a
condition that ended before the register was adopted as the PRD.**

**3. R-12's conclusion is right and its named mechanism is not.** The row says the model *"normalises
`_` and `-` variants to one type."* **No underscore normalisation is involved in any of the 8
invisible keys** — `account-units` and `non-model-assets` are both already hyphenated, and I measured
zero `_`→`-` normalisation across 57 files in `data/mdpf`.
The operative mechanism is worse: **the model is GENERATIVE, never OBSERVATIONAL.** `a4_expected =
len(SCOPES) * len(ARTIFACT_TYPES)` (`:968`) is compared against `emitted` — **both derived from the
same closed tuple.** Nothing ever lists the A4 prefix, so the check reads a clean **12/12 green**
while 8 live keys (newest 2026-08-05, same vintage as the main body) sit outside its universe.
**Two instruments sharing a derivation cannot cross-check each other**; an artifact type absent from
the tuple is not *missed*, it is *unaskable*. Consequence for the fix: adding `_`/`-` handling would
close nothing.

*Same shape as R-29 one row over, and as my own NFRA_PYFIELD finding this morning — a correct
conclusion carried on a wrong key / a normalisation hiding a population.*

---

## Blockers

**None.** Deliverable complete. Four decisions are now unblocked and **none of them is mine**:
R-9 → Andrew (served-shape change) · R-10 → Andrew (NEVER#3 + CONTRACT §B3) · R-12 → CTO (gate
change) · R-11 → COO (register edit only).

---

## Cross-agent

**`0.4.0_DS_ClientPlatform` — collision honoured, not worked around.** They held
`route_bindings.yaml` under W1-1 for the ~20 minutes it was genuinely between states. I asked before
reading rather than reading mid-edit, because an ABSENCE verdict here authorizes retiring a
client-facing field and a mid-edit read fails in exactly the direction that deletes a live one. They
answered **off the diff, not recollection**, with their own positive control, and pinned the settled
vintage at **`f999fb25f6` (UNPUSHED — `origin/CLOUD` still shows the superseded ddb-cohort row)**.
They also flagged that their commit adds one PROSE mention of `aggregate-aua-timeseries` at `:62`
that would move a naive textual count +1 for no real change. **My count excludes it** — I counted
reference rows, not string occurrences.

---

## Next Steps

1. **[Andrew]** R-9 relocation to `_provenance` — evidence is in §1. Recommend fixing the
   `DataSourceContext.tsx:106` fallback chain to fail loud **before** the move.
2. **[Andrew]** R-10 canonical-or-not. Client-facing surface is clear; the cost is three internal
   instruments (CVO layer-3 gate, DT parity baseline, `route_bindings` tie rows) — knowable and
   ordered in §2.
3. **[CTO]** R-12: make the completeness check observational (list the prefix, compare, surface
   unrecognised types by name). ⚠ **Do not let this become "delete the two unrecognised types"** —
   both are live at current vintage and **their producer is unidentified**; identifying it is the
   prerequisite and was not in this TO.
4. **[COO]** R-11: close as resolved-by-convergence.

---

## SURPRISE CHANNEL (banked, one line each — not re-opening this TO)

- `comp-transform schema-check` cannot see a React **context** file: `DataSourceContext` returns
  "Component not found" though it performs a live served-field read — a consuming surface invisible
  to the mandated Phase-2 check.
- 8 live keys under the MDPF served prefix (`cottonwood/account-units`, `global/non-model-assets`)
  have **no identified producer** — the consolidator does not emit them.

---

## Compiler Tools

| Tool + command | Denominator / result | Disposition |
|---|---|---|
| `comp-which "what consumes the mdpf aum-metrics artifact"` | near-tie, top 3 of 75 | Routed to `comp-estate --resource` / `comp-pipescript io`; declared a tie rather than guessing. Used `comp-find` for the field-level question it actually was. |
| `comp-find "last_updated" data/mdpf portal` | **77 hits / 1,317 files** (DEF 2 · SURFACED 17 · CONFIG 17 · TEST 7 · DOC 34) | R-9 census. The DEF band put the live reader on line 1. |
| `comp-find "last_updated" portal/src/pages portal/src/components` | **1 hit / 288 files** | The decisive R-9 number — and the single hit is a *negative* reference. |
| `comp-find "inflection_non_model_aua"` | **360 hits / 24,893 files** | R-10 estate-wide. |
| `comp-find "inflection_non_model_aua" portal` | **248 hits / 1,260 files — all CONFIG, all `.runtmp/`, 0 SURFACED** | The absence verdict. |
| `comp-find "aggregate-aua-timeseries" portal` | **22 hits / 1,260 files, 8 SURFACED** | **POSITIVE CONTROL** — proves the portal-scoped search finds source when source exists, so R-10's zero is measured, not broken. Run *because* the zero would authorize a deletion. |
| `comp-find 'replace(...)' data/mdpf` | **0 hits / 57 files** | Measured zero for `_`→`-` normalisation. ⚠ The tool **warned my regex used escaped parens/pipe that python `re` treats as literals** and told me a 0 could be the pattern, not the estate — I re-checked rather than banking the zero. Good tool behaviour; it prevented a false finding. |
| `comp-find "artifact-type\|artifact_type" data/mdpf` | 29 hits / 57 files (DEF 3) | Located the pair model at `mdpf_gold_consolidator.py`. |
| `aws s3api list-objects-v2` (full pagination, materialised) | **68 keys = 66 artifact + 2 manifest** | R-12's actual key listing. Counted client-side; **never `--query length()`** (page-count trap). |
| `comp-transform schema-check DataSourceContext` | **"Component not found"** | ⛔ **NOT a pass — a could-not-verify.** Recorded as a finding + banked to the surprise channel. |
| `comp-transform schema-check ModelPortfolios` | **WARN types-resolution, no types.ts found** | ⛔ **NOT a pass.** Recorded as could-not-verify. |
| `comp-to MDPF_REMED.W2-1...` | OK | Race-free per-session TO context. |

**Gap found:** `comp-transform schema-check` has no coverage for React context files (banked above).
Everything else behaved as designed; `comp-find`'s regex warning and its band/denominator output were
both load-bearing this session.
