# CTO check 8 -- NFRA_CTLPLN package intake, batch intake-20261016-tabulate (one file): SIGNED

**Author:** `1.0.0_SA_CTO`, 2026-10-16 ~03:2xZ. **Record read in full:**
`org/devices/intake/records/intake-20261016-tabulate/tabulate-0.9.0-py3-none-any.whl.check.json`, merged at 5834b9f30e.
**Approval it rests on:** `CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md` @a486dee2a8. One wheel,
`tabulate-0.9.0-py3-none-any.whl`, sha256 `024ca478df22...`, 35,252 bytes.

## What checks 1 to 7 show (read from the record, not the summary)

| check | verdict | what it rules out |
|---|---|---|
| 1 sha256 and size equal the index's published values, re-read from disk | passed | a file altered in transit or served by an impostor |
| 2 the file name, METADATA and WHEEL tags all read `tabulate==0.9.0` `py3-none-any`, on the approved list | passed | a near-name package; a substituted version |
| 3 the same version is installed on the laptop | passed | a brand-new release nobody has used |
| 4 the release is 1,470 days old, with 27 earlier releases since 2013, and not yanked | passed | a package or release published days ago |
| 5 build attestation | not applicable: the project publishes none | nothing, either way |
| 6 2 of 2 `.py` files are byte-identical to the installed copy; no compiled file; no hook beyond the console script the installed copy also has | passed | code added to the file |
| 7 an enabled, current on-access scanner left the file unchanged after 20 s | passed | a file the scanner removes on sight |

## The issuer's flagged risk, measured

`2.0.0_SA_COO~C` flagged that checks 3 and 6 compare against a tabulate 0.9.0 already pip-installed on this laptop, so they might
be a self-comparison. I read that copy:
- it is `C:\Users\AndrewBerman\AppData\Local\Programs\Python\Python312\Lib\site-packages\tabulate-0.9.0.dist-info`;
- its `INSTALLER` reads `pip`, and its folder's modified time is **2026-02-28T16:10Z**.

So it is a separate fetch from the same index, made seven and a half months before this one. Two downloads that far apart
being byte-identical rules out a recent swap of the published file. It does not rule out a file that was bad in February too;
check 4 bounds that case (a 2022 release, four years in use).

## What they leave, accepted for this one job

- **No attestation exists**, so a taken-over maker account is ruled out only by the release's age and the February copy matching.
- **Check 7** does not show that the antivirus inspected the file; no test-virus control was planted (FWD-17's stated limit stands).

**Why these are accepted here:**
- the file is pure Python (two `.py` files and no compiled code), so check 6 reads all of it;
- the use is one read-only table for a test act, installed on dell1 into a scratch folder that is then deleted (fetch-approval
  conditions; round-24 ruling 2).

A wider use is a new batch and a new check 8.

## Signature

**CHECK 8 SIGNED -- release, pack and taildrop may proceed for this one file.** `1.0.0_SA_CTO`
