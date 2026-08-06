# ADDENDUM to W-1a deploy-completion ledger — L1 rollback target RELOCATED (2026-08-06 ~2140Z)

**Author:** `0.0.0_AB_MSTR~Z` (the agent who executed the relocation) · 2026-08-06T2155Z
**Amends the READING of:** `20260806T0009Z_mdpf-canrte-w1a-aggregate-aua-repoint_deploy_completion.md`
**Why a sibling file:** the ledger is a RENDERING of `deploy_ledger.py`, which has no amend-leg verb —
a hand-edit inside it is silently overwritten on the next tool write (DS~Z base lane, measured
2026-08-05/06; live consequence re-routed to CTO~Z 2026-08-06). This addendum is the persistence
surface the correction actually survives in. **Read it BEFORE executing any rollback from that ledger.**

## WHAT CHANGED AFTER THE LEDGER CLOSED L1

Andrew-direct order, 2026-08-06 at the site-Z MSTR terminal (record @4a2651063, verbatim there):
clean the `platinum/mdpf/` root. Executed ~2140Z: the 439 historical partitions at
`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/` were **MOVED** to
`s3://opal-data-portal-v2/platinum/mdpf/archive/aggregate_aua/` (439/439 verified, 0 left at the old
path, bucket versioning Enabled).

**Therefore L1's proof clause "COPY not move — platinum source still 439, rollback target intact" is
TRUE AS OF ITS CLOSE (20260806T001833Z) and FALSE NOW.** The bytes are intact and content-identical;
the LOCATION moved. Nothing was lost.

## THE OPERATIONAL CONSEQUENCE — L5 ROLLBACK AS WRITTEN NOW FAILS SILENTLY

L5 re-pointed `opal-assets-daily-emitter` env (`PLATINUM_BUCKET` + `AGGREGATE_PREFIX`) to
`opal-data-assets` / `gold/mdpf_revamp/_aggregate_aua/`. A rollback executed from the ledger as
written re-points the emitter to `opal-data-portal-v2` / `platinum/mdpf/aggregate_aua/` — **which is
now EMPTY**. Per L6's own analysis the failure shape is a 404 → `ROLL_SOURCE_ABSENT` → **permanent
silent DEFER**, not a loud error. A rollback performed during an incident would quietly read nothing.

## CORRECTED L5 ROLLBACK PROCEDURE (either branch; (a) preferred)

**(a) Restore-then-rollback:**
```
aws s3 cp s3://opal-data-portal-v2/platinum/mdpf/archive/aggregate_aua/ \
          s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/ --recursive
# verify 439 objects at the destination, THEN apply the L5 env reversion via Terraform/safe-apply
```
**(b) Re-point-to-archive:** set `AGGREGATE_PREFIX='platinum/mdpf/archive/aggregate_aua/'`
(emitter concatenates bare — trailing slash REQUIRED per L5's own note) + `PLATINUM_BUCKET='opal-data-portal-v2'`.
Branch (b) leaves the serving root clean but departs from the pre-W-1a state; (a) reproduces it exactly.

**Do NOT move the archive back preemptively.** Andrew's root-clean order stands; the restore happens
only IF an L5 rollback is actually executed.

## STATE AT WRITING, measured

- Gold (live path): **440** partitions at `gold/mdpf_revamp/_aggregate_aua/` — the 439 L1-copied plus
  `2026-08-06.json` (13:33Z accrual-hop write, matching CTO F3). The live path needs no rollback today.
- Platinum archive: 439/439 at `archive/aggregate_aua/`, content-identical lineage (L1's own
  ETag/Size verification carries — the move used S3 copy semantics, same ETags).
- L6 is unaffected (its rollback is DELETE-two-keys, no platinum dependency).
- L7/L8/L9 remain OPEN/HELD per the ledger; this addendum does not adjudicate them.
