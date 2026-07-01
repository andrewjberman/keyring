# Graph + Traversal-Tooling End-to-End Validation Report

**Author:** 0.8.0_AE_CloudComp~B | **Date:** 2026-07-01 | **For:** 2.0.0_SA_COO~B (addendum owner) | **Requested by:** Andrew-direct
**Method:** 52-agent validation workflow (35 comp-tools x {runs? current? correct? dead-end?} + 5 cross-layer walks + 6 comp-which naturalness probes, each gap adversarially re-verified) over the canonical estate graph at Nessie HEAD `5cca1bdd` (fresh Phase-B derive, provenance CURRENT).

## Verdict: VALIDATED_WITH_GAPS

The graph and its query surface **work and are trustworthy for the load-bearing cases.** The canonical graph is categorically complete + current (52 node-type + 52 edge-type categories; 19844 nodes / 34834 edges; provenance CURRENT, pin==marker HEAD). **27 of 32 tools PASS with spot-checks matched to live AWS / TF / source ground truth; 0 hard failures.** 3 of 5 end-to-end cross-layer walks connect. The residual gaps are isolated, mostly self-disclosed, and none is a silent-wrong on a healthy primary path.

**Confirmed-good (sample, all spot-checked vs ground truth):** comp-kuzu (edge == live lambda config), comp-blast (== source writes line-for-line), comp-iam (== TF line-for-line), comp-routes (== cloudfront.tf), comp-freshness (== live s3 ls to the second), comp-lambdamap (== live CodeSha256), comp-secrets (== describe-secret), comp-xray (caught a real frozen-but-fresh the mtime tools miss), comp-platinum, comp-cache, comp-pii, comp-cluster, comp-constants, comp-diff, comp-dups, comp-chainrun, comp-registry, comp-adapter-audit, comp-graph, comp-tooltip, comp-symbols, comp-xref, comp-pipescript, comp-transform. Walks: IAM reachability; EventBridge->Lambda->S3 (9 paths); StateMachine->27 Lambdas.

---

## ERRORS (prioritized) -- each with source grounding + fix assessment

### E1 (HIGH, naturalness) -- comp-which surfaces the 8-min REBUILD for basic read questions
- **Symptom:** plain graph-traversal questions ("what lambdas read bucket X", "what state machine invokes which lambdas") route to `comp-aws derive` -- an 8-minute write-path rebuild the read-only path forbids -- and NEVER surface the read-query surface. 2/6 naturalness probes GAP. comp-which is the mandated default entrypoint (CLAUDE.md Rule 21), so this actively steers agents to a forbidden rebuild.
- **Grounding:** comp-which routes via `org/modules/graph/comp_route.py` + the `graph-call-manifest.yaml` catalog. The manifest ALREADY carries a per-entry `mode` field (`query | query-cached | rebuild`); `comp-aws derive` = `mode: rebuild` (id `cloud.derive.refresh`). The router does NOT use `mode` to exclude write-path tools from read-question results.
- **Fix (per Andrew's framing -- tagging, not "push comp-kuzu"):** (a) tag/name `comp-aws derive` unambiguously as the REBUILD / WRITE-PATH so it reads as "regenerate," never "answer"; (b) make `comp_route.py` HARD-EXCLUDE / floor-rank `mode: rebuild` entries when routing a read/traversal question -- a rebuild must never be the top answer to "what reads X"; (c) reposition comp-kuzu as the instant head/state check + the canned-query fallback for arbitrary traversal, so agents reach a read answer naturally (via the right rich tool or a canned query) rather than needing to know comp-kuzu by name. Andrew: "agents shouldn't need comp-kuzu aside from a cursory instant-state/head check of the traversal surface."
- **Owner (proposed):** comp-which / comp_route owner (~E authored the engine; CTO comp-routes surface).

### E2 (HIGH, connectivity) -- portal serving->production provenance dead-ends
- **Symptom:** a served portal URL cannot be traced back in-graph to its producing PipelineScript. The serving subgraph (Hook/Endpoint/ServedURL) and the production subgraph (Lambda/PipelineScript/S3Key) are DISJOINT -- joined only conceptually at the bucket layer. "What produces this served file" is unanswerable.
- **Grounding:** `infra/aws/globgrph/derive_runner.py:1300` `stitch_served_from` emits the `SERVED_FROM` edge to the coarse **S3 BUCKET** node (`opal-data-portal-v2`, 0 outbound edges = terminal sink), NOT a key-level S3Key (source comment lines 1302-1303). Resolution rule (1293-1297): `/api/general/{X}` -> `opal-data-portal-v2/json/{X}`. Separately, Endpoint nodes carry NO edge to a backend Lambda (Endpoint->Lambda = 0 paths within 5 hops).
- **Fix assessment (moderate derive-side enhancement):** (a) emit `SERVED_FROM` to the KEY-level S3Key node (`opal-data-portal-v2/json/{X}`) instead of the bucket; (b) enumerate the portal-served keys as S3Key nodes if not already present; (c) model the PUBLISH/COPY edge from the producing pipeline's data-bucket key (opal-data-bd/inf/... gold artifact) -> the portal-served key -- this requires identifying the publisher (the lambda/script that copies gold artifacts into opal-data-portal-v2); (d) optionally add Endpoint->Lambda edges for API-backed (non-static-S3) routes. (a)+(c) are the load-bearing pair that actually closes producer-provenance.
- **Owner (proposed):** NFRA_TSGRAPH / globgrph derive owner (~D / DE).

### E3 (HIGH, tool) -- comp-drift per-target parity mis-invoke reports clean as broken
- **Symptom:** reports a provably-clean lambda (bd-49f-fees-runner; comp-lambdamap parity confirms MATCH) as UNVERIFIABLE/DIVERGED integrity-break -- would send an agent chasing a phantom deploy break.
- **Grounding:** `org/modules/graph/drift_cli.py:217` `adapter_comp_lambdamap` runs `_bash("comp-lambdamap","parity", *([target] if target else []))` -- it passes the target lambda POSITIONALLY to `comp-lambdamap parity`, which accepts NO positional (argparse rc=2). So the per-target parity leg ALWAYS mis-invokes when a target is given. The `--deep` leg additionally mis-attributes whole-estate IAM census drift (38/14) to the single target.
- **Fix:** (a) drop the positional -- run `comp-lambdamap parity --json` (whole-estate) and FILTER the JSON for the target lambda's verdict (or use parity's real target-filter interface if one exists -- confirm at fix time); (b) scope the `--deep` IAM-drift attribution to the target, not the whole estate. Small + isolated; comp-drift's seam-ledger coverage is otherwise solid.
- **Owner (proposed):** comp-drift owner (~D -- drift_cli.py).

### MEDIUM -- work one-by-one in the addendum (RE-VERIFY FIRST; these were rate-limited out of adversarial re-check)
- **M1 comp-trace S3 edge direction inverted:** reports `s3.get_object` READS (e.g. `_load_allocation_signals` at A_03.positions_cube.py:151-177) as `WRITES_S3`; labels a GOLD script as writing a silver/ prefix. Upstream CALLS-chain is correct; S3-edge modeling is the unreliable part. `[UNVERIFIED]`
- **M2 comp-types nested-type index fabricates consumers:** for 0-direct-importer types (ModelPortfolioData, NonModelAssetsResponse, PeerModelData) it substitutes a bogus 38-site TenantLayoutConfig consumer graph AND persists it to types-index/*.yaml, printing PASS -- while its own `blast` reports 0 files. Confidently-wrong on the MP/benchmark SEV1 surface. `[UNVERIFIED]`
- **M3 comp-parity headline is a frozen constant:** the CLI only load+validate+prints config; live comparators are defined but never invoked (comp_parity_cli.py:271-304). "DAY-1 PROVEN 0/5892 value-breaks" is a hardcoded string literal (L290-293), not a re-measured verdict. `[UNVERIFIED]`
- **M4 comp-heat federated mode crashes on its own default:** unhandled ValueError ("SQL with a single quote is unsupported by the v0 run-task transport", _trino_fed.py:72) -- its built-in query contains a single quote the transport can't send. The other 3 modes (freshness/drift/score) run clean + verified CORRECT. `[UNVERIFIED]`

### LOW
- comp-coverage writes a hardcoded `Generated: 2026-05-15` stamp on every run (coverage_cli.py:211) though stdout is live; comp-coverage is a TO-compliance auditor, not a graph tool. Windows-console non-ASCII mojibake (display-only) across comp-transform/xref/secrets/pii/adapter-audit. comp-blast/comp-diff --help advertise a `File` query form that returns NOT-FOUND (canonical is prefix-qualified gold:/lambda:/component:); comp-diff cost doc ~2s vs actual ~13.6s.

---

## CAVEAT (transient API rate-limiting hit 8 workflow agents)
- **UNTESTED (not counted PASS):** comp-grep, comp-glob, comp-validate -- their tool agents rate-limited out. Status unknown, not assumed-good.
- **UNVERIFIED (self-disclosed w/ file:line, NOT adversarially re-checked):** M1-M4 above + E3's comp-drift verify. Findings are well-grounded and credible but not independently confirmed.

## PROPOSED ADDENDUM (fix -> retest -> revalidate)
1. **Re-verify (close the caveat):** re-run the 3 UNTESTED tools + adversarially confirm M1-M4 (+ E3). Cheap; closes the credibility gap before any fix.
2. **Fix (per error, to owners above):** E1 (comp-which mode-aware routing + comp-aws-derive tagging), E2 (SERVED_FROM key-level + publish-edge), E3 (comp-drift parity invocation), then M1-M4 one-by-one.
3. **Revalidate:** re-run the affected validation checks (or the full 52-agent workflow, script at `.claude/.../graph-tooling-e2e-validation-wf_36627032-99c.js`) -> target 0 open gaps + the 3 untested tools PASS.

**Bottom line:** the graph and query surface are correct and current where it counts; the friction is isolated and now NAMED with file:line. This report scopes the addendum.
