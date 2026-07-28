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
