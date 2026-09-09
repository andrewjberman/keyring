# DEPLOY COMPLETION LEDGER -- estate-report-runner PER-DEVICE CONSUMER (NFRA_OUTSET.TO-OS-s-22)

**Opened:** 2026-09-09T15:57Z by `0.7.0_AE_CloudOps~W` (committed OPEN at `7b9bbecd34`)
**Status:** **CLOSED 2026-09-09T15:59Z** -- all four legs verified; the ACCEPT remains pending the
2026-09-10 13:00Z scheduled fire and is NOT claimed here
**TO:** `org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-22.the-per-device-consumer.md`
(cell `OS-s-22`, outcome_ref FWD-3; issuance `6facf7eef3`, PRD v0.5 @`1ac8679844`)

⛔ **Committed OPEN before the upload**, so "opened first" is a fact in git history rather than a
claim in prose. Closed in a second commit after the legs verify. The OS-s-19 shape exactly, and the
third time this seat has used it today.

## What

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`, carrying
`git show HEAD:infra/aws/ec2/estate-report-runner/estate_report_runner.py` @`1dd59a6bab`.

**IT DOES NOT REPLACE THE HOST.** No `user_data` change is in this act, so
`instance.tf:83`'s `user_data_replace_on_change` is not triggered; the host pulls the runner at
every boot (`instance.tf:215` ExecStartPre). One replacement today was enough and this is not a
second.

**THE CHANGE:** group A composes every rostered `<prefix>/<device>/comp_heat_drift.json`, renders
each device with its own vintage and 26 h ceiling, and **RETIRES the single-key read with the
composition** rather than beside it.

## SEQUENCING, AND WHY THIS DEPLOY WAITED ~90 MINUTES FOR ITS SIBLING

Sequencing across the three open orders is this seat's (issuer, 2026-09-09 ~15:4xZ). Deploying this
consumer while NO per-device key existed would have retired a read of a REAL artifact
(`outset/comp_heat_drift.json`, 154 rows, published under OS-s-18) and replaced it with a roster
whose only answer was a QA probe -- a self-inflicted degradation of the served report, for a window
of unknown length, while OS-s-21's drift half was still being cut. So the device publisher landed
FIRST:

| key | bytes | written | content |
|---|---|---|---|
| `outset/laptop/comp_heat_drift.json` | 27,577 | 2026-09-09T15:55:16Z | device `laptop`, n=157 (6 modified, 151 untracked), **tracked_total 30,786**, git_head `1dd59a6bab55` |
| `outset/_os22_probe_device/comp_heat_drift.json` | 1,153 | 2026-09-09T15:55:18Z | the QA fixture: device `_os22_probe_device`, n=2, tracked_total 7 |

So at the moment of this upload the roster has a REAL reporting device and a probe, and the
composition has something true to render on its first served day.

## THE WINDOW

`estate-report-0900et` ENABLED, `cron(0 9 * * ? *)` `America/New_York`. The host self-stopped at
**15:32:42Z** after the creation-boot run (row `NFRA_OUTSET-S22`); the next scheduled fire is
**2026-09-10 13:00Z**. Instance state read LIVE immediately before this write: **`stopped`**.
**The upload lands OUTSIDE the window.** The box is NOT started to force an early exercise -- the
accept is the scheduled fire.

## EVERY CONSUMER OF THE KEY THIS ACT MOVES

Unchanged from the OS-s-19 census and re-stated rather than assumed carried: `comp-find
'code/estate_report_runner\.py'` resolved **154 hits across 152,096 files scanned** to exactly ONE
functional consumer -- `estate-report.service` on the host, whose `ExecStartPre` pulls the key at
every service start (`instance.tf:215`). The orchestrator Lambda holds one environment variable,
`ESTATE_INSTANCE_ID`, and reads no code key. ONE task family, no shared tag.
⚠ The host id changed today (`i-0512bd3cbaf602b7f` -> `i-0584e17d283fa7ef4`) and the consumer is the
same SERVICE on the new instance.

## PRE-STATE, measured live before the upload

| | value |
|---|---|
| Served object | **159,687 B**, ETag `e75c59a35457535ca0d339c9f59589f5`, LastModified 2026-09-09T13:53:22Z, VersionId `GQny85Je837UhagoFc0FY8eoJzcB1RFy` (OS-s-19's upload) |
| HEAD bytes to upload | **168,853 B**, sha256 `af1c3e01ee002a11...`, md5 `b6fd49329e80a1bae8152991893ac498` |

**THE BYTES ARE `git show HEAD:<path>`, COMPARED and not assumed equal to the worktree** -- a
worktree hash on this autocrlf box hashes the CHECKOUT, not the record. Measured identical here
(same length, same sha256, 0 CRLF both), so the distinction costs nothing today; recorded because
the next file may differ.

## OPEN/RED ENTRIES

Re-read at this act rather than carried from the OS-s-19 entry three hours ago: `.open_deploys/`
holds the same 6 named entries (4 OPEN: ADVI_INSURE x2, NFRA_OPSEC x2; 2 HELD-SOVEREIGN-GATED: D12
SMS, FRESHGUARD) and **ZERO name this key**. The 4 scoped hits remain inside
`.unindexed_red_state.json`, an index rather than an open deploy, pointing at two ledgers both
opened AND closed on 2026-08-05 -- three weeks OLDER than the served object's own vintage, so
neither is an unfinished promote of this key.

## Legs -- ALL FOUR VERIFIED

1. [x] Uploaded 2026-09-09T15:58:59Z. Instance state read LIVE immediately before: **`stopped`**.
       New VersionId `eg2KHrrDxdwdgZrpWYPudGBZ_ThwA.08`, ETag `b6fd49329e80a1bae8152991893ac498`.
2. [x] ETag `b6fd49329e80a1bae8152991893ac498` **== the HEAD md5**; ContentLength 168,853.
3. [x] **CONTENT diff, the deciding leg** (Rule 22a -- deployed bytes against the BUILD INPUT, never
       by filename): served sha256 `af1c3e01ee002a11...` == HEAD `af1c3e01ee002a11...`, 168,853 B
       both. **NEGATIVE CONTROL:** one bit flipped at offset 100 of a copy with the length held
       fixed -> the same comparator reports MISMATCH, so the match is a measurement.
4. [x] **THE RETIREMENT, SHOWN IN THE SERVED BYTES RATHER THAN ASSERTED**, with a control per token
       (`W1-S27`: a census of N tokens is N detectors). Compared against the PRIOR served object
       (VersionId `GQny85Je837UhagoFc0FY8eoJzcB1RFy`, the OS-s-19 runner):

       | token | prior | new | verdict |
       |---|---|---|---|
       | `OUTSET_DEVICES` | 0 | 3 | ADDED |
       | `_outset_device_fields` | 0 | 2 | ADDED |
       | `OUTSET_DRIFT_KEY` | 0 | 2 | ADDED |
       | `OUT-OF-CORPUS` | 0 | 4 | ADDED |
       | `tracked_total` | 0 | 15 | ADDED |
       | `prefix.rstrip("/") + "/comp_heat_drift.json"` | **1** | **0** | **RETIRED** |

       The retired read's own detector is proven by its PRIOR count of 1: a pattern that had been
       0 on both sides would have discriminated nothing, which is exactly the defect `S14` recorded.

## POST-STATE

| | value |
|---|---|
| Served object | **168,853 B**, ETag `b6fd49329e80a1bae8152991893ac498`, VersionId `eg2KHrrDxdwdgZrpWYPudGBZ_ThwA.08` |
| Identical to | `git show HEAD:infra/aws/ec2/estate-report-runner/estate_report_runner.py`, sha256 `af1c3e01ee002a11...` |
| Roster it will read | `laptop`, `site-z`, `_os22_probe_device` |
| Keys present for it | `outset/laptop/comp_heat_drift.json` (real), `outset/_os22_probe_device/comp_heat_drift.json` (QA fixture) |

## Rollback -- stated before the act

One `copy-object` from VersionId `GQny85Je837UhagoFc0FY8eoJzcB1RFy` (159,687 B, the OS-s-19
runner), in session, no Terraform. Versioning is Enabled and the prior object is not deleted by an
overwrite. The data plane is untouched in either direction -- no schedule, no IAM grant, no instance.

## Close condition

All four legs checked. Closed in a second commit flipping the Status line.
⛔ **THE ACCEPT IS NOT THIS ENTRY.** `O22-AC1` reads a SERVED DAY produced by a SCHEDULED run after
both this deploy and a device publish have landed. Both have now landed, so the first eligible
reading is **2026-09-10 13:00Z**. Nothing is armed to watch that fire (standing moratorium).
