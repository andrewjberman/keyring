# work 2300Z — FIND_INSURE.007 Rule 17 silver passthrough patch (5 dropped bronze meta fields)

**archetype:** IMPLEMENT

## Summary

Patched `data/find/imo/scripts/silver/parse_web_silver.py` to preserve 5 bronze meta crawler-process diagnostic fields previously dropped from both `build_silver_record` (SUCCESS path) and `build_blocked_record` (BLOCKED path), restoring CLAUDE.md Rule 17 compliance.

Closes FIND_INSURE.007 (`org/tier2_senior/0.1.0_DS_MarketIntelligence/task_orders/FIND_INSURE.007.dsa-rule17-silver-passthrough-patch.md`) per ws COO /drive cycle 165 GO 22:59Z + MSTR SPAWN-WITH-DIRECTION 22:50Z. Closes the (b)(ii) execution leg of CVO REPAIR-AMENDMENT-AUTHORIZED from `verify_channel_FIND_INSURE_andrew_mandate_2050Z_11_axes.md` §S1 Rule 17 sub-finding.

## Authority chain

- Andrew sovereign goal-set 2026-05-27T~22:49Z ("drive end-to-end FIND_INSURE through Phase 3 close")
- CVO 11-axes verdict `54ace66c8` §S1 grade C + REPAIR-AMENDMENT-AUTHORIZED (b)(ii) 21:00Z
- ws COO /drive cycle 165 Phase 1 close-gating triad → GO at 22:59Z
- MSTR SPAWN-WITH-DIRECTION at ~22:50Z (substance executed pre-GO via spawn directive; formal TO close routed via COO RAVC2 chain)

## Substance

The 5 fields now preserved end-to-end bronze → silver (positioned between `last_modified`/`content_type` and `bronze_key` per AC2/AC3 readability hint):

| Field | dtype | Load-bearing for |
|---|---|---|
| `http_headers` | dict\|None | Bright Data `x-brd-error*` diagnostics; carl-ostenson empty-body root-cause class |
| `crawl_depth` | int\|None | Crawler tree-depth audit |
| `robots_txt_compliance` | bool\|None | Legal/ethics audit |
| `scheme_fallback` | str\|None | https→http fallback flag |
| `tls_fail_original` | bool\|None | TLS error flag (AC-T2 EMPTY-BODY classification refinement) |

Strict Rule 17: `metadata.get(<field>)` passthrough — no transformation, no fillna, no dtype coercion. If bronze meta is missing a field (legitimate schema drift), silver carries `null` verbatim (AC4).

## Acceptance criteria — status

- **AC1** PASS — `from __future__ import annotations` first import; ds-commit-gate clean; ruff 0.15.11 `--target-version py39` clean
- **AC2** PASS — SUCCESS path 16 fields → 21 fields (additive)
- **AC3** PASS — BLOCKED path appends same 5 fields; carl-ostenson anchor preserved
- **AC4** PASS — strict Rule 17 passthrough; `metadata.get()` returns `None` on absence
- **AC5** PASS — no signature regression; gold consumers read existing keys, new fields ignored as unknown
- **AC6** PASS (this session, live S3) — local invocation of `parse_imo` against 3-IMO bronze:
  - 10 SUCCESS records emitted (5 avantax + 5 atlantic) carrying all 5 Rule-17 fields with non-null bronze-meta values
  - 1 BLOCKED record (carl-ostenson) carries `http_headers` dict (8 keys) including `x-brd-error-code = "net_err_cert_common_name_invalid"` — the canonical TLS-cert-mismatch root-cause that was previously dropped at silver
  - Totals: 11/11 records (matches FIND_INSURE.005 AC8 baseline)
- **AC7** DEFERRED to AE 0.7~A — Lambda Terraform redeploy + tag `imo-pipeline-v0.3.1` is AE-owned per Rule 1 (Terraform-only Lambda deploy). Source code shipped; live-Lambda parity requires AE redeploy.
- **AC8** PASS — `python parse_web_silver.py` self-test 46/46 OK including 10 new Rule-17 assertions (5 success-path + 5 blocked-path)
- **AC9** KNOWN-NOT-CORRECTNESS — `comp-pipescript io` returns "Unknown script" for `parse_web_silver.py` (comp-graph rebuild lag per .005 precedent; tooling-not-correctness)

## Ship evidence

- Code commit: `3ee6ee869` on origin/CLOUD
  - `data/find/imo/scripts/silver/parse_web_silver.py` (+39 lines, 1 file)
  - Author: `0.1.0_DS_MarketIntelligence~A`
  - Push: clean (safe-deploy hook no-op — Lambda-bundled file, AE owns Terraform)
- AC6 live S3 evidence:
  - `s3://opal-data-imo/corp/carl-ostenson/silver/web-scrape/2026-05-27/7fe8d70daaa829f2.json` carries `http_headers["x-brd-error-code"] = "net_err_cert_common_name_invalid"`
  - `s3://opal-data-imo/corp/avantax-wealth-management/silver/web-scrape/2026-05-27/<5 records>.json` carry `http_headers` dict[17 keys], `crawl_depth=1`, `robots_txt_compliance=True`
  - `s3://opal-data-imo/corp/1st-atlantic-insurance-group/silver/web-scrape/2026-05-27/<5 records>.json` likewise carry 5 fields populated
- Self-test: 46/46 OK at HEAD `3ee6ee869`

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `.tools/ds-commit-gate.sh` | PASS | py_compile + AST + ruff 0.15.11 — gate per Rule 14 |
| `python parse_web_silver.py` (self-test) | 46/46 OK | Added 10 new Rule-17 assertions (5 success + 5 blocked) |
| `comp-pipescript io` | "Unknown script" | Comp-graph rebuild lag; tooling-not-correctness per .005 precedent (AC9) |
| `.tools/safe-commit.sh` | clean | Single-file scoped pathspec (Rule 14a) |

## Cross-coord

- Sister DS~E silver-gold contract ref doc `180b4c21e` was anchored on pre-patch HEAD `b67ad03ec` — sent [sister-coord ACK] flagging the 5 new fields as v0.2 documentation-fix amendment fodder (additive schema, no retroactive cycle needed).
- AE 0.7~A: AC7 deferred — find-insure-lambda parse-web bundle needs Terraform redeploy for live-Lambda parity. Surface to ws COO for SYNC handoff timing if needed for Phase 1 close gate.

## Sequencing actual

| Phase | ETA target | Actual |
|---|---|---|
| Read CVO + .005 + bronze schema | ~5min | ~3min |
| Patch + extend self-test | ~10min | ~3min |
| ds-commit-gate + ruff + py_compile | ~5min | ~30s |
| Local 3-IMO invocation + spot-check | ~5min | ~1min |
| AE deploy parity (AC7) | ~10min | DEFERRED to AE |
| Commit + RAVC2 | ~5min | ~2min |
| **Total** | ~30-60min | ~10min substance + AC6 |

## Per LD-0116 notes

- Routed substantive close via ws COO (RAVC2-Request); CC ws CTO + ws CVO; CC MSTR is awareness-only per Article-VI sharpening (Tier-2/3 ↔ MSTR direct comms via T1 chain).
- /work 20m primary loop armed; standing by for COO RAVC2 close-ack + AE 0.7~A AC7 follow-on if Phase 1 close needs live-Lambda parity.

— 0.1.0_DS_MarketIntelligence~A 2026-05-27T~23:00Z
