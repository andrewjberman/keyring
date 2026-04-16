# 0.4.0_DT Session Log — ADVI_ROLLUP.IN-2.W0.002 watermark + atomic_write helper lib

**Agent:** 0.4.0_DT_ClientPlatform
**Date:** 2026-04-15 ET (evening)
**Task Order:** `ADVI_ROLLUP.IN-2.W0.002` (staged -> pending -> complete)

---

## Objective recap

Ship the two helper modules every IN Wave 1-5 per-script conversion will consume:
- `data/black_diamond/scripts/gold/_lib/watermark.py` — canonical Watermark dataclass + load/save/upstream_changed + migration readers for legacy B_00 + C_06 formats.
- `data/black_diamond/scripts/gold/_lib/atomic_write.py` — staging-then-promote S3 write (PRD Section 4).

Plus pytest coverage + `docs/data/watermark_contract.md` reference.

## Files

**New:**
- `data/black_diamond/scripts/gold/_lib/__init__.py`
- `data/black_diamond/scripts/gold/_lib/watermark.py`
- `data/black_diamond/scripts/gold/_lib/atomic_write.py`
- `tests/gold_lib/__init__.py`
- `tests/gold_lib/test_watermark.py` (12 cases)
- `tests/gold_lib/test_atomic_write.py` (4 cases)
- `docs/data/watermark_contract.md`

**Modified:** TO status staged -> pending -> complete.

No S3 writes, no Lambda deploys, no Terraform, no EC2. Pure library + tests + docs.

## Design decisions worth capturing

- **Module boundary:** all S3 I/O goes through an injectable `s3` client argument defaulting to `boto3.client("s3", region_name="us-east-1")`. Lets tests substitute a fake client without monkeypatching boto3 globally.
- **Migration readers are one-way:** writes always use the new schema. Legacy keys continue to be readable for the transition window; each successful `save_watermark` in a script's adopter TO implicitly migrates that script's format.
- **`upstream_changed` is tolerant of legacy upstreams:** if an upstream watermark is only in a legacy location, it is still read + hashed, so a late-migrating upstream doesn't force a false-positive rebuild. Missing watermarks (no new and no legacy) return True so first runs safely rebuild.
- **`compute_input_hashes` complements `upstream_changed`:** provides the dict you save on your own watermark right after a real run so subsequent runs can compare.
- **Atomic write:** PUT `{key}.staging` -> CopyObject -> Delete. S3 has no native rename; CopyObject is atomic at the object level, which is what the PRD's staging-then-promote rule actually guarantees.
- **`Watermark.to_json_bytes` sorts keys + uses compact separators** so hashing two identical-content watermarks always yields the same sha256 regardless of dict iteration order.

## Compiler Tools

| Phase | Tool | Result | Note |
|---|---|---|---|
| Before write (Phase 1) | `grep -rn 'CANONICAL_HOLDINGS_WATERMARK\|CLIENT_TIMESERIES_WATERMARK' data/black_diamond/scripts/gold/` | OK | Located usage sites: `B_00.canonical_holdings.py` (load/save `sealed_dates` format), `C_06.client_mix_timeseries.py` (`data_as_of` format), `lib/s3_layout.py` (key constants). Baselined migration reader surface. |
| Before write (Phase 1) | `comp-pipescript io C_06` | OK | Confirmed C_06 reads `CLIENT_TIMESERIES_WATERMARK` as input + writes own watermark. Gave the reference implementation for the migration reader (`{"data_as_of": "YYYY-MM-DD", "relationship_count": N}`). |
| Before commit (Phase 2) | `pytest tests/gold_lib/ -v` | 16/16 PASS | All API functions + migration-compat readers + atomic-write staging/promote ordering. |
| Before commit (Phase 2) | `python -m py_compile .../watermark.py .../atomic_write.py` | PY_COMPILE_OK both modules | Clean. |

No Lambda deploys, so no `comp-iam`. No portal components, so no `comp-transform`. No CloudFront, so no `comp-routes`.

## Acceptance Criteria Audit

1. Both modules exist with API exactly per PRD Section 3 + Section 4 — **OK**
2. Unit test coverage: all API funcs + migration-compat readers; pytest PASS — **OK (16/16)**
3. Watermark schema JSON-schema compliant (all required fields present on write) — **OK** (test_watermark_schema_jsonable enforces the required-field set on the serialized body)
4. `atomic_s3_write` uses `{key}.staging` intermediate; atomic rename via CopyObject + DeleteObject — **OK** (test_atomic_write_uses_staging_intermediate + test_atomic_write_final_body_matches_input + test_atomic_write_leaves_no_staging_on_success)
5. Migration readers emit `DeprecationWarning` — **OK** (both legacy-reader tests assert the warning)
6. `docs/data/watermark_contract.md` — **OK** (short reference doc for Wave 1-5 TOs)
7. Session log Compiler Tools section reproduces every run + observed + pass/fail — **OK (this doc)**
8. MCP COMPLETE to COO + CTO — pending after commit

## Current State

- `_lib/watermark.py` + `_lib/atomic_write.py` written; 16/16 tests pass; both modules py_compile-clean.
- `docs/data/watermark_contract.md` written as per-script adoption reference.
- W0.002 TO flipped to `<status>complete</status>`.
- No commit yet — about to stage + DT-author commit + MCP COMPLETE.

## Next Steps

- Commit (scoped with `--only` to the files listed above + this log + TO status flip).
- MCP COMPLETE to COO + CTO with module paths, test count, docs path.
- Flip W0.003 staged -> pending; begin comp-incrparity tool (gated on W0.002 landing, now unblocked).
