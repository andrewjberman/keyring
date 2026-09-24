# /verify -- Holdings end to end with the SNAPSHOT model overlay (Andrew's goal) -- 2026-09-24 07:2xZ

Verifier: `2.0.0_SA_COO~M` (the builder; instruments chosen to DIFFER from the publisher library that did the work:
the `.tools/aws` shim for every live read, an independent parse of served partitions, the function's own log group).
Goal: "Holdings end to end with SNAPSHOT model overlay for every 49 Financial and Inflection client, structurally
correct Cottonwood pipeline" (Andrew-direct 2026-09-23 ~22:4xZ; /loop 20m at this seat).
Done = the signed-in journey serves labelled Holdings with the model overlay at all three firms.

## VERDICT: UNVERIFIED@MECHANICAL (the deployed path has not READ the labelled revisions yet); DECLARATIVE PASS; SEMANTIC PASS

### MECHANICAL -- does the flow happen on the path the real user hits?
- Served objects EXIST and are the revisions claimed (aws shim `s3api head-object` / `get-object`, 07:1xZ):
  - 49F `s3://opal-data-49financial/irpt/49financial/platinum/holdings/current/manifest.json` etag ea06a1a0, version 9Vtkh61A, 06:58:45Z, row 2026-09-22 -> 3d59c80b
  - INF `s3://opal-data-inflection/irpt/inflection/platinum/holdings/current/manifest.json` etag d866755b, version .vBFsThYv, 07:04:38Z, row -> d03e91a4
  - COT `s3://opal-data-cottonwood/irpt/cottonwood/platinum/holdings/current/manifest.json` etag d81c9213, version mSFR0vat, 06:20:13Z, row -> dec293d6
  - one served partition per firm fetched by version id through the shim: sha256 equal to the revision manifest's (3 of 3).
- The deployed reader admits the members: irpt-holdings CodeSha256 kZygK57y.. (P 100327, 06:00:10Z) packages the
  schema copy carrying `display` + CUSTODY_UNITS; portal DEV 7c542fd2 carries the labels pin (MSTR 100365).
- **NOT EXERCISED:** `/aws/lambda/irpt-holdings` has ZERO events since 06:20:00Z (`logs filter-log-events`,
  start 1790230800000). Positive control: 104 REPORT events over the prior 30 h, latest stream event 04:32:51Z.
  So no signed-in client (and no seat) has read any of the three labelled revisions through the deployed function.
  The library-under-user reader matrices in the three receipts read the new revisions (75 / 13-32 / 76-105 nodes,
  every node labelled) -- the same code the function runs, under a different principal: EVIDENCE OF THE READER, not
  of the served path. This seat cannot exercise the path itself (an invented authorizer context is refused).
- Verdict: UNVERIFIED -- configured and served, not fired. Closes on ONE signed-in read per firm through the deployed
  function (Andrew's retest, the CRO's trace, or COO~D's IV trace), evidenced by the function's log + the rendered labels.

### DECLARATIVE -- does the record match reality?
- Overlays HOLDINGS_{49F,INF,COT}_MODEL_SNAPSHOT_20260924.json: published_revision + index.version_id == the live
  manifest reads above, 3 of 3 MATCH.
- Receipts HOLDINGS_49F/INF_LABELLED_PUBLICATION_RECEIPT_20260924.json, COT_LABELLED_PUBLICATION_RECEIPT_20260924.json:
  revision + index_version == live, 3 of 3 MATCH; each names the retained capture sha it was built with (49F
  032c68db.., INF 789dd95d.., COT none) and the CAS precondition executed.
- STATUS.md names all three served revisions and manifest versions (checked by string).
- Verdict: PASS.

### SEMANTIC -- is the served content the right thing?
- Independent parse of the LAST partition of each firm (fetched by version id through the shim):
  - 49F 752 nodes, 752 labelled (ACCOUNT 42/42, CASH 49/49, MODEL_LEAF 38/38, SECURITY 581/581, SLEEVE 42/42);
    a model leaf reads "Opal Long Term", a security "IEFA -- iShares Core MSCI EAFE ETF" (symbol IEFA);
    price facts 0; per-account children-sum vs account value within 0.01: 0 defects of 42.
  - INF 1,040 nodes, 1,040 labelled (ACCOUNT 20/20, MODEL_LEAF 15/15, SECURITY 984/984, SLEEVE 21/21);
    "Opal Intermediate Growth"; "IEFA"; price facts 0; 0 defects of 20.
  - COT 320 nodes, 320 labelled (ACCOUNT 17/17, MODEL_LEAF 13/13, MODEL_WRAPPER 11/11, SECURITY 271/271, SLEEVE 8/8);
    "Opal Intermediate-Term"; "BIV -- VANGUARD INTERMEDIATE-TERM BOND ETF"; price facts 0; CUSTODY_UNITS 268;
    0 defects of 17.
- Whole-population censuses over the bytes whose sha256 IS each served revision (the candidate census files):
  49F 151,582 of 151,697 labelled (27 directory-absent accounts, 88 ticker-less custody rows omit `display`);
  INF 33,327 of 33,328 (1 directory-absent account); COT 16,740 of 16,749 (9 directory-absent accounts).
  Reconcile exact at all three (1,835,875,624.28 / 209,358,359.48 / 548,412,662.59). Each labelled revision is the
  prior served tree to the node plus display (49F/INF: 0 ids added / removed; COT: the ruled re-cut published 03:56Z).
- Overlay grain: 49F 7 models / 7,475 accounts / 180 assets; INF 18 / 624 / 2,166; COT 7 constituent models / 521
  leaf rows / 119 assets -- every asset labelled; same model and account grain as the prior artifacts.
- Verdict: PASS on the served bytes. Not in scope of this pass: CUSTODY_UNITS for 49F/INF (built @d96513bc40, not
  published -- a disclosed absence, not a wrong value).

## Route
UNVERIFIED@MECHANICAL is closed by a signed-in read through the deployed function on each firm, owned outside this
seat (Andrew's retest / 4.0.0_SA_CRO's trace / 2.0.0_SA_COO~D's IV trace). The loop keeps driving: the units
candidate for 49F/INF, and re-reading the function's log for the closing evidence on each tick.

## ADDENDUM 13:5xZ -- the deployed path FIRED; the served revision is still the HAR's to show

- `/aws/lambda/irpt-holdings`: 6 invocations at 13:36:07-13:36:24Z (cold 1906 ms incl. 155 ms init; then 690 / 552 /
  635 / 634 / 576 ms; no error line) -- the first since 06:20Z. The function logs no application line, so the log
  proves the path fired on today's served revisions (the manifests read 5a25ae76 / d32e50c6 / dec293d6 since 09:04Z /
  09:00Z / 06:20Z), not which envelope was returned.
- Siblings in 13:30-13:45Z: directory-search 17 REPORTs (11 real searches + 6 warmer pings), performance-adapter 2
  requests at 13:36:11Z (internal SelectionUnsupported, public code UNEXPECTED -- P's hop 3 not served as named;
  reported 100658), everything else 0. Shape: one signed-in session; UNCONFIRMED as Andrew's until he says so
  (the CTO asked him at ~13:2xZ to load Anna on DEV with a HAR; CTO 100655).
- Verdict unchanged at the grain that matters: MECHANICAL moves from "not fired" to "fired, envelope unread";
  it closes on the HAR's holdings response read in place (revision / manifest version, display.label on the
  leaves, status READY) by the CTO or the CRO.

## ADDENDUM 18:4xZ -- goal criteria re-measured on the served revisions (closer mode, lease IRPT_BCKEND~M)

Served now (index reads through the library, 18:3xZ): 49F 5a25ae76 (index QC.bs6a5w, 174 parts), INF d32e50c6
(k9U4ucuT, 40 parts), COT dec293d6.

**(1) Signed-in journey.** Evidence: a signed-in HAR in Andrew's Downloads, `aaaaaa.har` (mtime 10:19 AM ET, 359
entries, 14:17:06-14:18:55Z), read in place. Only envelopes were printed; no header or token left the file. It matches
the function's own log: 5 REPORT lines at 14:17:32-14:17:47Z on `/aws/lambda/irpt-holdings`.
- COT: POST selections, then GET holdings, on two selections. Both READY / HOLDINGS_READY. The operation revision is
  dec293d6, the served row. Anna's pair returns 116 nodes, 116 labelled (2 wrappers "Rebalancer strategy: Anna *9237 /
  *9238", 7 leaves incl. "DIVZ SMA"). Her single account returns 41 nodes. unprojected_grant 0. **EXERCISED.**
- 49F: one selection, READY / HOLDINGS_READY on 5a25ae76. It holds 3 nodes (ACCOUNT, SLEEVE, CASH), all labelled: a
  Client-only cash account. The journey is **EXERCISED**, but no model node was on the path.
- INF: **ABSENT** from the HAR. Not exercised signed-in.
- The screen render (taxonomy + drill) is not provable from a HAR. It is the portal's; 2.0.0_SA_COO~D owns that surface.

**(2) Account census.** `HOLDINGS_ACCOUNT_CENSUS_49F_INF_20260924.json` @acaa51635d, by `holdings_account_census.py`.
Denominator: the served directory's ACTIVE entries.

| Firm | Active | With model | Client only | Refused | Silently empty |
|---|---|---|---|---|---|
| 49F | 7,454 | 5,908 | 1,509 | 37 | 0 |
| INF | 875 | 624 | 251 | 0 | 0 |

- **Refusal path:** a refused account raises `selected accounts absent from accepted publication` in the library.
  `snapshot.py:147-152` turns that into SnapshotUnavailable, which the public envelope reads as NOT_READY
  (`entry.py:146`). Explicit, never an empty 200.
- **Control:** the library's own `load()` on 3 accounts per class, 18 of 18 as classified.
- **The 37 refused 49F accounts** are RELATIONSHIP-scope entries with cohort UNKNOWN. Of them, 15 have no Black
  Diamond cross-reference; 11 are flagged in the 0833 universe and 11 are not. The publication header names none of
  them (0 of 37), so the user sees NOT_READY with no reason.
- **Published but not ACTIVE in the directory** (not selectable): 49F 105 (78 of them TERMINATED in the directory);
  INF 1.
- **Directory age:** as_of_business_date is 2026-09-17 at both firms, behind the 09-22 publication.

**(3) COT soundness.** Unchanged from the COT receipts: 841 accepted accounts; the refused population and the Black
Diamond window are disclosed in COT_LABELLED_PUBLICATION_RECEIPT_20260924.json and STATUS.md Parked (140 refused, CRO
re-check October 2026).

**Verdict: UNVERIFIED.**
- MECHANICAL closes on one signed-in INF read, and one 49F account that carries a model.
- DECLARATIVE PASS.
- SEMANTIC PASS on the served bytes and the census.
- Two enrichments: a refusal reason that names "not covered" rather than NOT_READY, and a disclosed refused-account
  population in the 49F header.

**The 37 refused 49F accounts carry no custody (18:5xZ).** Every raw account key in the build's four 49F source copies
(`.runtime/holdings-journey-20260923/`) was mapped through `ids.opaque` in 3 forms each (as-is, zero-padded to 10,
zero-stripped). The sources: Schwab dim_balance (business_date 2026-09-22, 7,522 rows), dim_position, fact_acc, and
the SmartX map (run_date 2026-09-23).
- **Matched to the 37:** 0 in every source.
- **Positive control:** the same mapping recovers 7,522 of 7,522 publication accounts, and 7,417 of 7,454
  directory-ACTIVE accounts.
- **Reading:** the 37 are ACTIVE in the 09-17 directory, and 49F custody holds no row for them at 09-22. The explicit
  refusal is the correct answer, not a dropped account. They sit in 29 entries (15 single-account, 14 multi-account).
- **Next-list item 3 closes on this read.**

## ADDENDUM 18:4xZ -- Andrew's second HAR (`bbbbbb.har`, 18:34-18:37Z), read in place

- **(1) EXERCISED at all three firms through the deployed API:**
  - INF: Greene ****1506 SIMPLE, READY / HOLDINGS_READY on d32e50c6. 5 nodes, Client-only, all labelled.
  - 49F: Alison Horton ****3941 IRA, READY on 5a25ae76. 19 nodes, including MODEL_LEAF "Opal Ultra Long Term" under
    the "Models" sleeve.
  - COT: READY on dec293d6 (14:17Z HAR).
  - The function log carries 6 REPORT lines at 18:36:11-18:37:01Z.
- **SEMANTIC FAIL on the screen.** Amounts render on a $10K grain: `portal/src/components/CategoryViewTree.tsx:360`,
  reached through `DrillTree.tsx:316`. The API carries cents, 24 of 24.
- **Journey defect on the firm tab.** `global/firms.ts:53` feeds the opaque firm id back as `selected_tenant`, and
  the server answers FIRM_BINDING.
- **Record and routing:** both are recorded at `ANDREW_DIRECT_20260924_184xZ_IRPT_FIRM_TAB_FILTER_AND_10K_ROUNDING.md`
  @af2dd7335d and routed to 2.0.0_SA_COO~D (portal owner).
- **Verdict: UNVERIFIED@SEMANTIC (screen).** It closes when ~D's fixes land on DEV and a re-walk shows exact amounts
  plus a working firm tab.

## ADDENDUM 19:0xZ -- both screen fixes on DEV; Andrew's eyes-on walk

- **2.0.0_SA_COO~D landed both fixes on portal DEV a65a8db5** (ls-remote read 19:0xZ; the 5174 main checkout is at
  a65a8db5 on DEV).
  - `FirmDropdown.tsx`: the internal viewer's tenant is no longer rewritten to the one-firm opaque firmId.
  - `CategoryViewTree exactAmounts`, turned on in `DrillTree.tsx:316`. Model Portfolios keeps its grain, per
    1.0.0_SA_CTO record @06730dfa2a.
  - ~D's run used stub fixtures (`DRIVER-FIXTURES-MATCH 5 of 5`): resolve tenants `["global","global"]`, against
    `["global","global","F-CW"]` before the fix.
- **Andrew, at the M terminal (~19:0xZ), verbatim:** "I just walked the Holdings page and it looks great, what did
  you want to confirm from the HAR exactly?" This is the signed-in, eyes-on screen check on the fixed build.
- **Still unread, in a HAR:** whether the firm-tab path sends the registry tenant, whether any FIRM_BINDING remains,
  and whether Holdings reads READY on the served revisions through a65a8db5.
