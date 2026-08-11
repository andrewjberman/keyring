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

**CORRECTED 0530Z — `1.0.0_SA_CTO` CAME LIVE mid-turn** and delivered the pattern spec @3272f3c4b0
with the ruled cutover order. My 0521Z read that "both gate-holders are unseated" was true when
measured and is now half-false; the CTO half is discharged. *Recorded rather than quietly overwritten,
because the staffing decision below was made under the older read.*

⚠ **SEATING GAPS — RAISED 0528Z, BOTH DISCHARGED BY 0534Z** (MSTR, LD-0390/0391):
- **`3.0.0_SA_CVO`** — owes the Rule-14e cert (gates cutover acts 2/3/4). **SPAWNED 0529Z (LD-0390)**
  on CTO's 052626Z surfaced need — *crossed in flight, before my ask arrived.* CTO's 052113Z cert
  request confirmed sitting in its inbox.
- **`0.7.0_AE_CloudOps`** — owns **TWO dispatchable acts** (cutover act 1 / X-iv, and C-3/CPR-3).
  **SPAWNED 0534Z (LD-0391)** with startup direction naming both acts + this register.

**Seating was a capacity fact, never a gate** — spawn authority is MSTR's; I surfaced and did not hold.
**The program is now fully seated: CTO, CVO, AE, DS, CRO, CRO~A, MSTR all live or booting.** The
binding constraint has moved from *seating* to *the CVO cert and Andrew's exception set* — both
correctly held by their owners, neither by me.

**Integrator push LANDED @7f579d72b6** (MSTR, sole shared-branch integrator per LD-0367 r2 / LD-0368):
zero local-ahead, carrying @f639b23c1f + @8ad0d6b641 + this register @014e7af672 + LD-0389/0390/0391.

---

## 0b · NAMESPACE — SETTLED FABRIC-WIDE, AND MY OWN LABELS MOVED

**Three `C-n`/`R-n` namespaces were live in one fabric tonight. The settled state (adopt verbatim):**

| namespace | form | owner / authority |
|---|---|---|
| CRO recon chapters | **`RECON-1`..`RECON-7`** (renamed *from* `C-n`) | CRO base @3833ce88d1 · CTO concurred @1d3875cc45 |
| Scheduling-jam findings | **`C-1` / `C-2` / `C-3`** — **KEEP, unchanged** | CRO~A's committed brief @1b43c23765 §4 |
| 08-10 taxonomy rulings | **`R-1`..`R-5`** — keep (oldest, most embedded) | @dedd7bdeab |
| **This register's landing acts** | **`CPR-1`..`CPR-4`** *(was `R-1`..`R-4`)* | **this seat — renamed, see below** |
| ITEM_0 landing acts / remediation register | `L-0`..`L-7` / `R-4b` — untouched, a third distinct thing | ITEM_0 |

**⚠ CTO briefly ruled the OPPOSITE (`JAM-C1..C3`, @ef75749af4) 15 seconds after CRO's commit, then
CORRECTED to CRO's form @1d3875cc45.** Two Tier-1 execs held contradictory conventions for ~90s. **I
did not adjudicate** — surfaced verbatim to both, ran a convention-independent interim protocol
(descriptive reference + `file:line`, correct under either outcome), and CTO conceded. **My live DS/AE
dispatches needed no edit**, because they carried `file:line` beside every label — habit, not design.

**>> AND I COMMITTED THE SAME DEFECT IN THIS FILE.** These acts were originally labelled `R-1`..`R-4`,
colliding with the 08-10 taxonomy rulings `R-1`..`R-5` — **I flagged the collision in two peers'
namespaces and created a third in my own, inside ten minutes.** Renamed to `CPR-*` by CRO's own rule:
**the newest, least-embedded namespace moves.** Mapping for the seats already dispatched:
`R-1 → CPR-1` (INF union-preserve) · `R-2 → CPR-2` (C-2 double-lag) · `R-3 → CPR-3` (C-3 sweep order) ·
`R-4 → CPR-4` (F4 D_04 residual). *Knowing a failure mode by name does not immunize you against
writing it — which is why the register is the control and care is not.*

**NAMING LAW (CTO-ruled @ef75749af4/@1d3875cc45, item unchanged by the correction): the FULL 8-DIGIT
account + the PRODUCT is the only unambiguous form.** Never the 4-digit prefix, never a bare "49F" —
`08335338` = **ADVI** (Advisor Intelligence; **HAS `gold/`**) · `08242234` = **MDPF** (Model Portfolios;
**no `gold/`** — incomplete, not violating). *I verified both live before the Andrew-direct ADVI
archetype reference propagated; that grounding is now cited in the spec.* **"49F" is a FIRM, not a
bucket** — it appears against `08242234` in the `49-schwab-conv` ingest path and against `08335338` as
the ADVI archetype, so the nickname alone cannot identify a substrate.

---

## 1 · DISPATCHABLE NOW — four landing acts (`CPR-1`..`CPR-4`)

### ACT CPR-1 · INF Sunday full-pull must UNION-PRESERVE departed accounts — ✅ **CLOSED 0542Z**

> **✅ LANDED + DEPLOYED + ACCEPTED (DS, 054212Z).** Baseline @9b29609e42 (deployed bytes byte-exact,
> **drift vs deployed measured ZERO**, no deploy) → fix @9196959b53 (union-preserve) → twin-sync
> @76386cd21c. **Acceptance EXERCISED 13/13** through the real module: T1 positive, T2 negative control
> (carried==0 no-op limb), **T3 mutant** (baseline erases the account → harness must FAIL). Live leg:
> bronze 1,434,473 rows × accounts_v2 869 ids → carry set **26,371 rows / 16 accounts, EXACTLY**
> CRO~A's independently-derived oracle. Sunday auto-detect limb exercised at pull-date 2026-08-16.
> Precondition (b) discharged by measurement (edit confined to the `if full_pull:` branch; the script
> runs in the INF chain, not the 13:02–15:05Z MDPF cadence).
> **⚠ POST-LANDING VERIFICATION, OWNER DS, SURVIVES THIS SESSION:** the Sunday 08-16 chain log must
> show the **UNION-PRESERVE line**. A zero-carry line **also passes** (Orion may resurrect the
> accounts); **ABSENCE of the line is the failure.** Event-driven read after Sunday — **no monitor
> built** (moratorium). The hard date is no longer a race; it is this one log read.
> **DS CAUGHT A NEAR-MISS MY DISPATCH WOULD HAVE CAUSED:** the script is **TRIPLE-HOMED** on S3
> (`code/gold/` + `code/manual_api/` + `code/bronze/`) and `orion-gold-dispatch.sh sync_scripts()`
> **fails loud on a differing-content basename collision** — so the gold-only deploy my dispatch
> implied would have **REFUSED the next chain sync = INF outage.** All three deployed, each
> ETag-verified against local md5. *My dispatch named the deploy target from the one prefix I knew
> about; the estate had three.*

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

### ACT CPR-2 · C-2 retry-net double-lag (Cottonwood bronze ingest)

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

### ACT CPR-3 · C-3 sweep/primary order (probe-day universe)

| field | value |
|---|---|
| **OWNER** | `0.7.0_AE_CloudOps` — **UNSEATED.** Infra/Terraform lane per Rule 13 |
| **SPEC** | strategy §4 Move 3 — `ssm.tf:143` vs `:165` |
| **TRIGGER** | AE seat exists (TO delivered to its inbox, wakes with the seat) |
| **PRECONDITION** | `safe-apply` (never bare `terraform apply`) **+** AE confirms the apply's blast radius does not touch a leg inside today's 13:02Z–15:05Z cadence — if it does, apply after the bar closes |
| **ROUTED** | TO to AE inbox now; spawn need surfaced to MSTR (spawn authority is MSTR's, not mine) |

---

### ACT CPR-4 · F4 D_04 non-fee-AUA residual → CLASSIFICATION (ready-to-land)

| field | value |
|---|---|
| **OWNER** | `0.4.0_DS_ClientPlatform` |
| **DRAFTER** | `4.0.0_SA_CRO~A` — diff already committed @ec874f6a8d, *"ready-to-land diff for the DS lane via COO wake-point"* |
| **TRIGGER** | **NOW** — DS started it 0542Z |
| **PRECONDITION** | none |

> ⚠ **SCOPE UPGRADED 0543Z BY ANDREW'S RATIFICATION (@d272021791), AND MY ORIGINAL CONSTRAINT ON THIS
> ACT WAS SUPERSEDED — recorded because DS was already executing under it.** This row originally read
> *"a classification + surfacing change, not a revaluation — DS confirms the diff changes
> labelling/surfacing ONLY."* That was correct pre-ratification and became **WRONG**: the act is now the
> **RETIREMENT VEHICLE** for a ratified-**TRANSITIONAL** member of the exception set — on verified
> landing the non-fee-AUA residual **leaves the exception set and becomes a raw field**, which is
> deliberately *more* than labelling. **A faithful application of my original constraint would have made
> DS stop and flag it**; corrected to DS at 054425Z before the cycle was spent, not after.
> **REVISED ACCEPTANCE (CTO-specified, verbatim):** (1) the raw Billing `is_fee_earning` **classified
> sum ties the served figure**; (2) the **residual CALCULATION retires from the serving path**
> (`sum(fee_aua)-balance` stops being the source of the served number); (3) the cross-source gap
> surfaces as `unreconciled_aua` rather than being absorbed. DS states which of the two the served
> number now comes FROM.
> **The C-1 caution SURVIVES NARROWED:** this retires the residual from *serving*; it does **not**
> resolve the C-1 revaluation asymmetry, which stays open at Andrew via CTO. **A green CPR-4 must not
> read as closing C-1.**

> **Why CPR-4 is dispatched and not banked:** *items that cost nothing are the ones that quietly never
> happen* (ITEM_0's organizing principle, my own form). A ready-to-land diff with no precondition is
> the single most likely act in this register to still be sitting here in a month.

**DS QUEUE ORDER: CPR-1 → CPR-4 → CPR-2.** CPR-1 first on the hard date; CPR-4 second because it is drafted and
free; CPR-2 third — its runtime is 22:30Z tonight, so it has the most slack of the three. DS may reorder
CPR-4/CPR-2 on its own readiness read; **CPR-1 stays first.**

---

## 2 · THE MDPF CUTOVER — staffed, with CTO's ruled order

**UPDATED 0530Z:** CTO delivered the **UNIFIED CANONICAL PATTERN SPEC v0.1** @3272f3c4b0
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/MDPF_ADVI_UNIFIED_CANONICAL_PATTERN_SPEC_20260811.md`) and
handed §5/§6 to this seat to staff. **This supersedes the "not dispatchable tonight" read above it** —
CTO ruled the act ORDER, and one act is now dispatchable.

Grounded on the CRO decomp Part A3 @41692cd3d2 + the spec §5. **Decomp status = DRY, UNCERTIFIED.**
**`opal-data-mdpf` is LOAD-BEARING LIVE — MIGRATE-BEFORE-KILL, never a delete** (3 feeds written
03:30Z tonight; per-firm bells exercised 08-10; both EC2 legs boot from it; DS deploys into it).

**⚖ CTO'S RULED ORDER IS REVERSE-BLAST, AND IT IS THE RIGHT SHAPE:** zero-risk first, highest-blast
last — `(iv) → (iii) → (ii) → (i)`. The table is ordered as it executes, not as it was numbered.

| # | Act | What re-homes | OWNER | TRIGGER | NAMED PRECONDITION |
|---|---|---|---|---|---|
| **1** | **X-iv** | Delete the 2 already-IAM-dead stages (3.5 legacy-emit, 5 OWNTS) | `0.7.0_AE_CloudOps` — **UNSEATED** | **NOW — CTO: "touches nothing served and can staff now."** NOT gated on CVO cert, NOT on Andrew's exception set | Still a deletion: **confirm dead on the LIVE primitive** (`get-role-policy` / an exercised call), never the comp-tool DESIRED view — a comp-tool cannot tell landed from planned (Rule 22a). Nothing served may change |
| **2** | **X-iii** | Accrual's `partner_roster` + code sync | DS (scripts) + AE (infra) | after X-iv **and** CVO cert | **atom 6: config NEVER in the code store** — `partner_roster.json` is the measured violation; this act is where it is fixed, not carried forward. Derive counts from the roster, never a literal |
| **3** | **X-ii** | The aggregate (`gold/mdpf_revamp/_aggregate_aua` staging → the floor consumes it) | AE | after X-iii; **producer + consumer move in the SAME window** (CTO) | W1a already staged the consumer-side repoint — **verify that staging is still valid before reusing it**, do not assume a 1-week-old stage still applies. Floor and chain are **SERIES-COUPLED, not parallel** (the false fork) |
| **4** | **X-i** | Feeder writes (`non_model_aua`, `etf_net_assets`, inflection feeds, bronze) — **the client-facing smartx read edge migrates WITH this** | DS (scripts) + AE (infra) | LAST. after X-ii **and** CVO cert | ⛔ **highest blast. The per-firm 49financial + inflection `account-distribution` bells are LIVE and client-facing — nothing staffed may touch them pre-cert (CTO, explicit).** Cottonwood + global + the flat key are FROZEN 07-23 by CTO ruling — *deliberately* frozen, not broken. Underscore-in-gold / hyphen-in-platinum spelling law holds per layer. **The atom-5 schedule floor lands HERE** |

**Two program-level preconditions, and neither is mine to discharge:**
1. **CVO Rule-14e certification** of the decomp ground truth (@41692cd3d2) — **requested by CTO
   052113Z; CVO is OFFLINE, seating flagged to MSTR.** Gates acts 2/3/4 (X-iii, X-ii, X-i); does **not**
   gate act 1 (X-iv). *Do not cut a live client-facing pipeline on an uncertified rectangle.*
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
| 1 | `comp-pipescript deployed` is structurally blind to the Lambda-zip code channel (returned MATCH while executing code was 4 days stale) | CTO (instrument roster) | OPEN — routed 031216Z. **Named in CPR-1's acceptance so it cannot be leaned on** |
| 2 | `comp-pipescript deployed` rendered 1 of mdpf's 6 code layers (7/49 objects, denominator unstated) | CTO | OPEN |
| 3 | `comp-estate` served rows carried a 404 platinum key + runner conflation | CTO | OPEN |
| 4 | Two live code channels + 17b grammar observation | CTO (DS-flagged 033615Z) | OPEN |
| 5 | C-1 revaluation asymmetry / conversion policy | CTO → Andrew | OPEN, live |
| 6 | Estate-wide point-in-time extension census | CTO | OPEN, diagnostic |
| 7 | Cottonwood deep-rekey adjudication | CTO (causation thread) | OPEN, deliberately not parallel-read |
| 8 | `MISSING_IN_REPO`: deployed-only gold scripts with no repo counterpart (CPR-1's script is one; the decomp measured **4 more** in the assets_gold layer) | DS + CTO | **AMENDED 0542Z: CPR-1's instance was MISHOMED, not missing** — `data/inf/manual_api/pull_inflection_transactions_rest.py` was byte-identical to the deployed artifact (md5=ETag 78f60cc7). Baseline still landed per protocol. **The class STANDS for the other 4 scripts**; this instance is reclassified, not resolved |
| 9 | 2 unpushed local commits (audit-archive baseline + snapshot, @f639b23c1f/@8ad0d6b641) | MSTR (sole shared-branch integrator, LD-0367 r2 / LD-0368) | **CLOSED** — push landed @7f579d72b6, zero local-ahead |
| 10 | **`C-n` NAMESPACE COLLISION**: recon chapters (CRO base @07c6f68bf4: C-1 MDPF / C-2,C-3 at ~A / C-4 join / C-5 cottonwood) vs scheduling-jam findings (CRO~A strategy §4: C-1 custody asymmetry / C-2 double-lag / C-3 sweep order). **Two meanings, one label, arrived 3 min apart; I routed the FINDINGS C-2→DS and C-3→AE, which a reader of the recon map reads as ~A's work.** Rule-24 axis hygiene one layer up | CRO base (map owner) + CTO (spec owner) | OPEN — flagged to CRO/CRO~A/CTO 0530Z. Proposal: `C-n` stays recon, findings become `JAM-C1..C3`. **Until settled every COO dispatch qualifies `(A)`/`(B)`** |
| 11 | **TRIPLE-HOMED DEPLOY TARGETS**: `pull_inflection_transactions_rest.py` lives at 3 S3 code prefixes and `orion-gold-dispatch.sh sync_scripts()` **fails loud on a differing-content basename collision** — a single-prefix deploy REFUSES the next chain sync (INF outage). Found by DS executing CPR-1, whose dispatch (mine) named one prefix | DS (instance closed, all 3 deployed + ETag-verified) · **CTO for the CLASS** | **OPEN as a class** — how many other multi-homed scripts carry this? A deploy-map that knows one home of three is the same two-channel blindness as rows 1/2, one layer out |
| 12 | **`comp-pipescript deployed --pipeline inf-gold`** renders ONE `aux:manual_api` row for a **triple-homed** script (reads MATCH) — corroborating only | CTO (instrument roster) | OPEN — joins rows 1/2 |

---

## 4b · STATE AS OF 0546Z — the deltas since 0525Z (a successor reads THIS first)

**⛔ NOTHING IN THIS PROGRAM WAITS ON ANDREW ANYMORE.** He **RATIFIED** the must-calculate exception set
**and** pattern spec **v1.0** at ~0542Z (@d272021791, *"im cool with your recs"*). **Both `AT ANDREW`
rows in §2 are STRUCK.** The **only live gate** on cutover acts X-iii/X-ii/X-i is the **CVO verdict**,
mid-flight. *CVO has surfaced one pulling thread worth watching: a designed clock-floor path in the
trigger lambda **source** that does not exist as a **live rule** — the no-schedule-floor class again,
delta-row-4 territory. Its verdict says which way it cuts.*

**RECON PHASE NOW FRONTS IMPLEMENTATION** (Andrew oversight mandate @3c8418e34b, CTO oversight at
`1.0.0_SA_CTO/deliverables/SSOT_RECON_MATRIX_20260811.md`). Implementation beyond X-iv stages on matrix
cells reading **CERTIFIED**. **This is the mandate's own ordering, not a new gate** — his words are
*"get all the information… so we can figure out what needs to happen."* **CARVE-OUT ON THE RECORD so
nobody re-derives a hold over it: CPR-1..CPR-4 and X-iv/W-E are UNAFFECTED**, CPR-1's Sunday date in
particular never waited on recon.

| item | state at 0546Z |
|---|---|
| **CPR-1** | ✅ **CLOSED** — landed, deployed to all 3 prefixes, exercised 13/13, oracle-exact. Sunday 08-16 log read remains, owner DS |
| **CPR-4** | IN FLIGHT at DS, **scope upgraded** to the residual's retirement vehicle (above) |
| **CPR-2 / CPR-3** | queued (DS after CPR-4) / with AE |
| **X-iv** | AE **WORKING** — live-primitive verify first, then delete. CTO endorsed the precondition **and added the load-bearing half: the 08-06 AccessDenied traceback is PRIOR evidence; the check must be CURRENT-state** (IAM may have moved in 5 days). Relayed to AE 053510Z |
| **RECON-4** | ✅ **DELIVERED** @be316d868c (CRO base) — per-firm, not aggregate |
| **RECON-6** endpoint-delta census | **ASSIGNED to CRO base** (freed by the RECON-4 delivery). **Critical path**: the one remaining input to run atom-8 conformance at scale. **My ~B spawn ask to MSTR was RETRACTED** — CRO base delivered ~30s before it arrived, so the premise was false |
| **RECON-5** | 5a (cot endpoint inventory, rides RCN-0001) queued at CRO base; 5b after the archetype stabilizes |
| **L5/L6 advi** | ONE sweep across all three firms after the archetype's L4 stabilizes (my call). Preconditions: L6 grounds on **what the DEPLOYED FE actually reads**, never docs or the builder; the sweep does **not** wait on RECON-5b |

**ITEM-3 SEQUENCING (my call, off RECON-4's per-firm verdict):** **(1) INFLECTION FIRST** — 98.0%
native-key join, rollup spine in place, **zero identity work** = the cheapest first TO and it de-risks
the overlay before either harder firm. **(2) 49F SECOND**, gated on **one identity fact** (does a SmartX
endpoint expose allocation→custodian-account); `account_id` is a SmartX allocation UUID with custodian
deliberately `None`. **No build TO is decomposable for the 49F leg until that fact lands** — not
manufacturing one on an assumption. **(3) COTTONWOOD LAST**, strictly after goal 1's custom-model pull —
*"no model feed exists"* is a **measured absence**, not a gap to design around.
Residual queued to DS behind CPR-4/CPR-2: **11 of 561 inflection accounts unmatched (2.0%), cause
UNMEASURED** — marked so nobody quotes 98.0% as if the remainder were understood.

**EGRESS QUESTION RAISED AND CLOSED (0543→0544Z), and it cut BOTH ways:**
- **49F Black Diamond:** I flagged that the standing lift is *cot-BD only, "not bd/49f"* while the ADVI
  field-map was recorded as *"egress granted… Orion/Eclipse/BD endpoints"* — and 49F **is** a Black
  Diamond firm. **CRO~A answered: AT REST ONLY**, no live 49F-BD endpoint call planned or needed; it
  will return for Andrew's per-use word **before** any such call. **No violation occurred.**
- **The mirror error, found 20 minutes later:** CRO base recorded the 49F unlock fact as
  *"vendor-egress-gated to verify"* — **but SmartX is ON the standing lifted list**, so that call needs
  no new authorization. **A too-WIDE grant read risks unauthorized egress; a too-NARROW one stalls a leg
  invisibly, presenting as a legitimate blocker.** Both are one root: **reading a grant at the wrong
  grain.** Only the first has a rule pointed at it.

**IDENTIFIER FAMILIES — MEASURED LIVE (Andrew-direct: "the existing 49F 49 Financial pipeline is known
as 'bd pipeline' and 'opal-data-bd' and bd-gold-runner"):**
`s3://opal-data-assets/blackdiamond/` → **`49f/` AND `cottonwood/`** · `s3://opal-data-bd/blackdiamond/`
→ `49f/` · `s3://opal-data-assets/schwab/` → `08242234/`, `08335338/`.
**So "bd" is ambiguous BY FAMILY: as a PIPELINE it means 49 Financial; as a vendor abbreviation it means
Black Diamond, which serves TWO firms.** The 8-digit+PRODUCT law fixes the *account* axis and does not
touch this one. **A census keyed `blackdiamond` reads two firms; keyed `bd` reads only 49f** — so an L1
count without its key family has a denominator ambiguous **across the firm-separation boundary the gate
and IAM exist to enforce.** *Open at CTO/CVO, explicitly not mine: whether a bd-tree script reading
`blackdiamond/cottonwood/*` trips the bd↔cot gate — `blackdiamond/` is a shared-vendor prefix in the
shared bucket, not a "cot bucket."*
**It already produced a correction:** CRO~A's *"49F chosen for COMPLETE fact tables"* was measured over
the **schwab/08335338 SDD family** (20 tables, 525 daily partitions), **NOT** `blackdiamond/49f` — now
stated explicitly in the archetype record, and every RECON count prints its key family.

---

## 4c · STATE AS OF 0552Z — ⛔ ONE TIME-BOUNDED SOVEREIGN GRANT A SUCCESSOR MUST NOT INHERIT

### ⏳ SESSION-SCOPED FREE EGRESS — Andrew-direct ~0549Z, @9e1fc54623

**VERBATIM: *"For the remainder of this session all agents have free egress as needed."***

**THE GRANT IS PERMISSIVE AND THE BOUND IS THE LOAD-BEARING HALF.** After session end the standing
regime resumes: **ORION · SMARTX · cot-BD (Cottonwood Black Diamond ONLY, not bd/49f) · arxiv (CRO,
cloud-Lambda-only) · ECLIPSE lifted; EVERYTHING ELSE HELD, per-use word required.**

⛔ **THE HAZARD, NAMED BECAUSE IT IS INVISIBLE BY CONSTRUCTION: a TIME-BOUNDED GRANT THAT GENERATES
DURABLE ARTIFACTS PROPAGATES AN EXPIRED AUTHORIZATION INTO THEM.** Any TO, spec row, or dispatch
written during this session that leans on free egress will be executed by someone *after* the grant
lapses — and the artifact will read as authorization. **Therefore: every dispatch relying on it MUST
carry the session bound inline.** *(This is the mirror of the LD-0340 forwarder lesson: there, a
non-durable fix propagated its expiry into 186 durable artifacts. Same mechanism, opposite sign — and
this direction ends in an unauthorized vendor egress rather than a broken PATH.)*

⚠ **SCOPE AMBIGUITY I AM SURFACING, NOT ADJUDICATING: *whose* session?** Andrew's working sitting, or
each agent's process lifetime? These diverge sharply — an agent process can outlive Andrew's sitting by
hours, and an agent reasoning *"my session is still live, therefore I still have egress"* at 14:00Z
would be egressing on a grant that ended when he stood up. **The conservative operating read (mine, and
it restricts nobody's authorized work): the grant ends with ANDREW'S session, and an agent must not
extend it on the strength of its own process still running.** Routed to CTO for one clarifying word
since CTO holds the record; **nothing is blocked meanwhile** — the grant is permissive, so the only
risk lives in over-extending it, never in under-using it.
**A RESPAWNED SEAT DOES NOT INHERIT THIS. If you are reading this file in a later session, you do not
have free egress.**

### RECON-4 CORRECTION — Andrew-direct ~0547Z (@a4d5147211): my *reason* was wrong, the call stands

Cottonwood's cell is **NOT** "no model feed exists." **The BD Rebalance endpoint IS the model-holdings
source** → cell = **`SOURCE-EXISTS-PIPELINE-ABSENT`**. Goal-1's opening move is **schema capture at
RCN-0001's rebalancer-models gap**.
**My §4b sequencing rationale said *"'no model feed exists' is a MEASURED ABSENCE, not a gap to design
around."* That reason is FALSE.** The conclusion — **Cottonwood last, strictly after goal 1** — is
unchanged, but it now rests on *cot goal-3 runs THROUGH goal-1 as an **INGEST BUILD***, not on a vendor
absence. **Correcting it explicitly because a right conclusion resting on a wrong mechanism is exactly
what gets copied forward into the next decision, where the mechanism is load-bearing.**

### 49F ITEM-3 UNLOCK — LANDED AT REST, ZERO EGRESS SPENT (CRO~A via CRO base, 055024Z)

`smartx/platform/silver/fact_allocation_account_map` (7,262 rows daily) maps `allocation_id` →
**8-digit Schwab `account_number`** with custodial names in-row, **at rest in `opal-data-assets`,
discovered from the converter's own test fixture.** So item-3's 49F leg is a **JOIN through the map
table**, *not* a feeder change — the feeder's `custodian=None` stays true of its own surface.
**ONE RESIDUAL BEFORE THE BUILD TO IS DECOMPOSABLE: KEY FORM — the map carries 8-digit, `fact_acc`
carries 10-digit.** At-rest join test running; RECON-4 amended once with the measured overlap.
**⚠ Do not decompose the 49F build TO until the overlap number lands** — a join on an unverified key
form is the defect, not the plan.
**ITEM-3 ORDER CONFIRMED UNCHANGED: INFLECTION FIRST** — zero identity work beats one join hop, even a
cheap one. 49F has moved closer than expected but has not overtaken it.
> **This is what the too-narrow-grant push was worth:** the unlock needed **no egress at all**. The leg
> was unblocked by *looking at what we already hold*, not by obtaining permission — Build-Ladder rung 2
> (the estate already has it) arriving as an egress answer.

### CPR-4 · SERVE-RELEASE STATE

**LANDED @7341b27d50, 12/12 exercised — and CORRECTLY NOT SERVING.** `INF_D_04` carries a live
`# DEPLOY-SERVE-HELD` sentinel (restored @1ae1ac882b as a CTO+COO condition of the 08-05 release);
mechanism verified at source, `safe_deploy_core.py:197-207` — sentinel-removal *is* authorizing serve,
gated behind an in-message `SERVE-RELEASE-ACK`, **all three checks FAIL CLOSED.**
**My COO half of the never-widen sign-off: GIVEN**, conditional on (1) CTO's half, (2) **the
AoR-absence premise VERIFIED not asserted** — the lift's whole basis, and the sentinel's unmet condition
is specifically the advisor-of-record fold, (3) a **deploy-completion ledger entry** with all four steps
(lift → deploy → **re-hold SAME WINDOW** → republish) finishing in-session or rolling back, (4) no
intersection with the 13:30Z MDPF bar window.
**Until both halves land, platinum serves the OLD arithmetic (~$606K vs the ratified-correct ~$128K).
That is a HELD state with named owners, not a stalled one — and it is safe, which is why the gate exists.**
**⚠ MY REGISTER SAID `PRECONDITION: none` ON THIS ACT. IT WAS WRONG.** Second time tonight a
precondition was understated here and caught by DS *executing* (the first: CPR-1's triple-homed deploy
targets). **My preconditions were derived from specs and drafts; the DEPLOY MECHANISM's own
preconditions are only visible from the lane.** Routing being right does not make the mechanism checks
mine to have found — and a register that says "none" is more dangerous than one that says "unknown."

---

## 5 · WHAT THIS REGISTER DELIBERATELY DOES NOT DO

No new gates (none asked for; one dissolved). No monitors/alerts/freshness checkers (moratorium). No
shadow or parallel channel to de-risk the cutover — **build correctly and port over** (Andrew's
complete veto; a standing comparator is vetoed on the same grounds). No engineering staffed against
the MDPF repair's priority. No spawn decisions — that is MSTR's authority. And no act above lands
"when someone gets to it."
