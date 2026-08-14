# DEPLOY LEDGER — MDPF_TRGALN.TO-2 Inflection retiming (§3 rows 8–15 + 6): uniform −2h15m + mirror

**Opened:** 2026-08-14T05:30Z by 0.7.0_AE_CloudOps (deploy-start; NEVER#6)
**Status:** OPEN
**GO:** 2.0.0_SA_COO 051505Z citing proof_TO-0.json rev 1 @772787a1e1 VALIDATED
**PRD:** docs/architecture/MDPF_TRGALN_PRD.md v1.1 @f50ee7223b §3 rows 8–15 + 6

## Legs

| Leg | Root | Resource | Edit | Status |
|---|---|---|---|---|
| 1 | inf-pipeline | opal-inf-jwt-fetch | cron(5 12Z)→cron(50 9Z) (eventbridge.tf:34) | OPEN |
| 1 | inf-pipeline | inf-api-reps-daily | cron(17 13Z)→cron(2 11Z) (inf-api-reps.tf:187) | OPEN |
| 1 | inf-pipeline | inf-accounts-v2-daily | cron(22 13Z)→cron(7 11Z) (inf-accounts-v2-daily.tf:199) | OPEN |
| 1 | inf-pipeline | opal-inf-bronze-runner-cron | cron(30 13Z)→cron(15 11Z) (eventbridge.tf:69) | OPEN |
| 1 | inf-pipeline | inf-api-assets-v2-daily | cron(32 13Z)→cron(17 11Z) (inf-api-assets-v2.tf:188) | OPEN |
| 1 | inf-pipeline | inf-api-eclipse-daily | cron(33 13Z)→cron(18 11Z) (br1-eclipse-rehome.tf:122) | OPEN |
| 1 | inf-pipeline | inf-api-positions-daily | cron(37 13Z)→cron(22 11Z) (inf-api-positions.tf:182) | OPEN |
| 1 | inf-pipeline | inf-api-txn-daily | cron(47 13Z)→cron(32 11Z) (inf-api-txn.tf:169) | OPEN |
| 2 | opal-assets | opal-assets-ingest-mirror-inf-daily | cron(5 15Z)→cron(5 13Z) (mirror.tf:106) | OPEN |

One inf-pipeline apply (-target ×8, plan READ) + one opal-assets targeted apply (-target mirror_inf,
plan READ; daily-aua row = dirty plan = STOP). Uniform −2h15m verified: every internal family offset
preserved (jwt −2h15m; reps/accounts/bronze/assets/eclipse/positions/txn each −2h15m exactly).

## Cutover-gap statement (pre-apply; apply ~05:3xZ — EARLIER than the TO's ~09:0xZ expected shape)

- Row 8 (jwt): old 12:05Z not yet fired today; new 09:50Z is later than apply time → ONE fire today
  at 09:50Z. NO skip (the TO's skip case applies only to a 09:50Z–12:05Z apply; we land ~05:4xZ).
  No ad-hoc jwt invoke needed.
- Rows 9–15: old 13:17–13:47Z not yet fired; new 11:02–11:32Z all later than apply time → ONE fire
  each today at the new times. No skip, no double-run.
- Row 6 (mirror): old 15:05Z not yet fired; new 13:05Z later than apply → ONE fire today at 13:05Z.
  No skip, no double-run.

## Interaction statement (mirror caveat, carried from TO-1)

The mirror is firm-scoped, NOT all-rows: handler reads `event.get("firm")` (:400) and this rule
passes {"firm":"inf"} (mirror.tf). The row-6 retime moves ONLY the inflection mirror leg; the cot
mirror (row 5) was retimed separately in TO-1 — neither apply re-times the other's leg.

## Out-of-scope surfacing (pre-registered, PRD §6)

The legacy convergence path (mdpf-daily-refresh-trigger on the INF sentinel → mdpf-daily-trigger →
EC2 feeders) WILL fire ~12:47Z after this retime (sentinel ≈12:44Z). It is OUT OF SCOPE, harmless
to serving, NOT touched, NOT reported fixed. (Its dim_model_portfolio write becomes pre-floor —
the TO-0 pinned coupling resolving as designed.)

## Rollback

Same-window cron revert: re-apply prior strings (verbatim in the table). Schedule strings only,
no data mutation.

## Close (checked only when TRUE, with evidence)

- [ ] safe-commit hash: ______ ; plans READ (9 expected rows only, no daily-aua); applies landed
- [ ] Post-apply 0-diff re-plans clean; live APPLIED reads == §3 targets verbatim (9/9)
- [ ] Tags created (push rides MSTR integration window): ______
- [ ] CLOSED at: ______ with proof_TO-2.json commit: ______
