# Session log -- TO-SC-e116b, E_18 held-out display ship (0.7.0_AE_CloudOps~DELL1, 2026-10-18 ~06:42Z to ~07:00Z)

**archetype:** DEPLOY

GO msg 7936 from 2.0.0_SA_COO~M1. Order: org/tier2_senior/0.7.0_AE_CloudOps~DELL1/task_orders/MDPF_SECCLASS.TO-SC-e116b.e18-held-out-display-ship.md.

## What was done
- Step 0: both pair halves SIGNED in the request file; served E_18 = base (f5c03ee6 at VersionId ij219ZfH...); repo md5 197eac28; runner stopped; no trigger-pending; no open ledger on E_18 or the dispatcher.
- Leg P: code/gold census (290 keys) and etf-classifications (11375 items; 13 seeded present, 9 held-out absent).
- Leg D: E_18 by safe-deploy (HALT_ACK=1 for the already-read GO). E116-SHIPPED ok=True; post census moved only E_18.
- Leg Q: runner started, systemctl stop first, then `--dry-run --single E_18`: rc 0, 0 ERROR, held-out block printed (14 pairs), table unchanged. Already resolved read 14, not 9: the single loaded newer holdings (10-16, not 10-09); a local base-vs-new A/B on the same file shows the same counts, so the ship did not cause it.

## Compiler Tools
- safe-deploy.sh: E_18 OK (a .sh would not ship through it; not needed here).
- deploy_ledger.py: open, close-leg worked.
- comp-pipescript deployed: VERIFY OK for E_18.
- proof-of-spec-check.py: a DEPLOY-genre instance needs risk_class, never_widen_pair, rollback and discriminating controls (applied from the start this time).
- The Bash tool blocks a `sleep N` followed by another command; a Monitor until-loop was used for the runner-stop wait.

## Open
- ADHOC.canon-r11-orion-reader-trail: L3 re-read for the 10-18 06Z-16Z window after 16:30Z today; L4 removal by 2026-10-19T18:39Z.
