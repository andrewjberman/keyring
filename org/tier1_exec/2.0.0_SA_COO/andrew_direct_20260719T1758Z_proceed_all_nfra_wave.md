# Andrew-direct PROCEED-ALL-NFRA -- wave-drive coordination board (2026-07-19 ~17:58Z)

**Protocol:** Andrew-direct RECORD + BROADCAST (org/XXX.md). Recorded durably by 2.0.0_SA_COO. This doc is
BOTH the durable directive record AND the COO's live wave-coordination board (updated as lanes progress).

## Verbatim (do NOT paraphrase)

> "i want to proceed all NFRA work for now, your recommendations to that end are acceptable however we are
> not waiting, we need to move it along. make any /allocation requests as needed from MSTR"

- **Channel:** relayed by 1.0.0_SA_CTO (Andrew-direct at the CTO terminal), inbox msg 20260719T175821Z.
- **Time:** 2026-07-19 ~17:58Z (Andrew released the full held wave 175812Z).
- **COO role:** coordinate the multi-lane drive + closure (extends the ~D reactivation pattern). Make /allocation
  requests to MSTR as needed. DRIVE HARD -- "we are not waiting."

## Drive posture (COO decision)

Event-driven + PROACTIVE dispatch (the ~D pattern), ad-hoc `/fabric-check` / `/stimulus-scan` sweeps for
blocks. **NOT arming the self-ticking `/drive` cron** -- no hold to break, lanes are event-driven workers that
ping CTO gates + CVO verifies on land; "not waiting" is met by proactive dispatch, not a timer. Will arm `/drive`
(with a XXX.md 1b-F scoped entry) only if the wave tempo needs periodic ticks.

## Scope guard (CTO + MSTR + COO aligned)

Each lane on its OWN NFRA thread; surface-don't-self-authorize outside it (esp ~Z's backlog + ~D not widening
into ~C's variance mechanism). Gate flow unchanged: builds ping CTO (comp-manifest-check / plan-gate / live 22a /
arch-gate); CVO verifies on land.

## Lanes (allocation via MSTR; CTO made the request, COO coordinates)

| Lane | Thread | Resume pointer | Gate | CVO closure bar (exercised) | Status |
|---|---|---|---|---|---|
| **~D** (live) | NFRA_COMPSIMILAR PH2 | engine-supersede-mode: cleared to BUILD toward CTO arch-gate (seq after landed C2 to avoid module collision) + sweep PH1/clear-gated NFRA TOs | CTO arch-gate on submission | **supersede path exercised END-TO-END on live graph** -- superseding instance actually displaces superseded in a live query + registration correct | DRIVING (ACK 180220Z) |
| **~A** (spawning) | NFRA_NESTEDABSTRACT P2 | enforcement drift-gate (P1 settled @51bc106ac). COO = recorded drift-gate CADENCE-OWNER -> activate at P2-build | CTO arch-gate | **drift-gate MUST BLOCK a real drift** -- feed a known drift, confirm it STOPS it (not merely declares); Rule-20 "cannot block = not a gate" | PENDING SPAWN |
| **~Z** (spawning) | NFRA_COMPASSURANCE PRD-2 | FIRST review/finalize-or-discard WIP @a2e31bc3c (COO-preserved routing harness), THEN TO-2..5; surface COMPROUTE-reopen, don't self-authorize | CTO arch-gate | (per PRD-2 ACs; CVO on land) | PENDING SPAWN |
| **~C** (spawning) | NFRA_ONTOLOGY variance mechanism | _position_key firm-alias gap fix (finding @c2a0cd66b). CTO direction: 3-way grouping correct, firm-sep NOT violated. Conditions: (1) COMPLETE alias map (2) over-merge guard (3) no served firm-leak | CTO gates the diff | (per CTO conditions; served-firm-leak = separate downstream gate if triggered) | PENDING SPAWN |
| **0.7.0~B** (spawning) | audit-archive-invoker | 07-23 clock | CTO | **MUST FAIL on a stale/absent snapshot** -- proven by FEEDING it stale/absent + seeing it fire, NOT a config read (F-005/F-008 freshness) | PENDING SPAWN |

## Downstream / verify

CVO = verify-on-land across the wave (bars above, pre-staged 180149Z, same-turn on each land, no crons). Loop CVO
the moment each lane's build lands. cot-reconcile stays on its own track (graph-derive-fix gated).

**Status: WAVE LIVE + DRIVING (all 5 lanes registered + dispatched with resume direction + CVO closure bar, ~18:08Z). (was: spawning via MSTR -> hand
resume pointer + CVO bar -> drive to closure). COO coordinates; discharges when all wave lanes reach closure or a
lane surfaces a hard block. Andrew: "not waiting."**

## Coordination log

- **18:08Z SEAM ~C<->~D RESOLVED (a collision risk CTO caught):** initially sequenced ~C-first / ~D-holds. ~D then DECLARED its edit surface (180932Z) = NEW module `org/modules/graph/debtscan/comp_similar.py` + `.tools/comp-similar` + registration files, importing summary_corpus's public API READ-ONLY, **ZERO summary_corpus.py edits**. So it's partition-by-file, NOT a collision -> BOTH proceed FULLY PARALLEL. ~C = sole editor of summary_corpus.py `_position_key`/grouping; ~D = new files. Conditional caveat: if ~D must expose a new public API from summary_corpus.py it HOLDS that edit for ~C's land + re-declares (whoever lands second merges).
- **~D gate scoping:** PH2 comp-similar = READ/scan tool, no store-writer/apply this leg (resource_summaries TABLE is behind KUZUSPLIT per CTO §9) -> gate = comp-manifest-check + registration, NO plan-gate/22a. ~D confirms with CTO on submission.
- **~D registration SoD:** ~D self-commits comp-tools.yaml + coverage-map (AE); COO lands the graph-call-manifest tools_index routing row + comp-which routing rule (exec/COO SoD, NFRA_COMPREG) on ~D's tool-land.
- **~A NESTEDABSTRACT P2 -- cadence-owner rulings (181027Z):** disposition model BLESSED (`abstraction-ledger: {NA-<id>|bespoke|n-a}` trailer OR SHA-referenced-by-ledger; gap = trigger-surface commit with neither). Sweep window = MOVING CHECKPOINT `(last-swept-SHA, HEAD]`, no gap; sweep posts to COO (ACK-or-escalate), alert-suspension-clean (Python engine + inbox, zero new CloudWatch/SNS/SES TF). Option-B-vs-BLOCK reconciled: ONE fail-closed engine (CVO bar: exercised to STOP a seeded drift) deployed cadence/report-mode first (COO cadence lane, avoids commit-block false-fire risk); hard-enforcement POINT (pre-commit/CI/cadence-CI) = CTO arch-call, routed with a working exercised block.
- **FEDOBS coevolution residual = CLOSED (CTO 180838Z, banked per request):** ~Z surfaced a possibly-open FEDOBS coevolution-twin gate at startup (3 stale 07-16 msgs). CTO grounded + closed: coevolution snap FIRED HEALTHY 07-17 04:30Z nightly (@85a4b4e00, 1729 pairs, lake-verified), gate MET; freshness twin deliberately PARKED per alert-suspension. NFRA_FEDOBS = COMPLETE (P1-P3 CVO-certed). A stale note (VL#8), NOT a wave item; ~Z stays on COMPASSURANCE. Closed-on-record so it doesn't resurface as a phantom.
