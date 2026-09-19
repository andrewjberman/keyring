# NEVER-WIDEN CO-SIGN -- COO HALVES. Round 14, chain E (executive management). One section per co-signed cell.

**Signer:** `2.0.0_SA_COO~Z`, at the L6 cut, BEFORE any spawn. **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO halves at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_CTO_HALVES.md` (DESIRED plane). **This plane:**
APPLIED and EXERCISED. Neither half stands alone; each worker reads BOTH before its first live act and STOPS with a
BLOCKING row if either is absent or lacks its cell's section. Sequencing the issuer imposes (s.22d): `rk-43` ->
`rk-45` (adapter single-writer queue, and `rk-45`'s one adapter line is sequenced behind `rk-43`) -> `rk-47` -> `rk-48`
(both on slot ~49; `enrich.py`'s pool-write region is shared by `rk-45` and `rk-47`, so `rk-47` is cut only after
`rk-45` drains) -> `rk-49` (not co-signed; gated on `rk-38`, `rk-47`, `rk-48`). `rk-44` and `rk-46` write nothing live.

**The shared rule, read once:** `management/v1/<key>/<as_of>.json` is written by `crosswalk.write_pool` (put +
head read-back) -- a dated key per name; `management/v1/_pool/<as_of>.json` is the pool object, ONE per date,
OVERWRITTEN in place by `enrich.main --write-pool` (`enrich.py:689-699`) unless `--skip-pool` (added by `rk-47`) is
passed. So the per-name keys roll back by DELETE (new dated key) and the pool object rolls back by RE-PUT (snapshot).

## `AMGT-rk-43` -- honest management states in the adapter; redeploy (R14-E1; FWD-17, E1, E4, E11, W32-S2)

**THE ACT.** ONE redeploy of `opal-amgt-scoped-api` from THIS worktree's bytes (`build-and-upload-scoped-amgt.sh` ->
artifact `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, new VersionId; ONE targeted
`safe-apply -target=module.scoped_amgt_api.aws_lambda_function.this`, 0 destroy). Portal edits (`ExecManagementTab.tsx`,
`types.ts`) are committed on the worker's portal branch and are NOT promoted by this cell (LD-0367/0368: the integrator
pushes; PROD promote HELD).

**BLAST RADIUS.** The whole served plane: `read_management` (`scoped_amgt.py:2305-2371`) gains `absent_because` and
the zero-officer ABSENT arm; `ceo_profile_reading` (`:2275-2302`) reads fields. Every served name's management payload
changes SHAPE; the 12 names with rosters keep their figures. NO pool write. NO IAM.

**WRITER CENSUS of the Lambda's bytes: N = 1** (`build-and-upload-scoped-amgt.sh` + the targeted apply); the ADAPTER
SINGLE-WRITER QUEUE holds `rk-45`, `rk-53`, `rk-61`, `rk-36`, `rk-37` until this cell drains; the worker's pre-build
`git log <merge-base>..SITEZ -- lib/research/api ...` MUST print nothing.

**EXPECTED OUTCOME, both branches (read from the new `read_management` rule as the order inlines it).** A name with a
roster (SAP_GY_Equity, the positive control): `management_status SERVED`, `ceo CONFIRMED`, unchanged figures. A name
whose Item-6 cut is EMPTY (ASML_NA_Equity, reads SERVED today -- the round-13 defect): `management_status ABSENT`,
`absent_because ZERO_OFFICERS`, `officer_count 0`, a reason naming the empty section. A name with no declared IR domain
(NU_US_Equity): `SERVED`, `ceo NOT_SEARCHED` with the reason. The 13-route census 13 of 13 `200` pre/post, `LOST=[]
GAINED=[]`. AC4 reads only already-served names; no producer runs.

**PER-KEY ROLLBACK.** Pre-act `CodeSha256` + artifact `VersionId` measured fresh by this worker immediately before the
build; rollback = restore the pre-act bytes as the current artifact version (`s3api copy-object` from the pre-act VersionId onto
the same key; versioning MEASURED Enabled, re-measured into the entry) then the same targeted `safe-apply` -- the module
resolves the CURRENT version and is never edited (CTO msg 23830). No pool key to restore.

**NOT COVERED:** any producer run; any pool write; a portal push or promote; a second redeploy.

## `AMGT-rk-45` -- one pool: the newest pool object for every reader (R14-E3; FWD-17, E5')

**THE ACT.** (i) ONE `put_object` of `management/v1/_pool/<today>.json` through `crosswalk.write_pool` (put + head
read-back) -- OVERWRITING today's null-value pool object (the state at the cut: `_pool/2026-09-18.json` carries
`pool_avg null`); (ii) the ONE-LINE adapter change (`scoped_amgt.py:2343`, the pool read without `as_of`) and its
redeploy -- sequenced after `rk-43` drains, from THIS worktree's bytes, or FOLDED into no one else's: the issuer's queue
rule makes this cell its own redeploy.

**BLAST RADIUS.** Pool: ONE object, `_pool/<today>.json`, rewritten in place (the ONE in-place overwrite in this chain).
Code: the served plane -- every name's `pool_object_key`, `pool_avg`, `pool_denominator` now come from the NEWEST pool
object (today BA serves the 2026-09-15 pool and NU serves pool ABSENT). Served: yes, every management payload.

**WRITER CENSUS of `_pool/<date>`: N = 2 writers** -- `enrich.main --write-pool` (`enrich.py:689-699`, rewrites the
date's object on every run; `rk-47` adds `--skip-pool` so chain E's later cells do NOT move it) and, for this act,
`crosswalk.write_pool` called directly. Rule read for both: same key, whole object replaced. The scheduled task
`OpalResearch-ExecManagement` has the identical split-path defect as `OpalResearch-FilingsAnalyzer` and is DISABLED
(chain F's census, measured 2026-09-18), so no schedule rewrites the pool during the round -- re-measured by the worker
at spawn (`schtasks /Query /TN OpalResearch-ExecManagement /XML`, `Enabled false` printed into the entry).

**EXPECTED OUTCOME, both branches, stated against the CHANGED producer (CTO msg 23833): the cell's step 1 makes
`compute_pool` read the NEWEST object per name ACROSS dates (PRD :752-755; today `enrich.py:594` filters to ONE date,
which is why the 2026-09-18 pool object is null), so the non-null pool below is reachable only through that change --
no live act runs before it is built and its test passes.** BA (a 2026-09-15 object) and NU (a 2026-09-18 object) BOTH serve
`pool_object_key management/v1/_pool/<today>.json` with the SAME non-null `pool_avg` and the SAME `pool_denominator`
(`names_with_roster` 7 at the cut; re-measured). The PLANTED nonexistent key: `management_status ABSENT`, `pool_avg
null` -- the newest-pool read never invents a pool for a name with no roster. If the pool object's rebuild yields
`pool_avg null` again (0 names with a roster on the read -- a branch the rule admits): the object is still written,
BA and NU both serve null CONSISTENTLY, and the criterion is recorded as such; the rollback below applies unchanged.

**PER-KEY ROLLBACK.** Pool: pre-act `get_object` bytes of `_pool/<today>.json` saved to `.scratch/` with sha256 in the
entry BEFORE the put; rollback = re-put + read-back. Code: pre-act `CodeSha256` + `VersionId` measured fresh by THIS
worker (never `rk-43`'s); rollback = the same copy-object restore + targeted apply as `rk-43`. Order if both moved: code first, then pool.

**NOT COVERED:** a producer run over the 33 (`enrich.main --write-pool` on the population); any per-name key; a
second redeploy; the E5/E6/E7 pool writes (their own sections / their own entries).

## `AMGT-rk-47` -- Bloomberg officer fallback on the three validation names (R14-E5; FWD-17, card 1)

**THE ACT.** ONE Bloomberg `ReferenceDataRequest` (`NAME`, `COMPANY_EXEC_OFFICERS`) on CAT/CSL/6861 (within the
validation bar), landing `raw/bloomberg/<key>/<stamp>/exec_officers.json` (3 fresh stamps, put-if-absent), then
`enrich` on the three with `--skip-pool`, writing `management/v1/<key>/<as_of>.json` (3 keys, expected ABSENT pre-act).

**BLAST RADIUS.** 3 raw stamps + 3 NEW dated management keys. Served: NO until `rk-31`'s crosswalk lands the three
identities, then served through the newest-key read. `_pool/` is NOT touched (AC3 prints the pool object's ETag before
and after -- EQUAL, or the criterion fails). NO Lambda, NO Terraform.

**WRITER CENSUS:** `management/v1/<key>/<as_of>` -- N = 1 (`crosswalk.write_pool`, dated key); `raw/bloomberg/<key>/
<stamp>/exec_officers.json` -- N = 1 (the fallback module, put-if-absent). No schedule (DISABLED, above).

**EXPECTED OUTCOME, both branches -- and the REFUSAL branch explicitly (CTO msg 23833):** at HEAD `management.schema.json`
has no `roster_source` and sets `additionalProperties: false`, so a write carrying it lands ZERO keys with a non-zero rc;
the cell's step 3 adds `roster_source` and its enum in the SAME act, and AC3 runs only after that schema lands. If the
schema still refuses, the branch is: nothing written, rc non-zero, the criterion FAILS naming the schema -- covered, and
the rollback below is a no-op. A name whose filing roster is empty or absent and whose Bloomberg officer list
resolves: `roster_source bloomberg`, officers > 0, the fallback label carried ON THE OBJECT (the adapter whitelist means
it reaches the page only through `rk-43`'s reading). A name whose Bloomberg field refuses or the terminal is signed out:
the object is written with `roster_source ABSENT` and the reason, and the criterion is recorded REFUSED with the surface
named -- never retried. Either branch: 3 dated keys, ETag of `_pool/` unchanged.

**PER-KEY ROLLBACK.** Pre-act `head_object` on the 3 management keys (expected 404) and `list_objects_v2` on the 3 raw
prefixes, recorded in the entry. Rollback = delete the new dated keys and the new raw stamps. Nothing is restored.

**NOT COVERED:** a fourth name; any write to `_pool/`; any write on a covered name; the CEO search (`rk-48`'s).

## `AMGT-rk-48` -- the CEO search: organizing agent over SERP records, validation names (R14-E6; FWD-17)

**THE ACT.** AC1-AC3 OFFLINE (the primitive fix in `serp.py`, the mutant pair, the namesake anchor, the verbatim
control) -- no live act, no pair needed. AC4-AC6 LIVE, ONLY IF the spawn prompt states the Bright Data per-use word is
on file (PRD v0.13 :751 -- Bright Data runs *"only under Andrew's per-use word"*; the ~17:2xZ record :44-45 does not
answer it for the running validation; the issuer will name the record in the spawn prompt or the worker refuses with a
row): at most 9 SERP requests (`serp_opal`) and an Anthropic call capped at US$2.00 on the 3 validation CEOs, then a
REWRITE of the 3 dated management keys `rk-47` wrote (`ceo_profile` block added; `ceo_public_profile` kept as its
projection so `read_management` and E1's reading do not break mid-round).

**BLAST RADIUS.** The 3 management keys `rk-47` wrote -- the ONE in-place rewrite of a dated key in this chain (the
worker prints pre-act sha and VersionId per key). Served: NO until `rk-31` lands; then yes. `_pool/` untouched
(`--skip-pool`). NO Lambda.

**WRITER CENSUS of those 3 keys: N = 1 active writer this round** (`crosswalk.write_pool` via `enrich`), two cells in
sequence (`rk-47` then `rk-48`, same slot, `rk-48` reading `rk-47`'s object as its pre-act state). No schedule.

**EXPECTED OUTCOME, both branches (CTO msg 23833: the domain comes from `rk-38`'s `verified_site`, never a hand list;
`domains.json` is not a source for a validation name).** A name with no `verified_site`: `NOT_ATTEMPTED` /
`NO_VERIFIED_SITE`, nothing searched, nothing rewritten for it. A CEO whose SERP records anchor to the namesake control: `ceo_profile` with the
anchored fields and the record ids. A CEO with no anchoring record, or the vendor word ABSENT from the spawn prompt:
`ceo_profile` ABSENT with the reason (offline branch -- AC4-AC6 REFUSED with the reason, nothing rewritten), and
`ceo_public_profile` unchanged. The `_pool/` ETag EQUAL before and after in every branch.

**PER-KEY ROLLBACK.** Pre-act: `get_object` bytes of each of the 3 keys saved to `.scratch/` with sha256 + VersionId
in the entry (the bucket is versioned -- `list-object-versions` confirms the pre-act VersionId). Rollback = re-put the
saved bytes (or `copy_object` from the pre-act VersionId), read back sha256.

**NOT COVERED:** any SERP request beyond the cap; any spend beyond US$2.00; any name outside the three; a `_pool/`
write; a run without the per-use word on file.

Signed `2.0.0_SA_COO~Z`, 2026-09-18, at the round-14 cut.

## `AMGT-rk-49` -- Lusha enrichment keyed off `rk-38`'s verified site, validation names (R14-F1 gate; FWD-17)

**ADDED MID-ROUND, 2026-09-19 ~13:5xZ, by the issuer, BEFORE the cell's first live act.** The cut read this cell as
*gated on R14-F1, not co-signed* and told the worker to make no live write until the spawn prompt said whether the chain E
pair already names these keys' rewrite. It does NOT: `rk-48`'s section names *"the ONE in-place rewrite of a dated key in
this chain"* and lists any second rewrite under NOT COVERED. So a section is owed here and the worker's refusal
(row `AMGT_RESAPP-Z-W50-S1`, AC3/AC4 REFUSED, nothing written) was correct. Measured at spawn by the worker: CAT and CSL
carry NO `verified_site`; Keyence carries `www.keyence.co.jp` (step 4). Sequencing: after `rk-38`, `rk-47`, `rk-48` (all
drained; `rk-48` drained @1f70d87d8d).

**THE ACT.** AC1-AC2 OFFLINE (the domain rule `domain_for` from the filings object's `verified_site` only, the unit arm,
the three-name dry run: `lusha client constructed 0 time(s); nothing written`) -- no pair needed. AC3 LIVE, under Andrew's
word quoted in the order (*"2.) Yes full egress."*, ruled *"Lusha calls are authorized inside the instantiation validation
(Caterpillar, CSL, Keyence) with NO credit ceiling"*, record @4de34f0d95): `enrich.main --enrich-only --skip-pool` on the
three validation names; the ONE billable call is `prospecting_page` on the verified domain, so today ONE Lusha call
(Keyence) and ZERO for CAT and CSL, which are written `lusha_enrichment.status SKIPPED` with reason `NO_VERIFIED_SITE`
(`domains.json` is never a source for a validation name). Then a REWRITE of the three dated management keys
`management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json` (the objects `rk-47`/`rk-48` wrote): the
`lusha_enrichment` block and, on the CALLED name, `officers[].profile_url / lusha_title / enrichment`. AC4 reads back.

**BLAST RADIUS.** Exactly those three dated keys, in place -- the SECOND in-place rewrite of a dated key in this chain
(`rk-48`'s was the first). Served: YES (`rk-31` landed; `read_management` reads the newest dated key). `_pool/`
untouched (`--skip-pool`; ETag EQUAL before and after). NO Lambda. NO covered name.

**WRITER CENSUS of those 3 keys: N = 1 active writer this round** (`crosswalk.write_pool` via `enrich`), three cells in
sequence on the same keys (`rk-47`, `rk-48`, then `rk-49` reading `rk-48`'s object as its pre-act state). No schedule.

**EXPECTED OUTCOME, both branches, read from `apply_lusha_enrichment`'s own rule.** A name with a `verified_site`:
`status CALLED`, `credits_used` printed, officers enriched where Lusha matches, unmatched officers `pull-missed`. A name
without one: `status SKIPPED`, `reason NO_VERIFIED_SITE`, `credits_used 0`, officers unchanged. A Lusha error: `status`
FAILED with the error text, officers unchanged, the key still rewritten (the block records the attempt). In every branch
the pre-existing `ceo_profile` / `ceo_public_profile` / `officers` content is preserved except the three enrichment fields.

**PER-KEY ROLLBACK.** Pre-act: `get_object` bytes of each of the 3 keys saved to `.scratch/` with sha256 + VersionId
printed into the entry (bucket versioned). Rollback = `copy_object` from the pre-act VersionId (or re-put the saved
bytes), read back sha256. `_pool/`: ETag compared, no write to roll back.

**NOT COVERED:** any Lusha call on a name outside the three; any call on a name without a `verified_site`; a `_pool/`
write; a Lambda; any run without the order's quoted word.

Signed `2.0.0_SA_COO~Z`, 2026-09-19 ~13:5xZ, mid-round, before the cell's first live act; counterpart half owed by
`1.0.0_SA_CTO~Z` (asked the same tick). The worker acts only when BOTH halves carry this section.
