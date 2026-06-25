# NFRA_COMPRAIL TO-5 LEG A — Coverage-Audit Backlog (pre-enforcement seed)

**Author:** 3.0.0_SA_CVO · **Date:** 2026-06-25 · **TO:** NFRA_COMPRAIL.TO-5 (AC4)
**Feeds:** TO-2 (coverage-proof), TO-4 (per-tier enforcement gate, flip 2026-06-26)
**Status:** SEED (early-deliverable per TO-5 LEG-A "can start early"); refine continuously off post-enforce override telemetry (LEG B).

## Method
Mined the LIVE rail telemetry `org/mcp/comp-which-rail.log` (481 lines) — the intent
gap feed the TO names — cross-referenced against the 22 `replaces` intent→tool maps in
`org/modules/graph/comp-tools.yaml`. (The deeper transcript-wide measure via
`hud3_classify.py` over the post-enforce window is LEG B; this seed is the rail-log
first cut, sufficient to inform the gate.)

## Finding: the rail is "complete-enough" to gate — no recurring no-tool intent

**Usage vs escape (the headline):**
- 211 on-rails primitive runs: `comp-grep` 148 · `comp-which` 46 · `comp-glob` 17.
- 3 `rail-checked` overrides total → **~1.4% override rate.** The rail is heavily used
  and rarely escaped — agents are reaching the tool, not bypassing it.

**DENY classes (raw call gated → routed to a tool) — ALL covered:**

| DENY class | n | Routed to | Coverage |
|---|---|---|---|
| infra_grep | 18 | comp-grep (text + dep-context) / comp-aws / comp-iam | COVERED |
| aws_freshness | 14 | comp-freshness | COVERED |
| aws_iam_inspect | 8 | comp-iam | COVERED |
| aws_dynamodb | 4 | comp-aws / comp-freshness ddb (data-plane get/scan is off-rail) | COVERED |
| aws_route | 2 | comp-routes | COVERED |
| aws_deploy_verify | 1 | comp-pipescript deployed | COVERED |

**The 3 overrides (the only escape signal) — none is a missing tool:**
1. `grep firmId infra/aws/x.tf # rail-checked: need raw text` → **FALSE gap**:
   `comp-grep` already gives raw-text match WITH dependency context. The on-rails
   answer exists; this was a reach for `grep` out of habit, not a coverage hole.
2. `gateway not graph-modeled until OPLM` → **graph-onboarding lag, not a tool gap**.
   The OPLMCP gateway has since been graph-onboarded (.07 close) — this class self-heals
   as resources land in the graph (the marker-oracle auto-refresh).
3. `structural prefix inventory to find ...` (S3 prefix layout) → **operational-free**:
   generic `aws s3 ls` is NOT gated (operational, per the rail); comp-freshness/pipescript
   answer freshness/io, not a raw key-tree, and that's by design.

## Build-list (prioritized) — currently EMPTY of urgent items
No recurring intent surfaced with NO tool. The three observed escapes are
covered-by-comp-grep / onboarding-lag / operational-free respectively. **Watch-items**
to confirm post-enforce (LEG B), not build-now:
- (low) "raw literal-token search in TF" — confirm agents accept `comp-grep` as the
  answer rather than override; if override recurs, the gap is UX (comp-grep discoverability),
  not a missing tool.
- (low) DDB inspect (4 DENY) — confirm the data-plane-vs-schema split is clean post-enforce
  (schema/edges → comp-aws; get/scan/query → operational). If schema-inspect overrides
  recur, consider a comp-ddb schema surface.

## Bottom line for the gate (TO-2 / TO-4)
The pre-enforcement evidence supports flipping Gate-1 on 2026-06-26: coverage is
complete-enough (every gated DENY class has a tool; ~1.4% override; zero recurring
no-tool intent). LEG B re-measures the AFTER (override rate, repeat-override intents,
any legit-work breakage) over the post-enforce window and tunes to the data.

— 3.0.0_SA_CVO
