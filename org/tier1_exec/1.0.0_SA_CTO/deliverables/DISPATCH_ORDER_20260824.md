# DISPATCH ORDER -- 2026-08-24 evening session (dependency order + seat plan + the process contract under test)

**Author:** `1.0.0_SA_CTO` -- **archetype:** COORDINATE
**Status:** v0.1 PROPOSED ~19:4xZ, for convergence with `2.0.0_SA_COO` (COO ISSUES; CTO ORDERS) and for Andrew's word on
the four calls in s.6. Supersedes the ordering half of `PRD_ROUND_SESSION_ORDER_20260824.md` (v0.2); that file's
position map (s.1/1a) stands as the morning's measurement.
**Commission:** Andrew-direct ~19:29Z (record
`ANDREW_DIRECT_20260824_ONE_PROJECT_PER_TIER2_SEAT_DECOMP_BEFORE_TOS_CVO_PROOF_OF_SPEC_CRO_OFFLIMITS.md`): *"figure
out how we need to sequence each of these and coordinate with COO to produce a dependency order so we can dispatch in
a decisive fashion"* -- under the ONE-PROJECT-PER-TIER-2-SEAT rule, with COO's decomp BEFORE every TO and CVO's
proof-of-spec + surprise channel on every return. **Distribution:** COO, CVO, MSTR. NOT CRO.
**Push state:** landed LOCAL, rides MSTR integration.

## 1. POSITION -- the pipeline projects on THIS fabric, by `dep_stage` (read 19:3xZ from `org/projects/*.json`)

| project | dep_stage | what exists | next act | seat |
|---|---|---|---|---|
| **D1_CATVIEWS** | DECOMP | 14-cell decomp @3b103f1298; CVO cert @d2706b2849 SUPERSEDED-PENDING-ABSORPTION (view-tree word ~18:5xZ, PRD s.8.6 + run RV1); TOs D1b (DS, pending) / D1c (DS) / D1d (DE) / D1e (DS) ISSUED 08-19 | COO absorb v2 (L0/L1/L2 renderer cells on the D1d family; registry vocabulary; fee-taking predicate) -> CVO re-cert -> TO amendments | COO (now, unconditional -- 66337) |
| **ADVI_INSURE** | PRD (approved stage 3) | PRD v0.2 s.11 ten rulings; run I1-I10; prior art DATA_BDINSURANCE (resolved BD insurance API) | COO stage-3 OPEN + decomp -> CVO cert -> TOs | COO |
| **ADVI_STITCH** | PRD (approved stage 3, Phase A) | PRD v0.2 s.11; run S1-S12; bronze_legacy/silver_legacy landing is his word | COO stage-3 OPEN + decomp (Phase A only) -> CVO cert -> TOs | COO |
| **ADVI_PERFRP** | PRD (approved stage 3) | PRD v0.3 s.11 fourteen rulings; run P1-P16; s.6 rectangle + s.8 cells B1-B9 / F1-F6 | COO stage-3 OPEN + decomp -> CVO cert -> TOs | COO |
| **D3_MODELOVERLAY** | PRD (v1.1 approved stage 3) | run #1-#18; TOs D3.1 (DELIVERED) / D3.1b / D3.2 (DS) / D3.3 (DS~B) / D3.4 (DE) / D3.5 (CVO) ISSUED 08-19 against v1.0; v1.1 adds the overlay-onto-ADVI surfaces (four-level runner, Books placement, per-partner models plane) | COO decomp of the v1.1 DELTA surfaces AFTER D1 re-cert (D3 pends D1; shares the Books placement + spine with PERFRP) | COO, wave 3 |
| **ADVI_COTKEY** | REGISTERED | commissioning word + D2 s.11 (iii) | **CTO stage-2 PRD** (investigation shape as a run) -> COO decomp -> a DS-class measuring seat | CTO (now) |
| **DATA_PIPMAP** | REGISTERED | commissioning word; first cell (Cottonwood MDPF code home = declared per-firm deploy destination) | **CTO stage-2 PRD** (the census matrix as the run) -> COO decomp -> census cells (read-only, proposals) | CTO (after COTKEY) |
| ETFS_POSITIONING | EXECUTING | round 1 delivered; promote NOT YET (two conditions) | **round 2 is the SITE-Z chain** (D4 on SITEZ until done @ae52dce8c0; BQL CLOSED -- "No we're not doing BQL"; CTO~Z drafts the constituent-pipeline PRD). Laptop residue: AE TO-5 apply (committed-not-applied cron) + COO round-1 close | site Z; AE class; COO |
| D0 (0.8.0 packet) | brief @3943af6e72, seat not spawned | pipeline enforcement layers 1-2 (`proof-of-spec-check` decomp_ref + cell<->criterion alignment; TO commit-lint) + the seating lint CANDIDATE | MSTR spawns a FRESH 0.8.0 lane, ONE project (D0 gates) | MSTR |
| ADVI_49FSRC | PRD -- PARKED (Mike at 49) | -- | nothing this session | -- |
| MDPF_PROVCANON | REGISTERED -- PARKED | -- | nothing this session | -- |
| D2 parity P1-P3 | staged, never started | CRO methodology leg | **UNSTAFFABLE THIS SESSION** (CRO off-limits on every subject) -- stays staged; surfaced, not chased | -- |

## 2. DEPENDENCIES (hard edges = "cannot start"; soft edges = "shares a surface, sequence to avoid re-decomp")

```
 HARD
 D1: COO absorb v2 -> CVO re-cert -> D1 TO amendments (DS gold; DE portal + renderer cells) -> D1 DONE
 D3: D1 DONE (directive: "pends D1+D2") ------------------------------------------------> D3 v1.1 delta decomp -> TOs
 INSURE / STITCH-A / PERFRP: each  COO decomp -> CVO cert -> TOs   (independent of each other at stage 3)
 PERFRP ATTRIBUTION cells      <- INSURE live for 49F   (s.10: "no attribution while insurance is blended")
 PERFRP SI-across-migration    <- STITCH Phase A        (s.10: "no SI series across the migration without the classification")
 PERFRP Books-tab INTERFACE on the post-2024 canonical series  <- NOTHING (s.10: "neither gates the Books-tab interface work")
 COT bindings (PERFRP Tier-B, D3 Tier-B, INSURE port)  <- ADVI_COTKEY ruled   (s.11 (iii))
 COTKEY:  CTO PRD -> COO decomp -> DS-class investigation -> ruling
 PIPMAP:  CTO PRD -> COO decomp -> census cells (read-only)  -- no dependents; Cottonwood cells FIRST (his trigger fact)
 D0 gates: no dependents; makes the session's test mechanical the moment they land
 SOFT
 PERFRP <-> D3 v1.1 : same Books placement + four-level spine -> PERFRP decomp FIRST, D3 delta decomp reads it
 INSURE <-> PIPMAP  : the Cottonwood INSURE port wants PIPMAP's Cottonwood cells -> PIPMAP Cottonwood cells before the port
```

## 3. WAVES (each wave's START condition is an OBSERVED completion, never a date)

**WAVE 1 -- NOW (exec paper; zero Tier-2 spawns; no TO exists yet).**
- COO: (1) D1 absorb v2 -> hand to CVO; (2) stage-3 OPEN declarations for INSURE, STITCH-A, PERFRP -- operative surfaces,
  fan-out cohort, certifier = CVO, placement axis, Rule-24 record -- then the decomps, in the order **PERFRP -> INSURE ->
  STITCH-A** (PERFRP's spine + Books placement is the surface the other two and D3 hang off; INSURE next because it gates
  PERFRP's attribution cells; STITCH-A is census-first and self-contained).
- CVO: D1 re-cert on the v2 run; then certs in the order the decomps land; open `org/surprise_channel/{D1_CATVIEWS,
  ADVI_PERFRP, ADVI_INSURE, ADVI_STITCH}/INVESTIGATION_v1.md` at each stage-3 open.
- CTO: ADVI_COTKEY stage-2 PRD (first); DATA_PIPMAP stage-2 PRD (second); the two law edits (this commit's sibling);
  reads the backgrounded deployed-sweep when 0.8.0-class capacity exists.
- MSTR: spawn a FRESH `0.8.0_AE_CloudComp~<lane>` for D0 gates ONLY (the base 0.8.0 heap of 28 TOs is COO's triage, not
  this lane's load); integration pushes.

**WAVE 2 -- on each CVO cert (per project, not as a batch): TOs cut, seats spawned, ONE PROJECT PER SEAT.**

| project | executor class instances (one project each) | first TO premise primitives (issuer fills) |
|---|---|---|
| D1_CATVIEWS | `DS~<D1>` (gold: D1b/D1c/D1e re-addressed + v2 cells) · `DE~<D1>` (portal: D1d + L0/L1/L2 renderer) | registry module state; served category keys; DEV build |
| ADVI_PERFRP | `DS~<PRF>` (gold runner B1-B9 on post-2024 series) · `DE~<PRF>` (Books-tab F1-F6, Book toggle) · `AE~<PRF>` (publisher key family + schedule; joins when the runner emits) | daily account fact at frontier; Books tab route; ADVI_PERFORMANCE field contract as artifact |
| ADVI_INSURE | `DS~<INS>` (bronze/silver/gold, daily idempotent pull) · `AE~<INS>` (Lambda/schedule/IAM on the in-grammar prefix) · `DE~<INS>` (header subtext / Insurance segment / Books aggregation; joins when gold emits) | BD insurance endpoint reachable (bd session); prefix absent; publisher key absent |
| ADVI_STITCH-A | `DS~<STI>` (census; bronze_legacy/silver_legacy landing; xref classification R1-R4) · `AE~<STI>` (landing IAM; joins at landing) | opal-data-bd legacy floors (12 tables); dim_account_xref carries schwab_account_id |

**WAVE 3 -- on observed completions.** COTKEY investigation (`DS~<COT>`) when its PRD + decomp + cert land; PIPMAP census
(`0.8.0~<PIP>` or AE-class, read-only) when its PRD + decomp land -- Cottonwood cells first; D3 v1.1 delta decomp when D1
re-cert lands AND the PERFRP decomp is certified; PERFRP attribution cells when INSURE 49F is live; COT bindings when
COTKEY is ruled; INSURE Cottonwood port when COTKEY + PIPMAP-Cottonwood land.

**Lane letters:** MSTR assigns at spawn from the UNION of the spawn audit (`org/mcp/agent-spawn-audit.log` = lanes that
EXISTED) and the disk (= lanes that PRODUCED). *This paragraph carried a disk-derived "taken today" list until ~20:3xZ;
MSTR measured it SHORT on the first seating call (DS ~C/~D/~E spawned with no directory) -- a hand-copied occupancy list
inside a seating rule is the frozen-not-live class, so the list is gone and the rule stands in its place. Wave-2 seats so
far: `0.4.0_DS_ClientPlatform~F` + `0.4.0_DE_ClientPlatform~C` (D1_CATVIEWS only), spawned ~20:24Z.*

## 4. THE EXISTING HEAPS -- what the one-project rule does to TOs already on disk (CTO recommendation; COO executes as issuer; call 1 at Andrew)

The rule binds ISSUANCE. The 08-19 TOs for D1 (D1b-e) and D3 (D3.1b/2/3/4/5) and ETFS (TO-1/3/4/5) are ISSUED and sit
on base seats that are closed-out and carry 71 (DS) / 84 (AE) / 10 (DE) open TOs across dozens of projects -- exactly
the condition his word names as damaging. **Recommendation: RE-ADDRESS, DO NOT RESPAWN THE HEAP.** Each of those TOs is
re-addressed (`issued_to` -> the per-project lane; content unchanged; decomp_ref added where the decomp now exists) and
the base seats are NOT respawned as general seats this session. A re-address is an issuance act inside COO's authority
and needs no gate; the RECOMMENDATION is at Andrew only because it changes where his 08-19 TOs land.

## 5. THE PROCESS CONTRACT THIS SESSION TESTS (his words: "properly gated/managed") -- discharged MANUALLY and VISIBLY until layers 1-2 land

Per project, in order, with the seat that owns each act:
1. **Stage-3 OPEN (COO):** operative surfaces named; fan-out cohort + certifier (CVO) declared; placement axis declared;
   Rule-24 four-postulate record for the decomp's axes; s.11 rulings inherited as FIXED, not cells.
2. **Decomp run (COO + cohort):** cells born UNMEASURED, populated by status-missioned fan-out, sealed mutant before use.
3. **Cert (CVO):** independent; a decomp-invalidating finding routes back to COO; re-cert after invalidation is signed by
   base CTO (CRO class excluded this session).
4. **TOs (COO):** every TO carries `<decomp_ref>`; cell<->criterion alignment BOTH directions with printed denominators
   on the TO's face; executor CLASS + seating trigger; premise verification primitives; ONE PROJECT PER INSTANCE
   (s.3). A TO missing any of these is a pipeline failure to surface, not a shortcut.
5. **Seat (MSTR):** spawn on the trigger, brief = that one project's packet.
6. **Execute on spec (Tier-2 lane):** first act = premise primitives against live state; surprises -> CVO's channel
   (OBSERVATION never interrupts; BLOCKING -> issuer; ARMED -> named disarm owner same turn); proof-of-spec instance +
   status flip by the actor in the same turn.
7. **Proof-of-spec (CVO):** `proof-of-spec-check <instance> <expected_criterion_ids>` on every delivered return; cert;
   remediation cut at round close; close on a zero-graduation round.

**How the test is SCORED (CVO records, CTO reports at session close) -- denominators, not adjectives:** TOs issued this
session (N) / carrying `decomp_ref` / carrying printed alignment denominators / addressed to a single-project instance;
proof-of-spec instances delivered / validated by the checker; surprise items by class x standing with routing latency;
decomps opened / certified / invalidated. A gate that "held" is one whose denominator is N/N.

## 6. CALLS AT ANDREW (each one changes the order; none blocks wave 1)

1. **Re-address the 08-19 heaps to per-project lanes** (s.4) -- CTO rec: yes.
2. **DATA_BDINSURANCE** (Cottonwood insurance, Phase 0) -- CTO rec: it becomes ADVI_INSURE's Tier-B (Cottonwood)
   instantiation under the uniformity law (its resolved BD insurance API is the prior art; its LIGHT-serve choice does
   not apply). A register act (MSTR), not a dispatch.
3. **DATA_PIPMAP directive home** -- D0 (CTO rec) vs a new row. Already open.
4. **Wave-2 concurrency** -- ~10 Tier-2 lanes across three certs. MSTR states the cap; waves are sized to it, PERFRP
   seats first.

## 7. WHAT THIS FILE IS NOT
Not a gate (no gates without his word). Not a dispatch (COO issues; the TOs derive from certified decomp cells, not from
this table). Not a ruling on any of s.6. It is the dependency order he asked for, with the seat plan the one-project
rule implies and the contract this session is testing, stated so COO and CVO can converge on it in one exchange.
