# L4-R REVIEW -- POSN_ASTTAX PRD v0.11 @ab2ee8052a, BRIEF HALF -- SIGN

**Reviewer:** 4.0.0_SA_CRO~Z (brief half; `TREE_PRD_SIGNOFF`; the seated CRO lane for POSN_ASTTAX -- Andrew ~03:5xZ @9dfee40ce0)
**Delivered by:** `1.0.0_SA_CTO~Z` msg 23003, 2026-09-15T04:07:48Z (the router again named `~W`; the half is `~Z`'s by Andrew's word)
**Reviewed:** 2026-09-15 ~04:1xZ (seventeenth review of this PRD by this seat)

## CONTROLS RUN BEFORE THE STAMP

| control | read | result |
|---|---|---|
| last-touch of the PRD == the review pin | `git log -1 -- prd/POSN_ASTTAX_PRD.md` -> `ab2ee8052a` (1.0.0_SA_CTO~Z, 2026-09-15T00:06:54-04:00) | MATCH |
| bump scope measured | `git diff --stat 59113e257a ab2ee8052a -- <prd>` -> +31 / -1: the header version line and ONE new s.0 ADDENDUM v0.11 block; no ENDPOINT byte | brief half only, as delivered; `prd-signoff.py status` before the stamp: ratified-text SIGNED current, brief STALE |
| **C-HOLDING-IDENTITY's measured basis, re-derived on this seat's own instruments** | the satellite ticker set derived from the 2026-09-14 rebalancer partition (nine `Opal Satellite` roots, sleeves' `components[].metadata.symbol`) = **25** tickers; DynamoDB `etf-classifications` scanned whole (285 items): rows present **25 of 25**, `name` non-empty and not the bare ticker **25 of 25**, `management_style` = passive 16 / active 8 / unknown 1 (CASH) | MATCHES the addendum's "all 25 satellite tickers carry name and management_style"; the `unknown` -> blank rule has exactly one member today (CASH) |
| the retag's landed state, seen in passing | GLD `commodities` / `Metals`, VXX `structured` / `Hedge` in the live table | R1 has landed in the served table; the lowercase raw spelling is the generator's normalisation contract (`Z-C-S42`), not a defect |

## CONTENT CHECK -- each entry, CONTENT not pointer

| entry | carries | verdict |
|---|---|---|
| verbatim | Andrew ~04:0xZ, entire (two items: the floats; "none of this is going through ETFClassifier", characteristics and performance blank) | matches relay 23003 held here |
| C-HOLDING-IDENTITY | `name` + `management_style` for every satellite ticker, read through ETFClassifier's one module, independent of the measures' precedence; NULL + counted where no row; render rule NAME (ticker only where no row) and ACTIVE (active YES / passive NO / unknown or NULL blank); beta overrides (PFDE, PFOE, UVXY) stay as Yang's spec | content present; basis re-measured above; the Yang-agreement figures (23 of 23 on both fields) are the CTO's and consistent with this seat's earlier read that Yang's `current_holdings` carries the same names |
| C-SUMMARY-COPY rounding clarified | at most two decimals, trailing zeros dropped; the defect named as the IEEE sum artifact; Models / ETFs labels byte-identical (82.6% / 17.4% -- matches the served ST allocation this seat read on 2026-09-14); "rounds like its two siblings" withdrawn with the reason (siblings round to whole percents) | content present; the withdrawal is the right call -- the sibling rule would have re-formatted every Models label |
| what it changes | brief half only; cuts no order; three issuer amendments inside round 6 named by order id | consistent with the gate read |

## TWO NOTES, NON-BLOCKING, RETURNED BY PINNED LINE

1. The addendum cites `PositioningSummary.tsx:1011` with no ref. At the recorded portal pin `e85f6eb84f` line 1011 is NOT the
   label (it is the close of a JSX block above the Custom-column placeholder comment); the line number belongs to the round's
   working ref (the worker's branch / the drain ref). A line citation carries its vintage or it is not a citation (Rule 22);
   the fix is `:1011@<ref>` on the next brief-half touch, never a touch of its own.
2. The ~04:0xZ word is carried verbatim with its screenshots and rows, but no `ANDREW_DIRECT_*` record path/hash is cited for
   it, unlike every other addendum. If a record exists, pin it on the next touch; if the rows are the record, say so.

## VERDICT

**SIGN.** Stamp: `python .tools/prd-signoff.py sign POSN_ASTTAX --half brief --review <this file>@<its pin>`.
