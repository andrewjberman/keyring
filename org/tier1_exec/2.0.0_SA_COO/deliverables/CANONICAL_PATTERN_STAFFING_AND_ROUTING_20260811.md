# CANONICAL-PATTERN PROGRAM — COO STAFFING + SEQUENCING REGISTER

**Author:** 2.0.0_SA_COO · **Date:** 2026-08-11 (Tuesday) ~0525Z · **HEAD:** @8ad0d6b641
**Boot payload:** `org/tier1_exec/1.0.0_SA_CTO/handoffs/2026-08-11_0503Z.md` @1a518b303f — this file is
its **COO half** (SELF DO-FIRST item 5, staffing + sequencing).
**Discipline:** ITEM_0 landing-plan (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ITEM_0_LANDING_PLAN_20260810.md`)
— **every act carries an OWNER + a TRIGGER + a NAMED PRECONDITION.** *"An act with no trigger is the
failure mode."* MDPF repair keeps engineering priority. This register **INFORMS and ROUTES; it GATES
NOTHING** — no act below is an approval step (CLAUDE.md no-inferred-gates).

---

## 0 · SEATING REALITY AS MEASURED (the actual constraint on this program)

`get_live_agents` @0521Z — **4 live:** `0.0.0_AB_MSTR`, `0.4.0_DS_ClientPlatform` (IDLE),
`4.0.0_SA_CRO` (idle/event-driven), `4.0.0_SA_CRO~A` (idle/event-driven).

⚠ **BOTH of the program's named gate-holders are UNSEATED:** `1.0.0_SA_CTO` (owes the unified pattern
spec + the ordered cutover sequence) and `3.0.0_SA_CVO` (owes the Rule-14e certification that gates
the cutover). `0.7.0_AE_CloudOps` is also unseated and owns C-3. **This is a capacity fact, not a
gate** — spawn authority is MSTR's (`/mstr-spawn`); surfaced to MSTR, not held on.

**Consequence for sequencing, stated plainly:** §2 (the cutover) cannot be *dispatched* tonight — it
needs CTO's ordered sequence and CVO's cert, and neither seat exists. §1 (three DS/AE landing acts) is
**fully dispatchable now** and does not touch the cutover. So §1 goes out this turn and §2 is staffed
as a frame that a CTO/CVO respawn drops into.

---

## 1 · DISPATCHABLE NOW — the three landing acts

### ACT R-1 · INF Sunday full-pull must UNION-PRESERVE departed accounts (⏰ HARD DATE)

| field | value |
|---|---|
| **OWNER** | `0.4.0_DS_ClientPlatform` (Rule 13: `data/inf/scripts/gold/*.py` is DS's full commit→QA-deploy cycle) |
| **DRAFTER** | `4.0.0_SA_CRO~A` — offered the diff for DS review @051637Z; accepted, to make the DS wake cheap |
| **TRIGGER** | **NOW.** Deadline-driven, not event-driven |
| **PRECONDITION** | none blocking. Two *ordering* preconditions inside the act, below |
| **DEADLINE** | **must be live before Sunday 2026-08-16** (5 days) — the full-pull branch auto-detects Sunday |

**Why it is existential and not hygiene:** `pull_inflection_transactions_rest.py`'s full-pull branch
rebuilds the snapshot from per-account inception pulls over the **CURRENT universe**. The 16 cancelled
accounts are no longer in that universe, so Sunday 08-16 **re-erases the 26,371 rows CRO~A restored
tonight**, and the F7 guard then correctly re-freezes the chain Monday 08-17. The repair that just
landed is undone by a scheduled job unless this ships first.

**NAMED ORDERING PRECONDITION (a) — the script is DEPLOYED-ONLY (`MISSING_IN_REPO`).** S3
`code/gold/`, LastModified 07-02, no repo counterpart. **Land it in two commits, not one:**
1. **baseline commit** — the *deployed artifact byte-exact* into `data/inf/scripts/gold/`, **no deploy**;
2. **fix commit** — union-preserve on top; **then** deploy.
Collapsing these deploys a *reconstruction* over live code, and any deployed-vs-authored drift ships
silently. This is the "which is RUNNING vs which is RIGHT" class (CLAUDE.md 17b) — the baseline commit
is what makes the answer recoverable.
> **Known friction, DS's call, not prescribed:** Rule 15 requires `from __future__ import annotations`
> and the commit-gate enforces it (ADHC_DSFLOW.004), so a *byte-exact* baseline may fail the gate. If
> so, land the minimal gate-required delta and **record the exact deployed-vs-committed diff in the
> commit message** — the delta must be visible, not absorbed.

**NAMED ORDERING PRECONDITION (b) — bar-window non-interference (cheap to discharge).** Confirm the
edit is confined to the **Sunday-only** full-pull branch and no path executing inside today's
13:02Z–15:05Z MDPF cadence reads the changed function. If confirmed, this lands *independently of the
13:30Z bar*. If not, the deploy waits for the bar; the commits do not.

**ACCEPTANCE:** union-preserve verified against the restored snapshot (departed-account rows survive a
simulated full-pull), plus `comp-pipescript deployed` MATCH on the inf tree. ⚠ **Do not accept on
`comp-pipescript deployed` alone** — it read MATCH while executing code was 4 days stale during
tonight's window (instrument gap, routed to CTO).

---

### ACT R-2 · C-2 retry-net double-lag (Cottonwood bronze ingest)

| field | value |
|---|---|
| **OWNER** | `0.4.0_DS_ClientPlatform` (bronze ingest script, Rule 13) |
| **SPEC** | `MDPF_SCHEDULING_JAM_STRATEGY_20260811.md` §4 Move 3 — as-of dates passed to a window builder that does not re-apply the lag: `cot_bronze_ingest.py:1135` + `:306-320` |
| **TRIGGER** | **NOW** for the fix + review; **deploy** per the precondition below |
| **PRECONDITION** | the cot ingest runs **18:30 ET (~22:30Z)** — after today's bar. DS confirms no MDPF-window leg reads the changed function before 13:30Z; if it does, deploy after the bar |
| **NOT GATED ON** | Andrew's Move-2 ruling — CRO~A's own measurement: *"correct under EITHER Move-2 answer, so they need not wait on it"* |

**⚖ THE "HIS NOD" CLAUSE IS DISSOLVED, AND THIS IS THE RULING THAT SAYS SO.** The strategy doc §6.4
reads *"C-2/C-3 routing is COO-lane once he nods at the direction."* My predecessor ruled that
wait-on-Andrew condition **manufactured** at 0403Z and dissolved it; MSTR carried the dissolution
forward at 051832Z. I **affirm** it: single-function mechanical corrections with no policy content,
inside an existing nightly, no new paths, no schedule change. CLAUDE.md's no-inferred-gates rule names
*"an exec's own routing habit"* as exactly the source a gate may **not** be manufactured from. No
Andrew nod is required and none is being waited on. *(An approval nobody asked for is invisible to
Andrew — work he believes is moving sits held on an approver he does not know exists.)*

---

### ACT R-3 · C-3 sweep/primary order (probe-day universe)

| field | value |
|---|---|
| **OWNER** | `0.7.0_AE_CloudOps` — **UNSEATED.** Infra/Terraform lane per Rule 13 |
| **SPEC** | strategy §4 Move 3 — `ssm.tf:143` vs `:165` |
| **TRIGGER** | AE seat exists (TO delivered to its inbox, wakes with the seat) |
| **PRECONDITION** | `safe-apply` (never bare `terraform apply`) **+** AE confirms the apply's blast radius does not touch a leg inside today's 13:02Z–15:05Z cadence — if it does, apply after the bar closes |
| **ROUTED** | TO to AE inbox now; spawn need surfaced to MSTR (spawn authority is MSTR's, not mine) |

---

### ACT R-4 · F4 D_04 non-fee-AUA residual → CLASSIFICATION (ready-to-land)

| field | value |
|---|---|
| **OWNER** | `0.4.0_DS_ClientPlatform` |
| **DRAFTER** | `4.0.0_SA_CRO~A` — diff already committed @ec874f6a8d, *"ready-to-land diff for the DS lane via COO wake-point"* |
| **TRIGGER** | **NOW** — lowest cost of the four; the diff exists |
| **PRECONDITION** | none. It is a *classification + surfacing* change (`unreconciled_aua`), not a revaluation — it must not silently reopen C-1 (revaluation asymmetry, live at Andrew via CTO). DS confirms the diff changes labelling/surfacing only |

> **Why R-4 is dispatched and not banked:** *items that cost nothing are the ones that quietly never
> happen* (ITEM_0's organizing principle, my own form). A ready-to-land diff with no precondition is
> the single most likely act in this register to still be sitting here in a month.

**DS QUEUE ORDER: R-1 → R-4 → R-2.** R-1 first on the hard date; R-4 second because it is drafted and
free; R-2 third — its runtime is 22:30Z tonight, so it has the most slack of the three. DS may reorder
R-4/R-2 on its own readiness read; **R-1 stays first.**

---

## 2 · THE MDPF CUTOVER — staffing frame (NOT dispatchable tonight)

Grounded on the CRO decomp Part A3 @41692cd3d2. **STATUS = DRY, UNCERTIFIED.** Per the handoff, CVO
must certify before any act touches the live client-facing chain. **`opal-data-mdpf` is LOAD-BEARING
LIVE — MIGRATE-BEFORE-KILL, never a delete** (3 feeds written 03:30Z tonight; per-firm bells exercised
08-10; both EC2 legs boot from it; DS deploys into it).

"Kill the EC2 chain" is **FOUR separable acts**, not one:

| Act | What re-homes | Proposed owner | TRIGGER | NAMED PRECONDITION |
|---|---|---|---|---|
| **X-i** | Feeder writes (`non_model_aua`, `etf_net_assets`, inflection feeds, bronze) — **the client-facing smartx read edge migrates WITH this** | DS (scripts) + AE (infra) | CVO cert **and** CTO's ordered sequence | ⛔ **per-firm 49financial + inflection `account-distribution` bells are LIVE and client-facing — they must not break.** Cottonwood + global + the flat key are FROZEN 07-23 by CTO ruling and are *deliberately* frozen, not broken. Underscore-in-gold / hyphen-in-platinum spelling law holds per layer |
| **X-ii** | The aggregate (`gold/mdpf_revamp/_aggregate_aua` staging → the floor consumes it) | AE | after X-i | W1a already staged the consumer-side repoint — **verify that staging is still valid before reusing it**, do not assume. The floor and the chain are **SERIES-COUPLED, not parallel** (the false fork) |
| **X-iii** | Accrual's `partner_roster` + code sync | DS + AE | after X-i | **atom 6: config NEVER in the code store** — `partner_roster.json` is the measured violation; this act is where it is fixed, not carried over. Derive the roster from the partner roster, never a literal count |
| **X-iv** | Delete the 2 already-IAM-dead stages (3.5 legacy-emit, 5 OWNTS) | AE | independent of X-i..X-iii | **already IAM-severed = the only genuinely low-risk act here.** Still a deletion: confirm dead on the live primitive (not the comp-tool DESIRED view) before removing |

**Two program-level preconditions that sit above all four acts, and neither is mine to discharge:**
1. **CVO Rule-14e certification** of the decomp ground truth (@41692cd3d2). *Do not cut a live
   client-facing pipeline on an uncertified rectangle.*
2. **Andrew's ratified must-calculate exception set** for atom 8 (raw-from-endpoint). Open at him since
   0500Z: is it `{net-new-assets [FLOW] + non-fee-AUA residual [BALANCE] + cross-account rollups}`,
   everything else raw — or is the non-fee residual itself retired for a raw pull?
   ⚠ **NNA (net new assets) and the non-fee-AUA residual are TWO calculated nodes, never one.** CTO
   conflated them 0455Z, Andrew caught it, corrected by 0458Z. **Do not re-merge.**

**A schedule floor belongs on every leg in this cutover (atom 5).** The chain's trigger has been dark
**11 days** (INF sentinel last wrote 2026-07-31T14:56:49Z) and nothing floored it — CLAUDE.md's
only-trigger-is-another-pipeline's-success defect, measured live again. Any re-homed leg that ships
without a clock floor reproduces it. *Event accelerates; clock floors.*

---

## 3 · 13:30Z BAR — today, ~8h out

**OWNER: this seat.** Face **12/12 on the ratified basis** (@e82326bdb2, Andrew VERBATIM *"Point-in-time,
history does not restate"* — the ruled table is tonight's exact collision). Adjudicate against the
Amendment-III interpretation table, **pre-registered before the evidence exists** (predecessor,
@4c10918958 — the discipline earned its keep twice in tonight's window). Record as an **ADDENDUM** to
`org/critical_paths/change_management/20260811T0150Z_mdpf-atomic-window.md`.
Non-cottonwood degradation = **failure, loud.**

⛔ **NOTHING IS ARMED AGAINST THIS BAR AND NOTHING WILL BE** — the alerts/monitors moratorium, and it
is the correct call: an unattended bar is *evidence about whether the schedule works*, and a watcher on
it measures the watcher. Zero crons at this seat (LD-0288/0289/0293; Step 1b-F COO row carries no live
scoped authorization — the 08-06 `/drive` re-arm was DISCHARGED 08-07).

⚠ **CONTINUITY RISK, NAMED:** the bar is ~8h out and this session may not live that long. The duty is
durable in the ledger with COO named, and is restated here. **A successor COO inherits it from these
two records, not from recollection.** Also relevant to the bar-day picture: CRO~A's INF QA chain run
`6a92d696` and the 13:47Z scheduled cycle are the **production proof** — the scheduled run is the
evidence, never the ad-hoc one.

---

## 4 · REMEDIATION REGISTER (ITEM_0 R-4b — a file with a path, not a norm)

*Norms decay, registers accumulate.* Mid-implementation slips get **one banked line here** and a second
pass — they do not break flow.

| # | Slip / residual | Owner | State |
|---|---|---|---|
| 1 | `comp-pipescript deployed` is structurally blind to the Lambda-zip code channel (returned MATCH while executing code was 4 days stale) | CTO (instrument roster) | OPEN — routed 031216Z. **Named in R-1's acceptance so it cannot be leaned on** |
| 2 | `comp-pipescript deployed` rendered 1 of mdpf's 6 code layers (7/49 objects, denominator unstated) | CTO | OPEN |
| 3 | `comp-estate` served rows carried a 404 platinum key + runner conflation | CTO | OPEN |
| 4 | Two live code channels + 17b grammar observation | CTO (DS-flagged 033615Z) | OPEN |
| 5 | C-1 revaluation asymmetry / conversion policy | CTO → Andrew | OPEN, live |
| 6 | Estate-wide point-in-time extension census | CTO | OPEN, diagnostic |
| 7 | Cottonwood deep-rekey adjudication | CTO (causation thread) | OPEN, deliberately not parallel-read |
| 8 | `MISSING_IN_REPO`: deployed-only gold scripts with no repo counterpart (R-1's script is one; the decomp measured **4 more** in the assets_gold layer) | DS + CTO | OPEN — R-1 closes one instance; **the class is not closed by it** |
| 9 | 2 unpushed local commits (audit-archive baseline + snapshot, @f639b23c1f/@8ad0d6b641) | MSTR (sole shared-branch integrator, LD-0367 r2 / LD-0368) | surfaced this turn |

---

## 5 · WHAT THIS REGISTER DELIBERATELY DOES NOT DO

No new gates (none asked for; one dissolved). No monitors/alerts/freshness checkers (moratorium). No
shadow or parallel channel to de-risk the cutover — **build correctly and port over** (Andrew's
complete veto; a standing comparator is vetoed on the same grounds). No engineering staffed against
the MDPF repair's priority. No spawn decisions — that is MSTR's authority. And no act above lands
"when someone gets to it."
