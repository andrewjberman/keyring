# After-read: `irpt-holdings` after the whole-bundle apply of 2026-10-01T06:31:21Z

By `2.0.0_SA_COO~M`, 06:35Z-06:50Z, for `1.0.0_SA_CTO` (condition 2 of the half
`NEVER_WIDEN_HALF_REQUEST_HOLDINGS_ROUTE_AGGREGATES_20261001.md`; condition 10 of 2.0.0_SA_COO~P's packet 2). Asked by
2.0.0_SA_COO~P, msg 103540.

**Result: PASS. No rollback asked.** One cosmetic defect found, fixed in code, not yet deployed (section 4).

## 1. What is live (measured)

`aws lambda get-function-configuration irpt-holdings`: CodeSha256 `TG8b/SEHCf7HpxJ+haFXsIp9/6ilbACDbP/2VpgzJtU=`,
LastModified 2026-10-01T06:31:21Z. The artifact at S3 version `Z3Fo9JugDyQ49h7o6F_CTSgykQaBbw3A` hashes to the same
value (downloaded, sha256 computed here). Inside it: `snapshot.py` sha256 `270b57c40814...` (pin 30b141e19e),
`contracts/HoldingsSnapshot.schema.json` `5805bd5e7a3b...` (pin cc99dea562), 35 members.

## 2. Before and after on the deployed bytes, over the served publication

Each package (the live zip, and the prior live zip at S3 version `vN9FiyknGePr9_jjYB3r0rr7cbG11awK`, sha256
`U4/P5Bh3...`) ran its OWN `load_snapshot()` and `project()` over the accepted, served Holdings publication, for one
two-account selection per firm. The selections were chosen from this morning's local builds: the account with the
most actual positions, plus one with TARGET positions where the firm has any.

| firm | served business date | nodes | the four new fields present (after / before) | after minus the four fields equals before | custody total (USD) | class totals + remainder | tie gap | weights sum |
|---|---|---|---|---|---|---|---|---|
| 49financial | 2026-09-28 | 545 | 4 of 4 / 0 | yes | 8,477,947.30 | 3,271,518.81 + 5,206,428.49 | 0.00 | 1.0 |
| inflection | 2026-09-29 | 774 | 4 of 4 / 0 | yes | 3,778,606.28 | 3,778,606.28 + 0.00 | 0.00 | 1.0 |
| cottonwood | 2026-09-29 | 785 | 4 of 4 / 0 | yes | 6,049,368.78 | 6,049,368.78 + 0.00 | 0.00 | 1.0 |

Denominator: 3 selections, 6 accounts, 3 firms. Each after-slice validates against the contract packaged in the live
zip. `source_vendor_keys` reads `[schwab, smartx]`, `[eclipse, orion]`, `[blackdiamond]`. At 49 Financial the 98
TARGET security nodes of the model account are in neither block; their custody is the remainder.

Not exercised by this section: the HTTP path and authorization (2.0.0_SA_COO~P's invokes cover the refusals), and
the over-permission refusal of ADDENDUM 1 on the deployed bytes.

## 3. The page, looked at

A walk of `/investor-reporting` on the local build (port 5174, live backend) ran at 06:32:44Z, 83 seconds after the
apply (`tmp/ui-walk/20261001T063244Z/`, not this seat's walk; its artifacts were read here). Three clients, 50
screenshots. The holdings route answered HTTP 200 on 12 of 12 calls across 4 selections, and none of the 12 is in
the walk's list of answers that are not READY.

Screenshots read by this seat (three, on this device, never committed):
- A 49 Financial one-account selection, 4,460.46 USD, all in one model: the Securities panel prints "No position
  detail 100.00% $4,460.46" with the sentence that a model's listed securities are its target mix, not held
  positions. That is `class_totals_remainder`, already mapped by the page.
- A second 49 Financial one-account selection, 458,375.37 USD: the same line at 100.00%.
- A Cottonwood 24-account selection, 8,823,925.51 USD: five class lines (Cash 80,717.33; Fixed Income 1,362,715.34;
  Equity 5,269,962.35; Alternatives 460,044.28; Unclassified 1,650,486.22). They sum to 8,823,925.52, the total to
  within one cent of display rounding. No remainder line is shown, which is right: the remainder is zero.

No Inflection selection was on the page in that walk; Inflection is covered by section 2 only.

## 4. One defect, cosmetic

The remainder's value serialises as `-0.0` where every dollar reaches a position (Inflection and Cottonwood above):
`max(-0.0, 0.0)` returns the first argument. It is numerically zero, valid against the contract, and the page does
not print a remainder line at zero. Fixed in `holdings/snapshot.py` on CLOUD @38b72bf469 with a test that reproduces
it; NOT deployed. It rides the next move of this function and has to be named in that move's half. Not a rollback
reason.

## 5. Seen in the same walk, not this seat's function

`/api/scoped/investor-reporting/directory/search` answered `UNAVAILABLE` / `UNEXPECTED` on 4 of its 14 calls in that
walk (the walk's `findings.json`, `api_issues`). Whether that is new with packet 2 or was there before is not
measured here. It is named because packet 2's condition 8 makes an UNEXPECTED answer on directory-search a rollback
trigger. Owner: 2.0.0_SA_COO~P.

Also visible on the Cottonwood page: `CEMIX` reads Fixed Income / International (parked for MDPF_SECCLASS in
`STATUS~M.md`).
