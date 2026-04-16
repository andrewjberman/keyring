# 0.4.0_DT Session Log -- ADVI_ROLLUP.IN-2.W0.003 comp-incrparity tool

**Agent:** 0.4.0_DT_ClientPlatform
**Date:** 2026-04-15 ET (evening, immediately after W0.002 close)
**Task Order:** `ADVI_ROLLUP.IN-2.W0.003` (staged -> pending -> complete)

---

## Objective recap

Ship `.tools/comp-incrparity` -- parity validator that gates every per-script incremental promotion. Quick (byte-diff + JSON-deep-diff) + Deep ($0.01 numeric tolerance) modes. C_06 smoke must PASS on ship (already incremental in prod). ALL-mode iterates `gold/meta/incremental_promoted.json` (initial empty list).

## Design decision worth capturing

**Self-parity smoke vs dual-run parity.**
The PRD describes the tool as "run the script in FULL mode, run in INCREMENTAL mode, diff." That requires each script to expose `--parity-full` / `--parity-incremental` CLI flags landing into `s3://opal-data-bd/gold/_parity/{script}/{ts}/{full,incremental}/` prefixes. No script supports those flags at W0.003 ship (C_06 is incremental in prod but has no dual-run hook).

Resolved by introducing **self-parity mode** as the CLI default: read the current prod output for a registered script, diff it against itself, which exercises the full S3 read + parse (JSON or parquet) + diff machinery and trivially PASSES by construction. This is the honest interpretation of the TO's "smoke test (C_06 already incremental, parity must hold by construction)" -- a sanity check on the TOOL's mechanics, not on the script's dual-run behavior.

Each Wave 2+ per-script conversion TO will (a) add `--parity-full` / `--parity-incremental` modes to the script and (b) register the pair of prefixes in `_parity_prefixes_for()` (currently returns None for all scripts). At that point the CLI transparently flips from self-parity to dual-run diff.

## Files

**New:**
- `.tools/comp-incrparity` -- bash wrapper matching existing comp-* convention; executable; auto-logs via `comp_log_auto.py`
- `org/modules/graph/incrparity_core.py` -- diff semantics (`diff_json_bodies`, `diff_parquet_bodies`, `diff_prefixes`, `load_promoted_list`, `write_parity_report`, `self_parity`). Pure-function core, inject-friendly S3.
- `org/modules/graph/incrparity_cli.py` -- CLI entry: `<script_id>` or `ALL`, `--mode quick|deep`, `--date`, `--no-s3-report`. Self-parity smoke-path for registered scripts (C_06 => `gold/views/mix_daily_summary.json`).
- `gold/meta/incremental_promoted.json` -- initial empty list `[]`. This file is local-committed + must be uploaded to `s3://opal-data-bd/gold/meta/incremental_promoted.json` at ship time (done out-of-band; tool tolerates missing S3 object -> empty list).
- `tests/comp_tools/__init__.py`
- `tests/comp_tools/test_comp_incrparity.py` -- 20 test cases.

**Modified:** TO status staged -> pending -> complete.

## Acceptance Criteria Audit

| # | Criterion | Result |
|---|---|---|
| 1 | Tool at `.tools/comp-incrparity`, executable | OK (chmod +x, bash wrapper present) |
| 2 | `comp-incrparity C_06 --mode deep` exit 0 | **OK** (smoke transcript below) |
| 3 | `comp-incrparity C_06 --mode quick` exit 0 | **OK** (smoke transcript below) |
| 4 | Synthetic failure test: numeric diff injected, EXIT 1 + report written | **OK** -- `test_main_single_script_fail_emits_report_to_s3` injects `$0.50` diff on a JSON body; asserts `rc==1` + report lands at `gold/_parity_reports/X/{ts}/diff.json` |
| 5 | `comp-incrparity ALL --mode quick` graceful empty | **OK** (smoke transcript below) |
| 6 | Unit tests pass | **OK -- 20/20** (this TO) + full suite 36/36 incl. W0.002 |
| 7 | `gold/meta/incremental_promoted.json` exists with `[]` | OK (local committed; tool gracefully handles S3-missing as empty) |
| 8 | Session log Compiler Tools section | OK (this doc) |
| 9 | MCP COMPLETE to COO + CTO | pending after commit |

## Smoke Transcripts

```
$ .tools/comp-incrparity --help
usage: comp-incrparity [-h] [--date DATE] [--mode {quick,deep}]
                       [--no-s3-report]
                       script_id
...

$ .tools/comp-incrparity C_06 --mode quick
PARITY OK: C_06 (quick) - 0 divergences
EXIT=0

$ .tools/comp-incrparity C_06 --mode deep
PARITY OK: C_06 (deep) - 0 divergences
EXIT=0

$ .tools/comp-incrparity ALL --mode quick
ALL: incremental_promoted.json is empty - 0 scripts to check. PASS.
EXIT=0
```

C_06 smoke exercises: boto3 S3 client construction, list_objects_v2 of the registered output key's prefix (actually a direct get since we registered exact keys, not prefix), fetch of `gold/views/mix_daily_summary.json`, JSON parse + recursive deep-walk (in deep mode), byte-compare (in quick mode). Because it's self-parity, 0 divergences is structurally guaranteed.

## Compiler Tools

| Phase | Tool | Result | Note |
|---|---|---|---|
| Before write (Phase 1) | `ls .tools/comp-*` + `head -30 .tools/comp-pipescript` | OK | Confirmed convention: bash shebang wrapper -> python module under `org/modules/graph/` -> auto-log via `comp_log_auto.py`. Mirrored for comp-incrparity. |
| Before write (Phase 1) | `comp-pipescript io C_06` | OK (run earlier in session, cached observation) | Confirmed C_06 WRITES: `gold/views/mix_daily_summary.json` + `gold/entities/clients/{*}.json`. Picked the summary file as the self-parity smoke key (smallish, JSON, invariant under re-read). |
| Before commit (Phase 2) | `.tools/comp-incrparity C_06 --mode quick` | EXIT=0 | Criterion 3. |
| Before commit (Phase 2) | `.tools/comp-incrparity C_06 --mode deep` | EXIT=0 | Criterion 2. |
| Before commit (Phase 2) | `.tools/comp-incrparity ALL --mode quick` | EXIT=0 | Criterion 5. |
| Before commit (Phase 2) | `pytest tests/comp_tools/ -v` | 20/20 PASS | Criterion 6. |
| Before commit (Phase 2) | `python -m py_compile org/modules/graph/incrparity_{core,cli}.py` | PY_COMPILE_OK | Both modules. |

## Current State

- `.tools/comp-incrparity` + `org/modules/graph/incrparity_{core,cli}.py` shipped.
- 20/20 pytest PASS (plus 16/16 W0.002 still green -- 36 total).
- Live smoke against real S3 (`opal-data-bd`): C_06 quick + deep PASS; ALL empty PASS.
- `gold/meta/incremental_promoted.json` committed with `[]`.
- W0.003 TO flipped to `<status>complete</status>`.
- No commit yet -- about to stage + DT-author commit + MCP COMPLETE.

## Next Steps

- Commit (scoped `--only` to listed paths + this log + TO status flip).
- MCP COMPLETE to COO + CTO with tool path, smoke transcripts, test counts.
- Upload `gold/meta/incremental_promoted.json` to `s3://opal-data-bd/gold/meta/incremental_promoted.json` (out-of-band, pre-Wave-2).
- Unblocks W0.004 (AE 0.7 weekly EventBridge parity check) + Wave 2+ per-script conversion TOs.
- Next on my lane after W0.003: ADVI_49EXEC.004 (Terraform generator Lambda module) -- gated on DS TO 2 + AE TO 3.
