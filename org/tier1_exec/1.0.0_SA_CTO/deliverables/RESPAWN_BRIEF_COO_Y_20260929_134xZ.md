# RESPAWN BRIEF -- 2.0.0_SA_COO~Y after the crash (Andrew-direct 2026-09-29 ~13:4xZ: "respawn COO~Y they crashed")

Written by 1.0.0_SA_CTO from live reads at 13:37-13:44Z. You are the WALKER of window 22, which is OPEN.

## Where you left off

- **Last commit:** `5426d09b28` 13:05Z (W22 preflight, all five bodies built and validated offline). Your worktree
  `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922` is clean. Your inbox has no unread mail; the last message you
  read was ~P 102810 (W22 OPEN).
- **Window 22:** ledger `org/critical_paths/.open_deploys/irpt-ui-walk-principal-w22-20260929.json`, operator ~P.
  - C1 closed 13:11:17Z. K1 is `USER#usr_irptuiwalk_1790687432`, created 13:10:37Z.
  - **The 120-min cap is 15:10:37Z.** Every body is terminal and credoff has run by then.
  - Legs Y, D1 and A1 are open. Leg Y is yours; D1 is ~P's credoff after your last body.
- **Uncommitted output:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/W22/` holds Y1_comparison_cottonwood.json
  and Y2_multicomp_cottonwood.json, both untracked.

## Body state, read live by the CTO

| body | K4 upload | K5 request | live state |
|---|---|---|---|
| Y1 Comparison `opal_long_term`, cottonwood | UP-bf609d33... NORMALIZED | REQ-7ea49c2d9b27957d0ea8888f, 13:14:45Z | **irpt-jobs state READY** (checkpoint_pdf + checkpoint_publication present) |
| Y2 Multi-Comp, cottonwood | UP-299bf8b1... | **never submitted** | **NORMALIZATION row NEEDS_CORRECTION, reason RESOLVE_RETRY_EXHAUSTED** |
| Y3 Target Weight, cottonwood | not started | -- | -- |
| Y4 Overview, 49financial | not started | -- | -- |
| Y5 Overview, inflection | not started | -- | -- |

The DLQ (irpt-generation-dlq) reads 1 visible / 0 in flight: unchanged from the 1 pre-existing message.

## What to do, in order

1. Register, arm /watcher, and read this brief plus the W22 packet (blob 1f3bf0914f @6550c62cdf) and your arms file
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/W22_PART_Y_ARMS_20260929.md` @ac0eade564.
2. **Y1:** case-trace REQ-7ea49c2d9b27957d0ea8888f to its terminal state, and read its `IRPT_RESIDENT_RESOLVE` line.
   The job reached READY, so S194's check passed: the PDF names `opal_long_term`. Record it as the S194 read.
3. **Y2 is TERMINAL as a named stop. Do NOT re-upload or replay it: the packet says no retry.**
   - The S193 bound fired LIVE on the same CSV (`aapl-vnq-12.03.csv`) that normalized for Y1 20 s earlier. Read the
     NEEDS_CORRECTION row itself (CTO condition 1) and the resident journal's resolve lines for UP-299bf8b1 by SSM,
     read-only.
   - File a surprise row: why did the vendor answer RETRY four times on a file it resolved at once 20 s earlier? Keep
     working after filing it.
   - Multi-Comp stays unexercised in W22. Carry it as an open arm.
4. **Y3, Y4, Y5 as armed**, one login, one K4 and one K5 each, no retry:
   - Y3 still runs. The bound has now been read on Y2, so Y3's pass is its own named terminal state.
   - Y4 and Y5 go through the foreign-firm name check (CRO condition 3).
5. After the last body is terminal, hand ~P the credoff: K1-CRED ParameterNotFound, K1 no-item. Then give leg Y's proof
   and the A1 route record. A1 includes a DLQ read: any growth over 1 is a BLOCKING row.
6. Commit the W22 outputs from your own worktree or through the shared index with safe-commit. Report to ~P.

If the cap (15:10:37Z) arrives before a body is terminal, stop submitting and let ~P run credoff at the cap. A hang
past the cap is a fail of that body, not a reason to extend the window.
