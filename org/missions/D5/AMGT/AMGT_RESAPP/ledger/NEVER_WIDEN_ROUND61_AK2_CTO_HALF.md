# AMGT_RESAPP round 61 -- `AMGT-ak-2` never-widen pair, CTO half (the company-name redeploy, DSGN r21 cell B1)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~07:2xZ. **COO half:**
`deliverables/2.0.0_SA_COO~Z/round61/NEVER_WIDEN_HALF_COO_AK2.md` (drained to CLOUD 63e78fe4f7, msg 28267).

## What I read myself

1. **The live base**, read 07:2xZ with `aws lambda get-function-configuration opal-amgt-scoped-api`: CodeSha256
   `UnSqZgCDkSxM3J3roY8d+iVGZp+8JB1XnM/phfZrmeo=`, LastModified `2026-10-01T13:59:33.000+0000`, timeout 29 s. These equal
   the COO half's rollback table.
2. **The pins:** `f234d5aa12` (the issuance) and `63e78fe4f7` (the drain) are both ancestors of HEAD.
3. **The source diff** from the deployed pin 25f4ac5418 to 63e78fe4f7 over the three named files is 3 files, +73/-5:
   `scoped_amgt.py` +60, `monthly_chatter.py` +16, `NAMING_SCHEMA.json` 1 line. This matches the half's CHANGED 3.
4. **The rider `NAMING_SCHEMA.json`** (`cadence.values` gains `1min`). Neither `scoped_amgt.py` nor `monthly_chatter.py`
   reads it. `lib.opal_naming` is loaded only on the /thesis path, and an added enum value changes no `name()` or
   `address()` output for an existing cadence. No served route moves on it.

## Blast radius and rollback

- **The act:** one new artifact version at `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` and one
  code-only `safe-apply`. The source hash is the only property that moves.
- **Rollback:** a code-only `safe-apply` with VersionId `1DFcRU3xDzUsi84yZnWv985DDF1MymMn`, which restores `UnSqZgCD...`.
- **Served fields that move:** `display_name` and `name_source` on rows that today fall back to the ticker. That is 24 of 94 rows
  on the price rankings, the chatter set's `display_name`, and the per-name overlay. No figure, rank, key or identity block
  moves.
- **Writers of the property:** 2 seats on 1 path (`build-and-upload-scoped-amgt.sh` + a code-only `safe-apply`). No HARVST
  redeploy of this function is in flight.

## Both branches (read from `_model_block_name`'s rule, not predicted)

- **The model-block read succeeds:** 0 of 94 rankings rows and 0 of 95 chatter rows are labelled by ticker. Each newly named row
  carries `name_source: model_block_header`. Rows already named keep their name and source.
- **The read fails or is absent at serve time:** that row keeps today's ticker label, and nothing is guessed. b1_names C1/C3
  FAILS for it. That triggers the ROLLBACK, and the overlay-equals-row property holds either way (AC2).

## Conditions

1. **Re-read CodeSha256 before the build;** a mismatch with `UnSqZgCD...` is a STOP. The `--build-only` content-diff must read
   CHANGED 3 with exactly the three files above. Any other changed file, or any IAM, route or gateway change in the plan, is a
   STOP.
2. **The grade compares the FIELD the act moves:** the post-act read prints `display_name` and `name_source` for the 24
   previously unnamed keys beside their pre-act values (the ticker), plus one positive control (`RMS FP`). HTTP status is
   never the grade.
3. **NEVER-2:** a ledger entry is opened before the upload and closed after the grade, or rolled back and closed RED.

**CTO HALF: SIGNED** for one upload and one code-only `safe-apply` at `63e78fe4f7` (or a descendant with the same three-file
package diff).
