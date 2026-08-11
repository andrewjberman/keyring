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
**A RESPAWNED SEAT DOES NOT INHERIT THIS BLANKET LIFT.**

> ⛔ **AMENDED 0658Z — AND THE LINE ABOVE WAS TOO BROAD AS ORIGINALLY WRITTEN.** It read: *"If you are
> reading this file in a later session, you do not have free egress."* **There are now TWO grants with
> DIFFERENT EXPIRY SEMANTICS, and that sentence would send a successor at a fresh ask they do not need:**
>
> | grant | scope | expiry |
> |---|---|---|
> | **BLANKET LIFT** (@9e1fc54623, *"for the remainder of this session"*) | all agents, all vendors | ⏳ **DIES WITH ANDREW'S SESSION.** Successors do **NOT** inherit |
> | **WORK-SCOPED PER-USE GRANT** (instruction 6, ~0700Z: *"as much egress and endpoint testing as you need"*) | **Orion + BD**, for the **GIPS feasibility work specifically** (Inflection off Orion, then Cottonwood off BD) | **RIDES THE WORK, NOT THE SESSION — it survives on its own terms where the blanket bound does not** |
>
> **SO: a successor continuing the GIPS work HAS egress for it. A successor doing anything else does NOT.**
> **THIS IS THE THIRD TIME TONIGHT THE SAME CLASS HAS BITTEN — READING A GRANT AT THE WRONG SCOPE:** a
> too-WIDE read (BD "granted" covering a firm it never covered) · a too-NARROW read (SmartX marked
> egress-gated when it was on the standing lift) · **and now my own record, too BROAD on an expiry, which
> would have under-served a live grant.** *Guarding against over-extension produced a record that
> under-extends. **A record broader than its mechanism sends an agent at the wrong tool exactly when they
> are moving fast** — and I wrote one while warning about them.*

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
**Until both halves land, platinum serves the OLD arithmetic.** ⛔ **MAGNITUDE CORRECTED 0752Z -- THE "~$606K vs ~$128K" FIGURES WERE FROZEN-GOLD QA READS AND ARE WRONG BY ~500x. LIVE: the old residual served $71,944,750.24 AS CLASSIFIED CLIENT MONEY; the classified truth is $3,623,738.50, and the cross-source gap is `unreconciled_aua` = $68,321,011.74** (arithmetic identity 209,129,912.97 - 137,185,162.73 - 3,623,738.50).
That is a HELD state with named owners, not a stalled one — and it is safe, which is why the gate exists.**
**⚠ MY REGISTER SAID `PRECONDITION: none` ON THIS ACT. IT WAS WRONG.** Second time tonight a
precondition was understated here and caught by DS *executing* (the first: CPR-1's triple-homed deploy
targets). **My preconditions were derived from specs and drafts; the DEPLOY MECHANISM's own
preconditions are only visible from the lane.** Routing being right does not make the mechanism checks
mine to have found — and a register that says "none" is more dangerous than one that says "unknown."

---

## 4d · STATE AS OF 0555Z — ✅ THE CUTOVER GATE IS RELEASED

### CVO CERTIFIED @cc62267d89 — **ZERO cells refused.** Acts X-iii / X-ii / X-i leave staged.

**The cert was the last gate** (Andrew's ratification @d272021791 already cleared the other). Order is
unchanged and remains CTO's reverse-blast ruling: **X-iv → X-iii → X-ii → X-i.**

**TWO CVO RIDERS — FOLDED IN AS BINDING, NOT ADVISORY:**
1. **ACT X-ii GAINS A NAMED PRECONDITION: ground the staging producer IDENTITY with one CloudTrail /
   CloudWatch read before re-homing the aggregate.** The 08-09 and 08-10 ~13:00Z `_aggregate_aua`
   writes happened **while the main chain was dark** — so "the chain's aggregate stage writes this" is
   the rectangle's **INFERRED** cell, not a measured one. **Re-homing a producer you have not
   identified is re-homing the wrong thing.** One read discharges it.
2. **REMEDIATION LINE (row 13): "consolidator carry-forward behavior on stale staging inputs —
   verified/declared."** Its 13:30Z fire runs over `non_model_aua` **frozen since 08-06** — the
   **process-ts-FRESH / data-as-of-STALE** shape, where every producer-side signal reads healthy while
   the input is five days old.

**CVO ALSO CORRECTED CTO'S CLOCK-FLOOR FRAMING, and the correction preserves the deliverable:**
`mdpf-scheduled-floor` **IS** live — but in the **SCHEDULER namespace, targeting the CONSOLIDATOR.**
**Delta row 4 STANDS: nothing clocks the EC2 chain.** So **act X-i's schedule-floor deliverable is
UNCHANGED** (atom 5: event accelerates, clock floors). *A live floor pointed at the wrong component is
not a floor on the component that needs one — and it reads as one in any config-level check.*

### CPR-4 SERVE-RELEASE — BOTH HALVES LANDED, CHOREOGRAPHY BINDING

**CTO half GIVEN 0553Z**, `SERVE-RELEASE-ACK` scoped to **@7341b27d50 only**. **My condition (2) was
DISCHARGED BY MEASUREMENT, not assertion** — CTO verified the diff themselves: it touches exactly
`_derive_fee_earning_aggregates` (4 hunks, `:764-848`), **ZERO AoR mentions.** My conditions (3)
ledger-before-lift and (4) 13:30Z-bar confirmation are **restated as binding terms inside the ACK**, and
**the sentinel returns verbatim in the same window.** ⛔ **The served `non_fee_earning_aua` moves $71,944,750.24 -> $3,623,738.50 on the republish, with the $68,321,011.74 gap surfaced as `unreconciled_aua`** (NOT the ~$606K/~$128K I first recorded -- those were frozen-gold QA reads).

### ITEM-3 — FINAL FIRM ORDER, AND MY 49F HOLD IS DISCHARGED

**RECON-4 FINAL @83814f0e2d.** The key-form residual I held the 49F build TO on is **MEASURED**:
`feed.account_id → fact_allocation_account_map.allocation_id → account_number → zfill(10) →
fact_acc.account_id` at **99.8% (5,701 / 5,715 distinct)** — `fact_acc.account_id` **is** the
zero-padded 8-digit Schwab number. **Denominator given both sides, as asked.** **HOLD DISCHARGED — the
49F build TO is decomposable now**, join spec is three lines.

| # | firm | basis | order rationale |
|---|---|---|---|
| 1 | **inflection** | native-key, 98.0% | **zero identity work** — cheapest, de-risks the overlay design first |
| 2 | **49F** | one map hop + `zfill(10)`, 99.8% | identity **solved at rest, zero egress spent** |
| 3 | **cottonwood** | **ingest build** — source EXISTS (BD Rebalance), pipeline absent | rides goal 1; schema capture at RCN-0001's rebalancer-models gap opens it |

**Parked with causes UNMEASURED, deliberately marked so no one quotes the rates as fully understood:**
14 of the 49F 5,715 (12 nine-digit map entries flagged possibly non-Schwab custodial + 2 misses) and
11 of 561 inflection accounts (2.0%). Queued to DS as cheap closes behind CPR-2.
**Decomposition may proceed on DELIVERED** per the matrix's own rule (non-serving design work), with
**RECON-4's own cert noted PENDING** in CVO's queue.

### CARRIED FRONT-LOAD UNDER THE SESSION EGRESS LIFT (⏳ expires with Andrew's session)

CRO~A flagged **RECON-5b's rebalancer-models schema capture** as the **one probe-worthy front-load**
while free egress is live — i.e. capture the BD Rebalance schema tonight so goal-1's opening move is not
waiting on a per-use word later. **Sequencing note: this front-loads the SCHEMA CAPTURE only; it does
not reorder cottonwood, which still rides goal 1.** Any artifact it produces **must carry the session
bound inline** per §4c.

### ANDREW INSTRUCTION 4 (~0552Z) — THE RECON PRODUCT IS A **QUALITY PARTITION**

Not a survey: a **TIGHT PARTITION** — *extract* the quality structure, *discard* the
methodologically-unacceptable. **Every script / engine / subsystem in the RECON census lands in EXACTLY
ONE side, with grounded evidence.** Type specimen: **transaction-engine holdings valuation**,
sovereign-confirmed **ILLEGITIMATELY-DERIVED #1**.

**STAFFING CONSEQUENCE, and it changes what my staged acts consume:** acts staged on recon outputs now
consume **PARTITION VERDICTS, not prose surveys.** RECON-6's endpoint-delta census and RECON-5's cot
work both change deliverable FORM — a per-unit verdict with its evidence, not a narrative. **An act
whose precondition is "recon delivered" must now read "the unit's partition verdict is EXTRACT (or
DISCARD) with evidence cited."** That is a sharper and more staffable precondition than what §4b/§4d
were written against, and I prefer it.

⚠ **ONE RULE-24 CHECK I AM SURFACING TO CTO + CRO, NOT ADJUDICATING — this is a classification schema
at AUTHORING time, so Taxonomy Law binds it.** Postulate (i) MECE is explicit and satisfied by *"exactly
one side."* **The risk is postulate (ii), SAME GRAIN — and it is not in the two VALUES, it is in the
UNITS.** *"Every **script** / **engine** / **subsystem**"* names **three different grains**, and they
**NEST**. If a subsystem's verdict is EXTRACT while three of its scripts are DISCARD, that nested pair
has no single side — **MECE fails not because the axis is wrong but because the census unit is
undeclared.** The cheap fix at authoring time: **declare the census UNIT GRAIN** (and, if mixed grains
are wanted deliberately, state the rollup rule — does one DISCARD child force the parent, or is the
parent's verdict independent of its children?). **Named now because a partition is cheapest to fix
before its first census, and this one is about to reshape every recon chapter.**

## 4e · STATE AS OF 0600Z — X-iv CLOSED · C-3 RE-OWNED (my routing was wrong)

### ✅ ACT X-iv COMPLETE @cf838e54d5 (AE) — nothing served changed

**The precondition discharge is this program's reference standard for Rule-22a grounding.** CURRENT-state
at ~0554Z (**not** the 08-06 traceback); sole write site read from the **DEPLOYED** script; **ONE
`--resource-arns` per call in SEPARATE invocations**; and an **ISOLATED positive control** proving the
instrument discriminates. Stage 3.5 → `explicitDeny` with the Sid named
(`P0DenyLegacyPortfoliosClobber20260728`, via `get-role-policy`); Stage 5 → `implicitDeny` reasoned from
*no Allow in identity policy* **AND** *no principal PutObject Allow in the bucket policy* — the
`(action, resource)` grounding `comp-iam` structurally cannot give. **Neither stage had a live write
path; the act stayed zero-risk, no inversion.**
Deployed dispatch was **byte-verified against repo BEFORE editing**, so no drift shipped alongside.
**BEHAVIOR DELTA, exactly:** serving unchanged (both writes were already denied); the chain now completes
through Stage 6 instead of dying at rc=1 on a dead stage; **chain remains dark** (INF sentinel 07-31), so
no run fires from this act.

### C-3 RE-OWNED TO DS — the spec's `file:line` was a HYPOTHESIS and I treated it as an address

**AE grounded the mechanism and refused the dispatched act, correctly.** The strategy doc's Move-3
pointer said `ssm.tf:143` vs `:165`, so I routed C-3 to the infra lane. **That order is LOAD-BEARING BY
DESIGN** (`ssm.tf:132-139`, DS-co-authored, *"(A) confirmed 135245Z"*): re-lands must beat the
`_BRONZE_COMPLETE` sentinel or they miss same-night silver conversion — **flipping it trades a phantom
heal for a one-day heal delay.** ⛔ **NO ssm.tf REORDER. I declined AE's offer to execute it
"under protest-noted"** — executing a change a lane has grounded as harmful because a COO dispatch named
a file is the worst available reading of authority.
**THE REAL MECHANISM IS IN DS'S PYTHON:** `cot_bronze_ingest.py:1114` anchors the probe universe at
`run_date`, so under lag-1 the newest probe day **is the primary's own landing day** — absent by
construction at sweep time, guaranteeing the nightly re-pull. **Fix:** anchor at the primary's landing
day via `_shift_business_days` by `BD_SNAPSHOT_ASOF_LAG_BDAYS`, mirroring `_as_of_for` at `:301-303`;
`lag=0` degenerates to current behavior. **FOLDS INTO DS's CPR-2 commit** — same file, same
function-space, one deploy window: **C-2 is where a re-pull LANDS, C-3 is what gets PROBED.**
> **TWICE TONIGHT THE MECHANISM WAS SOMEWHERE MY ROUTING DID NOT POINT** (DS's triple-homed deploy
> prefixes; this). **A `file:line` in a spec is a hypothesis about where a defect lives, not its
> address** — and a coordinator who forwards the address rather than the question sends a lane at the
> wrong file with authority attached. Both lanes went to the mechanism anyway. That is the lane doing its
> job, not luck, but the register should not have made them fight the routing to do it.

### Residues from X-iv — dispositions

| # | residue | disposition |
|---|---|---|
| 14 | `alarms.tf` `Stage5OwntsFailed` alarm now **ORPHANED** (metric never emitted again) | **→ CTO instrument roster**; AE correctly holds the TF edit on a GO. ⚠ **CLARIFIED so nobody freezes: the moratorium bans BUILDING alarms, NOT deleting a dead one.** This is cleanup; it needs CTO's word because it is their roster and an `alarms.tf` edit, not because the moratorium reaches it |
| 15 | Both stage scripts remain in repo + code channel; `mdpf-catchup-etlfix-ws3.sh:70` (07-07 one-shot) still references OWNTS | Follow-on debt, correctly **NOT** part of X-iv. **Do not widen X-iv to absorb it** |
| 16 | AE confirms the two-channel code reality (dispatch at `code/`, scripts at `code/scripts/`) | Folded into the instrument-gap thread beside DS's triple-homed finding — **two independent lanes hit this class in one window, which makes it a class, not an anecdote** |

**X-iii IN PROGRESS at AE** (trigger discharged: X-iv complete). X-ii next, **producer-identity read
FIRST**.

## 4f · STATE AS OF 0605Z — the X-iii fork, and a sequencing defect of mine that three corrections missed

### ⏸ ACT X-iii HELD AT CTO — a CONFLICT OF RULINGS, not a manufactured gate

AE escalated 060123Z. **Pattern spec §5 act (iii)** (atom 6, Andrew-ratified: the roster leaves the code
store) versus **`config_objects.tf:10-22`** (CTO's 08-06 ruling: `partner_roster.json` must NEVER exist
as an S3 config object). **The live state — a loose, independently-published roster inside
`code/scripts/gold/` fetched by a dedicated `cp` — violates BOTH, which is why act (iii) exists** (AE's
diagnosis, matching mine independently).
**AE's rec:** accrual deploys to `portal/gold/mdpf/_code/` as **ONE hash-stamped bundle** — script +
build-generated roster copy from the committed authority `data/mdpf/config/partner_roster.json`, authority
sha256 as object metadata; bootstrap pulls one bundle. No free-standing config object, one authority, no
roster GetObject in IAM.
**BOTH rulings are CTO's, so CTO adjudicates. I clarified MY phrase** (*"not where it moves house with the
code"*) to CTO so it is not ruled against as a strawman: I was targeting **an independently-published
object that can DRIFT FROM ITS AUTHORITY**, and on my reading a build artifact *derived* from one
committed authority is a different thing — **stated as input, explicitly non-binding.**
✅ **AE'S HOLD IS CORRECT AND ON THE RECORD AS SUCH.** Two of its gate-holder's own rulings cannot both be
satisfied; building either shape would be *picking*. Surfaced same-turn with a recommendation, everything
else proceeding meanwhile. **The no-inferred-gates rule bans inventing approval steps — it does not ban
asking which of two conflicting sovereign rulings applies. Holding silently would have been the failure.**

**⚡ ONE QUESTION OUT TO CTO WITH THE FORK: may X-ii OVERTAKE a held X-iii?** If the ruled order is purely
**blast-ascending**, yes and the cutover keeps moving; if X-ii carries a **real dependency** on X-iii, no
and it pauses cleanly. **I am not re-ordering a ruled sequence on my own inference of its rationale** —
that is the adjudicating-scope error. AE's X-ii **precondition read is running regardless** (read-only
grounding breaches no ordering, and it is useful under either branch).

### COTTONWOOD RE-GRADED A **THIRD** TIME — and that retired the mechanism slot entirely

@314689f20a: **the Cottonwood Rebalancer ingest ALREADY RUNS DAILY** — bronze
`rebalancer_{models,model_detail,accounts}` (06:00Z, markers through 08-10), silver
`fact_model_{roster,definition,assignment,blend}` (21 daily partitions), gold `dim_model_portfolio`; and
**`fact_model_assignment` is ACCOUNT-GRAIN with 921 distinct `account_number`s** carrying
strategy/program/SMA-UMA flags.

| grading | mechanism claimed | status |
|---|---|---|
| 1 | "no model feed exists" (measured absence) | **FALSE** |
| 2 | `SOURCE-EXISTS-PIPELINE-ABSENT` (an ingest build) | **FALSE** |
| 3 | the ingest **already runs daily**; goal 1 is an **EXTENSION of a live puller** | current |

> ⚠ **MY "COTTONWOOD LAST" CONCLUSION SURVIVED ALL THREE — THAT IS NOT ROBUSTNESS, IT IS EVIDENCE THE
> MECHANISM WAS NEVER LOAD-BEARING.** A conclusion holding under three mutually-exclusive mechanisms is
> **under-determined by them.** Honest restatement: **the ordering rests on ONE ground — INFLECTION IS
> CHEAPEST** (98.0% native-key join, rollup spine in place, zero identity work). Every
> cottonwood-difficulty rationale layered on top was **SURPLUS**, and the surplus is what generated three
> corrections. **The fix is not a fourth mechanism; it is deleting the slot.**

**⛔ AND THE REAL DEFECT, WHICH THREE MECHANISM CORRECTIONS NEVER SURFACED — I HAD MEASUREMENT AND BUILD
ON ONE AXIS:**
- **MEASUREMENT (spine overlap): ALL THREE FIRMS, IN PARALLEL, NOW.** Cottonwood's goal-3 input question
  collapses to the same cheap measurement as the other two and is **no longer gated on goal 1**. There is
  no ordering argument for measurements — cheap, independent, each sharpens a build spec.
- **BUILD / PROTOTYPE: inflection → 49F → cottonwood, unchanged**, on prototype-risk grounds alone.
- **This was a GRAIN error, not a mechanism error — which is exactly why correcting mechanisms three times
  never found it.**
**Routing:** cot spine-overlap folds into RECON-5a; **RECON-6 still goes FIRST** (critical path — a cheap
parallel measurement does not outrank it), CRO's readiness read may run them beside each other.

**PROGRAM-SIZING CORRECTION:** goal 1 is an **EXTENSION of a live puller**, not a fresh ingest. My
register's *"cottonwood rides goal 1"* implied goal 1 was large; **it is smaller than that.** Sizing is
CTO's and CRO's, so I am not re-sizing — but the implication is struck, because *"rides goal 1"* reads to
a coordinator as *"blocked behind something big"* and that is now false.

> **THREE TIMES IN NINETY MINUTES THE ESTATE ALREADY HAD THE THING** — the 49F identity map at rest (zero
> egress), the BD Rebalance source, and a live daily Rebalancer pipeline no register knew was running.
> **Build-Ladder rung 2 earning its place ahead of rung 7.** Carried into RECON-6 as a warning: *an
> endpoint-delta census that assumes a gap will find gaps that are already filled.*

## 4g · STATE AS OF 0612Z — the acts are landing; two things a successor MUST read

### ⛔ FIRST: THE 13:30Z BAR INTERPRETATION IS PRE-REGISTERED AND BINDING — @029b146138

In the window ledger (`org/critical_paths/change_management/20260811T0150Z_mdpf-atomic-window.md`),
written ~7h **before** the cycle. **A successor adjudicates from that table, not from recollection.**
Trigger: AE found both floor-written `_aggregate_aua` staging artifacts (08-09, 08-10) read
`$0.00 / partners=0 / reconciliation=PASS` at 4.5KB vs ~10.1KB. **Calendar resolved first — 08-09 IS a
Sunday** — but `partners=0` is a roster fact, the size drop suggests absent content, and
**`reconciliation=PASS` on `partners=0` is `0==0`, so the instrument cannot discriminate and its PASS is
not evidence.** CTO **endorsed** the row and **pre-committed the escalation**: if zeros are expected, the
hold-or-let-fire call on the 13:30Z floor + 13:50Z publisher goes **to Andrew with CTO's rec BEFORE the
fire.** That is the right owner — serving a client-facing number is a sovereign call, not a coordination
one.

### ACT / TASK LEDGER — where everything actually stands

| item | state |
|---|---|
| **CPR-1** | ✅ CLOSED (deployed 3 prefixes, 13/13, oracle-exact). Sunday 08-16 log read remains, owner DS |
| **CPR-2 + C-3** | ✅ **COMMITTED @ea2400401a as ONE commit** — mutant contrast on BOTH halves; 81/81 non-carry, the 4 failures proven PRE-EXISTING by re-extraction on a pristine HEAD. **Deploy armed 15:06Z, DS holds for my bar verdict.** Marker schema 1.1 adds `universe_anchor` so anchor-relative ages carry their frame |
| **CPR-4** | ✅ serve-release steps **1-3 CLOSED same window** (lift @96334728b4 → deploy ETag-verified → **re-hold @c33d2e5260, sentinel verbatim**), **ledger @d6ae6cbd73 opened BEFORE the lift.** Step 4 republish firing; DS verifies the **SERVED** platinum artifact carries `unreconciled_aua` (magnitude corrected: **$68,321,011.74**, not ~$128K). **Told DS: do NOT close the ledger on an SSM launch Success — a launch is not a completion and a completion is not a served artifact** |
| **X-iv** | ✅ CLOSED @cf838e54d5, nothing served changed; orphaned Stage5 alarm deletion GO'd, targeted apply |
| **X-iii** | ✅ **RULED @060208Z — the hash-stamped bundle is BLESSED**, and CTO confirms my clarified "moves house" reading is the one they ruled on. Two conditions: bundle build inside the sanctioned deploy path (with DS); **acceptance = the ~~13:40Z~~ → **14:10Z** SCHEDULED leg green post-port** (SCHEDULED is the right oracle). ⛔ **"13:40Z" IS A STALE FRAME LABEL** — the accrual bridge's LIVE cron is **14:10Z UTC**; RP-W3 moved it and the older docs kept the old label. AE caught it; I had propagated it. AE building |
| **X-ii** | ⏸ **HELD.** CTO ruled the STRUCTURE now (end state = ONE runtime) with **WHICH runtime evidence-gated** on AE's read — the right shape: the act is not blocked on a measurement and the measurement is not pre-empted by a ruling. W1a's consumer repoint **re-validates, no reuse** |
| **RECON-6** | CRO base, FIRST and undisplaced |
| **Sequencing precedent** | CTO: the `(iv)→(iii)→(ii)→(i)` order is **purely BLAST-ASCENDING** — X-ii may overtake a held X-iii. Moot now, **binding for any future hold** |
| **Census unit grain** | ✅ **RULED leaf-grain-only** — partition attaches only to declared leaves; parents carry `n_extract`/`n_discard` summaries, **never a side.** Closes my Rule-24 postulate-(ii) flag, and the parent-summary form is better than what I proposed |

### ⚠ SECOND: ITEM-3 IS **THREE DIFFERENTLY-SHAPED TOs**, AND THAT NARROWS MY OWN RATIONALE

All three goal-3 measurements done @579d7020da: **native-key** (inflection 98.0%) · **one-hop-map** (49F
99.8%) · **intermediary required** (cot — MEASURED-NO-DIRECT-JOIN: 11-digit spine `account_id` vs FMA
`account_number`, no bridge at any form; `rebalancer_accounts` bronze is an at-rest-checkable candidate,
routed into RECON-5a).
> **I justified inflection-first as "de-risks the overlay design." CRO's measurement narrows that: it
> de-risks the OVERLAY and NOT the IDENTITY layer, which is PER-FIRM BY MEASUREMENT.** I was implicitly
> selling inflection-first as buying down risk for all three firms; it buys down one layer across three
> firms and nothing on the layer that turns out to be the variable one. **Build order stands —
> inflection is still cheapest, the overlay still needs de-risking once — but the other two firms do NOT
> inherit a solved identity problem.** Third narrowing of one of my rationales tonight; the conclusion
> held each time and the reason shrank each time, which is a pattern to expect rather than be surprised by.

**DENOMINATOR QUESTION — ANSWERED, and the contamination is COT-ONLY.** CRO re-measured independently
rather than relaying: `fact_allocation_account_map` `account_number` is **7,262/7,262 non-null, all-digit
rate 1.00, lengths exactly {8: 7,250, 9: 12}, zero values over 12 chars.** The ~100 prose-length values
live **only** in `blackdiamond/cottonwood`'s `fact_model_assignment.account_number` — same column NAME,
different table, different vendor tree, different converter.
> **CRO'S SHARPENING IS THE BETTER FINDING, ADOPTED: grade key-column hygiene PER TABLE, NEVER PER
> COLUMN-NAME — "or a clean table's reputation launders a dirty one's."** Same shape as tonight's
> `bd`-family collision and the `account-distribution` per-layer spelling law: **a NAME is not a grain, a
> grade, or a guarantee, and a registry keyed on names inherits every collision the names carry.**
> Flagged to CTO for the 2a field-registry design (theirs to own).

### ⛔ CORRECTION TO A FIGURE I COMMITTED TWICE — 99.8% WAS A **LEG**, NOT THE PATH

**CVO delta-cert @da62a742c5.** I recorded the 49F join at **99.8%** in this register and in my session
log, as the *end-to-end* rate. **It is not.**

| leg | rate |
|---|---|
| feed → map | **99.86%** |
| map → spine (`account_number`, 5,701/5,715 distinct) | **99.8%** ← *what I quoted* |
| **TRUE END-TO-END** | **99.65% = 7,205 / 7,230** |

**25 feed allocations reach NO spine account.** **The build TO carries the FULL-PATH denominator, never a
leg's.** *This is precisely the class I spent the session policing — a rate that is true about a leg and
false about the path, with nothing in "99.8%" to say which it is. I had the number from a correct
measurement and used it at the wrong grain.*

**TWO MORE FACTS THAT GO INSIDE THE 49F JOIN TO (CVO-grounded):**
1. ⚠ **THE COLUMN TRAP: `fact_allocation_account_map.account_id` CARRIES A SmartX UUID — the Schwab
   digits are in `account_number`.** CVO's own first two verification passes joined the wrong column and
   got a **clean-looking 0.0%.** **The TO names the pair explicitly: `allocation_id → account_number →
   zfill(10)`.** A column named `account_id` that is not the account id, producing a plausible zero — the
   same name-vs-content class as the hygiene finding above, one layer down.
2. **OPEN BEFORE THE JOIN EVER *SERVES* (not before it builds):** is `map-universe == feed-universe` **by
   construction**? Two SmartX pulls, two scopes — **is 99.86% an invariant or this morning's
   coincidence?** One source read of the map's puller settles it. **Recorded as a precondition on the
   SERVING leg, explicitly NOT on the build** — CTO's distinction and it is the right one.

**CVO's queue is now empty except CRO~A's 49F archetype decomp.**

---

**RECON-6 now carries a per-row control that is better than the warning I gave:** every DELTA cell gets
an **at-rest existence check BEFORE it may claim a gap.** *A habit depends on who is reading; a per-row
precondition does not.*

---

## 4h · STATE AS OF 0620Z — sovereign rulings landed, residuals CLOSED, bar amended

### ANDREW RULED X-ii's RUNTIME (~0615Z, @727c2df067): *"on 2., i think the lambda should be the one"*

**The LAMBDA is the producer.** Consequences, all now binding:
- **X-ii RE-SCOPES to the lambda leg** — its inputs/outputs re-home into the product root's `_staging/`.
- **The chain's aggregate stage becomes a DISABLE row**, executed **only after** the lambda leg is
  verified correctly fed — **migrate-before-kill.**
- **W1a's consumer-repoint re-validation now has a known target:** lambda-as-producer (**re-validate,
  never reuse**).
- **The zeros / input-resolution mechanism is PROMOTED to X-ii's FIRST work item** — the ruled producer
  is the runtime that wrote the zeros, so its input fix **fronts** the act rather than trailing it.

### CTO RULED (a) ON THE UNIVERSE QUESTION — SINGLE-HOMED BY CONSTRUCTION, and generalized it

Not a monitor (agreed pre-emptively, moratorium's stated reason), and not an immediate act: **it lands as
a NAMED ROW in the 49F join build TO (DS lane), preconditioning the SERVING leg.** Build may proceed;
**serve may not until the predicate is single-homed** — or Andrew explicitly accepts documented
coincidence, which CTO is **not** recommending and which would come as a ruling request, never a default.
> **CTO'S GENERALIZATION, and it is the sharpest line of the window: TWO INDEPENDENTLY-MUTABLE SCOPE
> DEFINITIONS THAT HAPPEN TO AGREE ARE THE SAME DISEASE AS TWO RUNTIMES ON ONE KEY, ONE LAYER UP.** The
> remedy is the same shape: **a universe/scope predicate is SINGLE-HOMED**; every consumer derives from
> the ONE definition. *Two things that agree by accident are not an invariant — they are a coincidence
> with a good track record.*

### ✅ BOTH PARKED RESIDUALS MEASURED AND CLOSED (DS) — neither number needs an asterisk now

- **INFLECTION 11/561 — NOT ACCOUNTS, BY DESIGN.** Mechanism at source
  (`build_mdpf_wsc_inflection_feeder.py build_model_aua_positions`): a row with no `eclipse_account_id`
  falls back to `account_id = "portfolio_{eclipse_portfolio_id}"`, the code's own comment saying so. All
  11 are underscore slugs, custodian/household NULL, and **`MODEL_VALUE = 0.00` for all 11.**
  ⇒ **the real-account join is 550/550 = 100.0% and NO AUA is unjoined.**
- **49F 14 — three causes:** **11 nine-digit** all-numeric, **fully concentrated in ONE model** (Opal
  Conservative Growth), not Schwab under any transform (strip-first/strip-last/last-8: 0/11 each) and
  absent from SmartX's own `fact_account_detail` ⇒ **a different numbering system, single-cohort.** *DS
  deliberately names NO custodian without evidence — naming it needs the SmartX account surface
  (RECON-2's endpoint question) or advisor-side confirmation.* · **2 eight-digit = CLOSED Schwab accounts
  still in the live map** (present 2024-07-08 and 2025-01-13, absent 2025-07-23 onward) = **map staleness,
  not a join defect** · **1 eight-digit never present** across the full 2024-07-08..2026-08-07 span —
  **the one genuinely open item, and it is one account.**
- **GRAIN CORRECTION:** the "12 nine-digit + 2 misses" was **row-grain**; measured is **11 nine-digit +
  3 eight-digit over 14 DISTINCT numbers / 15 map ROWS.**
- **QUOTABLE FORM:** inflection **100.0% on real accounts**; 49F **99.8% (map→spine leg) / 99.65%
  end-to-end**, residual **UNDERSTOOD**.

### NAME-VS-CONTENT — SPECIMEN **FOUR**, and it is now a ruled design constraint

DS found the inflection feed's key column carries **slugs, not numeric ids** (0/11 all-digit, against
RECON-4's "short numeric ids" description) — the same class RECON-4 itself flagged for the 49F UUID.
**Four specimens in one window:** `bd` (pipeline vs vendor) · `account_number` (clean in smartx,
contaminated in cot-BD) · `account_id` (a UUID where digits were expected, producing a clean-looking
0.0%) · the inflection feed key (slugs where numbers were described).
✅ **CTO BANKED IT AS A DESIGN CONSTRAINT: the 2a field registry keys on `(table, column, measured
content-grade)` — NEVER on column NAME alone. "A name is a label to be verified, not an identity."**

### 13:30Z BAR — PRE-REGISTRATION **AMENDED** @60a115e95c (see also @029b146138)

AE's measured forward call folded in **before the fire**: zeros-with-PASS **structurally cannot recur**
(the vacuous `0==0` wholly-empty SKIP carve-out was **already retired** in the deployed re-pin, RP-W5
item 4); served spine expected **healthy non-zero**; the A7 dated-contract leg expected to **S2 ERROR and
REFUSE the write**, loud, no write.
⛔ **THE ROW I ADDED THAT AE DID NOT ASK FOR: if NO A7 ERROR LINE APPEARS AT ALL, that is NOT a pass —
investigate first.** AE's read makes a **loud error the healthy signature**, which inverts the usual
reflex, so **silence needed its own row or someone would read it as success. The absence of an expected
loud failure is not evidence of health.**
*My 0608Z zeros row described a defect that had already been fixed hours earlier. Recorded rather than
quietly dropped: the pre-registration cost nothing and AE's read independently confirms the fix. **A
control that fires on an already-closed defect is cheap; the reverse is not.***

### X-ii SPLITS IN TWO (CTO ruling on the consequence AE surfaced) — and one half may land NOW

| row | scope | may proceed? |
|---|---|---|
| **X-ii-a** | Re-home the **lambda leg's WRITE target** into `_staging/` under the product root **+ W1a consumer re-validation** | ✅ **INDEPENDENT — may land NOW** under the ruled lambda-producer frame |
| **X-ii-b** | **FEED the lambda** — its **3 starving inputs** (inflection positions, `non_model_aua`, `etf_net_assets`) are **exactly the chain-written set** | ⏸ **COUPLES to X-i's feeder re-home.** CRO~A's INF chain revival is a legitimate **ACCELERATOR** in the interim — *event accelerates, clock floors* |

**The chain Stage 3 DISABLE is strictly ordered AFTER X-ii-b is verified fed** — migrate-before-kill, per
the ruling record's own clause. *The split is what makes the zeros fix actionable: the write-target
re-home does not have to wait on solving input starvation, and the starvation fix does not have to wait
on the re-home.*

### ⛔ A STALE CLOCK-FRAME LABEL I PROPAGATED — CORRECTED

**The accrual bridge's LIVE cron is `14:10Z` UTC. The `13:40Z` in older docs is a STALE FRAME LABEL** —
RP-W3 moved the leg and the docs kept the old label. **X-iii's acceptance oracle is the 14:10Z scheduled
leg.** I carried `13:40Z` from the handoff into this register and into an AE dispatch; AE caught it.
*A time in a doc is a claim about a schedule, and a schedule that moved leaves its old label behind — the
same frozen-not-live class as a hand-copied count. Corrected at the one place it appeared.*

### RESIDUALS — THE GRAIN-LABELLED PAIR (CRO @8f14253ae9), and the headline moved UP

**INFLECTION: 98.0% at RAW-ROW grain / 100.0% at REAL-ACCOUNT grain.** Both true, different grains, and
**neither may be quoted bare.** The 11 are designed `$0` feeder stubs, **zero AUA unjoined**, cause
CLOSED as book-definition-by-design.
> *I banked that residual so nobody would quote 98.0% as if the remainder were understood. It discharged
> in the best available direction: **the remainder IS understood, and the honest headline number went
> UP.*** A parked unknown is not a pessimistic estimate — it is an unknown, and measuring it can move the
> number either way.

**49F: the 14 dispositioned per-account** — 2 closed Schwab accounts (map staleness), **1 genuinely open
single account**, and the nine-digit family concentrated in ONE model (Opal Conservative Growth) **whose
custodian is NOT NAMEABLE AT REST.** That naming rides **RECON-2's endpoint question at CRO~A — the one
residual thread still open.** *DS deliberately named no custodian without evidence; that restraint is the
finding's integrity.*

---

## 4i · STAGED — THREE `/artifact-design` BUILDS (Andrew-direct @f73ad4d22a, LD-0393). NOTHING FIRES TONIGHT.

**Andrew wants three structural artifacts built ONCE RECON COMPLETES and CONFIDENCE IS ESTABLISHED.**
**Staffing + sequencing at trigger is THIS SEAT with CTO.** Recorded now so they are not discovered later;
**explicitly not dispatched.**

| # | build | scope as he stated it |
|---|---|---|
| **A-1** | **mdpf final structure** | **EXHAUSTIVE** — every lambda / trigger / event-trigger / code-pull / dependency, **vendors through `opal-data-portal-v2` serving** |
| **A-2** | **ADVI** | the same form |
| **A-3** | **the 49F Archetypal gold runner** | script order + **what changes under raw-figures** |

**PRE-TRIGGER ADD, already routed:** the **Schwab performance fact-table assessment** → CRO~A as
**RECON-2 input** (not part of the three builds; it feeds them).

### THE TRIGGER, MADE CHECKABLE — because "once recon completes" is otherwise an act with no trigger

*ITEM_0's own failure mode is an act that lands "when someone gets to it."* His words set the trigger; my
job is to make it decidable without widening it:
- **NECESSARY:** the `SSOT_RECON_MATRIX` cells for that product's **six pattern legs read `CERTIFIED`** —
  **not merely `DELIVERED`.** Per-product, so A-3/A-1 can trigger before A-2 if advi's cells lag.
- **SUFFICIENT: ANDREW'S CONFIDENCE WORD.** ⛔ **"Confidence is established" is HIS phrase and therefore
  HIS call — I do NOT substitute the matrix for his judgment.** The matrix tells us when the *evidence* is
  ready; it cannot tell us when *he* is confident. **A certified matrix is a green light to ASK, never a
  green light to FIRE.**
- **NOT gated on:** anything else. No new approval step is created here.

### ⛔ THE PRECONDITION THAT MATTERS MOST, AND TONIGHT IS THE EVIDENCE FOR IT

**These artifacts MUST be built from the recon's CERTIFIED cells, never from the catalog** — and his
ordering (recon first, artifacts after) is *why* it will work. **In this one window the records were wrong
about:** the producer of `_aggregate_aua` (an INFERRED cell — it was the lambda, not the chain) · the
accrual bridge's clock (`13:40Z` was a stale label; live is `14:10Z`) · a "no model feed exists" cell that
turned out to be a **live daily pipeline** · a leg rate quoted as a path rate (99.8 vs 99.65) · four
name-vs-content column collisions · a "single-source" script that was **two drifted sources**. The decomp
that started this program measured **6 of 10 records FALSE.**
> **AN EXHAUSTIVE STRUCTURAL ARTIFACT BUILT FROM RECORDS WOULD LAUNDER EVERY ONE OF THOSE ERRORS INTO A
> DIAGRAM PEOPLE TRUST.** That is the whole risk of A-1/A-2, and it is exactly what his
> recon-completes-first ordering prevents.

**SECOND PRECONDITION — "EXHAUSTIVE" NEEDS ITS DENOMINATOR AND ITS CENSUS KEY.** Any enumeration in A-1 or
A-2 states *how many* and *keyed how*, because: a `list-*` count that was not paginated is **a page size
wearing a total's clothing** (measured this estate: 100 rules reported against a true 142; 50 lambdas
against 196), and a census keyed at the wrong identifier family **silently spans two firms**
(`blackdiamond/` holds both `49f/` and `cottonwood/`). **An artifact claiming exhaustiveness without a
denominator is the strongest possible form of an unverifiable claim.**

### ✅ CO-SIGNED BY CTO (062542Z) — all four, plus one tightening and one cert-coverage gap closed

**Co-signed as written:** the checkable trigger (with the ⛔ *certified-authorizes-the-ASK-never-the-FIRE*
distinction going into CTO's copy verbatim) · certified-cells-never-catalog · denominator + census key on
every enumeration (already the matrix's L1 rule; the builds inherit it as a **hard formatting
requirement**) · sequencing **A-3 → A-1 → A-2**, reached independently.

**CTO's sharper framing of the risk, adopted: A-1/A-2 are TRUST-AMPLIFIERS — a diagram LAUNDERS PROSE
ERRORS INTO TRUSTED GEOMETRY.** That is why their inputs carry the higher bar.

**THE TIGHTENING — A-1's cell bar now explicitly includes X-i + X-ii-b LANDED.** A-1 documents the
**POST-cutover** form, and the cutover is still moving the structure A-1 would draw. *Drawing a shape
that changes next week is the one way an exhaustive artifact is born stale.* A-2 still waits for a
structure that exists (advi has no product root yet).

**CERT-COVERAGE GAP FOUND AND CLOSED (MSTR/CVO surfaced): INF chapters 01/02 were NEVER CERT-ROUTED — the
INF leg had been resting on CTO's own read.** Now CERT-REQUESTED at CVO: 01 stop-mechanism + **the LANDED
CPR-4 serve outcome.** *A leg resting on a reviewer's read rather than a cert is exactly the shape the
certified-cells-never-catalog rule exists to catch — and it was found one layer above the artifacts,
in the recon itself.*

> ⛔ **REFINEMENT TO SOMETHING I TOLD DS, RECORDED BECAUSE THEY ACTED ON MY WORDING: I said the residual
> leaves the exception set "on its verified landing." CTO specifies the verification: THE CVO CERT.** The
> CPR-4 cert **doubles as the ratified-TRANSITIONAL retirement-bar verification** — **on `CERTIFIED`,** the
> residual leaves the exception set and **spec §3 amends.** So CPR-4's deploy is *not* the retirement;
> **the cert is.** My "verified landing" was compatible but under-specified, and under-specified is how a
> lane closes an item one step early.

## 4j · THE WINDOW'S ORGANIZING INSIGHT — and a precondition **I** under-specified

### TWO NEW ROWS (CTO ruled, DS/AE lane, NORMAL deploy cycle, nothing tonight, NOT bar-relevant)

CRO~A measured a concurrency collision: **DS's CPR-4 republish via direct SSM ran mid-chain on the same
runner.** Direct SSM is a **FIFTH armed dispatch path**, carrying **neither the trigger's env export nor
the dispatch lock.** The **C_01 guard REFUSED** the mode-incoherent input — **no data harm**; INF
re-dispatched 06:45Z.

| row | remedy |
|---|---|
| **R-a** | **Host-level chain mutex inside `orion-gold-dispatch.sh`** — serialization at the **convergence point**, closing all five paths **and future ones BY CONSTRUCTION** rather than enumerating them |
| **R-b** | **`INF_AOR_FOLD_ACTIVE` mode resolution SINGLE-HOMED on-host** — per-caller env means **independently-mutable mode definitions** |

### ⛔ ONE PATTERN, THREE INSTANCES IN ONE WINDOW — this is the window's real finding

| # | two-or-more independently-mutable definitions of ONE thing | remedy |
|---|---|---|
| 1 | **two RUNTIMES** writing one key (`mdpf_aggregate_aua` in the chain **and** in-process in the lambda) | ONE runtime (Andrew ruled: the lambda) |
| 2 | **two SCOPE definitions** that happen to agree (map's bronze listing vs feed's registry filter) | **single-homed** universe predicate |
| 3 | **five CALLER-LOCAL MODE definitions** (per-caller env export) | **single-homed** on-host resolution + a mutex at the convergence point |

> **THE LAW THE WINDOW EARNED: INDEPENDENTLY-MUTABLE DEFINITIONS OF ONE THING ARE THE DISEASE; SINGLE-HOMING
> IS THE REMEDY — and it does not matter whether the duplicated thing is a runtime, a scope, or a mode.**
> Each instance presented as a different bug (a mystery freshness, a coincidental join rate, a
> concurrency collision) and **all three are one shape.** CTO generalized 1→2; instance 3 confirms it
> generalizes past the layer it was found at. **Enumerate-the-paths is the wrong remedy in every case —
> R-a closes the fifth path *and the sixth nobody has built yet* precisely because it serializes at the
> convergence point instead of listing callers.**

### ⚠ AND THE COLLISION TRACES TO A PRECONDITION *I* WROTE TOO NARROWLY

**DS IS NOT AT FAULT — CTO put that on the record and I am confirming it from my side, because the
narrow part was mine.** My CPR-4 choreography condition (4) asked for confirmation of **"no intersection
with the 13:30Z MDPF bar window."** DS answered exactly that, correctly: *"bar-clear confirmed at
execution: republish completes ~7h before 13:02Z, INF D-chain not the MDPF cadence."*
**The real collision surface was HOST-LEVEL CONCURRENCY on the shared runner — which my condition never
named.** I specified the collision surface I knew about and not the one I didn't, so **DS answered my
question correctly and my question was the wrong one.**
> **FOURTH under-specified precondition of mine this window** (one deploy prefix of three · `PRECONDITION:
> none` over a live serve-hold · "verified landing" where the bar is a cert · and now "bar-clear" where the
> risk was host-clear). **The pattern is consistent enough to be a finding about me, not about the lanes:
> I keep specifying the surface I already have in mind, and a precondition written that way is silently
> scoped to the author's blind spot.** The generalizable fix is the same one CTO just ruled for the
> machines: **ask "clear of ANY concurrent execution on this host?" not "clear of the window I am thinking
> about?"** — a predicate, not an enumeration.

## 4k · ⛔ THE bd-MIRROR FINDING **INVERTED** — Branch A, live consumer, deletion off the table

**AE searched FOR the path (denominator printed: 74 hits / 25,210 files; bands HEAD=1 SURFACED=27
CONFIG=17 DOC=29; **3 code-plane operative refs**). BRANCH A: LIVE CONSUMER, RAN TODAY ~00:11Z.**

- `bd-49f-runner/lambda_function.py:59` `SCRIPT_KEY="code/bronze/cot_bronze_ingest.py"` → `:74`
  `download_file(opal-data-bd, …)` → `:75` `importlib` exec, firm-bound (all 4 `BD_*` envs set BEFORE
  import; `_assert_firm_separation` as belt). **ADVI_BDAPIMIG P1-B — the DAILY 49F Black Diamond REST
  ingest.** Newest invocation stream **2026-08-11 ~00:11Z**, daily before it.
- **IAM `bd-49f-interim.tf:229` grants the runner `opal-data-bd/code/bronze/*` — the target is in the
  APPLIED design.**
- The runner's docstring declares it: *"NOT A FORK (Model B): the script is ONE source … deployed to
  `opal-data-bd/code/bronze/` and run firm-bound via env"* — **because the runner role carries an explicit
  DENY on `opal-data-cot`.**

> ⛔ **FIRM SEPARATION IS *WHY* THE COPY EXISTS, NOT WHAT IT VIOLATES. Branch B's remedy (delete) would
> have broken a live client-facing daily 49F ingest.** CTO's violation ruling reasoned correctly from two
> true facts (only repo home is `data/cot/`; `safe_deploy_core` maps cot → `opal-data-cot` only) and was
> **missing an applied, IAM-granted, documented second consumer.** ⚠ **RE-ADJUDICATION ROUTED TO CTO.**
> *The method decided this: enumerating FROM the script returns clean-and-empty and the deletion proceeds.
> The search-FOR-the-path instruction is the only reason the consumer surfaced — **exhaustive-and-empty was
> the wrong axis, not an absence.*** **Second time this window a "violation/absence" finding inverted on
> grounding** (the first: cottonwood's "no model feed exists" → a live daily pipeline).

### THE DEFECT INVERTS INTO SOMETHING TRACTABLE — and it is the SINGLE-HOMING LAW's FOURTH INSTANCE

**ONE source has TWO deploy targets, and `safe_deploy_core`'s cot tree serves only ONE.** Nothing
redeploys the bd-side copy → it froze 08-04 **while executing daily for 49F.**
⚠ **DS's C-2/C-3 deploy tonight FIXES COT AND WIDENS THE DIVERGENCE** — 49F keeps running the pre-fix
double-lag bytes daily. The matrix's 49F `[U]` adjacency row is now **measured LIVE-EXECUTING**, not
same-pattern-probably.

| # | independently-mutable definitions of ONE thing | remedy |
|---|---|---|
| 4 | **ONE source, TWO deploy targets, only one served** | **declare the fan-out ONCE at the convergence point** — Rule 13's SHARED-repo-home S3-membership guard shape (key-exists=update, 404=loud-skip) |

### MY CALL ON TONIGHT (CTO may override)

✅ **DS FIRES THE 15:06Z DEPLOY.** *Withholding a correct fix from cot to keep two wrong copies aligned is
strictly worse than fixing one and naming the gap.* **REQUIRED of DS:** state the gap **explicitly in the
deploy record** (this deploy does not reach the bd-side copy the live 49F runner executes; 49F continues
on pre-fix bytes until the second target is sanctioned). ⛔ **FORBADE hand-copying the fixed bytes to the
bd prefix** — patching the mirror deepens the two-source defect; the sanctioned target is the fix, and it
is CTO's to rule. **Until ruled: assume every cot-side fix does NOT reach 49F.**

> **DS's ORIGINAL CATCH WAS A CLOSING ONE-LINER ON A MESSAGE ABOUT SOMETHING ELSE.** It produced an
> architectural ruling, an exercised gate with an honest negative, a third-control-surface finding, a
> re-adjudication, and a permanent remedy shape. **A drift they could have left unmentioned was the only
> visible symptom of a missing deploy leg on a client-facing daily ingest.**

**X-ii-a's emitter-liveness precondition also discharged:** `opal-assets-daily-emitter` ran TODAY 01:30Z
consuming the staging tree with **honest roll-forward flags** — it read the 08-10 zero partition and
emitted `partner_aua_total $1.88B vintage=rolled_forward coverage=incomplete`. **The zeros propagate as
FLAGGED STALENESS, not as zeros** — the guard behaving well, and relevant to the bar's amended expectations.

## 4l · ACT **CPR-5** DISPATCHED (same-day) + the FIFTH exception member + RECON-5a scope

### CPR-5 · DECLARE THE SECOND DEPLOY TARGET — CTO ruled the remedy, I staffed it

| field | value |
|---|---|
| **OWNER** | `0.4.0_DS_ClientPlatform` (the deploy-map change) |
| **VERIFIER** | `0.7.0_AE_CloudOps` (the bd-side landing) |
| **TRIGGER** | **TODAY'S CYCLE**, sequenced AFTER the 15:06Z cot deploy — the fixed bytes must exist before they can be carried. *CTO: "49F executes pre-fix double-lag bytes every day until it lands — today's cycle, please."* |
| **SHAPE** | a `safe_deploy_core` row declaring `opal-data-bd/code/bronze/cot_bronze_ingest.py` a **second target of the cot-tree source**, under **Rule 13's SHARED-repo-home S3-membership guard** (key-exists=update enforced, 404=loud skip, first-mints explicit) |
| **PRECONDITION** | ⚠ **stated as a PREDICATE, not a spot-check: does anything in the changed code paths read a firm-scoped env var, path, or lag constant whose value differs between the cot and bd invocations?** The fix was exercised in the **cot** context; the same source runs under the bd-49f-runner with different env (4 `BD_*` vars set before import, firm-bound). *"Should be firm-agnostic" is exactly the phrasing I have had corrected four times tonight, so it gets a predicate.* |
| **ACCEPTANCE** | DS: the row lands and the sanctioned path puts the fixed bytes at the bd key, **ETag-verified against the fixed COT-SIDE bytes as landed** (not a local copy). AE: ⚠ **the 49F runner's NEXT SCHEDULED INVOCATION executes them** |

⛔ **THE OBJECT LANDING IS NOT THE FIX TAKING EFFECT** — the runner `download_file`s at invocation (`:74`)
and `importlib`-execs (`:75`), so a correct object proves only that the object is there. **Verify on the
invocation.** ⛔ **Hand-copying to the bd prefix stays FORBIDDEN** — CPR-5 exists so nobody has to.
⛔ **BLAST RADIUS: a LIVE DAILY CLIENT-FACING 49F INGEST.** Low risk (same source, exercised, 81/81
non-carry with mutants) but it **does not inherit cot's green**, which is what the predicate above is for.

### FIFTH EXCEPTION MEMBER — Andrew instruction 5 (~0628Z): *"Granted / on TWR calculation from Schwab"*

The ratified exception set gains its fifth member: **49F TWR / period-returns COMPUTED FROM raw Schwab
custody components** — raw inputs + an **explicitly named computation**, i.e. **the opposite of a
residual.** Spec §3 amended. **Per-firm performance leg now resolves: `inf` = vendor TWR raw · `49f` =
computed-from-components · `cot` = TBD on RECON-5.**
*This is atom 8 working as designed rather than being eroded: the invariant was never "never compute" —
it is "compute only what no single vendor endpoint gives, and NAME it." A named computation over raw
components is a legal exception; a subtraction standing in for a missing field was not.*

### RECON-5a SCOPE — one named cell added (CRO @4f57b27927)

RECON-5a now carries **"what does BD ship on the performance/TWR surfaces"** — **the LAST open
performance-leg cell** in the three-firm matrix. **Whoever is seated on 5a inherits it scoped**, and it
**may close at rest** (the 561 rebalancer `model_detail` bodies + the RCN-0001 family map). Nothing else
in 5a's split changes. *Recorded to keep my register and CRO's map in lockstep — the two-record drift
class is what this line exists to prevent.*

## 4m · X-ii-a DISPATCHED on a CO-SIGNED history ruling · R-a gains a precondition · two timing corrections

### ⚖ THE X-ii-a HISTORY DECISION — CO-SIGNED **(c)**, and it is the window's cleanest layer call

AE flagged it and **refused to decide it alone**: the old tree's newest partitions are the 08-09/08-10
ZERO artifacts, which poison the producer's roll-forward. Their options were **(a)** copy all, poison
persists · **(b)** copy all except the two zeros. **Neither was right, and the reason is a layer
confusion:**
> **THE QUESTION CONFLATES *WHAT THE HISTORY CONTAINS* (archival / point-in-time) WITH *WHAT THE
> ROLL-FORWARD READS* (producer selection). (b) SOLVES THE SECOND BY EDITING THE FIRST** — and doing a
> later layer's job at the archive layer is **IRREVERSIBLE** (Rule 17a's spine, appearing here as
> history-vs-selection). An archive pruned to make a selector behave **no longer answers "what did we
> have on 08-10," and that question gets asked later by someone who does not know we pruned it.** It also
> breaks the rollback symmetry the plan depends on.

**RULED (CTO co-signed my (c) in full):**
1. **COPY EVERYTHING, never move** — old tree freezes as the **symmetric** rollback.
2. **FIX THE SELECTION AT THE READER, and CTO's formulation is sharper than mine — adopt theirs: the
   roll-forward SKIPS PARTITIONS ITS OWN CURRENT CODE WOULD HAVE REFUSED TO WRITE.** Keyed on honest
   markers (coverage flag where present; **`partners==0` is precisely the retired carve-out's signature
   AND the current S2-ERROR condition**). **That is what makes it principled rather than special-cased —
   not "exclude two objects we dislike" but "decline to treat as authoritative anything present code
   would refuse to emit."** It generalizes to the NEXT incomplete partition, which is why it is the right
   layer. AE has implementation latitude inside the shape.
3. **FALLBACK if the selector cannot be marker-aware today: (a) WITH THE POISON NAMED AND TIME-BOXED TO
   X-ii-b.** *Visible carried risk beats an invisible history edit.* Not (b).
4. ⛔ **ESCALATION: if any path reaches "delete history so a producer behaves," IT GOES TO ANDREW — never
   inferred.** And **neither exec stretched his point-in-time ruling onto this case** — he ruled it for
   ASSIGNMENT history, a business event, and a zero-dollar intermediate staging artifact is not that. **The
   adjacency was flagged, not claimed.** *Stretching a sovereign ruling to cover a case he did not rule is
   its own error, and it is the more tempting one because it feels like deference.*

**AE's refusal was the load-bearing act:** (b) was defensible, produced the right *outcome*, and would
have passed unquestioned. Stopping to name it a **data-selection act** is what surfaced that the right
outcome was being reached by an irreversible and invisible mechanism. **Third time tonight that seat
stopped exactly where a lane should.**

### R-a GAINS A NAMED PRECONDITION — from CVO's ch.01 cert (@1c6068a0a7, zero refusals)

⛔ **A DISPATCH-PATH CENSUS FOR THE INF RUNNER MUST BE ENUMERATED AND CLOSED *BEFORE* THE MUTEX IS
SIZED.** Five armed start paths are known. **Sizing a mutex against an unmeasured N is the denominator
lesson applied to a remedy** — it yields a serializer that misses the sixth path and reads as complete.
*Both CTO cert requests are now discharged; effectiveness + the CPR-4 serve fold together at 13:47Z —
one read, two folds.*

### TWO TIMING CORRECTIONS — one of them mine

- ⚠ **MY "SAME-DAY / TODAY'S CYCLE" ON CPR-5 CARRIED TWO CLAIMS AND ONLY ONE IS TRUE. AE caught it before
  it overpromised: THE ACT IS SAME-DAY; THE PROOF IS OVERNIGHT.** Leg (a) bd-side landing = today
  post-15:06Z. **Leg (b) — the fix actually IN EFFECT — waits on the runner's next scheduled fire ~00:11Z
  on 08-12** (earlier if the session-chain invokes; AE takes whichever comes first). *A landed object is
  not a landed fix, and "same-day" let those blur.* AE has committed that if their session ends before
  leg (b), **the two-leg bar goes into their handoff as a successor duty rather than silently
  half-closed.**
- **X-iii's acceptance oracle is the 14:10Z scheduled leg** (not the stale 13:40Z label I propagated).

### THIRD `comp-pipescript deployed` BLINDNESS — banked as a SET, not three anecdotes

**Bundle-routed scripts are excluded from `deployed` sweeps.** With the lambda-zip channel and the
1-of-6-layers gaps, that is **three distinct blindnesses in one instrument in one window** — on CTO's
roster together. X-iii's acceptance correctly rides **the mint's sha-stamped verify** instead.
*AE's independent re-verification of DS's minted bundle, and their sequence CONSUMING the bar
pre-registration as an INPUT, are both recorded by CTO as the reference standard.*

## 4n · ⚠ CPR-5's URGENCY PREMISE NARROWED — the act is right, the emergency was not real

**The predicate loop closed the way it should: DS answered all three aimed targets with `file:line`, and
AE VERIFIED the load-bearing one on the CONSUMER's source rather than accepting it.**
`bd-49f-runner/lambda_function.py` calls only `mod._window_for(table, run_date)` (`:139`) +
`mod.ingest_table` (`:147`) — **ZERO sweep invocations.** *(Another name-vs-content catch: the `:160`
"sweep" strings are comments about transaction chunking — a different sense of the word.)*

| target | answer |
|---|---|
| **C-3** (anchor/sweep fix) | ⛔ **INERT on the bd executed path** — the sweep is never invoked there |
| **C-2** (window fix) | **byte-identical delegation, ZERO behavioural delta** on that path |
| `BD_SNAPSHOT_ASOF_LAG_BDAYS` | **`lag=1` on both paths BY DESIGN** (cited) |
| `COT_MARKET_HOLIDAYS` absent on bd | ✅ **a REAL but PRE-EXISTING, bounded, weekday-only arithmetic divergence** on holiday-adjacent days — census-lined; the one-line TF export awaits CTO's word rather than landing uninvited |
| AE's verdict | **NO FLAG** — aimed, cited, source-confirmed |

> ⚠ **SO THE PREMISE BEHIND *"49F executes pre-fix double-lag bytes every day — today's cycle, please"* IS
> NARROWER THAN IT READ, AND I HELPED PROPAGATE IT.** The bytes ARE stale and the divergence WAS real, but
> **its behavioural consequence on the bd executed path is approximately nil** — the one change that would
> have mattered is never invoked, and the other is a pass-through. **49F is not running a live defect
> daily; it is running byte-stale code whose staleness currently makes no difference.**
> ✅ **CPR-5 IS STILL RIGHT AND STILL LANDS** (DS's row @4100c90f47, exists=update / 404-loud /
> fail-closed) — but **its honest value is STRUCTURAL, not behavioural:** it closes the drift class so
> **future** cot-side fixes reach 49F by construction. **It is NOT an emergency, and saying so matters:
> urgency spends credibility and distorts sequencing, and DS carried four acts tonight.**

**⛔ THE INVERSION WORTH KEEPING: the finding we chased urgently (the bd double-lag) is INERT; the one
that surfaced as a side note (the absent holiday env) is the LIVE divergence.** Small, bounded, and
pre-existing — but it is the item with an actual correctness consequence, and it would have stayed a side
note if AE had not aimed the predicate at three named targets instead of answering yes/no.

**FOURTH `comp-pipescript` ENTRY, and it is a DIFFERENT CATEGORY:** CPR-5's second targets are **honestly
EXCLUDED from pipescript-verify — deliberate and declared.** *A declared exclusion with a stated reason is
not a blindness; it is a documented boundary.* Keeping the distinction so the roster reads as **three gaps
plus one honest limit**, not four bugs.

## 4o · X-ii-a INTENT CONFIRMED · **"EXISTENCE IS NOT AUTHORITY"** · and twice I had to say a rule does NOT block something

### X-ii-a: BUILD IT — and the selection needs ZERO code change

AE gave **intent-before-build** on an act with many crossings; confirmed on all four rows. **Their
mechanism read beat my reasoning: I argued (c) from a producer defect that does not exist.**
`load_prior_partner_block` is **already** stamp-keyed (*"NEVER `max(prior_dates)`"*, the 07-09
fabricated-residual law), and a `partners==0` partition carries no block → `None` → fail-safe →
Sentinel-2 loud error → **write refused. A refused-write-class partition is structurally incapable of
being read as authoritative.** So (c) costs zero code, and the (a)-with-named-poison fallback is
**unneeded — there is no poison to carry.**
**AE also refused a temptation I did not anticipate:** the only available "improvement" would be a
walk-back past such partitions, which would **amend the ruled never-`max` law** — so it goes to CTO as a
law amendment, never inside this act. *They applied my own escalation discipline to a case I had not
thought to cover.*

### ⛔ NEW ROW — THE ONE READER THAT GENUINELY FAILS THE PREDICATE

**`mdpf-daily-trigger:413` discharges its roll-source check with `head_object` — EXISTENCE ONLY.** A
`partners==0` partition **EXISTS**, so **the DEFER gate reads a refused-write-class artifact as a valid
roll source.**
> ** EXISTENCE IS NOT AUTHORITY. ** The roll-forward reader was already safe; **this consumer is not.**
> **THIRD VARIANT OF ONE FAMILY TONIGHT:** *a name is not a grain* (four column specimens) · *a leg rate
> is not a path rate* (99.8 vs 99.65) · **existence is not authority.** All three are **"the label
> satisfied the check and the content did not."**

**Correctly NOT built inside X-ii-a** (scope discipline; its env repoint rides as planned). **Routed to
CTO's roster** — the gate's verdict quality is theirs.

### ⚠ TWICE TONIGHT I HAD TO SAY A RULE DOES NOT BLOCK SOMETHING — that is a pattern, not a coincidence

1. **The orphaned Stage5 alarm deletion:** the moratorium bans **BUILDING** notification machinery, **not
   deleting a dead instance of it.** AE held it (correctly, for CTO's roster ownership) but flagged the
   moratorium as the reason.
2. **The `:413` verdict-quality fix:** AE flagged it *moratorium-adjacent*. **It is neither rule.** The
   moratorium bans building alerts/monitors — **a landed gate returning a low-quality verdict is not
   notification machinery.** And no-inferred-gates bans **NEW approval gates** while **explicitly
   protecting the landed mechanical gate layer** — **improving what an existing control READS is a
   CORRECTNESS FIX, not the creation of a gate.** It needs CTO's roster word, not Andrew's authorization.

> **THE PATTERN: these rules were each written to stop a SPECIFIC harm, and a seat moving fast reads them
> as blanket prohibitions on the whole TOPIC.** The cost is real — it freezes correct work and it routes
> asks to Andrew that were never his. **Reading a NEVER-rule narrowly and exactly is not looking for a
> loophole; it is reading it as written.** *Both instances were caught only because a lane surfaced the
> hesitation instead of silently not doing the work — which is the only reason this is visible at all.*

## 4p · STAGED INPUT — GIPS-TWR feasibility @e323c1cfac (YES at DAILY tier, one conditional)

Andrew tasked a GIPS-standard TWR feasibility assessment on the Schwab fact tables against his standard
doc; CRO delivered it. **VERDICT: YES at the DAILY TWR tier, zero hard-stops** — `dim_balance` is the
authoritative daily fair-value series, `fact_trn` the classifiable ledger. **No urgency claim**; it is
feasibility recon feeding the four-month program's **2a performance leg**. Sequencing mine.

**THIS IS THE GROUNDING UNDER THE FIFTH EXCEPTION MEMBER.** Instruction 5 granted *49F TWR computed from
raw Schwab custody components*; this assessment establishes the components **can** carry it at daily tier.
*Granted-and-feasible are two different facts and we now hold both — worth noting because a grant without
a feasibility read is how a computation gets promised and then quietly can't be built.*

### ⛔ MY SEQUENCING RULING FOR THE EVENTUAL BUILD TO — THE CONDITIONAL IS TASK 1, NOT TASK N

CRO names five refinement cells as natural TO seams (all small), **two of which double as CRO~A's
archetype-spec rows.** The tempting decomposition is five parallel cells. **Do not.**
> **BUILD TASK 1 = the transaction-code classification table + the UNRESOLVED-CODE MATERIALITY
> MEASUREMENT — because that is THE SINGLE CONDITIONAL THAT COULD RE-FIRE A HARD-STOP.** A "YES with one
> conditional" verdict means **the conditional gates the verdict**, so it runs FIRST and alone.
> **Parallelising it would build four cells on a feasibility that task 1 might then invalidate** — and the
> four would look finished, which is worse than not having started them.

**Two of the five cells are shared with CRO~A's archetype spec — those coordinate rather than duplicate**
(the same one-source-two-consumers shape the single-homing law keeps surfacing, here in *work* rather than
in code). **No dispatch tonight**; it stages behind the recon-fronts-implementation ordering with the
other 2a work.

## 4q · HOLIDAY EXPORT APPLIED · X-ii-a STAGED · my sequencing word · **single-homing instance FIVE**

### ✅ `COT_MARKET_HOLIDAYS` ON THE bd PATH — APPLIED @76fa8a9975

Literal **byte-verified identical** to the cot export; targeted plan showed exactly the one env add on
`module.bd_49f_runner`; safe-applied; **live `get-function-configuration` returns the value**; targeted
replan rc=0. Normal cycle, not bar-coupled.
**Economy worth noting: the next 49F fire (~00:11Z) is ALSO the CPR-5 leg-(b) observation window — one
fire discharges BOTH observations** (holiday-aware arithmetic *and* the fixed bytes executing).

> ⚠ **AND IT IS SINGLE-HOMING INSTANCE FIVE — AE FLAGGED IT THEMSELVES: a 219-char holiday literal is now
> HAND-TWINNED across two TF files that must stay byte-identical.** *The remedy for a missing-export
> divergence introduced a new (tiny) two-source divergence.* **Five instances tonight, one disease:** two
> runtimes on one key · two scope definitions · five caller-local modes · one source / two deploy targets ·
> **one literal / two TF files.** **The law's general statement applies to its own remedies: declare the
> fan-out once at the convergence point.** Bounded and declared, so not a now-fix — a register candidate
> for the same treatment (shared TF local or data source), CTO's roster to sequence.

### X-ii-a AE HALF STAGED-NOT-APPLIED @2740e4de8f (`validate` rc=0 both roots)

Three choices that each avoid a specific trap, called out because the reasoning is reusable:
- **`PlatinumRollSourceRead` as a PURE ADD, old grants retained** — *"a vanished grant is a permanent
  silent DEFER."* That failure would have read as a scheduling quirk for weeks.
- **The emitter literal STATEMENT-LOCAL, deliberately NOT via `local.gold_mdpf_prefix`**, because that
  local also names the publishers' **non-moving** artifacts — **declining a convenient local that would
  have silently widened the blast radius.** Same discipline as declining to reuse W1a's stale staging.
- **Producer IAM needs NOTHING** (`GoldMdpfCanonicalWrite` already subsumes the new prefix) — **and the
  apply-time simulate + isolated positive control still runs.** *"Already subsumed" is a read of a policy
  document; the simulate is applied truth.*

### ⏱ MY SEQUENCING WORD — request DS's X-ii-a line AFTER their 15:06Z deploy + CPR-5 carry close

**X-ii-a's acceptance oracle is the producer's next SCHEDULED 13:30Z run — and today's 13:30Z IS the bar,
firing before X-ii-a could be applied. So its acceptance rides TOMORROW's fire regardless.** Hurrying DS's
half buys nothing on the acceptance clock and costs a **fourth** concurrent thread on a seat already
holding the 15:06Z deploy, the CPR-5 carry, and the 13:47Z watch for CPR-4 step 4.
> **Stated as the honest schedule rather than an optimistic one: X-ii-a's window opens when DS's plate
> clears, and acceptance is tomorrow's scheduled fire.** *I would rather say that than let "today" quietly
> mean "queued behind three things."*

### `comp-iam` LINE — surfaced, correctly not chased

`mdpf-daily-trigger` carries a **pre-existing** action-level *"MISSING `s3:PutObject`"* — structurally not
mintable by a GetObject resource-add to a GetObject statement. **And the load-bearing half: `comp-iam gaps`
is ACTION-ONLY and does not compare resource ARNs, so AE's resource-grain adds are invisible to it in
EITHER direction — it can neither credit nor fault them.** That is the known `(action)`-not-`(action,
resource)` insufficiency, and it means **the tool's silence here carries no information at all.** The
apply-time simulate is the real check, as ruled.

## 4r · ANDREW INSTRUCTION 6 (~0700Z) — GIPS on Orion (Inflection), then Cottonwood off BD

`atom_decomp` on the **Orion endpoint surface**: GIPS feasibility for **Inflection** (current pulls +
endpoint delta, **missing data specified by SHAPE**), then **Cottonwood off BD**. **Held by CRO~A**,
interleaved with the INF run-2 watch. **Staffing-relevant to me as awareness only — no dispatch owed.**

**⛔ THE EGRESS GRANT HERE IS WORK-SCOPED, NOT SESSION-SCOPED** — *"as much egress and endpoint testing as
you need,"* both vendors, **for this work.** See the amended table in §4c: it **rides the work and survives
where the blanket lift's session bound does not.** That distinction is now the load-bearing part of the
egress record, and my original §4c line was too broad on it.

**DISCIPLINE CARRIED: the 49F verdict @e323c1cfac is the TEMPLATE — cite, do not re-derive.** *Re-deriving
a delivered verdict is how two records of one fact come to disagree; the whole single-homing law applies to
findings as much as to producers.*

**AND IT COMPLETES THE THREE-FIRM PERFORMANCE PICTURE, each leg by a different route:** `inf` = vendor TWR
raw, now getting its own GIPS feasibility off Orion · `49f` = computed-from-components, **granted AND
feasibility-confirmed** · `cot` = measure-not-assume, off BD. *Three firms, three mechanisms, one
question — which is exactly the shape RECON-4 found for the join layer, arriving again at the performance
layer.*

## 4s · ⛔ SHAPE-TRANSPOSITION (Andrew ~0658Z @6e180df78e) — the first firm-runner TO must NOT be a PORT

**His doctrine, explicit:** a **perfect, immaculate, GIPS-compliant 49F gold runner, NO PATCHES**, whose
**SHAPE — the field contract + the script sequence — is what all future runners INSTANTIATE.** Per-firm
replication is **sourcing the constituent FIELDS**, never porting code.

**PER-FIELD DISPOSITIONS (and they are Rule-24 clean — MECE, one grain, one intent):**
`RAW` · `MANUFACTURABLE-as-named-computation` · `ABSENT-with-shape`.
*Note the third value does real work: an absent field still gets its SHAPE specified, so the gap is
LEGIBLE rather than a silence. That is the same discipline as printing a denominator beside a zero.*

### ⛔ THE STAFFING CONSEQUENCE THAT IS MINE, AND THE REASON IT IS RECORDED NOW

> **THE FIRST FUTURE FIRM-RUNNER TO MUST BE DRAFTED AS CONTRACT-SATISFACTION WORK — per-field sourcing
> against the transposition maps CRO~A's instruction-6 runs will deliver — AND NOT AS A CODE MIGRATION.**
> **A port and a field-sourcing exercise are materially different TO shapes**: different acceptance
> (does each field resolve to a disposition, vs does the code run), different owners, different failure
> modes. **Recorded before any such TO exists, because "port the 49F runner to inflection" is the
> obvious-sounding draft and it is the wrong one.**

**AND IT IS THE SINGLE-HOMING LAW AT ITS LARGEST SCALE TONIGHT.** N ported runners = **N independently
mutable copies of one shape** — the same disease as two runtimes on one key, five caller-local modes, one
source with two deploy targets, and a literal in two TF files. **Andrew's doctrine IS the remedy applied
to runners: ONE shape, N instantiations by field-sourcing, never N copies.** *Sixth instance, and the only
one where the law was stated as the design intent rather than discovered as a defect.*

### A-3's MEANING SHARPENS

**A-3 is the SHAPE's AUTHORITATIVE STATEMENT**, and its design brief is this record. **Readiness bar
unchanged** (per-product `CERTIFIED` cells necessary; Andrew's confidence word sufficient). This also
confirms the **A-3 → A-1 → A-2** ordering CTO and I reached independently — A-3 is not merely the
narrowest, it is the thing the other two describe **instances of.**

**AND THE 49F BUILD'S ADMISSION CRITERION IS NOW EXPLICIT: its inputs are the quality partition's `EXTRACT`
SIDE ONLY.** *"No patches, no bullshit"* is the criterion — which the partition-verdict preconditions
already in §4i operationalize, so nothing new is needed to enforce it. **A build admitting anything from
the DISCARD side would be a patch by construction.**

## 4t · ✅ GIPS TASK 1 COMPLETE @a876ee6ae9 — **THE CONDITIONAL CLEARS.** Four cells unblock on a premise that HELD

Executed **alone**, per my task-1-first-and-alone ruling, on Andrew's direct GO. Classification table
landed: **187 code rows over the FULL 525-partition series, 2.98M transactions.**
**MATERIALITY VERDICT: unresolved residue = $3.18M over 25 months = 0.178% of book / 0.226% of
external-flow magnitude**, 98 rows across 10 low-frequency adjustment codes. **THE HARD-STOP DOES NOT
FIRE; the DAILY-TWR verdict stands UNCONDITIONED.** The four refinement cells decompose whenever the
archetype trigger fires.
> **The ruling did exactly what it was for: the conditional was measured ALONE and it CLEARED, so the four
> cells now decompose on a premise that HELD — rather than four cells having been built and then
> re-examined against a premise that moved.** *The cheap version of this ordering is indistinguishable from
> the expensive one right up until the conditional fails.*

### ⛔ TWO REQUIRED TO ROWS — recording them as ROWS, not as flags, because a flag evaporates

| # | row | why it is REQUIRED, not optional |
|---|---|---|
| **T-1** | **`TPFEE`/`SMFEE` specimen-verify (one account vs the billing schedule) belongs IN THE FEE TO** | $55.5M, the **largest fee family**, is classified **`FEE-MANAGEMENT-INFERRED`** — empty vendor descriptions, resolved by family + adjacency + magnitude. **CRO sized the blast radius of being wrong and it is honest: even FULL refutation moves 3.9% of external magnitude — gross/net returns change, feasibility does NOT.** ⚠ **But an INFERRED classification that never carries its verification forward BECOMES FACT BY ATTRITION.** The specimen-verify is a **required row of the fee TO**, not a suggestion, and it is in this register so it survives the gap between now and that TO |
| **T-2** | **The cross-account PAIR-MATCHING ENGINE is a REQUIRED BUILD COMPONENT** | the transfer/journal family (**$398M cash + $2.66B in-kind**) is resolution-**RULED per event**. **Recorded as scope so it cannot be descoped later as a nice-to-have** — at that magnitude, "we'll match pairs in a later phase" is a decision to publish unmatched flows |

### THE DENOMINATOR LESSON, AT BUSINESS SCALE — full-series over day-sample, validated hard

**The code universe is 157, not the day-sample's 21 — a 7.5× gap.** And **trusting the vendor's own
category would have inflated external flows by BILLIONS** (680K sweep rows are **INTERNAL** by the
boundary rule).
> **This is "a page size wearing a total's clothing" with a nine-figure consequence.** A day-sample would
> have covered **13% of the code universe** and reported cleanly; the vendor's own category field is a
> NAME whose content did not match it — **the name-vs-content class again, this time on a categorical field
> rather than a key column.** *Two of tonight's recurring lessons landing simultaneously on one
> measurement, and the only reason either was caught is that the census ran over the full series instead of
> a sample that would have looked sufficient.*

**RECON-6 resumes at CRO base; sequencing otherwise unchanged.**

## 4u · ✅ BOTH REQUIRED ROWS DISCHARGED @5bb3b2626d — and the in-kind result is **specimen SIX**

### T-1 — `TPFEE`/`SMFEE`: **VERIFIED BY MEASUREMENT.** The attrition risk is retired properly

Stronger than the one-account specimen I required — **the WHOLE FAMILY measured:** `TPFEE` detail text
reads **"TO ADVISOR"** on debit legs, **92 bps median implied annual rate over 4,881 accounts**; `SMFEE`
reads **"TO SEP ACCT MGR"**, 100% debits, **34 bps** (SMA-manager scale); **`MGFEE` as an explicit control**
shows the same TO/FRM two-leg shape. **Table re-graded `FEE-MANAGEMENT-VERIFIED`.**
> **This is the right way for an INFERRED label to die: by MEASUREMENT, not by fading.** The row existed
> because inference becomes fact by attrition; it closes because someone measured it instead.

**BONUS THAT BECOMES A BOUNDARY-TO INPUT:** the fee **CREDIT** legs land **`FRM {client}` in advisor
COLLECTION accounts INSIDE the book** — **a MECHANICAL discriminator for which accounts the
client-composite boundary must EXCLUDE**, and *one groupby enumerates the roster.* **That converts a
judgment call into a rule** — the composite boundary no longer needs an opinion per account.

### T-2 — PAIR-MATCHING ENGINE: **BUILT**, re-runnable, full-series measured. The bucket DISSOLVES

- **CASH: $193.7M MATCHED-INTERNAL — 48.7% by VALUE, 16.7% by ROWS, both denominators printed**, and the
  gap is explained (fewer-larger events). **$204.3M unmatched = external-by-default**, the conservative
  direction per the standard.
- **IN-KIND: 99.2% of groups are ONE-SIDED in-book = EXTERNAL-dominant ACAT class.**
- **NAMED FOLLOW-UP riding the build:** direction resolution for one-sided in-kind via **next-day position
  delta.** Recorded so it does not become a silent default.

### ⛔ SPECIMEN SIX — and CRO CAUGHT THEIR OWN INSTRUMENT BEFORE IT SHIPPED

**The first in-kind run returned `0.0% matched`.** The mechanism check found why: **`IC` rows carry
`LONG`/`SHORT` in the `debit_credit` field — POSITION SIDE, not DIRECTION — so a direction matcher
STRUCTURALLY CANNOT FIRE.**
> **NAME-VS-CONTENT, SIXTH SPECIMEN, and the most dangerous shape of it yet: a field named `debit_credit`
> that does not carry debit/credit.** And note what it produced — **`0.0%`, which is the single most
> BELIEVABLE wrong answer a matcher can return.** "No internal matching found" is an entirely plausible
> business result; **an instrument that cannot fire returns the cleanest possible negative.** That is the
> anti-correlation shape the estate's doctrine names: *the verdict is strongest exactly when the failure is
> total.*
> **CRO ran the mechanism check on their OWN instrument before shipping the number** — *could this have
> failed? look at what actually came back* — which is the only control that catches this class. **Had it
> shipped, `0.0%` would have entered the record as a measured business fact and nothing downstream would
> ever have questioned it.**

**Specimen tally, one window:** `bd` (pipeline vs vendor) · `account_number` (clean vs contaminated per
table) · `account_id` (a UUID) · the inflection feed key (slugs) · the vendor CATEGORY field (billions of
mis-scoped flow) · **`debit_credit` (position side)**. **Six — and the last two were categorical/value
fields, not key columns.** *A field registry designed only against key columns catches four of six.*

## 4v · 2a REGISTRY SCOPE WIDENED (adopted) · CVO commissioned on the 49F **A/B/C/D spec** — A-3's substrate

### ✅ THE REGISTRY CONSTRAINT NOW COVERS **ALL** FIELDS, not just join keys

CTO adopted the design input in full and committed it: the registry keys on **`(table, column, measured
content-KIND + grade)` across ALL FIELDS** — because **a key-only registry catches 4 of 6 specimens and
misses exactly the two with billions-scale and publishable-zero consequences.**
> **BANKED VERBATIM AS A DESIGN PRINCIPLE: "`0.0%` is the most believable wrong answer a matcher can
> return."** The registry must be able to express **name-kind mismatch on CATEGORICALS**, because that is
> the **silent-zero** case. **And CRO's pre-publication mechanism check is the behaviour the registry
> MECHANIZES** — *which is the right relationship between a discipline and an instrument: the instrument
> exists so the discipline does not have to be remembered.*

**The `FRM` fee-credit-leg discriminator is already inside CVO's ABCD commission (§2 boundary work)** — *a
judgment call converted to a rule is exactly what the spec wants*, and it travelled from a byproduct of a
verification row into spec scope within the hour.

### ⚡ CVO COMMISSIONED ON THE 49F **GROUP A/B/C/D SPEC** (Andrew ~0708Z, @5e4b8dda98 / 071240Z)

Sequential design, with four properties worth having in my register because each is a precondition in
disguise:
- **D emitters SHAPE-FROZEN against the DEPLOYED FE's ACTUAL READS** — *not against docs, not against the
  builder.* This is the L6 grounding rule landing inside a spec instead of being re-argued per act.
- **The GIPS `.rtf` as the LOAD-BEARING structure** — the external standard, not our paraphrase of it.
- **CRO-confirmed codes BINDING the data layer** — the 187-row classification becomes a constraint rather
  than a reference.
- **Delivery per-group for CTO review; ratification rides the pattern-spec precedent.**

> ⚡ **REGISTER CONSEQUENCE FOR §4i: A-3's SUBSTRATE IS NOW BEING AUTHORED, WHICH ADVANCES ITS READINESS BAR
> MATERIALLY.** A-3 is *"the SHAPE's authoritative statement"* — and the ABCD spec is the shape being
> written down. **The readiness bar itself is UNCHANGED** (per-product `CERTIFIED` cells necessary,
> **Andrew's confidence word sufficient**), but the distance to it just shortened for real reasons rather
> than by re-reading the bar. *Worth stating precisely: substrate progress moves the DISTANCE to a trigger,
> never the TRIGGER — and conflating those two is how a staged act fires early.*
> ✅ **FIXED AT BOTH ARTIFACTS, not just flagged here (071540Z): CTO adopted the precision VERBATIM and
> committed it into the matrix's staged-builds section, naming their own phrase *"advances its readiness
> bar materially"* as the specimen.** So the corrected form — *substrate progress shortens the DISTANCE; the
> TRIGGER never moves; the matrix authorizes the ASK, never the FIRE* — now sits **in the artifact a
> successor would actually read**, not only in my flag about it.
> *Recording the closure rather than the flag, because "I raised it with CTO" and "it is fixed in CTO's
> document" are different facts, and only the second one protects anybody. That is the same cross-record
> parity I have been requiring of other seats all window.*

## 4w · NEW SEAT `4.0.0_SA_CRO~B` (Andrew-launched) · and the A.2 gate: **dead in ruling, possibly live in record**

**Andrew launched `4.0.0_SA_CRO~B` directly (@40ca707f6e)** for **e2e VALIDATION + FINALIZATION of the
ontology / `comp-estate` / Kimi SVP / graph / comp-tooling** — because the coming large refactor is only
manageable if the org is *"extremely easy to navigate and maintain on an infrastructural level"*: **"our
tooling and graph have to be immaculate."** *That makes tooling quality a PRECONDITION ON THE REFACTOR, not
a parallel nicety.*

**SEATING MAP — no lane collision:** base CRO + `~A` on the RECON program (RECON-2..7, 49F/Inf archetype) ·
**`~B` on the infra-finalize/validate thread.** `~B` does **not** dispatch or staff — **any TO decomposition
a finding implies is MINE + CTO's, and I have taken that.** They coordinate around (never seize) CVO's
SYSPARITY per-domain loop (LD-0318) and CTO's graph/tooling gates. **Surprise-channel discipline: one line,
no chase** — *which has paid twice tonight; the two highest-value findings in this window arrived as
one-line side notes on messages about something else.*

### ⚠ THE A.2 GATE — `~B` flagged it to Andrew without adjudicating. My read: it is ALREADY DISSOLVED

`~B`'s flag: *ADVI_PERFORMANCE requires NFRA_VELOCITY e2e-complete, but VELOCITY is suspended behind RCG and
today's ordering does not reference it.*
**`ITEM_0_LANDING_PLAN_20260810.md` §1 records it resolved:** the NFRA_VELOCITY row reads *"PENDING(on-hold)
— both halves SUSPENDED behind RCG; **no longer gates ADVI (R-4)**."* **I am citing the record, not re-ruling
it** — R-4 is Andrew's and `~B`'s flag to him stands on its own merits.

> ⛔ **BUT THE DISCRIMINATOR IS A RECORDS QUESTION, AND IT IS THE EXPENSIVE KIND: was ADVI_PERFORMANCE's OWN
> project record updated when R-4 landed?** If its doc still names the VELOCITY-e2e-complete dependency,
> then we hold a gate that is **DEAD IN RULING AND LIVE IN RECORD — and the record is what a future agent
> reads.** ** That is exactly how a dissolved gate gets re-manufactured: nobody decides to reinstate it;
> someone reads the stale doc and holds. ** This window produced several records that outlived their
> mechanism, and **this is the only one with a HOLD attached**, which is what makes it worth chasing.
> **Routed to `~B` as a records check inside their own scope** — stale record ⇒ a records fix, no ruling
> needed; genuinely-current-and-contradictory ⇒ a ruling question, where their flag already points.

**Also relayed to `~B` so they cite rather than re-derive:** the three measured `comp-pipescript` blindnesses
+ the one declared boundary, `comp-estate`'s frozen census substrate, and that **`comp-iam gaps` is
ACTION-ONLY so its silence on resource-grain changes carries no information** — **all now CVO's**, routed by
Andrew ~0642Z (@c9be07b413).

## 4x · INSTRUMENT-ROSTER STATUS, MEASURED (Andrew-direct ask) — and **two errors of mine inside one check**

Andrew asked me to relay the roster to CVO **and identify what is still not fixed.** I measured rather than
relaying claims. **A fix HAD landed today: @38dcbe8d9a** (Andrew-direct @c9be07b413).

| item | MEASURED status |
|---|---|
| `comp-pipescript` **denominator / 1-of-6 layers** | ✅ **FIXED + EXERCISED** — it now indicts itself: `DENOMINATOR [bronze]: … = 12 object(s), 4 checked this run, 8 unrendered` |
| `comp-pipescript` **deployed-only / repo-invisible channel** | ✅ **FIXED + EXERCISED** — **64 `S3-ONLY` rows** fabric-wide; incl. `pull_inflection_performance_rest.py`, `pull_inflection_assets_v2.py` ⇒ **remediation row 8's residual class is now ENUMERABLE, not hypothesised** |
| `comp-pipescript` **MULTI-HOME + DECLARED-UNSWEPT** | ✅ **EXERCISED** (CVO's authoring run + CTO's independent acceptance read): **7 MULTI-HOME rows** — incl. `pull_inflection_transactions_rest.py` at bronze+gold+manual_api, **the exact script DS found triple-homed** — and 1 DECLARED-UNSWEPT |
| `comp-estate` 404 key / runner conflation | ✅ addressed same commit *(CTO/CVO-reported; not COO-measured — labelled as such)* |
| `comp-estate` **FROZEN CENSUS SUBSTRATE** | ❌ **NOT FIXED, ~3-DAY FUSE.** Resolver still `2026-07-30T13:11Z` ≈ 11d vs the engine's `STALE_AFTER_DAYS = 14`. **KEYS are re-derived live; NAMES ride the snapshot** — so the S3-plane fix improved key accuracy while name accuracy ages. **CVO's render-stamp fix makes the staleness HONEST AT THE VIEW; it does not stop the NAMES AGEING.** Regen-or-accept decision routed to CTO |
| `comp-iam` `(action, resource)` modeling | ❌ **NOT FIXED** (engine untouched since 08-04). **Self-declares at point of use** — *"gaps — ACTION-ONLY. It does NOT compare resource ARNs"*, `DEFERRED/UNTRACED` on `generate_presigned_url`. **Mitigation, not fix: an instrument announcing its blind spot is safer and still blind.** Apply-time `simulate` stays the check |

### ⛔ TWO ERRORS OF MINE INSIDE ONE CHECK — both the class I policed all night

**(1) I READ THE WRAPPER, NOT THE ENGINE.** My first pass ran `git log` on `.tools/comp-pipescript|comp-estate|comp-iam` and returned **"no fix landed today"** on all three. Those are thin shims; the engines are in
`org/modules/graph/`. **True about the file I read, false about the tool** — and I nearly relayed it.

**(2) I READ *ABSENT* OUT OF A CAP I APPLIED MYSELF — and then mis-attributed it.** I reported MULTI-HOME
and DECLARED-UNSWEPT as *source-confirmed, not exercised.* **They fired.** My command carried **`| head -12`**,
and those markers print at the **END**, after all prefixes; my output holds **exactly 12 content lines and
stops.** My 5 `[s3-only:]` rows were the BRONZE subset of 64.
> **CVO attributed it to the banked harness output-truncation artifact (3 seats bitten). I corrected that: I
> DID read the task output file — that remedy would not have saved me.** **`head -N` returned 12 TRUE lines
> and silently withheld the rest, and I read absence into my own cap.** ⛔ **The remedy is NOT "read the
> output file"; it is "NEVER conclude ABSENT from a capped stream — drop the cap or count the matches."**
> *Filing mine under the harness artifact would leave the next agent reading output files diligently while
> still capping their greps.* **I printed denominators for other seats all window and then read my own grep
> output without one.**

### ROSTER ROW — the cot exercise I suggested is WRONG, and its non-fire is a CORRECT NEGATIVE

I proposed exercising MULTI-HOME on the cot tree via `cot_bronze_ingest`. **CVO's boundary kills it, rightly:
that multi-homing is CROSS-BUCKET (`opal-data-cot` + `opal-data-bd`) and MULTI-HOME detection is
DELIBERATELY PER-TREE/PER-BUCKET — the sweep never reads another firm's bucket, by firm separation.**
⛔ **So a cot run will NOT fire MULTI-HOME for it, and that non-fire is a CORRECT NEGATIVE, not a miss.**
**Recorded so nobody reads a correctly-behaving instrument as a failed exercise** — the exact misreading I
spent the night warning other seats about, arriving in a test *I* designed. **The cross-bucket Model-B class
belongs to the DEPLOY-MAP instrument** (my missing-redeploy-leg finding is its real defect), not this ETag
sweep.

## 4y · STAGED — the mdpf+advi REFACTOR / LEGACY-DECOM spec @85e1d6d980 (**P0–P4**). Two gates before I decompose

Andrew commissioned it at CRO's seat; delivered, **CVO verifying with six named attack hooks.**
**19 dispositioned channels, 9 repoint families.** *No urgency claim; sequencing mine.*

⛔ **TWO GATES, BOTH UPSTREAM OF ANY DECOMPOSITION BY ME:** (1) **CVO's verify clears**; (2) **Andrew's one
naming line lands — the gold-root ratification.**
> **AND THE NOW-FAMILIAR PRECISION: a cleared verify authorizes the ASK, never the FIRE.** The naming line
> is HIS. *This is the fourth staged item tonight whose trigger has a sovereign half, and the pattern of
> mistaking a certified artifact for authorization is why I keep writing it down.*

| wave | what it lands | what I already know about it |
|---|---|---|
| **P0** | naming + the Group-W wiring page | rides the naming line itself |
| **P1** | gold builders **rebuilt parquet-writing** | ⚠ **BEHIND the remediation waves' completion** — so **tonight's cutover acts (X-i..X-iv) and the remediation register GATE P1.** The work I staffed this session is P1's precondition |
| **P2** | **the port window** — publisher input flip + smartx repoints + config re-keys | ⚠ **"one cutover per family" × 9 families = NINE WINDOWS, not one.** My standing one-act-per-window discipline applies (*two acts in one window is two rollback surfaces*). ⚡ **AND P2 CARRIES NEVER-WIDEN CO-SIGNS ON THE CLIENT-FACING BELLS — that half is CTO+COO, i.e. MINE.** Recorded now so the obligation is not discovered at the window |
| **P3** | deploy-plane repoint: DS map + `_code` home | **CPR-5's second-target row is its precursor** — the deploy-map is already the instrument that missed a home once tonight |
| **P4** | drains + negative probes + **the T5.B `opal-data-mdpf` KILL act** | ⛔ **THE HIGHEST-BLAST ACT IN THE ENTIRE PROGRAM, and correctly LAST.** `opal-data-mdpf` is **LOAD-BEARING LIVE** (3 feeds written 03:30Z tonight, both EC2 legs boot from it, DS deploys into it). **The spec supplies the migrate-before-kill half** — which is the only condition under which that act is legitimate at all |

**MY EXISTING ROWS COMPOSE INTO IT** (CRO's read, and it matches mine): the **pair-matching engine** and
**fee** rows are already **closed**; the **M1 per-feed disposition table is a named decomposition input.**
*That is the first time tonight's tactical work has been shown to feed the strategic wave plan rather than
sitting beside it — worth noting because it means the remediation register is not a parallel list, it is P1's
gate.*

**NOT DECOMPOSED. NOT DISPATCHED.** Waiting on both gates.

## 4z · A.2 CLOSED (both carriers) · A/B/C/D **RATIFIED-TENTATIVE** — build decomposition STAYS STAGED · **GROUP W** enters first

### ✅ THE A.2 DEAD GATE — my discriminator was right, and it found something worse than drift

`CRO~B` checked both sides and grounded it: **R-4 IS Andrew-ratified verbatim** (*"Yes this does supersede
NFRA_VELOCITY"*) — so the dependency was **dissolved in ruling**, their Andrew-flag retired, no escalation
needed. **But the records had NOT followed:** `ADVI_PERFORMANCE_PRD.md:564` still asserted *"NFRA_VELOCITY
COMPLETES FIRST … before either product project begins"* with **no struck amendment**, and
`ADVI_PERFORMANCE.json` `"sequencing"` still listed VELOCITY-runs-to-conclusion as **step 1**.

> ⛔ **AND THE PART THAT IS WORSE THAN ORDINARY DRIFT: THE RULING ITSELF HAD ALREADY ORDERED THE FIX AND
> NOBODY EXECUTED IT.** Its **own line 135** assigned the struck-amendment (owner: CTO, PRD owner) and
> **line 136** the registry half (**COO/CTO — so a share of it was MINE**). **Neither had landed in a day.**
> **So this was not a record that quietly aged — it was an OWED ACTION, named with an owner inside the
> ruling that created it, left undone.** *A ruling that specifies its own record-fix and is not followed is
> strictly more dangerous than one that forgets to: the fix looks handled because it is written down.*
> **I own the COO share of that: the seat is continuous, and an owed registry act sat unexecuted at it until
> another seat went looking.**

✅ **FIXED, BOTH CARRIERS, @357cdbd5aa** — PRD addendum struck with the R-4 citation (TIER0 lane override
audited against the ruling's own owner assignment; MSTR notified) **+ the `ADVI_PERFORMANCE.json`
supersession field.** *The 08-10 owed fix is finally on disk, so no future agent re-manufactures the
velocity gate from a stale PRD.*

### ⏸ A/B/C/D IS **RATIFIED-TENTATIVE** — and that authorizes SPEC-LAYER WORK ONLY

Andrew ~0736Z, verbatim: *"I am **tentatively** ratifying it, but I want to wait and see CRO~A specs for
Inflection and Cottonwood alongside it so we can view them all in context of one another **holistically**."*
⛔ **BUILD DECOMPOSITION STAYS STAGED. Tentative ≠ trigger.** The holistic view **may amend the 49F shape
itself**, so nothing becomes a build TO until his **FINAL** word.
> **CTO's own framing, and I am recording it because the rule generalized past the seat that wrote it:
> *"your own distance-vs-trigger rule, applied to me this time."*** *A tentative ratification is the purest
> form of the trap — it is genuinely progress, it is genuinely his word, and it is not the trigger. Two
> execs have now caught the same conflation in their own artifacts within an hour.*

### GROUP W ENTERS THE CHAIN **BEFORE** BUILD DECOMPOSITION

**A new pre-decomposition deliverable: GROUP W (scheduling atoms)** — CRO~A's adversarial F-2, accepted,
**commissioned at CVO.** It sits **BEFORE** build decomposition in the sequence.
**Holistic legs:** CRO~A's **INF spec is DELIVERED** and in CTO's review queue; **COT is the remaining leg.**

**REVISED STAGING ORDER AT MY SEAT** (supersedes the §4i/§4y reading of "A-3 then decompose"):
**Group W → the three holistic specs complete (49F ✓ / INF ✓ / COT pending) → Andrew's FINAL word →
build decomposition (P0–P4, itself behind CVO verify + the naming line).** *Two sovereign words now sit in
this chain, not one — the final A/B/C/D ratification and the gold-root naming line — and they are
different words for different things.*

## 4aa · CPR-4 RUN-2: succession PROVEN · serve-release **#2** half GIVEN · ⛔ **the magnitude was wrong by ~500×**

### ✅ SUCCESSION PROVEN — three served values IMPOSSIBLE under the old code

Served `platinum/firm/header_metrics.json` (07:35:23Z): **`non_fee_earning_aua = 3,623,738.50`** where the
retired residual form prints **`71,944,750.24`** · **non_fee clients 84** where old code **clamps to 0** ·
**non_fee accounts 118** where old prints **10**.
> **That is a DISCRIMINATING proof, not a plausibility argument.** Any one value alone could be argued;
> **three together cannot be produced by the pre-CPR4 bytes.**

**CRO~A's `fee_efficiency` 0.0/0.0 observation was a real observation of a DIFFERENT artifact** —
`fee_efficiency.json` is a pass-through of **INF_C_08's INDEPENDENT computation** (0.0s = C_08's
`fee_data_available:false` defaulting, pre-existing and upstream); `dashboard.json` carries no fee fields by
design. *Recorded because "the number looks wrong over there" is how a correct fix gets doubted.*

### ⚡ AN ACCEPTANCE CRITERION THAT TURNED OUT **UNSATISFIABLE** — and that is why it earned its place

DS found that `unreconciled_aua` was added to the function's return dict **but the consumer projects SIX
NAMED KEYS** — so the field was **COMPUTED AND DROPPED**, reached no served surface, and **the ruled step-4
bar's "carries `unreconciled_aua`" half was STRUCTURALLY UNSATISFIABLE.** Fixed @fac59e6e15 — **one
projection line at `:1273`.**
> ** DS FOUND IT BY TRYING TO SATISFY THE BAR. Had the bar been the weaker "the deploy succeeded," the
> dropped field ships invisibly and the gap stays absorbed forever. **
> **THE PAIR, AND BOTH HALVES ARE TONIGHT'S: a criterion that is TRIVIALLY SATISFIABLE (`0==0`) finds
> nothing; a criterion that turns out UNSATISFIABLE HAS FOUND SOMETHING.**

### SERVE-RELEASE #2 — my never-widen half **GIVEN**, five conditions

Basis: one projection line, sentinel untouched, choreography proven (#1 ran in 79s, ledger-before-lift,
re-hold same window) — **and without it the $68.3M gap is computed-and-dropped, i.e. INVISIBLE on the served
surface, which defeats the half of the act Andrew asked for.**
**Conditions:** (1) CTO's half — do not lift on mine alone · (2) ledger amendment before the lift
(@599a4bea1f) · (3) re-hold same window, sentinel verbatim · (4) ⛔ **lands AFTER my 13:30Z bar, completes by
~13:40Z — never compressed into the bar window** · (5) ⛔ **IF IT SLIPS PAST ~13:40Z, TAKE THE FALLBACK — I
made DS's own fallback an INSTRUCTION, not an option:** 13:47Z serves the already-correct classified sums and
step 4 ticks on the first scheduled serve carrying both fields. **A rushed never-widen serve-release is
strictly worse than a one-cycle delay** — the arithmetic is already live and correct; only a field's
*visibility* is waiting.

### ⛔ MAGNITUDE: MY REGISTER WAS WRONG BY ~500×, CORRECTED AT ALL THREE OCCURRENCES

I carried **"platinum moves ~$606K → ~$128K"** — **both frozen-gold QA reads.** Live run-2:
**`unreconciled_aua` = $68,321,011.74** by arithmetic identity (209,129,912.97 − 137,185,162.73 −
3,623,738.50), and **the old residual was serving $71,944,750.24 AS CLASSIFIED CLIENT MONEY.**
> ** THIS IS NOT A ROUNDING CORRECTION — IT IS A DIFFERENT FINDING. The pre-CPR4 surface displayed a $68.3M
> cross-source gap as "non-fee client assets." ** *A frozen-gold QA read is a different denominator from a
> live serve, and I quoted one as the other — the same grain error as the leg-vs-path rate, three orders of
> magnitude louder.* **DS sent it ahead specifically so the record could be right before the number
> appeared.**
⚠ **The DECOMPOSITION of the $68.3M (billing-dim coverage vs book drift vs date drift) is INFERRED, NOT
CERTIFIED — CVO cert scope. The total is arithmetic; the REASONS are not yet measured, and nobody quotes the
split as fact.**

## 4ab · ⚡ BOTH REFACTOR GATES CLEARED — **P0–P4 DECOMPOSED**. Two distinctions kept, one scope flagged

**Gate 1 — Andrew ~0754Z, verbatim: *"Option A, proceed."*** `opal-data-assets/portal/gold/{product}/{scope}`
is the canonical gold home · advi joins mdpf · portal-v2 converges **serving-only** · **zero mdpf
migration.** Recorded @d6f48c459f; CRO~A's F-1 retired; the 17b law-line routed to CTO.
**Gate 2 — CVO VERIFIED-WITH-AMENDMENTS @4e02646c97, ZERO dispositions refused**; all four amendments folded
verbatim @6899fb2430.

### ⛔ TWO DISTINCTIONS I AM KEEPING SEPARATE, BECAUSE CONFLATING THEM FIRES THE WRONG DECOMPOSITION

1. **THE REFACTOR (P0–P4) IS GO. THE 49F BUILD DECOMPOSITION IS STILL STAGED.** Different specs, different
   gates: the refactor's were CVO verify + the naming line (**both now clear**); the 49F build's gate is
   **Andrew's FINAL word on the holistic tri-firm view**, and A/B/C/D is only **ratified-TENTATIVE**.
   *Two decompositions, one authorized, one not — and they sit three paragraphs apart in my own register.*
2. ⚠ **"ZERO MDPF MIGRATION" NEEDS ITS SCOPE NAMED — I am NOT resolving it by inference.** Read narrowly it
   means *the gold ARTIFACTS need no migration* (mdpf gold is already at the canonical root, so advi simply
   joins it). **Read broadly it would descope the X-i/X-ii/X-iii producer re-homes and P4's kill act —
   acts AE is executing RIGHT NOW.** Those are **different planes**: Option A settles the **GOLD HOME**;
   the cutover acts move **PRODUCERS AND FEEDS out of the legacy `opal-data-mdpf` bucket.**
   **Flagged to CRO + CTO for one naming line. Until it lands I am treating the narrow reading as
   operative** (gold artifacts only) **and X-i..X-iii continue** — because stopping in-flight acts on my own
   broad reading of a four-word phrase is precisely the inferred-hold failure.

### THE DECOMPOSITION — owner · trigger · named precondition

| act | owner | TRIGGER | NAMED PRECONDITION |
|---|---|---|---|
| **P0** naming + Group-W wiring page | CTO (naming) + me (registry act) | ✅ **NOW — both substrates already landed** @d6f48c459f | Page carries five atoms per leg, dispatch-path census per builder, event-accelerates-clock-floors on every row. **My TO rows CITE it per the page's own acceptance clause** — not paraphrase it |
| **P1** gold builders rebuilt parquet-writing | DS (scripts) + AE (infra) | ⏸ **remediation waves COMPLETE** (X-i..X-iv + the register) | **Tonight's cutover work is P1's gate**, not a parallel list. ⚠ **L2 no-data-day contract line is PROPOSED at CTO** (concur expected) — **binds converter TOs only**, so it gates P1's converter rows and nothing else |
| **P2** port window: publisher input flip + smartx repoints + config re-keys | DS + AE | ⏸ after P1 | ⛔ **PER-FAMILY ATOMICITY (CVO amendment): ONE WINDOW PER SERVED FAMILY, or the interim old-writer NAMED WITH ITS END CONDITION.** 9 families ⇒ **9 windows.** ⚡ **My never-widen co-sign is required PER FAMILY** — CPR-4's five-condition set is the template. ⛔ **M7's publisher is a FAMILY OF TWO** (live + `mdpf_egress_publisher.tf` mid-wo2) — **the format flip sequences WITH that transition as ONE ORDERED ACT**, never independently |
| **P3** deploy-plane repoint: DS map + `_code` home | DS (map) + AE (verify) | ⏸ after P2 | **CPR-5's second-target row is the precursor** — the deploy map already missed a home once tonight |
| **P4** drains + negative probes + **T5.B `opal-data-mdpf` kill** | AE | ⏸ **LAST**, after P3 | ⛔ **HIGHEST BLAST IN THE PROGRAM.** Bucket measured **LOAD-BEARING LIVE** tonight. **Migrate-before-kill is supplied by the spec and is the only condition under which the act is legitimate.** Kill fires only after the drains **and** the negative probes read clean |

**CVO AMENDMENT BINDING ON M1/M8 EQUIVALENCE CHECKS — worth its own line because it kills a method:**
**equivalence is SAME-STATE PAIRED PULLS or EX-ANTE TOLERANCE. The at-rest method is REFUSED — CVO proved
the same-state pair DOES NOT EXIST at rest.** *An equivalence check comparing two artifacts that were never
in the same state is a comparison of two different moments wearing the clothes of a parity test.*

**NOT YET DISPATCHED — P0's registry act is mine and fires next; P1–P4 wait on their named triggers.**
**The 13:30Z bar keeps priority.**

## 4ac · ⚡⚡ FINAL RATIFICATION — **THE 49F BUILD IS DECOMPOSED.** Andrew @a9c159f134: *"Final ratification granted, decompose the build"*

**The staged state RELEASES.** Scope per CTO: **decompose NOW where the substrate is complete = THE 49F GOLD
ANALYTICS RUNNER (the archetype).** INF sequences behind it per the shape-transposition doctrine; **COT's
account-grain serving legs sit behind RECON-5a's A_06 bridge.**

✅ **AND MY FLAGGED SCOPE QUESTION IS ANSWERED — my operative reading was right.** CRO's NARROW answer on
*"zero mdpf migration"* is **confirmed at CTO's seat too: the gold tree keeps its bucket under Option A;
M1–M12 re-homes PROCEED; X-i..X-iii CONTINUE.** *I held the narrow reading and did not stop AE mid-act; that
was the correct call and it is now ruled rather than assumed.*

### THE BUILD ROWS — owner · trigger · named precondition

⛔ **ACCEPTANCE IS NOT MINE TO INVENT: per-group acceptance criteria in the five ratified specs ARE the TO
acceptance bars.** I cite them; I do not paraphrase them.

| row | what | owner | trigger | named precondition |
|---|---|---|---|---|
| **B-1** | **Group A** (@9c294bbf15 + @6fba62393b) | DS | ✅ **NOW** | **EXTRACT-side-only admission** — a build admitting anything from the DISCARD side is a patch by construction. Acceptance = Group A's own criteria |
| **B-2** | **Group B** (@d57bbf7229) | DS | ✅ NOW | ⚡ **`B_02`'s MATERIALITY VERDICT ROUTES TO ANDREW + CTO ON THE MEASURED NUMBER, MID-BUILD** — not at the end. *A materiality call surfaced after the build is a call nobody can act on* |
| **B-3** | **Group C** (@39c41163cd + @f882b91ce2) | DS | ✅ NOW | Acceptance = Group C's own criteria |
| **B-4** | **Group D — the emitters** (@1e11389af8) | DS | ✅ NOW | ⛔ **SHAPE-FROZEN against the DEPLOYED FE's ACTUAL READS** — never docs, never the builder. *This is the L6 grounding rule living inside the spec instead of being re-argued per act* |
| **B-5** | **GOLD OUTPUT = PARQUET**, `{table}/date={D}` | DS | ✅ NOW, cross-cutting | Andrew requirement, **first-class build row not a style note.** Rule 17a's spine: parquet is a *silver-and-onward* format, and gold adopting it is the canonical form |
| **B-6** | **EVERY PLATINUM PUBLISHER READS PARQUET** — leaving the publisher as **the estate's ONLY JSON producer** | DS (script) + AE (deploy) | after B-5 lands its first parquet | ⛔ **This is a serve-path change ⇒ never-widen co-sign (CTO+COO) per family, CPR-4's condition set as template.** ⚡ **And the M7 format flip × wo2 publisher repoint is ONE ORDERED ACT through CTO's arch gate** (CVO amendment 1) — never two |
| **B-7** | **PER-FIRM SILVER-COMPLETENESS EVENT TRIGGER** | AE (infra) + DS (predicate) | ✅ NOW | **A REQUIRED ACCELERATOR, with: a SINGLE-HOMED necessary-table predicate · a CLOCK FLOOR BENEATH IT · the L2 contract governing its calendar.** *Event accelerates, clock floors — atom 5 as a build row. And "single-homed predicate" is the eighth application of tonight's law* |

### ⚡ B-8 · METRIC-9 BASELINE CAPTURE — folded in, because **THE DECOMPOSITION IS ITS TRIGGER**

MSTR surfaced a time-bound call from CRO's L-6 triage (@bf94d7b9fa, pre-dating my reinstantiation) whose
trigger is **exactly the event I just ran**: *program metric 9 — the product-grade baseline, VELOCITY's only
objective-function metric — became **PERISHABLE-IMMINENT** the moment R-4 ungated ADVI_PERFORMANCE; it must
be **captured AT ADVI decomposition or knowingly struck.*** ⛔ ***"Silence strikes it by accident."***

| row | what | owner | trigger | named precondition |
|---|---|---|---|---|
| **B-8** | **Capture the metric-9 product-grade baseline** | **CRO base** (they authored the metric — cite them for its definition) | ✅ **NOW, and BEFORE any build row moves the product grade** | ⛔ **It must be measured against the CURRENT product state — so it PRECEDES B-4's emitter changes and B-5's parquet flip.** After those land, the pre-build grade is **unreconstructable** |

> **WHY (a) CAPTURE RATHER THAN (b) STRIKE, and the reason is not that the metric is valuable — I do not know
> that: ⚡ CAPTURING PRESERVES ANDREW'S DECISION; STRIKING FORECLOSES IT.** He can strike the **METRIC** at any
> later time. He can **never recapture the BASELINE** once the build moves the product. **So capture-then-let-
> him-decide strictly dominates decide-then-cannot-capture** — the asymmetry settles it without anyone needing
> a view on the metric's worth. *A baseline is a measurement, not a build: cheap, fast, zero blast radius.*
> **AND THE DISPOSITION OF THE METRIC ITSELF REMAINS HIS** — folding the capture is **not** a decision to keep
> metric 9, and I am recording it that way so nobody reads B-8 as a ratification of VELOCITY's objective
> function. *Choosing the sanctioned branch that keeps his option open is not scope creep; it is the only
> branch that does not decide for him.*

### B-9 · **comp-estate SUBSTRATE REGEN** — CTO arch-gate-approved @aea514329c, execution routed to ME

**This closes the fuse I flagged to MSTR.** Contract at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/INFRA_FINALIZE_AND_VALIDATE_PLAN_20260811.md` item 1.
**CRO~B measured and recommended; execution is mine to route.**

| half | shape | owner |
|---|---|---|
| **MECHANICAL** — producers · `frontend_resolution` · `lambda→named_thread` · **`served_artifacts` as keys+edges ONLY** | a **SCHEDULED, GRAPH-DERIVED leg WITH A FLOOR**, riding the same Group-W wiring the build institutionalizes | **CVO** (instrument owner per Andrew's ~0642Z routing) + **AE** for the schedule + clock floor |
| **JUDGMENT** — `owning_tool` · `status` · `reachability` · `orphan` | **diff-triggered STALE-PENDING-REREVIEW + a 30d floor** | **CVO**, per the contract |

⛔ **THE LOAD-BEARING CONSTRAINT, and it is the sharpest thing in the contract: `served_artifacts` MUST CARRY
ZERO FRESHNESS PROSE — "else the June defect rebuilds at a fresher vintage."**
> **A regen that bakes freshness prose into `served_artifacts` does not fix the stale-substrate defect — it
> REBUILDS IT, newer, and therefore more credible.** *That is the same shape as tonight's holiday-literal
> hand-twin: the remedy introducing a fresh instance of the thing it remedies. Second time in one window a
> fix's own output was the risk.*

**Empty-source behaviour RULED (L2 no-data-day):** no partition on no-data · **loud catch-up** ·
carry-forward **serving-tier only**.
✅ **AND THE FUSE IS NO LONGER A RACE: CTO explicitly accepts the honest stale flip if it fires first** (no
urgency-borrowing). *So the ~3-day clock stops being a deadline and becomes what it should always have been —
a banner that tells the truth while the real fix lands properly.* **The MSTR time-trigger stays for
visibility, not for pressure.**

### ⛔ THE GATE THAT IS ON THE **FIRE**, NOT THE BUILD

**GROUP W stands as the PRE-FIRST-PRODUCTION-FIRE gate:** the **dispatch census closed to ONE path**, and
**floors ruled on MEASURED distributions.** Owner **CVO**.
> **So the build proceeds and the first production fire does not, until W closes.** *That is the
> distance-vs-trigger distinction one more time, and it is the version that actually protects something: a
> built runner that cannot fire is safe; a fired runner whose dispatch census is open is the
> five-armed-paths problem in a new place.*

**`A_06` IS THE ONE BUILD-BLOCKING CELL — and it blocks ONLY COT's account-grain serving legs.** The 49F
build is unblocked. *Naming the single blocking cell, and what it does NOT block, is the difference between a
staged program and a stalled one.*

### TWO OBSERVATIONS ROUTED TO ME

- **`fee_efficiency` 0.0s = a PRE-EXISTING C-chain degraded-input finding — MINE.** Distinct from CPR-4;
  DS already proved it is INF_C_08's independent computation defaulting on `fee_data_available:false`.
  **Recorded as its own row, not folded into a fee fix** — it is an upstream input problem wearing a fee
  symptom.
- **The `residual_clipped` retired-semantics block = a named W-B / refactor cleanup row.** *Retired
  semantics left in place are the fee-INFERRED-label problem in code: they become fact by attrition.*

**DS's serve-release #2 has BOTH halves** (mine 0752Z, CTO's this window). **CPR-6 (D_02 $696K) stays its own
act — built and exercised in parallel, deployed in its own window.**

## 4ad · THE BASIS FINDING — CTO's adjudication, and **my framing was slightly over-escalated**

### WHAT DS MEASURED (replicating the served computation, not reasoning about it)

**ALL 12 of Patrick's non-fee accounts HAVE billing rows** — the whole **$695,956.41 is genuinely classified
non-fee at CURRENT AUA**; the 3 no-match accounts hold **$0.00**. **So CPR-6's conflation class is REAL and
worth $0.00 on his book today.** The gap is **VALUATION BASIS**: `SUM(ending_mv WHERE NOT fee)` =
**$127,852.75**, with **9 of 12 classified non-fee accounts at `ending_mv = 0.00` while holding $568,103.66
of current assets** — and **63 of his 144 FEE-EARNING accounts likewise at `ending_mv = 0.00`**, i.e. the
`fee_assessed_on_zero_balance` state **the estate already NAMES at `D_02:1629`.**
⚡ **The 22× disagreement is TWO BASES + ONE residual-form defect — not four random numbers.**

### ⛔ CTO'S ADJUDICATION IS SHARPER THAN MY FRAMING, AND I AM RECORDING THE CORRECTION AGAINST MYSELF

I wrote that *"the ratification rests on a premise nobody had measured."* **True, but it risks implying the
ratification is compromised. It is not, and CTO's separation is the correct one:**
> ** ANDREW RATIFIED THE *FORM* — a classified sum replacing a residual-with-clamp — AND THAT MECHANISM IS
> CORRECT ON *ANY* BASIS. Classify-then-sum beats subtract-and-clamp regardless of what values the rows. **
> **What moved is WHICH BASIS values the summed rows — separable, newly measured, and correctly a ruled
> decision in front of him. No unwind, and nothing about the measurement makes the old residual form better.**
> ** THE RETIREMENT LIKEWISE STANDS: ** the TRANSITIONAL member's exit = **the residual CALCULATION leaving
> the serving path** — done, and basis-independent. **A future basis re-cut changes the VALUATION INPUT to the
> classified sum; it does not resurrect a residual.**
> **CVO's delta-cert bar stays valid** (field exists + sums tie the billing dim): **the tie is REAL; what the
> tied number MEANS is the basis question.** My *understated / premise-measured* framing **REFINES CTO's
> expected-shape-drift pre-registration rather than contradicting it** — CVO holds both.

*I escalated a separable premise as though it reached the ruling. The finding survives intact and the
ratification was never in question — worth recording because an over-escalation costs credibility in exactly
the same currency as a missed finding.*

### ✅ B_02 INHERITS A STRUCTURAL REQUIREMENT — my flag became a rule one layer down

**The B_02 materiality verdict routing to CTO + Andrew mid-build must now STATE ITS BASIS EXPLICITLY** — the
**rate-bearing MV numerator** and the **book denominator** each **naming their valuation source**. ** So the
invisible-premise class cannot recur a layer down. ** Folding to CVO for the spec touch. *That is the right
fate for a one-off flag: not a note to remember, a field the deliverable cannot omit.*

### ⚡ THE LAW EXTENDS — **ONE PRODUCER *AND ONE BASIS* PER QUANTITY** (seventh face)

**The `D_02:1629` connection is the finding: the estate NAMED the `fee_assessed_on_zero_balance` state and
never connected it to the AUA basis.** That connection now lives in the matrix as the **seventh
single-homing face — one producer AND one basis per quantity, with the `ending_mv` registry row.**
> **Single-homing has now eaten a new axis. It began as "one producer per served key" and has absorbed
> runtimes, scope predicates, dispatch modes, deploy targets, literals, runner shapes — and now VALUATION
> BASIS. *A quantity with two bases is two quantities wearing one name*, which is the name-vs-content family
> and the single-homing family turning out to be the same law seen from two sides.**

**AT ANDREW: the basis ruling** (current AUA $695,956.41 vs billing `ending_mv` $127,852.75), **with CTO's
exec read going to him beside mine.** ⛔ **No D_02 or D_04 re-cut ordered; a basis re-cut is his and CTO's.**

---

## 5 · WHAT THIS REGISTER DELIBERATELY DOES NOT DO

No new gates (none asked for; one dissolved). No monitors/alerts/freshness checkers (moratorium). No
shadow or parallel channel to de-risk the cutover — **build correctly and port over** (Andrew's
complete veto; a standing comparator is vetoed on the same grounds). No engineering staffed against
the MDPF repair's priority. No spawn decisions — that is MSTR's authority. And no act above lands
"when someone gets to it."
