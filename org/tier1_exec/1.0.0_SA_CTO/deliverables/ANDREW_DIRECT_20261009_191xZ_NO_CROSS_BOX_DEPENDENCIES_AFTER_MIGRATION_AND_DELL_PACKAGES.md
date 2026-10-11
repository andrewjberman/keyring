# Andrew-direct 2026-10-09 ~19:1xZ -- no cross-box dependencies after a migration; check the Dells' missing packages

**Where:** 1.0.0_SA_CTO terminal (laptop). **Verbatim:**

> Yeah there is no reason for boxes to ever be sharing work across boxes, i understand a migration but no dependencies post migration. Also
> check out if there are packages / modules not in the dells that they need to work, saw a comment on that in the report

## 1. The rule, as this seat reads it (scope: verbatim, nothing wider)

A box shares work with another box only DURING a migration. Once a project is placed on a box, everything it needs to run (its COO, workers,
deploy lane, sign-offs, credentials, packages, hosts) is on that box. A standing cross-box dependency after the move is a defect to remove,
not a process to manage. This is NOT yet a CLAUDE.md law edit; it binds by this record until Andrew orders the law line.

## 2. Cross-box dependencies seen TODAY (this seat's record and today's reports; inferred where marked)

| Project (box) | Depends on | Why |
|---|---|---|
| MDPF_DEMQUE, MDPF_SECHIST, ETFS_RIVALS, AMGT_HARVST, AMGT_CORPUS (dell1) | site Z deploy lanes `~ZQ`, `~ZW`, `~ZC`, `~ZV` and site Z's manager windows | the Bloomberg Terminal (Opal_Terminal) and the harvest/induction runners live on site Z -- a HARDWARE dependency (inferred: the main cause) |
| NFRA_TRNSPT FWD-6 (dell2), ADVI_BILLING (dell2) | site Z's gateway release queue (NFRA_OPLGTW) | the Opal Gateway host is on site Z |
| IRPT_ANLREQ, IRPT_YCDGEN, TCKT_VNEXT (dell2) | laptop `0.7.0_AE_CloudOps~CTL` opening svc-irpt password windows (5 today) | the secret's resource policy is applied from the laptop |
| AMGT_RESAPP kk-1 (dell1) | a laptop deploy seat | the name-list republish needed laptop rights |
| MDPF_STRATID (dell1) | the laptop CTO's never-widen half | MDPF_GLOBAL is owned by the laptop CTO |
| dell1/dell2 IAM changes | laptop TO-APPLY-29 | permissions applied from the laptop |
| NFRA_CTLPLN (laptop) | dell1 exercises CT-x-1/CT-x-2 | by design: it tests the Dells (migration-class) |

## 3. Dell packages (the "comment in the report")

- The tool exists: `org/devices/kit_python_census.py` (NFRA_CTLPLN order CT-k-2, complete). Laptop `required` re-run 19:1xZ: 888 files,
  148 modules, **21 third-party, 20 distributions**, `ok=True` (`org/devices/kit_python_required.json` refreshed).
- **Neither Dell has a committed `installed`/`compare` result** (none under `org/devices/`), so what each Dell lacks is UNMEASURED. Known
  from the KIT cell: both Dells lacked `pandas_market_calendars` (the trading-day module changes its answers without it) and `ruff`.
- Package-level misses seen today were DEPLOY-PACKAGE gaps, not box gaps:
  - irpt-status composition.py predating a kwarg;
  - MDPF gold package lacking the gap module and `opal_naming` (row MDPF_SECHIST-D1-S2);
  - the STRATID 14:51Z import break.
  These are covered by the import-closure reads now required before deploys.

## 4. Routing (1.0.0_SA_CTO rulings)

1. **Packages:** each Dell's manager runs `python org/devices/kit_python_census.py installed --out org/devices/state/<box>/kit_python_installed.json`
   then `compare` against `org/devices/kit_python_required.json`, commits both, and installs every missing HARD module ITSELF. CLAUDE.md
   opens egress on every channel except Bloomberg, so a Dell installs from the package index on its own, with no laptop carry. Report the
   before/after counts. Owners: `0.0.0_AB_MSTR~DELL1`, `0.0.0_AB_MSTR~DELL2`.
2. **Dependencies:** folded into 4.0.0_SA_CRO's brief on the external feedback (same theme: "keep the four boxes autonomous, remove shared
   writable state"). For each row of section 2, the brief proposes how the dependency is removed: rights on the owning box, a box-local
   lane, or a served interface. The Bloomberg Terminal row likely stays a served interface (the DEMQUE queue), since the Terminal is one
   physical machine.
