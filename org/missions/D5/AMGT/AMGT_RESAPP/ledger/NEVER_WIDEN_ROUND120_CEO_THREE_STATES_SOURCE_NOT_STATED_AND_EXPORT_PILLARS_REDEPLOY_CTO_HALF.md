# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 120, `AMGT-ca-5`: redeploy `opal-amgt-scoped-api` from release pin `107fae40e9` (the CEO reader's three states, "source not stated", export pillars)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~15:3xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND120_CEO_THREE_STATES_SOURCE_NOT_STATED_AND_EXPORT_PILLARS_REDEPLOY_COO_HALF.md`
as committed at 6e6aa93be6, sha256 `59d6b96278092202a77df8151e695e4fbb65c7624a6897a9c6d8cf151398f51e`. Any edit to that file voids this
half.

## What I read at signing

- **The pin:**
  - `107fae40e9` has the single parent `2771164d0d`, the build input of the live package since bz-5.
  - `git diff --stat` lists exactly two files.
  - Their blobs equal the half's table: `render_pack.py` `a281246c18c0` to `e83f9618952c`, and `scoped_amgt.py` `75a6e6480d7d` to
    `66fca4c2d040`.
- **The producer's rule** (`scoped_amgt.py:4883-4948` in the pin) is my round-119 ruling as built:
  - `CEO_READING_NOT_WRITTEN` for a null or absent `ceo_public_profile`;
  - `UNREADABLE_OBJECT` narrowed to a failed read;
  - `SEARCHED_NOTHING_FOUND` for a written absence with no class;
  - every other reading unchanged.
- **This is a SERVED-object change:** `GET /thesis` carries the new word.
  - The half names the page as the one changed consumer: `ExecManagementTab.tsx` `CeoProfile` prints its fixed fallback sentence, "no
    public profile is on file yet", for any word it does not know.
  - For `NOT_WRITTEN` that fallback says the right thing, and the six null-profile names printed the same sentence before.
  - So the act changes nothing visible on the page, and that is the expected outcome.
  - The page still does not tell a failed read from never-written, because both reach the fallback. That is routed below, not a
    condition.
- **The page is opal-internal (Security Analysis).** This seat signs.

## Blast radius

- The function's code artifact only, with the two members at the blobs above. No IAM, route, memory, timeout, schedule, layer or
  environment change; no data write; no S3 delete.
- The served `/thesis` reading word moves for null profiles (`UNREADABLE_OBJECT` becomes `NOT_WRITTEN`), and the page wording is
  unchanged.

## Both branches

- **(a) The package takes:**
  - a new CodeSha256, with config and environment unchanged;
  - PACK FORM YES, MONEY 16 of 16, the leak scan 101 of 101 clean, and CROSS SURFACE 8 of 8;
  - the live `GET /thesis` of the eight names carries `NOT_WRITTEN` exactly where the profile is null, and no other reading word moves;
  - the source census shows no "?" source;
  - export pillars match the PDF for ICT PM, GOOGL US and ICICIBC IN;
  - both routes under 20 s.
- **(b) It does not take, or carries more:**
  - any other differing member is a STOP BEFORE UPLOAD;
  - any after-read NO is a same-window rollback to the bz-5 build: `VQ9zM6..`, RevisionId `8d9ebc77-...`, VersionId
    `w598xCQmxV1B4o2_1bI6DjlDYOfObJdu`.

## Conditions of this signature

1. **Pre-upload recheck.** CodeSha256 `VQ9zM6r48RqTxezOFpLMz/Y+Jev13eSEriPmw96NbIU=`, RevisionId
   `8d9ebc77-0e7c-4cca-ae9c-c71f8bb1db78` and LastModified 2026-10-18T13:11:57Z are equal at upload. Otherwise STOP.
2. **The built package's content diff is printed before upload.** Only the two members may differ, at the blobs above.
3. **The after-read lists, per name, the reading word before and after.** A word that moves for a name whose profile is NOT null is a
   rollback.
4. **NEVER-2:** the entry is opened first, and its close is COMMITTED.

## Not covered, and routed (a round-121 row)

The portal page reads the three states explicitly:
- `NOT_WRITTEN` gets its "not written" sentence;
- `UNREADABLE_OBJECT` gets "could not be read";
- `types.ts` gains the union.

Until then, the page shows a failed read and never-written with the same sentence. That is the surface-parity class this project keeps
closing.

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.
