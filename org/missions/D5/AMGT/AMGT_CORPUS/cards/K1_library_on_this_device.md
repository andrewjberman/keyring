# K1 -- the research library on this device (CRPS-c-4)

Answers PRD row K1 in plain words, each line quoting this worker's own printed
output from `0.9.0_WK_AMGT_CORPUS~1`'s run on this device (2026-09-22/23).

## The derived root and how it was derived

`python -m lib.research.corpus.library --census` printed:

```
root C:\Users\Opal Bloomberg\OneDrive - Opal Capital\Shared - Documents\Asset Management\Research
root_source env:OneDriveCommercial+relative
```

`library_root()`'s derivation order is: (1) env `OPAL_RESEARCH_LIBRARY_ROOT`
(not set on this device); (2) env `OneDriveCommercial` joined with
`Shared - Documents/Asset Management/Research` -- **this is the candidate
that won**, since `OneDriveCommercial` is set to
`C:\Users\Opal Bloomberg\OneDrive - Opal Capital` on this device; (3)
`Path.home()` joined with `OneDrive - Opal Capital/Shared - Documents/Asset
Management/Research` (would have resolved to the identical path here, but
candidate 2 wins first). No path string is typed anywhere outside
`lib/research/corpus/library.py`'s `_candidates()`.

## Folder and file counts against the scan's 93 and 351

Same run printed:

```
folders 93 files 351
ext .docx 71
ext .html 1
ext .pdf 184
ext .png 17
ext .xlsx 78
```

This matches the L5 scan's own denominators exactly: **93 folders, 351
files** (184 .pdf, 78 .xlsx, 71 .docx, 17 .png, 1 .html). `folders` is
`library.list_folders(root)` (an independent top-level directory listing, so
a folder with zero files would still count -- none does on this device).
`loose_root_files 0` -- no loose files sit directly at the library root, also
matching the scan.

`python -m lib.research.corpus.backlog --write` independently confirms the
folder count from the SAME fresh listing: `folders_read 93 = resolved 33 +
unresolved 60 + ambiguous 0`, `sum_check OK`.

## The placeholder count

Same run printed:

```
placeholders 103 of 351
```

Matches the scan's measured **103 of 351** OneDrive cloud placeholders
(`st_file_attributes & 0x400000`, `FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS`).
`library.census()` reads this bit via `os.stat(follow_symlinks=False)` only
-- it never calls `open()`, so none of the 103 was hydrated by this cell's
run (`LISTING DOES NOT OPEN`, proven offline in
`lib/research/corpus/tests/test_library.py::test_census_does_not_open` with
`builtins.open` monkeypatched to raise).

## What separates a PARTIAL sync from a SMALL library

Same run printed:

```
partial_sync_signal 103 of 351 listed files carry st_file_attributes & FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS (0x400000) -- a OneDrive cloud placeholder not yet hydrated on this device. os.stat exposes this bit on the LISTING plane without opening the file, so a placeholder count > 0 is itself measured evidence the sync is still in progress, distinguishing a PARTIAL sync from a genuinely SMALL library on this signal alone.
```

So on THIS device, at this run, the placeholder count IS the listing-plane
signal, and it reads non-zero (103), which is itself evidence this sync is
not fully hydrated -- a small, fully-synced library would read
`placeholders 0 of <n>`.

**What separates the two cases when the placeholder count reads zero:**
nothing on the listing plane does (a fully-synced small library and a
fully-synced partial one both read `placeholders 0 of <n>` identically).
`lib/research/corpus/library.py`'s `_partial_sync_signal()` states this
explicitly in that branch: the fallback is comparing THIS census's
folders/files counts against a **prior vintage's counts read back from the
store** -- `python -m lib.research.corpus.backlog --read-latest`, which reads
the gold `research-backlog` object this same cell writes
(`lib/research/corpus/gold.py` `gold_put`/`gold_list`, one object per scan
vintage, never overwritten). A library that is genuinely shrinking or
growing across vintages is distinguishable that way; a library that holds
steady at 0 placeholders across two vintages is evidence, not proof, of a
small and stable library rather than a sync artifact.
