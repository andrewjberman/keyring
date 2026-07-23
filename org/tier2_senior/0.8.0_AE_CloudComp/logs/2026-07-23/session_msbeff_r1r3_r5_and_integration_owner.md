# NFRA_MSBEFF batch: R1R3 (output contract + verdict-set derivation) + R5 (comp-keys) + integration-owner role

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

Window 2026-07-23 ~17:04Z -> ~18:50Z. Serial `0.8.0_AE_CloudComp`. Andrew-direct respawn: build the full
MSBEFF remediation set; CTO~Z authoring + dispatching TOs direct (Andrew batch GO, verbatim: "lET'S GET
0.8.0 WORKING ON ALL OF THESE"). Standing mode unchanged.

## Commits this window (all pushed, chronological)

| Commit | What |
|---|---|
| `926487fe6` | R1R3 CORE: comp_output_contract.py helper + M3 verdict-set derivation (frozen VERDICT_EXIT_TOOLS retired) + output-contract registration invariant in comp-manifest-check + 19/19 tests incl. 2 required mutants + M3 mutant + no-regression |
| `325841910` | R1R3 fold-in D: comp-validate BD/INF/COT tree registry DERIVED from PIPELINE_MAP (behaviour-identical, cot isolation fail-safe) + 11 tests |
| `da0d5679e` | R1R3 AC-6: comp_msbeff_rebaseline.py -- 517 rows re-verdicted (the exact 358+59 the interim targeted, now derived) |
| `546f8c0e7` | R1R3 two corrections (CVO~Z-adjudicated): comp-freshness rc2 VERDICT->REFUSE + --refuse-enum artifact for CVO~Z (61 REFUSE rows, source-cited bindings) |
| `b78d41fb0` | R5: comp-keys -- KEY/PARTITION ENUMERATION primitive, registered 5-member-clean + comp-system regen folded in |
| (closeout) | this log (AC-7) + snapshot-vintage header on the enumeration artifact (CVO~Z rec) |

## R1R3 -- THE OUTPUT CONTRACT + verdict-set derivation (6/7 AC, CVO~Z PASS; AC-7 = this log)

THE HEADLINE, and it is the whole thesis of the program: the TO's phase-1 `if_mismatch` clause fired BEFORE
I wrote code -- the TO (and main CTO's gate ruling, and the original M3 proposal) all named comp-tools.yaml
as the derivation source, a CURATED SUBSET whose own header says "Do NOT count tools from this file." That
is instance #4 of the denominator-is-its-own-configuration class, INSIDE the TO whose subject is that class.
I surfaced with machine-enumerated evidence (29 tools / 6 exit_* declared vs a 14-member frozen set; a
literal derive would SURVIVE 2 and DROP 12); CTO~Z re-ruled to tools_index; MSTR verified + main CTO
accepted-in-full, no re-gate. The control caught the class that care did not.

Built:
- ONE shared helper (`comp_output_contract.py`), N consumers. `coverage_line` (R1) + `plane_header` (R3)
  generalize comp-kuzu's provenance header + the mdpf-preflip denominator convention. `classify_exit` (M3)
  DERIVES VERDICT/REFUSE/FAIL/UNKNOWN from the declared exit_codes. Consumer denominator derived at run time
  from tools_index -- the TO's own subject applied to itself.
- `comp-output-contracts.yaml`: enforced-COMPLETE (not curated) against tools_index by a new
  comp-manifest-check member. Header carries the supersession history incl. the re-plane (condition c).
- Frozen VERDICT_EXIT_TOOLS / _REFUSE_EXITS RETIRED; comp_log_auto derives, fail-honest to UNKNOWN.
- Two GROUNDED corrections the frozen hardcode structurally could not make:
  - comp-blast rc3 -> REFUSE (NOT-FOUND, cli.py:263) -- grounds CTO~Z's UNCONFIRMED-39-rows item.
  - comp-iam rc3 VERDICT -> REFUSE (COVERAGE REFUSAL, iam_cli.py:858,900) -- the frozen set was laundering
    12 refusal rows as findings. CVO~Z verified at source, now doctrine instance #6.
- comp-freshness rc2 VERDICT -> REFUSE: I initially called it VERDICT ("artifact was engaged"); CVO~Z's
  axis argument overruled me and is right -- the axis is "concluded about the ESTATE," not "touched the
  artifact." Adopted.
- Fold-in D: comp-validate's 3 hardcoded firm config paths derived from PIPELINE_MAP; cot's PATH-isolation
  preserved as the FAIL-SAFE default (a new firm auto-isolates; merging is opt-in).
- Re-baseline: 517 of ~7100 rows re-verdicted off the REAL-rc jsonl sink (never the md log -- no rc-from-
  text inference). comp-pulse 358 + comp-system 59 = the exact interim target, now derived. Enumeration
  artifact for CVO~Z carries a snapshot-vintage header (rows/sha/as_of) so it self-pins.

CVO~Z independently re-derived the re-baseline (did not accept my numbers): 3 corrections EXACT.

## R5 -- comp-keys (KEY/PARTITION ENUMERATION primitive) -- ACCEPTED

Closes the largest measured rail-override demand (268 aws_freshness entries: 178 DENY + 90 RUN-OVERRIDE),
whose intent was key/partition/prefix discovery, NOT freshness. Dedicated primitive (not a comp-freshness
--raw-prefix mode -- a raw prefix has no freshness basis, would REFUSE, wrong semantics). Three caps:
prefix / partitions (earliest-latest-gaps, derived from full key listing NOT --delimiter, MSYS-safe) /
exists (complete-over data/firm_registry.json). Explicit-Z (s3api, never `aws s3 ls`); never a zero without
its denominator. Carries the R1R3 output contract -- the FIRST new tool built ON the helper AND the first
live test of registration invariant condition (a): comp-keys BLOCKED until it declared its contract, and
the existence member BLOCKED until it was git-tracked. The constitutional law worked on brick #2, unprompted.
Live-exercised (415 keys / 142 partition dates / per-firm existence); mutants on the record (not-found LOUD
rc0, error rc1, separate invocations); 8/8 CI-safe tests.

## Integration-owner role (Andrew spawned ~A/~B/~C/~D under me)

The serial batch-GO (R1R3->R5->R2->R4R6) fanned out: I KEEP R5, R2->~A, R4R6->~B, ~C=ONTOLOGY2 rails,
~D=census. I own the shared registration surface (comp-output-contracts.yaml + tools_index +
comp-manifest-check + comp_output_contract.py) as the merge/coherence hub.
- ~B (R6 retired-alias check): gave the exact insertion point (member fn + one-line tuple append); bound
  the rule -- real-name set derives from the SAME registration universe, never a hand-list. ~B adopted +
  will land a `retired_aliases:` section in the same manifest (one authority, three sections). Blessed with
  two guardrails (exactly-one-section membership; successor validates against the live universe).
- ~C (ONTOLOGY2 vocab): opened the (rail,grain,plane,scope) convergence thread. CTO~Z RULED two-stage
  enforcement -- STAGE 1 (live now): invariant enforces PRESENCE of a declaration (comp-keys proved it);
  STAGE 2 (when ~C P1 lands): invariant ALSO validates declaration VALUES against the canonical vocabulary.
  Builds DO NOT block on ~C; provisional-then-reconcile. My job: reconcile comp-output-contracts.yaml to
  ~C's enums + turn on stage-2 validation when they land.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-manifest-check | completeness (live x3, + output-contract member mutant) | PASS 63/63 -> 64/64 | the new output-contract member; mutant (drop comp-blast) BLOCKS; existence member BLOCKED comp-keys until git-tracked (working as designed) |
| comp_output_contract | --self-test + classify_exit matrix | PASS | 15 verdict tools, 4 refuse exits derived; consumer denominator = live tools_index |
| comp-keys | prefix/partitions/exists LIVE on estate + mutants | PASS | 415 keys, 142 partition dates 2 weekday gaps, 3-firm existence; not-found LOUD rc0, error rc1 |
| comp-which | self-route for comp-keys use_case + phase-1 rail-log read | NEARTIE | comp-keys surfaces #2 (WARN not MISS); rail log gave the 268-override denominator |
| comp-validate | --list post fold-in D | PASS | derived firm registry, behaviour-identical (bd+inf 21 ids merged, cot 2 isolated) |
| comp-system | --check + regen x3 | CURRENT | fail-closed gate fired on each new source (comp-output-contracts.yaml, comp-keys); regen folded into each commit |
| comp-pulse | risk-reflex (every commit) | CLEAN | measured, all files vs 1484 danger nodes |
| commit-gate / safe-commit | every commit | PASS | ruff caught one unused import (fixed); owned-paths gate caught the new-yaml lane gap (1 audited override, then CTO~Z granted the durable rule) |
| pytest | 4 suites | 20 + 11 + 8 + prior | contract + bd-hold + comp-keys; both required mutants on the record |

**What worked:** the phase-1 if_mismatch mandate catching the curated-subset defect before code (the whole
program's thesis, on its own TO). The registration invariant earning its keep on the first new tool. The
derivation catching 2 miscounts (comp-iam rc3, comp-freshness rc2) the frozen hardcode could not.
**What I got wrong + was corrected:** comp-freshness rc2 -- I called it VERDICT; CVO~Z's axis argument
("concluded about the estate" not "touched the artifact") is better and I adopted it. **Gaps found:** the
new registry-class yaml had no owned-paths rule (recurring same-tool graph-module gap; CTO~Z granted the
durable rule); msbeff_log_audit.py's RESULT_TOKENS lacks VERDICT/REFUSE/UNKNOWN and reads the md log not the
rc-bearing jsonl (routed to CTO~Z, his tool).

## Blockers

None. R1R3 6/7 (AC-7 = this log -> 7/7). R5 accepted. Integration hub active, event-driven on ~A/~B/~C/~D
landings + ~C's vocab.

## Next Steps

- [0.8.0_AE_CloudComp] Integration owner: keep the shared surface coherent as ~A (R2) + ~B (R4R6) register
  new tools; reconcile comp-output-contracts.yaml to ~C's (rail,grain,plane,scope) vocab when P1 lands +
  turn on stage-2 value-validation. Batch comp-system regen after the lane wave settles.
- [3.0.0_SA_CVO~Z] R5 verify (signaled ready; parity restored @b78d41fb0).
- [0.8.0_AE_CloudComp~B] land retired_aliases: section + ping hash. [~C] send the vocab tuple ETA.
