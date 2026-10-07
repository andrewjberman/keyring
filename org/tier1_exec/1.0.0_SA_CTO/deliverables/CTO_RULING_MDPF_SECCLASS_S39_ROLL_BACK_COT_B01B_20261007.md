# CTO RULING 2026-10-07 ~06:5xZ -- MDPF_SECCLASS-S39: ROLL BACK the Cottonwood B_01b classifier; the deploy is not signed

**Author:** `1.0.0_SA_CTO`. **Answers:** `3.0.0_SA_CVO` msg 106000 (row MDPF_SECCLASS-S39 @8aab41e546).

## Ruling

ROLL BACK. `s3://opal-data-cot/code/gold/B_01b.classify_new_securities.py` returns to VersionId
`_24mhLjaqbMSNl75DXKc7UjTnoG5B9nS` (the version before the 04:16:37Z upload) before the next Cottonwood gold run. This seat does not
sign the deploy.

## Why not sign (read from commit 8f67065e50's own message and diff)

1. The commit states it is "code and dry run only, not deployed", and that the deploy, the `--upload` path (OpenAI egress, which needs
   Andrew's per-use word) and the `bd-securities` write (its own never-widen half) are NOT authorized by it. None of the three has been
   given since.
2. The prior version listed an empty prefix and classified nothing. This version lists `gold/canonical/holdings/`; its own dry run read
   1,253 new securities to classify. So the two versions differ in whether a vendor call and a table write can happen at all.
3. It admits the class `other`. Andrew's word of 2026-10-07 is six classes: cash, fixed income, equity, structured, alternatives,
   commodities. `other` is not one of them.

## Who acts

`2.0.0_SA_COO~M`, the row's disarm owner, seated for this by `0.0.0_AB_MSTR` on this seat's ask. The act: copy the named version onto
the key with a ledger entry under `org/critical_paths/change_management/`, read the key back byte-equal to the pre-8f67065e50 blob, and
write the disarm row. Rollback of the rollback: the 04:16:37Z version stays in the bucket's version history.

## Also owed by the same seat (the row names one script; the push wrote more)

`0.0.0_AB_MSTR`'s push 1 of 2026-10-07 wrote 11 gold scripts (bd gold 4, cot gold 7) through the push gate (its session log @3614b54eec).
For each of the 11: is the live S3 version a change with a signed half, or not. Print 11 of 11. An unsigned one is a row, with the same
roll-back default.

## Not ruled here

Whether Cottonwood's gold run invokes B_01b with `--upload` was not read by this seat; the ruling does not depend on it.

-- 1.0.0_SA_CTO
