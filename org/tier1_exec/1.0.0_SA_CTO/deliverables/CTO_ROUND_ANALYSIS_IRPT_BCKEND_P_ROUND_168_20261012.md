# CTO ROUND-168 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering the round-167 L10 slug (2026-10-12 ~21:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `surprise-channel/remediations/REMEDIATION_v44.md` @1325d97848 (3.0.0_SA_CVO msg 6558), on
the drain packet `deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_167_P_DRAIN_END_20261012.md`. **No PRD addendum.**

## 1. Where it stands

Round 167 restored the frozen v1 schema (W334-S2 closed), built the C-CHAINCLAIM + PARTIAL release of `irpt-performance-adapter`
(IB-pr-482, not applied; both halves now signed: CTO half @63796cf95c, Branch A), merged `bd_adapter.py`'s rename (unapplied) and put
the portal reader on a candidate branch. The live resident's bindings read UNBOUND (the issuer's measurement), so W333-S1 breaks
nothing live; the staging fix rides the next resident release.

## 2. The portal candidate, reviewed (C-VALUEFACTS step 1)

`wk-IRPT_BCKEND-338-portal` @183860ba (parent on portal `origin/DEV` 53506d49, this seat's read). Two files:
`src/pages/InvestorReporting/contracts/adapt.ts` (+12/-4) and a new test (110 lines, 8 cases, synthetic values). Read by this seat:
the tiles read `start_value`/`end_value` on every provider; the market-value names are read ONLY when `lineage.provider` is
`BLACK_DIAMOND` and the contract member is absent; the window and currency guard is unchanged; `FIELD_MAP` names the contract
members. **APPROVED for DEV** as a product candidate; the box manager lands it as a fast-forward under `/govern`, VALGATE on the push.

**The visible change:** on holdings, 49 Financial and orion performance answers, the opening and closing value tiles show a value
where they read "not supplied" today. The Reporting tab is opened by partner-firm logins, so its PROD push is a CLIENT-FACING change
and waits on Andrew's word (push law; the CVO's v0.50 condition). Carried to him as an open call, held.

## 3. ENRICHMENT LIST for round 168 (~P, ONE issuance)

1. **The IB-pr-482 apply** (`0.7.0_AE_CloudOps~IB2`) under the signed pair, the COO half's seven limbs and Branch B's
   version-named-before-upload.
2. **C-VALUEFACTS, in order:** the candidate to DEV (item 2 above), a render of the Reporting tab on DEV read against a holdings
   answer; then, on Andrew's word, PROD; then the `bd_adapter.py` rename's own never-widen pair and apply; then the fallback's
   removal at that pair's close. No step starts before the one before it is read live.
3. **W333-S1:** nothing to cut; the staging fix rides the next resident release (after W328-S1's repair, per D2-S109).

## 3a. After the cluster lead's ruling on call 29b7 (2026-10-12 ~21:2xZ, relay msg 6570)

- **PROD:** call `dell2-20261012T211055Z-29b7` CLOSED, folded into Andrew's held promote `dell1-e7f2` ("No for now, I would need to
  visual smoke that + want a breakdown"), record `CTO_RULING_DELL2_29B7_IRPT_TILES_PROD_PUSH_NOT_YET_FOLDED_INTO_E7F2_20261012.md`.
  The tiles join that one breakdown; section 4's act is withdrawn.
- **The coupling, stated as the ruling asks: it is NOT DEV-only.** `bd_adapter.py` is a member of `irpt-performance-adapter`
  (`lambda-source-map.json`), the one live function behind both portals; this seat's gets for `irpt-performance-adapter-dev`,
  `-DEV` and `dev-irpt-performance-adapter` return not-found (positive control: the base name resolves). PROD's Reporting tab
  reads the market-value names only, so applying the rename before the reader is on PROD turns PROD's Black Diamond tiles to "not
  supplied" on a client-facing page. **So:** the rename is BUILT and its pair is written now; its APPLY waits until the reader is on
  PROD (the CVO's v0.50 condition stands). Not measured: whether some other DEV-only backend fronts the DEV portal.

## 3b. Correction after the DEV render (2026-10-12 ~21:4xZ; 2.0.0_SA_COO~P2 msg 6595)

`2.0.0_SA_COO~D2`'s `/ui-walk` on a local build at portal 183860bac0 (msgs 6582, 6593): **49 Financial shows NO opening/closing
value tiles at all** -- its answers render the total-return chart, the headline tiles never mount, and "not supplied" appears
nowhere (3 clients walked: 2 charts, 1 zero-value account refused "not available yet"). Section 2's "holdings, 49 Financial and orion
... tiles show a value" is WRONG for 49 Financial: this seat's error, a code read taken for a render. **The visible change is on the
holdings-basis and orion answers only.** Orion was not reached by the walk.

**Ruling on the orion ask: accept the code read and the test; no CRO chase.** The adapter test runs the ORION provider path through
the contract members (`value-facts-members.test.ts`, case 2), and the PROD promote is gated on Andrew's own visual smoke of DEV
(`e7f2`), which is the render that counts; a chase for a client name to put through a walk buys nothing that smoke does not, and
puts a client name on a seat's bus. The e7f2 breakdown line is corrected to "two providers, 49F unchanged (its page has no tiles)".

## 4. Acts only Andrew can do

- **PROD push of the Reporting tab's value tiles** (open call, held). REC yes: the tiles go from "not supplied" to the window's
  opening and closing value on three providers; no figure the page already shows changes.

-- 1.0.0_SA_CTO~DELL2
