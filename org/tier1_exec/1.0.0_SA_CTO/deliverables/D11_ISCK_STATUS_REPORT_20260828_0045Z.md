# D11 / ISCK — STATUS REPORT AT REBOOT (2026-08-28 00:45Z)

**Author:** `1.0.0_SA_CTO~X` (laptop, designated seat for D11 / NFRA_C3MATERIALIZE orientation) ·
**For:** Andrew, to hand to GPT · **Window covered:** 2026-08-27 13:04Z reinstantiation → 2026-08-28
00:45Z stand-down for device reboot · **Push state at writing:** origin/CLOUD @3fbb493cda carries
everything through the boundary pin 9760630ae7 and the boundary record ece1ac0f41; the commits after
that (listed in §7) are LOCAL on this device and ride the first post-reboot integration window.

---

## 0. ONE-PARAGRAPH SUMMARY

D11 is the directive under which the NFRA substrate work (`NFRA_SUBSTRATECARDING`, the one member
project, `status: active`, `dep_stage: EXECUTING`) prepares the estate for `NFRA_C3MATERIALIZE`.
Today the work re-oriented around three issues Andrew framed — (1) the Identity/Grain Spine, (2) the
materializers, (3) "unified coherence" — and the third became, on his ruling, the **Identity-State
Coherence Kernel (ISCK)**: minted opaque serials for enduring mutable entities, hashes only for
immutable observations/versions/receipts, temporal substrate bindings, versioned fingerprints,
append-only succession and reconciliation. In eleven hours the ISCK went from a concept to a
**v0.2-candidate contract** (doctrine + JSON Schema + validator + six-gate suite) that survived two
full adversarial rounds by four seats: **round 1** (21 findings, 3 refuted) closed at a boundary with
version pins; **round 2** (~40 listed contributions, 0 refuted — a statistic filed as a target, see §4)
closed tonight at `BOUNDARY_ROUND2.md`. The contract is **attacked, not frozen**, and it does **not**
exit to operational use: the charter's third exit condition, an end-to-end vertical-slice battery
(mint → bind → rename → observe → reconcile → materialize-from-frontier → Nessie advance → Kuzu
dislocation → history preservation), needs the WP-3 ledger and live substrates and has not been
built. Alongside, the L0 emission arc (the census/layer contracts that feed C3MATERIALIZE) reached
a validated rework with a certified emission-authority mechanism, and the `/self-drive D11` loop
ran its first full cycle (gap → CVO verdict → governed amendment → certified, ~100 minutes, zero
Andrew touches) and adopted Andrew's two skill corrections mid-flight.

## 1. WHAT WAS ACCOMPLISHED, IN ORDER

### 1.1 Orientation and the ruling (13:04Z–17:0xZ)
- Reinstantiated after the accidental view close; recovered D11 state from self-drive logs and
  commits; corrected my own stale claims against the live record.
- Read `0.8.0_AE_CloudComp~Y`'s three briefs (C3MATERIALIZE_LAYER_ARCHITECTURE,
  SPINE_FOUNDATION_BRIEF, C3MATERIALIZE_REPO_STATE_AND_GAPS). Framed issue 1 (spine) / issue 2
  (materializers); proposed issue 3 and surfaced the mint-vs-derive fork.
- **Andrew's ISCK ruling** (GPT-assisted, his authority) recorded verbatim @d869c9ffe0 with both
  memoranda: adopt Issue 3 as the ISCK under D11; opaque minted serials win the fork; hashes may
  identify immutables only. Deliverable folder:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/D11_ISCK_RULING_20260827/`.
- **WP-0:** `c2_motifs.json` canonical rename @b56bd2b7f0 (Andrew's word); the ephemeral SBM ad-hoc
  run found on the Desktop and pinned (producer/output/input ABSENT; Result-7 optimiser caveat
  carried into WP-6). **WP-1** PRD amendments @208308bd47. **WP-2** contract v0 @2cdda17b51.
- Six /open-calls recs approved by Andrew ("Recs approved, including call 6"): PRD RATIFIED
  (`docs/architecture/NFRA_C3MATERIALIZE_PRD.md` §10–10.3); adversarial pass released three-seated;
  minting authority laptop-primary; retention git<50MB; 540 deferred to WP-6; MDPF call 6 routed to
  CTO base ("a matter to discuss with CTO Base").

### 1.2 Round 1 of the adversarial pass (18:4x–20:0xZ)
- 21 findings + 3 refutations across COO~X (F1–F7), DT~X (DT-1–8), CVO~X (CV-1–6); all
  adjudicated; v0.1 boundary @21d6fc7325 in one commit (no-moving-target rule); `BOUNDARY_ROUND1.md`
  with the independence ledger, DT~X's registered prediction, and four version pins (CRO~X's gap 6).
- Round 2 chartered @14e6bcc50d from the two external reviews Andrew supplied (GPT + CRO~X's six
  gaps), synthesized on his word.

### 1.3 Round 2 (20:0x–00:4xZ) — the bulk of the night
Landed, each with a cited commit (full table in `BOUNDARY_ROUND2.md` §3):
- **R2-1 fabric semantics** @9fa5a91af5 — execution-family vs referent-family fields; CRO FINAL ACCEPT.
- **R2-3 warrants** @1b08f0e37e + @5ffb98936c — the paired require+forbid idiom ("the forbid half is
  the idiom"); **R2-6 frontier uniqueness** @1b08f0e37e; **R2-5 observed_absent** @e07b9efec0;
  **R2-7 mint_receipt** (LAW 1's compensating control defined) @7b6629d3b7; **R2-8 bridge_assertion**
  @547730fd8a + @7a1192b0c3 (CRO VERIFIED ACCEPT; CV-1 CERTIFIED CLOSED @4f66d2edf2).
- **R2-9 battery maturation:** `run_gates.sh` runs every gate against an ATOMIC git-archive extract
  of a cited commit (DT-R2-3: a working tree is not atomic) @d2fc841873; path-grained mutant
  assertions with declared attack targets + a drift meta-control @3c37267b91 (the first all-green
  suite in the package's life, two-seat reproduced); seat-authored gates (DT~X coverage probes ARMs
  1–4, COO~X labels/collisions/isolation/ablation); the runner summary now prints the candidate
  DENOMINATOR beside the colour @f18f4cf8d4 + @9760630ae7 (COO-R2-1: a green runner masked 15
  open candidates the moment nothing upstream was red).
- **R2-2 append-only + derived status — DESIGN, attacked-dry, NOT landed.**
  `R2_2_DERIVED_STATUS_DESIGN.md` @1061546c63 → four attack rounds → @7c093caff5. The design:
  events are the truth, status is a projection; `status_basis` is a FIELD-SCOPED exact-key map on
  five records / six axes; the `superseded` value leaves `verification_standing` (kills CVO's
  laundering cell) with append-only migration receipts; contests are their own record with a typed
  target (entity | binding) and `upheld` requires its consequence; a `retirement` relation kind with
  no successor; a CLOSED per-kind direction table (`replaces`/`successor_of` retire the OBJECT,
  `merged_into` and `canonicalized_as` retire the SUBJECT); post-boundary absence of the map is
  INVALID, vintage is a migration-manifest lookup; two declared axis classes (five DERIVABLE-AT-WP-3,
  `registry_standing` ADJUDICATION-CARRIED). Landing checklist (8 lines) @bfcebc58c5. **Landing gate
  MET tonight:** COO~X's superseded-consumer census (77156, 00:44Z): 17 files swept; 3 schema arms
  + 2 mutants + 1 probe row break on the enum change; 2 must survive untouched (`superseded` also
  lives in `materializer.current_status` — same-sense collision, edited separately); one set-shrink
  hazard named (`identity_relation` forbid arm keyed on a value SET, not a const).
- **ARM-4 adjudicated 25 of 25** (`ARM4_ADJUDICATION.md` @8f8fe7db5f → @05086d045c): 4 forbid-mirrors
  cut (`held_on` outside held; `store_owner` outside inadmissible; `absent_components` on a complete
  bundle; `delta_summary` on non-mismatch integrity), 21 ruled NO by class with the reason a future
  run must overcome. CUT-4 went narrow → wide on the doctrine's own remedy column ("unverified" =
  the check has not run; FREE means free of REQUIRED warrants, not free of contradiction) — three
  surfaces in one commit.
- **DT-R2-6** (candidate × contradicted structurally uninhabitable on bridge_assertion; COO
  corroborated by 6,144-instance enumeration): `contradicted -> adjudicated_by` RETIRED on BOTH
  consumers @2795145b63; §3.2 re-recorded — contradicted is ENTERED on evidence and LEFT only by
  SUPERSESSION on the assertion chain @d144e7937c (my first re-recording cited an impossible
  carrier; CRO caught it).
- **ARM-3 census 95 of 95 inhabitable** (DT~X @db4062c3a7). **ARM-4 consume gate** (DT~X
  @9fb81b743a; triple-key corrected to four parts by generator count; loader duplicate-key guard
  @6245dc0a3d; consumption-time entry validation @bb7444a08e after CRO's superset-values attack
  falsified it; CRO's three-vector regression ACCEPTED). RUN_GATES now reads
  `overall exit 0 | 11 open candidates (ARM1 9, ARM3 0, ARM4 2 of 20 undisposed)`.
- **ROUND-2 BOUNDARY** `BOUNDARY_ROUND2.md` @ece1ac0f41, amended @7c776ccc5d (exit condition 2 MET
  on my own on-origin read), @8bce3fa495 (CRO's four re-verify defects: span 37 not 35; 6245 is
  inside the pin; ARM-4 blob-at-commit; tally denominator not auditable), @f6269a9a82 (condition 2
  EXERCISED by a post-fetch re-run; CRO regression acceptance). Re-verified at their own invocation
  by CVO (9 cells, denominator stated), COO (gates + pins byte-for-byte), DT (own sections, partial
  declared partial).

### 1.4 The L0 emission arc (parallel, other seats executing)
- The stall worked correctly (CRO~A silence measured against the right clock, WAIT vindicated).
- Rework 4 released on Andrew's "rec approved" @ab9d42206f; DT~X returned it @2ccda14e4a (73/73);
  CRO~X's Base validation WITHHELD on one precise finding (the self-blind no-debris control arm —
  `__pycache__` created by the control's own imports before its baseline); repair authorized
  (R4-6), DT~X reports it ACCEPTED at 2feca185e7.
- **The v1-emission-authorizer gap** (authority orphaned by the CRO~A → CRO~X coverage transfer):
  pitched → CVO~X verdict (CRO seat FAMILY via a consumer-rejectable `v1_emission_authority` field)
  → governed amendment @1a5624ae2a → CERTIFIED BY EXERCISE (4-cell gate matrix) → ledger
  CLOSED-CERTIFIED @5cd7726d8e. The self-drive loop's first full cycle.
- **L2 stays HELD by Andrew's word**, re-seated to CRO~X.

### 1.5 The loop and its law
- `/self-drive D11` armed on Andrew's invocation ~20:45Z; carrier clause in `org/XXX.md` Step 1b-F
  @f6b4fb0c56 (ON ORIGIN); paired with `/drive D11` at `2.0.0_SA_COO~X` (+15m); ledger
  `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/D11/VERDICTS.jsonl`.
- Andrew's two corrections landed as skill law by CTO base and were adopted here mid-flight:
  ADJUDICABLE-default + citation-gated RESERVED + CVO validates reservations per tick (@6c427578d5);
  delta-driven logging (@c68376a47a). My own over-RESERVED classification of the rework-4 release
  (his "textbook case" correction) is recorded in the tick-4 log.
- Ticks 1–6; logs: `ctoX_self_drive_D11_tick2.md`, `tick4.md`, `tick5.md` @f04363536c, session arc
  `ctoX_session_isck_arc_1304-2236Z.md` @e1b54fa5ea. Six audited overrides granted to DT~X across the
  night, each scoped and cited.

## 2. CURRENT STATE — the artifacts a successor needs (files vs dirs stated)

- **DIR `org/standards/isck/`** — the ISCK package:
  - FILE `ISCK_CONTRACT.md` — doctrine: five laws, 12-record catalog, 15 enum records in five-label
    Rule-24 form with conditional-arm tables, §5 minting authority (RATIFIED), §6 ten declared limits,
    §7 changelog. Blob at the boundary pin: d1506ca0944e.
  - FILE `ISCK_CONTRACT.v0.schema.json` — `$id opal:standards:isck:contract:v0.1` (filename stable),
    Draft 2020-12, 12 record `$defs`. Blob b2e3c3683e15; sha256 586bf52c… (LF-as-stored).
  - FILE `validate_isck.py` — self-test: 4/4 axes + 14/14 fixtures + 67/67 reason+path-asserted
    mutants at declared targets + 11/11 semantic + drift + gutted-schema meta-controls.
  - FILE `run_gates.sh <commit>` — atomic-extract six-gate runner; summary line carries the
    candidate denominator; a missing consume line renders UNREAD, never zero.
  - FILES `isck_coverage_probes.py` (DT~X; ARMs 1–4 + consume gate + 22 self-controls),
    `ARM4_ADJUDICATION.json` (generated sidecar), `check_postulate_labels.py`,
    `check_enum_collisions.py`, `check_mutant_isolation.py`, `check_rule_ablation.py` (COO~X).
  - FILES `BOUNDARY_ROUND1.md`, `ROUND2_CHARTER.md`, `BOUNDARY_ROUND2.md`,
    `R2_2_DERIVED_STATUS_DESIGN.md` (design draft, attacked-dry), `ARM4_ADJUDICATION.md`.
  - DIR `vocab/` — `entity_classes.json`, `identity_spaces.json`, `identity_policies.json` (warn-gated).
- **FILE `docs/architecture/NFRA_C3MATERIALIZE_PRD.md`** — RATIFIED; §10–10.3 ISCK adoption + C0
  semantics + canonical-materializer interpretation.
- **DIR `org/tier1_exec/1.0.0_SA_CTO/deliverables/D11_ISCK_RULING_20260827/`** — RULING.md,
  WP0_EVIDENCE_CAPSULE.md (+ SBM addendum), both memoranda, the C3i structural brief pinned.
- **FILE `org/projects/NFRA_SUBSTRATECARDING.json`** — `status: active`, `dep_stage: EXECUTING`,
  2 open TOs; the D11 completion-test target.
- **Evidence pins:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/kimi_subdivision_harness/c2_motifs.json`
  (sha256 cc9b6627…) + `c3_structures.json` (sha256 55025132…) @b56bd2b7f0; graph_vintage nodes
  8601547680771488785 / edges 6655148935215910630.

## 3. GATE STATE AT THE BOUNDARY PIN (9760630ae7, re-run post-fetch 00:39Z)

```
validate_isck.py           exit 0   4/4 axes · 14/14 · 67/67 reason-asserted · 11/11 semantic · meta
check_rule_ablation.py     exit 0   45 of 45 conditionals mutant-covered (47 -> 45 = two wrong arms retired)
check_enum_collisions.py   exit 0   7 collisions, 7 allowed, 0 undeclared
check_mutant_isolation.py  exit 0   (redundancy family reported as INFO)
check_postulate_labels.py  exit 0   15 of 15 enum records in five-label form
isck_coverage_probes.py    exit 0   ARM1 9 candidates · ARM3 0 · ARM4 20 (18 adjudicated, 2 deferred)
RUN_GATES                  exit 0 | 11 open candidates (ARM1 9, ARM3 0, ARM4 2 of 20 undisposed)
```

## 4. WHERE WE ARE LEAVING OFF — owned, unblocked, in order

1. **FINDING REGISTER for round 2** (owner: me; OWED before "0 refuted" may be quoted as a rate).
   CRO~X showed the boundary tally mixes findings with inputs/accepts/censuses; a deduplicated
   register (one id per finding: source, disposition, commit) is the remedy. Id census from the
   inbox at stand-down: DT-R2-1..6, CVR2-1..2 (four findings under CVR2-2), COO-R2-1, CRO gaps 1–6 +
   inputs 1–5 + RA-1..5 + CUT-4 + carrier, CVO AT-1..6 + RE-1..2. Not started beyond the census.
2. **ARM-1's 9 candidates** (owner: me). Four already adjudicated in prose at
   `ISCK_CONTRACT.md :81-83` (`retired`, `producer_declared`, `human_adjudicated` — traced by the
   CVO rubric, not schema — and `unverified`); the register must say so per candidate. Likely
   cuts: `entity_binding.status open` forbids a non-null `valid_to`; `state_observation.failure_state
   partial` requires evidence. Likely NO with citation: `currency unknown` (FREE by §3.14),
   `collision_preflight deferred_to_reconciliation`, `materializer retired` (R2-2 makes it a
   projection). `binding disputed` defers to R2-2.
3. **R2-2 LANDING** (owner: me; gate MET by COO's census 77156; checklist @bfcebc58c5 lines a–h):
   drop `superseded` from `verification_standing` on both consumers with migration receipts; remove
   the two require arms AND the set-keyed forbid arm COO named; retire the two class-D ARM-4 rows in
   the same commit (they flip to live defects otherwise); contest record shape + typed target;
   `retirement` kind; direction table into §3.12; `status_basis` exact-key maps REQUIRED + migration
   manifest; `partial_legacy -> partial`. Sequenced for the implementing boundary (WP-3 ledger);
   can be cut earlier as a v0.2 schema step if Andrew wants the design landed before the ledger.
4. **THE VERTICAL-SLICE BATTERY** (exit condition 3; needs the WP-3 ledger + live Nessie/Kuzu
   substrates; not started). This is what turns "attacked" into "operational".
5. **WP-3** L0 migration + Nessie parts registration; **56 L3 cells** populate only after the pass
   closes; **DEC-02..05** thresholds are mine and must be pre-declaration-bound before any fusion
   run (DEC-02 fed by the bridge `declared_cardinality` census).
6. **L0 arc** (other seats): rework-4 Base PASS at CRO~X → per-emission GO through the certified
   authorizer gate → v1 emission (DT~X) → pair commit → **my step 4** (basis tightening +
   `parts_registered` removal, ONE commit, after the pair commits) → release. **L2 HELD** by
   Andrew's word.
7. Routed at other seats: derive-from-schema gate denominators (COO~X); the consume gate's next
   attack cycle if CRO finds a fourth vector; the census/labels gates' own maintenance.

## 5. OPEN AT ANDREW: NONE

Zero RESERVED cards. L2's hold is his by name and stands; nothing else waits on his word. If a
round-3 charter is wanted (targets: source_frontier and surface_version, unattacked all round; the
consume gate as a suppression mechanism; refuting an ACCEPTANCE rather than a finding), that is a
fresh word — the skill does not open rounds on its own.

## 6. THE LOOP AT REBOOT

`/self-drive D11` is ARMED at tick 6 (cron b7128813, session-only; dies with this session).
**The carrier is the `org/XXX.md` Step 1b-F row for `1.0.0_SA_CTO~X` @f6b4fb0c56, ON ORIGIN** —
the successor session re-arms ONLY from that row (skill §0.4/§5), and re-arms/asks-for the paired
`/drive D11` half at `2.0.0_SA_COO~X`. This stand-down is an OPERATOR stop for a reboot, not a
stand-down on the scope; the clause is NOT struck. If Andrew intends the scope stood down, his word
at a terminal strikes it. Completion test at stand-down: NOT DONE — 0 of 1 projects complete;
REACHABLE 1 / UNREACHABLE 0.

## 7. COMMITS UNDER THIS AUTHOR LINE THAT ARE LOCAL AT WRITING (ride the next window)

d144e7937c (sec 3.2 carrier) · 7c093caff5 (R2-2 fold binding) · 9760630ae7 (runner consume line)
· ece1ac0f41 / 7c776ccc5d / 8bce3fa495 / f6269a9a82 (boundary + 3 amendments) · this report and the
session-close log. Other seats' local tails: db4062c3a7 (DT ARM-3), 9fb81b743a / 6245dc0a3d /
bb7444a08e (DT consume gate + guards), CVO/CRO/COO deliverable commits named in their logs.
Origin/CLOUD @3fbb493cda at 00:39Z carries 9760630ae7 and ece1ac0f41 (is-ancestor read, this seat).

## 8. WHAT THE DAY TAUGHT (the reusable part, five lines)

- The message scrolls, the artifact persists — applied to the author: three of my five round-2
  errors were dispositions describing fixes the artifact did not carry; every patch is now
  match-asserted and every "landed" is a grep count at the commit.
- A prediction must name an instrument that can return both its answers (DT~X).
- A re-verifier's report carries its own denominator or it inherits the record's authority for
  the cells it skipped (CVO~X).
- Naming a class does not discharge it — demonstrated twice in one night by the seat that banked
  it (DT~X).
- FREE means free of required warrants, not free of contradiction; a one-value enum is a
  discriminator with no discrimination; one field serving two intents makes a real state
  uninhabitable.
