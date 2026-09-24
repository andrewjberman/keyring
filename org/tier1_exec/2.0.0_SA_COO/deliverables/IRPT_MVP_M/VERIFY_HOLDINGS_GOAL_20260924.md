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
