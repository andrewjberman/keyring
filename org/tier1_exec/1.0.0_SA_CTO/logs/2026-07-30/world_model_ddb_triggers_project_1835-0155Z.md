# World-model program pt.2: DynamoDB layer, the trigger protocol, the defrost, and NFRA_WORLDMODEL registered

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, VALIDATE, SCRIBE, IMPLEMENT

**Window:** 2026-07-30 18:35Z -> 2026-07-31 01:55Z. Continues
`world_model_census_s3_complete_1330-1835Z.md` (same session, same Andrew-direct thread).
**Written because Andrew directed it (2026-07-31 ~0145Z): everyone who touched this work owes a log a
SUCCESSOR CAN RESTART FROM.** That is this file's only job.

## 1. What closed in this window

**THE DYNAMODB LAYER IS COMPLETE — 37/37**, in 5 batches, same protocol as S3 (blind instruments ->
Andrew rules -> delta classed). Every survivor carries a sovereign `business_function`.

Rulings of consequence:
- **`opal-users-v2` IS THE OFFICIAL USER DATABASE** (Andrew: *"very important to note and log wherever
  possible"*) — confirmed at source: `trade-auth-handler` + `opal-partners-data` both carry
  `USERS_TABLE=opal-users-v2` in deployed env; `opal-users` is the deprecated predecessor (email-HASH
  only, no GSI, rows already in v2 shape = written then abandoned). Landed as a durable memory entry.
- **`opal-sessions` system decommission** ruled (table + `opal-session-analytics` + 4 `/analytics/*`
  routes + portal ingest). **DELETE DENIED at my permission layer — staged Q-23.**
- **`opal-pii-lookup`** ruled DELETE, same permission denial, same staging.
- **Investigations answered:** `opal-inf-launch-locks` is a HEALTHY TTL-backed EC2 launch mutex (zero
  rows IS the success state); `opal-pm-snapshots` is NEVER-ADOPTED (TTL *disabled* + zero rows = never
  written). **One `describe-time-to-live` call separates two identical-looking tables into opposite
  verdicts.**
- **`opal-firms`/`offices`/`invitations`: Andrew's "unused" inclination CONFIRMED, my card was WRONG.**
  I had written "likely load-bearing for auth." Measured: one FICTIONAL firm (`smith-wealth` / "Smith
  Wealth Management"), one fictional office ("Boston Office"), invitations empty — and the real
  `users-v2` rows carry `firmId` `49financial`/`opal-capital`, **neither in the firms table. The join
  does not resolve.** Row count said small, schema said plausible, only the VALUES said fictional.

**THE EVENTBRIDGE LAYER OPENED** on ~A's `TRIGGER_GRAPH_AND_RUNTIME_MAP.md` (154 triggers,
zero-drift-verified). Group 1 (Advisor Intelligence / Data Platform, 55 triggers) carded as five
chains. **Groups 2-13 unstarted — the resume point.** Findings: the Inflection 09:00-10:27 and 49F
17:38-18:30 **wall-clock ladders** (each step assumes the last finished; Cottonwood does it correctly
with an event spine, so a right answer exists in the same estate); **`inf-gold-trigger` has three
rules and ALL THREE ARE DISABLED yet gold wrote at 15:02Z** — a production layer with no
trigger-graph representation; 49F has **no** hourly value-parity check while inf and cot both do.

**`FIRMSEP-s3-direct-access-bypass` — broken twice, and the first break hid the second.** Re-verified
live: ~250K invocations/day, `FailedInvocations` equal to `Invocations` exactly, every day
(positive-controlled). AND the pattern matches every non-CloudFront read — i.e. all legitimate
internal traffic — so **repairing the delivery would create a 250K/day page storm.** Moratorium
applies; it is an exist-or-not decision (Q-32), not an SNS fix.

## 2. What I built (frameworks, all mirrored fabric-side)

- **`TRIGGER_ASSESSMENT_PROTOCOL.md`** — T1-T7 battery (fires / delivers / executes / writes / writes
  DATA-not-receipt / writes WHERE IT SHOULD / ordered correctly) + **P1-P17 pathology checklist, every
  entry measured in this estate, append-only by design** + JSONL edge schema + firm-estate chunking.
  TAP pilot dispatched to `~A` (23 Inflection edges); `~B` held behind protocol validation.
- **`RESOLVER_DEFROST_DESIGN.md`** — the 10 census fields split **5 deterministic / 4 prose / 1 key**;
  the resolver becomes a prose layer + a compile step, so the stale-able file ceases to exist.
- **`CORPUS_INTERFACE.md`** — after ruling 6 made my ledger ~B's interface, the declared contract
  INCLUDING measured instability (`sits_at`/`scope` on 97/116, `type` an open vocabulary at 36 values,
  append-only with retraction rows, `id` not a join key).
- **Doctrine:** the cardinal rule *"we can never ever have dependencies on frozen maps"* + CVO's scope
  clause (*dependence is the operative verb*) into `docs/doctrine/CHECK_LIVE_NOT_FROZEN.md`.

## 3. The two-graphs finding (Andrew asked; I had conflated them)

**Graph A — the fact graph** (`kuzu_nessie_db`): deterministically derived, dual-producer refresh
(02:00Z full re-derive + CloudTrail event-driven incremental), **observed refreshing to Nessie HEAD
repeatedly mid-session.** Not stale.
**Graph B — the thread model** (`estate-coverage-resolver.json`): a JOIN of a LIVE hand-adjudicated
manifest (committed twice that day) and a census read from a **hardcoded date-pinned path**
(`logs/2026-06-15/estate_census/`) with **no refresh path** (recorded 07-24: *"FREEZE, do not fix by
regenerating"*). **Live half joined to frozen half → current vocabulary over stale facts, and new
vocabulary renders as UNASSIGNED rather than an error — so decay is silent AND grows in proportion to
how well the living half is maintained.** All three comp-estate defects traced to this one asymmetry.

## 4. Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-kuzu` (~10 this window) | DDB edge census, trigger edges, table drift-class | PASS |
| `comp-estate` | **feasibility test of the descent ladder** (`--segments`, vertical, `--structure`) | FEASIBLE + 4 defects; 3 fixed by CVO within the hour and **independently re-verified by me on the live tool** |
| `comp-grep` / `comp-glob` | resolver generator hunt, doctrine home, Kimi harness | PASS |
| `comp-dataflow` | (prior window) gate over inf producers | FUNCTIONAL, 1 blocking find |
| `commit-gate.sh` | every `.py` | PASS |

**What worked:** using the estate's own artifacts as instruments (the DR snapshot's `dynamodb-configs`
gave me all 37 tables free). **What failed:** long mixed-quote bash heredocs, repeatedly — switched to
writing scripts to files and running them, which is now my default for anything with JSON in it.
**Gap:** no comp-tool covers live DDB row-grain or TTL status; used raw primitives with `# rail-checked`.

## 5. Coordination (the substantive ones only)

- **Seeking-alpha teardown:** Andrew GO'd -> 0.7.0 executed **step 1/5** (both head rules DISABLED,
  applied read-back verified, positive control) then **deliberately halted** rather than open a
  multi-leg irreversible chain on a thin budget. Re-scoped by them into **4 consistency-seam tranches**
  (T1 capture / T2 inert compute / T3 code leg / T4 irreversible), Andrew approved, **A1-A3 TF
  resurrection hazards first**. They then stopped at the seam again and committed the plan to their
  tracker — *"a plan that lives only in an MCP thread dies with the session."*
- **Telemetry spill:** CVO routed it; I verified **27x wider** (134 shadow trees / 7,557 rows) but the
  causal clause **inverted** — the producer was fixed 07-17, the residue is historical. CVO retracted
  in full and propagated. MSTR landed a fail-closed guard (LD-0355) that **upgraded past my one-liner**
  to catch wrong-derived roots too.
- **Andrew standing ruling, broadcast to all 5 seats:** *"P0 is what i say it is and everything else
  that I do not explicitly say we're doing does not matter until I say otherwise"* — **the restriction
  is on SCOPE, not writing; a queued item is NOT authorization.** 0.7.0 then found the exact overclaim
  it targeted **in their own tracker** ("everything below is authorized") and corrected it in place
  with the reason stated.
- **Rulings 5/6/7/7a** (via CVO): the daily loop keeps the reference artifact honest; the corpus is
  USER INPUT not git activity; the real story is **<1000 chars/day**. Limb C is CVO/Kimi-held.

## 6. NFRA_WORLDMODEL — REGISTERED AND PARKED

`docs/architecture/NFRA_WORLDMODEL_PRD.md` + `org/projects/NFRA_WORLDMODEL.json` + REGISTRY row
@`8ce0119fab`. Three limbs (capture walk / substrate defrost / text-recording + The Story). **Parked by
the sovereign — nothing executes until he names it.**

## 7. Current State (for a cold reader)

**Canonical program home:** `C:\Users\AndrewBerman\Desktop\OPAL_WORLD_MODEL\` (own repo, ~45 commits,
**NO REMOTE**). **Fabric mirror:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/AWS_ESTATE_CENSUS_20260730/`
(manual CTO copy; `FABRIC_MIRROR_README.md` carries the discipline + declared dependents).
Ledger **119 rows** · **30 ontology classes** · **C-1..C-17** · **Q-1..Q-33**.
**Walked:** S3 35/35, DDB 37/37, EventBridge 55/154. **Decommissioned:** 19 resources, all
capture-before-delete + positive-controlled.
**Lanes:** `~A` held (TAP read-first complete, probes unstarted) · `~B` held → now on the estate-report
build · `0.7.0` base on enrichment + tranches · CVO on comp-estate + Limb C + a new dialed-tool-flow
commission.

## 8. Next Steps

1. **[Andrew]** THE REMOTE on the canonical repo — raised 4x, now holds a daily pipeline's primary
   feed behind a hand-run copy. Then: A6/A7 TF second legs · the two human-confirm sweeps · the
   wsd-49f frozen-frontier decision · ~A/~B hold clearances.
2. **[1.0.0_SA_CTO]** Resume at **EventBridge groups 2-13**, then compute (192 lambdas + EC2, folding
   Q-9 unmapped-lambda sweep + Q-6 shared-reader measurement), then IAM last.
3. **[0.7.0_AE_CloudOps]** Kill-list confirmation + the tranche plan (A1-A3 → T1-T4). **Aug-1 14:00Z
   ETFS fire is theirs and does not wait.**
4. **[0.7.0_AE_CloudOps~A]** TAP pilot on release; **[~B]** estate-report build (CVO approves).
5. **[3.0.0_SA_CVO]** Limb C; census regen with `last_review` preserved (gates the Limb B cutover);
   comp-estate defect 4 (`etf-reports` UNASSIGNED-RESIDUE) post-fire.
