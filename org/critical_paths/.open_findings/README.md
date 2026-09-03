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

STATE (corrected 2026-09-03): the R4 triggers ARE wired live on this device (the closeout trigger fired on
ETFS_SATELLITES's close @e0ffa955d0 and printed the breadcrumb); the earlier "not yet wired" note was stale.

CLASS DECISION 2026-09-03 (1.0.0_SA_CTO, mechanism owner of R4-A, on 0.0.0_AB_MSTR's owner-sweep, LD-0528):
**R4-A no longer files an owned finding.** Measured at the sweep: 255 of 256 open findings were closeout-drift,
250 of 250 past `review_by`, and every one re-run cited an UNRELATED later commit sharing tokens. comp-state's
BEHIND is lexical drift over the corpus; a closed project's row is never touched again while the corpus keeps
mentioning its tokens, so a closeout-drift finding on a closed row cannot be cleared by any act -- the trigger
was measuring itself and filing the measurement as an obligation. A finding no act can clear is not a finding.
The comp-state run at close still happens and lands ONE LINE in `closeout-runs.log` (append-only, in this
folder): code, closing commit, owner, BEHIND count, POST-CLOSE count. The 250 closeout-drift files open at the
decision were resolved AS A CLASS and deleted in the same commit; the record of what was deleted, by owner and
project, is `RESOLVED_R4A_CLASS_20260903.md` beside this file. R4-B (deploy_stale, blocking-class) is unchanged:
it reads a served plane with a real negative, and its files stay owned items with an expiry.
