# Source input capture and historical cutoffs — 2026-09-22

## 2026-09-23 exact held-candidate commit preparation

The previously held source is unchanged: holdings_snapshot.py Git blob
`8a2011533d1b8ef173d2fcc0cb39bb07cfc58a7d`, LF SHA256
`5f310f5c26f66fbe66d62598253afbe8b8781fd4d4f86441086863147478190f`.
Final authority is CTO `15157a666c0f1cd0f720e2c3f678cc9f71c05715` and separately
committed carrier `0a7810c77273215fee26885ce1a321adb23a4d89`.
Ordinary safe-merge completed rc0 at `bb3f3ecd04f3d835050218827bd242de2e272ed1`,
preserving all six held files byte-for-byte and both index/worktree diffs before
this evidence update. The existing ownership rules/rulings were retained; three
old CTO oversight status rows were replaced with their current CTO versions.
Mechanism `5de3df146f`, protection `9a07a90f6e`, authority and carrier are ancestors.
Committed and working gate bytes match reviewed SHA256
`0ba14823bee91aef26d1ab6b6c640f0feb72fba938d2e5d35b5c9ff8732ed5f2`.
The committed-HEAD loader reports one usable entry, zero rejected entries.

Fresh local tests on this integrated candidate: Gold suite **121 passed**;
holdings suite **119 passed**. Naming preflight with --enforce: rc0, six literals
graded; exact Inflection **WAIVED-READ**, one existing SmartX RAISE warning and
four Cottonwood CONFORMANT warnings. This preflight is not the full source commit
result; the ordinary safe-commit receipt must separately establish success.
Case expiry is 2026-09-24T00:00:00Z with no automatic renewal. No gate override,
source repoint, source-scope expansion, live read/write, deployment or push was
performed in this commit preparation.

The three-firm canonical destination tests now exercise the held runner fix.
The older real-source probes below remain historical failed probes, not a fresh
published/E2E result. Calendar validation applies to _latest_date_partition;
the Eclipse helper retains its existing date-shape/completion-marker logic with
the new cutoff. These bounded tests do not establish full custody, source-clock
compatibility, economic reconciliation or publication correctness.

Authority: `IRPT_MVP_COMPLETION_20260922/CONTRACT.md`, M1/M4/M5. This extends the independently bounded-reviewed output publication candidate `62139c3a1a`; it does not establish complete custody or a historical account/model crosswalk.

The runner now applies the requested business-date cutoff to partition selection. SmartX, Cottonwood assignment/blend/roster/custody, Inflection accounts and completed Eclipse partitions all receive the cutoff. This prevents a historical run from silently substituting a later assignment. Selection of a past dated table alone is not proof of complete dated ownership.

`source_inputs.VersionedInputs` captures every successfully read input with bucket, key, non-null VersionId, SHA256 and byte count. The first read is verified against a second exact-version read; repeat key reads remain pinned even if current changes. Unversioned, changed or oversized sources refuse. The per-object bound is 256 MiB. Both real-client dry runs and upload builds use the adapter. Listings still discover partitions; listed presence does not certify content or freshness.

The receipt bundle hash enters output `source_set_revision` and hence the content revision. Full receipts remain in the internal accepted manifest. Publication checks the receipt/hash binding before writes and bounds the full manifest. This does not turn optional/missing inputs into a complete population or make a stale input current. Missing critical facts still need builder-specific refusal or explicit coverage.

## Read-only source evidence

Local probe `.runtime/m-source-shapes.json` records exact versions, hashes, byte lengths and column/census metadata. No row-level client values or identifiers were printed. Measured at approximately 23:14 UTC:

| Source | Actual partition | Rows | Relevant population | Versioned |
|---|---|---:|---|---|
| COT monolith fact_holdings | 2026-09-21 | 19,527 | 974 distinct AccountID; 1,334 AssetID; relationship grain still must be collapsed | yes |
| COT model assignments | 2026-09-22 | 966 | 966 account_id; 963 account_number | yes |
| INF positions_mv | 2026-09-22 | 36,044 | 958 distinct account_id; 1,663 ticker values | yes |
| INF assets_v2 | 2026-09-22 | 36,044 | same position-shaped population, not a unique security master | yes |
| 49F Schwab master 08335338 fact_sec | 2026-09-21 | 2,490 | 2,466 distinct non-null CUSIP; 2,292 ticker values | yes |
| 49F Schwab master 08335338 fact_acc | 2026-09-21 | 7,523 | 7,523 distinct account_id | yes |

These are scoped source denominators, not a claim of all-firm custody. In particular the 49F probe covered one master only; model membership cannot replace the independently enumerated account population. A non-null identifier can still be blank, ambiguous or unsuitable for a vendor.

`comp-freshness chain cot` passed its legacy pipeline checks but is not a monolith holdings census. `chain inf` reported current positions/accounts and several stale older metadata/activity/household surfaces; it returned FAIL overall. `chain bd` declined its held freshness configuration under the repository sovereign hold. No bypass was attempted. None is a live IRPT E2E PASS.

Y agreed explicit local resolution fields `security_key`, `canonical_identifier`, `canonical_identifier_namespace` (TICKER/CUSIP/CASH), `resolution_revision`. Prices bind the local key, exact date, USD and source revision. Vendor-returned upload identities remain a separate retained fact. Current adapter implementation, accepted custody normalization and real authorized profile lookup remain open; no guessed S:ticker or profile defaults are approved.

## Real source build probe and tests

`m-holdings-source-probe.json` records read-only construction attempts for 2026-09-22. **None published or passed end to end.** 49F refused reconciliation despite passing schema. COT and INF reached landing but refused because the runner still supplied its legacy routed bucket while canonical publication expects the registered primary firm home. These are actionable findings for the next patch; the checks are not weakened here.

The full Gold suite passed **94 tests** after adding the source reader and historical cutoffs. The holdings suite passed **81 tests**, including receipt-bundle binding before any artifact write. The Gold suite includes existing read-only schedule/bundle checks; it does not activate schedules. The runtime import probe initially caught a missing local script import root, which was fixed before the passing result.
