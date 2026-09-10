# DEPLOY COMPLETION LEDGER -- estate-report-runner OS-s-27 STRATUM STRINGS SERIALIZED

**Opened:** 2026-09-10T14:12Z by `0.7.0_AE_CloudOps~W` (committed OPEN at `b1dff81db7`)
**Status:** **CLOSED 2026-09-10T14:18Z** -- all four legs verified. **The ACCEPT is not claimed
here and neither is the SERVED confirmation**: the first run to serialize these fields is
2026-09-11 13:00Z.
**TO:** `org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-27.the-stratums-own-strings-reach-the-artifact.md`
(cell `OS-s-27`, issued @`c556e21178`, decomposition v0.9 s.32; GO at msg 95206)

⛔ **Committed OPEN before the upload**, so "opened first" is a fact in git history rather than a
claim in prose. Closed in a second commit after the legs verify.

## What

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`.

**No `user_data` change, so no host replacement. No IAM change. No served report rewritten.**

**THE CHANGE:** a stratum's own `vintage` and `denominator` are serialized as FIELDS
(`stratum_vintage`, `stratum_denominator`) beside `stratum_status` at `ai.groups.<G>`, via one new
named function `group_out_fields()`.

## WHY BOTH, AND WHY ONE WOULD HAVE BEEN A FAILED CELL RATHER THAN A PARTIAL ONE

Rows `NFRA_OUTSET-S40` and its correction `NFRA_OUTSET-S41`. Two adjacent lines in the runner send
the two halves of the group-B disclosure to **different strings**:

```
:1424   den = "%s -- %s" % (den, grain_note)                          -> DENOMINATOR
:1425   vin = "%s [grain=%s, NOT resource-grain]" % (vin, grain)      -> VINTAGE
```

| field | what it carries | which accept reads it |
|---|---|---|
| `stratum_denominator` | the ROSTER, the per-device states, the grain NOTE | **O22-AC1 clause (v)** |
| `stratum_vintage` | the grain TAG `[grain=..., NOT resource-grain]` | **O23-AC1** |

S40 attributed both to the denominator. **S41 corrected that before the remedy was cut**, which is
why this cell serializes both. A denominator-only fix would have closed one accept and presented as
complete.

## WHAT REACHED THE ARTIFACT BEFORE, AND WHY IT WAS NOT ENOUGH

Neither string. What a reader met was `ai.proposals[].tool_row_cited` -- **a string the MODEL
composes**, admitted by `tool_row_resolves` on a two-token substring containment test
(`name in cited_ref and vintage in cited_ref`), against a ref built from the **TRACE's** vintage,
not the field `:1425` writes. So the grain tag could not have been caught by that gate under any
composition, and on the 13:00Z run five of five candidates shipped without it while nothing failed.

⛔ **THE VALIDATOR IS DELIBERATELY OUT OF BOUNDS** (issuer, 95206). Once the artifact carries the
runner's own strings as fields, that validator stops being the only carrier and its looseness stops
being load-bearing. If it still admits an unlabelled citation AFTER this lands, that is its own
finding with its own evidence and its own cell. **Recorded here rather than fixed here.**

## THE PRE-STATE, measured live before the upload (2026-09-10T14:11:37Z)

| | value |
|---|---|
| Served object | **180,310 B**, ETag `d9b82ec4578251ed3c335e992e2fbe84`, LastModified 2026-09-10T12:55:13Z, VersionId `Vl2cyFrB8dphstJ8IX2iNt01oDrMt7Sp` (the OS-s-22 disclosure-arm runner) |
| Instance `i-0584e17d283fa7ef4` | **`stopped`** (read LIVE at 14:11:37Z) |
| Next scheduled fire | **2026-09-11 13:00Z**; today's already ran at 13:01:01Z |

⛔ **ALREADY-SERVED CHECK, required by arm (f) before uploading:** the served ETag above is the
md5 of the PREVIOUS commit's blob, not of the bytes this act carries. They differ, so this is a
real upload and **not** a SUPERSEDED close.

## THE WINDOW

The host is `stopped` and is NOT started by this act. Today's run has already completed, so this
upload lands **outside** any run window and the first execution of these bytes is the
**2026-09-11 13:00Z** scheduled fire. **No ad-hoc run is fired to force an early exercise.**

## EVERY CONSUMER OF THE KEY THIS ACT MOVES

Re-stated at this act rather than carried: exactly ONE functional consumer --
`estate-report.service` on `i-0584e17d283fa7ef4`, whose `ExecStartPre` pulls
`code/estate_report_runner.py` at every service start (`instance.tf:215`). The orchestrator Lambda
holds one environment variable, `ESTATE_INSTANCE_ID`, and reads no code key. **ONE task family, no
shared tag.**

## Rollback -- stated before the act

One `copy-object` from VersionId `Vl2cyFrB8dphstJ8IX2iNt01oDrMt7Sp` (180,310 B), in session, no
Terraform. Versioning is Enabled and the prior object is not deleted by an overwrite. **The data
plane is untouched in either direction** -- no schedule, no IAM grant, no instance, and no served
report key.

## Legs -- ALL FOUR VERIFIED

1. [x] Uploaded **2026-09-10T14:15:40Z**. Instance state read LIVE at 14:15:23Z, immediately
       before: **`stopped`**. New VersionId `8pG9vs5I4CSGNVC8OcUy2Q9ARArGgumx`, ETag
       `3468e13b854c5e9af649c90cd1e11c39`.
2. [x] ETag `3468e13b854c5e9af649c90cd1e11c39` **== the md5 of `git show HEAD:<path>`**;
       ContentLength **182,986 B** (from 180,310 B).
3. [x] **CONTENT diff.** The object was **RE-DOWNLOADED BY ITS NEW VersionId** rather than trusted
       from the PUT response or from `head-object`'s ETag: sha256 `ee3bda020b355da6...` on both
       sides, 182,986 B both. **NEGATIVE CONTROL:** one bit flipped at offset 100 with the length
       held fixed -> the comparator reports MISMATCH.
4. [x] **NOTHING ELSE MOVED**, four separate checks with printed denominators:
       - the composed strings at `:1421-1425`: **2 of 2** present on both sides, counts unchanged.
       - `tool_row_resolves` **823 B, sha256 `df759dfcc3cc`** and `tool_row_ref` **590 B, sha256
         `b36dfc7a4b61`** -- **BYTE-IDENTICAL** between the prior served version and this one.
         Compared as function bodies, not counted, because a count cannot see an edit that keeps
         the length.
       - the 13:00Z run's four group statuses (`A OK, B OK, C INSTRUMENT_FAILED, D OK`) read from
         the served artifact and rewritten by nothing.
       - **0 of 6** served report/manifest keys moved: the 09-09 pair and manifest still stamped
         00:58Z, the 09-10 pair and manifest still 13:34:36Z.

## POST-STATE

| | value |
|---|---|
| Served object | **182,986 B**, ETag `3468e13b854c5e9af649c90cd1e11c39`, VersionId `8pG9vs5I4CSGNVC8OcUy2Q9ARArGgumx`, LastModified 2026-09-10T14:15:40Z |
| Identical to | `git show 22ca10d25e:infra/aws/ec2/estate-report-runner/estate_report_runner.py`, sha256 `ee3bda020b355da6...` |
| New fields it will serialize | `stratum_vintage`, `stratum_denominator`, at `ai.groups.<G>` |
| Versions of the code key | **22**, rollback target named from the live list rather than from memory |

## Close condition

All four legs checked. Closed in a second commit flipping the Status line.
⛔ **THE ACCEPT IS NOT THIS ENTRY,** and the SERVED confirmation is not claimed by it either: the
first run to serialize these fields is **2026-09-11 13:00Z**. `O27-AC1`'s arms (b), (c) and (d)
render the new block OFFLINE from the SAME pinned inputs the 13:00Z run read, through the DEPLOYED
bytes -- which is what the face asks for, and which the cell's own bound ("no served report is
rewritten") requires.
