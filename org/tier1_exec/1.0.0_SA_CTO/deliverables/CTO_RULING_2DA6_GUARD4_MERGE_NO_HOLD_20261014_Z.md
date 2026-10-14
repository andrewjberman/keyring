# CTO ruling -- site Z call sitez-20261013T021538Z-2da6: merge OPAL_BBGTML TO-GUARD-4, change-managed (`1.0.0_SA_CTO~Z`, 2026-10-14 ~09:5xZ)

**The call:** "Merge TO-GUARD-4 ... the custom-CIX recency check ported into the T-zero Bloomberg tripwire, built and proved
on branch rv-bbgtml-guard4?" It was listed as Andrew's act on the 10-06 no-modify hold.

## Why this is no longer Andrew's act

- **Andrew-direct 2026-10-14 ~09:0xZ** (`ANDREW_DIRECT_20261014_090xZ_NO_HOLD_ON_BLOOMBERG_SIGN_IN_REPAIRS.md`, CLOUD
  @dd20a5edf4): "What is the hold you are referring to? There should be no hold".
- **What binds is his 10-06 verbatim aim:** "avoid ... accidentally overwriting any operations in the 'Positioning' pipeline
  and ETFS view operations".
- The "merge waits on Andrew's word" line in the order, and the hold's extension to `integrations/bloomberg/` beyond his
  sentence, were seat text, not his words.
- **Tested against his sentence:** GUARD-4 is a DELIBERATE, proven addition of one check to the T-zero PKL tripwire.
  - `git diff --stat HEAD...rv-bbgtml-guard4`: `pipeline/tzero/tools/bbg_pkl_tripwire.py` +87, plus its report and proof.
  - It overwrites no Positioning or ETFS-view operation.
  - So it is a call this seat rules.

## Ruling: YES, merge as a change-managed deploy under OPAL_BBGTML (issuer `2.0.0_SA_COO~ZB`)

- **The tripwire is the publish gate,** so a stricter check can stop a publish. The merge is therefore a deploy:
  - a change-management entry, opened first;
  - landing OUTSIDE the 10:30Z-12:30Z pull window;
  - one real run of the T-zero tripwire on that day's PKLs, read back as PASS, before the next scheduled pull depends on it.
- **A FAIL on real data** reverts the merge the same act and files a row. The check is never relaxed in place.
- **Branch:** `rv-bbgtml-guard4` @3b65362444 is LOCAL only, in locked worktree `C:/tmp/rv-guard4`. The issuer merges from
  there; the lock is lifted only after the merge reads on `box/sitez`.
- **Not touched:** any Positioning or ETFS-view operation, the notebooks and the upload path.

-- 1.0.0_SA_CTO~Z
