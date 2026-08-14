# DEPLOY LEDGER — MDPF_TRGALN.TO-3 MDPF trio tighten (§3 rows 2, 3): accrual + publisher −30m

**Opened:** 2026-08-14T05:38Z by 0.7.0_AE_CloudOps (deploy-start; NEVER#6)
**Status:** OPEN
**GO:** 2.0.0_SA_COO 051505Z citing proof_TO-0.json rev 1 @772787a1e1 VALIDATED
**PRD:** docs/architecture/MDPF_TRGALN_PRD.md v1.1 @f50ee7223b §3 rows 2/3; §0 Andrew verbatim
("i dont think we need to wait until 10:10 and 10:20, seems like both of those could be pushed
30 min earlier")

## Legs

| Leg | Root | Resource | Edit | Status |
|---|---|---|---|---|
| 1 | mdpf-pipeline | mdpf-accrual-bridge-daily | cron(10 14Z)→cron(40 13Z) (accrual-bridge.tf:185) | OPEN |
| 2 | opal-assets | opal-assets-mdpf-portal-publisher-daily | cron(20 14Z)→cron(50 13Z) (mdpf_portal_publisher.tf:225) | OPEN |

⛔ Floor (mdpf-scheduled-floor, cron(30 13Z)) UNCHANGED BY DECLARATION — a plan showing a floor
row is a dirty plan = STOP. opal-assets leg `-target`ed + plan READ (daily-aua = dirty = STOP).
End-state ordering: floor 13:30Z → accrual 13:40Z → publish 13:50Z.

## Cutover-gap statement (pre-apply)

Both old fire-times (14:10Z / 14:20Z) have NOT yet fired today (apply ~05:4xZ); both new times
(13:40Z / 13:50Z) are later than apply time → exactly ONE fire each today at the new times.
No skip, no double-run.

## Rollback

Same-window cron revert to the prior strings (verbatim in the table). Schedule strings only.

## Close (checked only when TRUE, with evidence)

- [ ] safe-commit hash: ______ ; plans READ (one expected row each, NO floor row, NO daily-aua)
- [ ] Post-apply 0-diff re-plans clean; live APPLIED reads == §3 targets verbatim (2/2)
- [ ] Tags created (push rides MSTR integration window): ______
- [ ] CLOSED at: ______ with proof_TO-3.json commit: ______
