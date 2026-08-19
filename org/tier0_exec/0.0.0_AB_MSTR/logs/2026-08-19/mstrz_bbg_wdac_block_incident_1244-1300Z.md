# MSTR~Z incident log — 08-19 07:00 BBG pull FAILED (WDAC block), rectified + re-served by 12:55Z

**archetype:** DIAGNOSE
**serial:** 0.0.0_AB_MSTR~Z (session f155df1b)
**trigger:** Andrew-direct URGENT (laptop terminal ~11:3xZ, verbatim): *"CHeck in with
0.0.0_AB_MSTR~Z, I notice that the Bloomberg data pull did not run this morning, need to
understand why and rectify it immedaitely."* Relayed over agentbus 64210a8e, ACKed 12:46Z.

## WHY (grounded; both prior hypotheses ruled out)

- The 07:00 trigger DID fire: LastRunTime 08/19 07:00:01 ET, LastTaskResult **0x1**. Box up
  all night (uptime 17.5h at read) — **failed run, not a missed slot**.
- NOT terminal logout: the run's own log (`~/opal_bbg_logs/bbg_tplus1_20260819_070001.log`)
  shows the DAPI precheck read **UP**, no sign-in needed (laptop's candidate hypothesis dead).
- NOT a publisher gate: log line *"PULL FAILED rc=1 -- nothing sent, publish NOT attempted"*
  — it died in the PULL leg (supplement's candidate dead).
- **ROOT CAUSE:** WDAC/Code Integrity policy **ID {0283ac0f-fff1-49ae-ada1-8a933130cad6}**
  ("Enterprise signing level"; Win32_DeviceGuard UsermodeCodeIntegrityPolicyEnforcementStatus=2)
  blocked `C:\Anaconda\envs\cma\Lib\site-packages\psutil\_psutil_windows.pyd` at ipykernel
  start → kernel died before the notebook ran. Oracle: CodeIntegrity/Operational events
  3077+3033 at 07:00:05–08 naming file + policy; live repro at 08:47:30 generated fresh
  events (instrument discriminates, positive-controlled).
- **Activation pinned to reboot #2:** 08-18 07:00 run PASS → 08-18 13:53 ad-hoc PASS →
  15:10 ET reboot → first blocks 08-19 07:00:05. WDAC policies activate at reboot. The WS-2
  acceptance could not have seen this: a policy is invisible until a blocked load is attempted.
- Scope at repro time: `pywintypes313.dll` blocked at 07:00 but passed by 08:48; pandas,
  numpy, blpapi, win32api, tia, zmq, tornado all import clean — **reputation-class policy**
  (allowance warms per file); the conda-built psutil binary stayed blocked.

## RECTIFY (landed 12:49–12:55Z)

1. `pip install --force-reinstall --no-deps psutil` into the cma env: conda 7.0.0 (blocked)
   → **PyPI wheel 7.2.2**, imports clean rc=0. Minimal, reversible, no policy touched.
   ⚠ **A conda reinstall/update of psutil in cma resurrects the blocked binary** — keep it
   pip-owned until the policy question is settled.
2. Ad-hoc end-to-end re-pull (sanctioned repair instrument; production path stays the
   schedule): rc=0 in ~6 min. Run's content-verify: served data_as_of **2026-08-18**
   (generated_at 2026-08-19T12:55:36Z), 1D matches PKL for all five models.
3. **Independent serve-side verify (this seat, not the producer's self-report):**
   `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json` head-object
   LastModified 2026-08-19T12:55:37Z + content read `data_as_of: 2026-08-18` — correct
   Wednesday T-1. World current again (had been serving 08-17 = T-2).

## OPEN

- **AT ANDREW (recurrence):** MSP exemption for the cma env / box vs standing reputation-risk
  — any unsigned binary a scheduler loads can be next. Framed at his laptop terminal by base
  MSTR; his word pending. NO alarm/checker built (moratorium): detection stays the daily
  guardrail + the schedule's exit contract.
- **Tomorrow 08-20 07:00 scheduled fire = the real acceptance** of the repair (the ad-hoc
  proves repair, not the schedule). This seat reads it at the served object.
- BG seat briefed (env change + class recognition + no-silent-workaround routing), 12:56Z.

## Compiler Tools

No comp-tools run: single-box incident grounded on the failing run's own log, the
CodeIntegrity event oracle (with a live positive control), live imports, and the served S3
artifact (Rule 22a APPLIED/EXERCISED layers). comp-freshness would have read the symptom
(stale platinum), not the mechanism; no coverage gap found.
