# CTO ROUND-17 ANALYSIS -- DSGN_IRPTV1 -- answering the rounds 14-16 L10 slug (2026-10-11 ~10:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/remediations/REMEDIATION_v8.md`
@17cccc75ee (3.0.0_SA_CVO msg 4686). **Prior:** the round-13 analysis @72e8e2bb59. **No PRD addendum.**

## 1. Where the project stands

**FWD-1 is NOT MET on the rendered walk.** Two walks ran tonight on DEV, by the laptop. Sign-in, search, the account pick, the
identity card and the security list PASS. Holdings reads PARTIAL (the category split is one layer in). Performance does not
hold. The suite on DEV reads 9 failing of 1,159 by the issuer's run, against 43 at the baseline.

## 2. Row D2-S11 (BLOCKING; owner this seat): which release may serve the Performance hop

**This seat's error, restated where it belongs.** The round-13 analysis and msg 4416 made a vendor-path release the fix for
this hop. That release served Cottonwood a vendor-calculated return, against IRPT_BCKEND's ENDPOINT (PRD line 498: a vendor
figure is only a comparison point), and was rolled back (ruling @210d01cb0c; the adapter read `9kYLdR64...` again at
10:04:34Z by this seat). The re-walk's PARTIAL at that hop is not evidence for FWD-1.

**The release the ENDPOINT admits is one that serves Opal's own return for the named client's account.** Two exist on paper:
IRPT_DASHBD's reporting read (its FWD-11, one firm today) and IRPT_BCKEND FWD-3's holdings-basis figure. Both stand on
Cottonwood's own data, and 2.0.0_SA_COO~C2 measured that data today (msg 4685; not re-read here):
- year to date, 9,613 of 80,390 Cottonwood account-days carry a return (12%); 659 of 769 accounts are measured on under a
  tenth of their days; 54 are measured on 90% or more;
- **the table ends on 2026-06-22**: no account has a day after it.

So neither source can serve a year-to-date return for October today, for any Cottonwood account, and for most accounts
neither can serve one at all. **This seat names no release for the hop in this round.** It rules it when two reads are in:
the walk's own account (measured days, year to date) and why the table stops in June. Until then no FWD-11 build is cut.

The row stays BLOCKING. FWD-1's client is named in the ratified text and this analysis does not change it.

## 3. The slug's other items and the rows

| row | ruling |
|---|---|
| **D2-S7** (BLOCKING; owner 2.0.0_SA_COO~D2) | The Performance half waits on section 2. The Holdings half is cut now: the Holdings face opens on the PICKED account's Models / SMAs / Client split, which is what FWD-1's words name. A product change; its candidate comes to this seat. This reverses this seat's msg 4427 ("do not change the page"): the reviewer has graded it. |
| **D2-W49-S9** (two tests on DEV excuse any route with no response schema) | First cell of the round: the excused set is asserted by name. A test that cannot fail when a route loses its schema is not a test of that. |
| **D2-W49-S7** (owner this seat): two response schemas do not declare `unprojected_grant` | The producer always sends it and the parser requires it, so the contract is the member out of step. IRPT_BCKEND declares it on `comparison-catalogue` and `analysis-request-pdf`. Placed with 2.0.0_SA_COO~P2, after its rollback closes. |
| **D2-W49-S8** (owner this seat): the smoke map at 22 keys or 12 | 22: one entry per scoped route is the map's own stated purpose. The two tests pinning 12 follow. The two routes with no producer fixture are excused BY NAME until IRPT_BCKEND publishes them. |
| **D2-S9** (owner this seat): the export-download answer borrows another fixture's members | IRPT_BCKEND publishes a schema entry and a fixture for that answer; same placement as W49-S7. |
| **D2-W49-S5** (owner this seat): happy-dom 20.14.6 | Closed by the override this seat required: portal c34b1c6a holds it at 20.14.5 (read by this seat in the lock diff). |
| **D2-W52-S2** (owner this seat): `frozen_as_of ?? null` | Ruled in msg 4631 and it stands as the answer: the contract never sends null, so absent is the only "none" and the coalesce conflates nothing; the scan records the line as an exception; iv-e-162 is not retired; the contract does not change. |
| **D2-W49-S3, S4, S1, D2-W52-S3, D2-W50-S1** | One hygiene cell each or batched: refresh the lock once on purpose; declare playwright-core or state the skip; the calendar generator refuses the fallback or carries it as a claim; the pin accepts either line ending; the three ids get owners. |
| **S7, W21-S2** (ARMED) | Two retirements remain unruled: the explicit-null `business_date` arm. The issuer printed the schema (a string, no null), so the arm now expects the parser's refusal and no retirement is needed. The issuer sends that line to the reviewer; the rows disarm on its read. |

## 4. ENRICHMENT LIST for round 17 (ONE issuance, in this order)

1. The excused set pinned by name (D2-W49-S9).
2. The Holdings face opens on the picked account's category split (D2-S7, second half).
3. The smoke map at 22 with two named excuses (D2-W49-S8).
4. The hygiene cells of section 3.
5. NOT cut: anything for the Performance hop, until section 2's two reads are in.

Items 1 to 4 are independent. Each build order carries at most three mechanical criteria. IRPT_DASHBD keeps priority on this
lane.

## 5. Acts only Andrew can do

- A portal PROD push of the Investor Reporting changes on DEV (CLAUDE.md, Agent Autonomy: a client-facing page).
- Any word that changes which figure Cottonwood's Performance tab may show (IRPT_BCKEND ENDPOINT, his word of 2026-09-28).

## 6. What this analysis did not measure

It rests on the slug, the reviewer's grade, the two walk records and 2.0.0_SA_COO~C2's counts as filed. This seat read the
adapter's live digest and the portal diffs it approved; it read no row of the returns table.

-- 1.0.0_SA_CTO~DELL2
