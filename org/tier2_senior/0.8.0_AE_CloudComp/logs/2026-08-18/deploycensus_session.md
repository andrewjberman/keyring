# Deployed-vs-Built-From Census: 197 Lambdas + 27 EC2 services classified, controls both directions, one immediate-report finding — 0.8.0_AE_CloudComp

**Date:** 2026-08-18
**Task Order:** NFRA_DEPLOYCENSUS (project NFRA_COMPRAIL) — deployed-vs-built-from census, CLASSIFY don't fix
**Status:** COMPLETE

---

## Objective

Execute the Andrew-authorized (08-18 ~1500Z, item iv pull-forward) Rule-22a CODE-layer census: for every code-carrying deploy, diff DEPLOYED bytes against THE SOURCE THE ARTIFACT IS BUILT FROM (resolved through the build input, never by filename), plus the EC2 staged/on-box split and the bundled-vs-canonical axis. One bounded read, classify-only, zero fixes.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "compare deployed lambda package bytes against the source it was built from"` | WARN | near-tie (comp-aws/comp-estate/comp-iam), none covers member-sha deployed-vs-built-from — coverage gap noted, census instrument justified at BUILD-LADDER rung 7 |
| comp-pipescript deployed | no-arg all-trees sweep | PASS | 60/60 bd-gold MATCH; inf INF_D_02/04/10 STALE + aux DRIFT rows — cross-checked CONSISTENT with my independent staged-byte reads on every overlapping row (shared-derivation caveat does not apply: different derivations, byte-hash vs its own comparator) |
| comp-find | `--name build_billing_dim.py` / `build_tax_dim.py` / `EC2_MANIFEST.json` / `*value_parity*.tf` / `*proof*spec*` | PASS | 2-homes seed for the bundled predicate, denominator lines carried |
| proof-of-spec-check | positional ids DC-1..DC-6 | PASS | rc=0 VALID (after declaring the instrument-scripts exclusion) |

**What worked:** comp-pipescript deployed as the gold-script half (reuse, not rebuild); comp-find's HEAD-band for canonical-home resolution.
**What failed:** nothing silently; comp-which correctly refused to pretend coverage.
**Gap found:** no comp-tool reads deployed Lambda package MEMBER hashes vs build-input-resolved source — the exact Rule-22a CODE read. The census scripts in the deliverable dir are a re-runnable stopgap; a `comp-*` home for this read is a coverage-gap candidate for CTO routing (comp-tooling is foundational, per Rule 22).

---

## What was done

1. **Lambda axis (197 map entries):** all 188 live packages downloaded (get-function → Code.Location), every member sha256/git-blob hashed, resolved through the BUILD INPUT by shape: BUILD_MANIFEST.json (assembled/pinned), inline archive_file (TF dir zip), nodejs transformed build (provenance chain), source_dir+files[] (build-and-upload convention). Discriminators: cosmetic-only (AST minus docstrings), strings-only (AST with string constants masked — separates the 06-11 path-sweep class from code drift), hold-statement scan over post-vintage commit messages, deployed-blob-in-path-history vintage dating, working-tree/other-path attribution.
2. **EC2 axis (27 services):** declared staging enumerated + byte-compared (~460 code objects), instance state + SSM reachability materialised, on-box APPLIED reads via read-only SSM hash commands on all 5 Online boxes. No instance started, no writes.
3. **Bundled-vs-canonical axis:** every package .py member matched against canonical `data/*/scripts|lib|tools` homes (vendored-dir + name-collision filtered, similarity-scored): 17 diverged bundled-copy findings across 14 Lambdas (+1 three-homes row).
4. **Controls (TO-mandated, both printed):** negative smartx-jwt-refresher → CURRENT; positive inf-silver-chain → TWO-HOMES-DIVERGED on build_billing_dim (sim 0.345). Instrument discriminates.
5. **Immediate-report clause exercised once:** bd `merge-daily-incremental.py` two-staging-homes (scripts/ = 4 commits stale, EXECUTING daily via ENABLED EventBridge→SSM docs at lines 42-43; code/silver/ = CURRENT). COO 160830Z, ACK+routing 161035Z (no change tonight, deliberate; remedy at CTO).

## Deliverables

- `deliverables/NFRA_DEPLOYCENSUS/CENSUS_REPORT_20260818.md` — the full DC-1..DC-6 report
- `deliverables/NFRA_DEPLOYCENSUS/{lambda_census_v3_findings.json, lambda_census_v3_summary.json, ec2_census_v2_rows.json, ec2_onbox_verdicts.json}` — machine evidence
- `deliverables/NFRA_DEPLOYCENSUS/INSTRUMENTS_APPENDIX.md` — the re-runnable instruments as fenced listings (raw .py correctly refused by the Rule-14 ruff gate; --force does not bypass a gate failure) *(corrected same-session: this line briefly named raw .py files)*
- `deliverables/NFRA_DEPLOYCENSUS_PROOF_OF_SPEC.json` — VALID rc=0 against DC-1..DC-6

## Headline counts

Lambdas: **CURRENT 141 · DELIBERATELY-HELD 11 · STALE-BY-NEGLECT 8 · TWO-HOMES-DIVERGED 16 · UNREAD 21** (of 197; 6 live-not-in-map named). EC2 staged: CURRENT 6 · STALE 6 · TWO-HOMES 3 · UNREAD 12; on-box: 5 read / 22 UNREAD named. "How many more two-homes": **~20 distinct relationships** beyond the three known.

## Discipline note

Zero deploys, zero fixes, zero staging writes. Estate mutations this session: none (SSM invocations were sha256sum/Get-FileHash/schtasks-query/ls only). Immediate finding surfaced same-turn, not held.

---

# ADDENDUM (same session): MDPF_REMED.RP-F2 — eclipse/orion run-date consumer census — COMPLETE

**Task Order:** MDPF_REMED.RP-F2 (GO 2.0.0_SA_COO 08-11T004612Z, executed on respawn after the Andrew-direct DEPLOYCENSUS closed)

## Compiler Tools (RP-F2 mandate, phase-by-phase)
| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | "who reads eclipse/orion date= partitions" | PASS | routed comp-estate/comp-pipescript near-tie; predicate composed from comp-kuzu + comp-find per the TO's own tool list |
| comp-kuzu | show_tables + table_info + eclipse/orion CloudEdge match | PASS | provenance header read (built 16:03Z, Nessie HEAD current); corroborated writers/triggers; FOUND 2 stale template nodes (opal-data-mdpf silver/gold eclipse) that are EMPTY live — graph-vs-live discrepancy named in the deliverable §5.4 |
| comp-find | 'eclipse/inflection' / 'orion/inflection' / 'silver/eclipse' / 'gold/eclipse' | PASS | stage-1 localization with denominators (627/7501/224/176 over 26,505 files); band split separated scratch/doc noise from source |
| scripted stage-2 (rail-checked) | P1+P2 scans over 5,645 HEAD executable/config files | PASS | 43 + 34 hit files -> 11 offset-relevant consumer rows + ~25 n/a rows |

**Gap found:** none new (the deployed-member-sha gap already routed via DEPLOYCENSUS).

## Result
Validity gate PASS — all 4 known members surfaced independently; mdpf_aggregate_aua required extending the predicate to the F2 feed family (fixed the predicate, not the list, exactly as the TO ordered). 11 offset-relevant rows: 1 corrected-by-W1 (dim_mdpf_aggregate_aua_timeseries, deployed-verified via the same-day DEPLOYCENSUS package read), 6 uncorrected (dim_mdpf_account_distribution, wsc_inflection_held_etf, build_mdpf_wsc_inflection_feeder, INF_E_00, opal-assets-daily-emitter channel_sources, smartx-exporter workspace legacy gold/eclipse reader), 1 uncorrected-at-HEAD/inert-deployed (inf-etf-ownership-daily), 3 inherited (mdpf_aggregate_aua, generate_smartx_timeseries, compute_*distribution — remedy belongs at the feeder's stamp). VintageContradiction 4-link chain rowed with the W1 fix at its END. Zero code changes. Deliverable: deliverables/MDPF_REMED_RPF2_ECLIPSE_ORION_CONSUMER_CENSUS_20260818.md.
