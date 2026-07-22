# MDPF — EXECUTION PLAN (sequenced)

**Andrew-direct ~1552Z:** *"I want a comprehensive plan created and sequenced, not more ad hoc stuff. If you
have the plan ready to go, send to CVO for review and /verify of assumptions. Then we can issue to COO for
decomposition of TOs and dispatch."*

**Author:** `1.0.0_SA_CTO` | **Status:** DRAFT → CVO review → COO decomposition → dispatch
**State annex:** `MDPF_CONSOLIDATED_PLAN_20260722.md` (verified live state, standing rulings R1–R12, the armed
hazard, per-lane resumption). **This document is the SEQUENCE. That one is the STATE. Neither replaces the other.**

---

## A. WHAT THIS PLAN IS ACTUALLY FOR

**Reframe, from `0.4.0_DE`'s Phase-0 census (`@0aa0f2200`):** this is **FIRMSEP.11 — the MDPF DATA half of
firm separation.** FIRMSEP.10 shipped the *tenancy/routing* half in May. The data half sits at
`ADVI_FIRMSEP.md:365` as a **QUEUED PLACEHOLDER**, gated on Andrew-direct 2026-05-07 (*"cant be implemented
yet"*), **and no TO was ever authored.**

> **The estate encodes exactly-two-firms throughout MDPF BY DECISION, not by neglect. We have been executing
> an unscoped phase under the name of a completed one. That is why every estimate came in short.**

**And MDPF is the LAGGARD, not the frontier** — which lowers design risk. Three-firm canonical tuples already
run in production siblings (`etfs-canon-fanin:47`, `opal-assets-daily-emitter:696`, both
`("49financial","inflection","cottonwood")`), `partner-firms/cottonwood.tf` since 2026-04-29, a 16-file
`cot-pipeline/`, cottonwood live in `firm-config.mjs:51-54`. **Every MDPF two-firm site is KNOWN-DIVERGENT
from a working shipped pattern.**

---

## B. DECISIONS THAT GATE CODE — RULED HERE, NOT LEFT OPEN

`0.4.0_DE` surfaced six. **None is an engineering call; all six are now closed or ruled.** *(Two were already
closed by earlier rulings — the durable-carrier discipline paying off.)*

| # | Decision | Ruling | Basis |
|---|---|---|---|
| **D1** | Is cottonwood a **DRIVER**, a **SKIPPABLE PARTNER**, or a third category? | **SKIPPABLE PARTNER.** | `spine_fresh` is a **SCALAR** — no code path can express two drivers, and `run_date` derives from the spine. Making a **2-day-old feed** a driver would let Cottonwood **halt the entire nightly**. Inflection stays the spine; the EventBridge trigger stays inflection's sentinel. **CTO ruling.** |
| **D2** | Cottonwood's audit **failure policy** — fail-hard or report-only? | **REPORT-ONLY at first; promote to FAIL-HARD after 3 clean scheduled cycles.** Promotion is a CTO ruling, not automatic. | Mirrors the existing asymmetry (inflection FAIL / 49F report-only) and its reason: **a leg with a known-immature source that fails hard fails EVERY night, and a gate that fails by construction becomes an alarm people scroll past.** There is **no default for an unlisted firm** — this supplies it. **CTO ruling.** |
| **D3** | Does the two-leg **conservation identity** become a fold, or does Global re-derive? | **GENERALISE IT TO AN N-FIRM FOLD. Excluding cottonwood to make it pass is EXPLICITLY REFUSED.** | The identity is a **CORRECTNESS gate** that a third firm makes **arithmetically false**. It fails loudly — *so the path of least resistance under schedule pressure is to make it pass by excluding cottonwood.* **DE named that incentive before anyone was under time pressure; this ruling exists to remove the option.** **CTO ruling.** |
| **D4** | Do per-firm named artifact keys become **firm-keyed maps**? | **NO. Keep per-firm named artifacts; cottonwood is one more named artifact.** | A firm-keyed map is a **breaking shape change with live FE consumers**, taken mid-consolidation, for no benefit the named-artifact pattern does not already give. **The estate's own working pattern is named per-firm slices.** **CTO ruling.** |
| **D5** | Which cottonwood source is canonical for MDPF? | **CLOSED** — `s3://opal-data-assets/blackdiamond/cottonwood/**` ONLY. Never `opal-data-cot`, never `opal-data-bd`. | CTO firm-separation ruling 2026-07-22 ~1308Z, conditions (i)–(iii); reads stated in the ledger so the claim is checkable. |
| **D6** | Merge-vs-add for the two unresolved model keys | **CLOSED by Andrew** ~1412Z / ~1421Z / ~1425Z. `cottonwood_opal_conservative_growth` → **MERGES** to `opal_long_term_conservative`; `Opal - Income` → **NON-MODEL**, no canonical key. | Governing principle: **the labelled key space is the ARCHETYPAL LADDER, not vendor strategy names.** |

---

## C. THE SEQUENCE

**Ordering law: DECISIONS → ENUMERATION-TO-EXIT → BUILD → WIRE → EMIT → PIN → CO-SIGN → FLIP.
Every inversion attempted today cost a re-do.**

### S1 — FINISH PHASE 0 TO ITS ACTUAL EXIT *(owner DE; gates all build)*
**Phase 0's exit is NOT met and must not be reported as met.** The population has two axes:
- **firm-TOKEN axis** — searchable, measurable. Substantially covered.
- **unnamed-ARITY axis** — a hardcoded count, a 2-element concat, a two-term sum, a closed series list.
  **Names no firm → not reliably searchable.** Every confirmed member was found by **READING**.
**EXIT CRITERION: a stated READ fraction per dense file, not a search denominator.** The three densest are
currently **10% / 33% / 31%** read — and the 10% is `dim_mdpf_aggregate_aua_timeseries.py`, home of
`build_global_artifact`. **Report two fractions. Never blend them into one number.**
**Also in S1:** the fixture render (`ui-smoke.mjs --fixtures firmId:cottonwood`) — **GO'd**; it confirms or
kills five FE findings including `STACK_SERIES` (a closed 7-entry literal against a data-driven legend/donut
→ a model outside the 7 renders a slice and a swatch with **NO BAR**, and the trend silently totals less than
the donut).

### S2 — BUILD *(parallel; each gated on S1's exit, not on each other)*
- **S2a · DE** — re-home cottonwood as `build_cottonwood_artifact()` **inside the shared producer**; extend
  `build_global_artifact` to the **N-firm fold** (D3); `--firm` choices; `want` sets. **Cottonwood joins the
  existing trading-day axis (R2).** Apply D6: merge CG→LTC, Income→non-model.
- **S2b · DS** — the **third audit leg** for cottonwood, **report-only** (D2).
- **S2c · DE** — FE: cottonwood in `ALL_MDPF_PARTNER_FIRMS`; `STACK_SERIES` generalised if the render
  confirms; the `$0`/"rolled forward" fixes already landed (`08c6d8b2`).

### S3 — WIRE *(owner AE; the step that was never in anyone's scope)*
Add the **cottonwood leg** to `revamp_stage()` **and** DS's audit wiring, **in the same change.**
> **⚠ FORCED ORDERING, MEASURED (DE): `gold/mdpf_revamp/` has NO `cottonwood/` prefix, and the
> count-source-audit tripwire is ARMED (`rc=1` on any unaudited prefix, BEFORE the `--firm` branches). So the
> THIRD AUDIT LEG MUST LAND IN THE SAME CHANGE AS THE STAGING LOOPS. Stage first and the nightly returns
> non-zero, no cycle-complete marker is written, and the parity streak cannot accrue even if every cottonwood
> artifact is perfect. YOU CANNOT STAGE FIRST AND AUDIT LATER.**

### S4 — EMIT *(scheduled nightly only)*
**No hand-staging.** A hand-staged artifact proves the code works, not that the production path emits it —
and that masking class already bit us once today in WS-5.

### S5 — PIN + 3-PASS *(owner CTO pins; DS/CVO/DT verify)*
CTO pins the **emitted** ETags. Fresh three-pass: DS producer-validate (incl. the audit hand-run on the
pinned set), CVO from-scratch re-derive, DT consistency.
**BINDING (R9): none of today's gate proofs transfer** — every gate was mutant-proven against
`f(49f, inflection)`; all are re-exercised against `f(a,b,c)`. **(R10)** every limb states its **coverage
fraction against the defect-capable population**, never a percentage. **49F COUNT-mode render cell cannot be
waived.**

### S6 — CO-SIGN + FLIP
Fresh **CTO + COO + Andrew** never-widen co-sign carrying the declared terms (49F unbounded-by-construction;
retained legacy runtime dependency; the 20-date Global gap; 1-of-6 historical coverage). → FE-first promote →
AE `-target` apply → **immediate revert-plan hard gate** → verify-before-serve → rollback armed until explicit
disarm.
**⚠ PART 0 of the state annex applies throughout: `portal-auth` is 9 behaviors ahead of live. NO untargeted
apply in that root, ever, by anyone.**

---

## D. ASSUMPTIONS THIS PLAN RESTS ON — **CVO: `/verify` THESE**

**Every one is falsifiable and none is verified by me beyond the citation given. If any fails, the sequence
changes.**

| # | Assumption | How to falsify |
|---|---|---|
| **A1** | `spine_fresh` is a **scalar** and no code path can express two drivers — the basis for D1. | Read the spine/trigger path. If two drivers are expressible, D1 reopens. |
| **A2** | The count-source-audit tripwire really does `rc=1` on an unaudited prefix **before** the `--firm` branches — the basis for the S3 forced ordering. | **Exercise it**: add a fake unaudited prefix and confirm non-zero. Do not read it. |
| **A3** | Three-firm tuples in `etfs-canon-fanin:47` and `opal-assets-daily-emitter:696` are **live and exercised**, not declared-and-unapplied. | Declared-vs-applied: check the deployed artifacts, not the repo. *(This estate produced an unapplied IAM grant today.)* |
| **A4** | The conservation identity is **generalisable** to N firms without a basis change. | Derive it for 3 and confirm it reduces to the 2-firm form. |
| **A5** | Cottonwood contributes **nothing before 2026-07-21**, so every pre-07-21 Global value is byte-identical with cottonwood absent. | Assert byte-identity against a cottonwood-absent build. **This is the (A) honest-null safety bound and it must be a GATE, not a claim.** |
| **A6** | `STACK_SERIES` is a closed 7-entry literal while legend/donut are data-driven. | The render. |
| **A7** | 49F's count axis has **no per-date source anywhere** — the basis for treating it as unfixable. | Any per-date 49F roster history falsifies it and reopens the decouple. |
| **A8** | The `json/` FE-mirror dual-write is **graceful-degrade** (WARN, not non-zero) — so a build can succeed with a stale served copy. | `build_aggregate_aua_timeseries.py:654-661`. **Ungated today.** |
| **A9** | Phase 0's unnamed-arity axis is **genuinely unsearchable** — i.e. reading is the only method. | Find a search that reliably finds arity sites. Would collapse S1's cost. |
| **A10** | No named thread references `json/mdpf/{firm}/aggregate-aua-timeseries.json` — the estate's thread traversal does not reach a six-consumer artifact. | `pipescript --resource`. Affects what impact analysis can be trusted for. |

**CVO also to check:** that the six D-decisions above are consistent with each other and with R1–R12, and that
nothing in the sequence inverts the ordering law.

---

## E. NOT COVERED — stated, not implied

`infra/` dispatch + IAM, the publisher/promote path, `dim_mdpf_account_distribution.py`,
`dim_mdpf_aum_{metrics,timeseries}.py`, the FE per-firm distribution path — **all outside Phase 0's current
read coverage.** Silver-family vendor staleness (4 of 9, `silver_registry.py` the common axis) is a **separate
workstream**, not MDPF. Three stale records surfaced and unreconciled (`ADVI_FIRMSEP.json`,
`comp-constants.config.yaml:564-568`, the missing ONBOARDING_PLAYBOOK). **`Glob`/`comp-glob` is
CASE-SENSITIVE — any prior Glob-based negative on the portal tree is a possible false clean.**

**NO DATE IS QUOTED.** The sequence is bounded except S1, whose exit is a read fraction. **A date becomes
honest when S1 prints its two fractions — not before.**
