# AMGT_HARVST / Lead Panel step 2a -- current state

Seat `2.0.0_SA_COO~Y` (Claude, site Z, PID 37052; the Codex companions were reaped on Andrew's word 2026-09-24
~03:0xZ). Mandate `COO_Y_LEADPANEL.md` as corrected by R-19 @815d6c75da and R-20 @9faf3497d4. One project on
this lane: AMGT (the IRPT ~Y instance is dead, PID 27444). Own worktree `C:/tmp/coo-y-leadpanel-20260924`,
branch `closer/amgt-leadpanel-y-20260924`. Trunk `CLOUD`; commit only, `0.0.0_AB_MSTR~Z` pushes.

## Step 2a -- BUILT, NOT DEPLOYED. Nonpublishing by construction.

**lib/ half COMMITTED** at `6e9868b903` (branch above): the reviewed safeguards of `4dc4b667f3` /
`ac4316c447` / `621bf1d5d7` / `56621b4949` / `1b6cd9d4e0` / `b6eeef6ebd` carried byte-for-byte onto a
CLOUD base (12 files, merge-base `4756dde175`, CLOUD untouched since), plus one addition of this lane's own:
`pool_reader._gold_latest_snapshot_rows` memoises the parsed snapshot by (bucket, key, ETag) within a run.
Tests: 217 at the carry, 181 (coverage + metrics + handler arms) after.

**infra/ half is a PINNED PATCH, not a commit**: `H03_2A_INFRA.patch` beside this file, 41,198 bytes, sha256
`4cffba6dade024209564c9ec26bef4c316626ded0c03307174177344fad89ebf`, applies clean on CLOUD @`4845974639`. The
five paths resolve to lane `CLOUD_OPS_OR_ETL`, where the owned-paths hook REFUSED `2.0.0_SA_COO~Y` at commit
(three `lambda_src/*.py` violations printed; the `.tf`/`.sh` sit in the same tree). Per the mandate a refusal
at a granted path is a BLOCKER, not a workaround: no author override was used. The patch carries the handler
(`CHATTER_AXIS_SOURCE` validated against `SOURCE_COUNT_FNS`, same `count_fn` on both compute paths, `{"dry_run":
true}` -> `write_fn=None`, `clear_caches()` per invocation, `names_with_links` printed WITH its population),
`build_zip.py` (closure root `lib.opal_naming`, registry + `NAMING_SCHEMA.json` data members, pyarrow 15.0.2 +
numpy 1.26.4 copied from THIS ACCOUNT's layer `pyiceberg-nessie-deps:3` under pinned sha256
`DjKQluriv2wSb8e3H568gylHrD0Ed+f2sBlD9sCFWWw=`), `chatter-axis-schedule.tf` (moved onto `modules/yang-lambda`,
log group imported with retention kept never-expire, env `CHATTER_AXIS_SOURCE=gold`, 512 MB / 120 s, ONE additive
pool prefix `amgt/harvest/gold/chatter_daily/` = builder output), `build-and-upload-chatter-axis.sh`, and six
handler tests.

**Artifact of record (CONTRACT.md s.5a), both read back after upload:**
`s3://opal-313476888478-lambda-artifacts/harvest/amgt-resapp-chatter-axis.zip` -- rollback VersionId
`PUSLcUMaAwg.oPLW0ZdH6nO8t7ylo_eY` 669,924 B sha256 `I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=` (== deployed
CodeSha256); candidate VersionId `lPwA35XO3ZOG4KvCebxoJN1t45ljL1z9` 55,418,293 B sha256
`Xdwp7IrPaNho7y0Nz1L4TsihsueqDG+QDuvRsA+acYM=` (hex `5ddc29ec...7183`). Built 845 entries, 185,488,948 B
unzipped = 70.8% of the 250 MiB ceiling. Host smoke: packaged registry yields exactly the granted prefix.

**Plan against live state (worktree, backend S3): `1 to import, 0 to add, 3 to change, 0 to destroy`** --
role policy (+1 prefix), the function in place (`moved`, no replace; code hash `I6eitc...` -> `Xdwp7I...`,
env added, 128 -> 512 MB, 60 -> 120 s), the log group imported (tags only, `retention_in_days = 0` unchanged).

## Gates on the apply, in order
1. Never-widen pair: COO half FILED at `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_H03_2A_COO_HALF.md`;
   CTO half requested from `1.0.0_SA_CTO~Z`. No apply on one half.
2. The infra patch lands under an AE identity (`0.7.0_AE_CloudOps~A` held H03 steps 1-3) or on the CTO's
   route; then `HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply` from a tree carrying
   both halves, after `build-and-upload-chatter-axis.sh upload` has been confirmed to be THIS candidate's
   bytes (the S3 object is already the candidate; a rebuild is a different artifact).
3. Ledger `amgt-h03-leadpanel-y-20260924`: `baseline` and `artifact` CLOSED with proof; `pair`, `tf`, `daily`,
   `served` OPEN. Post-apply: a `{"dry_run": true}` invoke proves the Linux Arrow bytes and the gold read with
   zero writes; the 10:00Z fire is the `daily` leg (expected: both products FAILED / INCOMPLETE_GOLD_INPUT,
   RESOLVED 0 of 191, marker beside the retained 09-23 pointers, no pointer moved).

## Served consequence, read from the reader's own rule (scoped_amgt.py :555-653)
Once 2a holds, no new COMPLETE chatter pointer is written until 2b. Trending x Chatter serves the 09-23 two-row
generation `dated: true` through the 14-day lookback (last day 2026-10-07), then ABSENT. Breakout x Chatter has
no COMPLETE pointer in any window and reads ABSENT at every hour (today: ABSENT before 10Z, EMPTY after). That
is the disclosed cost of a nonpublishing cutover and is the CTO half's to accept or refuse.

## Parked (one line each, owner, un-park condition)
- 2b: populate `chatter_daily` gold for the AMGT universe -- Andrew scope item (R-19); un-parks when owned.
- `lib/research/price/**` explicit-state migration rides in `6e9868b903` for coherence -- `2.0.0_SA_COO~Z` may
  overwrite; un-parks on that seat's word.
- Tuple binding for the writer(Arrow 24)/reader(15.0.2) coupling (R-15/R-17 thread, initial tuple NOT_ACCEPTED)
  -- `4.0.0_SA_CRO~Z` holds the design; the dry-run invoke is the first target-runtime read and un-parks it.
- Hold helper cannot represent a preflight hold (tool gap, R-20) -- `1.0.0_SA_CTO~Z`.
