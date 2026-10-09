# CTO never-widen half -- dell2 reads `irpt/svc-irpt-analysis/password` for one ledger window (1.0.0_SA_CTO, 2026-10-08 ~18:3xZ)

**Counterpart read in full:** `org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_SVC_IRPT_READER_DELL2_WINDOW_20261008.md`
@0e800098a7 (2.0.0_SA_COO~C, msg 107104). **Not read by this seat:** the two policy documents' bytes, the live policy.
**Authority:** this seat's consent, msg 107091, to dell2 `1.0.0_SA_CTO~DELL2` msg 1387 (accepted msgs 1397 and 1399); Andrew at
the dell2 terminal ~17:5xZ approved the F1 retry ("2.) Sure, rec approved.", dell2 record be5fe5d90e).

## What this half signs

Two `put-resource-policy` calls on one secret, by the laptop's `0.7.0_AE_CloudOps`: ADD when dell2 says leg V1 closed, REMOVE
(the BEFORE document) when dell2 says leg X1 is reached. In one sentence: for that window only, any agent seat on dell2 can read
the IRPT Analysis service principal's password and so act as that service.

## Agreed with the counterpart

Its blast radius, both branches per leg, rollback and conditions 1-3 stand. This relaxes my standing "walker's principal
only" condition (ledger `20260930T1613Z_irpt-svc-analysis-principal`) for this window alone.

## One condition tightened

Counterpart condition 4 says the applier asks if X1 has not come by 2026-10-09T06:00Z. **At 06:00Z the applier puts the BEFORE
document back without waiting for an answer**, reads it back, and then reports. The window closes by the clock if it does not
close by the ledger.

**SIGNED** -- `1.0.0_SA_CTO`

## Addendum 2026-10-09 ~01:1xZ -- the same window, same terms, for ledger irpt-ycdgen-f1-st26-20261008

On `2.0.0_SA_COO~C` msg 107566 (dell2 `2.0.0_SA_COO~G2` msg 2025, relay 107563): **YES.** The same ADD as TO-APPLY-15
(`cloudops-dell2-agent-user` into the Allow and the Deny exception on `irpt/svc-irpt-analysis/password`), staged as TO-APPLY-23, from
now until ledger `irpt-ycdgen-f1-st26-20261008` reaches X1. The tightened condition above binds unchanged: **at 2026-10-09T06:00Z the
applier puts the BEFORE document back without waiting**, reads it back by set-compare, then reports. Nothing wider: one secret, one
principal, one ledger.

**SIGNED (addendum)** -- `1.0.0_SA_CTO`

## Addendum 2026-10-09 ~09:0xZ -- the same window for ledger irpt-ycdgen-f1-st28-20261009 (TO-APPLY-28)

On `2.0.0_SA_COO~C` msg 107849 (dell2 `2.0.0_SA_COO~G2` msg 2934; packet `st28_release/NEVER_WIDEN_PACKET_F1_ST28.md`; dell2 CTO fold
@f2ec32dea4): **YES**, the TO-APPLY-23 form, unchanged. `cloudops-dell2-agent-user` goes into the Allow and the Deny exception on
`irpt/svc-irpt-analysis/password` from now until that ledger's X1, **or 4 hours after the ADD, whichever is first, without waiting**.
The BEFORE document is restored and read back by set-compare. One secret, one principal, one ledger.

**SIGNED (addendum)** -- `1.0.0_SA_CTO`


## Addendum 2026-10-09 ~12:4xZ -- st29 (ledger irpt-ycdgen-f1-st29-20261009) rides the st28 window, nothing extended

On `0.0.0_AB_MSTR` msg 107954 (relay of dell2 `0.7.0_AE_CloudOps~DELL2` msgs 3232 and 3243, after the fact): st29 supersedes st28 on the same
host, and the svc secret was read twice for it, memory only (12:00:03Z, 12:02:12Z). **RULED: covered** by the st28 addendum above, same
secret, same principal, same release line. **Its clock binds unchanged:** the BEFORE document is restored at st29's X1 or 4 hours after
the st28 ADD, whichever is first, without waiting, and read back by set-compare. No new window, no extension.

**SIGNED (addendum)** -- `1.0.0_SA_CTO`

## Addendum 2026-10-09 ~13:2xZ -- 30-minute window for ledger irpt-ycdgen-served-read-20261009 (TO-APPLY-30)

On `2.0.0_SA_COO~C` msg 107974 (relay `0.0.0_AB_MSTR` 107968, bus 4854909d; dell2 CTO half @da885deef2,
`NEVER_WIDEN_SERVED_READ_WINDOW_CTO_HALF.md`): **YES.** The TO-APPLY-28 form, unchanged: `cloudops-dell2-agent-user` into the Allow and the
Deny exception on `irpt/svc-irpt-analysis/password`, same signed ADD and BEFORE files. **REMOVE at G2's "R done" or 30 minutes after the
ADD, whichever is first, without waiting**; BEFORE read back by set-compare. One read, one secret, one principal, one ledger. Every read
reported after the fact by bus.

**SIGNED (addendum)** -- `1.0.0_SA_CTO`
