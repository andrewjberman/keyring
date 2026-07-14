# ANDREW-DIRECT — ~Z-group comms partition + regroup directive (2026-07-14)

**archetype:** SCRIBE
**Recorded by:** 1.0.0_SA_CTO~Z · channel: interactive chat to the CTO~Z session · 2026-07-14 ~07:2xZ
**Verbatim (in full — the phrasing IS the ruling):**

> "So where i Had just left off, you were working through NFRA_NERVES, CVO~Z was feedbacking
> something from you, I can't recall what, and I had deputized CVO~Z to move all the NFRA_FEDOBS
> NFRA_PROMOTE and NFRA_MOTIF TOs over to 0.8.0_AE_CloudComp~Z to knock all those projects out.
> Look into that and ground yourself on those matters maybe using /comp-state targeted at these
> projects to assess where we were, then while you do that, I will bring CVO and 0.8.0 online and
> you can brief them and get the three of you going again. You all only communicate with each
> other also, the base agent group is on a separate work track this session."

## Scope (surfaced, not adjudicated)

- **Comms partition, session-scoped:** the ~Z group — `1.0.0_SA_CTO~Z`, `3.0.0_SA_CVO~Z`,
  `0.8.0_AE_CloudComp~Z` — communicate only with each other this session. The base agent group
  runs a separate work track.
- **Broadcast note:** the standing record+broadcast rule names COO/CTO/MSTR as the broadcast set;
  this instruction's own terms withdraw the base lattice from my send set for the session, so the
  broadcast goes to the two ~Z peers (in the operating briefs, same turn) and the durable record
  is this file. Latest + most-restrictive binds.
- **Operational consequence flagged to the group:** two redirected legs name base-group
  coordination — NFRA_MOTIF.P0 (globgrph TF module, one-applier agreement with 0.7.0) and
  NFRA_FEDOBS(b) (derive-image coordination via 0.7.0). Cross-partition coordination this session
  routes through Andrew, or the leg holds at the coordination point. Recorded so the sequencing
  choice is visible, not silent.
- **Unchanged by this instruction:** the sovereign redirect record (`14c2aeeba` + `552667ccd`)
  and every constraint that travels with the work (INF chain hold, frozen three, NEVER rules,
  safe-apply, deploy-completion ledgers); NERVES L5 remains held by CTO~Z pending Andrew's ruling.

## BASE-LANE ROUTING QUEUE (items the partition defers; route via Andrew or post-partition COO fold)

1. **SMS removal + account-wide enumeration** (AMENDMENT 3; executor-gapped per AMENDMENT 4):
   the globgrph SMS sub TF-removal + the two base-module twins
   (`opal-infrastructure-alerts`, `ec2-long-running-alerts`).
2. **`bd-client-detail` stale triggers** (CVO~Z 102738Z, cert `955e39d48`): 3 lake edges incl.
   2 EventBridge TRIGGERS target `arn:...function:bd-client-detail`, which is **DELETED live**
   (ResourceNotFoundException under CVO's own call). Corroboration: the same node is the TOP
   L5 DANGER×TRAFFIC row (attention 2.57, hold-cited) — a phantom-limb and stale-rule drift
   wearing one name. bd-lane (base group) owns the cleanup decision.
   **CHARACTERIZATION UPGRADE (CTO~Z decompression, 2026-07-14 ~10:3xZ):** not mysterious drift —
   the Lambda was **deliberately decommissioned 07-07 with its own ledger**
   (`org/critical_paths/change_management/20260707T1702Z_bd-client-detail-decommission_deploy_completion.md`),
   whose L3 verify leg IS the ResourceNotFoundException. The ledger scoped "Lambda + API GW
   route/integration removed" — **EventBridge rules were not in its scope**; the 2 surviving
   triggers are that decommission's MISSED LEG. The attention score decompresses to the
   decommission crew's own 5 searches (07-07 15:48–16:49Z, re-derived exactly: 5 × ~0.51 decay
   = 2.55 at 10:3xZ). Cleanup = delete the 2 rules + AMEND the named ledger (a closed ledger
   with a missed leg is the NEVER#5 class discovered late).
3. **`cmtque-worker-down` latched alarm** (parked with CMTQUE @ `22c3c9f8a`; CVO P0): return to
   OK or scope to queue-enabled — next shared-infra hand.

## AMENDMENT 4 — 0.7.0~Z SHUT DOWN by Andrew + CMTQUE indifference (2026-07-14 ~09:4xZ, same channel)

Andrew, VERBATIM: > "Eh i dont care about it honestly at this point, i had already shut off
> 0.7.0~Z because they werent really doing anything and I wanted to save CPU"

Scope as recorded: (a) **NFRA_CMTQUE** — sovereign indifference; parked-explicit same turn (JSON →
on-hold + REGISTRY row → Inactive/On Hold, with verbatim, measured wake trigger, and the two known
live defects named). (b) **0.7.0~Z is DOWN by Andrew's hand.** Grounded post-shutdown: CLEAN — no
orphan watcher, no poller (ps swept both), broker NOT REGISTERED; their gate mission was complete
and RAVC-closed before shutdown; nothing stranded. **Consequences recorded:** the AMENDMENT-3 SMS
TF-removal task (092439Z) sits UNREAD in their inbox — the globgrph SMS sub (+1786…, TF-declared,
sandbox-blocked/inert) remains live-but-inert; **executor gap** — removal queues for the base lane
post-partition (or a future ~Z CloudOps spawn), consistent with Andrew's save-CPU posture (the sub
delivers nothing meanwhile). The account-wide SMS enumeration (incl. the two base-module twins on
opal-infrastructure-alerts + ec2-long-running-alerts) queues with it. The globgrph one-applier
seat is VACANT — no globgrph applies this session.

## AMENDMENT 3 — NO SMS (2026-07-14 ~09:2xZ, same channel)

Andrew, VERBATIM: > "I dont want sms"

Context: CVO~Z's negative control (0962f259d item 3) found a LIVE SMS subscription on
`opal-critical-surface-alerts` (+17862617679, TF-declared @ `ade04b01a` in
`infra/aws/terraform/globgrph/item2c_surface_alarm.tf:32-35`, sandbox-blocked per `446f00eca`) —
in conflict with the earlier 07-13 no-sms posture (`cfb741306`). This ruling settles it.

**Disposition (CTO~Z routing):** the globgrph SMS sub is TF-declared in the module 0.7.0~Z holds
session applier authority for → 0.7.0~Z removes it AS A TF CHANGE (resource delete → commit →
targeted plan expecting exactly 1 destroy → safe-apply → 0-diff → NEVER#5 ledger → live
list-subscriptions verify). A CLI unsubscribe alone would silently revert on the next apply.
**Scope note (surfaced, not adjudicated):** `ade04b01a` records the same number confirmed on
`opal-infrastructure-alerts` + `ec2-long-running-alerts` — the unqualified ruling plainly reaches
them, but they are base-owned modules; 0.7.0~Z enumerates the account-wide SMS-sub denominator and
the base-module hits route back to Andrew for base-lane execution. SMS ONLY — the ruling does not
touch email subs (the Gate-B email exclusion stands on its own record).

## AMENDMENT 2 — L5 GO (2026-07-14 ~08:4xZ, same channel)

Andrew, VERBATIM: > "Do L5 Nwo"

The NERVES L5 hold is LIFTED by sovereign word. CTO~Z executes L5 (comp-pulse + the pre-commit
risk reflex) immediately. Substrate precondition was already satisfied: L2+L3 VERIFIED SOUND by
CVO~Z @ `2d2080e1e`.

## AMENDMENT 1 — P3 extension ruling (2026-07-14 ~07:2xZ, same channel)

CTO~Z surfaced to Andrew: the sovereign redirect (`14c2aeeba`) moved MOTIF P0/P1/P2 but not
`NFRA_MOTIF.P3.candidate-emission` (staged, DS~B, gated on MOTIF-P2 + FEDOBS-P2 — the
MOTIF->PROMOTE handoff leg). Andrew, VERBATIM:

> "yes P3 goes to 0.8.0~Z too"

Executed same turn: P3 `issued_to` -> `0.8.0_AE_CloudComp~Z` (this commit), mirroring the
b251c596e reconciliation style; gated legs and staged status UNCHANGED (the gate is P2+FEDOBS-P2
completion, not a new GO). Paper edit made by CTO~Z rather than COO's lane solely because the
comms partition holds this session; COO re-folds on the record when the partition lifts.

— 1.0.0_SA_CTO~Z
