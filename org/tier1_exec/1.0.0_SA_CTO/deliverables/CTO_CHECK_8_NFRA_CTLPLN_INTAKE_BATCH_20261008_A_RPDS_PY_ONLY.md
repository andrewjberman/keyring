# CTO check 8 -- NFRA_CTLPLN package intake, batch intake-20261008-a: ONE file signed

**Author:** `1.0.0_SA_CTO`, 2026-10-08 ~04:3xZ. **Read by this seat, itself:** the fetch record and the check record under
`org/devices/intake/records/intake-20261008-a/` @904660c444 for the file named below, every check line; and `check_8` of
`org/devices/intake/intake_check.py` (lines 713 to 745), to know what this file is matched on.

## The one file this signs

```
intake-20261008-a
rpds_py-2026.6.3-cp314-cp314-win_amd64.whl
```

sha256 `0be972be84cfcaf46c8c6edf690ca0f154ac17babf1f6a955a51579b34ad2dc5`, 220,380 bytes. For site Z, its cell AMGT-bb-18.

## What the seven checks said, as this seat read them

| # | Check | Verdict | What this seat takes from it |
|---|---|---|---|
| 1 | the file's digest equals the index's | passed | computed and published digests and sizes are equal |
| 2 | name, version and tags are the approved line | passed | file name, metadata and tags all read rpds-py 2026.6.3, cp314, win_amd64 |
| 3 | a version this machine already runs | NOT APPLICABLE | the laptop runs 0.30.0; no copy of 2026.6.3 exists here to compare |
| 4 | the release's age and history | passed | 99.87 days old; 71 earlier releases since 2023-03-01 |
| 5 | build attestation | passed | the index shows one for this file |
| 6 | the archive's files against an installed copy | NOT APPLICABLE | follows from check 3 |
| 7 | the antivirus's on-access read | passed | the managed antivirus enabled and current; file present and unchanged after 20 s; no on-demand verdict exists |

## What is and is not established, in plain words

Established: this is the file the real rpds-py project published under that exact name on 2026-06-30, unaltered, with a build
attestation, from a project with a long release history, and the laptop's antivirus did not act on it.
NOT established: that the file's contents are what a Python 3.12 build of the same version would hold, because no such copy
exists here; and nothing here is a behavioural test of the compiled code. The research officer's review named this limit
before the fetch (site Z batch 1, row B) and this seat accepted it then (msg 106436). The delivery text to site Z repeats it.

## What this does NOT sign

The second file of the batch, the click package, is not named in this file and is not signed. Its check 6 reads failed for a
reason in the tool, and it is not released on a failed check.

A note for the tool's owner: this seat's approval-to-fetch file names the batch and BOTH file names, so `check_8` as written
would accept it as a signature for either file. It is not one. Only a file like this one, written after the checks and naming
one file, is passed as `--signed-by`.

**SIGNED, check 8, for the one file above** -- `1.0.0_SA_CTO`
