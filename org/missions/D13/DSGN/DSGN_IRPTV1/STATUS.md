# DSGN_IRPTV1 -- status (FAST: /closer-drive under the lease, drive-mode.log line 16)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.18
@5d44d0fa62. Reviewer `3.0.0_SA_CVO` (grades each landed pin after the fact). Authority: Andrew-direct 17:3xZ record
@229b3fd184; CTO placement @1d443e50db (msg 102388); LIVE_ARMS row `/canonical-drive 10m`, the FAST lease routing each
tick here. As of 2026-09-28T17:5xZ.

## Pins

| What | Value |
|---|---|
| Lease | FAST DSGN_IRPTV1, surface `portal/src/pages/InvestorReporting`, until 2026-09-28T19:47:43Z (presence-extended) |
| Working tree | the main portal checkout `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, branch DEV |
| Portal candidate pin | local DEV `28f5118c` (round 9 drained: IV-e-68/69/70/73/74/78/79) |
| Portal origin | origin DEV `c3dd9ca9`, PROD `a0314f22` (ls-remote read 17:5xZ); local DEV ahead 97, behind 0 -- every commit is this seat's or its workers' |
| Suite on 28f5118c | 933 pass / 27 skip / 5 fail (the 5 known); tsc -b 0; lint 0 |
| Screen | `localhost:5174` (dev-live from the main checkout) |
| Workspace push state | CLOUD LOCAL; the push is 0.0.0_AB_MSTR's |

## Live thread

State: LIVE END TO END on local DEV for Holdings, Performance and Analysis, with two defects on the face: the COT
eleven-account pie draws nothing (NEW-02, row S30) and UIC-09 reopened (row S29). The last walk was the CRO re-walk
@f330857833 on DEV 4b9df1e7, which predates the IV-e-70/73/74/79 drains.

## Round 9 at the boundary

Terminal and drained: IV-e-68, 69, 70, 73, 74, 78, 79. Superseded by this lease, unbuilt, rows moved below verbatim:
IV-e-71, 72, 75, 76, 77 (issuer close in each order).

## Next (in order; a defect that breaks the live thread goes first)

1. **S30 + IV-e-72 rows (UIC-10/12/13):** a negative account is a separate labelled line, never a slice, and the
   pie's shares sum to the positive total (DrillTree.tsx `donutRows` keeps negatives today); small slices move to the
   legend; every account reachable from OVER WHAT (IdentityCard.tsx list clipped). Real run: the COT eleven-account client.
2. **S29 (UIC-09 reopened):** "No source age yet" must not show before any source exists.
3. **IV-e-71 rows (UIR-32/34/49):** one account mask everywhere (`****1234 / TYPE`); ALL CATEGORIES draws no one-slice pie.
4. **IV-e-75 rows (UIC-18..22, W35-S2):** Analysis setup behaves like a form; Export on Analysis opens only on an
   answer-bearing report.
5. **IV-e-77 rows (UIR-45, UIC-14, UIC-17):** one client date format on Performance and the directory stamp; the
   source line in client words; the scope panel never prints 'unknown'.
6. **IV-e-76 rows (UIR-04/13/30, W35-S1):** firm display names from the registry generated view. Per CTO 102351 the
   view target lands in `lib/opal_naming.py`, outside this lease's surface: CTO reads the diff before it lands.
7. **UIC-03:** no fix of record yet.
8. CRO /ui-walk findings and Andrew's transcripts enter here as they arrive (CTO placement act 3).

## Write claims

`portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx`, `.../tabs/holdings/slices.ts`,
`.../global/IdentityCard.tsx` (item 1).

## Next proof

Item 1: a fixture test (11+ accounts, one negative; 3-account control), then ONE real run of Holdings on 5174 for the
COT eleven-account client with the pie's non-white pixel share read from the screenshot.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| K8 re-run window (adapter RENDER_DELEGATE fix + R11 RUNNING answer) | 2.0.0_SA_COO~P | served export path | AWAITED |
| K10 re-run window (irpt-status rebuild 3) | 2.0.0_SA_COO~P | served status path | AWAITED |
| Ruling on row W39-S2 (OwnedAnalysisRequestWire has no client field) | 1.0.0_SA_CTO | row W39-S2 | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| The one-line FAST notice to the CVO ("FAST from 17:47Z; pins graded after the fact") | 3.0.0_SA_CVO | the CVO is seated (not LIVE at 17:5xZ) |
| NEW-01 (49F YTD -100%, HIGH) | 2.0.0_SA_COO~P | ~P's first post-reboot item (CTO 102358) |

## Limits

No FAST pin is graded yet. The round-9 judgment criteria (AC2 rows) wait on the CVO's grade of the landed pins. PROD
promotion stays gated. Any deploy is WORLD and runs under the deploy ledger.
