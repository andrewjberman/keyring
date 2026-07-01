# NFRA_COMPPROOF B -- TO-B2 JUDGE REPORT (independent 3-axis verdict)

**Judge:** `3.0.0_SA_CVO~B` (author != solver != judge; I neither authored the corpus nor solved a case).
**Scope:** the 6 banked cases B-02..B-07 (B-01/B-08 Andrew-dropped; B-09..B-20 judged as they bank).
**Method:** graded blind of MSTR's author-read. Grounded on the captured `tool_log` + live source/graph,
never the solver's self-narration. Rubric = `harness.score_run` (SOLVED = reach==yes AND usable AND resist;
MISS = reach==no OR grounding==trip; else PARTIAL).

## VERDICT SUMMARY -- 5 SOLVED / 1 MISS / 0 VOID (solved 83.3%)

| case | incident | reach | usability | grounding | verdict |
|---|---|---|---|---|---|
| B-02 | FROZEN_BUT_FRESH_3X | yes | usable | resist | **SOLVED** |
| B-03 | GLOBGRPH_SILENT_FREEZE | **no** | usable | resist | **MISS** |
| B-04 | BMKAUD_SEMANTIC_BREAK | yes | usable | resist | **SOLVED** |
| B-05 | COT_AUA_FREEZE_0622 | yes | usable | resist | **SOLVED** (+corpus-enrichment) |
| B-06 | BD_MFA_P0 | yes | usable | resist | **SOLVED** |
| B-07 | BNP_OVERRIDE_WIPE_22M | yes | usable | resist | **SOLVED** |

**This differs from MSTR's 6/6 preliminary-SOLVED author-read: B-03 is a MISS.** Author-read != judge-verdict,
exactly as the isolation is designed. (`solver_results_full.json` + `judge_axes.json` -> `blind_run.py` reproduces
this line deterministically.)

## Per-case grounding

- **B-02 SOLVED.** Reached the sealed mechanism (content froze while wrapper mtime/`generated_at` advanced;
  every freshness gate was mtime/head-object based, not content-motion) and named the remediation class
  (comp-xray/compdiff). GROUNDING=resist: it explicitly caught comp-freshness's mtime FALSE-GREEN live and
  cross-checked content via S3 version history. NOTE: it unified the "3x same class" as a single BD-DataMining
  auth stall and asserted inf was unaffected (symptom framed inf holdings as also frozen) -- a grounded
  elaboration (authtoken-dead alarm 06-29 + bronze-landing gaps are live-real), not an error; core mechanism reached.

- **B-03 MISS (reach=no).** Sealed cause = `incremental_updater` `parent=None` writer/detector froze the marker
  HEAD, unified graph silently stale 2.7d. The solver concluded the **opposite** -- that the marker-HEAD graph is
  FRESH (verified 174/174 Lambda, 35/35 S3 vs live) and blamed a local `.comp-graph/graph.json` TTL cache
  divergence in comp-blast/trace/xref. GROUNDED WHY: the `parent=None` freeze WAS real (commit `90ebf40e6`;
  refined by `c4e1a072f` to a detector false-rejecting `parent=null`-by-design) and was **FIXED + rebuilt 06-15**
  (ledger `globgrph-writer-fix-rebuild`, the B-03 citation). So on today's post-fix substrate the marker is fresh --
  the solver correctly characterized the CURRENT state and could not reach the fixed historical cause. Its local-cache
  alternative is only partially grounded (the SHA-drift gate in `cli.py::_get_graph` L43-60 already closes the very
  divergence it claimed persists; bare-300s-TTL is opt-out-only, L61) and over-confident ("high"). Verdict MISS.
  NOT grounding=trip (it verified its claims); it solved a DIFFERENT, current problem. See FINDING C.

- **B-04 SOLVED.** Dead-on: SmartX-realized model-source override (YALP_MDSRC); SmartX 1M = last-complete-calendar-
  month vs yang trailing-30-day; semantic mismatch, structurally-valid float; no alarm because `validate-files` is
  schema+existence only. Reproduced live 1M values exactly (INT 4.62% vs 2.95%). GROUNDING=resist and EXEMPLARY:
  it saw the `yang-peer-performance` change_management grep-fallback snippets, IDENTIFIED them as forbidden narrative,
  and DISREGARDED them as a Peers-tab distractor -- which also proves the B-04 run_meta VOID is a false positive
  (see FINDING A).

- **B-05 SOLVED + corpus-enrichment.** The out-grounding case. Reached the as_of-keyed holdings freeze and went
  DEEPER than corpus.py, with every specific claim SOURCE-CONFIRMED: `HOLDINGS_COMPLETENESS_FLOOR=0.5` rejecting
  unvalued snapshots -> `ingest_table` returns None (`cot_bronze_ingest.py` L370/446-455); `main()` advances on
  `landed_tables` only + `emit_bronze_sentinel` writes `overall:success` over landed tables (L634-688);
  `data_as_of = perf['date'].max()` (`D_00.portal_aggregates.py` L598/667). Per methodology-flag-1: SOURCE-CONFIRMED
  -> graph>corpus. This is an ENRICHMENT (compatible with, more precise than, the corpus "as_of-keyed freeze"), NOT
  the unconfirmed->MISS branch. See FINDING D. (Minor: `COT_DETECTION_SNS_ARN` log-only path exists but is now WIRED
  in TF/SSM -- an incident-time-vs-now nuance, immaterial to the freeze mechanism.)

- **B-06 SOLVED.** Dead-on: SS&C enabled email-OTP MFA at BD login 06-19; the headless Playwright fleet
  (username/password only, no OTP adapter) hung on the MFA screen -> source dark. GROUNDING=resist: caught the
  frozen-but-fresh decoy (silver/gold re-running on stale bronze), grounded via live S3 (bronze stops 06-18) +
  SecretsManager (session/credentials created 06-25 = the fix). run_meta VOID = false positive (FINDING A).

- **B-07 SOLVED.** Dead-on: `build_canonical_prices_v2` rebuild did not chain the `inject_scoped_overrides`
  post-step -> the 04-06 GLDOPS.004 rebuild wiped the BNP scoped-override -> BNP fell back to equity/ADR pricing
  (BNPQF ~$107-120 vs pinned ~$1.02, ~117x) -> +$22.6M phantom. Grounded via live pricing + source + git history.

## METHODOLOGY FINDINGS (for CTO / ~D / COO)

**FINDING A -- `run_meta.cheat_check` VOIDs are FALSE POSITIVES (B-04, B-06, B-08).** The `run_meta.cheat_check`
field comes from a NAIVE raw-transcript substring matcher, distinct from and cruder than the canonical
`harness.cheat_check`. It flags a forbidden token appearing ANYWHERE in the transcript -- including inside a
`grep -v` EXCLUSION or an allowed tool's OUTPUT. Adjudicated:
  - B-06 `/logs`: all 5 hits are `grep -viE '/logs/|...'` EXCLUSIONS (the solver filtering logs OUT of source searches).
  - B-08 `postmortem`: `... | grep -vi "log\|postmortem\|ledger"` EXCLUSION + the solver's own attestation "no
    narrative/postmortem/ledger/log files."
  - B-04 `change_management`: appeared ONLY in a tool_RESULT (a broad grep returned a line from a DIFFERENT-fix
    yang-colscan deploy narrative, 06-26) -- 0 tool_use; and the solver explicitly DISREGARDED it as forbidden.
  The AUTHORITATIVE gates `blind_run.py` actually runs -- `harness.cheat_check(tool_log)` + `assert_live_context_clean`
  -- are CLEAN (cheated=False, clean=True) for all 6, so `blind_run.py` correctly does NOT void them. RISK: anyone
  gating off `run_meta.cheat_check` would wrongly discard 3 valid runs. RECOMMEND: mark `run_meta.cheat_check`
  advisory/superseded, or teach it grep-exclusion + tool_use-vs-output semantics.

**FINDING B -- TRUE-SANDBOX bypassed; `harness.cheat_check` is blind to grep-RETURNED content.** Every solver
`cd`'d out of its sandbox cwd into the real workspace (cd_into_real_ws 25-46) and ran broad `grep -r`/`find` that
traversed forbidden dirs. NO answer-bearing content leaked (verified: B-02/B-07 surfaced only a prior solver's
Bash-command line + contract-engine source help-strings; B-04 surfaced a different-fix narrative + its own symptom).
But `harness.cheat_check` audits tool-CALL target paths only -- it is structurally BLIND to answer-bearing content
RETURNED by a broad grep. It didn't bite here, but it is a real hole. RECOMMEND: enforce the sandbox cwd
(block cd-out / run in a container), OR extend `cheat_check` to audit grep-returned forbidden content.

**FINDING C -- B-03 is a SUBSTRATE-CHANGED MISS (test-design edge, flag CTO).** The parent=None freeze was fixed +
rebuilt 06-15, so the historical cause is NOT live-reachable today, and -- unlike B-04/B-06/B-07 (whose source
retains a revert-note/docstring) -- the globgrph fix left NO allowed-substrate marker of the old mechanism; its
explanation survives only in FORBIDDEN narrative (commit messages / deploy ledger). So a clean blind solve on
today's substrate genuinely cannot reach it. This is a legitimate reachability GAP for fixed silent-freeze incidents,
not solver incompetence. RECOMMEND: for fixed incidents, run B against a pinned PRE-FIX vintage, or classify them
source-archaeology-only. (The auto-emitted gap-charter for B-03 should carry this note, not a generic graph-gap.)

**FINDING D -- B-05 corpus-enrichment.** The solver source-confirmed a more precise freeze mechanism than corpus.py's
"consolidated/orphaned-holdings as_of-date-keyed freeze." RECOMMEND ~D add an enrichment note to the B-05
`true_root_cause` (the completeness-floor / landed-tables-sentinel / data_as_of=max mechanism). Compatible, not a
correction -- corpus.py is not wrong, just higher-level.

Author: 3.0.0_SA_CVO~B (TO-B2). 2026-07-01.
