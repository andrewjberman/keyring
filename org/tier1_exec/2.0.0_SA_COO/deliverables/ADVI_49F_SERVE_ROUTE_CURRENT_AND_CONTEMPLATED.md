# ADVI 49F — SERVE ROUTE: CURRENT vs CONTEMPLATED, and the HOLD

**Author:** `2.0.0_SA_COO` · 2026-08-21 · **Status:** ACTIVE HOLD (Andrew-direct, below)
**Purpose:** the switch reference — what serves 49 Financial Advisor Intelligence today, what is

> **LANE NOTE:** authored for `docs/architecture/`; the owned-paths gate correctly refused a COO
> commit there (lane `ANY_CTO`). Landed in the COO deliverables tree instead, un-overridden.
> **CTO: promote to `docs/architecture/` if you want it in the architecture set** -- the content is
> lane-agnostic and I did not use the audited override to place it myself.
contemplated, which resources and paths each route uses, and the two conditions that gate the switch.
Written so a seat with no session context can act on it.

---

## 0. THE RULING — Andrew-direct 2026-08-21

> **"the position on flipping this should be held until source gaps and schedule are addressed, that
> needs to be documented, including relevant publisher resources, paths, and etc for the switch
> covering what is the current route and what is the contemplated route."**

**TWO CONDITIONS, BOTH REQUIRED, NEITHER SUFFICIENT ALONE — §4.** The hold is on the FLIP (pointing the
product at the canonical twins). It is **not** a hold on building toward it, on the canonical chain
(which runs daily and should keep running), or on the BD-migration work.

**STRATEGIC FRAME (Andrew-direct, same session):** *"if 49 gets off Black Diamond (which is the goal,
we are trying to replace this function for them), then these 'custom' dim tables that provide these
non-schwab data points, are going to need to be hosted by them direct."* The switch is therefore not
only a serve re-point; it is a **source-ownership migration** — §5.

---

## 1. CURRENT ROUTE — LIVE, and what a 49F advisor sees right now

| leg | resource / path |
|---|---|
| **Served artifacts** | `s3://opal-data-bd/platinum/firm/*.json` |
| **Producers** | the D-series family emitters, `data/assets/scripts/gold/runners_49f/d01…d14` (`d01_firm_header_metrics`, `d02_firm_dashboard`, `d03_firm_fee_efficiency`, `d06_firm_mix_summary`, `d07_firm_leaderboard`, `d08_firm_ownership_map`, `d09_firm_timeseries_overview`, `d10_firm_cumulative_chart`, `d14_advisor_nna_canonical`, …). Each declares its own `FAMILY = "platinum/firm/<leaf>"`. |
| **Refresh** | the **04:00Z serve of record**, true landing ~05:27–05:43Z (R1 rider, CTO `@9988b2dd66`). Measured 2026-08-21: all `platinum/firm/*` LM 05:27:53–05:43:21Z. |
| **Content frontier** | `data_as_of` = **T-2** at any morning read. This is the ACCEPTED steady state (CTO R1 ACCEPT-WITH-RECORD), **not** a staleness defect — see NEVER#1. |
| **Richness (measured 2026-08-21)** | `timeseries_chart.json` **37,006,983 B** (≈6.6 yrs, 2020-01-02→) · `leaderboard.json` 1,625,301 B (**163 advisors**) · `advisor_nna_canonical.json` 3,867,607 B · nine geo states · nine offices |
| **Reader** | the deployed portal PROD bundle, `origin/PROD` @ `8a96c916` — requests LEGACY urls |

⚠ **UNMEASURED AT THIS SEAT — one gap, named rather than guessed:** the 04:00Z producer act is **NOT**
an EventBridge Scheduler entry and **NOT** an EventBridge rule (both enumerated; no 49F/ADVI schedule
in the 03:xx–05:xx window). It is most likely an **on-host cron on the bd EC2 plane** or an
event-chain off `bd-49f-session-*`. **Whoever owns the switch must identify it by name before
decommissioning anything** — a route swap that leaves an unidentified producer running is how two
writers end up on one key.

---

## 2. CONTEMPLATED ROUTE — BUILT, EXERCISED, and NOT LIVE

| leg | resource / path |
|---|---|
| **Canonical source** | `s3://opal-data-49financial/gold/advi/{dimensions,canonical,reference}/…` |
| **Canonical schedule** | **`advi-49f-gold-floor`** — `cron(45 12 * * ? *)` = **12:45Z**, **ENABLED**. Runs daily; T-1 derived via `prev_trading_day`. |
| **Twin publisher (code)** | `data/assets/scripts/gold/runners_49f/d_publisher_port.py` — reads canonical + JD2, writes the twins. Grant-gated (`OPAL_ADVI_PUBLISH_GRANT=1 --publish`). |
| **Twin publisher (schedule)** | **`advi-49f-publisher`** — `cron(15 13 * * ? *)` = 13:15Z, target `arn:aws:lambda:us-east-1:313476888478:function:advi-49f-gold-dispatch` — **⛔ DISABLED** |
| **Twin artifacts** | `s3://opal-data-portal-v2/platinum/advi/49financial/*.json` + `_manifests/{asof}/{run}.json` + `_manifests/latest.json` |
| **Twin state (2026-08-21)** | **FROZEN at 15:04:19Z** — a MANUAL publish. Nothing refreshes them. |
| **Edge route** | CloudFront **advisor-intelligence** router, remedy (A): path-class override — keys matching `platinum/advi/{firm}/` resolve `bucket=opal-data-portal-v2`; everything else keeps `FIRM_CONFIG`. OAI **`E139998VWH0PD`**, `s3:GetObject` scoped to `platinum/advi/*`. Tenant assertion enforced (cross-firm → 401 *Firm scope mismatch*). Edge v24/v5, tag `portal-auth-v1.23.0`. **LIVE.** |
| **Reader** | `portal/src/api/endpoints/adviKeyRepoint.ts` — `ADVI_ROUTE_LIVE` + the `ADVI_REPOINT` registry (state as DATA, so a held key structurally cannot prefer the twin). |
| **Registry state** | **FLIP 1 / HELD 13 / STRUCTURAL 1** (the P4E-1 frozen list of 15). The one FLIP key is `clients-tab-slim`, which has **no portal reader** — so nothing client-visible currently differs. |

> **Counting note for any future census of `adviKeyRepoint.ts`:** a bare `grep "state: 'flip'"`
> **over-counts** — the file contains a TYPE DECLARATION line. Filter to registry rows first:
> `grep "leaf: '" | grep -oE "state: '(flip|held|structural)'"`. The file carries its own marker.

---

## 3. WHY THE SWITCH DID NOT HAPPEN 2026-08-21 — the finding, not a failure

The chain executed correctly end to end: pins (`@28bb34a56d`, 4,613,107 fields, **zero undeclared
divergences**), Rule-14e certs, the route act, the flip, five PARITY_BAR §8 legs, never-widen verified
at BOTH the listing and consumer planes (**zero twin requests per held key**).

**What failed was SOURCE READINESS AT THE PRODUCT PLANE.** DE's complete pass measured material
regressions on **9 of 10** certified keys; only `clients-tab-slim` (no portal reader) came back clean.

⛔ **THE LESSON WORTH KEEPING:** every one of those nine sat **inside a DECLARED band** — which is
exactly why the pins read *zero undeclared divergences* and said nothing about any of them. **The pin
instrument was correct throughout.** It answers *"does this value depart from what the pipeline
declared."* The question that mattered was *"would a client notice."* A **9-of-10 miss rate against
the second question is the measurable distance between those two planes**, and no rigor inside the
first would have closed it. Certs cover ROUTE and VALUE; they are **not** product clearance and must
not be cited as such (CVO wrote that limit into the cert itself, `@ab585bb00e`).

---

## 4. THE TWO HOLD CONDITIONS

### (A) SOURCE GAPS — three, with different costs. Do not card them together.

| gap | measured state | cost class |
|---|---|---|
| **History** | canonical series = **529 partitions, 2024-07-08 → 2026-08-20**; the twin's floor IS its source's first day. ⛔ **THE "TREE-WIDE FLOOR" CLAIM IS FALSIFIED — SEE THE CORRECTION BLOCK BELOW THIS TABLE.** | **STILL PROBABLY SOURCE-LIMITED, BUT THE STATED BASIS WAS WRONG.** A recompute may or may not extend it; the question is now OPEN, not settled. ⛔ **Do not use the word "backfill" for this** until someone has measured that the history is obtainable — that caution stands and is now doubly warranted. |
| **Geography / state** | canonical dims tree = **eleven dims, none geographic**. BUT `schwab/08335338/silver/fact_acc` carries `ac_st` **100% populated (7,331/7,331), 48 distinct**, top values TX 3,576 / CA 505 / GA 408 / AR 362 / NC 263 / KS 247 / FL 204 — **the legacy chart's own state set** — plus city (1,071), zip (1,587), country, 3 address lines, all 100%. | **NOT source-limited. An UNBUILT DIM over data already held.** A dim build from `fact_acc`, no vendor involved. ⚠ The producer declaration *"geography is a BD-side attribute with no canonical dim"* is TRUE of the canonical layer and MISLEADING about availability. |
| **Office** | `fact_acc.schwab_br_cd` 100% populated, **285 distinct branch codes** vs the legacy product's **NINE offices**. | **UNKNOWN — a GRAIN MISMATCH, not a match.** A Schwab branch code may or may not roll up to a 49F office. **CANDIDATE ONLY**; one measurement settles whether it behaves like state or like history. |
| **Leaderboard** | 163 → 146, **twenty named advisors absent in every window** | **POSSIBLY A BUG, NOT AN EXTENT.** Advisor disappearance is not explained by a missing dimension. Needs its own measurement cell — *"not ready"* and *"broken"* take different answers. |

⛔ **CORRECTION 2026-08-21T20:4xZ (2.0.0_SA_COO, own-lane) — THE HISTORY ROW'S MECHANISM WAS FALSE. MEASURED
LIVE, NEGATIVE-CONTROLLED, DENOMINATOR PRINTED.**

The row read: *"all six Schwab silver tables share earliest 2024-07-08, a **TREE-WIDE** floor."* **Both halves
of that are wrong.**

**MEASURED** — `aws s3 ls s3://opal-data-assets/schwab/08335338/silver/{table}/ | head -1`, **12 of 12 tables
returned an earliest partition** (negative control: a nonexistent table name returns empty, so the instrument
discriminates):

| earliest partition | tables |
|---|---|
| `date=2023-07-12` | **`fact_rld`** — **782 partitions**, dense from that day. **A YEAR DEEPER than the claimed floor.** |
| `date=2023-07-31` | `fact_rly` |
| `date=2023-09-01` | `fact_rlu` · `fact_rtu` |
| `date=2024-07-08` | `dim_asset` `dim_balance` `dim_position` `dim_transaction` `fact_acc` (534 partitions) `fact_fam` `fact_rps` `fact_rps_s2` |

**TWO INDEPENDENT ERRORS:**
1. **"six tables" — THERE ARE TWELVE.** The census that produced the claim covered **half the tree** and the
   number was written as though it were the denominator. *A partial census reported as a total is the exact
   floor-vs-denominator class this estate keeps re-learning.*
2. **"TREE-WIDE" — IT IS NOT.** **Four of twelve floor EARLIER**, the deepest by **almost a full year**.

⛔ **WHAT THIS DOES AND DOES NOT OVERTURN — stated precisely, because the conclusion may well survive:**
- **OVERTURNED:** the *mechanism*. There is no tree-wide 2024-07-08 floor to inherit.
- **NOT ESTABLISHED:** that the canonical series *can* reach deeper. **I have NOT measured which tables the
  canonical series actually consumes**, and the `rl*`/`rtu` family reads like a rolling/derived grain that may
  not be a usable input at all. **That measurement is the open cell.**
- **SO:** *source-limited* is now an **OPEN QUESTION**, not a settled finding. It was recorded as settled on a
  basis that does not hold.

**WHY THIS MATTERS BEYOND THE ROW:** this row is the evidence base for a **sovereign call carried at Andrew**
(*pursue ~4.5 yrs of vendor history, or accept ~2?*). **That call was framed as a cost/scope tradeoff on the
strength of a floor that does not exist.** A decision taken on it would have been taken on a wrong premise —
and the wrongness ran in the direction of *understating* what we already hold.

*Found while grounding the carried call rather than answering it from the record — which is the only reason it
was found at all: the record was internally consistent and confidently wrong.*

### (B) SCHEDULE — the independent leg

**`advi-49f-publisher` IS DISABLED.** The twins have **no enabled producer schedule**. Flipping the
product to them would point it at artifacts nothing refreshes.

⛔ **CLASSIFIED AT SOURCE 2026-08-21 (CTO), AND THE CLASSIFICATION CHANGES THE REMEDY — READ IT BEFORE
TOUCHING THE ENABLE FLAG. THIS IS `DELIBERATELY-HELD`, *NOT* `STALE-BY-NEGLECT`.**
`infra/aws/terraform/opal-assets/advi_49f_publisher.tf` (AE `@1abc54fa4c`, 2026-08-19, OPAL_ADVIPOINTERS
P4-PUBIAM-49F / **P4I-3**) declares `state = "DISABLED"` with the header verbatim:
*"STATE = DISABLED, DELIBERATELY -- THIS IS THE CONTRACTED DESIGN, NOT A HALF-LANDING. The publisher
schedule activates only when DS~B's emitters are deploy-ready."*

**ACTIVATION IS ONE TF CHANGE, THREE STEPS, NAMED IN THAT SAME HEADER:**
1. mint `aws_ssm_document.advi_49f_publisher_dispatch` with DS~B's contracted body (sync `_code` → the
   contracted entrypoint → log upload → conditional self-halt, same frame as the chain document);
2. append its name to the dispatcher's `ALLOWED_DOCUMENTS` env;
3. flip `state` to `ENABLED`.

⛔⛔ **THE OBVIOUS REFLEX — "just re-enable the schedule" — IS WRONG TWICE: it is not the remedy, AND it
fails closed.** Per the header: *"even a stray manual enable fails CLOSED + LOUD -- the dispatcher
refuses any document not on its allowlist, and the named document does not exist."* So a bare enable
buys nothing and produces a loud refusal.

**WHAT ACTUALLY LAPSED — and it is a sharper finding than a missing schedule:** the condition this hold
waited on (**emitters deploy-ready**) **WAS MET 2026-08-21** — they ran, and the twins published
(manually, 15:04Z) — **and nobody fired the activation, because every seat was on the cutover.
A CORRECT HOLD OUTLIVED ITS CONDITION.** That is the Rule-22a classification lesson live: a detector
that cannot tell a deliberate hold from neglect manufactures the wrong reflex, and here the wrong
reflex (`enable`) is also the one the state most invites.

**RELEASE PATH:** the schedule condition is therefore **NOT an open question and NOT a new build** — it
is a **NAMED EXISTING ACT (P4I-3)** with a named owner class (**AE**, the TF author) and a named
contract input (**DS~B's invocation form**: entrypoint + args). The activation TO is COO's to re-ground
at pickup and issue when the hold lifts on BOTH conditions; it does not execute before then, but it
**can be READY**.

⛔ This is the NEVER-rule class ruled after MDPF: *a production pipeline MUST have a schedule; a
pipeline whose only trigger is another pipeline's success has no schedule and is a defect* — MDPF then
froze for six days with fresh inputs sitting unused. **Here it is starker: not event-triggered, but
disabled outright.** Even with every source gap closed, a flip without re-enabling this schedule ships
a frozen product.

**BOTH CONDITIONS MUST CLEAR. Neither is sufficient alone.**

---

## 5. BD-EXCLUSIVE DEPENDENCIES — what 49F must host direct

The chain already treats external-source tables as **JOIN DIMS**: read by date partition (latest
`<= asof`), vintage-stamped, **absent-not-silent**. The framework is **already multi-vendor** — JD1 is
SmartX-scoped and read cross-source by construction — so hosting a custom dim at a new source is a
**SOURCE SWAP INSIDE AN EXISTING PATTERN**, not a new mechanism.

| | source | prefix | supplies | read by | freshness 2026-08-21 |
|---|---|---|---|---|---|
| **JD2** | **Black Diamond** | `blackdiamond/49f/silver/dim_advisor_fee_role/` | advisor **ROLES + fee splits** | `a00_runner.py:51`, `d_publisher_port.py:72` (`:299`) | `date=2026-08-20`, written 07:06:44Z — **FRESH, daily** |
| — | **Black Diamond** | `blackdiamond/49f/silver/dim_account_xref/` | account crosswalk / custodial tail | `a01_dim_relationship.py:50` | `date=2026-08-20`, 07:06:44Z — **FRESH, daily** |
| — | **Black Diamond** | `blackdiamond/49f/silver/fact_bd_allocation/` | BD allocation → portfolio group | `bd49f_dim_portfolio_group.py:79` | `date=2026-08-18` — **BEHIND**, see below |
| **JD1** | SmartX | `smartx/platform/silver/fact_allocation_account_map/` | model membership | `a00_runner.py` | (not BD; listed as the multi-vendor precedent) |

**ABSENCE BEHAVIOUR, verbatim** (`a00_runner.py:129`):
`WARN: join dim 2 absent <= asof -- roles will be None, unbridged=-1 (stated)`
**ROLE PROVENANCE LAW** (`a00_dim_account.py:18`): roles are JD2 FACTS — *"NEVER txn-derived;
unbridged accounts REPORTED, never defaulted."*

**THE ROLE FAN-OUT** — `architect / implementor / consultant / additional_advisor / local_ops` is
consumed by `d03_fee_efficiency`, `d05_client_detail`, `d07_leaderboard`, `d08_ownership_map`,
`d09_timeseries_overview`, `d10_cumulative_chart`, `d14_advisor_nna`. **That is essentially the entire
regressed key set** — the 9-of-10 finding and this dependency map are the same fact from two ends.

⚠ **`fact_bd_allocation` IS ALREADY ON A DEGRADED VENDOR CADENCE, BEFORE ANY MIGRATION.** It matches the
**FRIDAY-ONLY** BD snapshot pattern measured independently 2026-08-21 (`0.6.0_AE_PartnerETL`):
allocations + unrealized land full-size **only on Friday as-ofs, six straight weeks**; weekday pulls
return header-only 0-data-row exports the FIX-1 guard correctly refuses. So it runs up to **four
trading days stale by Thursday** — a vendor-side condition, not a defect in our chain.

### 5a. DESIGN NOTE FOR THE HANDOFF
JD2's absence path warns and sets roles `None` / `unbridged=-1` — **loud in a log, and the DOWNSTREAM
consequence is views collapsing to `other`/`unassigned` while the pipeline reports itself healthy.**
If 49F self-hosts these tables, that absence path becomes THEIR operational responsibility and would
present as *"the warning fired in a log nobody read."* **Design the handoff so a missing custom dim
fails where a person sees it** — noting the standing monitoring moratorium makes this a
ROUTE-AND-OWNERSHIP question, not an alerting build.

---

## 6. WHAT IS BUILT AND STANDS — do not rebuild

Route act (edge + OAI + tenant assertion) · `ADVI_REPOINT` registry with state-as-data · per-key
never-widen machinery · pins `@28bb34a56d` · Rule-14e certs `@5c004cacf6`/`@ec0933f6d5` (with the
plane limit written in at `@ab585bb00e`) · POST-FLIP five-leg file · the OR-series flip oracles
(including **inverted oracles on held rows** — the only detector that stays true if the registry
module itself is edited).

**A re-flip is ONE WORD PER ROW in the registry.** That is what makes this hold cheap and the
eventual switch cheap.

---

## 7. OPEN / UNMEASURED — the honest boundary

1. **The 04:00Z legacy producer resource** (§1) — must be named before decommissioning.
2. **Why the twins lose roles** with JD2 present, fresh, and demonstrably read by the publisher
   (`d_publisher_port.py:299`). **The loss is DOWNSTREAM of the read** — join or compute step. Not yet traced.
3. **Office grain** (§4A).
4. **Leaderboard −20** — bug vs extent (§4A).
5. **Completeness of the BD census.** It keyed on the literal `blackdiamond` token, and only **~11% of
   in-scope S3 key call sites NAME their key** (AE, measured) — the rest build keys generatively. **This
   map is a FLOOR, not a denominator.**

**Session record:** LD-0429 / LD-0441 / LD-0442; `MDPF_PROVCANON` PRD; `BD_EXCLUSIVE_DEPENDENCY_MAP_49F_20260821.md`.
