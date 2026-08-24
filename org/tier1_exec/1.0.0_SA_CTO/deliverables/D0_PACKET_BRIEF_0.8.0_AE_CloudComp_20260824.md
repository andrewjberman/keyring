# D0 PACKET BRIEF -- the spawn brief for `0.8.0_AE_CloudComp` (Monday push order D0: "Yes we should bring on 0.8.0_AE_CloudComp to proceed the work here")

**Author:** `1.0.0_SA_CTO` -- 2026-08-24 ~15:1xZ -- **archetype:** COORDINATE / SCRIBE
**For:** `0.0.0_AB_MSTR` (spawns the seat; this brief travels IN the spawn message, per the third-surface
rule -- a fresh seat's only live surface during the integration window) and the seat itself.
**Authority:** Andrew-direct 2026-08-24 ~13:2xZ, D0 note, verbatim: *"D0: Yes we should bring on
0.8.0_AE_CloudComp to proceed the work here."* Disposition (`ANDREW_DIRECT_20260824_MONDAY_PUSH_ORDER_BY_DIRECTIVE.md`):
*"MSTR spawns; the brief carries the routed tooling packet ... + the pipeline enforcement builds ... + D0-T1
broker primitives -- all previously build-routed to that lane."*
**This is a BRIEF, not a TO.** COO issues TOs (stage 3 of any pipeline-bound work); MSTR spawns. Nothing here
is a gate. Push state: landed LOCAL at commit, rides integration -- the spawn message carries the text.

---

## 0. The seat, in one paragraph

Directive **D0 -- Infrastructure (ongoing)**, `docs/architecture/D0_INFRA_TIGHTENING_PRD.md`; placement
**LAPTOP** (criterion b: ontology/infra local; T1 EXERCISE legs run on both fabrics as small verification
kickoffs, never as moved builds). Members: `NFRA_COMPTOOLS`, `NFRA_DEPLOYLEDGER`, `NFRA_DEPLOYCENSUS`.
The seat is the estate's **tooling lane** (comp-tools, graph, broker, gates). Its base last logged 08-21
(lane ~A: comp-adversary control 2 CLOSED; base: 17 pending pre-pipeline TOs, listed in s.5). Every other
lane is closed-out on Andrew's 08-24 order; this seat comes up FIRST among lanes because the gates it
builds serve every TO round that follows (session order `PRD_ROUND_SESSION_ORDER_20260824.md` Phase 2).

## 1. Startup (the standard, stated once)

`/watcher` once (persistent Monitor, `/cygdrive/c` prefix resolved, `TaskOutput -> running`); register under
the FULL serial; `python .tools/to-check.py --all --assignee 0.8.0_AE_CloudComp`; `comp-state --self-test`
must print PASS 4/4 before any record is trusted; zero crons. Read `org/XXX.md` Step 1b in full -- the
A.3 EXERCISE line (run a forwarder, score on output) is the one that bit this lane's family on 07-25/29.

## 2. THE PACKET -- five items, each with its pointer, its expected deliverable, and its verification

| # | item | where it is recorded | deliverable | verified by |
|---|---|---|---|---|
| P1 | **Pipeline gate 1 -- `proof-of-spec-check.py` extension:** a proof instance for a pipeline-bound project is INVALID without a `decomp_ref` + a bidirectional cell<->criterion mapping, denominators printed; no VALID instance -> no `complete` flip. | `org/ref/DIRECTIVE_EXECUTION_PIPELINE.md:149` ("build routed (tooling lane; Andrew's word granted in the ratification)"); positional-citation rule in `docs/architecture/PRD_AUTHORING_PROTOCOL.md` (a bare rc=0 establishes well-formedness, never completeness -- the checker must NAME the expected-id set) | the extended checker + its own mutant battery (delete a criterion row -> INVALID; drop `decomp_ref` -> INVALID; a conformant instance -> VALID) | CVO re-runs the mutants independently; first live subject = the D1_CATVIEWS TOs COO cuts (14 cells @3b103f129) |
| P2 | **Pipeline gate 2 -- TO commit-lint:** a NEW TO file under `org/**/task_orders/` whose project is pipeline-registered (`dep_stage` present in `org/projects/{CODE}.json`) must carry `<decomp_ref>` -- refused otherwise. Teaches at violation time. | `DIRECTIVE_EXECUTION_PIPELINE.md:150`; the choke-point principle at `:142-146` (gate the NECK: TO issuance) | a `safe-commit` gate (same family as `commit-gate.sh` / owned-paths), with the announce-then-enforce ramp the comp-rail used (NFRA_COMPRAIL) and an audited override marker | exercised both ways: a pipeline-registered TO without `<decomp_ref>` REFUSED; a non-pipeline TO passes; the refusal names the rule |
| P3 | **comp-trigger IS the schedule-state instrument** -- three seats independently hit the events-vs-scheduler WRONG-SERVICE zero (an EventBridge `events` listing reads 0 for a rule that lives in `scheduler`, and vice-versa; the zero is clean and false). | CTO log `2026-08-24/session_1742fri-1255Z_etfs_r1_cotfix_d1catviews.md` s.2 (tooling routed en route); `comp-trigger advi-49f-publisher` / `mdpf --days 3` exercised there | (a) a `comp-which` curated rule routing any "is X scheduled / when does X fire / is the schedule enabled" question to `comp-trigger`; (b) the PreToolUse HUD nudge on raw `aws events` / `aws scheduler` INSPECTION (same shape as the IAM/s3-ls nudges in `comp-tool-hud.sh`) | `comp-which "is advi-49f-publisher scheduled"` routes to comp-trigger (score in the vetted band, not a fuzzy guess); the HUD nudge fires on `aws scheduler get-schedule` and does NOT fire on operational calls |
| P4 | **comp-estate framed zero + WARRANTED LIST** -- the `served:` field mixes live-derived detail with snapshot prose with no marker; a firm-scoped absence reads as nonexistence (the `header_metrics_fresh` class, CLAUDE.md comp-estate row). | CLAUDE.md Compiler Tools table, comp-estate row (the PC-003 correction + the "UNTIL the header carries a WARRANTED list" clause); CTO 08-24 log s.2 (framed-zero routing) | the provenance header carries a WARRANTED list: what was live-verified this run, everything unlisted UNVERIFIED BY CONSTRUCTION; any absence verdict NAMES THE TREE it searched; a cross-tree nonexistence claim enumerates every tree or is not emitted | positive control: a known-live served key lists as WARRANTED with its bucket; negative control: a nonexistent key returns a framed zero naming the tree(s) searched, never "does not exist" |
| P5 | **comp-routes edge-versions false-[OK]** on a pinned `qualified_arn` -- reports `[OK]` on all five edge associations including the three pinned ones, so an edge pin that would ship a silent 404 passes every 22a rung. THIRD measured instance (ETFS_POSITIONING channel item S6; disarm owner AE for the pin, this lane for the instrument). | `org/surprise_channel/ETFS_POSITIONING/INVESTIGATION_v1.md` item `ETFS_POSITIONING-S6` (surfaced by 0.7.0_AE_CloudOps 2026-08-21T20:25Z; class BLOCKING, standing ARMED, grounding GROUNDED -- CVO reproduced the source census: `ignore_changes = [qualified_arn, source_code_hash]` at `lambda-edge.tf:96` / `:151` / `:197`, exactly THREE pinned; and CVO RAN THE TOOL: it prints "DYNAMIC (5) -- these auto-update on terraform apply" and marks all five `[OK]` INCLUDING the three pinned); CTO log `2026-08-21/session_1530-1650Z_pipeline_ratified_decree_provcanon_first_case.md:73` ("-> 0.8.0 via COO"); the ETF pin itself was dropped at `:197` by AE (TO-2) -- the other two pins stand | the sub-mode discriminates: a pinned qualified_arn whose version != the live association reads `[PINNED-STALE]` (or the Rule-24-clean vocabulary the lane proposes -- with its four-postulate record), never `[OK]` | mutant: pin one association to an older version in a scratch TF plan -> the tool flags it; the un-pinned four stay `[OK]` |

**Sequencing inside the packet (CTO recommendation, COO decides):** P1 + P2 first -- they are the neck of
the pipeline every round this week runs through (D1 TOs are the first live subject); P3/P4/P5 next, each a
bounded instrument fix with its own control pair. Every item's TO carries the three-phase compiler mandate
and a `<proof_of_spec>`; P1's own proof is checked by the checker it builds (state that explicitly -- and
have CVO run the mutants, not the author).

## 3. D0-T1 broker primitives -- BUILT; what is left is the cross-fabric exercise

The D0 PRD's TO table (row 1, `:125`) still reads *"T1 broker build ... 0.8.0-class at respawn"*. **It is
behind:** the three primitives are LIVE in `org/mcp/server.py` -- `send_message(to_agents=[...])` with the
per-recipient DELIVERED/QUEUED/REFUSED map, `get_delivery_state` (SENT / EMITTED / READ / UNKNOWN-PRE-T1),
`ack_messages` (the READ clock) -- built by this seat @ded91deb55 (08-19), @ee60ec75cc (08-19),
@9a16770cbb (08-20, "part 2 of 2 -- server.py wiring + the A1-A5 harness"); `ack_messages` schema made
resident @83e6a786d7 (0.5.0~Z). Exercised live this session at the CTO seat (3 sends with per-recipient
maps; READ ack recorded on 66211).
**Open leg, per the PRD's own bar (`:154`): "T1 acceptance trio green on BOTH fabrics"** -- the site-Z
exercise is UNVERIFIED at this seat. First cheap act for the seat: run the acceptance trio on the laptop
broker, then hand the site-Z kickoff over the bus (a verification kickoff, never a moved build -- D0
placement row). Then the PRD row is corrected to BUILT with the hashes.

## 4. The rest of D0's live legs (the PRD's dated rows -- COO re-grounds at pickup)

T2a stamp generalization (both `build_package.py` homes emit BUILD_MANIFEST; `:126`); T4 two-homes
declarations (every census row FORK-DELIBERATE(why) or DRIFT(owner) against the READ denominator -- the
16+3 is a prior the TO re-reads, never an acceptance value; `:129`); REG-SCAN-ATOMCHECK + J3 (08-20,
REQUIRED before INF binds -- state at pickup); LD-0424 kill-instrument self-exclusion fix; GLDRNS wrapper
disambiguation (08-25); the CRO-led infra-graph program. These are NOT re-specified here -- the D0 PRD is
the spec; the packet in s.2 is what Andrew's D0 note added on top.

## 5. The seat's inherited TO set -- COO's triage, not the seat's first act

`to-check --all --assignee 0.8.0_AE_CloudComp` will list ~17 pending pre-pipeline TOs (NFRA_COMPLEARN
AMD-P3b/c/d, NFRA_COMPSIMILAR PH1, NFRA_GRAPHFEED W1, NFRA_KUZUSPLIT P0-P1, NFRA_MSBEFF R4R6,
NFRA_PASSCRAFT TO-1/2/3, NFRA_SYSPARITY DENOM, NFRA_TOOLGRAPH TO-1/2, NFRA_VELOCITY_CORE WS-C8,
OPAL_ASSETS P0-A, OPAL_CONSOLIDATION P3-CENSUS, ADHOC graph-tests) plus the base folder's newest
(NFRA_EPISTEMY C3/C4, NFRA_ONTOLOGY R1/W-15, LD0433 RETIRE, NFRA_TRUNCLASS, NFRA_WORLDMODEL). Per the
TO-status law (supersede = need met another way, cancel = ruling killed it -- COO or issuer sets them),
**COO adjudicates that set at pickup; the seat does not self-select from it.** The packet (s.2) + the T1
exercise (s.3) are the seat's work until COO's TOs land. Two unread items sit in its inbox from 08-21
(CVO R1 LEG-1 ruling; MSTR's Andrew-direct stop-word relay) -- read them first; the stop-word was the
fabric-wide 08-21 order, discharged by the 08-24 close-out.

## 6. What this brief does NOT do
No gate, no dispatch, no self-selection of TOs, no cadence (zero crons). It carries pointers + expected
deliverables so the seat's first hour is not spent re-deriving what four seats already measured.
