# .open_findings/ — owned trigger findings (NFRA_MSBEFF.R4)

Out-of-band landing surface for the R4 post-commit triggers (TRIGGER_LAYER doctrine: a
finding lands as an OWNED ITEM, not a log line nobody reads). Each file is a `{owner,
severity, review_by}` finding whose PRESENCE is the visible-until-resolved carrier.

Producers (async, detached, non-blocking — never taxes the commit):
- `closeout-comp-state-post-commit.sh` (R4-A) — `<CODE>_closeout_drift_<ts>.json`:
  comp-state still reads a project BEHIND after its closeout commit. ADVISORY.
- `deploy-pipescript-check-post-commit.sh` (R4-B) — `deploy_stale_<ts>.json`:
  a deploy-completion ledger closed but comp-pipescript deployed reports the named
  script(s) STALE/MISSING on S3 (the bd-gold-trigger-vs-4-stale-scripts class). blocking-class.

Lifecycle: the OWNER resolves the drift/stale (or records why it is expected), then DELETES
the finding file. A file lingering past `review_by` is itself the visible signal.

SURFACING (CTO~Z ruling-1, 2026-07-23): there is NO separate sweeper and NO new cadence — a new
cadence is the fan-out that trains skimming. Instead every R4 trigger's fast-path breadcrumb
reports `N open finding(s) (M PAST review_by)` (`_open-findings-status.sh`), on the surface
agents already touch. That closes both TRIGGER_LAYER limbs: the open COUNT kills "an honest flag
nobody owns", and the PAST-DUE count kills the dangling expiry. The finding file keeps
owner+review_by as the accountability record; the breadcrumb is the surfacing. If findings later
accumulate ignored DESPITE a past-due breadcrumb, escalate to an owner-sweep then — measured,
not preemptive.

NOTE (arm-gate): the R4 triggers are BUILT + mutant-proven but NOT yet wired live — live-arm is
gated to a non-serve window on 1.0.0_SA_CTO~Z's GO. Arming is one command:
`bash .tools/git-hooks/install-closeout-comp-state.sh`.
