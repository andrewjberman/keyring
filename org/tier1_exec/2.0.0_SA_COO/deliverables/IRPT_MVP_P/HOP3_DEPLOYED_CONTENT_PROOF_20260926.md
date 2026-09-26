# Hop 3 deployed by content -- the six patched files in both served packages

**Author:** `2.0.0_SA_COO~P`, 2026-09-26 ~19:4xZ. **Order:** `1.0.0_SA_CTO` 101441: "prove the deployed zips by
CONTENT: every patched file in the served generate and resident packages must be byte-equal to the patch's tree (a
hash list)". **Ledger:** `irpt-hop3-generate-resident-20260926`.

## The patch's tree

~Y's `P_HOP3_SUBMISSION_FIXES_20260926.patch` (proof @24a87c9d53), committed on the backend branch as 03ea5980cc
and a219094b1a. The reference hashes are `sha256(git show a219094b1a:<path>)`, the committed LF bytes.

The six files were byte-identical at f624e8a72f (the live resident), 19d8f3038c (the live generate row) and
260399e940 (the tip before the patch). So each package is its live bytes plus exactly the patch.

## Hash list (sha256)

| file (ycharts/generate/) | a219094b1a blob | served generate `/iFhTAvT..` | resident host root `fe64236bbb` |
|---|---|---|---|
| custody_submission.py | e347d1d198d0c21a8f99cf60f5b8259bcb7066483ad1cdbbbba61d1b9a30399d | equal | equal |
| prospect_submission.py | 2d9e71eb09c99b0e4b9b1b8d2b9564259bbe387ce47662f160060b9148bb05f4 | equal | equal |
| recipe.py | a724b653b5d7c928853f7f98cb3408da75b6e36c966574d8202e85e023e7403a | equal | equal |
| recipe_snapshot.py | f71c3a31d8eb3130d194fe171e87b22bb41f96eeb76d85de126b79e354fda31d | equal | equal |
| submission.py | 9929a829047fc9673fbeba746df9a3c6b5165442ffa92e6d1294c9d65faac824 | equal | equal |
| templates.json | d10e412f0aef447b76babbc273099fbd15d33528e83605855797b89315163428 | equal | equal |

How each column was read:
- **Served generate:** the zip downloaded from `lambda get-function` Code.Location after the apply. CodeSha256
  `/iFhTAvTZNnhtdhwQPJ+sPPfF67WcMYJY+NE5Fx9XXI=`, S3 version uM1YL.noW5pNrWzZ6osy4mPxss7aPZXC, layers
  [irpt-common:5].
- **Resident:** `sha256sum` on the host, under the unit's running root `/opt/irpt-resident/fe64236bbb`, read in the
  same SSM command (9a5444d6) that confirmed the unit active on that root.

## Everything else unchanged

- **Generate:** the new zip against the live 85TXFzzv zip, member by member: 111 and 111 members, none added or
  removed, and exactly these six differ.
- **Resident:** the package SHA256SUMS against a rebuilt f624e8a72f package: exactly these six plus
  `reports/resident_bindings.json` (its provenance pin and time) differ.

## One trap caught before the apply

The first generate build (`ZxNASliN..`) served `templates.json` with CRLF line endings (sha 08f6ee3d..). The
publish worktree checks out JSON with CRLF, the builder zips the working file, and the live 85TXFzzv carried CRLF
too. That build was never applied.

`recipe_snapshot.capture_configuration` records `sha256(templates.json bytes)` in the frozen composition, while the
resident carries the LF blob. So the working file was rewritten from the blob and rebuilt (`/iFhTAvT..`), making
both packages carry the same bytes.

Parked for the owner of `infra/aws/lambda/ci/build-and-upload.sh`: a source_dir JSON member's bytes depend on the
checkout's EOL setting. This un-parks when a second function packs a hashed JSON from its source_dir.

## Not proved here

- A live composition: no login window for hop 3 until ~Y's offline pre-flights of hops 5-10 land (CTO 101441).
- The vendor session and PDF (hops 6-7).
