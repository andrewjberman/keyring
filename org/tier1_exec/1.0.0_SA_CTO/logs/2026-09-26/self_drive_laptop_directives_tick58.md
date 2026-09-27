# SELF-DRIVE laptop directives -- ticks 57-58 (2026-09-27 ~16:17Z to ~17:17Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 55-56 log (@`7c78eaf38e`, ~16:17Z). **State: ARMED.**

## Milestone

**The FIRST READY Analysis report: window 15, REQ-67e12718, RPT-5288c06d, READY at 16:23:00Z (~P @`d34d148579`).**
Bounds held: 2 receives, 3 status GETs, 1 saved GET, 0 re-captures. The stored `level_as_of_type` is `custom_date`;
S159 and S160 are filed.

## Acts

1. **Halves signed @`93780555f5`:**
   - window 15 amendment 1 (K10 page read of the READY report), blob `3207cf8e`;
   - window 16 (the K8 export on e8a00b23), blob `907073b1`.
   - The CRO halves are @`ff6622ce41`.
2. **S160 ruling (~Y 101969):**
   - window 16 is not gated;
   - W15-3 is kept, narrowed to Static portfolios (custom_date on a non-Static portfolio refuses, on the next resident);
   - ~Y's read-only saved GET of an advisor-created prior_close portfolio is approved, in its own packet;
   - ~Y's 101938 reason is withdrawn.
3. **S158, the COT session refresh (MSTR 101975):**
   - the base lane is encumbered by COT_SUPERVISED G1;
   - the issuer is ~P, with ONE order to `0.6.2_AE_PartnerETL~S`, and MSTR spawns on its commit;
   - the order has three criteria: name the failure cause from the box log, upload the log on failure, and one scheduled
     Success that moves AWSCURRENT.
4. **Andrew's status nudge (CRO 101980): answered at 17:03:31Z.**
   - My reply cited two message ids I had not read back. It was corrected at 17:03:51Z, citing by timestamp.
5. **Window 16 was refused ReportDenied (~P 101986). Ruled (a):**
   - export admits the P-REOPEN-01 callers through the SAME scope check, same firm only;
   - the render grant is minted for the caller;
   - two proof arms: an in-scope second principal exports, and an out-of-scope principal is denied.
   - The CRO view (101989) agrees and adds two arms: the owner is unchanged, and the receipt names the caller.

## State

- C: has 19 GB free (16:49Z).
- Active commitments in the last 24 h: 0 lines.
- Drains: wk-DSGN_IRPTV1-35 and -36.

## Open calls in scope

1. CARRIED, at Andrew: the purge of the S19 screenshots from history. REC: keep history.

## Completion test

NOT DONE: 0 of 2 IRPT projects are complete (both `active`). D10 is UNMEASURABLE (no members).

## Waiting

| on | what |
|---|---|
| ~P | the export authz TO, then the K8 re-cut with 4 arms; the S158 TO |
| 0.0.0_AB_MSTR | spawning 0.6.2_AE_PartnerETL~S on the S158 TO's commit |
| ~Y | the saved-GET test; the Static-only narrowing on the next resident version |
| ~D | the K10 page read of RPT-5288c06d |

state: ARMED
