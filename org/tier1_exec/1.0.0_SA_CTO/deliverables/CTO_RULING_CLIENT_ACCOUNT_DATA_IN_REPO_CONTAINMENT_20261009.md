# CTO RULING -- client account data in tracked files on dell2: containment scope

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~16:1xZ | **Sources:**
- CVO msg 3606 (URGENT);
- `~D2` msgs 3634 and 3639 (census);
- `~P2` msg 3636; `~G2` msg 3635.

## What is measured

**Removed so far** (bytes kept outside the repo; history still holds them):
- @20e0b6408b: W73_S1, W73_S2 (IRPT_DASHBD);
- @cb16f8b2f9: the ADVI_COTBKF ARD manifest (1,533 account ids);
- @d2eb7316f2: 15 IRPT_DASHBD tie-out files (up to 5,252 accounts each).

**Census of every file under `org/missions/D9/IRPT/` at HEAD:** 3,776 files, **130 hits**.
- IRPT_DASHBD: 59 evidence JSONs, 27 docs, 14 code files.
- IRPT_BCKEND: 10 evidence, 8 docs, 12 code.
- Some filenames are themselves account numbers.
- The path list is OUTSIDE the repo: `C:/dev/_irpt_private_evidence_20261009/IRPT_WIDE_CENSUS_20261009.json`, sha256 `168225f140882ea2...`.

**Today-only censuses:** `~G2` (YCDGEN/ANLREQ) 0 of 108; `~P2` (BCKEND) 0 of 414. That denominator was too narrow, since BCKEND has 30 hits at HEAD.

## Ruling

1. **Evidence files (DASHBD 59, BCKEND 10): MOVE NOW** under the audited `TREE_DELIVERABLES` override, byte-copied outside the repo first, by `~D2` and `~P2` this hour.
2. **Docs (DASHBD 27, BCKEND 8): REDACT in place.** Each account number becomes a stable token, `acct#<first 8 hex of sha256(firm:account)>`, so cross-references survive.
   - Task orders, PRD and decompositions are redacted by their lane owners.
   - Channel and adjudication rows are the CVO's (append-only), so the CVO redacts them, by relay.
   - The token key never enters the repo.
3. **Code (DASHBD 14, BCKEND 12):**
   - a real account number in a TEST becomes a synthetic fixture;
   - in a RUNTIME literal, it moves to a config read from outside the repo, or from the firm's served data.
   - ONE cell per project in the next issuance, under its own pair where the code is deployed.
4. **Filenames that are account numbers:** renamed to their token, in the same commits.
5. **A census over EVERY `org/missions/` tree at HEAD, not only IRPT:**
   - every dell2 COO, for its own projects, with the denominator printed, this tick;
   - a hit follows items 1 to 4.
6. **Rule from now on (msgs 3628-3632):** no account id, balance, fee or flow in any tracked file. The repo carries counts, sha256 and reason codes only. Every
   worker prompt states it.
7. **History:** every path above remains in git history on origin box/dell2 and CLOUD (GitHub Opal-Capital/ajb_workspace). **Purging it is destructive git and
   Andrew's act.** MSTR~DELL2 holds the full path list (outside the repo) for him.
8. **Proposal only, to the laptop commit-gate owner:** a `ds-precommit` limb that refuses tracked files carrying tokens equal to served account ids. It is a gate
   edit, not an approval gate, and it waits on its owner.

-- 1.0.0_SA_CTO~DELL2

## AMENDMENT 1 (~16:1xZ, dell1 `1.0.0_SA_CTO~DELL1` msg 2785, via MSTR~DELL2 msg 3662): one test across both boxes

dell1's scope ruling is `CTO_RULING_CLIENT_DATA_SCOPE_RELATIONSHIP_ID_KEY_PATHS_20261009.md` @dc2b1d9ee0. Dell2 ADOPTS its two carve-outs, so the two boxes apply one
test.
- **OUT of the sweep:**
  - relationship-id KEY PATHS (an S3 key or address that embeds a relationship id);
  - object metadata (VersionId, ETag, size).
- **IN:** any file that pairs an id with a name, account number, balance or holding, as dell1 states.

**One point where dell2 stays stricter, recorded so the boxes do not diverge silently:** a client ACCOUNT NUMBER is client data on its own, paired or not. A file
that only lists account numbers, or keys a map by them (the ARD `first_data_date` map), is IN.
- This seat asks dell1 to adopt that point, so the test becomes identical.
- Until dell1 answers, dell2 applies it on dell2 and does not apply it to dell1's tree.

-- 1.0.0_SA_CTO~DELL2

## AMENDMENT 2 (~16:3xZ, CVO msg 3690): ONE token form across every seat

The CVO's channel redactions are done:
- ADVI_COTBKF: 11 files, 101 ids, @22a636941b;
- IRPT_DASHBD: 6 files, 6 ids, @e0023e4cc9;
- IRPT_BCKEND: INVESTIGATION_v1, 10 ids plus per-account figures, @ae1c3f61dc.

The split it reports:
- `~D2` @eee372447f tokens with sha256(account);
- this ruling (and this seat's PRD redaction @6d0b2b1103) uses sha256(firm:account).

**RULING: ONE form, the ruling's: `acct#<first 8 hex of sha256("<firm>:<account>")>`, with the firm lowercase as it appears in the canon** (`49financial`, `cottonwood`,
`inflection`).
- The firm prefix keeps two firms' identical account strings from colliding into one token. A schema with two token forms fails rule 24 (ii), same grain.
- **The bare-form tokens are re-tokenized by their owners**, a mechanical pass from the private id list:
  - `~D2` re-tokenizes its 13 IRPT_DASHBD docs;
  - the CVO re-tokenizes its 6 IRPT_DASHBD channel ids.
- The re-scan after each pass reads 0 bare-form tokens. Cross-references survive because both sides are re-tokenized from the same list.

**The census pattern grows (CVO finding):** the cot id shapes `z0` + 9 digits, `cv` + 8 digits, and 11-digit zero-led ids are IN.
- `~C2` re-runs its census with them before its doc redaction.
- Every seat's census adds them.

-- 1.0.0_SA_CTO~DELL2

## AMENDMENT 3 (~17:1xZ, `~CB2` msg 3761, row ADVI_COTBKF-D2-S75 ARMED): a shape detector is blind -- detect by the SERVED id set

**Measured:**
- `test_cotbkf_no_account_ids.py`:20-23 is three regexes, each needing a letter at a fixed offset.
- `acct#df101fce` (letter + 8 digits) and `acct#21a12aa6` (11 digits) match none of them, and both are client accounts.
- Cleartext survived inside a file the sweep rewrote, so "442 files, 0 hits" was clean against three regexes, not against client accounts. This seat's own COTBKF
  analysis carried one such id and was redacted @c68f765ef8.

**RULING:**
1. **The detector of record is the SERVED account-id set, not a list of shapes.** Every census and every test asserts against `sha256(UPPER(id))` membership in the
   hash list (`~/.opal/account_id_hashes.txt`, outside the repo; `client-data-check.py` @8c1d8a1966).
   - **`~P2`'s builder (msg 3726) now covers EVERY firm's served account column** for 49financial, cottonwood and inflection, not only 49F. That is the one
     instrument for all seats.
   - Every id-shaped token in a file is hashed and looked up. A hit is client data whatever its shape.
2. **Until the list exists, the shape list widens** to `[A-Z]\d{8}`, zero-led `\d{11}`, `z0\d{9}`, `cv\d{8}` and the 10-digit 49F form. It is a stopgap, and a
   0 from it is not called "clean".
3. **Re-sweep, then re-assert:** `~C2` re-sweeps COTBKF with the widened shapes now, and with the hash list once built.
   - `~CB2`'s 4 files are taken by the re-sweep, not by hand, because a hand token while the detector is blind hides the class.
   - Every seat's "0 hits" is re-stated against the hash list once it exists.

-- 1.0.0_SA_CTO~DELL2
