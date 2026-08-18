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
- `deliverables/NFRA_DEPLOYCENSUS/{lambda_census_v3.py, ec2_census_v2.py, ec2_onbox.py}` — the re-runnable instruments
- `deliverables/NFRA_DEPLOYCENSUS_PROOF_OF_SPEC.json` — VALID rc=0 against DC-1..DC-6

## Headline counts

Lambdas: **CURRENT 141 · DELIBERATELY-HELD 11 · STALE-BY-NEGLECT 8 · TWO-HOMES-DIVERGED 16 · UNREAD 21** (of 197; 6 live-not-in-map named). EC2 staged: CURRENT 6 · STALE 6 · TWO-HOMES 3 · UNREAD 12; on-box: 5 read / 22 UNREAD named. "How many more two-homes": **~20 distinct relationships** beyond the three known.

## Discipline note

Zero deploys, zero fixes, zero staging writes. Estate mutations this session: none (SSM invocations were sha256sum/Get-FileHash/schtasks-query/ls only). Immediate finding surfaced same-turn, not held.
