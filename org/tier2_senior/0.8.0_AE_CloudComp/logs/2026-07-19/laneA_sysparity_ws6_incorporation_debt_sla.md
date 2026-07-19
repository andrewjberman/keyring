# NFRA_SYSPARITY WS-6 -- incorporation-debt SLA (the 8/8 closer) (0.8.0_AE_CloudComp~A)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Summary

COO GO'd WS-6 (@233031Z, refined TO @069157b64) after the WS-3c seed paused post-wave -- the SYSPARITY 8/8
CLOSER, sanctioned in-flight completion (MSTR "~A-after-WS-6"). Set an incorporation-debt SLA on the
NESTEDABSTRACT abstraction-ledger that converts it from a CALENDAR into a CONTROL. Designed + COO-confirmed
(N=14/M=60) + built + exercised both LD-0318 conditions + landed @5e85e2583. Pending CVO-clear = 8/8.

## Design (COO-confirmed @233530Z; CTO confirm-window on N/M open)

- **(1a) DISPOSITIONED, NOT DATED:** every pending NA row must INCORPORATE or carry an explicit
  `deferred_until: <trigger>` (an honest "can't incorporate yet + exactly what fires it"). A pending row with
  NO deferred_until, aged past **N=14d**, is a SILENT-PENDING breach -- it moves or declares, it can't sit.
  The `deferred_until` field (added to `ledger_schema.json`, optional) IS the calendar->control conversion.
- **(1b) BURN-DOWN > GENERATION (converges, not permanent-by-construction):** BOUND-THE-FEED -- only
  ABSTRACTABLE core-mechanism enhancements enter the ledger (n-a/bespoke never do; the drift-gate denominator
  gates that; ~D's warrant = rare/wave-specific). Forced disposition drives silent-pending -> 0; a DEFERRAL
  RE-REVIEW at **M=60d** re-surfaces a deferred-forever row. Bounded feed + forced disposition + triggered
  burn-down + re-review = provable convergence (not a burn-down-rate race).
- **Mechanism:** `incorporation_sla.py` -- on-demand REPORT, ALERT-SUSPENSION-CLEAN (no new CI/alert). The
  breach surface JOINS COO's cadence-owner milestone reporting (drift-gate sweep + comp-system override-rate +
  this SLA). Does NOT duplicate the NESTEDABSTRACT forward loop (that burns it down).

## Exercised (TO phase 1-2 + CVO's two conditions)

| Check | Result |
|---|---|
| phase-1: the 6 pending rows + triggers | NA-0001/0002/0004/0005/0006/0007, each grounded to a named SDK-incorporation target |
| (1a) disposition the 6 | 6 within-SLA -> 6 explicitly-DEFERRED = **0 silent-pending** (VERDICT CLEAN) |
| self-test silent-pending-breach | PASS -- a synthetic aged non-deferred row surfaces |
| self-test within-sla-silent | PASS -- a fresh (< N) row does not fire |
| self-test deferred-not-breach | PASS -- an explicit deferral clears it |
| self-test deferral-review-breach | PASS -- a deferred row past M re-surfaces (no deferred-forever) |
| self-test incorporated-terminal | PASS -- incorporated rows not chased |
| self-test live-no-silent-pending | PASS -- the real ledger has 0 silent-pending after disposition |
| drift-gate ledger-integrity | PASS -- the new `deferred_until` field is schema-valid (added to schema first) |

## Compiler Tools

| Tool | Verdict | Note |
|---|---|---|
| `incorporation_sla.py` (built) | PASS | self-test 6/6; live 6-deferred/0-silent; the WS-6 SLA control |
| `drift_gate.py --self-test` | PASS | ledger-integrity clean after the schema + 6-row disposition |
| `.tools/commit-gate.sh` | PASS | incorporation_sla.py py_compile + ds-precommit + ruff clean |

What worked: grounding all 6 to REAL SDK-incorporation triggers made the (1a) disposition honest, not
hand-waved. The schema-first discipline (add `deferred_until` to `ledger_schema.json` before the rows) avoided
a self-inflicted drift-gate ledger-integrity fail (additionalProperties:false). What I caught: the py3.12
`utcnow()` deprecation (cosmetic on py39 runners) -- switched to a naive-UTC helper for clean output. Gap found:
none; both LD-0318 conditions exercised.

## Files Modified

See commit @5e85e2583: incorporation_sla.py [new], ledger_schema.json (+deferred_until), ABSTRACTION_LEDGER.jsonl
(6 rows dispositioned to deferred_until).

## Blockers

NONE. WS-6 landed. NOT "done" until CVO clears the LD-0318 two-condition gate (pinged @234132Z) -- that is the
gate, not a blocker. CVO-clear = SYSPARITY 8/8 COMPLETE.

## Current State (handoff, zero-context)

NFRA_SYSPARITY WS-6 landed @5e85e2583. The incorporation-debt SLA is `incorporation_sla.py` (run on-demand;
`--enforce` for rc-2-on-breach; `--json`; `--self-test`). The 6 pending NA rows each carry `deferred_until`
(a named SDK-incorporation trigger). SLA state: 0 silent-pending breaches / 6 tracked-deferred / 1 incorporated
(NA-0003). N=14d (silent-pending), M=60d (deferral re-review). The breach surface feeds COO's cadence reporting.
SYSPARITY status: WS-1 CLOSED, WS-3(a/b/retroactive/c-tooling) done + batch-1a seeded (governed bulk + flip
deferred post-wave, .py-ruff fork = COO-ruled d/b hybrid), WS-6 landed pending CVO. After CVO-clear = 8/8 and
~A HOLDS for Andrew's phase-steer (per MSTR).

## Next Steps

1. **[3.0.0_SA_CVO]** the LD-0318 two-condition gate: (i) the 6 dispositioned-not-dated (each deferred_until a
   real trigger), (ii) closes-faster-than-it-feeds / bounds-the-feed. Reproduce via --self-test + the live
   report. CVO-clear = SYSPARITY 8/8. Pinged @234132Z.
2. **[2.0.0_SA_COO]** carry the SLA-breach surface in the cadence-owner milestone reporting set (3 signals).
3. **[1.0.0_SA_CTO]** confirm-window on N=14/M=60 + the feed-boundary (abstraction-model domain) before CVO-close.
4. **[0.8.0_AE_CloudComp~A / me]** on CVO-clear: SYSPARITY 8/8, then HOLD for Andrew's phase-steer (MSTR). The
   WS-3c governed-bulk seed + flip resume post-wave once the .py-ruff fork is CTO-co-decided.
