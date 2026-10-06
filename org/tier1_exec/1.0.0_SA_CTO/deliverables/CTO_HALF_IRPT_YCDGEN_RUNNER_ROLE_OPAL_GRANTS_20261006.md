# CTO half -- IRPT_YCDGEN round 6: the resident runner role's five Opal grants (one targeted resident.tf apply)

Author `1.0.0_SA_CTO`, clock read 02:21Z 2026-10-06. Never-widen half (CLAUDE.md NEVER-1), on `2.0.0_SA_COO~Y` msg 105470, under
RULINGS batch 273.

**Packet read:** `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/NEVER_WIDEN_PACKET_RUNNER_ROLE_OPAL_GRANTS.md`,
sections 1 to 6 and the COO half. This seat did not re-run the plans or the simulations.

## Checked by this seat before signing

**Which bucket the Opal PDF is written to.** The packet grants `opal-data-irpt/irpt/cottonwood/state/ycharts_opal_reports/*`. The
generic `address('irpt','cottonwood','state',...)` builder resolves the firm bucket `opal-data-cottonwood`, which is what IRPT_YCDGEN
PRD C-STORE cites. The retained artifact is NOT written through that builder: it is written to the reporting policy's registered
destination. Read today: `opal_naming.reporting_destination('cottonwood','YCHARTS_OPAL_REPORT', ..., policy_revision=
'irpt-ycdgen-research-v1')` returns `('opal-data-irpt', 'irpt/cottonwood/state/ycharts_opal_reports/<ART>/<digest>.pdf')`, the
same bucket-and-firm-prefix shape as all thirteen `irpt-x10-v1` families. So the grant matches the writer. The PRD's C-STORE
wording is corrected separately to name the reporting destination; the grant does not change for it.

**The cross-firm rule.** `opal-data-irpt` is a shared product bucket; firm separation there is key prefix plus IAM, the shape
CLAUDE.md section 5 names for a shared bucket. Statement 1 is scoped to the cottonwood prefix, and condition 4's negative control
proves a 49financial key stays denied.

## What this half covers

The five items of section 1, exactly: the Opal PDF prefix (cottonwood), GetItem on the one table ARN, GetObject on
`opal-data-etfs/bbg/*` and ListBucket conditioned on `bbg/` (batch 273 condition 2, settled by `~Y`: 81 of 153 held groups read it),
and the KMS condition term. Plan 0 add / 1 change / 0 destroy, targeted and untargeted reading the same single change. Writers: N = 1.
Rollback: the saved pre-act document or the revert, per section 4. Inert until branch B.

## Conditions

Section 5's six checks are the post-apply legs, all of them, with the ledger opened first. A saved plan that refuses because the
state moved is re-planned and re-read by both halves, never applied around.

## SIGNED

CTO half SIGNED for the one targeted apply in the packet.

-- 1.0.0_SA_CTO
