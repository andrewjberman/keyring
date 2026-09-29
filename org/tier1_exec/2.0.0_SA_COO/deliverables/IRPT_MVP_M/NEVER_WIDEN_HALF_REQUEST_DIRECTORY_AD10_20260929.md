# Never-widen half requested -- every DirectoryEntry gains a per-account `account_masks` field

From `0.9.0_WK_IRPT_BCKEND~75` (worker of `2.0.0_SA_COO~M`), 2026-09-29, task order
IRPT_BCKEND.TO-IB-m22-221 (round 22, workstream ~M, cell `IB-mr-221`, brief item AD-10: "each account shows
its own tail everywhere"). The CRO measured the served picker showing three 49F accounts all as
`****9079 / IRA` and five INF accounts as `****3302 / JOINT` (CRO 102699, CTO 102702).

**This changes a served figure (round-19 analysis section 2), so it is sent as a half rather than merged
straight to a release.** Nothing in this half has been uploaded, deployed or served; the build is LOCAL
only (real reads, no upload -- see AC2 evidence below).

## The act

Land the new `account_masks` field on every entry the directory runner already builds, at the runner's
regular publication step (`directory_runner.py --firms <firm> --upload`), through the existing publish path
(firm bucket, `investor-reporting/directory/{as_of}/directory.json` + `.../latest.json`, prod and QA
prefixes) -- no new bucket, no new key, no new pipeline. The served pointer moves to the new revision only
if the runner's own validation passes, exactly as today.

## What moves: one ADDITIVE array field, nothing else

Before: `DirectoryEntry.masked_discriminator` is minted ONCE per entry from the entry's HEAD account row
(`head = account_rows[0]`), so every account under a multi-account entry (a household, a relationship) reads
the same tail and the same registration type -- the exact defect the CRO measured.

After: `DirectoryEntry.account_masks` is an ADDITIVE array, one item per account in `ids.account_ids` and in
the SAME order, each `{"account_id", "masked_discriminator"}` built from THAT account's own row with the
SAME `masked_discriminator()` function the head field already uses. `masked_discriminator` itself is
UNCHANGED (still the head row) so a reader that has not migrated keeps reading exactly what it reads today.
`account_masks` is OPTIONAL in the schema (not in `required`), so a document built before this change stays
valid.

**Local candidate diff** (`git diff --stat`, this branch, not yet merged):
```
 data/assets/scripts/gold/investor_reporting/directory_runner.py           | 15 +++++++++++++
 docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json           | 23 +++++++++++++++++++
 2 files changed, 38 insertions(+)
```
`_entry()` now builds `account_masks` from EVERY account row (deduped the same way `ids.account_ids` is
deduped -- one item per unique opaque account id, first row wins), and the docs contract at
`docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json` declares the property (additive, optional,
`additionalProperties: false` required it be declared or every document carrying it fails validation).

Measured on REAL local builds, no upload (`R22_AD10_ACCOUNT_MASKS_SUMMARY_20260929.json`, IBM22-221-AC2):

| Firm (as_of) | Entries | Accounts | Own mask | >4-digit masks | Multi-account entries | ...with distinct tails |
|---|---|---|---|---|---|---|
| 49financial (2026-09-28) | 4,642 | 7,598 | 7,598 | 0 | 1,945 | 1,945 |
| inflection (2026-09-29) | 298 | 884 | 884 | 0 | 205 | 205 |
| cottonwood (2026-09-25) | 263 | 953 | 953 | 0 | 180 | 179 |

Every account gets its own mask; no mask carries more than the last 4 digits; every multi-account entry but
one (a Cottonwood entry with two accounts sharing the same number+type -- a real duplicate, not a builder
defect) now shows distinct tails where it used to show one repeated tail. Example (49F sample): an entry that
today reads `****0251 / Joint Tenant` for both its accounts will carry `account_masks` =
`[{****0251 / Joint Tenant}, {****5762 / Rollover IRA}]`.

Does NOT move: `masked_discriminator` (unchanged, still the head row), amounts, ids, `permitted_scope`,
`permitted_capabilities`, `termination`, `access`, `revision`, `cohort` -- nothing else in the contract, and
no other pipeline's output.

## Blast radius -- every reader of the directory entry, censused

| Reader | Kind | Today | After this field lands on a served document, UNRELEASED | Needs a change before serving? |
|---|---|---|---|---|
| `data/assets/scripts/gold/investor_reporting/directory_runner.py` (`validate_entries`/`main`) | producer's own pre-flight validator | validates against `CONTRACT_PATH` = the LAMBDA's packaged copy (`infra/aws/lambda/investor-reporting/_contracts/DirectoryEntry.schema.json`) | REJECTS every entry (`additionalProperties: false`, field undeclared there) -- `main()` returns rc=1 with a schema ERROR line per entry. Measured this session: real local build, 49F/INF/COT all show `valid=0 of <entry_count>`. | YES -- the Lambda contract copy (see release order) |
| `infra/aws/lambda/investor-reporting/directory/entry.py` (`_document_fields`) | Lambda wire-field whitelist | reads the property set from `docs/contracts/.../v1/DirectoryEntry.schema.json` in a checkout, else `IRPT_CONTRACTS_DIR` (the shared layer's mounted copy) in the deployed runtime | a CHECKOUT run now whitelists `account_masks` (the docs copy just gained it); the DEPLOYED Lambda reads the shared layer's copy, which is packaged from the same source as `infra/aws/lambda/investor-reporting/_contracts/` and has NOT changed | YES if/when the layer is repackaged -- named so the repackage step does not silently widen the wire before the directory bundle carries the field |
| `infra/aws/lambda/investor-reporting/directory/handler.py` (`irpt-directory-search`: `search`/`resolve`) | the served picker/identity backend | emits `masked_discriminator` per entry only (lines ~205, ~302) -- the exact defect the CRO measured | unchanged by this field alone; a document carrying `account_masks` passes through untouched until this handler is edited to read it | YES -- this is the edit `2.0.0_SA_COO~D` (or its issuer) points at `account_masks`; NOT done in this order |
| `portal/src/pages/InvestorReporting/contracts/directory-browse.ts` (`object(value, required, optional)`) | portal wire-shape validator | its `object()` helper THROWS on any key not in its `required`/`optional` lists (line 15); `account_masks` is in neither | REJECTS a document carrying it: `Invalid directory page` | YES -- the portal validator's allowed-key list, before a document with the field reaches the portal |
| `portal/src/pages/InvestorReporting/contracts/wire/{DirectoryEntry.ts,consumed.ts}`, `adapt.ts` | portal wire types + adapter | type `DirectoryEntry` and `consumed.ts`'s declared `reads`/`required` do not list `account_masks` | no runtime effect until a consumer reads the field; the account picker (`header/BrowseDrawer.tsx`), `header/ClientSearch.tsx`, `header/IdentityCard.tsx`, `tabs/reporting/AccountsTable.tsx`, `render/performance/AccountDetail.tsx` all read `maskedDiscriminator` today and are unaffected by an UNREAD additive field | YES -- these are the "account picker and identity list" the task names for `2.0.0_SA_COO~D` to point at `account_masks`; NOT done here |
| directory search cache (`handler.py:_CACHE`, per-container, keyed on `firm_bucket+key`) | in-process cache of the fetched directory doc | caches whatever `s3:GetObject` returns, whole document | carries `account_masks` through unread once the field is on a served document; no cache invalidation issue (a new revision is a new S3 key, so `latest.json`'s pointer change is what a container next reads) | NO -- the cache is transparent to an added field |
| exports | none found | `comp-find "DirectoryEntry.schema.json"` and `comp-find "masked_discriminator"` (this session, corpus=all) surface no export/report producer reading `DirectoryEntry` outside the files above | n/a | n/a |

## Release order (named per Build step 5)

1. **The handlers' contract copy first**: `infra/aws/lambda/investor-reporting/_contracts/DirectoryEntry.schema.json`
   (and whatever shared layer packages it for `IRPT_CONTRACTS_DIR`) gains `account_masks`, identically to the
   edit already landed at `docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json` in this cell. This
   is 2.0.0_SA_COO~P's shared packaging (named, not done here -- outside this order's `<paths>` grant).
2. **The directory bundle re-mint**: `directory_runner.py --upload` runs against the updated contract copy so
   `validate_entries`/`main` pass and a served revision carries `account_masks`.
3. **The portal reads the new field**: `directory-browse.ts`'s allowed-key list admits `account_masks`,
   `irpt-directory-search`'s `search`/`resolve` project it, and the account picker / identity list
   (`BrowseDrawer.tsx`, `ClientSearch.tsx`, `IdentityCard.tsx`, `AccountsTable.tsx`, `AccountDetail.tsx`) read
   it per-account instead of the entry-level `masked_discriminator` -- `2.0.0_SA_COO~D`'s cell.

Reversing this order (serving a document with `account_masks` before step 1) is exactly the regression
measured above: `directory_runner.py`'s own pre-flight validation refuses every entry, so in practice step 2
cannot upload successfully until step 1 lands -- the ordering is enforced by the producer's own gate, not
only by convention.

## The half's two branches

- **The publication validates** (after step 1 lands): the new revision serves with `account_masks` on every
  entry, as measured above at the firm's then-current as_of.
- **It refuses** (before step 1 lands, or if the Lambda contract copy is not yet updated): the served
  revision is unchanged; the refusal is the runner's own pre-flight validation, as measured this session.

## Rollback per key

Per firm, repoint `latest.json` to the prior revision (retained, as for every directory publication). No
other object is written; `account_masks` is additive so a rollback to a pre-AD-10 revision is read by every
current consumer exactly as before this change.

## The ask

Sign or refuse. Named per Build step 5 of task order IRPT_BCKEND.TO-IB-m22-221. Nothing publishes before the
Lambda contract copy (release order step 1) and nothing under this half is uploaded, deployed or served --
the local build and its summary (`R22_AD10_ACCOUNT_MASKS_SUMMARY_20260929.json`) are the whole candidate.
