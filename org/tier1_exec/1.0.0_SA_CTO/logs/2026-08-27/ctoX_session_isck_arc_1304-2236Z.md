# 1.0.0_SA_CTO~X session — the ISCK arc: from "what is issue 3" to a certified identity contract with a self-running adversarial pass

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT, VALIDATE, SCRIBE

**Window:** 13:04Z reinstantiation -> 22:36Z. **27 commits under this author line.** MCP traffic:
~120 messages handled (all READ-acked); significant: 1 CVO verdict executed + certified, 2 Andrew
rulings recorded + broadcast, 1 CVO adjudication pitched, ~15 cited landings/dispositions.
Self-drive tick detail lives in `ctoX_self_drive_D11_tick2.md` / `tick4.md` — this log is the
session arc, not a re-derivation of those windows.

## THE ARC, in phases

1. **REINSTANTIATION (13:04Z).** Fresh session after Andrew closed the prior view. /watcher healed
   (predecessor PID dead-verified before re-register — no orphan, no peer). Recovered D11 state
   from self-drive logs + commits, corrected my own stale claims against the live record.
2. **THE L0 STALL WORKED (13:0x–14:0xZ).** CRO~A 85.5-min silence: WAIT disposition (measured
   against the right clock, fabric-wide file census, both controls) — vindicated by 4.5 min.
   Snapshot-resolution finding (11 Iceberg homes, 0 refs; `_branch_head` present-as-subject,
   absent-as-relation). TO-KU-REDERIVE closed: 7 of 12 limit claims stale.
3. **DESIGNATION + THE THREE BRIEFS (14:1xZ).** Andrew designated this seat D11/C3MATERIALIZE.
   Read CloudComp~Y's three Desktop briefs; framed issue 1 (spine) / issue 2 (materializers);
   proposed issue 3 (unified coherence) with the mint-vs-derive fork surfaced.
4. **THE ISCK RULING (17:0xZ).** Andrew adopted Issue 3 as the Identity-State Coherence Kernel
   (minted serials win the fork). Recorded @d869c9ffe0 with both memoranda; WP-0 executed
   (c2_motifs.json canonical rename @b56bd2b7f0; SBM record found on the Desktop and pinned
   @ab9e4a36cb — producer/output/input ABSENT, Result-7 optimiser caveat carried into WP-6);
   WP-1 amendments @208308bd47; WP-2 contract v0 drafted @2cdda17b51 (10 record types, mutant
   battery; the battery's first run found LAW-1 unexpressible — declared, not papered).
5. **SIX RULINGS + THE ADVERSARIAL PASS (18:4x–20:0xZ).** Andrew approved all six /open-calls recs
   (PRD RATIFIED; pass released 3-seated; minting + retention ratified; 540 deferred to WP-6;
   call 6 routed to base). Round 1: 21 findings + 3 refutations (F1-F7, DT-1-8, CV-1-6), ALL
   upheld; v0.1 boundary @21d6fc7325 in ONE commit (no-moving-target rule held); BOUNDARY_ROUND1.md
   carries the independence ledger (semi-blind downgrades measured by send-times, the
   build-time-anchor class named) + version pins (CRO~X gap 6). Round 2 chartered @14e6bcc50d from
   the TWO external reviews Andrew supplied (GPT + CRO~X), synthesized on his word.
6. **ROUND 2 (20:0x–22:3xZ).** Landings: R2-3 warrants + R2-6 frontier uniqueness @1b08f0e37e;
   batch 2 (forbid-mirror idiom, contested warrant, limit-2 reclassification) @5ffb98936c;
   R2-1 fabric split @9fa5a91af5 -> FINAL ACCEPT at CRO~X (execution vs referent families,
   fabric_local added); run_gates.sh @d2fc841873 (DT-R2-3: atomic commit extracts — it bit its own
   integrator same-hour); battery-integrity batch @3c37267b91 (**first all-green RUN_GATES in the
   package's life**, two-seat reproduced; path-grained assertions close same-keyword drift with a
   standing drift meta-control); R2-5 observed_absent @e07b9efec0; R2-8 BRIDGE_ASSERTION
   @547730fd8a + isolation @7a1192b0c3 (VERIFIED ACCEPT; CV-1 CERTIFIED CLOSED, its one finding
   closed @4f66d2edf2); R2-7 mint_receipt @7b6629d3b7. Gates green at every cited tip.
7. **/self-drive D11 ARMED (20:45Z, Andrew-direct).** Carrier-before-tick-1 @f6b4fb0c56; paired
   with COO~X /drive. Tick-2 call (v1-emission authorizer, the gap CRO~X refused to inherit):
   pitch -> CVO verdict (CRO seat FAMILY, consumer-rejectable field) -> drive-pair dispatch ->
   governed amendment @1a5624ae2a -> CERTIFIED BY EXERCISE -> ledger CLOSED — **~100 minutes,
   zero Andrew touches.** His two corrections landed as skill law (ADJUDICABLE-default +
   delta-driven logs) and were adopted mid-flight. His "rec approved" released REWORK 4;
   DT~X returned it @2ccda14e4a (73/73; both old reds were wrong-instrument arms, not missing
   laws). Awaiting CRO~X Base verdict -> per-emission GO -> pair commit -> my step 4.

## Files Modified

See commit messages: the 27 commits under this author line this window (git log --author
"1.0.0_SA_CTO~X" --since 13:00Z) each carry per-file summaries. Primary artifacts:
`org/standards/isck/` (contract, schema, validator, gates, vocab, boundary + charter),
`docs/architecture/NFRA_C3MATERIALIZE_PRD.md` (RATIFIED), `org/tier1_exec/1.0.0_SA_CTO/
deliverables/D11_ISCK_RULING_20260827/` (ruling + WP-0 capsule + pinned evidence),
`org/XXX.md` (carrier clause), drive_pairs/D11/ ledger, project JSON, tick logs.

## Compiler Tools

| tool | result | note |
|---|---|---|
| run_gates.sh (atomic extracts) | PASS | built this session (DT-R2-3 remedy); every cited number from it or provenance-stamped |
| validate_isck.py --self-test | PASS | grew 10/19 -> 14 fixtures/65 reason+path-asserted mutants/11 semantic + 2 meta-controls |
| check_rule_ablation / isolation / labels / collisions / coverage probes | PASS | six-gate suite; ablation caught 5 uncovered rules + the double-trip class; labels caught its own stale denominator |
| directives-check --json | PASS | scope resolution + freshness each tick |
| comp-find/Grep (rail-scoped) | PARTIAL | one whole-tree grep timeout early; scoped thereafter |
| git forensics (cat-file/ls-remote/is-ancestor/log -S, with controls) | PASS | every push-state and unverified-sender claim measured, never inherited |

**What worked:** atomic-extract gating; declared-attack-target assertions; the anchoring-events
discipline; classification-derived-not-inherited (learned the hard way). **What failed (mine):**
three instrument errors round-tripped (residual bucket, wrong grain, false-zero glob) — all caught
by disagreement, none by vigilance; one false attribution of a good state (76388); one
over-RESERVED classification Andrew had to flag. Each is named in the record where it happened.
**Gap found:** a gate that maintains its own denominator cannot see it go stale — derive-from-schema
routed to the gate owner.

## Blockers

NONE at this seat. The L0 sequence waits on `4.0.0_SA_CRO~X`'s Base verdict over @2ccda14e4a
(evidence-cited, their armed act, not a stall).

## Current State (zero-context handoff)

- **ISCK v0.1+ at `org/standards/isck/`**, all six gates green at tip (RUN_GATES exit 0), 12
  record types, 15/15 labels. NOT frozen; round 2 open. Remaining: R2-2 design doc (inputs: the
  superseded laundering cell, contested/disputed overlays, partial-not-legacy fusion, retirement
  reasons), ARM-4's 24 require-only candidates adjudication, then the round-2 boundary (four
  version pins) and the vertical-slice exit gate.
- **/self-drive D11 ARMED**: cron b7128813 (session-only), carrier = XXX.md Step 1b-F row
  (@f6b4fb0c56, ON ORIGIN) — a successor re-arms from THAT ROW ONLY. Paired /drive at COO~X.
  Ledger: drive_pairs/D11/VERDICTS.jsonl. Skill amendments in force: ADJUDICABLE-default
  (citation-gated RESERVED, CVO validates), delta-driven logs.
- **L0 arc**: rework-4 landed @2ccda14e4a awaiting CRO~X Base validation; authorizer = CRO seat
  family via certified consumer-rejectable field @1a5624ae2a; on Base PASS: per-emission GO ->
  v1 emission -> pair commit -> **CTO step 4 (mine: basis tightening + parts_registered removal,
  ONE commit, after the pair commits)** -> release. L2 HELD by Andrew's word, re-seated to CRO~X.
- **Standing decisions mine:** DEC-02..05 (L3/L4 thresholds; DEC-02 fed by bridge
  declared_cardinality census; all pre-declaration-bound before any fusion run).

## Next Steps

1. **[1.0.0_SA_CTO~X]** R2-2 design doc; ARM-4 adjudication; round-2 boundary on attacker dry.
2. **[4.0.0_SA_CRO~X]** Base validation of @2ccda14e4a; on PASS, the per-emission GO is yours
   through your own gate.
3. **[0.4.0_DT_ClientPlatform~X]** on GO: v1 emission + pair commit; then hand to step 4.
4. **[2.0.0_SA_COO~X]** derive-from-schema gate denominators (routed); /drive pair continues.
5. **[3.0.0_SA_CVO~X]** R2-2 attack when cut; reservation-validation duty each tick.
