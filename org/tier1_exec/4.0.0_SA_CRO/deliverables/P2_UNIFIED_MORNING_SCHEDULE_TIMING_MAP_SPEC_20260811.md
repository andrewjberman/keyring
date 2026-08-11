# P2 TIMING MAP + UNIFIED MORNING SCHEDULE — SPEC (per `docs/architecture/GOLD_MIGRATION_PHASE_FRAMEWORK.md` P2 row)

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Commission:** CTO, Andrew-direct ~1750Z (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260811_PHASE_FRAMEWORK_FORMALIZE_UNIFIED_MORNING_DEBT_BRIEF.md`), retargeted to CRO base ~1757Z mid-turn. **Protocol: CRO authors -> CVO reviews -> CTO ratifies -> AE implements at P2-open.**
**Status:** DRAFT, first pass. Every claim below is traced to a captured artifact (file:line / commit) or explicitly marked NOT LOCATED. Per the commission's own framing: *"the ADVI-endpoints-morning-ready premise is VERIFIED by the spec, not assumed"* — §5 is that verification, and it does not close clean.

---

## 0. Provenance note (read before citing this spec elsewhere)

`GOLD_MIGRATION_PHASE_FRAMEWORK.md`'s CURRENT STATE section (line 49, as of this writing) still reads *"Spec commissioned to CRO~A (author)."* That is **stale**, per CTO's own later record: the debt-identification research (not this spec) was retargeted to `~A` at ~1757Z, and *"the P2 TIMING spec commission (directive 4) moves to CRO BASE... the seats swap cleanly"* (`ANDREW_DIRECT_20260811_PHASE_FRAMEWORK_FORMALIZE_UNIFIED_MORNING_DEBT_BRIEF.md:38-41`). Confirmed three independent ways: the CTO MCP message addressed to this seat (*"this commission comes to BASE because Andrew retargeted the debt-identification research to ~A mid-turn"*), CTO's own deliverable above, and `4.0.0_SA_CRO~A`'s live broker status (*"P5 debt-ID methodology spec DELIVERED... BD-REST retime recorded+routed (P2 keystone)"* — producing inputs, not authoring). `docs/architecture/**` is `ANY_CTO`-laned (`.owned-paths.yaml:1670-1672`); this is flagged to CTO for a one-line correction rather than edited here.

---

## 1. VENDOR LANDING TIMES (verified, not believed)

| Vendor / pipeline | Landing time | Source | Confidence |
|---|---|---|---|
| **BD REST (49F/bd + cot)** | Day D data available **D+1 01:02 ET (05:02Z)** | Andrew-direct verbatim, `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260811_BD_REST_0102ET_COT_MORNING_SCHEDULE.md:5-12` (commit `accf58083e`) | **SOVEREIGN-STATED**, bracketed by 5 first-ask-success sentinels 08-06..08-10 (consistent, not independent proof) |
| **Orion (inf custody feed)** | Daily landing **~14:16Z** | `docs/architecture/MDPF_PIPELINE_TRUTH.md:120-137` (measured); corroborated `org/mcp/inbox/1.0.0_SA_CTO/read/20260811T143108Z_0.7.0_AE_CloudOps_comp-freshness_canonical_ADD_LANDED__e5e.md:16` (08-10 instance) | **MEASURED**, live comp-freshness read |
| **Schwab (mdpf)** | Morning-ready | Andrew-direct verbatim, `ANDREW_DIRECT_20260811_PHASE_FRAMEWORK_FORMALIZE_UNIFIED_MORNING_DEBT_BRIEF.md:12`: *"mdpf they certainly are [good to go by the morning]"* | **SOVEREIGN-STATED** |
| **cot rebalancer bronze pull** | Currently `cron(0 6 * * ? *)` = 06:00Z | `infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf:171` — comment marks it **PLACEHOLDER**, "exact time = CTO/WS-4 chain-timing confirm" | **DEPLOYED VALUE, UNRULED** — not yet a measured/ruled anchor |

**Correction to the commission's own framing:** the commission cites *"Orion lands ~14:16Z today (the 45-min inversion vs the 13:31Z consolidator read)."* The 13:31Z figure is **not a read of Orion's own data** — it is the timestamp a **comp-freshness/inflection freshness-check lambda fires**, which structurally precedes Orion's actual daily landing by ~45 minutes (`org/mcp/inbox/0.7.0_AE_CloudOps/read/20260811T143219Z_1.0.0_SA_CTO_Freshness_ADD_VALIDATED___both_condition.md:6`: *"THE 45-MINUTE SCHEDULING-ORDER FACT (the 13:31Z lambda read structurally precedes Orion's ~14:16Z daily landing) is a P2-TIMING KEYSTONE... it means the bar's inflection read will show a same-day 'gap' EVERY day by construction until P2 re-orders the morning."*). This matters for §5: it is not "Orion vs. a consolidator," it is **"a freshness check firing before its own vendor's data exists" — a wrongly-timed CHECK, not a wrongly-timed vendor.**

---

## 2. THE ANCHOR MAP

**Method, named per the commission's ask:** the **N-date timing sample** pattern — run the pipeline stage in question across a historical date range (ad-hoc QA, run-and-read, never standing/never production evidence — CLAUDE.md's ad-hoc-permitted rule), measure wall-clock per date, extrapolate with a stated uniform-cost assumption. Precedent: the COO-authorized 20-date sample (`org/critical_paths/change_management/20260811T1750Z_49f-canonical-window-backfill.md:8`, actually run at n=59, "59/59 rc=0; ~15 min warm extrapolation, stated as an extrapolation with uniform-cost assumption"). **This is the sanctioned measurement method for every pipeline below that does not yet have one; it is explicitly NOT a standing comparator (CLAUDE.md shadow-pipeline veto) — one bounded run, read, done.**

**Per-pipeline anchor = mdpf-floor (13:30Z) MINUS measured chain-duration**, per the commission's formula:

| Pipeline | Silver/input readiness | Measured chain-duration | Anchor status |
|---|---|---|---|
| **mdpf** | Schwab, morning | Floor 13:30Z -> accrual 14:10Z (+40m) -> publisher 14:20Z (+10m) = **~50min measured chain** (`infra/aws/terraform/mdpf-pipeline/{scheduled-floor,accrual-bridge}.tf`, `opal-assets/mdpf_portal_publisher.tf:225`) | **RULED** (Andrew ~2334Z 08-10; already the reference pipeline) |
| **49F/bd** | Pull 02:30Z, reattempt 04:30Z, silver-convert 03:05Z (`opal-assets/bd49f_{pull,convert}.tf`) — silver ready by ~04:30Z, **~9 hours of margin** before the mdpf floor | Not yet N-date measured for the A+B+C gold chain | **PROPOSED, NOT RULED, AND STALE RELATIVE TO THE UNIFIED-MORNING DIRECTIVE:** CVO's Group W spec proposed "A+B+C on ONE dispatch, clock floor daily 14:30Z" (`SPEC_49F_GROUP_W_WIRING_20260811.md:45-46`) — **later than mdpf's own floor**, and written *before* Andrew's ~1750Z unified-schedule word. Given ~9h of silver margin, there is no vendor-timing reason 49F gold cannot floor at-or-before 13:30Z. **Recommend an N-date sample on the A+B+C chain to fix a floor ≤13:30Z; this is a retarget of an already-PROPOSED value, not a new build.** |
| **cot** | BD-REST settles 05:02Z ET (09:02Z); ruling directs the session→bronze→silver→assets-mirror chain to "morning hours, completing before the mdpf floor (13:30Z)" with *"exact anchor = implementing lane's choice within (05:02 ET, floor − chain-duration)"* (`ANDREW_DIRECT_20260811_BD_REST_0102ET_COT_MORNING_SCHEDULE.md:19-21`) | **UNMEASURED** — no N-date sample run yet on the cot session-chain | **RULED IN DIRECTION, NOT IN VALUE.** The rebalancer-bronze placeholder (06:00Z) is itself inside the ruled window but is explicitly marked unconfirmed by its own comment. **Gap: an N-date sample on the cot session→silver chain is a P2 prerequisite before AE can implement a specific cron value, not just "morning."** |
| **inf** | Orion lands ~14:16Z — **after** the mdpf floor | Existing chain spans crons from 12:05Z (JWT prefetch) through 13:17-13:47Z (reps/accounts/assets/positions/txn) to 14:22-14:47Z (billing/performance) to 19:30Z (NNA checker) (`infra/aws/terraform/inf-pipeline/*.tf`) | **CANNOT close before the floor on Orion-sourced legs, structurally — see §5.** This is the finding the commission asked the spec to surface rather than assume past. |

---

## 3. THE FLOORS

**Law (NEVER#4, CLAUDE.md):** *"A PRODUCTION PIPELINE MUST HAVE A SCHEDULE... a pipeline whose only trigger is another pipeline's success has no schedule and is a defect."* Composed with the ~0757Z ruling (`ANDREW_DIRECT_20260811_GOLD_PARQUET_AND_SILVER_EVENT_TRIGGER.md:19-26`): the **silver-completeness event trigger is now REQUIRED per firm** (not optional) as an **ACCELERATOR**, and **the clock floor remains beneath it always** — event-only stays prohibited (the mdpf/INF starvation class, measured twice: mdpf's 11-day freeze on a dead upstream sentinel, INF's 9-day freeze on the same shape).

**Group W atoms (A1-A5 per leg) exist today only for mdpf and 49F** (`GROUP_W_MDPF_WIRING_20260811.md`, `SPEC_49F_GROUP_W_WIRING_20260811.md`) — **comp-find confirms zero Group W pages for inf or cot** (`comp-find --name "*group.w*inf*"` / `*cot*` — measured 0/25,498 files). This spec does not attempt to author full Group W pages for inf/cot (that is COO/CVO build-decomposition territory per the mdpf/49F precedent); it names the gap so P2 does not silently skip two of four pipelines:

- **inf:** needs its own A1-A5 declaration before a floor can be RULED (not just observed from current crons). The silver-completeness event trigger for inf is not confirmed built (only spec'd for mdpf/49F so far) — named blocker for AE.
- **cot:** the BD-REST ruling supplies A2/A3 direction; A1/A4/A5 (write-cardinality, re-delivery, settle window) are undeclared. Named blocker for AE, same class.

**Dispatch-path census (both EventBridge namespaces):** *"schedule-existence questions MUST sweep BOTH EventBridge namespaces (`events list-rules` AND `scheduler list-schedules`) — a single-namespace sweep returns a clean, complete-looking absence"* (`SSOT_RECON_MATRIX_20260811.md:84-87`). **Required for every pipeline touched in P2 before a floor is called final** — a namespace-blind sweep cannot tell "no schedule" from "schedule lives in the namespace you didn't check." I could not independently locate the specific "10:20Z same-S3-event replay" specimen the commission cited as the live example (searched by timestamp and by description across `org/` — not found; flagged in §6 rather than fabricated).

**Mutex + mode-homing** (carried from the 49F Group W spec, applies estate-wide per the ratified composition law): one host-level lock per runner, refuses loud under a live lock; run mode resolves once at dispatch and propagates via env to every stage.

---

## 4. WHAT NOT TO DO

- **No alarms/monitors/SNS/SES/freshness-checkers** for any of this, absent Andrew's explicit word (CLAUDE.md moratorium, Andrew-direct 2026-07-28, verbatim: *"We need to establish a moratorium on blindly creating alerts and SES and so on unless I explicitly ask for it. It is an anti-pattern"*). Nothing in this spec proposes one.
- **comp-freshness entries revise AFTER each retime PROVES, never before.** The BD-REST ruling states this explicitly for cot (`ANDREW_DIRECT_20260811_BD_REST_0102ET_COT_MORNING_SCHEDULE.md:23-26`: entries "are correct descriptions of the CURRENT schedule until the schedule moves") — the same rule applies to every comp-freshness entry touched by a 49F/inf retime under this spec. **The instrument describes what RUNS, not what is planned.**
- **The D+2 framework is retired-by-ruling; do not carry it forward.** It was a CSV-export-channel artifact, not a BD REST property (same source, `:16-18`). Do not re-derive a D+2 tolerance for any pipeline under this spec.

---

## 5. THE ADVI-MORNING-READY VERIFICATION (the deliverable the commission actually asked for)

Andrew's premise: *"I suspect they [rest endpoints] are probably fine for ADVI too, so I'd like a unified schedule."* Verified per vendor:

- **49F/bd REST — VERIFIED MORNING-READY.** BD REST lands D+1 01:02 ET (05:02Z), ~8.5 hours of margin before the mdpf floor. The premise holds cleanly for this leg.
- **inf/Orion — NOT VERIFIED MORNING-READY; the premise does not hold as measured.** Orion's own daily landing (~14:16Z) is **after** the mdpf floor (13:30Z) and after the existing freshness-check's own read (13:31Z) by ~45 minutes. Under a floor at-or-before 13:30Z, any inf leg sourced from Orion is **structurally reading stale (pre-landing) data every single day, by construction** — not an intermittent gap, a scheduled one.

**This is not a new problem — mdpf already has a ratified answer for the identical shape, on its OWN read of Orion data**, per the mdpf floor terraform's own comment (`scheduled-floor.tf:120-127`, DS-option-A / COO-endorsed): mdpf's floor fires on **measured vendor hours**, orion-mirror legs read **latest-settled-at-floor-time, carry/participation-labeled per the ruled honesty**, and **heal to full T-1 when Orion lands, via an event accelerator** — never blocking the floor, never silently presenting stale data as complete.

**The open question this spec surfaces rather than resolves:** does INF's own gold runner (as opposed to mdpf's read of INF's silver) need the identical carry-forward + accelerator-heal treatment, or does an ADVI-specific floor genuinely need to sit later than 14:16Z plus inf's own measured chain margin — which would be a **schedule fork**, not a unified one, and contradicts the "unified" half of Andrew's word. **I am not ruling this either way — it is a genuine tradeoff (unification vs. Orion's fixed landing time) that the commission's own protocol routes to CVO review -> CTO ratify -> Andrew where it bounds the directive.** Recommend the mdpf pattern (carry-forward + accelerator-heal, one unified floor) as the default unless CTO/Andrew prefer a later ADVI-specific floor; either way this is a **named decision point for P2 ratification, not a closed item.**

---

## 6. OPEN GAPS (marked, not silently absorbed)

- **cot session-chain duration:** unmeasured: an N-date sample is a P2 prerequisite (§2).
- **inf/cot Group W A1-A5 pages:** do not exist; comp-find confirms zero hits (§3).
- **"10:20Z same-S3-event replay" specimen** cited in the commission: not located after a reasonable search of `org/`. Either a different naming/date than searched, or not yet committed to the record. Flagging rather than fabricating a source.
- **Whether inf's own silver-completeness event trigger is built** (as opposed to spec'd for mdpf/49F): not confirmed either way in this pass — named for AE/CTO to close before P2-open.

---

## Acceptance criteria (for CVO review)

- Every vendor-timing claim above traces to a captured artifact (table in §1) — none inferred.
- The ADVI-morning-ready premise is given a explicit VERIFIED / NOT-VERIFIED verdict per vendor (§5), not a single estate-wide yes/no.
- Every floor proposal states its measurement method (N-date sample) and whether that method has actually been run yet, per pipeline (§2).
- No new alarm/monitor/comparator proposed anywhere in this document (§4 self-check).
- Gaps are named with an owner-shaped next step, not left implicit (§6).

-- 4.0.0_SA_CRO
