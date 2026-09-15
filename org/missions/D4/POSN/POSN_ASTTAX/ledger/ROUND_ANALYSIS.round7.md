# POSN_ASTTAX -- ROUND-7 ANALYSIS (L10; the LAST round analysis: the close)

**Author:** `1.0.0_SA_CTO~W`, on Andrew's word at this terminal 2026-09-15 ~15:5xZ, verbatim: *"Do me a favor and close out
POSN_ASTTAX. It is done officially but there is no other CTO online but you"* (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_155xZ_CLOSE_OUT_POSN_ASTTAX_NO_OTHER_CTO_ONLINE.md`).
`1.0.0_SA_CTO~Z`, the project's CTO limb, is out on the API weekly limit until Sep 19 (measured by `0.0.0_AB_MSTR~Z`
~14:4xZ). This seat holds the limb for this one act and nothing else on POSN.
**Date:** 2026-09-15 ~16:1xZ. **The slug read:** `surprise-channel/remediations/REMEDIATION_v7.Z.md` @`41305718d4`
(`3.0.0_SA_CVO~Z`: 32 orders terminal, all proofs valid, 312 investigation rows dispositioned; the completeness read
`adjudications/ADJUDICATION_v11.Z.md`, C-S182..C-S189). **The COO's report:** `ledger/COMPLETION_REPORT.round7.json`
@`ac0ff45dfe` (7 of 7 COVERED; 38 cells, 32 orders, 28 terminal with a valid proof). **The grades:**
`ledger/COMPLETION_GRADES.round7.json` (this commit). **PRD:** v0.11 @`ab2ee8052a`, seven outcomes.

## 1. The two reads on two axes (the spine's close)

The COO's report is the coverage axis: every outcome names the cells that served it. The grades are the realization
axis, and by the spine they are read from the EXERCISED ARTIFACT each card's `DONE WHEN` names, never from the report.
What this seat read itself, with its instrument and vintage:

| read | instrument | result |
|---|---|---|
| the 28 distinct proof instances the report cites | `git ls-tree <cited sha> -- <path>` (exists at the cited vintage); `git diff --quiet <sha> HEAD` (unchanged since); `.tools/proof-of-spec-check.py <instance> <its own criterion list>` | **28 of 28**: at vintage, unchanged, VALID rc=0; every instance PASS on every mechanical criterion, one UNVERIFIABLE-BY-INSTRUMENT judgment limb each (the CVO's plane) |
| the served models file `s3://opal-data-portal-v2/json/positioning/positioning_data.json` | `head-object` (VersionId `aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou`, 2026-09-15T11:06:20Z); the gzip body parsed by section | `data_as_of 2026-09-14` (= T-1); **110 of 110 current-holdings rows in exactly one class** (Fixed Income 59, Equity 48, Structured 3); the 91 classless ticker rows are `portfolios/*/holdings` (target allocations) and the six labelled benchmark definitions -- not holdings |
| the served satellites holdings `s3://opal-data-cot/platinum/satellites/holdings.json` | `head-object` (`5tjkvDfus1antRLsbDrLikcMQzH1Hk.F`, 07:00:20Z); body parsed | **177 of 177 rows classed, 0 classless**; classes fixed_income 74, equity 88, commodities 7, structured 8; VXX structured/Hedge, GLD commodities/Metals |
| the served characteristics `s3://opal-data-cot/platinum/satellites/characteristics.json` | `head-object` (`02SGBCPDoeVPy7JBJcEHxUw4J0.nQneh`, 12:30:54Z -- the scheduled fire); body parsed | 25 of 25 tickers; inputs 2026-09-15 / 2026-09-14 / 2026-09-14; valued fee 24, aum 24, returns 24, yield 22, beta 11 of 25 |
| the ETF-mode file `platinum/etfs/positioning_data.json` | body parsed | Equity 178, Fixed Income 8; generated 13:01Z, data_as_of 2026-09-14 |
| the promoted portal | `git -C portal fetch origin PROD`; `merge-base --is-ancestor` | origin/PROD `edf85ce5` CONTAINS the POSN leg `ebbee2e6`; the AMGT leg `9aef3734` does NOT (the control) |
| the presentation on the promoted tree | two seats' DOM reads read here: COO~Z `present_20260915_0813Z` @`ad3a87b244` (0 of 512 cells differing, 32 of 32 rows the served name); MSTR~Z `ASTTAX_INDEPENDENT_VERDICT_20260915_0840Z.md` @`580bc43d77` (544 of 544 cells, mutation arm discriminates, 0 unrounded) | PRESENTS PROPERLY; MSTR~Z's 08:40Z vintage qualifier (23 of 25 a day behind) resolved by the 11:00Z run, as the models file's `data_as_of` shows |
| the scope of "every place" (FWD-3, FWD-4) | PRD v0.11 C-POSITIONING-ONLY (supersedes C-TWO-SURFACES): the Positioning page only, 14 files; *"The Attribution page is NOT touched (two classes, Yang's layout)"* by Andrew's word | the Attribution page's three-class `ASSET_CLASS_ORDER` at origin/PROD is read and recorded as OUTSIDE the cards' domain, not as a miss |

## 2. The grades

| outcome | bar | observed | verdict | the artifact read |
|---|---|---|---|---|
| FWD-1 every holding in exactly one of five | EXERCISED | EXERCISED | REALIZED | the served models and satellites files (above); R1's retag V8-1 |
| FWD-2 volatility/hedge apart from equity | EXERCISED | EXERCISED | REALIZED | the same files: VXX Structured/Hedge, GLD commodities/Metals; T5-1's bar |
| FWD-3 one order everywhere (Positioning) | APPLIED | APPLIED | REALIZED | the registry V5-1, the renders V6-1/W3-1, the promoted head, two DOM reads |
| FWD-4 one colour per class everywhere (Positioning) | APPLIED | APPLIED | REALIZED | U1-1's 11-reader census, U2-1, V5-1, V6-1, two DOM reads |
| FWD-5 one source flows everywhere | EXERCISED | EXERCISED | REALIZED | S1A-1 (ETFClassifier), R1 in the single source flowing to both surfaces (V8-1), the guard V3-1/U3-1/X1-1 |
| FWD-6 the Positioning modes agree | EXERCISED | EXERCISED | REALIZED | the three modes read on the promoted tree by two instruments; the presence rule over the served inputs |
| FWD-7 Satellites shows characteristics and performance | EXERCISED | EXERCISED | REALIZED | the served characteristics artifact at the scheduled fire; W1-1/W2-1; the two DOM reads of Satellite 15 and 80 |

**7 of 7 REALIZED; no grade cites a state below its card.** `CLOSED` follows mechanically (R6).

## 3. Rows, and the one disarm the CTO owed

The slug's one row `POSN_ASTTAX-Z-C-S189` (REMEDIATED): C-S177 -- the seeder guard's owned tuple vs the R1
`management_style` write surface -- is answered by TO-X1-1 (3 of 3 fields agree; management_style is outside that
writer). C-S177's investigation-plane disarm was `1.0.0_SA_CTO~Z`'s; this seat files it in this commit as a citing
row (`DISMISSED_WITH_REASON`, adjudicating `POSN_ASTTAX-Z-C-S177`) on X1-1's proof and the CVO's C-S189. The COO's
`Z-S181` (three CVO completeness rows state another card's contract for FWD-3/4/5) is INERT: the grades above read
the cards themselves and the artifacts, not those rows.

## 4. What this close does NOT do

No POSN build, cut, cell, deploy, promote or push; no change to the `~Z` lanes' ownership of any later POSN round; no
act on any other `~Z` project; the standing holds (portal freeze until the promote itself, site-Z push hold, the
never-rules, the monitor moratorium) unchanged. The Attribution page's own class vocabulary is Yang's layout by
Andrew's word and is not a finding of this project. Push state: LOCAL (`0.0.0_AB_MSTR~Z` carries).

-- `1.0.0_SA_CTO~W`
