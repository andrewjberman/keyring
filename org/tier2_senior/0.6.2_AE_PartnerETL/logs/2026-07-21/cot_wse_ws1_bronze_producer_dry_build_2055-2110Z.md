# WSE_COTMDL.WS1 -- bronze Rebalancer producer DRY BUILD

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, TRACE

**Agent:** 0.6.2_AE_PartnerETL · **Window:** 2026-07-21 ~20:55Z -> ~21:10Z · **TO:** WSE_COTMDL.WS1.bronze-rebalancer-producer (GO @761b2b86a, BUILD-phase-only)

## Summary

Executed the BUILD-phase-only GO from COO: dry-built + unit-tested `opal-assets-bd-rebalancer-daily-pull`, the WS-E WS-1 bronze producer that lands Cottonwood's BD Rebalancer model-portfolio data (the MDPF fold-in source) as raw JSON under `blackdiamond/cottonwood/bronze/`. Mirrors the `opal-assets-bd49f-*` producer structure; Rebalancer REST/JSON pull logic (not the DataMining xlsx path). 11 unit tests GREEN, commit-gate PASS. Committed @e55bcbb00, pushed. Scheduled pull HELD on the standing Andrew egress word + WS-5 role/schedule (both surfaced/coordinated).

## Work done

1. **Grounded the mirror pattern (read-only):** bd49f producer (`_request`/`_land`/complete-stamp/fail-loud), the CTO-ratified `landing_guard.py` (set-identity, listing-based, raises on shortfall AND surplus -- vendored verbatim), the C5 `smartx_client` (requests.Session + urllib3 Retry + `get_bytes` byte-for-byte + LOUD auth). comp-pipescript io does not cover a bronze producer -> grounded by source read.
2. **Built the producer** (`lambda_function.py`, 743 LOC incl tests): auth-mint off `blackdiamond/cot/session` (cookie in-memory only); 3 bronze pulls (models `strategies/search`, model_detail `GET /api/models/{id}`, accounts `accounts/search` take=200 paginated); RAW JSON (Rule 17a, no parquet); paginated types assembled LOSSLESSLY (every raw row preserved); firm-sep asserted on every write; **Sec.5 count-reconcile SELF-GATE fail-closed** (per-strategy accounts/search counts must equal roster accountCount; mismatch/orphan -> RAISE, no stamp); complete-stamp `meta/{date}-complete.json` LAST via the set-identity conservation guard.
3. **Design decisions (flagged to CTO):** (a) model-detail scope default `opal_closure` (Opal-named roster models + blend child-closure; honors Andrew's Opal ruling at the pull layer) with a `scope=all` knob; (b) paginated bronze = one lossless-assembled artifact per PRD filename (vs strict per-page byte-for-byte).
4. **11 unit tests GREEN** (dry, mocked client + in-memory S3, ZERO live egress): stamp-last, self-gate fail-closed blocks stamp, firm-sep refusal, pagination assembly, Opal child-closure (pulls non-Opal blend child USTX, excludes non-Opal standalone CS50), scope=all, orphan raise, unknown-mode fail-loud, landing_guard shortfall/surplus/identity.

## Compiler Tools (TO acceptance criterion #4 -- every <run> vs <expect>)

| Phase | Run | Result vs expect |
|---|---|---|
| 1a | `comp-iam service opal-assets-bd49f-daily-pull` (mirror role as pattern) | PARTIAL-AS-EXPECTED: pattern role holds s3:PutObject/ListBucket/GetObject on opal-data-assets; the NEW blackdiamond/cottonwood prefix reads UNRESOLVABLE-RESOURCE (comp-iam models action not (action,resource)) -> exact-ARN `simulate-principal-policy` is a WS-5 deploy gate (role doesn't exist yet; 0.7.0 owns it). Matches the TO if_mismatch path. |
| 1b | `comp-pipescript io opal-assets-bd49f-daily-pull` | N/A: "Script not found" -- comp-pipescript io targets gold pipescripts, not bronze producers. Grounded the mirror pattern (landing-guard + complete-stamp + firm-sep) by reading source instead (TO intent met). |
| 2 | `.tools/commit-gate.sh` on the 3 .py files | PASS (py_compile + ds-precommit + ruff py39; `from __future__ import annotations` present; caught 2 unused-import/var, fixed). |
| 2 | `python test_lambda_function.py` (dry unit tests) | 11 passed. |
| 3 | post-deploy `aws s3 ls .../cottonwood/bronze/` listing verify | DEFERRED to the live run (post standing-egress GO + WS-5 deploy). |

**What worked:** the vendored `landing_guard` gave the set-identity conservation guard for free (CTO-ratified, exercised in tests both directions). The Sec.5 count-reconcile self-gate is a genuine oracle -- a truncated-pagination test reproduces exactly the failure it's meant to catch. **What failed:** n/a. **Gap:** comp-pipescript io has no bronze-producer mode (only gold); comp-iam can't resolve a not-yet-created role's new-prefix grants (expected, Rule 22a covers it at deploy).

## Files Modified

- `infra/aws/lambda/opal-assets/opal-assets-bd-rebalancer-daily-pull/lambda_function.py` (new)
- `.../test_lambda_function.py` (new, 11 tests)
- `.../landing_guard.py` (vendored verbatim from etf, CTO-ratified)
- `org/tier2_senior/0.6.2_AE_PartnerETL/task_orders/WSE_COTMDL.WS1.bronze-rebalancer-producer.md` (staged -> pending)
- All @e55bcbb00, pushed CLOUD.

## Compliance

Zero live egress this session (mocked tests only; per-use grant spent, standing word pending). cot READ-ONLY design; cookie in-memory only. Firm-sep blackdiamond/cottonwood only (asserted in code + tested). No parquet at bronze (Rule 17a). No new alarm/twin (07-17 suspend). Source-map entry deliberately NOT added (undeployed = CI drift) -> deploy-time with WS-5.

## Blockers / Next Steps

- **[ANDREW]** standing vendor-egress word for the recurring pull (surfaced by COO) -- HARD gate before the scheduled pull activates.
- **[0.7.0_AE_CloudOps / WS-5]** scoped role (exact-ARN grants + firm-sep deny) + EventBridge schedule + source-map + layer -- coordination note sent; I'll pair on the TF/role.
- **[1.0.0_SA_CTO]** ratify the 2 design decisions (model-detail scope; paginated bronze shape).
- **[self]** DS (WS-2) notify pending first bronze land (per TO). IDLE/reachable for WS-5 pairing, CTO clarifications, or the next TO.
