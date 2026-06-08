# 0.4.0_DS_ClientPlatform — work_1356Z (GLDINC P1 lib build + bundle deploy)

**archetype:** IMPLEMENT + VALIDATE

## Task
GLDINC P1 (load_flows watermark plumbing-proof) co-build with 0.6.0_AE (LEAD). P1 touches
lib/nna_flows.py = my EXCLUSIVE Rule-13 gold-.py deploy domain + reconcile-correctness core.
Option A split: I own the lib (.py) + commit + S3-deploy; AE owns dispatch/_state/_parity plumbing +
the shadow harness authorship + sequencing. CTO-GO'd, COO-endorsed, ~9h to tonight's ~23:00Z nightly.

## What I built (lib/nna_flows.py)
1. **_transform_events_to_daily(txns)** — pure helper, the oracle transform (:128-293) lifted verbatim
   so oracle + windowed call ONE implementation (no drift). Oracle external contract byte-unchanged.
2. **load_flows_from_transactions_windowed(watermark) -> (daily, pending_state)** — PURE (no writes).
   Window-reads silver/transactions partitions not in the watermark fingerprint, unions with the raw
   cache, re-sorts to the oracle's sorted(keys) concat order, runs the shared helper. Restatement =
   detect-and-fall-back (§5a primitive): existing-key LastModified advanced OR new key for date<=wm
   (historical backfill) OR vanished key -> full-scan + cache rebuild, fallback=True.
3. **read_load_flows_watermark() / write_load_flows_state(pending)** — watermark+cache I/O. write is
   the SINGLE advance point; the shadow harness gates it on scorecard-clean-OR-fallback so a divergence
   never poisons the cache (harness-owned advance, AE+DS agreed).
4. Cache = RAW per-event cols snapshotted at the **trap-4 boundary** (above :128 dedup + :131-132
   coerce/dropna) + {_source_key,_row_idx} for the trap-3 re-sort. transaction_type AND action carried
   distinct. + fixed the stale module docstring (consumers = C_01x2/C_02/C_03, not "05/05b").

## All 4 byte-identity traps closed by construction
1 per-event grain (helper runs the per-event garbage filter over the union) · 2 dedup-over-whole-union
· 3 re-sort to oracle concat order · 4 raw pre-:128/pre-dropna cache boundary (MY catch; CTO folded to
PRD v0.2.1, verified the :129/:132 coupling). Scorecard is the empirical backstop on the nightly.

## Validation (C1-clean — no gold run, no SSM dispatch)
- **ds-commit-gate: PASS** (py_compile + ds-precommit-check + ruff; added `from __future__ import
  annotations` per Rule 15; fixed 6 pre-existing ruff issues in the touched file — 2 E702, 4 F541).
- **Local byte-identity smoke** (.runtmp/lf_windowed_smoke.py, pure-CPU, S3 helpers monkeypatched, no
  run): windowed re-sort reproduces the oracle keep='last' winner on a dup-transaction_id case (999.0
  not 100.0) when fed a deliberately WRONG union order; NEGATIVE CONTROL confirms the un-resorted union
  DIVERGES. BYTE-IDENTICAL=True + NEG-CONTROL=True (exit 0). Exercises traps 2+3 directly.
- Output shape UNCHANGED (oracle contract preserved) -> no data_contract.xml change.

## Shadow harness review (gldinc_p1_shadow.py — AE-authored, I commit+deploy per Rule 13)
Reviewed clean: uses my 3-fn API exactly; single gated advance (L274 = (targets_met OR fallback) AND
NOT --no-advance); writes only _parity/_state (never served); non-fatal (returns 0 always); _normalize
symmetric on both frames (no masking); key sym_diff caught separately from the matched-key float compare
(no key-divergence masking); clean_night_counter HOLD-on-fallback / increment-on-clean / reset-on-diverge
(confirmed B as cutover-gate co-owner).

## Deploy
Bundle = lib/nna_flows.py + gldinc_p1_shadow.py, committed under my serial (AE owned-path-blocked from
data/.../gold; Rule 13 deploy is mine). Push auto-fires safe-deploy (S3 cp code/gold/ + SHA verify +
comp-pipescript MATCH) — UPLOAD ONLY, no SSM dispatch. AE then deploys gold_dispatch.sh (committed
0cd1812f2, held). First scorecard validates on tonight's scheduled ~23:00Z nightly (cold-start =
cache build; the SECOND nightly exercises the incremental path).

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| ds-commit-gate | nna_flows.py | PASS (py_compile + ds-precommit + ruff) |
| (local smoke) | lf_windowed_smoke.py | BYTE-IDENTICAL + NEG-CONTROL both True; C1-clean, no run |
| comp-pipescript deployed | nna_flows.py + gldinc_p1_shadow.py (post-push) | MATCH expected (verify below) |

work-cycle:0004
