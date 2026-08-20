# R14-T1FIX: 49F chain production date derivation -> prev_trading_day, deployed 20h44m ahead of the fire — 0.4.0_DS_ClientPlatform~B

**archetype:** IMPLEMENT
**Date:** 2026-08-20
**Task Order:** D2_ADVI_49F.R14-T1FIX (pending; GO COO 63232 @1550Z; deadline FRI 2026-08-21 12:45Z)
**Status:** IN PROGRESS — T1–T4+T6 discharged today; T5 (named-reader FIRST-green read) fires FRI 12:45–13:15Z

---

## Objective

Fix the 49F canonical chain's PRODUCTION date derivation so it targets the T-1 read frontier
its own doc promises (per the RULED fix shape, CTO 63213), land + deploy before the FRI
2026-08-21 12:45Z fire — the re-dated FIRST green gating D2's sovereign single-green FRI
flip+promote (Andrew-ruled (a), MSTR 63259).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript io | `io chain_49f_entrypoint --pipeline bd` | WARN | "Unknown script" — the 49f chain entrypoint is not in the bd-gold registry; orientation taken from the entrypoint's own doc block + the CVO 63207 / CTO 63213 mechanism records |
| comp-find | `--name 'chain_49f_entrypoint*'` | PASS | 1 hit / 27,049 scanned — exact file located with denominator |
| comp-find | `'opal-data-49financial/_code'` | PASS | 34 hits / 27,040 — located the declared deploy mechanism (safe_deploy_core longest-prefix map) + the seat's prior deploy-evidence pattern |
| safe-deploy | direct form, 1 file | PASS | `DEPLOYED [advi]` + internal `comp-pipescript deployed` leg `VERIFY OK`, gate PASS |
| comp-pipescript deployed | standalone, same path | FAIL | swept the **mdpf** tree, 0 match ("No scripts matched filter") — same nominal call verifies advi/_code inside safe-deploy; routing gap surfaced to COO (surprise channel) |
| proof-of-spec-check | instance + `T1,T2,T3,T4,T5,T6` | PASS | VALID rc=0, violations=0 |

**What worked:** comp-find's denominator lines; safe-deploy's atomic deploy+verify; the schema
checker caught 8 real shape violations on first pass (group/phase enums, compiler_tools item shape).
**What failed:** standalone `comp-pipescript deployed` on a runners_49f path resolves to the mdpf
tree — the advi `_code/` verify leg is reachable only through safe-deploy's invocation context.
**Gap found:** the 49f chain entrypoint has no `comp-pipescript io` registry row (bd-gold IDs only),
and `deployed` standalone cannot address the advi home — both halves of one coverage gap, surfaced
as my one-line surprise to COO, no action taken in-lane.

---

## Work Completed

### 1. Startup + orientation (1548–1553Z)
Registered `0.4.0_DS_ClientPlatform~B` (PID 27124), armed the persistent inbox Monitor (task
`bqk25k1jj`, TaskOutput=running), processed 7 queued + 4 live messages. Absorbed: CVO P1 finding
63206 (mechanism), CVO 63225 (caller-audit complete @412f3886a4 + both-lines rider), COO GO 63232,
COO weekday correction 63253 (today is THU 08-20; deadline instant unchanged FRI 08-21 12:45Z),
MSTR 63259 (Andrew-ruled (a): single-green FRIDAY flip+promote; my instant unchanged). dim-436
thread closed (dropped by Andrew) — no action at this seat; COO 020321Z explicitly held by COO
020805Z, not answered.

### 2. The fix @b5b0f26238
`data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py`, call-site only, calendar UNTOUCHED:
- **:230-family (production branch):** `expected_last_trading_day(now)` -> `prev_trading_day(now)`
- **:237-family (dry-run default):** identical change (CVO rider 1 — both lines or neither)
- **Doc block corrected** to name `prev_trading_day` and state why `expected_last_trading_day` is
  wrong here (FRESHNESS frontier, returns T-0 on any trading day); refusal-stays-loud stated.
- Commit message carries the CTO P2 rider line on the doc-vs-code seam ("a comment that performs
  compliance").

### 3. Battery + refusal control (T3) — ALL GREEN
Scratchpad run-and-read harness (nothing standing):
- **Leg A** (primitive vs hand-computed constants, calendar_source=NYSE/pandas_market_calendars):
  THU 08-20 -> WED 08-19; MON 08-24 -> FRI 08-21; day-after-Labor-Day TUE 09-08 -> FRI 09-04;
  defect contrast `expected_last_trading_day(08-20)==08-20`; mutant control (primitives disagree).
- **Leg B** (both call sites executed via `main()`, stages stubbed, asserted against the LITERAL
  2026-08-19): `CHAIN START date=2026-08-19` in dry-run AND production modes, rc=0 both.
- **Leg C** (real CLI, no stubs): `--date 2026-08-20` -> `REFUSED: fact_acc has no partition
  date=2026-08-20 (have ...['2026-08-17','2026-08-18','2026-08-19'])` + `CHAIN ABORT
  stage=a00_dim_account rc=1 wall=1.9s`, process rc=1. Refusal EXERCISED, no fallback.
- **Determinism:** battery re-run twice, outputs byte-identical.

### 4. Deploy (T4) — 20h44m ahead of the fire
Push to CLOUD correctly BLOCKED (LD-0367/0368 integrator-only; commit rides the hourly integration
window — MSTR pushes). Deploy via safe-deploy's sanctioned direct form (HALT-GATE: 2 stale routine
COO quiesce/release msgs reviewed, HALT_ACK=1): `DEPLOYED [advi]` + `VERIFY OK`, gate PASS.
Independent Rule-22a read at 16:01:35Z: `s3://opal-data-49financial/_code/chain_49f_entrypoint.py`
LastModified 2026-08-20T16:00:56Z, 18,559 B, **sha256 byte-identical** to the committed file
(`8c18cec9...b858`); content controls on deployed bytes: `_tc.prev_trading_day(` = 2 (want 2),
`_tc.expected_last_trading_day(` = 0 (want 0).

### 5. Proof instance (T6)
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/D2_ADVI_49F.R14-T1FIX_PROOF_OF_SPEC.json`
— VALID rc=0 on the full positional set T1–T6. T5 carried honestly as UNCOMPUTABLE (future event:
tomorrow's fire) with its recompute condition named; instance re-validates on the T5 flip before
any `complete` flip.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Deploy via safe-deploy direct form rather than waiting for the integrator push | The pre-push deploy leg is integrator-gated (LD-0367/0368); the TO holds THIS seat to T4 before the fire; direct form is the header-sanctioned path and the seat's own precedent (c00-FIX, WP-4) |
| T5 recorded UNCOMPUTABLE (not omitted, not pre-passed) | The criterion names a future event; a row shipped with its reason is a result, a silent omission is a defect (the CANNOT-ANSWER form this seat is on record for) |
| Battery leg-B asserts the LITERAL `2026-08-19` | Deriving the expected value from the same primitive under test would be a shared-derivation tie (self-comparison ban) |
| Caller-audit cited, not re-run | Ruled by the amended TO + GO (T2); re-deriving a completed audit burns deadline for nothing |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py` | Both derivation call sites -> `prev_trading_day`; doc block corrected | Yes — `b5b0f26238` (+ deployed, sha-verified) |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/D2_ADVI_49F.R14-T1FIX_PROOF_OF_SPEC.json` | New proof instance, VALID rc=0 | This commit |
| `org/tier2_senior/0.4.0_DS_ClientPlatform~B/logs/2026-08-20/session_r14_t1fix_1548-1610Z.md` | This log | This commit |

---

## Blockers

None. Evidence-cited wait only: T5 is tomorrow's event (FRI 08-21 12:45Z fire; my read by 13:15Z).

## Next Steps

1. **[THIS SEAT, FRI 12:45–13:15Z]** Read `s3://opal-data-49financial/gold/advi/_logs/` for the
   12:45Z fire — expect `CHAIN OK date=2026-08-20`. ABORT found = same-hour surface to COO.
   Then flip T5, re-validate the instance, flip the TO `complete`, RAVC-close.
2. **[MSTR window]** Commit `b5b0f26238` + this deliverable commit ride the hourly integration
   push (deploy already live; the S3 bytes do not wait on the push).
3. **[COO, routed]** comp-pipescript advi routing gap (surprise line in RAVC close); mdpf-trigger:812
   CONDITIONAL already routed to 0.7.0_AE by COO — not mine.
