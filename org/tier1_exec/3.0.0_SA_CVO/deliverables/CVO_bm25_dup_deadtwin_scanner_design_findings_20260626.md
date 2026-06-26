# BM25 Dup / Dead-Twin Scanner -- Design + First Cloud Findings

**Owner:** 3.0.0_SA_CVO | **Date:** 2026-06-26 | **Dispatch:** Andrew-direct via CTO | **Gate:** CTO arch-gate (pre-standing-dimension)
**Status:** prototype RUN against the live estate; design + first ranked findings for arch-gate.

## Mandate
A fuzzy-match scanner for duplicated / overlapping resources + **dead resources that never got
cleared but still carry a (near-)same name**. Andrew named **BM25** as the lexical matcher.
Design + prototype + **test on the cloud** (run against the live estate, surface real cases).

## The load-bearing design insight (the classifier)
**BM25 alone over-flags** -- some duplication is legitimate (per-partner, per-environment). The
real classifier is **BM25 (lexical) x THE GRAPH (reachability + firm + partner) x structure**:

| lexical twin + ... | verdict |
|---|---|
| one side graph-**UNREACHABLE** (zero downstream consumers) | **DEAD-DUPLICATE** -> worklist (the "never-cleared dead resource") |
| both reachable, **different** firm/partner | **BENIGN** -> suppress (expected architecture) |
| both reachable, **same** firm/partner | **NEEDS-REVIEW** -> human adjudication |

The graph is what separates concerning from benign. **Firm-separation is a hard suppressor:**
a bd resource and its cot/inf twin is EXPECTED architecture, NEVER duplication -- suppress, never flag.

## Guardrails (non-negotiable)
- **Advisory/scanner ONLY.** Never auto-removes anything (removal is human-confirm). Output = a
  RANKED candidate-duplication ledger = a worklist for human/graph adjudication.
- **Rule 22:** a "dead resource" claim is a HYPOTHESIS until the graph CONFIRMS zero-consumers.
  "dead" is INFERRED until graph-grounded. The scanner PROPOSES; the graph CONFIRMS; a human adjudicates.

## Architecture
**Doc model (tiered):** `document` = the matchable token set per resource-type.
- **NAME-level** (cheap; catches twins + dead-names) -- prototyped.
- **CONTENT-level** (catches drifted near-duplicate scripts/TF blocks sharing a body) -- tier 2.
Per-type doc: S3 prefix, Lambda fn, TF resource block, gold/silver script, EventBridge rule, doc/deck file.

**BM25 mechanics:** inverted index (all-pairs is O(n^2); the index gives near-neighbors in ~O(n*k));
per-doc top-k neighbors above a threshold. BM25 scores are corpus-relative/unbounded -> output
**RANKED candidate PAIRS** with a normalized score + a review-band, NOT a binary verdict.

**Suppression loop:** reuse the existing `org/modules/graph/debtscan/suppression_v1.yaml` mechanism --
legitimate per-partner dups + confirmed-benign go there so they never re-flag.

**Home + surface (proposed, for your gate):**
- a new debtscan **DIMENSION** under `org/modules/graph/debtscan/` (alongside D1-D5; the duplication/dead-twin class), producing the ledger.
- a comp-tool front (**`comp-dups`**) registered in `graph-call-manifest.yaml` + comp-which-routable; queries/triggers the dimension.

## First cloud findings (PROTOTYPE, NAME-level, 2 classes; live estate)

### Validation -- it RE-FOUND both live cases CTO cited
- **comp-iam collision class:** flagged `aws_iam_role "step_functions" / "yang_pipeline_lambda" /
  "portal_lambda" / "bd_exporter"` as EXACT-LABEL twins across modules -- the same bare-label class
  as the orchestrator/scheduler bug.
- **D3 doc-clobber class:** flagged `DATA_PLATFORM_D2_BLACK_DIAMOND_ARCH_SPEC.md` (docs/architecture)
  vs `DATA_PLATFORM_D2_black_diamond_arch_spec.md` (docs/briefs) -- a case-only collision (clobber risk
  on a case-insensitive FS), the exact sibling of the D2/D3 case.

### New real candidates surfaced (ranked, post-firm-suppression)
- **DEAD-TWIN (high value):** `aws_lambda_function "this"` + `aws_cloudwatch_event_target "lambda"`
  in `infra/aws/lambda/deprecated/` twinned with live modules -- a `deprecated/`-path resource still
  carrying a live twin name = the "never-cleared dead resource" Andrew named. (`deprecated/` path is a
  strong DEAD prior -- to be graph-confirmed per Rule 22.)
- **NEEDS-REVIEW (same-firm):** `aws_dynamodb_table "opal_users_v2"` declared in BOTH
  `terraform/portal-auth` and `terraform/shared-infra` -- a same-name table across two modules (real
  overlap or a data-source ref? worth adjudication). `aws_iam_role "bd_exporter"` across
  `ec2/bd-exporter/terraform` ~ `terraform/bd-pipeline` (intra-bd cross-module).
- **Doc stale-twins:** canonical `docs/architecture/X.md` vs `docs/architecture/archive/X.md` or
  `docs/briefs/X.md` (API_PATH_RESTRUCTURE, PARTNER_IDENTITY_TABLE, TRADE_SUBMISSION) -- a live doc +
  an archived/brief near-twin = the clobber/staleness class.

### What the live data TAUGHT (refinements the prototype evidenced -- "BM25 over-flags")
The over-flags are the proof of the thesis; each is a precise suppressor to add:
1. **Environment-twins:** dev/staging/prod copies of the same module label (yang_pipeline_lambda x3,
   step_functions, portal_lambda) are LEGITIMATE per-environment -- suppress like firm-twins
   (env detected from the module path `environments/{dev,staging,prod}`).
2. **Per-agent-tree multiplicity:** `session_summary.md` / `advisor_intelligence_completion.md` across
   many `org/.../{logs,task_orders}/` trees is expected (every agent has one) -- suppress same-name in
   per-agent/per-thread trees.
3. **Service-split policies:** `<base>_s3` / `_cw` / `_sm` / `_ddb` / `_secrets` are one role's
   policies split by service -- legitimate, suppress (a shared base-name + a known service suffix).
4. **`archive/` + `deprecated/` paths** = strong DEAD/stale priors -> raise dead-confidence, not benign.

## Plan (for your arch-gate)
- **Now (done):** NAME-level prototype, 2 classes, live-run, the above findings + suppressor list.
- **Next (gated):** add env / per-agent-tree / service-suffix suppressors; fold in the GRAPH-reachability
  tier (comp-blast/downstream -> the dead-confirm leg, Rule-22); broaden classes (S3 prefixes, Lambda fns,
  gold/silver scripts); CONTENT-level tier for drifted near-dups; wire `suppression_v1.yaml`.
- **Productionize (gated):** the debtscan dimension home + `comp-dups` comp-tool + manifest registration
  (COO formalizes the registry/TO once the design lands).

Prototype: `org/tier1_exec/3.0.0_SA_CVO/deliverables/dup_scan_proto.py` (NAME-level, advisory, read-only).

---

# v2 (POST-ARCH-GATE BUILD) -- results against the live estate

CTO arch-gated GO (86d56a3c7) with 4 conditions. v2 (`dup_scan_v2.py`, advisory/read-only) carries
all four; run against the live estate. Machine-readable ledger: `dup_scan_v2_ledger.json`.

## Condition 1 -- precise + auditable suppressors (NO silent suppression)
The v1 over-flag (1358 "concerning" TF pairs) was dominated by LEGITIMATE structure. v2 adds four
PRECISE suppressors, each matching ONLY its exact benign pattern and LOGGING what it hid (a
suppressor masking a real dup is therefore inspectable). Live run: **524 pairs suppressed, all
audited** -- `BENIGN_CROSS_FIRM` 276, `BENIGN_IAM_POLICY_SPLIT` 148, `BENIGN_SERVICE_SPLIT` 84,
`BENIGN_ENV_TWIN` 16. The decisive one was **STRUCTURAL, not string-heuristic**: `BENIGN_IAM_POLICY_SPLIT`
parses the actual `role =` attribute and suppresses two inline policies attached to the SAME role
(one role's policy split by action-area) -- it does NOT mask a real dup, because a true duplicate
surfaces as an EXACT label or identical CONTENT, neither of which that branch touches.
Result: the NAME tier collapsed from 1358 to **10 high-value EXACT-label cross-module collisions**
(the real twin/double-management signal) + a demoted informational near-band.

The 10 high-value catches incl.: `aws_dynamodb_table.opal_users_v2` (the routed first-catch),
`aws_iam_role.bd_exporter` x2 (ec2 vs bd-pipeline), `aws_iam_role_policy.step_functions_lambda_invoke`
(multi-account prod/staging vs bd-pipeline), and the `infra/aws/lambda/deprecated/` `aws_lambda_function.this`
+ `aws_cloudwatch_event_target.lambda` twins (dead-prior -> see condition 2).

## Condition 2 -- DEAD = graph-confirmed (Rule 22), else graph-pending
The dead-confirm leg runs ONLY on high-value findings (cached, short-timeout). A `deprecated//archive/`
path RAISES the dead-prior but the verdict is **`INFERRED_DEAD_GRAPH_PENDING`** until a real graph
result shows zero consumers -- it NEVER prints `CONFIRMED_DEAD` off a path prior alone. Live run: the
`deprecated/` lambda.this + event_target.lambda correctly returned `INFERRED_DEAD_GRAPH_PENDING`.
**Refinement from COO's adjacent finding (opal-users v1):** the dead-confirm leg should take TWO
evidence sources -- graph-reachability (comp-blast/downstream) AND runtime read-metrics
(CloudWatch `ConsumedReadCapacity`). opal-users(v1) is a validated DEAD-TWIN by metric (0 reads/24h
vs v2's 103) -> it becomes the **regression fixture** for the dead-confirm leg: 0-reads + 0-consumers
= `CONFIRMED_DEAD`; either signal alone or absent = `INFERRED_*, pending`. Removal always human-confirm.

## Condition 4 -- CONTENT-level tier + DOGFOOD (proven)
Content tier scans **git-tracked first-party py bodies only** (3184; vendored layer/site-packages
deps excluded by construction + a belt filter). Two sub-tiers: **C1 exact-body-hash groups** (O(N),
catches byte-identical copied modules) and **C2 BM25 near** (drifted shared-body dups).
- **C1 real finds:** `build_transaction_engine.py` x3 (canonical + two timestamped `_GOOD_` backups in
  `archive/versions/`), `bd-price-update/lambda_function_v1_backup.py` IDENTICAL to the archived
  price_update body (a backup-twin living in the LIVE lambda tree), and
  `data/smartx/scripts/lambda_smartx_query.py` == `infra/aws/lambda/smartx_query/lambda_function.py`
  (the same code dual-homed in a source dir AND the lambda tree -> drift risk).
- **C2 DOGFOOD (CTO's explicit test): PASSED.** The top content-neighbors of `lib/trading_calendar.py`
  are EXACTLY the 5 not-yet-migrated copies CTO named:
  `data/mdpf/scripts/gold/_trading_day_calendar.py` (norm 0.524, top hit), `mdpf-daily-trigger`,
  `bd-cot-freshness-probe`, `bd-49f-freshness-probe`, `mdpf-freshness-checker` (all lambda_function.py).
  => the content tier WOULD have flagged the triplicated calendar pre-convergence. Dogfood confirmed.

## What v2 still owes (the standing-dimension arch-gate ask)
- the C2 exhaustive all-pairs near-sweep is bounded for the prototype (proven via exact-dup groups +
  the one-doc dogfood); production needs the blocked-by-stem + max-df candidate-gen at full corpus.
- wire `suppression_v1.yaml` (the 4 suppressor classes land as `pending_review_classes` until CVO-ruled).
- the metrics+graph dual-evidence dead-confirm leg (opal-users v1 as regression fixture).
- broaden classes to S3 prefixes + EventBridge rules; CONTENT tier over gold/silver scripts.
Then COO formalizes the debtscan-dimension home + `comp-dups` manifest registration.

Build: `dup_scan_v2.py` + `dup_scan_v2_ledger.json` (advisory, read-only, never removes).
