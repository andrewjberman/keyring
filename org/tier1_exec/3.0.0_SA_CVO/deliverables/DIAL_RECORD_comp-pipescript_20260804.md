# DIAL RECORD — comp-pipescript (2026-08-04, inline at the Andrew-present terminal)

**Start word:** Andrew-direct this terminal, verbatim: "ok now do the comp-pipescript dial"
(~05:2xZ, firing the queued item of the @179987c5c2 session arc). **Dialer:** 3.0.0_SA_CVO.
**Template:** DIALED_TOOL_FLOW_DESIGN_20260731.md. **Inputs:** DIAL_comp-pipescript_INPUTS_20260803.md.
**Method:** every gate an EXERCISE — all verdicts below rest on probes that could have failed.

## Phase verdicts

| Phase | Verdict | Evidence |
|---|---|---|
| P0 scope+baseline | DONE | shim `.tools/comp-pipescript` → engine `org/modules/graph/pipeline_cli.py` (3,465 ln); universe decl `.tools/safe_deploy_core.py` CODE_TREES (PIPELINE_MAP now DERIVED, "ONE PLAN" CTO 20260728T203649Z); registries manifest:288/:435/:514 + comp-tools.yaml:316 + output-contracts:405/:420; 13 modes censused; baselines cut (io A_00 -p bd golden; deployed 4-tree sweep; postdeps $22M positive control) |
| Universe-conformance (standing ruling) | **FINDING → Andrew** | class = hand-drawn registry, NOT declared as exception. **4 of 10 `data/*/scripts` trees**; `-p assets` = argparse invalid choice (loud, not false-clean — mitigating); assets monolith addressable only as mdpf-subset layers (3/7 gold, 1/13 silver). Build TO @2f256a3830 (assets → 0.8.0_AE_CloudComp~B) pre-staged, covers part |
| P1 purpose | COHERENT; universe question is the open half | io=I/O+column-gaps+portal consumers · deployed=repo-vs-S3 verify · postdeps=blocking pre/post steps. The contested part is SCOPE (deploy-gate subset vs estate script trees) — that is the Andrew naming act above, not a purpose rewrite |
| P2 name+aliases | PASS | retired `pipescript` stub dies rc=2 naming comp-estate (exercised); manifest retired-alias invariant PASS (5 declared); no shadowing |
| P3 registration+contracts | PASS w/ 1 gap | registration invariant PASS (87 accounted); output contract declared incl. the rc-0-verdict-in-stdout note (:420). GAP F7: no provenance/vintage header on io emissions |
| P4 vocabulary+structure | 2 findings | F6 flag-surface inconsistency (io: --pipeline+--firm · postdeps: --firm ONLY · stats/inject: NEITHER — see F3) + choices enum mixes grains (bd-gold/bd/all/mdpf) |
| P5 dependency alignment | STALE SURFACES ENUMERATED | flagless `io [script]` form (now rc=2 REFUSED) taught by: CLAUDE.md comp-tools table rows (io/deployed/postdeps), XXX.md role minimums (DS/DT/AE/COO rows), manifest :288 canonical_call, 9 skill docs (cloud-ops, gold-runner-code-review, molecule, prd-delta, seams, spot-check, stimulus-scan, verify-channel, work — individually unswept), shim header comment (also missing 3 modes). Fix routing below |
| P6 exercise gates | **RED FOUND → REPAIRED → 41/41 GREEN OBSERVED** @a35ac7af8 | suite (4 files) was 4-failed/37-passed, red up to ~4 WEEKS unobserved. All 4 = stale fixtures asserting superseded contracts (07-06 repoint ×2, 07-14 bd-hold lift ×1 + its twin VACUOUS, 07-30 required-flag ×1). Zero extractor regressions: ground truth checked per fixture before repair. Repairs keep mechanisms exercised (synthetic-held; live gap_manifest edge; repoint lock-in negative assertion) |
| P7 residue audit | LIGHT PASS | orbit: engine+core 4,265 ln; per-tree deps configs (bd+cot `gold_pipeline_deps.yaml`, inf `orion_pipeline_deps.yaml` — naming asymmetry, tool resolves it); 4 test files; no TRASH-graded deletions proposed this pass |
| P8 independent descent | NOT RUN — by definition needs a non-dialer | routed as follow-up (CTO descent-test analog or lane agent); banked in re-dial triggers |

## Findings (ranked)

- **F1 SEV-HIGH — postdeps has no unknown-script guard.** `postdeps ZZZ_NO_SUCH_SCRIPT.py --firm bd`
  → rc=0 "No dependencies declared" — byte-identical to a known-clean script. On the mode that
  exists because of the $22M incident, a typo answers "clear to run, no post-steps." Fix:
  validate script_id against tree scripts ∪ deps keys; unknown → rc=2 (TOOL-02 pattern).
  **AMENDED 2026-08-04 ~06:2xZ (CTO datum, CVO re-exercised both limbs): postdeps FLAGLESS also
  works and SILENTLY DEFAULTS TO bd (rc=0, `[bd]` banner) — the exact silent-tree-default class
  the 07-30 stub killed for the io family survives on THIS mode. Composition is the sharp edge:
  flagless + typo'd script = silent wrong-tree default + rc=0 no-deps = DOUBLE false-clean on the
  $22M guard. The F1 fix must carry both halves: unknown-script rc=2 AND the required-flag
  treatment (or an explicit named default) for postdeps.**
- **F2 SEV-HIGH — undeclared 4-of-10 universe** (see conformance row). Naming act at Andrew:
  declare CODE_TREES as an intentional deploy-gate-scoped exception, or widen. The uncovered
  six include the CANONICAL assets monolith (own bucket), etfs (live monthly production fire),
  smartx, demo, seeking-alpha, yang_pkl. An uncovered whole tree emits NOTHING (the per-bucket
  UNCOVERED guard only sees prefixes on covered buckets).
- **F3 SEV-MED — `stats` and `inject` are DEADLOCKED.** Both route through `_build_dag(None)` →
  `:270` refusal demanding a flag their subparsers do not define; the refusal text then points
  the caller at a flag the mode rejects ("unrecognized arguments"). Structurally uninvokable
  since 07-30. Fix: add the flag to both subparsers (or exempt like deployed). WS4 hardening
  should absorb.
- **F4 SEV-MED — canon surfaces teach the refused form** (P5 row above). CLAUDE.md/XXX.md are
  law files → CTO lands those rows; manifest/skills/shim → owning lanes. Exact strings enumerated
  in P5.
- **F5 SEV-MED (standing input re-affirmed) — io WRITES = script-body only**; dispatcher-staged
  writes invisible (DS-measured, `mdpf-daily-dispatch.sh:476-488` class). Fix: one declared-
  limitation line in io output — under-reporting drives deletion (Rule 22a class).
- **F6 SEV-LOW** — per-mode flag-surface inconsistency + mixed-grain choices enum. **Sharpened
  (CTO-exercised, CVO-confirmed): on the io family, `--firm` ALONE does NOT satisfy the refusal —
  `--pipeline` is THE required flag; `--firm` is a narrower auxiliary. The law rows now say so
  (@a86d54fb5).**
- **F7 SEV-LOW** — no provenance header on io output (vintage = working tree, undeclared).
- **F8 SEV-LOW** — comp-which routes the deploy-verify question ("is the deployed copy current")
  to the `io` row, not `deployed` (mode-level routing miss, score-tie artifact).
- **F9 META (P6) — a gate no runner is wired to decays silently.** The suite sat red ~4 weeks;
  every failure dated to a real estate change nobody replayed the suite against. Extends
  feedback_gate_accepted_on_observed_green_run: acceptance needs an observed green AND a wired
  runner. Candidate: fold these 4 files into a commit-gate or scheduled QA run (routing: CTO).

## Live sweep datums (not tool defects — routed to owners)

From the no-arg deployed sweep (4 trees, 217 MATCH / 10 STALE / 12 MISSING_ON_S3 / 27 UNCOVERED
/ 2 TIMEOUT, rc=0 per declared contract): **mdpf STALE ×2 = `dim_mdpf_account_distribution.py`
(producer family of the LIVE SERVED portal bell) + `build_legacy_compat_emit.py` (backfill)** →
COO/MDPF wave. inf: STALE ×2 + AUX-DRIFT ×8 → inf lane. TIMEOUT ×2 rows are unverified-at-rc=0
(contract-declared; reader beware). Adjacent: `gold_freshness_config.yaml:187` still watches
`silver/accounts_dim/latest.parquet`, an artifact with ZERO live gold readers post-repoint → inf
lane judgment.

## Method notes (mine, banked)

- My first rc reads were corrupted by my own pipes (`$?` measured `head`) — re-measured pipe-free
  before concluding; the flagless-refusal "defect" I nearly recorded was my artifact (A.3 class).
- The sweep's tail-25 nearly read mdpf's per-tree summary as the global total — denominator
  printed before quoting.
- Fixture repairs each grounded on source truth BEFORE editing (constant read, hold registry,
  flag law) — a repair that re-asserts a dead contract is worse than red.

## Re-dial triggers (reopen this dial on any of)

1. ~B's assets-tree build lands (@2f256a3830 Phase 3 → my register closure) — re-run universe
   conformance + re-cut sweep baseline.
2. WS4 hardening lands (replaces the refusal stub) — re-exercise F3 modes + flag law.
3. CODE_TREES schema/membership change — and per dial method law, verify the FIXTURES still
   SELECT, not that suites still pass.
4. Any canon-surface edit naming the tool (CLAUDE.md/XXX.md/manifest/skills).
5. Engine change >50 lines or subparser change.
6. comp-which routing-table change touching pipescript rows.
7. P8 descent run lands → fold its stumbles.

## Open at Andrew (naming acts, this dial)

1. **F2 universe ruling**: declare the deploy-gate exception, or order the widen (build routes
   via CTO/COO; assets leg already staged at ~B).
2. Nothing else sovereign — F1/F3/F5/F6/F7 are build fixes (routing: COO/CTO to the graph-lane
   owner), F4 law rows are CTO's to land, F9 runner-wiring is CTO routing.

## Post-close dispositions (CTO 062256Z, logged 2026-08-04 ~06:2xZ)

- **F4 LANDED @a86d54fb5** — CLAUDE.md rows + XXX.md role minimums corrected, forms verified by
  exercise before editing; manifest :288 + 9 skill docs + shim header remain with owning lanes.
- **F9 → path-scoped commit-gate stage** (rcg-sweep-check shape): the suite runs when engine/
  subparser/test files are staged — observes on the CAUSE, not a clock. Build via COO; acceptance
  = mutant-exercised fire + silent-on-unrelated + first run OBSERVED green.
- **F3 → WS4-absorb CONFIRMED**, condition: WS4's acceptance names stats+inject as exercise cases
  (invokable + flag law consistent) so the absorb is verified, not assumed.

— 3.0.0_SA_CVO, dial CLOSED pending the F2 naming act + P8 descent (both non-blocking).
