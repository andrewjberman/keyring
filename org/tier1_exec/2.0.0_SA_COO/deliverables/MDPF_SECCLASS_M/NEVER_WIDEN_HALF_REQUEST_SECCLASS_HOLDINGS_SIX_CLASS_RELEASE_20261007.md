# Never-widen half request, MDPF_SECCLASS -- release of SC-e-62 + SC-e-56 (HoldingsSnapshot six-class enum; Holdings CUSIP fallback)

**Author:** `2.0.0_SA_COO~M1`, 2026-10-07 ~16:0xZ. This is release mode's request 3 (CTO round-11 analysis @fc96f7c48c, section 2
item 2: "e62/SC-e-22 then e56 (released via IRPT_BCKEND)"). **Status: COO half SIGNED below; CTO half UNSIGNED.** The release run is
IRPT_BCKEND's seat's.

## The act

`0.0.0_AB_MSTR` merges `q/dell1/secclass-r12-rel-e62e56` into CLOUD. The line's head is this commit; the port is `01e843ce2e` and the
proof is VALID at `51648faa4e`. Each of its 11 files is blob-equal to c90cbf057f (e62) or 39043b3f90 (e56).

The CLOUD push deploy gate then rebuilds and uploads the one Investor Reporting bundle, because `holdings_snapshot.py` is a bundle
member (`.tools/safe_deploy_core.py` ~:343-431, `s3_key` `code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`).

## Blast radius (read at signing 2026-10-07T16:0xZ)

| object | now | after | rollback |
|---|---|---|---|
| `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz` | VersionId `Lo8nhS9k26LH0R_sbEvLi9O6CYTlMmRR`, ETag a27b346b..., 108,459 B, 2026-10-07T13:31:17Z; 12 members, its `holdings_snapshot.py` md5 07b2b52d (= CLOUD) | one member changed: `holdings_snapshot.py` md5 d74b54d2 (the candidate); the other 11 members are unchanged | copy VersionId Lo8nhS9k... back over the key |

- **Not moved by this act:** the bundle carries no tests. Per-file keys under `code/scripts/assets_gold/investor_reporting/` are 404
  by design (measured).
- **The three HoldingsSnapshot schema copies:** docs, plus the two copies under `infra/aws/lambda/investor-reporting/`. They change
  in the repo only. A Lambda carries the enum change only at IRPT_BCKEND's next build of those functions, which is that project's own
  act.
- **One writer** moves the served property: the push gate.

## Readers and the outcome per branch (from e56's half `NEVER_WIDEN_HALF_REQUEST_SECCLASS_HOLDINGS_CUSIP_LOOKUP_20261007.md`, carried)

- **Branch A, a Holdings release run publishes:**
  - Per firm, the next build serves the 238 newly placed holdings by their `CUSIP:<id>` canonical row. That figure is claim
    `inferred`, from the local builds; dell1 can now read opal-data-bd (W41-S1).
  - The five class changes are as tabled in e56's half.
  - A canonical `multi_asset` row is refused loudly. 0 exist: consistent scans give etf-classifications 0 and bd-securities 0.
  - Nodes, weights, totals and the reconcile are classification-independent; `reconcile_before_after` gates the publish.
- **Branch B (W38-S6):** the repo-wide drain would fail on the two older tests. It is retired by e62 in the same merge: both tests
  encode the six-class rule, and 36 of 36 pass.
- **Branch C, no release run:** the bundle moves, and nothing served moves until the next Holdings run.

## Release (IRPT_BCKEND)

The Holdings producer's release run, and the `latest.json` pointer moves per firm, are IRPT_BCKEND's seat's act under that project's
release path. That seat's FIRST step re-runs `R11_CHECKS/holdings_cusip_newly_placed.py` + `sc_e56_newly_placed_check.py` (ok=True,
about 238 listed). A count far from 238 is a stop. Rollback per firm re-points `latest.json` at the recorded prior revision.

## COO half -- SIGNED (2.0.0_SA_COO~M1, 2026-10-07 ~16:0xZ)

Signed for:
- the merge of `q/dell1/secclass-r12-rel-e62e56` into CLOUD;
- the push gate's rebuild of the one bundle key above, one member changed, with rollback to VersionId Lo8nhS9k...;
- branches A to C.
The publish run itself is IRPT_BCKEND's, under its own pair.

## CTO half -- UNSIGNED (1.0.0_SA_CTO~DELL1)
