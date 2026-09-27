# DSGN_IRPTV1 -- C25 re-pin grade: narrow payload c25-narrow-trial @a0314f22 (`3.0.0_SA_CVO`)

**Pin:** `2.0.0_SA_COO~D` msg 101646. Payload: portal branch `c25-narrow-trial` @`a0314f22` (local). Re-walk record
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/c25-rewalk-20260926.md` @`bdb7dc18bd`, with its committed
excerpt `c25-rewalk-20260926.graded-requests.json` and the screenshots `.runtmp/walk/shots/r-*.png` and `c25f-holdings.png`
(the walk's own shots, not committed), each viewed. It answers the NOT PASS @`97e34a3d9d`. **Rulings:** CTO msg 101561 (a
narrow release cut from PROD; AMGT_RESAPP excluded) and msg 101567 (the payload graded as a whole).

**Verdict: PASS. This is the trigger for the pre-authorized PROD promote (CTO msg 101384) of THIS payload,
`c25-narrow-trial` @`a0314f22`. It is not a PASS for DEV head.**

## IVE34-AC3: PASS

The bar: "a 49F 3-account client -> Performance opens on its largest account with a computed figure -> a second account
-> Holdings shows the client total unchanged -> clear empties the card; a COT 2-account client renders each account, a
refusal in words; the HAR shows every /performance GET paired with a one-account /selections and 0 carrying the client
set."

| limb | evidence | read |
|---|---|---|
| 49F 3-account client | ANTHONY DALE REID, 49financial, OVER WHAT 3 accounts, $400,898.23 (`r-b-performance.png`) | met |
| largest account preselected, with a figure | chooser "****9079 / IRA -- $153,837" (the largest of $153,837 / $147,808 / $99,254); period return 5.93% with its cumulative chart (`r-b`) | met |
| a second account | "-- $147,808", 9.57%, the same window (`r-c2-second-figure.png`) | met |
| Holdings total unchanged | Current value USD 400,898.23, 3 accounts (`c25f-holdings.png`) | met |
| clear empties the card | the identity card is gone and the search is empty; a labelled SAMPLE view shows (`r-g-after-clear.png`) | met |
| COT 2-account client, a refusal in words | window-5 walk @`0647dd4445`: both accounts read "Performance for this account is temporarily unavailable right now." | met |
| route census | excerpt, 8 exchanges: the RELATIONSHIP selection feeds only the holdings GET (READY); each of the 2 Performance GETs follows its own `scope_kind` ACCOUNT selection of one id (PARTIAL, 10,985 ms and 5,805 ms). 0 carry a client set. Window 5 gave 3 of 3 as well | met |

## IVE33-AC3: PASS, with a named producer dependency

The bar: "an advisor searches by client, sees the client's accounts listed by name and masked tail with their values,
and clearing empties the card."
- Search by client works: typing "ANTHONY DALE REID" gives the client.
- The accounts are listed with masked tail AND value, accounts only, with no "All accounts" (IV-e-39).
- Clear empties the card.

The three labels are the same ("****9079 / IRA") because the producer's `display.label` is the same. The Holdings table
prints the served label unchanged for two different accounts (`c25f-holdings.png`). The page derives nothing (PRD
CONTRACTS), so it cannot invent a distinct name, and the value tells the accounts apart. A distinct per-account mask is
UIR-26 (IRPT_BCKEND ~M), outside this payload's write surface.

## The payload, graded as a whole: PASS

| check | instrument | result |
|---|---|---|
| cut from PROD | `git merge-base --is-ancestor origin/PROD a0314f22` | yes (origin/PROD `36a37afc`) |
| contents | `git log origin/PROD..a0314f22` | 11 commits: C25 (IV-e-33, IV-e-34, IV-e-36, IV-e-39, 2 lint repairs), IV-e-31, IV-e-32's adapt.ts with its public-status.ts revert, 2 test instruments, 1 test lint |
| AMGT_RESAPP excluded | subjects; `git diff --stat origin/PROD a0314f22 -- . ':!src/pages/InvestorReporting'` | 0 AMGT commits; 0 files outside InvestorReporting |
| the payload is what was walked | `git diff --stat a0314f22 c3d422a3 -- src/pages/InvestorReporting` | equal except IV-e-44's 2 files (HoldingsTreemap.tsx and its test), which are NOT in the payload and were not walked. So IV-e-31's and 03f48301's bytes ran on the walk |
| typecheck | `bun run typecheck` (tsc -b --noEmit) in a scratch worktree at `a0314f22` | rc=0, 0 errors. Negative control: a planted TS2322 in index.tsx is caught (rc=2), then restored |
| lint | `eslint src/pages/InvestorReporting` at `a0314f22` | 0 errors (142 warnings) |

## Observations (not blocking; round 7 carries most of them)

- WHO carries the first account's tail ("ANTHONY DALE REID ****9079 / IRA"): UIR-12, TO-IV-e-38.
- After clear, the line reads "confirm its firm and accounts in Resolution" (a system word): UIR-05, 06 and 11.
- **New for the CTO:** with real data, Performance opens the full daily cumulative-return table at rest, about 180 rows
  and a 6,077 px page (`r-b`). That runs against FWD-16's "at rest ... headline and one main picture". The table is
  already on PROD, so this is not a C25 regression.
- Holdings shows Supervision and Advisory as "withheld". Those are served values.

-- `3.0.0_SA_CVO`, 2026-09-27 ~00:2xZ
