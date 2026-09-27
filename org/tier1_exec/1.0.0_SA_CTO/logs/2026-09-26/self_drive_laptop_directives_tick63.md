# SELF-DRIVE laptop directives -- ticks 62-63 (2026-09-27 ~18:18Z to ~19:18Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 59-61 log (@`82401284e8`). **State: ARMED.**

## Window 17 result (~P ledger @`ca5ae4f5ea`)

K8 ran ONE export POST.
- It passed the reopen-rule authorizer: arm 1 admitted on the live path.
- It then failed in the narrative build: rejected prose was kept with asserts_causation=true, and NarrativePacket
  validation raised. The submit ran 60.4 s, and API Gateway returned 503 at 29.3 s.
- Nothing was written.
- Arm 3: the owner is unchanged (sha12 before equals after).
- Arm 4 is not measurable live (no grant persisted); it is unit-proven.
- No arm failed, so no rollback was owed.

## Rulings

1. **Window 17's defects (18:48:41Z):**
   - rejected prose is WITHHELD, and a validation failure never fails the export;
   - the submit returns after resolve plus grant pre-validation, and the build and render run async behind the receipt.
2. **~P 102029, the async path: (a) the function invokes itself with InvocationType=Event.** Four conditions:
   - maximum_retry_attempts=0 in Terraform;
   - a terminal receipt state on every exit;
   - a pending receipt older than the function timeout reads as FAILED (TIMED_OUT);
   - a one-hop marker, so the async leg never re-invokes.
   ~P's item 1 (rejected prose withheld; 3 of 3 negative controls fail on HEAD) is accepted.
3. **~Y 102023 (S159):** the vendor's printed "Data as of" line is R10's label for Analysis sections. There is no
   certifier change; the hop-7 check that the line is present stays. S163 (@`5465f7dcd1`) closes S159.
4. **~Y 102027, Comparison and Multi-Comp (FWD-4 acceptance arms, `IRPT_BCKEND_PRD.md:52`):**
   - (1) 4 read-only securities_info GETs go into ~P's next window with two halves, under the API-egress arm. ~Y
     prepared the act spec and grader @`5e97af4153`.
   - (2) The firm reporting-permission against Opal's model portfolios is an ENTITLEMENT. It is carded to Andrew
     (below).

## Other movement

- 0.6.2_AE_PartnerETL~S @`de68b15717`: the session-fetch now uploads its log on failure (`EXIT_CODE=$?` was dead code
  under `set -e`).
- Drain: wk-DSGN_IRPTV1-36.
- C: has 24 GB free.

## Open calls in scope

1. BLOCKING, at Andrew: may firms' Comparison and Multi-Comp reports compare against Opal's model portfolios
   (P:1728413/1728415/1728315/1728420)? REC: yes, for firms that already see them in Model Portfolios (FWD-11).
2. CARRIED, at Andrew: the purge of the S19 screenshots from history. REC: keep history.

## Completion test

NOT DONE: 0 of 2 IRPT projects are complete (both `active`). D10 is UNMEASURABLE (no members).

state: ARMED
