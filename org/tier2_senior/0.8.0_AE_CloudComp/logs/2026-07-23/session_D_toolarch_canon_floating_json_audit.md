# NFRA_TOOLARCH.CANON P1 -- tool data-source audit + exhibit root-cause (~D lane)

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, COORDINATE

Session 2026-07-23 ~20:03Z -> ~20:38Z, continuing the same ~D session after TOOLARCH.P1. Serial
`0.8.0_AE_CloudComp~D`. Event-driven; arms zero crons.

## What happened

Second GO landed same session: CTO~Z dispatched NFRA_TOOLARCH.CANON (Andrew-direct from tonight's MDPF
key-scramble, @7e0f8005d) -- audit which comp-tools read floating JSONs vs comp-kuzu canonical, reroute
them, fix the pipescript-mdpf stale-key exhibit, rule on the comp-routes CF gap. ACK'd, flipped pending,
delivered the P1 audit + exhibit root-cause, routed 3 gate decisions to CTO~Z.

## Deliverable -- @fd12a515b

`deliverables/NFRA_TOOLARCH_CANON_TOOL_SOURCE_AUDIT.md` + reproducible `tool_source_audit.py`.

- **Audit (derived, denominator 84 wrapped tools):** 12 read a floating-json graph/estate projection, in
  3 families / 3 severities:
  - **ACUTE (exhibit):** `estate-coverage-resolver.json` (comp-pipescript, pipescript) -- generated from a
    FROZEN manifest @61e91d334, asserts the stale platinum mdpf key "LIVE fresh 2026-06-15" with no vintage
    disclosure. The s.2 intent==denominator defect (cannot report its own staleness).
  - **ARCHITECTURAL but self-invalidating (NOT silent drift):** `graph.json` (9 tools via cli.py/
    trace_graph) -- source-scanned, HEAD-pinned rebuild-on-drift; the kuzu re-point is a DOCUMENTED
    deferred follow-on (cli.py:56 verbatim). A second projection answering a different question.
  - **UPSTREAM producer:** `stitch_graph.json` (comp-stitch-refresh produces, comp-graph reads) -- input to
    the kuzu build, where the mdpf staleness originates.
  - **Accepted exception (keep):** `nerves-risk-edges.json` (6 tools) is LOUD-VINTAGE (comp-pulse says
    "20.2h old" on every number) -- the sanctioned pattern the resolver should follow.
- **Exhibit root cause (grounded live, case C-ii = canonical itself stale):** live S3 has the current key
  `json/mdpf/global/aggregate-aua-timeseries.json` (fresh today, 242KB -- COO's tonight MDPF cutover), but
  kuzu canonical has NO node for it, only the stale platinum key. So reroute-to-kuzu is NECESSARY BUT
  INSUFFICIENT -- canonical must refresh first, and it's stale precisely BECAUSE the product cutover
  post-dates the 14:52Z graph build. mdpf key TRUTH read as DE/COO-owned, not re-ruled.

## Gate decisions routed to CTO~Z (awaiting ruling)

1. Exhibit interim: land a loud-vintage disclosure on pipescript NOW vs wait for full refresh+reroute (I
   recommend land-now -- small, in-lane, kills the silent mis-scope).
2. graph.json family (9 tools): SEPARATE sibling TO gated on a kuzu-covers-trace_graph coverage-parity
   check, coord base (I recommend separate, not folded -- the census R-0/frontend boundary is the coverage
   risk).
3. Item D comp-routes CF-static-rewrite gap: SEPARATE TO (capability build + main-CTO co-equal, orthogonal
   to this data-sourcing audit).

Canonical-refresh (rec 1a) is graph-derive work I must NOT hand-edit -> graph-refresh/stitch owner, CTO~Z's
routing. Base 0.8.0 (integration owner) given a heads-up on the shared cli.py/pipeline_cli surfaces.

## Gotchas caught

- **Raw-grep connection-blindness (the exact CLAUDE.md Rule-21 hazard):** my first mechanical scanner
  MISSED estate-coverage-resolver.json in pipescript_cli (path defined line 44, json.load line 99 -- the
  read and the filename on different lines) and false-positived KUZU on docstring mentions of "comp-kuzu".
  Caught by ground-truthing the material clusters at source (cli.py:45/56, pipescript_cli:44/99) instead of
  trusting the grep -- rewrote to detect ACTUAL kuzu use + capture json refs anywhere.
- **The naive fix would have been wrong:** "reroute the tool to kuzu" fails because kuzu is ALSO stale on
  mdpf -- only caught by grounding the current key on LIVE S3 + querying kuzu directly, not trusting either
  the resolver or the assumption that canonical is fresh. Verification Law 7 ("well grounded != freshly
  grounded") in action.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-kuzu | mdpf S3Key node queries (current vs stale key), vintage header | PASS | proved canonical stale on mdpf (no json/mdpf/global node) -- the C-ii finding |
| comp-to | set session TO_ID = NFRA_TOOLARCH.CANON... | PASS | race-free |
| aws s3 ls | current vs stale mdpf served key on live S3 | PASS | grounded the current key fresh today (DE/COO truth, read not re-ruled) |
| safe-commit / commit-gate | 1 commit @fd12a515b (-F body); audit script ruff-cleaned | PASS | risk-reflex clean |
| ruff | format+fix on tool_source_audit.py | PASS | clean |
| (grep/read) | ground-truth cli.py/pipescript_cli/derive_stitch data sources | PASS | the connection-aware re-scan that fixed the naive grep |

**What worked:** grounding the material clusters at source instead of trusting the mechanical grep -- caught
both the missed resolver read AND the false KUZU positives. **What failed then was caught:** the first
scanner's line-local json detection + docstring-KUZU false positives (rewrote); the naive reroute-to-kuzu
assumption (falsified by the live-S3 + kuzu grounding). **Gap found:** the estate has 12 floating-json tools
in 3 families; the canonical graph is stale on the freshly-cutover mdpf thread.

## Addendum -- CTO~Z ruled all 3, ruling 1 EXECUTED (~20:40Z -> ~21:00Z)

**CTO~Z accepted the audit and ruled all three my way** (204001Z): (1) loud-vintage interim APPROVED
LAND NOW; (2) graph.json family = separate sibling TO gated on the kuzu-covers-trace_graph coverage-parity
check; (3) comp-routes CF gap = separate capability TO. Plus the exhibit sequence: (a) loud-vintage ->
(b) stitch-definition refresh derived-from-source -> (c) reroute -> (d) verify.

**Ruling 1 LANDED @dcf153915, exercised.** `pipescript` now discloses on stderr, above every served-key
line: `SOURCE: estate-coverage-resolver.json SNAPSHOT -- last_review 2026-06-15 (38d old) -- NOT comp-kuzu
canonical` + a verify-before-acting warning. Controls: stdout byte-identical (stderr-only), rc preserved,
age COMPUTED not static (stays honest as it ages), always-on (no suppress flag -- a control that can be
silently disabled is weaker).

**SITING -- the boundary I checked BEFORE editing (the real lesson of this leg).** CTO~Z said "land
in-lane"; the obvious site, `org/modules/graph/pipescript_cli.py`, is the **NFRA_PIPESCRIPT_TOOL
exec-lock** -- DS 0.4.0 family + execs, with the whole 0.8.0_AE family deliberately excluded and the
NFRA_COMPREG general grant *explicitly preserving* that lock. I read `.owned-paths.yaml` and resolved the
lane membership BEFORE making the edit, rather than discovering it at the commit gate (as happened earlier
today with docs/architecture on the P1 census). Sited the control in the WRAPPER `.tools/pipescript`
(lane ANY) instead: same user-visible effect, engine lock intact, **zero owned-paths override**. An
approval to "land now" is not an approval to cross a lane -- the two are independent, and the ruling
authorizes the WHAT, never the WHERE.

**Routed:** stitch/canonical refresh (b) to base with grounded specifics (kuzu has no node for the live
key; producer is `infra/aws/globgrph/derive_stitch.py`); base to route to the actual producer owner. I take
(c)+(d) the moment canonical carries the new key. Base separately ACKed the coverage-parity precheck as its
own and flagged a coupling for the sibling TO: re-pointing the 9 tools CHANGES their declared
output-contract plane/vintage, which the stage-2 gate validates -> the reroute TO needs an
output-contract-update leg (base owns it).

## Blockers

None blocking me. (c)+(d) of the exhibit sequence are GATED on the canonical/stitch refresh (base-routed,
not my hand-edit); rulings 2+3 are CTO~Z-authored sibling TOs. Event-driven standing by; offered to draft
the sibling-TO scope from the audit if CTO~Z wants it off their plate.
