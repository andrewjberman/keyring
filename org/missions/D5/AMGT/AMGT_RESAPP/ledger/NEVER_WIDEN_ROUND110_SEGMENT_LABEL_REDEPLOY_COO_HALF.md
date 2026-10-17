# NEVER-WIDEN CO-SIGN -- COO HALF. Round 109, `AMGT-bp-6`: the redeploy of `opal-amgt-scoped-api` from the release pin `7a8f2bb8e6`, carrying `AMGT-bp-3`'s segment-column label

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-17 ~14:1xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND110_SEGMENT_LABEL_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND106_FORWARD_PE_WITHHOLD_REDEPLOY_COO_HALF.md`.
**Applier:** the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34; CTO msg 6816 names `0.7.0_AE_CloudOps~SC1`). **Source:** the CTO's round-108 analysis item 2 (`ledger/ROUND_ANALYSIS.round108.md`, msg 7490) and round-109 analysis item 2 (msg 7530); orders `AMGT_RESAPP.TO-AMGT-bp-3.*` (merged `1514402a12`) and `AMGT-bp-6` (cut when both halves are signed).
**Status:** DRAFT, not yet signed: it binds on the bytes the CTO half names. Nothing is deployed by this document.
**Measured from** the live function (read 2026-10-17 ~14:1xZ) and this checkout's handler over the live pool, instruments in `deliverables/2.0.0_SA_COO~R1/round110_prep/checks/` (`r110_bp3_served_delta.py`) and `round94_prep/checks/r94_admission_table.py`; outputs `round110_prep/bp3_served_delta.json` and `bp3_served_delta_summary.txt` @`dc66bb9e70`.

## THE ACT

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from the RELEASE PIN **`7a8f2bb8e6`** (branch `rel-amgt-bp6`, LOCAL on dell1): its parent is the live pin `3818736e6b` (the build input of the live package, round 106 `bm-3`) and its only change against it is `lib/research/api/segment_served.py`, taken byte for byte from the bp-3 merge `1514402a12`. **The pin is NOT the box branch head on purpose:** between `3818736e6b` and `1514402a12` sixty-three packaged members differ (`lib/research/harvest/store.py` +162 -8, eight `aifill` members, `opal_data_harvest`, registry files; `r94_admission_table.py 1514402a12 --pin 3818736e6b`), none of which belongs to this act. Read now: `r94_admission_table.py 7a8f2bb8e6 --pin 3818736e6b` prints **`members whose bytes differ: 1`**, `lib/research/api/segment_served.py`, blob `cd72ba96223a` at the live pin to `cbf094d0b633` at the release pin (+9 -5).
Live pre-act, read 2026-10-17 ~14:1xZ (`get-function-configuration`): CodeSha256 `UIkRgr9gbz2RbsaOJq2uRe3aZPOgNE/YoCAG6j7HyO4=`, LastModified 2026-10-16T09:12:01Z (the AI-fill hold removal, an environment change under `ar-8`; the code is the `bm-3` package), memory 1769, timeout 29, RevisionId `54f36694-8c00-4ce9-9dc1-dcfa3be92406`, environment `{HARVEST_METRICS_TABLE, HARVEST_ARTICLES_TABLE}` (no `AMGT_AIFILL_ROOT`: the hold is lifted and stays lifted).

What changes at request time (read in the pin's `segment_served.py`, `_serve`): a segment-table period whose `fiscal_year` is unresolved AND whose `top_level_sum` is not null is served `label` `Year not stated (column <n>)` instead of `Period <n>`; a period with no figure keeps `Period <n>`; a tied period keeps `Fiscal year <Y>`. The three period-note constants `NOTE_NO_REVENUE`, `NOTE_NONE_TIE` and the second sentence of `NOTE_SOME_NAMED` say "the years ... are not stated" instead of "keep Bloomberg's own period numbers". `fiscal_year`, `top_level_sum`, every row value, `currency`, `units` and `status` are not changed. No new key is added to any body.

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE function's `/thesis` body against this checkout's own handler on the same live pool, the `segment_table` block compared (the checkout also carries other merged rounds the live function has not deployed, so nothing else is compared). Read at the cut: every non-test file under `lib/research/api/` is byte-identical between the release pin `7a8f2bb8e6` and the checkout `1514402a12` (`git diff --stat` empty for `segment_served.py`, `segment_table.py`, `segment_period.py`, `segment_labels.py` and `scoped_amgt.py`; only two test files differ), so the pin's handler and the checkout's are the same code for this block. NOT asserted: that `lib/research/harvest/store.py` (+162 -8 between the live pin and the checkout, read by the checkout during the measurement, absent from the release pin) does not touch the segment read; the post-act read below is the control for that.. Floating-point summation noise below a relative 1e-9 (the Lambda runtime and this checkout add the same figures in a different order) is not a difference.

| reading | value |
|---|---|
| resolved names read | **95**, status 200 and 200 on every one (ERROR 0) |
| `segment_table` EQUAL | **82** |
| differs ONLY in a period label and/or a period note | **13** (LABEL_NOTE) |
| differs in ANY other key (rows, currency, units, status, `top_level_sum`, `fiscal_year`) | **0** (OTHER 0) |
| columns relabelled | **16 on 10 names**: `8766 JP` (column 1), `9433 JP` (4), `AMD US` (2, 3, 4, 5), `CDNS US` (5), `KPN NA` (4, 5), `NG/ LN` (4), `RIO LN` (5), `RWE GR` (3), `SAN FP` (1, 4, 5), `SNPS US` (4); `AMXB MM`, `BATS LN` and `JD US` differ only in a reworded period note |
| controls | `RIO LN` reads LABEL_NOTE with `Period 5` to `Year not stated (column 5)`; `ICT PM` and `VLO US` read EQUAL |

The first run of the instrument read ten OTHER names; all ten were floating-point noise in `top_level_sum` (for example `992 HK` 83074.555 against 83074.55500000001), and a thread-unsafe stdout redirect had swallowed its summary lines; both are fixed in the committed script.

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, admitted by BLOB at the GO

**ONE member:** `lib/research/api/segment_served.py`, blob `cbf094d0b633` (the live package carries `cd72ba96223a`). **The BUILT package's content diff against the live package is the authority.** If the built package carries ANY other member that differs from the live package, or `segment_served.py` at another blob, that is a STOP BEFORE UPLOAD and returns to me for an addendum to both halves. NO IAM, route, memory, timeout, schedule, layer, environment variable, store write or S3 delete. The act writes NO data object. The Terraform plan must show the CODE only (the artifact hash and key) on the function; a plan that moves the environment, role, layers, memory or timeout is a STOP.

## WRITER CENSUS of the moved served property (N printed, each rule read in the pin)

- `periods[].label`: **ONE** assignment, `_serve` in `segment_served.py` (`label, note = "Fiscal year %s" % year, None` for a tied column, else the new rule); a second label path exists only for the `status none` branch (`rows` empty, `operating_income_rows` present), where `periods` are built `"Period %d" % n` with `top_level_sum` None and are NOT changed (no figure, so no relabel). **N = 1 for the changed rule.**
- `period_note` and each period's `note`: the three constants above, selected by `top_reason` and the named-column count in `_serve`; **N = 1** selection site.
- READERS of the served label: the portal's `SegmentTable.tsx` (prints `period.label` as the column head and `<label> is not shown: <note>` for a dropped no-figure column, which keeps `Period <n>`); `lib/research/api/scoped_amgt.py` only passes the block through. No other reader of a segment period label was found in `lib/research` (a search for `segment_table`, `period.label` and `.periods` matched `segment_served.py`, `scoped_amgt.py` and `segment_table.py` only; the portal was read for `SegmentTable.tsx` only).

## SEQUENCE CONDITION

None on the page: `SegmentTable.tsx` prints the served label verbatim, so the portal needs no change and no page lands first. The act is independent of the DEV landing of `bp-1` and `bp-4`.

## THE GO, THE READS AFTER, AND THE ROLLBACK

1. **GO:** after the CTO half is signed on these bytes, the issuer cuts `AMGT-bp-6` to the applier with this half and the CTO half inlined and the pin named; the applier builds from a detached worktree at `7a8f2bb8e6`, prints the content diff against the live package, and STOPS on anything outside the blast radius.
2. **Reads after the act (the issuer's, same turn):** `r110_bp3_served_delta.py` re-run against the NEW live function must read **EQUAL on all 95 names, LABEL_NOTE 0, OTHER 0** (the live function now equals this checkout on the block), and `RIO LN`'s live `/thesis` `segment_table.periods[4].label` must read `Year not stated (column 5)`. A name that still reads LABEL_NOTE after the act means the package did not take: STOP and roll back.
3. **Rollback (same window):** re-point the function to the previous package, the `bm-3` build at pin `3818736e6b` (CodeSha256 as printed above, RevisionId `54f36694-8c00-4ce9-9dc1-dcfa3be92406`), by re-applying that build through the same saved-plan route; no data object was written, so there is nothing to restore per key. The served labels return to `Period <n>` on the next request.
4. **Ledger:** a change-management entry opened at the start and closed at completion (CLAUDE.md NEVER-2); the applier names every task family that pulls the artifact (one `describe-function`/task-definition sweep; this half asserts none beyond the function itself and does not census other consumers of the package).

## WHAT THIS HALF DOES NOT COVER

The portal candidates (`bp-1`, `bq-1`, `bp-4`), the G4 filings task and its first positive arm, any other served property, and any later pin. A different pin, a second leg or a widened member set needs a new pair.
