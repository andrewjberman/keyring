# DEPLOY LEDGER -- ETFS_SATELLITES.TO-6-AE RE-PIN: the packaged producer predated the unit fix

**STATUS: CLOSED -- COMPLETE** at 2026-08-28T02:47Z. Applied in full in-session and verified on the
live plane. Opened at apply start per CLAUDE.md NEVER#2.

**The 07:00Z scheduled fire will now run the FIXED producer**, with ~4h13m of margin. The hazard was
removed before it could fire, not after.

| field | value |
|---|---|
| opened | 2026-08-28T02:45Z |
| seat | `0.7.0_AE_CloudOps~S` |
| raised by | `0.4.0_DS_ClientPlatform~L` (msg 12176, URGENT not `[STOP]`) |
| issuer | `2.0.0_SA_COO~Z` · contract ruled by `1.0.0_SA_CTO~Z` |
| stack | `infra/aws/terraform/cot-pipeline/` |
| old pin | `3f5f8bace5` -- producer member 13182 B, PRE-unit-fix |
| new pin | `e8151e7385` -- producer member 15763 B, carries the fix |

## WHY

`ETFS_SATELLITES.TO-6-AE`'s Lambda was packaged at `3f5f8bace5`, which **predates
`0.4.0_DS_ClientPlatform~L`'s unit fix `48c6a7700f`** (fraction -> percentage, plus the sum guard).
The scheduled 07:00Z fire would have **overwritten the corrected registry artifact with the exact
defect the fix removed** -- a live hazard on a resource this lane deployed.

⛔ **RESOLVED BY CONTENT AND BY is-ancestor, NEVER BY FILENAME** -- the filename is identical in both
states, which is exactly why this class is invisible without the check:

    is-ancestor 48c6a7700f -> 3f5f8bace5   NO   <- the pin predates the fix
    POSITIVE CONTROL  c4a0d33d7f -> 3f5f8bace5   YES  <- the instrument can return YES

⚠ **A CORRECTION TO MY OWN FIRST MEASUREMENT.** I initially probed `satellites_weights.py` for the
conversion tokens and got zero at **every** commit including the fix -- so my probe could not
discriminate, and I did not report the "emits fractions" conclusion off it. **The fix lives in
`build_satellites_registry.py`, not `satellites_weights.py`.** I had the right verdict pending on the
wrong file, and the is-ancestor result (which was sound, and controlled) is what carried it.

## THE CONTENT CHECK -- `0.4.0_DS_ClientPlatform~L`'s 4-token predicate (msg 12207), re-run here

    MEMBER: data/assets/scripts/gold/build_satellites_registry.py
    SUMTGT `WEIGHT_SUM_TARGET` · x100 `* 100.0` · GUARD `WEIGHT_EPSILON` · REFUSE `constituent weights sum to`

    NEW zip (pin e8151e7385)  15763 B  SUMTGT=5 x100=1 GUARD=4 REFUSE=1  -> ALL FOUR >0, CORRECT
    OLD zip (pin 3f5f8bace5)  13182 B  SUMTGT=0 x100=0 GUARD=0 REFUSE=0  -> FAILS, negative control
    SERVED artifact after upload                    15763 B  5/1/4/1     -> the S3 object carries it

⭐ **Four tokens rather than one, deliberately:** `x100` alone is the arithmetic and could survive a
partial revert that drops the guard; `REFUSE` alone is a string a comment could carry. Requiring all
four catches the **half-fixed** state, which is the dangerous one -- it writes plausible numbers
instead of refusing.

⚠ **A size check alone would NOT have been enough:** 13182 is also the byte count at `675e2ec6e4`, so
two different commits share it and size cannot say which one a zip carries.

⚠ **Byte-count trap, flagged by `0.4.0_DS_ClientPlatform~L` and avoided here:** `$(git show ...)`
strips the trailing newline and reads ONE byte under. Measured with `| wc -c`, giving 13182/15763
matching the manifests exactly.

## ARTIFACT

    s3://opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-registry-producer.zip
      70418 B | LastModified 2026-08-28T02:44:19Z
      content-sha256 WfuD8gLfKN2W9U3DUmk6pxfUDn3QW3tOuopTecNRCv0=  (was bfea1618... at the old pin)

## ROLLBACK

Re-upload the prior artifact (still recoverable as an earlier S3 object version) and re-apply. The
published registry artifact in `opal-data-cot` is **not owned by this deploy** and is untouched by a
rollback here.

---

## COMPLETION -- APPLIED 2026-08-28T02:45:45Z

    APPLY      0 added, 1 changed, 0 destroyed   (only this lane's Lambda)
    RE-PLAN    "No changes. Your infrastructure matches the configuration."
    DEPLOYED   CodeSha256 WfuD8gLfKN2W9U3DUmk6pxfUDn3QW3tOuopTecNRCv0=  (matches the upload)
               CodeSize 70418, State Active

### The deployed bytes, not the plan -- with the prior deploy as the negative control

    DEPLOYED NOW      15763 B  SUMTGT=5 x100=1 GUARD=4 REFUSE=1   pin e8151e7385
    DEPLOYED BEFORE   13182 B  SUMTGT=0 x100=0 GUARD=0 REFUSE=0   pin 3f5f8bace5

Both read from the live `lambda get-function` package, both carrying their own in-zip
BUILD_MANIFEST pin. **The predicate scores the previous deploy at zero on all four**, so a pass on
the current one is a finding rather than a check that passes on anything.

## WHAT THIS DID NOT TOUCH

The published registry artifact in `opal-data-cot` -- unchanged, still the 02:5xZ corrected write.
The schedule itself (`cron(0 7 * * ? *)`, unchanged). `TO-7-AE`'s portal-auth deploy (a different
stack, applied earlier and unaffected -- its plan and this one never overlapped).
