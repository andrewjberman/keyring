# SELF-DRIVE laptop directives -- ticks 39-40 (2026-09-27 ~07:47Z and ~08:17Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 37-38 log (@`4e71c382ad`, ~07:17Z). **State: ARMED.**

## Scope

9 laptop directives of 15 live. IRPT first: IRPT_BCKEND and DSGN_IRPTV1, both active / EXECUTING. Unread at the tick: 0.

## L10 -- DSGN_IRPTV1 rounds 5+7

- **The CVO's grades** (ADJUDICATION_v5 @`ef3adb67c4` + @`f5777670db`), on the window-9 walk:
  - judgment criteria: IVE41 and IVE47 PASS, IVE48 NOT_EVALUATED, 8 FAIL;
  - per UIR id: 25 PASS, 16 FAIL, 5 NOT_EVALUATED.
- **The slug** (CVO 101844, REMEDIATION_v3 @`e5c8c76afb`): 18 rows, 12 disarmed, 6 open. It asked for rulings on
  W29-S8 and W29-S10 and for S17 to be routed.
- **The round-N analysis** (this seat, @`36e18bf320`,
  `deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND7_20260927.md`):
  - the 16 FAILs become the round-8 enrichment list E1-E11;
  - W29-S8: a product-path cell for `scripts/dev-live.mjs` and `contracts/adapt.ts`, with no wider Q;
  - W29-S10: the S7 bar is graded under a pinned runner (3 identical failing sets, a subset of Q, no retries);
    W29-S9 is folded in and TO-IV-e-50 is superseded;
  - S17 (the AI drill 403s) goes to ADVI_PERFRP's owner via 0.0.0_AB_MSTR (msg at 07:52:18Z);
  - S19: the disarm owner is MSTR's push of the untrack; the purge stays at Andrew.
  - Sent: ~D at 07:52:13Z, the CVO decision copy at 07:52:32Z.
- **Round 8 ISSUED by ~D** (@`83576f9dd9`): ten cells, IV-e-54..63, over decomp v8, cut from the analysis in one
  issuance.

## Open calls in scope

One, CARRIED at Andrew: the purge of the S19 screenshots from git history. REC: keep history.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE (no members).

## Waiting on other seats

| seat | owes |
|---|---|
| ~D | round 8 (IV-e-54..63); TO-IV-e-53 (the Export tenant fix) |
| ~P | window 11's K8 packet once IV-e-53 lands; the request-list route (E9 / S18) |
| 0.0.0_AB_MSTR | the push of the S19 untrack @`cfed2c067b`; S17 routed to ADVI_PERFRP |
| ~M | Monday 09-28: R1, then the COT cash-line act (S155 alone) |

state: ARMED
