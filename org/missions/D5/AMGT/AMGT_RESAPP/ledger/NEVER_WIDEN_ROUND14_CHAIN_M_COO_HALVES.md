# NEVER-WIDEN CO-SIGN -- COO HALVES. Round 14, chain M (the model block). One section per co-signed cell.

**Signer:** `2.0.0_SA_COO~Z`, at the L6 cut, BEFORE any spawn. **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO halves at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_CTO_HALVES.md` (DESIRED plane). **This plane:**
APPLIED and EXERCISED. Neither half stands alone; each worker reads BOTH files before its first live act and STOPS with a
BLOCKING row if either is absent or lacks its cell's section. The four cells run SEQUENTIALLY (rk-34 on slot ~38 after
rk-33 drains; rk-35 -> rk-36 -> rk-37 on slot ~39), every one cut from HEAD after the previous drain, so no cell's
worktree carries `model_block_pull.py` or `scoped_amgt.py` bytes behind the shared branch.

**The shared rule for the whole chain, read once (STORE_CONTRACT rule 1, `integrations/bloomberg/research/
model_block_pull.py` as each order cites it):** every derived and raw write is a NEW STAMP under its key; nothing is
overwritten; the adapter serves a key only if the crosswalk carries it, and serves the NEWEST stamp. So the blast radius
of a derive is "a new newest stamp for the keys named", and the rollback of a derive is "delete the new stamp" -- the
previous stamp becomes newest again with no redeploy.

## `AMGT-rk-34` -- the unit map covers every name; re-derive over the 33 (R14-M1; FWD-10, M1)

**THE ACT.** `model_block_pull.py derive` over the 33 crosswalk keys (11 invocations of at most 3), each writing
`s3://opal-data-harvest/derived/model_block/<key>/<NEW stamp>/model_block.json`. NO Bloomberg request (a derive reads
the raw already landed), NO Lambda, NO Terraform. This is the one round-14 act that touches all 33 served names, and it
is authorized by the CTO's analysis row M1 exactly because it re-derives from raw already held -- it is NOT a re-pull
(Andrew's no-re-run word binds pulls; the order says so and pulls nothing).

**BLAST RADIUS.** 33 keys under `derived/model_block/`, one NEW stamp each. Served: yes -- every one of the 33 is in the
crosswalk, so the model tab's newest-stamp read moves for all 33 at once. Nothing else: no raw key, no crosswalk key.

**WRITER CENSUS of "newest model_block stamp per key": N = 1 writer** -- `model_block_pull.py` (derive and pull both
write through its one `_write_derived`); no schedule (the batch task `OpalResearch-*` families do not derive model
blocks; `comp-schedule` at the cut: 0). Rule: new stamp, never overwrite.

**EXPECTED OUTCOME, both branches.** Branch MAPPED: a name whose unit map now covers every mnemonic derives with 0
`unit: ABSENT` rows (AC3 counts them; denominator 33). Branch STILL-ABSENT (a mnemonic the map cannot express): the row
is written ABSENT with its reason -- the object still lands as a new stamp and is still covered here. Branch a derive
FAILS for a key: no stamp lands for that key, the previous stamp stays newest; the worker prints the key. All three are
covered by the same rollback.

**PER-KEY ROLLBACK, from the live pre-act state measured FRESH.** Pre-act: for each of the 33 keys, the newest stamp
name and its ETag (`list_objects_v2` per key; 33 lines in the entry). Rollback = `delete_object` of every stamp NEWER
than the recorded one, per key. The pre-act newest stamp is never touched, so the restore is a delete, not a re-put.

**NOT COVERED:** any `pull` (a Bloomberg request) on any name; any stamp under a key not in the 33; any adapter redeploy.

## `AMGT-rk-35` -- rolling history window, validation names only (R14-M2; FWD-1, FWD-16, M2)

**THE ACT.** ONE Bloomberg pull each for `CAT_US_Equity`, `CSL_AU_Equity`, `6861_JP_Equity` (within the validation bar)
landing `raw/bloomberg/<key>/<stamp>/{refdata,histdata}.json` (6 raw objects), then a derive landing
`derived/model_block/<key>/<stamp>/model_block.json` (3 objects), and `record_run` in the input ledger for three landings.

**BLAST RADIUS.** 9 objects on 3 keys, all NEW stamps. **Served: NO** -- the three keys are NOT in the pool crosswalk
until R14-I1 (`rk-31`) lands their identity AND that crosswalk object becomes newest; until then no route can resolve
them. This half is signed anyway because `rk-31` may land first (the two run in parallel), at which point these objects
become served the moment they exist. Both orderings are covered.

**WRITER CENSUS:** the raw prefixes -- N = 1 (`model_block_pull.py pull`); the derived prefix -- N = 1 (above); the
input ledger -- N = 1 (`record_run`). No schedule.

**EXPECTED OUTCOME, both branches.** Branch PULLED: 6 raw + 3 derived land, the window rule (the order's section 1)
yields `history_rows` >= the floor it names, per key. Branch REFUSED (terminal signed out, a field refused by the
budgeted sign-in, a name the entity test rejects): NOTHING lands for that key; the criterion is recorded REFUSED with
the surface named (READ_HERE s.2), never retried, and the other keys proceed. Covered either way.

**PER-KEY ROLLBACK:** pre-act `list_objects_v2` on each of the 6 raw and 3 derived prefixes (expected EMPTY at the cut;
re-measured at spawn -- if `rk-36`/`rk-37` have not run, empty; if a stamp exists, its name recorded). Rollback =
`delete_object` of every stamp newer than the recorded state.

**NOT COVERED:** any pull on a fourth name; any write on a covered name; a redeploy.

## `AMGT-rk-36` -- consensus forecasts with the SA fallback; adapter serves forecast_* (R14-M3; M3, C-MODEL-FORECASTS)

**THE ACT.** (i) the pull/derive of `rk-35`'s shape plus `bestdata.json` on the three validation keys, plus, for a name
with a Bloomberg gap and an entity-tested SA symbol, `raw/seekingalpha/<key>/<stamp>/{symbol,metrics}.json` (Seeking
Alpha AUTHORIZED by name for the `SA_FALLBACK` cells: PRD v0.13 @1699960261, C-SA-VENDOR-WORD lifted); (ii) ONE
redeploy of `opal-amgt-scoped-api` from THIS worktree's bytes through `build-and-upload-scoped-amgt.sh` (artifact
`s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, a new VersionId) and ONE targeted
`safe-apply -target=module.scoped_amgt_api.aws_lambda_function.this` (0 destroy; a non-zero destroy is a STOP).

**BLAST RADIUS.** Pool: the 3 keys' raw and derived prefixes (new stamps; UNSERVED until `rk-31`'s crosswalk lands,
served the moment it does). **Code: the whole served plane** -- one Lambda, 16 routes (13 GET); `read_model` gains
`forecast_figures / forecast_periods / forecast_source_counts / forecast_reason` and `read_thesis_bundle`'s check face
includes forecast figures. Every served name's model payload GAINS KEYS; no existing figure moves (AC5's planted
comparison on BA: `check_face_len` and `fiscal_row_count` EQUAL pre/post).

**WRITER CENSUS of the Lambda's bytes: N = 1 writer** -- `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`
+ the targeted apply (`aws lambda update-function-code` is NEVER used). The ADAPTER SINGLE-WRITER QUEUE (the issuer's
rule in every adapter order) guarantees no other round-14 cell holds adapter bytes in flight; the worker's pre-build
`git log <merge-base>..SITEZ -- lib/research/api ...` MUST print nothing, or it STOPS.

**EXPECTED OUTCOME, both branches (read from `read_model`'s rule as the order inlines it).** A name WITH bestdata:
`forecast_figures` > 0 with periods FY1-FY3 and source counts. A name WITHOUT (BA_US_Equity, pulled 2026-09-16 before
C-MODEL-FORECASTS): `forecast_figures 0`, `forecast_reason` naming the missing bestdata -- the honest served state, NOT
a re-pull. The PLANTED NEGATIVE (a hollow key): `model_status ABSENT`, `has_forecast_keys True`, `forecast_figures 0`.
The 13-route census: 13 of 13 `200` pre AND post, `LOST=[] GAINED=[]`.

**PER-KEY ROLLBACK.** Code: the pre-act `CodeSha256` and the artifact's pre-act `VersionId` (measured by the worker
immediately before the build; `list-object-versions` on the key), rollback = RESTORE THE PRE-ACT BYTES AS THE CURRENT VERSION -- `s3api copy-object` from the pre-act VersionId onto the
same key (bucket versioning MEASURED Enabled 2026-09-18 ~22:4xZ; re-measured by the worker into the entry), then the SAME
targeted `safe-apply`; the module (`yang-lambda/main.tf:17-20`, `:38`) resolves the CURRENT artifact version and is NEVER
edited (CTO msg 23830 -- the earlier "re-point at that VersionId through the resource" named a move the module cannot make). Pool: delete the new stamps (as `rk-35`). Order of
rollback if both moved: code first (the served plane), then pool.

**NOT COVERED:** a pull on any covered name; a fallback call on a name whose Bloomberg forecast is present; an IAM or
Terraform change beyond the one targeted resource; a second redeploy.

## `AMGT-rk-37` -- five sheet-row fields, description line, Base case; adapter serves them (R14-M4; M4, M5, L8, C-DESCRIPTION-LINE)

**THE ACT.** As `rk-36`: the validation-name pull/derive (`bestdata` included; `CIE_DES`/`CIE_DES_BULK` added to the
mnemonic set) and ONE redeploy of `opal-amgt-scoped-api` from THIS worktree's bytes, sequenced after `rk-36` drains.

**BLAST RADIUS.** Pool: the 3 keys' prefixes (new stamps). Code: the whole served plane -- `read_description` gains the
describes-the-business test and probes; `_model_cases` serves `base` from the block and `upside`/`downside` ABSENT by
ruling (card 5: *"methodology to be discussed with Andrew"*), for EVERY served name regardless of block content.

**WRITER CENSUS of the Lambda's bytes: N = 1** (as `rk-36`), single-writer queue enforced.

**EXPECTED OUTCOME, both branches.** The PRD's two measured negatives (BA, HD, drafted 2026-09-16 with no CIE_DES):
description ABSENT, `test passed False`, 3 probes named, NO segment-sales text served; `base` ABSENT with the no-cases
reason (not re-derived); upside/downside ABSENT with the exact card-5 reason. A name whose raw carries CIE_DES and
whose block carries consensus EPS and a trailing-median P/E: description served WITH the test passed and `base` served
as a number. The 13-route census: 13 of 13 `200` pre and post, `LOST=[] GAINED=[]`; each name's `check_face_len` equal
pre/post. The PLANTED NEGATIVE hollow key: description ABSENT and every case ABSENT.

**PER-KEY ROLLBACK.** As `rk-36`: pre-act `CodeSha256` + artifact `VersionId` measured fresh by THIS worker (never
`rk-36`'s values -- a co-sign rollback goes stale the moment a second act hits the same address); pool stamps deleted.

**NOT COVERED:** any Upside/Downside methodology (Andrew's); a pull on a covered name; a second redeploy.

Signed `2.0.0_SA_COO~Z`, 2026-09-18, at the round-14 cut.
