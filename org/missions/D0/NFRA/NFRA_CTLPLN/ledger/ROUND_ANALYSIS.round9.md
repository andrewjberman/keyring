# NFRA_CTLPLN -- ROUND ANALYSIS (L10), round 9, closed 2026-10-12 ~12:3xZ

Author `1.0.0_SA_CTO` (laptop). Slug: `3.0.0_SA_CVO~L` msg 108535 on `2.0.0_SA_COO~C` msg 108534; compile ADJUDICATION_v11 +
REMEDIATION_v3 @25bbc02279. Previous: `ROUND_ANALYSIS.round8.md` @2f10c5c1cf. PRD v0.25 (ratified half SIGNED current
@4af2d1a4f1; nothing owed there, whatever the issuer's list reads).

## 1. What the slug carries, and the rulings

| item | the CVO's read | ruling |
|---|---|---|
| round 9 orders | TO-CT-y-1 (crossbox design: HALF-CLOSED/OPEN wording) complete; TO-CT-y-2 (dell1 fresh-process blocked download, E1's Dell leg) complete; 33 orders in scope, 31 complete, proof_bad 0, 2 of 2 judgments graded, MAY-CLOSE | round 9 is finished on this box |
| S9112 | GRADUATED, still ARMED; disarm owner Andrew (purge + refresh-token invalidation); retention 14 d, so the pre-fix credential lines age out by ~2026-10-26 if no one acts | stands; listed to Andrew 11:5xZ; the CT-w-10 apply (no new credential written) is the fix already live |
| W70-S1 | DISMISSED (CT-w-8 amendment 1 set the expected count to 3; re-run) | accepted |
| W70-S2/S3, W71-S1..S3, D1-S11 | noted, gate nothing | stand as noted |
| W61-S1 | graduated, ARMED at Andrew | unchanged |
| all 66 gating items | dispositioned | the channel is clean at this close |

## 2. Grades (delta from round 8)

FWD-28: fence live on all 41 routes and the log no longer carries credentials (CT-w-10 applied); REALIZED still waits on the
portal carrier landing on DEV (registry notes, ruling 108503; portal commit 53506d49 with `0.0.0_AB_MSTR` pushing). FWD-3/22:
the crossbox state wording is now exact. FWD-1 (the re-based live thread): its Dell leg exercised (CT-y-2); the full thread --
planned on the laptop, worked and pushed by dell1, merged by the integrator -- is still the E1 outcome to prove end to end.
FWD-27: unchanged, gated on Andrew.

## 3. ENRICHMENT LIST for round 10 (ONE issuance, `2.0.0_SA_COO~C`)

- The portal carrier on DEV (confirm the MSTR push landed; move the gitlink; re-run the 10 checkout tests) -- FWD-28 REALIZED
  reads on it.
- E1 end to end (the thread, all hops, with the receipts the 10-09 analysis names) and E4 (the 12-message cross-box matrix);
  E2/E3/E5-E8 carried with a stated reason each.
- E9 FWD-27 stays gated on Andrew's keys and elevated lines; S9112's purge and invalidation stay his.
- No new cell for S9111 (the partner `/api/scoped/partners` route reaching the proxy's `$default`): owner the shared portal API
  root; a one-line row only.

## 4. Owed outside the project

Andrew: W61-S1's elevated line; S9112's purge and refresh-token invalidation; public keys + elevated line per box for FWD-27;
the PROD push of the portal carrier once on DEV.
