# MDPF RESET DIRECTIVE — 2026-07-28T2220Z — THE ONLY LIVE TASKING

**Authority:** Andrew-direct ~2157Z (verbatim @`5256829864`) + Andrew fabric reset ~2218Z:
> *"I closed out all the subagents because I think we need to reset the fabric with clean directives
> because too much information is floating around and we're firing from the hip rather than operating
> on a directed basis."*

**Issuer:** `1.0.0_SA_CTO`.

## ⛔ SUPERSESSION — read this first
**This file supersedes EVERY inbox message, dispatch, GO, and transfer timestamped before
2026-07-28T22:20Z.** A successor session waking under any worker serial will find stale traffic in its
inbox (including a chain-fire order, a publisher dispatch, an ownership transfer, and a revocation — all
sent to sessions that were already closing). **Drain the inbox, act on NOTHING in it. This file is the
tasking.** Latest + most-restrictive binds; this is latest.

**State of record at reset:** nothing in flight, nothing half-landed by tonight's sessions — Stage-6
grant, R14 fence, egress principal, CODE_TREES + router fixes all APPLIED/VERIFIED/ledger-CLOSED. The
chain was NOT re-fired. The publisher was NOT built. *(Residual: `~C` surfaced 3 OTHER agents' open
deploy ledgers, oldest 98.6h, one malformed — WO-0 for the COO, below.)*

---

## THE MISSION (Andrew, verbatim ~2157Z — this is the whole of it)
> *"First, I need MDPF completely done end to end… all production of mdpf artifacts from the
> opal-data-assets bronze and silver layers need to be condensed in
> opal-data-assets/portal/gold/mdpf/{"firm" or "global"}/… validated immediately. Second… validate that
> the publisher lambda that writes those assets to the opal-data-portal-v2 bucket is functional and on
> schedule. Third, we need to run it right now and make sure that we have maximally updated data for
> every single channel."*

**Standing test for every action: does it advance WO-1, WO-2, or WO-3? If not, it does not happen.**

---

## ⚡⚡ AMENDMENT 2 — THE DONE DEFINITION (Andrew ~2230Z, verbatim) + THE COMPLETE WO SET

> *"We are not done here until the entire pipeline is locked in completely and you can tell me for a
> FACT that we have complete data in gold for all cohorts, that all pipelines are operating correctly
> on a day over day basis, that all related publishers are emitting what they are supposed to, to the
> correct location in the pipeline as we are designing it, and that the portal reader and publisher is
> executed as we've described here in the /platinum format."*

**FOUR DONE CONDITIONS — nothing closes until all four are independently certified:**
```
D1  COMPLETE DATA IN GOLD, ALL COHORTS   32/32 rows fresh-or-declared per cadence; zero false zeros;
                                         backfill landed; cohort ingestion paths traced (COO, in flight)
D2  DAY-OVER-DAY OPERATION               every stage fires from its OWN schedule, proven by an
                                         UNATTENDED fire — a hand-run never counts (chain 15:00Z,
                                         emitter 17:15Z, publisher ~16:15Z)
D3  PUBLISHERS → CORRECT LOCATIONS       written set ≡ canonical design set, both directions, per §III-g
D4  /platinum FORMAT END-TO-END          publisher writes platinum/mdpf/{scope}/{type}.json AND the
                                         portal READS it (WO-3 complete)
```
**CERTIFIER: `3.0.0_SA_CVO` (live, idle, independent).** When WO-owners report done, CVO runs the
end-to-end verification against D1–D4 and certifies — or refuses. **"For a FACT" = CVO's independent
verdict on live state, never an executor's self-report.** (Verification law: the verifier is not the
do-er.)

**THE COMPLETE WO SET** *(4a/1/4b/2/3 unchanged below; 5–7 new, from COO's 2218Z gap list)*:
| WO | what | owner | state |
|---|---|---|---|
| 4a | emitter fix (stale-source selection + false zero) | AE (pid 26488) | IN FLIGHT |
| 1 | chain fire + gold validation **+ COTTONWOOD CONDITIONAL** (below) | AE | IN FLIGHT |
| 4b | DDB backfill from historical inputs | AE | gated: 4a+1 |
| 2 | publisher re-point + own schedule + first publish | AE | gated: 4+1 |
| 5 | **PER-CHANNEL SCHEDULE CENSUS** — every channel: trigger mechanism, ScheduleExpression, applied-plane verified, UNKNOWN declared where unknown. Mandate part 1, never completed. | COO (subagent fleet) | NEW |
| 6 | cohort ingestion-path tracing, 27 remaining | COO (in flight ~20 min) | IN FLIGHT |
| 7 | **UNATTENDED-FIRE LEDGER + CVO CERTIFICATION** of D1–D4 | CVO | gated: all above |
| 3 | portal re-point to /platinum | COO seq → DE/DT | gated: WO-2 |

**THE COTTONWOOD CONDITIONAL (WO-1, explicit):** the known cause of the silver→gold gap is the `:523`
IAM short-circuit, fixed 20:26Z with **zero runs since** — WO-1's fire is the test. **If cottonwood
gold does NOT advance to its silver frontier after the run, the IAM fix was NOT the whole cause: STOP,
report it as a NEW untraced defect, do not iterate blind re-runs.** Andrew: *"We need to look into the
Cottonwood chain and figure out what is going on with that"* — one run answers it one way or the other.

## ⚡ AMENDMENT 1 — ANDREW RE-SEQUENCING, ~2225Z (supersedes the WO order below where they conflict)

Andrew, going element-by-element down the chain status: **(4) "Have we fixed the emitter and backfilled
properly? That is the first thing to do here."** · **(6)** the publisher is fixed **after** 4 is
rectified · **(7)** cottonwood's absence from platinum is rectified **by moving to the /platinum
structure already rendered canonical** — i.e. by WO-2 publishing the canonical gold tree (which HAS
cottonwood), never by enrolling cottonwood into the legacy producer. Cohort mapping (1) is COO's, in
flight via its subagents.

**EXECUTION ORDER, revised:**
```
WO-4a  EMITTER FIX (new, FIRST)      ┐ parallel — code work vs chain runtime
WO-1   CHAIN FIRE + gold validation  ┘
WO-4b  DDB BACKFILL (after 4a lands and WO-1 gives fresh inputs)
WO-2   PUBLISHER (unchanged content; now gated behind WO-4 + WO-1)
WO-3   CONSUMER RE-POINT (unchanged; gated behind WO-2)
```

### WO-4 — EMITTER FIX + PROPER BACKFILL  *(owner: fresh `0.7.0_AE_CloudOps`; FIRST)*
**The defect, located tonight (mechanism measured, per-cohort logic still unread):**
`opal-assets-daily-emitter` (17:15Z cron → `opal-assets-daily-aua`) wrote `as_of 2026-07-06`
`rolled_forward` for the four 49F ETF cohorts (~$522mm) **while its own input**
(`platinum/mdpf/aggregate_aua/2026-07-28.json`) **carried `partner_held_etf: {49financial: 2026-07-28}`
with current values** — self-declared via the row's own `source_field`, which names
`opal-data-etfs/daily/49financial/2026-07-06.json`. **The data was collected; the emitter selected a
stale source.** Discriminator: the SAME input array yields FRESH for inflection
(`attribution_basis: rps_actual:49financial; target_weight:inflection`).
**Second defect, same component:** `_total__partner_aua` emits **value 0 with a current `as_of`** when
100% of its additive constituents are missing — a false zero, worse than a declared hole.

**DO (4a):** read the per-cohort logic; fix why the 49F-ETF path prefers `opal-data-etfs/daily/` over
the fresh `partner_held_etf` in its input (or fix that source's selection); make the zero-constituent
total emit ABSENT with a reason, never 0. **Sovereign note:** Andrew's direct order IS the authorization
to touch this component — the R1 legacy-hands-off posture yields to it here, for the emitter only,
attributed in the commit.
**DO (4b), after 4a + WO-1:** backfill the DDB rows the defect corrupted — the four ETF cohorts from
07-06 forward (inputs exist: the 434-object date-keyed accrual series), the false-zero totals, and the
07-23/24 hole where no rows landed at all. **Backfill = re-emit from the historical inputs, never
hand-written values.** Verify per §III-g: sets both directions, per-row `vintage_state` read, not row
presence.

---

## WO-1 — GOLD CONSOLIDATION: RUN + VALIDATE  *(owner: fresh `0.7.0_AE_CloudOps`)*

**State (grounded 2157Z, applied plane):** `portal/gold/mdpf/` produces daily — 11 objects, 4 scopes,
all written 15:49Z today. Vintages: 49f 07-27/28 · inflection 07-27 · global 07-27/28 ·
**cottonwood 07-20/07-22** (stale for a KNOWN, FIXED cause: the emitters were IAM-blocked at dispatch
`:523` until the Stage-6 grant landed 20:26Z; the 15:49Z run predates it).

**DO:**
1. Fire the mdpf chain once, now. **Andrew's explicit word IS the ad-hoc carve-out.** This run doubles
   as the Stage-6 grant's acceptance: `:523` passes → `:524`/`:525` execute → cottonwood lands under
   `gold/mdpf_revamp/cottonwood/` → Stage 6 rc=0 → `cycle-complete.json` emitted (first time ever).
2. After completion, report the **per-(scope,type) vintage table of `portal/gold/mdpf/**`** — the set,
   not a count. Any scope/type still stale → named, with cause.
3. Rule on the type asymmetry (aum-metrics/account-units cottonwood-only; non-model-assets global-only):
   **DECLARED or DRIFT** — read the accrual script's declared type sets; do not adjudicate from a listing.

**DO NOT:** deploy the two repo-side cottonwood scripts (976-line generation gap, coupled to DS's held
read-preference — neither moves alone) · touch `mdpf_aggregate_aua.py` (legacy stays untouched) · build
any alarm/monitor/freshness-checker (moratorium).

## WO-2 — PUBLISHER: FUNCTIONAL + SCHEDULED + RUN  *(owner: same fresh `0.7.0_AE_CloudOps`; serialize behind WO-1's fire)*

**State (grounded 2157Z):** `opal-assets-mdpf-portal-publisher` fails both halves — reads
`STAGING_ROOT=gold/mdpf_revamp` (pre-canonical), runs the FENCED role (explicit-denied from portal-v2),
**zero EventBridge rules target it**. The fix's IAM is DONE: egress role `a11b8e2cc3`
(read `portal/gold/mdpf/*`, write `platinum/mdpf/*`, on no fence, battery 8/8), live-serve grant staged
at `count = 0`.

**DO:**
1. Re-point BOTH legs: read `portal/gold/mdpf/{scope}/{type}/{date}.json`, latest per (scope,type),
   **types DERIVED per scope, never hand-listed**; write
   `opal-data-portal-v2/platinum/mdpf/{scope}/{type}.json` (locked layout, hyphens).
2. Swap the function to the egress role. The old fenced role ends attached to nothing.
3. Flip `var.mdpf_egress_live_serve_write_cosigned` = true. **Paper complete:** Andrew 2157Z (sovereign)
   + CTO (on record) + **COO co-sign 221211Z, SCOPED: `platinum/mdpf/*` ONLY — a policy that reaches
   `json/mdpf/*` is UNSIGNED and is a STOP.**
4. Give it its OWN `ScheduleExpression` (~16:15Z daily; state the reasoning). `cycle-complete.json` may
   be an accelerator later; it is never the gate (it has never been emitted — a publisher gated on it is
   born dead).
5. Provenance stamp per object (`written_by, written_at, source_keys[], source_vintages{}`) if cheap;
   else first follow-up. Say which.
6. TF only · commit-before-apply · targeted (`mdpf-pipeline` row 10 must not ride) · deploy ledger
   open→closed in-session · NEVER#6.
7. **INVOKE once, only after WO-1's chain completes** (else cottonwood publishes stale). Verify: written
   set ≡ gold-tree (scope,type) set **both directions**, ETag/size/vintage per object, old `json/*`
   Denies unmoved.

**⚠ THE OPEN ITEM NO CLEAN RUN CLOSES (COO, binding):** *an ad-hoc run proves the DATA FLOWS; it cannot
prove the SCHEDULE WORKS.* "On schedule" closes ONLY on the first **unattended** `ScheduleExpression`
fire (expected tomorrow ~16:15Z). Log it as open; a publisher only ever run by hand is never reported
as scheduled.

## WO-3 — CONSUMER RE-POINT  *(owner: COO sequences; DE builds; DT promotes — GATED behind WO-2's first verified publish)*
The portal reads `json/mdpf/*`; the publisher writes `platinum/mdpf/*` — so WO-2's first run cannot
change what a client sees (that is the safety property, per COO). "Every single channel" reaches clients
only here. Decompose against DT's derived 23-key/6-namespace union @`ef18a5fac` — **the DERIVATION +
its 401-gating residual, never the count** — reconciled against PRD §17.2 (G9, CTO) first.
**Not tonight unless Andrew says.**

## WO-0 — LEDGER HYGIENE  *(owner: `2.0.0_SA_COO`, live now)*
Disposition the 3 open deploy ledgers `~C` surfaced (oldest 98.6h, one malformed). An unclosed ledger at
session end is COO-alarm material by rule; these predate tonight.

---

## STANDING CONSTRAINTS (unchanged, carried so successors need no archaeology)
Legacy runs untouched; both `json/*` explicitDenys STAY; teardown is the LAST cutover step ·
No serve-side hand-fixes, ever (a producer clobbers them) · Roster (`partner_roster.json`) is the one
authority; every divergence resolves TOWARD it · No alarms/monitors/freshness-checkers (moratorium) ·
`data/analysis/` archive PARKED · Everything not named in a WO is BELOW the line.
