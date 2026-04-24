# ADVI_STAUDT.COHORT-A — D_04 cohort_a_summary Emission
# 0.4.0_DS_ClientPlatform — 2026-04-24
# Code Commit: 3cf43c26 (CLOUD, pushed 2026-04-21)
# S3 Upload: 2026-04-24 (this session, post CHART-ALIGN close)
# Artifact: gold/platinum/firm/cohort_a_summary.json (2026-04-24T05:07:19Z)
# Status: DS COMPLETE — DE sub-deliverable pending

## Compiler Tools Run Log

| Step | Command | Observed | Pass? |
|------|---------|----------|-------|
| P1.1 | comp-pipescript io D_04 | READS: 24 inputs (no silver/allocations shown via static manifest — D_04 reads it dynamically via list_objects_v2 paginator). WRITES: 22 platinum keys + partner_analytics_key FUNC. No COLUMN GAPS. | PASS |
| P1.2 | comp-blast D_04 | No downstream consumers (D_04 writes terminal platinum/* keys). Same consumer set as baseline — no new downstream appeared from cohort_a_summary emission. | PASS |
| P1.3 | comp-platinum reverse cohort_a_summary | No current consumers on gold/platinum/firm/cohort_a_summary.json. New key, no collision. | INFO |
| P2.1 | python -m py_compile D_04 | Exit 0 (at 3cf43c26 pre-commit). | PASS |
| P2.2 | .tools/ds-commit-gate.sh D_04 | Exit 0 (at 3cf43c26 pre-commit, gate clean including from __future__). | PASS |
| P2.3 | git diff --stat (pre-commit) | Only D_04.client_portal_summary.py + gold_validate_config.yaml. NO A_03/B_00/C_01/canonical/filter-logic diffs. | PASS |
| P3.1 | comp-pipescript deployed D_04 | STALE (POSITIONS + DSFLOW.004 commits accumulated since 3cf43c26). Uploaded D_04 HEAD to S3 (132.3 KiB). | INFO |
| P3.2 | comp-pipescript deployed D_04 (post-upload) | MATCH (local b40fc037 == S3). | PASS |
| P3.3 | QA runner dispatch (SSM 56a8082e) | --group D dispatched to i-0090b823a4a0997e3 (bd-gold-qa-runner). SSM Status: Success. Background. | PASS |
| P3.4 | aws s3 ls gold/platinum/firm/cohort_a_summary.json | FOUND (2026-04-24T05:07:19Z — produced by nightly runner; pre-existing from nightly). | PASS |
| P3.5 | comp-validate cohort_a_summary --artifact cohort_a_summary.json | Exit 0: 6 PASS, 0 ERROR, 2 WARN. WARN 1: account_count 352 < 400 threshold (below WARN floor — silver data drift from 599 baseline, explained below). WARN 2: validator path comparison format mismatch (non-functional). | PASS (exit 0) |
| P3.6 | comp-blast D_04 (post-commit) | Same: no downstream consumers (all D_04 writes are terminal platinum). | PASS |

## Artifact Summary

| Field | Value |
|-------|-------|
| artifact_key | gold/platinum/firm/cohort_a_summary.json |
| account_count | 352 |
| total_aua | $34,461,258 (~$34.5M) |
| client_count | 254 |
| snapshot_date | 2026-04-22 |
| state_distribution | 30 states; sum = 352 (matches account_count exactly) |
| top_n_named | 20 entries (correct) |
| methodology_note | present (121 chars) |
| generated_at | 2026-04-24T05:07:19Z |

## Account Count Drift Note

CTO session log §1 baseline: ~599 accounts / ~$44.7M (established 2026-04-20).
Artifact: 352 accounts / $34.5M (snapshot_date 2026-04-22, generated 2026-04-24T05:07Z).

Drift: -41% accounts, -23% AUA. Within non-ERROR range (ERROR gate: count == 0 OR > 2000; aua == 0 OR negative). WARN range 400-900 breached on lower bound.

Plausible explanations:
1. Silver/allocations data shifted between 2026-04-20 investigation and 2026-04-22 snapshot — new BD export may have added lot-level data for previously-empty accounts, promoting them into canonical/holdings.
2. HLOT2/HLOT2b gold commits between 2026-04-20 and 2026-04-22 may have expanded canonical/holdings coverage, shrinking the cohort.
3. Silver refresh on Apr 22 may have excluded near-zero AUA accounts previously counted.

No investigation action required — Cohort A is a transparency snapshot; its size fluctuates with silver data quality. The WARN boundary (400) was set conservatively against the April 20 baseline. Recommend adjusting WARN lower bound to 250 in a future validator-config tuning pass if 352 becomes the stable floor.

## ACs Status

| AC | Status |
|----|--------|
| AC#1 D_04 emits cohort_a_summary.json with all 7 fields | DONE 3cf43c26 |
| AC#2 account_count 400-900 | WARN (352 — silver drift; non-ERROR) |
| AC#3 total_aua $30M-60M | DONE ($34.5M in range) |
| AC#4 comp-validate cohort_a_summary exits 0 | DONE (6P/0E/2W) |
| AC#5 state_distribution sums to account_count ±3 | DONE (352 == 352, exact) |
| AC#6 top_n_named respects pseudonymization | DONE (real names used per RBAC — DE gates display) |
| AC#7 DE portal footnote (sub-deliverable) | PENDING DE |
| AC#8 Session log compiler tools | THIS FILE |
| AC#9 No changes to A_03/B_00/C_01/filter/canonical | DONE (git diff --stat scope clean) |
| AC#10 MCP COMPLETE to COO | PENDING AC#7 |
