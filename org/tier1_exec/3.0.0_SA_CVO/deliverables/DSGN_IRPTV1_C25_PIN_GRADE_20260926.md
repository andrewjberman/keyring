# DSGN_IRPTV1 -- C25 pin grade: portal DEV fe7beb7a (`3.0.0_SA_CVO`)

**Pin:** `2.0.0_SA_COO~D` msg 101556, candidate portal local DEV `fe7beb7a` (unpushed). Walk record
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/c25-devwalk-20260926.md` @`0647dd4445`, with its
committed excerpt `c25-devwalk-20260926.graded-requests.json`.
**What this grade triggers:** Andrew's pre-authorization (CTO msg 101384): "your PASS on that pin is the trigger";
MSTR then promotes DEV to PROD. The payload must be C25 as reviewed, and other unreviewed product changes need their
own word.

**Verdict: NOT PASS. The promote must not fire on this pin.** The routing core of C25 is proven. The two walk
criteria are not met, and the payload carries product changes that are not C25.

## What the walk proves (PASS on these limbs)

This was a real signed-in walk: a bounded admin + internal + Dev principal against the live IR API, on local DEV
through localhost:5174.
- **Performance is one account at a time.** The committed excerpt's 16 exchanges pair every Performance GET (3 of
  3) with a one-account `POST /selections` (`scope_kind` ACCOUNT, one id). The two RELATIONSHIP selections feed only
  holdings GETs (READY). 0 client-set Performance requests: FWD-19's route rule holds, read by this seat from the
  excerpt.
- **A refusal is shown in words.** Both of the COT 2-account client's accounts answer "Performance for this account
  is temporarily unavailable right now." One of them is the FWD-1 account, `acc_d486fc9455d6b2aa18e13af1`.
- **A computed figure renders for one account:** JASON JONES ****9978 (49F), 8.05%, PARTIAL.

## Criteria not met (FAIL)

- **IVE33-AC3.** The bar: "an advisor searches by client, sees the client's accounts listed by name and masked tail
  with their values, and clearing empties the card" (FWD-19, FWD-2). The walk searches by client (pass). But the two
  accounts both read "****9237 / BROKERAGE", which is the same label twice with no value, and clearing "was not
  exercised on this walk". The advisor cannot tell the two accounts apart, which also fails FWD-19's "Performance
  always says which account its figure belongs to".
- **IVE34-AC3.** The bar opens with "a 49F 3-account client -> Performance opens on its largest account with a
  computed figure -> a second account -> Holdings shows the client total unchanged -> clear empties the card". No
  such client was walked. The 49F read was a one-account client (JASON JONES), and the multi-account client (COT,
  Anna Thiessen) had no computed figure. Largest-account preselection, switching between two figures, the unchanged
  Holdings total and clear are all unshown. The chooser also carries an "All accounts" entry, which sits against
  FWD-19's "never shows a return for the whole client". It sent no client-set request, but it is offered.

The walk record itself files these as UIR-12, 15, 16, 19 and 20 for round 7 (TO-IV-e-38, 39, 45).

## The payload is not C25 only

`git log --no-merges origin/PROD..fe7beb7a` in the portal repo lists 12 commits (origin/PROD `36a37afc`):
- **C25:** `c55c4e29` (IV-e-33), `c12d37ae` (IV-e-34), `fdccc6e6` (lint repair), and `a5f073c2` (IV-e-36: the
  Export preview follows the focused account, which the ROUTE STRUCTURE names; its preview fetch was not exercised
  on the walk).
- **Test or instrument only:** `d556d7d2`, `8b36968e`, `1e821a6e`.
- **Product changes that are NOT C25** (non-test files):
  - `6712c742` and `5cd4e231` (AMGT_RESAPP, another project): `src/pages/SecurityAnalysis/tabs/ModelTab.tsx`, +95/-7
    in the net PROD..fe7beb7a diff, plus `__harness__/exportCompare.harness.cjs`;
  - `72ed1256` (IV-e-31, round 5): `tabs/holdings/DrillTree.tsx`, model colour by served code only;
  - `03f48301` (IV-e-32, superseded): `contracts/adapt.ts`. Its `public-status.ts` change is reverted by `0f61e0e1`.

These need their own word under the pre-authorization, or the promote payload must be C25 alone.

## What would PASS

1. A walk of IVE34-AC3's own path: a 49F multi-account client, Performance opening on its largest account with a
   computed figure, a second account, the Holdings total unchanged, then clear.
2. The account list showing each account by a distinct name, masked tail and value, with no "All accounts" choice on
   Performance. This is UIR-15 and UIR-16 in round 7; otherwise the CTO rules that this limb of IVE33-AC3 moves there.
3. A C25-only payload, or Andrew's word for the four non-C25 product commits above.

## Instruments

| question | instrument | result |
|---|---|---|
| walk content | the walk record @`0647dd4445`, read in full | as cited |
| the route census | the committed graded-requests excerpt, all 16 exchanges read | 3 of 3 Performance GETs after an ACCOUNT selection; RELATIONSHIP selections feed holdings only |
| the criteria | IVE33-AC3 and IVE34-AC3 read at HEAD in their task orders | quoted above |
| the payload | `git log --no-merges origin/PROD..fe7beb7a`; `git show --name-only` per commit; `git diff --stat origin/PROD fe7beb7a` outside InvestorReporting | 12 commits; 4 non-C25 product commits; SecurityAnalysis/tabs/ModelTab.tsx +95/-7 |

-- `3.0.0_SA_CVO`, 2026-09-26 ~22:4xZ
