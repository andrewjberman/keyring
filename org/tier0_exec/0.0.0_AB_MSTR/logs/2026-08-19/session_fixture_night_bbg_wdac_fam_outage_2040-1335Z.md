# 0.0.0_AB_MSTR session log — 2026-08-18 20:40Z → 2026-08-19 13:35Z (delta since the pre-fixture checkpoint; same session, PID 28080)

**Archetype:** integrator/carry window through the fixture night + the two morning incidents. Written on
Andrew's ~13:16Z fleet /log order; wind-down HELD for CTO's explicit GO (spares CTO/COO/CRO~A; I sequence
myself last per the verbatim scope).

## CURRENT STATE (successor-grade)
- **origin/CLOUD @9c1f032a7d** (== local; 18 integrator pushes across the session; exposure read printed
  before every push; every remote-verified via ls-remote). Both fabrics at parity as of @f970ea785d
  (08-18); site-Z commits since (BBG incident records) land on origin/SITEZ — sweep on the next /integrate.
- **ROW-0 / ADVI_BDPLAT_RESTORE: CLOSED 6/6** (fixture accepted, COO validator record, AE ledger closed,
  d12 surprise falsified+superseded, TO-4 10/10 complete). Andrew's line delivered (canonical +8.31%
  cent-exact; served +3.7% vs the old ~$108M overstatement; ~$28.5M basis residual to the P4 pins).
- **GOLDHOME-REPOINT-49F: COMPLETE end-to-end + issuer-flipped** (mint w/ exercised Deny → 4,222 sync →
  code SPLIT flips → re-anchor → live-verify → old-prefix delete on Andrew's ~12:46Z word). LD-0422 is
  the SOLE ledger home (second LD declined as two-homes). Deploy target verified flipped to
  `opal-data-49financial/_code/`; zero old-root writes through my windows.
- **T-B Half 1 landed** (FLAG-2 re-point, sha MATCH); PB-1/2 proof = the 13:30Z scheduled run — which
  also gates the held `json/mdpf/49financial` delete. PB-3 (smartx :482) APPLIED ahead of its clock.
- **BBG pull incident (08-19 07:00): RECTIFIED, triple-verified** — root cause an MSP WDAC reputation
  policy blocking conda `_psutil_windows.pyd` at kernel start (CodeIntegrity 3077/3033 + repro; terminal-
  logout and gate hypotheses RULED OUT); fix = PyPI wheel swap, reversible, no policy touched; ad-hoc
  re-pull served `data_as_of=2026-08-18` at 12:55Z (run's own content-verify + site-Z read + my read).
  RESIDUALS: 08-20 07:00 scheduled fire is the real acceptance (site Z reads it); the class has 2 members
  (pywintypes dodging by copy-resolution); **conda-meta/disk disagreement leaves the resurrection path
  OPEN** — any conda op on the cma env restores the blocked binary; WDAC exemption-vs-migration decision
  AT ANDREW. Instrument note banked: `NumberOfMissedRuns` counts never-STARTED only — blind to rc=1.
- **Schwab FAM outage (external): 08335338 FAM absent after as_of 08-10, six trading days** — our pull
  lane + converter proven healthy; a01's refusal correct; client-facing serve UNAFFECTED (bd platinum T-1).
  **49F P2→P4 dates re-dated to R..R+3 from FAM resumption** (@f79760179a, pushed); everything else
  proceeds. Andrew's two accelerators framed: the enumerate-mode SSM word + the Schwab contact.
  Self-heal on resumption: 30-day lookback + DS~A catch-up.
- **Portal**: PROD @e27dd5fa (v2.1.163 promote, both pushes on DT's exact refs; the edcc503e rider
  declared-not-stripped). CTO~X's 8cbb2f86 still QUEUED at my seat on DT's freeze — release message never
  arrived; whoever winds DT down should discharge or explicitly carry that freeze.
- **Tailnet**: live both ends under andrew@opalinvest.com (laptop ↔ opal-bloomberg, 4ms direct); RDP
  enable done at the box (tailnet-scoped); Andrew's mstsc test still pending.
- **AT ANDREW (open words):** WDAC exemption-vs-migration · Schwab FAM contact · enumerate-mode SSM run ·
  mstsc test. **AT CTO:** master log + program brief; wind-down GO.

## Window acts (compressed)
Fixture-night pushes (TO-1 proof, ledger closes, TO-4 kills, 49financial mint, tag shared-infra-v1.46.0,
COO validator close, d12 supersede arc, T-B Half 1 + GOLDHOME DSA/CVO legs, housekeeping); morning sweeps
(CTO R1 ruling ACCEPT-WITH-RECORD, PB-3 fix, 4b determination 15-EMIT, CVO repair-send — the broker-cc
lesson); BBG incident carry (urgent relay → mechanism → rectify → triple-verify → WDAC frame + supplement);
FAM outage carry (AE frame + COO consequence line + re-date push); GOLDHOME close window; Andrew carries
throughout. Bus loops all ACK-closed both directions.

## Compiler tools
comp-which (routing), comp-find (bloomberg pull source location — SURFACED band), comp-estate --list;
raw aws reads were evidence-grade serve/version reads beside named keys (head-object/list-object-versions
per the carve-outs). deploy_ledger/to-check not re-run this window (no disposition act pending).
