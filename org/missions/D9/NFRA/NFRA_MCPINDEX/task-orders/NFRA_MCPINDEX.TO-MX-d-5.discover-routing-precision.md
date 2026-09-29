# NFRA_MCPINDEX task order -- `MX-d-5` -- routing precision: Q22's vocabulary, a NOT_CATALOGUED rule for weak one-common-word matches, and the ETF ask no longer mis-routed (Z-W10-S1 + Z-W2-S8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-d-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~14</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and catalog-entry text.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- measured misses, graded on the existing harness.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-d-5` (round 4; `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round3.md` @f354170b42)

**Start after MX-d-4 is complete and drained.** The issuer continues you with this order.

**Why.** The MX-v-6 harness reads 23 of 27. The misses:
- Q22 (an S&P/index ask) has no catalog vocabulary;
- Q09, Q13 and Q25 are asks whose true answer is NOT_CATALOGUED, yet they match one common channel keyword
  (row Z-W10-S1);
- the ETF ask "ETF holdings and fund flows" mis-routes to positioning rows on the common word "holdings" (Z-W2-S8,
  seen live in the round-3 close run).

**The act:**
1. **Q22.** Add index-name vocabulary as keywords on the EXISTING catalog row that answers it, `mkt.01`. That is its
   channel's keywords or example asks, through the emitter's source, never a hand edit of `DATA_CATALOG.yaml`.
   Regenerate with the emitter in your worktree. No new row and no new served surface: widening is Andrew-only.
2. **A NOT_CATALOGUED rule for weak matches.** When the ask's only link to a channel is ONE common word (the Q09, Q13
   and Q25 signature), answer NOT_CATALOGUED. State the rule in one sentence. Grade it on recall too: the harness's
   positive asks must not fall (AC3).
3. **The ETF ask.** The catalog holds NO `platinum/etfs` row, and adding one is widening held at Andrew (cell MX-t-10,
   HELD). So the correct answer TODAY is NOT_CATALOGUED, never a positioning row. If a `platinum/etfs` row exists when
   you run, it must come first. AC2 grades both states.
4. Tests on a synthetic catalog. Run AC1-AC3 and commit.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-29 ~07:1xZ) -- the harness compares by DATASET, not by route vocabulary.**
- **Measured at the issuer's re-grade on CLOUD** after the MX-d-5 drain (d1bbe77360) joined MX-t-9's row:
  - ROUTING 25 of 27; dataset asks 1 of 3; d5.AC3 FAILs.
  - The misses are Q05 and Q07: `routed=mdpf_get_model_benchmarks expected=query_v0:json/benchmarks/model_portfolio_benchmarks.json`.
  - That is R-13 working. The purpose-built tool reads EXACTLY the expected dataset. The harness still encodes the
    pre-R-13 route.
- **Granted for this fix only:** `infra/aws/ec2/opal-gateway/tests/routing/run_routing.py`.
  - The harness resolves a routed purpose-built tool to its catalog `portal_datasets` row's dataset key, through the
    row's `read_tool` + `accessor` and that accessor's channel key.
  - It then scores HIT when that key equals the expected key.
  - The question set (`questions.yaml`) is NOT edited.
  - `--plant-mislabel` must still drop the score by exactly one.
- Re-run AC1-AC3 on a tree that carries MX-t-9 (your worktree is fast-forwarded to CLOUD), and update the proof
  instance.

## 2. BOUNDS

1. The harness and its question set are READ, never edited.
2. No new catalog row and no new served surface. Keywords go on existing rows only.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
infra/aws/ec2/opal-gateway/tests/routing/run_routing.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/catalog_entries/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~14/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W14-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-d-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/d5.AC1.sh; echo "exit=$?"</invocation><expect>plain run rc=0 ROUTING k of 27 with k>=25 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-d-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/d5.AC2.sh; echo "exit=$?"</invocation><expect>catalog platinum/etfs mentions=0 and catalogued=False, or a platinum/etfs row first -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-d-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/d5.AC3.sh; echo "exit=$?"</invocation><expect>dataset asks routed first k of n with n>=3 and k>=2 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~14/NFRA_MCPINDEX.TO-MX-d-5.discover-routing-precision.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-3 analysis s.5 item 4. The issuer scoped the analysis's 'ETF dataset ask routes first 1 of 1' to what is reachable without widening (AC2's two states), because the catalog holds no platinum/etfs row and adding one is RESERVED to Andrew (DATA_CATALOG.yaml:32; RESERVED card to 1.0.0_SA_CTO~O).

<status>pending</status>
<round>4</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
