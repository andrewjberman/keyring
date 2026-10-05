# DSGN_AMGTV1 -- CTO countersign of the round-41 completion grades, rulings and the round-42 list (1.0.0_SA_CTO~Z, 2026-10-05 ~16:3xZ)

**Input:** `2.0.0_SA_COO~D` msg 29685; `deliverables/2.0.0_SA_COO~D/round41/COMPLETION_GRADES.round41.json` @a5c89f6552. Graded on DEV
`e6ab82ad` against RESAPP `GS//XHnV`: 19 REALIZED, 4 NOT_REALIZED (FWD-4, 7, 8, 27), 3 NOT_EVALUATED (FWD-1, 13, 19), 1 RETIRED (FWD-3).

## Countersign

**COUNTERSIGNED,** with one grade moved: FWD-13 goes NOT_EVALUATED -> NOT_REALIZED (ruling 3). The tally becomes 19 / 5 / 2 / 1.

## Rulings

1. **FWD-7: a correction to my own round-36 ruling 2.**
   - That ruling's second grading branch ("the designed 'no list published yet' sentence with the source chain it tried") grades the
     PAGE's behaviour. It is not the outcome's realization.
   - FWD-7 is "A PM sees who runs the company, for every covered name". It cannot be REALIZED while 84 of 95 names show no officers.
   - **The grade stays NOT_REALIZED.** The page component passes (ASML shows 7 officers with the source named; AMD and MSFT show the
     chain-tried sentence).
   - **The cure is the producer's officers for the 84.** RESAPP's stored sources yield 0 more (round 70), so the remaining source is the
     Bloomberg exec-officer pull, row Z-W227-S1. That is Andrew's act: a vendor use no word of his names.
2. **FWD-4 (ROG SW 3 of 7, no reason visible).**
   - The producer now serves a reason per missing figure (RESAPP r70 c30 YES). So the page shows that served reason in the missing
     figure's place, in words: a designed absent state from served words, which FWD-27 permits.
   - Completeness on non-USD names stays NOT_REALIZED until the figures exist.
   - RESAPP's round-72 census lists, per covered name, which of the seven are missing and the cause.
3. **FWD-13: the open question since round 32.**
   - The DONE WHEN says the tooltip carries "the full-precision value verbatim". A value carried only in `data-full-value` (the DOM) does
     not meet it.
   - The ACCEPT forbids a raw float ("No 161867780096.00003 anywhere"). Both hold when the tooltip prints the full-precision value
     formatted: thousands separators and its unit, with no float noise (for example "USD 161,867,780,096").
   - Grade: **NOT_REALIZED.** A round-42 page cell.
4. **FWD-19 (only the no-permission limb unread).** It is exercised by a simulated viewer whose `firmId` is not `opal-capital`: the
   walker rewrites its own auth response, browser only, with no server write. The page shows the designed no-permission state.
   NOT_EVALUATED until that read.
5. **FWD-8:** the page side is fixed (no cross-currency average). The numeric tickers are the producer's, routed to RESAPP.
   NOT_REALIZED.
6. **FWD-27:** the Exec tab's "yet:No" wording becomes plain words. A round-42 page cell.
7. **FWD-1:** its DONE WHEN is "one live walk, signed in with a real account ... on the live product". It waits on the PROD promote,
   which Andrew holds until RESAPP au-6's speed clarity. NOT_EVALUATED is correct.

## ROUND 42 (ONE issuance by `2.0.0_SA_COO~D`)

1. **FWD-4:** a missing header figure prints the producer's served reason in its place, in words.
2. **FWD-13:** the tooltip carries the full-precision value, formatted with separators and its unit, with no float noise.
3. **FWD-27:** the Exec tab's "yet:No" becomes plain words.
4. **FWD-19:** the no-permission read through a simulated non-Opal `firmId` viewer.
5. **Then** the candidate goes to my review and a DEV push on Andrew's word.

## Routed to AMGT_RESAPP (`2.0.0_SA_COO~Z`, the round-71 analysis)

- The FWD-4 census of missing header figures and their causes.
- FWD-8's numeric member tickers.
- FWD-7's officers: Andrew's Bloomberg pull (row Z-W227-S1).

## Acts for Andrew (cited)

- **Row Z-W227-S1:** the Bloomberg exec-officer pull (a vendor use), the only path left to FWD-7.
- **The PROD promote** (his hold) and the FWD-1 live walk on a real account.

## ANDREW-DIRECT at the 1.0.0_SA_CTO~Z terminal (2026-10-05 ~16:4xZ): the no-permission concept

Verbatim: "On the no permission concept, no that is the wrong way to go about it, and I have already talked to COO~D about the proper
approach. It should simply not be visible if you are not permitted. E.g., you dont see a sidebar element for Security Analysis if you
are not an opal user. That is the easiest way to handle that."

Then: "I dont think we really need to go into the backend ops of how its not visible, because its just market data, not client data,
so im not that concerned at this stage about making that URL completely blocked to non Opal users."

**Effect:**
- My RE 29701 ruling (a) is WITHDRAWN; COO~D was told (my messages at 16:36:52Z and 16:37:31Z).
- Round-42 item 4 is ONE read: a non-Opal viewer sees no Security Analysis sidebar item.
- There is no route, redirect or backend work, and the existing route guard is unchanged.

## REVIEW -- round 42, portal `1135984d` (COO~D msg 29717), 2026-10-05 ~17:1xZ

- **Placement:** `1135984d` CONTAINS `origin/DEV` `e6ab82ad`, so it is a fast-forward. 2 files, `HeaderCards.tsx` and
  `ExecManagementTab.tsx`, +43/-7.
- **FWD-4:** a header figure served as `value: null` WITH a `reason` renders an ABSENT tile carrying that reason in words. A null with no
  reason prints nothing (FWD-27). This is correct.
  - **ROG SW still shows 3 tiles and 0 reasons, and the cause is the PRODUCER.** RESAPP at-1's `_header_figures` adds reasoned nulls only
    when a stored model block exists ("a name with no stored block still serves `[]`"), so a name whose tiles come from another path
    gets none.
  - Routed to `2.0.0_SA_COO~Z`: the reasoned-null rule covers every covered name, including those with no stored block, proven on ROG SW.
- **FWD-13:** the tooltip's "full value" row prints the served value with separators, the served currency first for money, and
  " million" for a MILLIONS unit; float noise prints whole. This meets "the full-precision value verbatim" with no raw float.
- **FWD-27:** the Exec tab now reads "No officer list has been published for this name yet.", with the served reason as its detail.
  The "yet:No" splice is gone.
- **FWD-19:** the sidebar is hidden for a simulated partner firm and shown for Opal, per Andrew's approach.

**APPROVED for DEV.** The push needs Andrew's word (a per-push word for product files) and is held at `0.0.0_AB_MSTR~Z`.
