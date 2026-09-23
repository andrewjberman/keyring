# Independent exact-dollar upload/create review

Reviewer `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
Candidate `386f2e1b495f629f4e53584566fd6a2aa2eae0cd`.
Baseline `bfe5a33e17486e01186bd97d3d8e801442485fad`.

**Y-D01 CLOSED for the exact-dollar upload/create boundary.** The producer's
original one-cent false reconciliation is independently reproduced at the
baseline and refused by the candidate. Supplied **19/19 tests PASS** and
**7/7 independent controls PASS**. No new defect in those controls; no full
Y4/S3 or integrated criterion grade follows.

## Evidence

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_recipe_decimal.py --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/RECIPE_DECIMAL_386f2e1b49.json
```

The probe materializes both exact Git pins and records their file SHA-256s.
Actual recipe.step_upload, recipe.step_create and transport multipart code run
with injected offline replies. Socket connections are explicitly forbidden in
the probe and supplied-suite subprocess. The notice provided no producer probe
file: the original source amount, echo amount, security and USD case were
recreated independently and kept identical across both pins.

| Independent control | Observed |
|---|---|
| Source S:AAPL USD9007199254740993.01, actual JSON echo9007199254740993.02 | Baseline ok/reconciled=true with binary-float echo9007199254740994.0; candidate ok/reconciled=false and no returned rows |
| Exact large-cent positive through upload, JSON checkpoint and actual step_create | CSV and multipart JSON preserve9007199254740993.01; unquoted numeric weighting and matching weight_text |
| One-cent positive through the same path | Exact0.01 preserved as JSON number |
| High-precision fraction positive through the same path | Exact0.1000000000000000000000000001 preserved as JSON number |
| Echo reorders S:AAPL and $:CASH rows | Exact typed identities and9007199254740993.01/123.45 preserved in actual create wire |
| Duplicate echo rows | Refused; no accepted rows |
| Duplicate source rows | RecipeRefused before any transport call |

Create positives call the real step_create, capture its POST payload for
`/model_portfolios/fixed/`, and parse both multipart fields. Numeric values are
parsed as Decimal and checked against source; strings would fail the type
check. The injected201 reply is only an offline response, not vendor acceptance.

The source repair parses JSON decimal tokens as Decimal, rejects nonpositive,
nonfinite and boolean dollars, reconciles unique typed rows exactly, retains
decimal text across a JSON checkpoint, and restores Decimal only at the numeric
serialization boundary. Supplied tests additionally cover invalid source/echo
values and nonfinite multipart refusal; their19 count is separate from the7
independent controls. Broader generation-suite success is producer-reported,
not rerun or added to these totals.

The three changed files and relevant recipe/transport call boundaries were
inspected; no full generation-worker audit is claimed. Local JSON serialization
is not a durable worker restart. No vendor/session, persistent server, runtime
assembly, browser, released report or READY proof was attempted. All fourteen
integrated criteria remain NOT_EVALUATED. Original unrelated closures remain.
Evidence is LOCAL; no implementation source changed by this reviewer.

-- 3.0.0_SA_CVO~Y
