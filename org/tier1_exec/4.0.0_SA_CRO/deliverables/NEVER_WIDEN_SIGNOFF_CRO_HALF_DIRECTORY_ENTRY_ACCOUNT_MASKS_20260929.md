# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- DirectoryEntry `account_masks` (AD-10 step 1) in irpt-directory-search and irpt-ycharts-generate (IB-pr-231)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_DIRECTORY_ENTRY_ACCOUNT_MASKS_20260929.md`
blob `74d19716ff` (at `46ca5fc444`; read 2026-09-29 13:2x-13:4xZ).
- **Word diff:** a new packet for a new act; its shape is the HoldingsSnapshot CATEGORY packet's (this seat's half
  `NEVER_WIDEN_SIGNOFF_CRO_HALF_HOLDINGS_CONTRACT_CATEGORY_20260929.md`, SIGNED, closed 12:28Z) with the contract,
  the functions and the ordering changed. The field it admits is AD-10 of this seat's master guidance brief ("each
  account shows its own tail everywhere"), the page half of which this seat routed to ~D at 10:0xZ.
- **Asked by:** 2.0.0_SA_COO~P, msg 102816 (for ~M 102808, release order @1a031f514d step 1). **Other half:**
  1.0.0_SA_CTO. **Ledger:** `irpt-directory-entry-account-masks-20260929` (U1 closed; D1, A1 open). This seat is not
  in the act.

## VERDICT: SIGNED on blob 74d19716ff, with three conditions and two named items

One optional property arrives in the two functions that package the contract. The one served reader of the file
(directory-search's wire field set) carries it only on an entry that holds it, and no served entry holds it; the
other packager never validates a directory document. Ordered after window 22, whose pins both functions are.

## 1. The artifacts, read here by S3 version (the newest version of each key, equal to the packet's)

| function | key / version | sha | census vs live | the one member that moves |
|---|---|---|---|---|
| irpt-directory-search | `investor-reporting/irpt-directory-search.zip` `2RmObc9v` (13:17:11Z, latest) | `s0riHZ9h` | 20 -> 20, nothing added or removed | `contracts/DirectoryEntry.schema.json` 7ed220ff -> **6ad840a5** |
| irpt-ycharts-generate | `investor-reporting/irpt-ycharts-generate.zip` `DWP1wKAI` (13:17:29Z, latest) | `inrij6hL` | 111 -> 111, nothing added or removed | the same member 7ed220ff -> **6ad840a5** |

- Live today: directory-search `o1TXq5PH` (2026-09-26), generate `wnt7hjAB` (12:09Z today); both live copies are the
  same bytes (7ed220ff).
- `6ad840a5` is `git show 4ecbaca410:docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json` (git blob
  `27d9a8f7`), equal to HEAD's committed docs copy and HEAD's committed `_contracts` copy; the source map pins both
  functions' rows to `4ecbaca410` with that sha256 (`lambda-source-map.json:3552-3555`, `:4227-4230`). The generate
  resident-side members are unchanged from `wnt7hjAB` (the census shows one member moving).
- **The worktree is dirty on both copies and the act does not read it:** the docs copy and the `_contracts` copy sit at
  `f24ed783` on disk, uncommitted and ahead of the pin; the artifacts carry `6ad840a5`, so the dirty tree is outside
  this act and belongs to whichever later cell is editing it.

## 2. The contract change, structurally diffed here (7ed220ff -> 6ad840a5)

- Added: `/properties/account_masks` -- an optional array, one item per account, each `{account_id,
  masked_discriminator}` with `additionalProperties: false` and both keys required inside the item. Nothing else
  changes: no enum, no top-level `required`, no `additionalProperties` on an existing object. `masked_discriminator`
  at the top level stays the head account's mask, so an unmigrated reader keeps working.

## 3. The two readers, read in the zips (both branches)

- **irpt-directory-search reads the contract on the served path:** `entry.py:71-90` `_document_fields()` takes the
  search response's field set from the contract's `properties` (checkout path, then `IRPT_CONTRACTS_DIR`), and RAISES
  if no contract is readable rather than sending everything. After the act `account_masks` is admissible on the wire
  and travels only on an entry document that holds it.
- **Every served entry, validated here** (each firm's `investor-reporting/directory/latest.json` -> `directory.json`,
  per-entry Draft 2020-12): 49financial 4,620 (as of 2026-09-24), cottonwood 258 (2026-09-22), inflection 292
  (2026-09-25) = **5,170 entries; 0 carry `account_masks`; 0 invalid under the live copy; 0 invalid under the new
  copy.** So the wire is byte-identical after the act until ~M's directory re-mint (step 3), which the release order
  places after portal PROD reads the field (step 2).
- **irpt-ycharts-generate never validates a directory document:** `DirectoryEntry` appears in its `.py` members only in
  docstrings (`enforce.py:28`, `:229`; `resolve.py:16`; `loaders.py:187`, whose `load_directory` reads the artifact
  and validates nothing); the file feeds the ingestion digest (`schemas-4780eaf8...` -> `schemas-cb6e1c3c...`,
  recorded on new acceptances, never compared on read -- `owned_requests.py:92-93`, read for the CATEGORY act) and
  the admission Registry.

## 4. Blast radius

- **Moves:** directory-search may carry `account_masks` on the wire once an entry holds it; generate's digest string
  for new acceptances. **Unchanged:** every served search answer today (5,170 entries hold no such field), every
  retained request, every other member, IAM, routes, tables, schedules.
- **Rollback per key:** directory-search -> the `o1TXq5PH` version restored as latest and re-applied; generate ->
  `GP__8T1n` (`wnt7hjAB`) restored as latest and re-applied.

## Conditions

1. **After window 22 closes, never inside it:** both functions are W22 pins; the apply waits for that ledger's close,
   and the S3 latest version of each key equals `2RmObc9v` / `DWP1wKAI` at apply, written in the ledger.
2. **BEFORE and AFTER are the per-entry validation of section 3 with the counts printed** (5,170 entries, 0 carrying
   `account_masks`, 0 invalid) under the live and then the deployed copy, plus one signed-in directory search on one
   firm whose response carries the same field set as before and no `account_masks`. That page read is this seat's
   walk once the local dev build is running again (it was stopped by the machine's memory reaper at 12:4xZ and
   restarts only on Andrew's word) or ~D's page read, whichever comes first.
3. **A fresh-container invoke per function** as the packet's step 5 (the refused generate POST that builds the digest;
   the API-shaped refused directory request), with CodeSha256 read-backs and the deployed zips member-equal to the
   artifacts.

## Named items (not refusal grounds)

1. The dirty worktree copies (`f24ed783`, docs and `_contracts`) are ahead of the pin and uncommitted; the source
   map's pin is what keeps them out of these builds, and the U1 census is what would show them.
2. Step 2 (portal PROD reading the field, ~D) and step 3 (the directory re-mint, ~M) are where the page changes; the
   finding this field answers (three `****9079 / IRA` in one picker) is graded there, not here.

## Addendum 1 (2026-09-29 15:1xZ) -- D1 read: applied after window 22 closed; A1 waits on a signed-in search

Ledger `irpt-directory-entry-account-masks-20260929` D1 CLOSED 15:03:16Z: window 22 CLOSED 14:50:29Z before the apply
(condition 1); S3 latest at apply `2RmObc9v` / `DWP1wKAI`; safe-apply 14:55:56Z and 14:58:31Z; read-backs `s0riHZ9h`
(14:58:27Z) and `inrij6hL` (15:00:32Z), deployed zips member-equal; the live handler's own `load_directory` BEFORE
(14:52Z) and the deployed handler AFTER: 4,620 / 258 / 292 entries, 0 invalid under either copy, 0 carrying
`account_masks` (condition 2's validation); fresh-container invokes on both functions clean (condition 3); re-plans No
changes. A1 (one signed-in directory search on one firm, the field set unchanged) is open: this seat's local build is
down pending Andrew's word and the walker refuses a PROD base by his 2026-09-26 guard, so ~D's page read serves,
as condition 2 allows.

## What this half signs against

- Packet blob `74d19716ff`; commit 4ecbaca410 (blob `27d9a8f7`); the source-map rows in section 1.
- Artifacts `s0riHZ9h` (S3 `2RmObc9v`) and `inrij6hL` (S3 `DWP1wKAI`) with their censuses against live `o1TXq5PH` and
  `wnt7hjAB`; the diff in section 2; the 5,170-entry validation and the reader reads in section 3.
- The blast radius in section 4 and the three conditions.
