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
| **D3-bis** *(new 1640Z — CVO STOP-BEFORE-BUILD; D3 and R2 were ARITHMETICALLY INCOMPATIBLE)* | How does a firm that **did not exist yet** enter the fold? | **A THIRD STATE. `NOT_YET_ONBOARDED` ≠ `None`.** A pre-onboarding absence **contributes ZERO and leaves the row COMPUTABLE**; only a genuinely broken feed yields `None` and fires the all-or-nothing rule. **THE ONBOARDING DATE IS DECLARED PER FIRM, NEVER INFERRED FROM DATA PRESENCE** — inferring it means a real outage in a firm's first week reads as not-yet-onboarded and silently contributes zero. | **CVO measured the collision:** `:1226-27` `None if None in (m49, nm49, minf) else …` and `:1237-39` *if the aggregate is None, null its components too* — the **all-or-nothing row rule**. Cottonwood's `fact_model_*` tables have **ZERO pre-2026-07-21 dates**. **So a naive 4th term makes `None in (...)` TRUE for the ENTIRE historical series and NULLS EVERY PRE-07-21 GLOBAL ROW.** **AND IT WOULD NOT LOOK LIKE A FAILURE** — it renders as *honest nulls*, the pattern the estate reads as correct conservative behaviour; **no exception, no non-zero exit, and the composition gate STILL PASSES** because an identity over all-None terms is **vacuously satisfied**. *(Precedent in this same file: the identity held 7/7 while the whole sum sat on the wrong day. **An identity between terms cannot see a common-mode error, and this is one.**)* **The distinction never existed because both firms existed for the whole series — onboarding a firm mid-series is the first time "did not exist" and "is broken" come apart. A pre-onboarding absence is a KNOWN ZERO, not an unknown; treating a known zero as an unknown destroys the history.** **CTO ruling.** |
| **D4** | Do per-firm named artifact keys become **firm-keyed maps**? | **NO. Keep per-firm named artifacts; cottonwood is one more named artifact.** | A firm-keyed map is a **breaking shape change with live FE consumers**, taken mid-consolidation, for no benefit the named-artifact pattern does not already give. **The estate's own working pattern is named per-firm slices.** **CTO ruling.** |
| **D5** | Which cottonwood source is canonical for MDPF? | **CLOSED** — `s3://opal-data-assets/blackdiamond/cottonwood/**` ONLY. Never `opal-data-cot`, never `opal-data-bd`. | CTO firm-separation ruling 2026-07-22 ~1308Z, conditions (i)–(iii); reads stated in the ledger so the claim is checkable. |
| **D6** | Merge-vs-add for the two unresolved model keys | **CLOSED by Andrew** ~1412Z / ~1421Z / ~1425Z. `cottonwood_opal_conservative_growth` → **MERGES** to `opal_long_term_conservative`; `Opal - Income` → **NON-MODEL**, no canonical key. | Governing principle: **the labelled key space is the ARCHETYPAL LADDER, not vendor strategy names.** |

---

## C. THE SEQUENCE

**Ordering law: DECISIONS → ENUMERATION-TO-EXIT → BUILD → WIRE → EMIT → PIN → CO-SIGN → FLIP.
Every inversion attempted today cost a re-do.**

### S0 — **JULY SOURCE COMPLETENESS PER CHANNEL** *(Andrew-direct ~1612Z/~1615Z; owner `0.6.2_AE_PartnerETL~A`; UPSTREAM OF EVERYTHING)*
**Andrew-direct, VERBATIM:** *"we should have complete data every single day of July thus far aside from
weekends (4 and 5, 11 and 12, 18 and 19) and July 3."* / *"That is step 1, making sure we have complete data
for July for each channel."* / *"Ok yes, have 0.6.2 do the Inflection repull"*
**This is a SOVEREIGN CARVE-OUT of the planning hold — directed during it, so latest binds. The plan does not
survive incomplete inputs; this precedes S1.**

**MEASURED (CTO, 1614Z) against the 15 expected trading days — Jul 1, 2, 6-10, 13-17, 20-22:**
| channel | source | July |
|---|---|---|
| Inflection | `eclipse fact_portfolios_full` | **MISSING 07-01, 07-13, 07-14, 07-15** |
| Inflection | `orion fact_assets` | **MISSING 07-13, 07-14, 07-15** |
| 49F | `smartx fact_model_aum_daily` | **COMPLETE 07-01 → 07-21** |
| 49F | `schwab 0824 fact_rps_s2` | complete except today |
| Cottonwood | `fact_holdings` | through 07-20 |
| Cottonwood | `fact_model_assignment` | **only 07-21, 07-22** — Rebalancer is live-state with NO history; **not an ingest failure and not recoverable by re-pull** |

> **THE DISPOSITION-CHANGING FINDING: ECLIPSE AND ORION ARE INDEPENDENT VENDORS MISSING THE IDENTICAL THREE
> DAYS.** Two simultaneous 3-day outages at two unrelated providers on exactly the same dates is not the
> likely explanation — **the common factor is almost certainly OUR INGEST, which makes the data probably
> RECOVERABLE.** *(CTO had previously told Andrew this was a vendor gap needing re-delivery. That reading is
> superseded.)* **07-01 is ECLIPSE-ONLY — a DIFFERENT shape. Two findings are likely, not one.**
**ORDER: ground the mechanism BEFORE pulling** (Rule 22 — ingest scheduler history, logs, DLQ, the bronze
beneath both silvers). **Guardrails:** bronze **additive-only, never overwrite** (17a); **verify ABSENT, not
present-but-empty** *(an empty artifact was proven today to read as CLEAN, rc=0, on a real gate)*;
positive-controlled listing (`CommonPrefixes` returned `None` where prefixes existed, this estate, today);
**no new vendor wire without CTO word**; **NO REBUILD** — a source re-pull does not touch
`gold/mdpf_revamp/*`, which stays a checkpoint under the held co-sign.

> ### ⚠ INSTRUMENT CAUTION, EARNED — CTO NEARLY REPORTED A FALSE 8-DAY GAP
> My first pass reported **smartx missing EIGHT July days. That was the instrument, not a gap.**
> `fact_model_aum_daily` is partitioned by **RUN_DATE** and carries **FULL HISTORY inside each partition**
> (one partition = 1,225 data days back to 2021, incl. all 14 July trading days through the 21st). **I was
> counting run-date folders and calling them data dates.**
> **BEFORE TREATING A MISSING PARTITION AS MISSING DATA, ESTABLISH WHETHER THE TABLE IS DATA-DATE OR
> RUN-DATE PARTITIONED.** Had it shipped, it would have been a false hole on the exact firm Andrew had just
> questioned — **a wrong number that lands on a real suspicion is the most persuasive kind.**

### S1 — FINISH PHASE 0 TO ITS ACTUAL EXIT *(owner DE; gates all build)*
**Phase 0's exit is NOT met and must not be reported as met.** The population has **THREE** axes
*(amended 1556Z — it was two; the third was proved by the IAM finding in S1b)*:
- **A · firm-TOKEN axis** — searchable, measurable. Substantially covered.
- **B · unnamed-ARITY axis** — a hardcoded count, a 2-element concat, a two-term sum, a closed series list.
  **Names no firm → not reliably searchable.** Every confirmed member found by **READING**.
- **C · ENCODING BY OMISSION** — *a firm simply MISSING from a list that should contain it.*
  > **AN ABSENCE HAS NO TOKEN. YOU CANNOT GREP FOR WHAT IS NOT THERE.**
  Axis A cannot see it (`main.tf:56-61` declares `bd_bucket` and `inf_bucket` and no `cot_bucket` — those name
  **buckets, not firms**). Axis B cannot see it either (**there is no `2` anywhere** — five ARNs covering two
  firms, so `== 2` / `[0]`/`[1]` / concat-pair searches return nothing). **Both A and B are PATTERN searches,
  and every pattern search enumerates WHAT IS PRESENT.**
  **THE INSTRUMENT FOR C IS A SET-DIFFERENCE, NOT A PATTERN MATCH:** wherever the estate **enumerates its
  subjects** — IAM `Resource` lists, prefix `Condition`s, EventBridge patterns, `argparse choices=[...]`,
  config maps, `FIRM_CONFIG`-style dicts — **take the list and DIFF it against the real firm population.**
  Cheap: the lists are few and short. **It is the only axis that can close the enumeration.**

- **D · ENCODING BY ALIAS** *(added 1610Z — CVO falsified A11 and found this)*: **a firm that IS enumerated,
  under a token from a DIFFERENT NAMESPACE.**
  > **AXIS C'S INSTRUMENT, AS I SPECIFIED IT, DOES NOT MERELY MISS THIS — IT MISREPORTS IT.**
  Of the five ARNs in `AssetsRevampSilverRead`, **two name no firm at all**: `smartx/platform` is a
  **platform**, `schwab/08242234` is a **custodial account number**. Both are 49financial. **So a naive
  set-difference reports `cottonwood ABSENT` (true) AND `49financial ABSENT` (FALSE) — indistinguishable in
  the output.** Axes A and B fail **silent**; **axis C fails LOUD AND WRONG**, and a census that flags a firm
  which is actually wired is one somebody "fixes" by adding a grant that already exists.
  **This is the estate's declared grammar, not an accident** — `monolith.tf:22-32`, `{source}/{scope}/{layer}`,
  where **`scope` is heterogeneous BY DESIGN** (account numbers · platform · firm · ticker). *Segment 2 is
  SCOPE; firm is only sometimes the scope.*
  **AND THE RESOLVER THIS NEEDS HAS TWO MAPPINGS THAT ARE NOT FUNCTIONS:** `blackdiamond` → firm is
  **ONE-TO-MANY** (49financial via `bd`, cottonwood via `blackdiamond/cottonwood/**`); and
  `schwab/{account}` → firm is **MANY-TO-ONE — and collapsing it would destroy a control we deliberately
  built.** `router_iam.tf:173-177` enumerates the two masters individually *"so no single identity can write
  both trees and 'do not commingle 0824 and 0833' becomes a property of the ROLE."* **A resolver mapping both
  0824 and 0833 to `49financial` erases exactly the distinction that control exists to enforce, and collides
  with Andrew's two standing prohibitions (never SUM, never SUBSTITUTE).**

**~~EXIT CRITERION: THREE STATED FRACTIONS~~ — REPLACED 1610Z. A11 FAILED.**
**The old second limb ("is the list-of-lists bounded?") was the WRONG QUESTION.** It is answerable and
probably *yes*, and closure does not depend on it. **Closure depends on: (i) are the NAMESPACES through which
the estate can name a firm bounded and enumerated, and (ii) is each namespace→firm resolver TOTAL and
LAW-PRESERVING?** CVO grounded **seven namespaces from three files without looking hard** — firm-id ·
short-code (`bd`/`inf`/`cot`) · scope · vendor/source · custodian+account · bucket name (`main.tf:56-61`,
**no `cot_bucket`** — a genuine axis-C instance) · portal `firmId`. **Seven is not established as all of them,
and THAT is the open question S1's exit now rests on.**

**NEW EXIT CRITERION FOR AXIS C/D (CVO's, adopted):** *C is closed when (1) the firm-naming namespaces are
enumerated with a STATED METHOD, (2) each list is RESOLVED into a common namespace before differencing, and
(3) every entry that CANNOT be resolved is reported as **UNRESOLVED** — never silently dropped, never assumed
firm-agnostic.* **(3) is the load bearer: an unresolvable entry silently dropped is precisely how
`smartx/platform` becomes "not a firm list" and the census returns clean.**

**EXIT CRITERION: FOUR STATED FRACTIONS + AN UNRESOLVED COUNT, NEVER BLENDED.** Axis A a search denominator; **axis B a READ
fraction** (currently **10% / 33% / 31%** on the three densest — the 10% being
`dim_mdpf_aggregate_aua_timeseries.py`, home of `build_global_artifact`); **axis C a set-difference over every
enumerated-subject list.**
> **THE STANDING LESSON, and it generalises past this census: A CENSUS MUST STATE WHICH KIND OF ENCODING ITS
> INSTRUMENT CAN RETURN — because an instrument that enumerates only what is PRESENT will report an ABSENCE
> as a CLEAN RESULT.** Same family as the Glob case-sensitivity note in §E: both answer *"nothing found"* when
> the honest answer is *"I cannot see that kind of thing."*
**Each axis was invisible to its predecessor's method** — CTO adopted a one-axis view, DE proved a second,
and the second proved there had to be a third. **If Phase 0 closes on axes A and B alone, class C closes
UNMEASURED — and its first known instance sits on the runtime path of the very first build step.**
**Also in S1:** the fixture render (`ui-smoke.mjs --fixtures firmId:cottonwood`) — **GO'd**; it confirms or
kills five FE findings including `STACK_SERIES` (a closed 7-entry literal against a data-driven legend/donut
→ a model outside the 7 renders a slice and a swatch with **NO BAR**, and the trend silently totals less than
the donut).

### S1b — **IAM: TWO ADDITIVE STATEMENTS. S2a CANNOT RUN WITHOUT THEM.** *(owner AE; CTO gates the apply)*
**AMENDED 1556Z — S2a was listed as "parallel, all unblocked". IT IS NOT.**
`mdpf-pipeline/iam.tf:243-252`, Sid `AssetsRevampSilverRead`, grants `s3:GetObject` on **exactly five ARNs**
(`smartx/platform/silver`, `schwab/08242234/silver`, `eclipse/inflection/silver`, `orion/inflection/silver`,
`gold/mdpf_revamp`). **`blackdiamond/cottonwood/silver/*` is NOT among them — while Cottonwood silver EXISTS
there (12 `fact_*` tables from the WS-5 converter).** `AssetsRevampListScoped` carries the same closed
prefix-condition list, so **partition discovery (`_latest_date` / `_read_partition`) fails identically.**
**GROUNDED ON ALL THREE LIMBS (Rule 22a):** `desired` (TF at HEAD) = 5 ARNs · `applied` (live
`get-role-policy` on `mdpf-daily-runner-ec2-role`) = **the same 5** · `exercised`
(`simulate-principal-policy`, ONE `--resource-arns`) → Cottonwood **`implicitDeny`** · **control, SEPARATE
invocation** → inflection **`allowed`**. **The control discriminates, so the deny is real. And desired ==
applied, so this is NOT DRIFT — IT WAS NEVER BUILT.** There is nothing to reconcile; there is something to add.
**Two additive statements, no widening beyond one new source tree. Held: IAM under the planning hold.**
**Bears on D5:** the IAM that exists points at **neither** candidate source for the revamp role, and the silver
that exists sits under `blackdiamond/cottonwood/`. **D5's ruling therefore has an asymmetric IAM cost attached
— that is now known before the ruling rather than after.**

### S2 — BUILD *(gated on S1's exit AND on S1b; NOT parallel-unblocked)*
- **S2a · DE** — re-home cottonwood as `build_cottonwood_artifact()` **inside the shared producer**; extend
  `build_global_artifact` to the **N-firm fold** (D3); `--firm` choices; `want` sets. **Cottonwood joins the
  existing trading-day axis (R2).** Apply D6: merge CG→LTC, Income→non-model.
- **S2b · DS** — the **third audit leg** for cottonwood, **report-only** (D2).
  > **⚠ CVO side-finding (exercised, 1603Z): AN EMPTY ARTIFACT READS AS CLEAN.** `audit_inflection()` against
  > an artifact with `dates: []` returns **`rc=0`** with *"no disagreement on the audited dates"* — while the
  > docstring promises `2` on an instrument problem. **The human-readable output IS honest (`0 date(s)
  > audited`, `0 of 0`); an `rc`-only consumer is blind to exactly that.** **BINDING: the `cycle_complete`
  > fold in 1e must gate on the COVERAGE NUMBERS, not on `rc` alone — otherwise a cycle that produced NOTHING
  > is indistinguishable from a cycle that produced something clean. The fix must be IN the fold, not after it.**
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
| **A5** | ~~Cottonwood contributes nothing before 2026-07-21.~~ **BASIS CONTRADICTED AT SOURCE, 1640Z (CVO): 91 of 93 distinct cottonwood data dates are PRE-07-21, earliest 2026-03-09.** The true, narrower statement is **cottonwood's `fact_model_*` tables begin 2026-07-21.** **So the conclusion may still hold — but ONLY IF THE GLOBAL FOLD READS EXCLUSIVELY THE `fact_model_*` FAMILY.** If it touches `allocations`/`unrealized`/`holdings`, cottonwood has **4 months of pre-07-21 data** and the byte-identity bound breaks the other way. | **A5 IS NOW A TESTABLE GATE AND THE TEST IS: WHICH TABLE FAMILIES FEED THE GLOBAL FOLD?** Answerable at S2a build time; **not answerable by asserting the firm is new.** **⚠ D3-bis AND A5 PULL IN OPPOSITE DIRECTIONS** — the null rule would wipe history to `None`, the non-model tables would inject real pre-07-21 value. **BOTH ARE LIVE UNTIL THE FOLD'S INPUT SET IS PINNED.** *(CVO could not turn this into a control read-only — it needs a cottonwood-absent build — and reported it as STILL-AN-ARGUMENT rather than dressing a reasoning pass as a gate.)* |
| **A6** | `STACK_SERIES` is a closed 7-entry literal while legend/donut are data-driven. | The render. |
| **A7** | 49F's count axis has **no per-date source anywhere** — the basis for treating it as unfixable. | Any per-date 49F roster history falsifies it and reopens the decouple. |
| **A8** | The `json/` FE-mirror dual-write is **graceful-degrade** (WARN, not non-zero) — so a build can succeed with a stale served copy. | `build_aggregate_aua_timeseries.py:654-661`. **Ungated today.** |
| **A9** | Phase 0's unnamed-arity axis (B) is **genuinely unsearchable** — reading is the only method. | Find a search that reliably finds arity sites. Would collapse S1's cost. |
| **A11** *(new 1556Z)* | **Axis C (encoding-by-omission) is closable by set-difference** over the estate's enumerated-subject lists — and those lists are **few and short enough to enumerate exhaustively.** | Try to enumerate every place the estate lists its firms/subjects. **If that set is itself open-ended, S1 has no exit and the plan needs a different closure criterion.** This is the assumption the whole S1 exit now rests on. |
| **A12** *(new 1556Z)* | The **two additive IAM statements** in S1b are sufficient for S2a to run green — i.e. `GetObject` + the `List` prefix-condition are the only denials on the Cottonwood read path. | **Exercise after apply, do not infer:** `simulate-principal-policy` on both the object read and the list, separate invocations, with a positive control. A second hidden denial would re-block S2a after an apply. |
| **A10** | No named thread references `json/mdpf/{firm}/aggregate-aua-timeseries.json` — the estate's thread traversal does not reach a six-consumer artifact. | `pipescript --resource`. Affects what impact analysis can be trusted for. |

**CVO also to check:** that the six D-decisions above are consistent with each other and with R1–R12, and that
nothing in the sequence inverts the ordering law.

---

## D-bis. ⚠ A CUTOVER COUPLING NOBODY HAD FLAGGED — `opal-assets-daily-aua`

*Surfaced by an Andrew question to CVO (~1612Z) about `opal-assets-daily-aua`; CVO measured the table, CTO
then grounded the emitter's read path. **This is a POST-CUTOVER DIVERGENCE RISK on the exact field this
morning's P0 was about.***

**WHAT IT IS (CVO, measured):** a **DynamoDB table, not a bucket** — `run_date` HASH + `cohort_id` RANGE,
**588 items, 21 run_dates 2026-06-12 → 2026-07-18**. **NOT ETF-exclusive:** 252 of 588 rows are **MDPF cohort
space** (`49f_{7 models}`, `49f_schwab_custody`, `49f_smartx_platform`, `inflection_models`); 336 are
ETF-related. The emitter's own header calls `etf_ownership_held` **"the 6th class"** — **ETFs were ADDED to a
pre-existing daily-AUM table; they are not its purpose.**

**WHAT THE EMITTER ACTUALLY READS (CTO, source-grounded at
`infra/aws/lambda/opal-assets/opal-assets-daily-emitter/lambda_function.py`):**
`PLATINUM_BUCKET = opal-data-portal-v2` (`:52`) · `AGGREGATE_PREFIX = platinum/mdpf/aggregate_aua/` (`:53`) ·
`carried = agg.get("opal_aggregate_aua")` (`:1028`) · `"source_field": "mdpf aggregate.opal_aggregate_aua
(CARRIED VERBATIM)"` (`:1041`).
**It references `opal-data-assets` ZERO times — the name implies canonical-assets membership the DATAFLOW
DOES NOT HAVE.**

> ### THE RISK, PLAINLY
> **This table CARRIES VERBATIM the `opal_aggregate_aua` value from the LEGACY served platinum partitions.
> That is the EXACT field this morning's P0 was about, and the exact field DS rebased to basis B.**
> **Post-cutover the portal serves the REVAMP's `opal_aggregate_aua`, while the legacy producer keeps running
> as an untouched shadow and keeps feeding this table the LEGACY value. Two systems of record on one field,
> diverging silently — and the DDB one is what downstream consumers read.**
> Its own header certifies the carried value *"with residual $0.0000 on 427 of 427"* — **post-cutover that
> certification is against a superseded basis.**

**CTO READ (architectural, not a measurement — no measurement answers it):** the DDB shape is **correct** for
`run_date`+`cohort_id` access; **the INPUT is what is wrong.** A daily-AUM table derived from the **SERVED**
layer is **the layer grammar running backwards**. **So Andrew's instinct is directionally right and the fix is
NOT "move the ETF data into the bucket" — it is RE-POINT THE INPUTS AT CANONICAL GOLD.** Whether the table is
a **serving projection** (legitimate) or a **system of record** (an architectural gap — no bronze/silver/gold
lineage exists for those cohort rows) is the deciding scope call. **OPAL_CONSOLIDATION scope; NOT started
under the hold; recorded here so it is not a clock with no keeper.**

**Supports DE's "MDPF is the laggard" finding:** `FOLD_PARTNERS = ("49financial","inflection","cottonwood")`
at `:696` — **this emitter is already 3-firm, with `# Cottonwood folds ONE-WAY (PRD 3e)`.**

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
