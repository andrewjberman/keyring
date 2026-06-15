# CVO Audit — comp-pipescript full-coverage across system + projects (2026-06-15)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE
**Trigger:** Andrew-direct ("ensure comp-pipescript has full coverage across our
system and projects") after a worker hit `io` = "Unknown script" on the
find-dualbiz tree (correctly called tooling-coverage, not correctness).
**Method:** ran every coverage-bearing subcommand against a real script per tree;
read the coverage source-of-truth in `org/modules/graph/pipeline_cli.py`. Ground
truth, not the choices-list.

## Bottom line

The FIRM DATA-PIPELINE coverage (bd/inf/cot/mdpf) is **near-complete** — TOOL-01/02/03
+ the `io --pipeline` fix closed almost every gap banked on 06-12. Two small
residues remain inside that scope (one honestly-guarded). The real "full coverage
across our system + projects" question is the **non-pipeline script trees** (the
find-dualbiz class), which sit entirely outside comp-pipescript's model — that is a
CTO scoping ruling, not a code hole.

## Coverage matrix (ground-truthed)

| Subcommand | Selector | bd | inf | cot | mdpf | non-pipeline trees* |
|---|---|---|---|---|---|---|
| `deployed` (no-arg sweep) | auto all-trees (`_ALL_DEPLOYED_TREES`, TOOL-01/03) | OK | OK | OK | OK (check-only) | not in model |
| `io` / `dag` / `chain` / `feeds` / `consumers` / `overlap` | `--pipeline {tree}-{layer}` | OK | OK | **OK (fixed since 06-12)** | OK | "Script not found" |
| `postdeps` | `--firm {bd\|inf\|cot\|mdpf}` (TOOL-02) | OK | OK | OK | **UNCOVERED (guarded)** | n/a |

*non-pipeline trees with .py present, NOT in `safe_deploy_core.PIPELINE_MAP`:
`data/find/dualbiz/scripts` (7), `data/smartx/scripts` (32), `data/seeking-alpha/scripts` (14),
`data/demo/scripts` (4), `data/yang_pkl/scripts` (1).

**Evidence the banked gaps are now CLOSED:**
- `io A_03 --pipeline cot-gold` → header `[cot-gold]` with cot-specific reads
  (`schwab_bd_account_mapping`, `bd_realized_agg`); contrast default `io A_03` →
  `[bd-gold]`. The 06-12 "io falls back to bd / header [bd-gold]" gap is FIXED.
- `io A_03 --pipeline inf-gold` → `INF_A_03 [inf-gold]`. inf covered.
- `postdeps A_03 --firm {bd,inf,cot}` → each loads its OWN config
  (`_POSTDEPS_CONFIGS`: bd/inf/cot yamls all exist on disk). TOOL-02 added `--firm`
  + a FALSE-CLEAN guard (path auto-detect beats bd-default).
- `deployed` no-arg sweep = `_ALL_DEPLOYED_TREES` from PIPELINE_MAP (bd/inf/cot
  gold+silver+bronze) + mdpf check-only (TOOL-01/03, b5050f6b2).

## Findings

- **G1 — mdpf postdeps config absent (P2, DS; honestly guarded).**
  `_POSTDEPS_CONFIGS["mdpf"] = None` (pipeline_cli.py:~2597), and
  `data/mdpf/scripts/gold/gold_pipeline_deps.yaml` does not exist. `postdeps --firm
  mdpf` correctly prints `UNCOVERED ... not 0-deps` and exits 2 — NOT silent, so
  low severity. Close it by either authoring the mdpf gold deps yaml (DS judgment
  on mdpf's real post-steps) or formally affirming mdpf gold has no post-step deps
  and flipping `None` → an explicit empty-config sentinel so the verdict reads
  "0 deps (affirmed)" rather than "UNCOVERED."

- **G2 — selector flag inconsistency across subcommands (P2, DS/CTO).** `io` &
  the DAG family take `--pipeline {tree}-{layer}` (e.g. `cot-gold`); `postdeps`
  takes `--firm {tree}`. Same coverage intent, two flag vocabularies — an easy
  foot-gun (I hit it this audit: `postdeps --pipeline cot-gold` → "unrecognized
  arguments", which reads like a coverage hole but is just the wrong flag).
  Harmonize (accept `--firm` on `io` as an alias, or document the split in
  `--help`). UX/coverage-consistency, not a hole.

- **G3 — non-pipeline trees are outside comp-pipescript's model entirely
  (P1, CTO scoping ruling — the real "full coverage" question).** comp-pipescript
  is "the authoritative *pipeline* script dependency tool" keyed on the firm
  gold/silver/bronze DAG + the deploy PIPELINE_MAP. The find-dualbiz / smartx /
  seeking-alpha / demo / yang_pkl trees have live .py but no DAG and no
  PIPELINE_MAP entry, so `io`/`postdeps`/`deployed` all return Unknown / not-in-model.
  This is a coverage *boundary*, not a bug. The decision is CTO's: (a) EXTEND the
  tool to register the trees that genuinely have a dependency/deploy chain worth
  modeling (find-dualbiz has discover→harvest→serp→pipeline; smartx has a real
  ingestion→aggregate→precompute chain), or (b) formally SCOPE THEM OUT, document
  the determination (so "Unknown" is a known-answer not a blind spot), and — for
  any tree that deploys code to S3/Lambda — point it at the correct deploy/
  dependency discipline instead. Do not let "Unknown" silently read as "clean."

## Recommendation (per driver)

- **CTO (P1):** rule on G3 — the coverage *mandate* of comp-pipescript vs the
  non-pipeline trees. This is the substance of Andrew's "full coverage across
  system + projects." Recommend a short, explicit coverage-boundary statement in
  the tool's manifest/header so every future "Unknown script" is adjudicable.
- **COO (P2):** once CTO rules, decompose G1 (mdpf postdeps config — DS) and G2
  (flag harmonization — DS) into DS-facing TOs. Both are small, neither blocks.
- **CVO (me):** I will re-verify any landed fix against actual tool output (run
  the subcommand per tree), not the commit message.

## What you should have asked but did not

Whether a tree being "Unknown" to comp-pipescript is *recorded* anywhere as an
intentional out-of-scope determination. Today it is not: `deployed`, `io`, and
`postdeps` each have their own internal coverage source (`_ALL_DEPLOYED_TREES`,
`_PIPELINE_CHOICES`, `_POSTDEPS_CONFIGS`) and the FALSE-CLEAN guard exists for
`postdeps` only. So a coverage grep that miscounts "Unknown" as "clean" is still
possible on `io`/`deployed` for an unregistered tree — the exact miscount class
TOOL-02 fixed for postdeps. The highest-leverage structural fix is a single
declared coverage-manifest (which trees ARE in scope, which are explicitly OUT,
last-reviewed date) that all three subcommands read — so "is X covered?" has one
auditable answer and "Unknown" can never silently pass as "clean" on any
subcommand. That generalizes the per-subcommand TOOL-01/02/03 fixes into one
coverage-source-of-truth.

— 3.0.0_SA_CVO, 2026-06-15 comp-pipescript coverage audit
