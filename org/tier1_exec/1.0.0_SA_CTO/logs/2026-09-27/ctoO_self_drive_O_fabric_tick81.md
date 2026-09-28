# /self-drive ~O fabric -- tick 81 (1.0.0_SA_CTO~O, 2026-09-27 19:46Z)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d.

**OG-e-2 LANDED (R2-k SERVED step 1).** opal-gateway has served `fe94911257` since 18:43:56Z (COO~O complete @bc66889185,
drain @cc8561cc9e). The worker's proof reads AC1-AC3 PASS, VALID (@3a5de98b2e). No rollback was needed.

This half's GO conditions, read against the record:

| condition | reading |
|---|---|
| EMAILDENY = 0 at GO | 0 of 163 before the upload and 0 of 167 after, on the issuer's re-scan (@bc66889185). CVO~O's own scan also reads 0 of 167 (@841e32111a). The ledger does not carry the pre-upload read; the issuer's commit does. |
| host md5 = the release | 4 of 4 = fe94911257 (CVO~O post-act read) |
| tool list | 46 = 46 |
| ENABLED_INTEGRATIONS | unchanged |
| mcportal bundle | pinned |
| off-hours | Sunday, 18:43Z |

CVO~O's post-act adjudication (row Z-C-S3, @841e32111a) reads the act as inside the signed radius.

**Open in R2-k:**
- Step 2 (the Alyssa backfill) is superseded in intent by the `/sprint` roster card at Andrew. REC (a): set the roster
  in the `deploy-to-ec2.sh` `.env` template.
- Step 3, the grant-writer Lambda rebuild, must land before any grant is made through the dashboard.

**Cards at Andrew:** (1) `/sprint` for Andrew only; (2) the Black Diamond login around 06-23; (3) the switchover sitting.
**Completion test:** NOT DONE. 0 of 4 projects are complete.

state: ARMED
