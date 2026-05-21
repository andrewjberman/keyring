# Session Log — YALP_MDSRC.F6 FRED-vs-Bloomberg merge spec

| Field | Value |
|---|---|
| Agent | 0.2.0_DS_PortfolioAnalytics~A |
| Date | 2026-05-21 |
| Task Order | YALP_MDSRC.F6 (dsa-fred-bloomberg-residue-merge-spec) |
| Status | COMPLETE — merge spec shipped; RAVC2 to COO CC CTO |

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| F6 merge spec | docs/briefs/mdsrc-f6-fred-bloomberg-merge-spec-20260521.md | CTO (v0.4) / COO (RAVC) / merge-implementation follow-on TO |

## What was done

Specced the FRED-vs-Bloomberg-residue merge — the integration step F4 flagged for
v0.4. How the F4 FRED artifact (51 indicators, macro_data_fred.json) and the Bloomberg
residue (29 indicators) combine into the page's consumed macro_data.json with no
dual-writer.

## Headline recommendation

The design is driven by a cadence tension: FRED is daily, yang-generate-macro is weekly
(data_pkl cadence). So the merge producer CANNOT be yang-generate-macro, or FRED data
sits 6/7-days stale. Recommended (Option b):
- yang-generate-macro: one-line output-key change -> json/macro/macro_data_bloomberg.json
  (still emits all 79; weekly). Stops being the macro_data.json writer.
- ingest_fred_macro.py (F4): unchanged -> macro_data_fred.json (daily).
- NEW daily merge step: reads both intermediates, writes json/macro/macro_data.json --
  the SOLE writer. No key has two writers => no dual-writer.
Reconciliation: FRED wins for the 51, Bloomberg for the 29 residue; boundary = set
membership in macro_data_fred.json (not a duplicated static list -> no drift).
Graceful degradation: if the FRED artifact is missing/stale (>3d) the merge falls back
to all-Bloomberg + logs loud -- fail-safe for the page, fail-loud for ops.
Cutover: 3 stages -- FRED pull live (F5) -> merge step in shadow writing a staging key
(parallel-run gate: 29 residue byte-identical, 51 FRED show F4 fidelity deltas) ->
atomic 3-key flip in ONE deploy (zero transient dual-writer). Single-revert rollback.
Post-merge the page grows 79 -> 80 (S&P CoreLogic restored from FRED; heatmap renders
dynamically -> no FE change).

## Files Modified

| File | Change |
|------|--------|
| docs/briefs/mdsrc-f6-fred-bloomberg-merge-spec-20260521.md | NEW — F6 merge spec |
| org/tier2_senior/0.2.0_DS_PortfolioAnalytics/task_orders/YALP_MDSRC.F6.dsa-fred-bloomberg-residue-merge-spec.md | status pending -> complete |
| org/tier2_senior/0.2.0_DS_PortfolioAnalytics/logs/2026-05-21/yalp_mdsrc_f6_fred_bloomberg_merge_spec.md | NEW — this log |

No code / Terraform / Lambda / portal file changed — F6 is a spec; the reference merge
implementation is deferred to a follow-on DS-author/AE-deploy TO (spec §7).

## Compiler Tools

| Tool | Command | Result | vs expect |
|------|---------|--------|-----------|
| comp-routes | `comp-routes behaviors` | behavior 16 /api/general/* -> S3 opal-data-portal-v2 | MATCH — anchors the merge step's CloudFront invalidation path + the served-key identity |
| comp-pipescript | `comp-pipescript io yang-generate-macro` | "Unknown script" — yang generators not comp-graph nodes | MISMATCH handled per TO if_mismatch — source-read fallback (F1/F4 reads of yang-generate-macro + ingest_fred_macro.py) |
| ds-commit-gate | n/a | no reference implementation .py authored | per TO compiler mandate phase 2 = documented-N/A |

## Next Steps

- [COO] RAVC2 — YALP_MDSRC.F6 complete; validate the merge spec.
- [CTO / v0.4] Consume the spec into the v0.4 FRED-architecture section.
- [COO, after F5 lands] Issue the merge-implementation follow-on TO (spec §7) —
  DS-author the merge step + AE-deploy.
