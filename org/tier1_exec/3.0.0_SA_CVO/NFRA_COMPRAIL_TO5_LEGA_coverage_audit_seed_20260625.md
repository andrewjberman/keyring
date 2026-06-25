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

**Usage vs escape (the headline) — corrected per CTO RAVC 2026-06-25:**
- 382 on-rails primitive runs: RUN-GREP 192 · ROUTE 171 · RUN-GLOB 19.
- **11 raw RUN-OVERRIDE events → ~2.80% override rate** (raw-event lens). The 3 in the
  first cut were a distinct-INTENT dedup (a defensible lens, but it under-reads the raw
  rate). The rail is still heavily used and rarely escaped — but see the recurring
  override below; it is NOT "none recurring."
- **Two telemetry-fidelity caveats (CTO) that bound this number for LEG-B:** (B, FIXED
  c1790819c) the rail-log truncated `q` at 100 chars, dropping the `# rail-checked:`
  reason on compound `cd && aws … # rail-checked: X` lines — a dedicated `reason=` field
  now captures it, so pre-06-25 overrides are reason-blind but post-flip ones are not;
  (C, flagged not-fixed pre-flip) the `comp-|pipescript` negative filter exits before the
  override-log when the reason cites a comp-tool, so those (correctly-allowed) overrides
  go UNLOGGED → the true count is an UNDERCOUNT (likely >11). Fix = filter reorder, a
  LEG-B post-flip item (deliberately not touched on the eve of the flip).

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

## Build-list (prioritized) — corrected: ONE real candidate (CTO RAVC)

**P1 candidate — comp-freshness coverage gap for arbitrary/unregistered gold-prefix
listing.** The `aws_freshness` override is **RECURRING — 7× across 06-23/24/25** (the
single biggest repeat-override intent; per the NFRA_COMPRAIL "repeat override = coverage
gap" principle, that is a signal, not noise). Mechanism: `comp-freshness` answers a
freshness VERDICT for REGISTERED cadence artifacts only; an agent wanting to list/inventory
an arbitrary or unregistered gold/bronze S3 prefix (raw `aws s3 ls .../gold/`) has no tool,
so falls back to raw aws. **Corroborated first-hand this session (CVO):** verifying the BD
bronze recovery, `comp-freshness` did not cover `forwardfill_v2/`/bronze prefixes (only
registered silver) → I used raw boto3 head/list. So this gap is real and I hit it myself.
Build options: extend `comp-freshness` to a raw-prefix listing/inventory mode, or a thin
`comp-ls`-style on-rails prefix-tree with freshness annotation. CONFIRM exact need from the
post-flip `reason=` field (gap B) before building — but it's no longer "empty build-list."

**Low watch-items (confirm post-enforce, not build-now):**
- "raw literal-token search in TF" — confirm agents accept `comp-grep` rather than override;
  if it recurs, the gap is UX (comp-grep discoverability), not a missing tool.
- DDB inspect (4 DENY) — confirm the data-plane-vs-schema split is clean (schema/edges →
  comp-aws; get/scan/query → operational); if schema-inspect overrides recur, consider a
  comp-ddb schema surface.

## Bottom line for the gate (TO-2 / TO-4)
The pre-enforcement evidence supports flipping Gate-1 on 2026-06-26 (CTO-validated): every
gated DENY class has a tool and the override rate is low (~2.80% raw / 11 events; an
undercount pending gap-C). Coverage is complete-enough to gate — with ONE known build
candidate (the recurring aws_freshness override, P1 above) that is a refinement, not a
flip-blocker (the raw-prefix-listing fallback is operational-free today, so no legit work
is denied). LEG B re-measures the AFTER (override rate via the new reason= field, the
aws_freshness repeat-intent specifically, gap-C true-count fix, any legit-work breakage)
over the post-enforce window and tunes to the data.

— 3.0.0_SA_CVO
