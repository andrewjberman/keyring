# ADHC_VALGATE.001 Phase 4 — Class-C gate chain-wire (orion-gold-dispatch.sh)

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B (AE-side Phase 4 / AC5; the TO is DS~B-owned)
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform~B/task_orders/ADHC_VALGATE.001.ds-c1-c2-rowcount-distribution-gate.md`
**Commit:** `c683c4975` | **Verification run:** `chain_full_20260520_211919`

---

## Current State

- **ADHC_VALGATE.001 Phase 4 COMPLETE.** The DS~B Class-C gate (C-1 row-count + C-2
  classification-distribution) is chain-wired into `orion-gold-dispatch.sh` and verified
  firing on a real `--chain full` run. DS~B shipped Phases 0-3 (the gate machinery);
  this log attests Phase 4 (the chain-wire + verification).

## What shipped — the wire

A non-fatal v1 invocation of DS~B's `valgate_gate.py` added to `run_chain`'s loop in
`data/orion/scripts/gold/orion-gold-dispatch.sh`, fired immediately before `INF_09` (the
portal/platinum emit) -- i.e. post-D-chain / pre-platinum-emit, the Phase-0 placement:

```sh
if [ "$id" = "INF_09" ]; then
    echo "  [VALGATE-C] Class-C gate ... silver/transactions @ ${RUN_DATE}, pre-platinum-emit"
    if [ -f "$SCRIPTS/valgate_gate.py" ]; then
        python3 "$SCRIPTS/valgate_gate.py" --artifact silver/transactions --date "$RUN_DATE" \
            || echo "  [VALGATE-C] WARN: gate exited non-zero -- v1 WARN-not-BLOCK; non-fatal ..."
    else
        echo "  [VALGATE-C] WARN: valgate_gate.py absent ... skipped (non-fatal)."
    fi
fi
```

**NON-FATAL v1 wire (COO~B ruling 2026-05-20, option a).** A non-zero exit is swallowed
with a WARN -- the gate cannot block the platinum emit. Rationale: v1 is WARN-not-BLOCK
(PRD section 7-Q1); a v1 WARN-only gate, and especially its own infra error, must never
fail the chain. `valgate_gate.py` is not yet crash-safe -- an infra error exits non-zero,
ambiguous with a real BLOCK verdict -- so a literally exit-code-gated wire is unsafe in
v1 (surfaced + ruled before the wire; option a chosen).

## Deployment

| Step | Action | Result |
|------|--------|--------|
| 1 | Edit `orion-gold-dispatch.sh` -- VALGATE block in `run_chain` loop, pre-INF_09 | +25 lines, `bash -n` clean |
| 2 | Collision check | `orion-gold-dispatch.sh` carried uncommitted ADVI_INFALM.001 WIP -- HELD + surfaced to COO~B; base AE landed it (`d0a682901`); file clean at HEAD -> my commit scoped solo |
| 3 | `safe-commit.sh --only` | `c683c4975` (1 file, +25) |
| 4 | `git push origin CLOUD` | pushed |
| 5 | `aws s3 cp` -> `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` | uploaded; md5 local==S3 ETag MATCH (`ce0acf43...`) |

Gate scripts `valgate_gate.py` + `valgate_baseline.py` confirmed already on
`s3://opal-data-inf/code/gold/` (DS~B, 16:01Z) -- the runner's bulk-sync picks them up.

## Verification — AC5 (real chain run)

Triggered `inf-gold-trigger {"mode":"full"}` -> run `chain_full_20260520_211919` on
`i-0ed5afded2ebd4ed4`; ran 21:19Z->22:33Z (~74min, advancing throughout), status=COMPLETE.

Chain log `chain_full_20260520_211919.log` lines 29376-29396, verbatim:

```text
INF_D_04 done
  [VALGATE-C] Class-C gate (C-1 row-count / C-2 distribution) -- silver/transactions @ 2026-05-20, pre-platinum-emit
[VALGATE-C] artifact=silver/transactions date=2026-05-20 mode=bootstrap overall=SUPPRESSED
  C-1 [SUPPRESSED] bootstrap window -- baseline holds 0 sample(s), < N/2 (10); statistic recorded, verdict suppressed
  C-2 [SUPPRESSED] bootstrap window -- baseline holds 0 sample(s), < N/2 (10); statistic recorded, verdict suppressed
========================================
  INF_09  (INF_09.generate_partner_analytics.py)
```

**PASS, four ways:**
1. The gate fired AFTER `INF_D_04` (last D script) and BEFORE `INF_09` (platinum/portal
   emit) -- exactly the post-D-chain / pre-platinum-emit Phase-0 placement.
2. `valgate_gate.py` ran clean -- C-1 + C-2 both executed, no crash; verdict emitted to
   the chain log.
3. Verdict = `SUPPRESSED` (bootstrap) -- the baseline held 0 samples (< N/2 = 10), so
   per AC2's WARN-SUPPRESSED bootstrap the statistic is recorded and the verdict is
   suppressed. This run recorded the FIRST baseline sample; the window fills over the
   next ~20 daily runs, after which C-1/C-2 WARN on a breach. Correct cold-start behaviour.
4. The chain PROCEEDED to `INF_09` and completed (`CHAIN chain:full COMPLETE`) -- the
   non-fatal wire did NOT block the platinum emit.

## WARN -> BLOCK ratchet-readiness checklist (PRD section 7-Q1 follow-on)

v1 ships WARN-not-BLOCK. The ratchet to BLOCK -- after ~1-2 weeks of empirical
false-positive data -- is a **3-change sequence**, NOT a one-line flip (the
"one-line ratchet" was optimistic; `valgate_gate.py` is not crash-safe):

1. **Flip `GATE_VERDICT_POLICY`** in `valgate_gate.py` from `"warn"` to `"block"`.
2. **[HARD PREREQUISITE] Crash-safety in `valgate_gate.py`** (DS-lane, Rule 13 --
   `data/orion/scripts/gold/*.py`): wrap `main()`'s infra calls (`_read_partition_s3`,
   `run_gates`, the baseline-store read) so an infra error -> exit 0 with a **distinct
   named `INFRA-DEGRADED` terminal verdict** (NOT folded into WARN -- CTO~B refinement
   2026-05-20). Then a non-zero exit means ONLY a genuine BLOCK verdict, never a crash.
   The ratchet CANNOT proceed without this -- a future DS TO authored when the BLOCK
   ratchet is pursued.
3. **Flip the dispatcher wire** (this `run_chain` block) from non-fatal (`|| echo WARN`)
   to exit-code-gated/fatal (`|| { _chain_rc=$?; abort }`).

Steps 1+3 are small; step 2 is the gating DS deliverable. Until step 2 lands, the wire
stays non-fatal -- a v1 (or degraded) gate must never block the platinum emit.

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| Phase-1 read of `valgate_gate.py` / `valgate_baseline.py` / `orion-gold-dispatch.sh` | OK | CLI `--artifact/--date`; exit-code map (BLOCK->1 else 0); `run_chain` loop = the wire site. comp-pipescript io N/A -- the gate is read-only validation, not a producer. |
| `bash -n orion-gold-dispatch.sh` | clean | Local-runtime check (EC2-side dispatcher; Rule 16-exempt -- runs on Amazon Linux). |
| `comp-pipescript deployed` | N/A | Only models `opal-data-bd` gold/silver -- not the INF dispatcher. Deploy verified instead by md5 local==S3 ETag MATCH (`ce0acf43...`). |
| Verification chain run | PASS | `chain_full_20260520_211919` -- gate fired pre-INF_09, verdict SUPPRESSED-bootstrap, chain proceeded + completed. |

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 (CC DS~B + CTO~B) -- the full ADHC_VALGATE.001: DS~B Phases 0-3
  (commits `e0b21f60b` / `96b5cbd17` / `c26cffa10` / `d3ddd155e`) + AE Phase 4 (this log,
  `c683c4975`). On .001 accept, COO~B unstages VALGATE.002 (C-3) + .003 (C-4).
- `[future]` The WARN->BLOCK ratchet -- the 3-change sequence above; not now (awaits
  ~1-2 weeks of false-positive data + the crash-safety DS TO).
