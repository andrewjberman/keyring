# CTO~A -- W1b enrichment landed on Andrew's GO + the first live divergence read (2026-08-11 01:20-01:55Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, SCRIBE

**Serial:** `1.0.0_SA_CTO~A` -- window: since `recompile_design_w1a_and_rule14_closure_0015-0055Z.md`.

## Andrew-direct received + recorded (same turn, per law)

VERBATIM (~0122Z, this terminal): *"Go ahead with the enrichment + i am not attached to any old
snapshot, get rid of it whenever convenietn"* [sic]. Recorded durably at
`deliverables/ANDREW_DIRECT_20260811_0122Z_W1B_GO_AND_SNAPSHOT_DELETE_WORD.md` (committed) and
broadcast COO + CTO base + MSTR. Recorded scope: (1) W1b GO; (2) the design s.6 call #1 (W3
snapshot-deletion word) DISCHARGED EARLY -- authorization granted, Rule-9 sequencing unchanged,
deletion executes at W3 post-cutover with no second ask. Only the W4 label GO remains banked.

## Commits (this author line, this window)

| commit | what |
|---|---|
| record commit | the Andrew-direct verbatim record above |
| `@eba455834c` | W1b: READS_S3/WRITES_S3 from deployed-AST + firm-qualification + Dockerfile firmq COPY + 10 new tests |

## W1b mechanism (landed)

Direction from the METHOD (boto3 + pandas method sets); keys from literals or f-string CONSTANT
PREFIXES (level=prefix per the ~C glob=prefix ruling); bare s3:// mentions with no operating
method emit NOTHING (mutant-tested); ownership: firmq writers map (288 keys; image COPY added;
absence declared via firmq_loaded_keys) -> reader-firm fallback -> the one source-grounded
read-override ported with provenance; genuine ambiguity EMITTED as S3KEY_FIRM_UNRESOLVED, never
guessed. S3Key nodes layer=aws per ratified NODE_TYPE_LAYER. Live: 40 evidence-bar I/O edges,
1 honest unresolved. Battery 21/21. W2's precondition (no orphaned pipeline S3-I/O class at
cutover) is met in code.

## QA-METHOD CORRECTION (self-caught, on the record)

The planned "one flagged ad-hoc QA derive" would have COMMITTED to the production Iceberg graph
(derive_runner main() commits + stamps markers) and double-populated `pipeline:` ids beside
graphuni's same-id nodes. QA is now two NON-WRITING acts: (a) dev-box parity/divergence read
(DONE, below); (b) in-container proof = image rebuild AFTER the 02:00Z nightly (a :latest push
reaches five task-defs; never raced) + `ecs run-task` command-override running the module's
READ-ONLY `__main__`. No production write before W2 itself, whose one cutover commit skips
graphuni's pipeline members (double-population structurally impossible).

## The divergence read (first live measurement of the design's thesis)

- Live graph @ Nessie HEAD (comp-kuzu, provenance current): Pipeline 3 / PipelineScript 133
  (bd 69, inf 46, mdpf 18, cot 0) / PipelineFunction 1,201 -- frozen July-1 truth confirmed.
- Deployed universe: 415 objects; per-firm gold: bd 94, inf 143, cot 60, mdpf 20+3.
- CLASSIFICATION (deployed blob-SHA vs `git ls-tree` at local HEAD): **MATCH 310 /
  DIFFERS-FROM-HEAD 29 / MISSING_IN_REPO 76** (per-firm: bd 122/2/5, cot 65/1/10,
  inf 94/22/59, mdpf 29/4/2). Inverse: **75 committed-but-never-deployed** repo .py.
- Declared caveats: DIFFERS direction not determined by SHA alone (local HEAD is 125 commits
  ahead of origin; per-node vintages discriminate); inf's 59 MISSING_IN_REPO = deployed residue
  the frozen chain could never see (explained delta class, headline size); mdpf rows surfaced
  as graph data only -- anything repair-actionable routes to base CTO's MDPF lane.
- Evidence package delivered to CVO 014911Z for the certification pass.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-kuzu` | pipeline population x2 (auto-refreshed to HEAD, provenance read) | PASS -- 133/3/1201 baseline confirmed |
| live extractor exercise | W1b run + per-(firm,tier) census + divergence classifier | PASS -- the parity evidence itself |
| test battery | 21/21 incl. 2 new mutants (no-method mention; ambiguity-never-guessed) | PASS |

**What worked:** exercising before committing caught the production-write hazard in the QA plan
itself. **Gap found:** none new in tooling.

## Blockers

NONE. In-container leg waits only on the 02:00Z nightly completing (NOT-BEFORE, artifact-readable).

## Current State (handoff surface)

- `infra/aws/globgrph/extract_pipeline_cloud.py` @eba455834c: W1a+W1b complete, flag
  `EXTRACT_PIPELINE_CLOUD=1` default OFF, read-only `__main__`.
- Dockerfile carries 3 new COPYs (module, safe_deploy_core, firmq JSON); image NOT yet rebuilt.
- Production graph untouched; subdivided estate-report runner live at S3 code/ key awaiting its
  09:00 ET first unattended fire (Andrew + CVO's pre-registered V1-V6 are the oracle).
- Commits lane-local on CLOUD, HELD per Andrew's standing no-push.

## Next Steps

1. **[this seat]** post-nightly: globgrph image rebuild (CodeBuild) + in-container read-only
   standalone run; notify [3.0.0_SA_CVO] -> their coherence-armed certification.
2. **[this seat]** stage the W2 cutover commit (flag default ON + graphuni pipeline members
   skipped, one commit) -- fires only after CVO's pass.
3. **[this seat]** W3 snapshot deletion at its wave (authorization already in hand, recorded).
4. **[3.0.0_SA_CVO]** certification on the delivered evidence + the in-container leg.
