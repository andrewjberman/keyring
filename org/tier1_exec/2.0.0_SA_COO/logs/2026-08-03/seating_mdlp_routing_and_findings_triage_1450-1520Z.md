# 2.0.0_SA_COO -- Seating, MDLP_MONPUB routing, and the 10-finding closeout-drift triage
**Window:** 2026-08-03 14:50Z-15:20Z (computed UTC; host is UTC-4) · **archetype:** COORDINATE
**Context:** Fresh COO session. MDLP_MONPUB (ST Model Portfolio manifest silent-regression) is the
live driven thread; site-Z device down (hardware hang, per MSTR).

## Current State
Seated: registered PID 26808, watcher Monitor `bn6jzoti6` armed and consumer-confirmed (its first
act was delivering 4 queued messages). LD-0290 serial file written. Zero crons -- XXX.md 1b-F COO
row carries no live scoped authorization (all prior /drive re-arms struck through + discharged).
Inbox drained: 4 messages, all closures or already-routed (AE~B fix-landed; MSTR broker/token
closure; CVO send-path confirm; AE~F ST-MP regression FYI already folded into MDLP_MONPUB).

## Routing done
- **MDLP_MONPUB spawn gap flagged to MSTR:** W1-W4 GOs issued @2733bfceff to
  `0.2.0_DS_PortfolioAnalytics`, which is NOT LIVE -- the GOs land in an unwatched inbox while the
  portal serves 07-27 (3 trading days regressed, client-facing). Spawn request already at MSTR;
  asked for priority.
- **Integrator push flagged to MSTR:** CLOUD ahead of origin/CLOUD by 21 commits (includes the
  whole MDLP_MONPUB chain). Lanes commit, integrators push; COO prompt bars me from pushing.
- **Division of labor with CTO (accepted 145934Z):** CTO holds arch gates + CVO W2 re-read +
  acceptance-flex; I drive W1-W4 RAVC close-loops once seats exist. Sequencing gates noted: W1
  pre-fire head-object gate (serve must read 07-27 or STOP), W4 only after W2 live-verified, CVO
  witnesses W2's failing-direction exercise. Standing attention on residual R2 (raw-S3 byte-copy
  backward writes, 3 days running): any "serve moved unexpectedly" mid-project = that class live;
  verify-live-before-mutation, never re-fire.

## Findings triage (CTO-routed housekeeping): all 10 expired closeout-drift findings RESOLVED + deleted
Per `.open_findings/README` lifecycle (owner resolves or records-why-expected, then deletes).
comp-state self-test PASS 3/3 before any verdict was trusted; drift re-confirmed still-live on all
8 projects before disposition. The finding JSONs were never git-tracked (producer writes async to
the working tree; only README.md is tracked), so deletion is filesystem-only and THIS LOG is the
durable disposition record.

**Group A -- EXPECTED BY DESIGN (5): NFRA_COMPLEARN, NFRA_COMPLEARN_PRD, NFRA_TOOLARCH,
NFRA_TOOLBHVR, NFRA_TOOLSTACK.** Closing commit `5782b1ded1` is the genuine Andrew-ruled
NFRA_VELOCITY supersession close (8 projects, 2-step atomic); open work is deliberately carried in
NFRA_VELOCITY_PROGRAM s.3b ledger, so post-close BEHIND reads on old-code TOs/records are the
supersession working as specified. Residual surfaced to CTO: the NFRA_TOOLSTACK program umbrella
row (REGISTRY.md:47) still sits Active while all 4 of its layers are complete-as-superseded --
recommended program-row closure, NOT executed unilaterally (Andrew's ruling named the layers, not
the program row).

**Group B -- MISATTRIBUTED, NOT CLOSEOUTS (4): ADVI_TWR, MDPF_CHANNEL_INDEPENDENCE,
OPAL_CONSOLIDATION, OPAL_GLDRNS.** All four JSONs read `status: active` -- never closed. The
recorded "closing commits" are REGISTRATION commits: `8ca69b870b` registered ADVI_PERFORMANCE,
`d1cca72e10` registered MDPF_CHANNEL_INDEPENDENCE. Mechanism source-grounded:
`.tools/git-hooks/closeout-comp-state-post-commit.sh:44-48` @ HEAD 2733bfceff -- the REGISTRY-only
branch greps ALL `[A-Z]+_[A-Z0-9_]+` tokens from added/removed diff rows, so a registration row
mentioning (or diff-adjacent to) other project codes sweeps them in as "closing." The BEHIND reads
on these four are ordinary active-project record-lag owned by their live drivers, not closeout
drift. **Instrument defect routed to CTO** (R4-A owner-side remediation: derive codes from rows
that MOVE to Completed or JSONs whose status flips to a closure value, not from all diff tokens).

## Compiler Tools
| Tool | Result | Notes |
|---|---|---|
| `comp-state --self-test` | PASS 3/3 | Gate before trusting any verdict, per skill. |
| `comp-state --project X --all` x8 | BEHIND/POST-CLOSE confirmed on all 8 | Drift still live as of this session; verdicts used as recall, triage was the precision layer. |
| `comp-which "how do I grep the repo"` | banner ran | A.3 exercise probe -- forwarder EXECUTES, not merely resolves (94/94 resolve bare). |

## Next / Open
- **MSTR:** DS/DT_PortfolioAnalytics spawn (gates W1); integrator push (CLOUD ahead 21).
- **Me:** drive W1-W4 RAVC loops the moment the seat registers; R2 standing attention.
- **CTO:** R4-A token-sweep defect remediation routing; NFRA_TOOLSTACK program-row closure call.
- **My pending TO** `NFRA_SCTY_PREMCP.P2` (network-isolation broker review): deferred residual,
  not urgent, unchanged.
