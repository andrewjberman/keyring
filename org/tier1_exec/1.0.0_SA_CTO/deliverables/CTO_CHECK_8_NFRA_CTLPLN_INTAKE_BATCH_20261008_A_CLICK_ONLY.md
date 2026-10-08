# CTO check 8 -- NFRA_CTLPLN package intake, batch intake-20261008-a: the second file signed

**Author:** `1.0.0_SA_CTO`, 2026-10-08 ~07:0xZ. **Read by this seat, itself:** the check record
`org/devices/intake/records/intake-20261008-a/click-8.3.1-py3-none-any.whl.check.json` @a4004b9f02, every check line; and the
held file's SHA-256, computed by this seat from `C:\opal-intake\holding\intake-20261008-a\`.

CHECK 8 SIGNED

## The one file this signs

```
intake-20261008-a
click-8.3.1-py3-none-any.whl
```

sha256 `981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6` (this seat's own hash of the held file equals the
record's), 108,274 bytes. For both Dells: the one package of the 162 that the Python 3.12 kit could not carry.

## What the seven checks said, as this seat read them

| # | Check | Verdict | What this seat takes from it |
|---|---|---|---|
| 1 | the file's digest equals the index's | passed | digest and size equal the published values |
| 2 | name, version and tags are the approved line | passed | click 8.3.1, a pure-Python file for any platform |
| 3 | a version this machine already runs | NOT APPLICABLE | the laptop runs 8.3.1, but as an editable install whose source folder is gone: there is no copy of the published files to compare |
| 4 | the release's age and history | passed | 326 days old; 64 earlier releases |
| 5 | build attestation | passed | the index shows one for this file |
| 6 | the archive's files against an installed copy | NOT APPLICABLE | follows from check 3 |
| 7 | the antivirus's on-access read | passed | enabled and current; the file present and unchanged after 20 s |

## What is and is not established

Established: this is the file the click project published under that name eleven months ago, unaltered, with a build
attestation; the same version has been in use on this laptop. NOT established by a comparison: that its code equals a
known-good copy, since none exists here in published form. For a pure-Python file of a widely used project at that age this
seat accepts the remainder. The first run of this file was a failed check 6 caused by the tool counting missing reference
files as different; the tool was repaired (@4a584469fb) and the file re-checked before this signature, not signed around.

**SIGNED, check 8, for the one file above** -- `1.0.0_SA_CTO`
