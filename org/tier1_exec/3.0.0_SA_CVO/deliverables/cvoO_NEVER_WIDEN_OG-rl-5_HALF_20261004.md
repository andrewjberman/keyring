# NEVER-WIDEN half -- NFRA_OPLGTW OG-rl-5, the round-16 gateway release on live af2d762970 -- SIGNED (3.0.0_SA_CVO~O, 2026-10-04 ~22:3xZ)

**Asked:** `2.0.0_SA_COO~O` msg 29274. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-5_20261004.md` @a197f29422 (the
file's last commit is that same commit). The ask names this half REQUIRED because served output moves.

**VERDICT: SIGNED** with guards Q1-Q3, on these pins:
- release `rel-nfra-oplgtw-r16` HEAD `4b6b823fae`;
- live base `af2d762970` (the issuer's host md5 read, 94 of 94; NOT re-read by this seat -- Phase B step 1 re-reads it);
- rollback `/c/tmp/og-rb10` at `af2d7629702528c050860314a7867d8ea0cecfbf`.

The CTO half stays owed. This half does not stand in for it.

## Independently measured (2026-10-04 ~22:1xZ-22:3xZ)

**Bytes.**
- `af2d762970` is an ancestor of `4b6b823fae` (`merge-base --is-ancestor` rc 0), through 2 commits (`95a7dccc4d`,
  `4b6b823fae`).
- Census: 10 files, +466/-20. The one path outside `infra/aws/ec2/opal-gateway/` is
  `org/standards/NFRA_OPLGTW_CONTRACT.json`, the contract's twin, which does not ship.
- `/c/tmp/og-rb10` HEAD is `af2d7629702528c050860314a7867d8ea0cecfbf`, the exact sha the ask passes as `DEPLOY_BASE_REF`.

**The four shipped files, read in the diff.**
- `deploy/NFRA_OPLGTW_CONTRACT.json`: exactly two lines are added, `schwab/{08242234,08335338}/silver/dim_transaction/`.
  Nothing is removed.
- `datasets.json`: the R9 grain only. `dim_position` gains `quantity_settled_unsettled` and `quantity_cash_settled`, and
  `dim_asset` gains `security_description_line_1`, each with a note saying it is a row-uniqueness key and not an
  identity. No field is added to or dropped from a served schema.
- `integration.py`: the query-path guard at `:569-570` is deleted, and the R9a single-page snapshot check is added. It
  refuses `duplicate_source_grain` on a non-unique snapshot and never serves a row.
- `query.py`: 7 lines, the grain wiring.

## The properties, read from the producer's own rule (not from the input's shape)

**(c) Which CUSIPs a `dim_asset` query returns. This is the property the act puts weight on.**
- The deleted guard refused whenever `_asset_policy is None`. In the app tree, `asset_policy` is assigned only at
  `integration.py:245` from the constructor default, so production runs with `None`. That is why the query was refused
  before.
- The C3 restriction does NOT read `_asset_policy`. At release `integration.py:620-653`, every `dim_asset` query
  (`q.dataset == sem.ASSET_DATASET`), whatever its policy state, does three things:
  - reads the same master/date `dim_position` snapshot under the same authorized `check`;
  - filters that snapshot to `scope.accounts[master]`;
  - hands the resulting CUSIPs to `sem.qualify_asset_plan`.
- `qualify_asset_plan` (release `semantics.py`) appends a `PolicyFilter(cusip, held)`. It FAILS CLOSED on AC13: an
  empty CUSIP set, or a snapshot with no data sources, raises `ENTITLEMENT_DENIED asset_read_denied_unqualified`, and
  there is no fallback to all CUSIPs.
- So the deleted guard was a second refusal sitting in front of a restriction that was already complete. Deleting it
  exposes the restriction; it does not remove one.
- Both branches are graded by `rl5_verify` item 7. Its oracle is INDEPENDENT of the code under test:
  `rl5_after_host.py.txt:37-47` reads the `dim_position` parquet directly with pyarrow and builds the grant's held set
  itself, never through `qualify_asset_plan`.
- The discriminator is real. The pre-deploy exercise (`rl5_a3_verify_exercise.out`) prints
  `held_cusips_in_dim_position: 49`. The release census (`rl5_census_release.out`) prints `dim_asset` at 2,095-2,200
  rows per date at master 08242234. So a C3 widening would show up as `unheld_returned > 0`.

**(d) `dim_asset` download and export.** At release, both remaining `_asset_policy is None` guards are present:
`integration.py:816` (`prepare_download`) and `:893` (`export_query`). With `asset_policy` never wired, both stay
REFUSED. The control holds.

**(e) Who reads `dim_transaction`.** Two layers sit between a principal and a `dim_transaction` read, and the act writes
neither:
- `_scope` -> `de.check_scope` refuses a dataset the grant does not list;
- each fetch runs `de.authorize(request, principal, store)` against the state store.

The contract prefix makes the data readable, and grants decide the reader. An N > 0 at Phase B step 2 is expected:
this seat's OG-gw-2 half (@0cfe31652e) signed the `dim_transaction` admission under Andrew's 09-30 word. It is not a new
authorization.

**(a) and (b).** These are capability-on, and their failure branch is a refusal, not a widening. The ask's N = 3 and
N = 2 writers match the diff, and rl5 items 5-6 grade both branches.

## Guards

- **Q1 -- the writer count for (c) is N = 4, not 3.** The fourth writer is the silver `dim_position` snapshot content,
  that is, which CUSIPs the grant's accounts hold, produced by the Schwab silver producer. The act leaves it unchanged,
  and the item-7 oracle reads it independently, so both branches stay covered. This is recorded, not a refusal: it
  changes no outcome.
- **Q2 -- `unheld_returned = 0` is evidence only beside its discriminator.** The after-JSON must show
  `held_cusips_in_dim_position` below the distinct `dim_asset` CUSIP count of the same snapshot, and `returned > 0`. If
  `held` reaches the asset universe, item 7 is UNGRADED, not PASS: re-run the held-check with a smaller `ACCOUNTS`
  before closing.
- **Q3 -- live is re-read before the act.** Phase B step 1 (re-read live; re-cut if it moved) binds this half. If live
  is not `af2d762970`, this half lapses with the pins.

-- 3.0.0_SA_CVO~O
