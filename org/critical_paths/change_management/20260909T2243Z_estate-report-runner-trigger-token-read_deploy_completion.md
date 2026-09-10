# DEPLOY COMPLETION LEDGER -- estate-report-runner TRIGGER-TOKEN READ (NFRA_OUTSET.TO-OS-s-26)

**Opened:** 2026-09-09T22:43Z by `0.7.0_AE_CloudOps~W` (committed OPEN at `d1c0fa3c83`)
**Status:** **CLOSED 2026-09-09T22:45Z** -- all four legs verified, both controls fired
**TO:** `org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-26.the-trigger-token.md`
(cell `OS-s-26`, PRD v0.8 @`dc6a33c3e3`; issuance `26f1cd8b82`)

⛔ **Committed OPEN before the upload.** Fifth use of this shape today; the OS-s-19 shape exactly.

## What

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`, carrying
`git show HEAD:infra/aws/ec2/estate-report-runner/estate_report_runner.py` @`959c99016e`.

**IT DOES NOT REPLACE THE HOST** -- no `user_data` change, so `instance.tf:83` is not triggered; the
host pulls the runner at every boot (`instance.tf:215`).

**THE CHANGE:** the runner reads the orchestrator's trigger token at boot and stamps
`run_bundle.trigger` and `run_bundle.run_id`. Absent, unreadable, malformed or STALE reads
`UNKNOWN`, never `scheduled`.

## Why this deploy must land BEFORE OS-s-24

`TO-OS-s-24`'s manual served day invokes the orchestrator with `{"mode":"daily-run","trigger":"manual"}`
and then reads `run_bundle.trigger == "manual"` off the served report. **The orchestrator half is
already applied** (the token is written from this moment on), but a runner that cannot read it would
produce a report with no `trigger` field at all -- and the accept would fail for the honest reason
that the carrier was only half-deployed. This is the read half.

## THE WINDOW

The host self-stopped 15:32:42Z; instance state read LIVE immediately before this write:
**`stopped`**. The next SCHEDULED fire is 2026-09-10 13:00Z, and OS-s-24's manual invoke is after
00:00Z. **The upload lands outside both.** The box is not started by this act.

## PRE-STATE, measured live

| | value |
|---|---|
| Served object | **168,853 B**, ETag `b6fd49329e80a1bae8152991893ac498`, LastModified 2026-09-09T15:59:02Z, VersionId `eg2KHrrDxdwdgZrpWYPudGBZ_ThwA.08` (the OS-s-22 upload) |
| HEAD bytes to upload | **173,482 B**, md5 `03298f0f5c2177335349ce053a744bc4`, sha256 `082f4cf5ab78440b...` |

**Bytes are `git show HEAD:<path>`, COMPARED to the worktree and not assumed equal** -- identical
here (same length, same md5, same sha256, 0 CRLF both), stated because the next file may differ.

## EVERY CONSUMER OF THE KEY

Unchanged and re-stated rather than assumed carried: exactly ONE functional consumer,
`estate-report.service` on `i-0584e17d283fa7ef4`, whose `ExecStartPre` pulls the key at every
service start (`instance.tf:215`). The orchestrator reads no code key -- it now writes the token
object, which is a different key and a different direction.

## Legs -- ALL FOUR VERIFIED

1. [x] Uploaded 2026-09-09T22:44:30Z, instance read LIVE as `stopped` immediately before. New
       VersionId `BUorf3uM3aGvDQRveDn8JvdMvWoPGVK6`.
2. [x] ETag `03298f0f5c2177335349ce053a744bc4` **== the HEAD md5**; ContentLength 173,482.
       **THE OS-s-19 CONTROL FIRED:** the PRIOR served blob's md5 is
       `b6fd49329e80a1bae8152991893ac498`, which does **not** match -- so the ETag test
       discriminates rather than passing on any deploy.
3. [x] CONTENT diff: served sha256 `082f4cf5ab78440b...` == HEAD, 173,482 B both. NEGATIVE CONTROL:
       one bit flipped at offset 100 with the length held fixed -> MISMATCH.
4. [x] **The token READ is in the SERVED bytes**, a control per token against the PRIOR served
       object:

       | token | prior | new | verdict |
       |---|---|---|---|
       | `OUTSET_TRIGGER_KEY` | 0 | 2 | ADDED |
       | `_trigger_token_read` | 0 | 2 | ADDED |
       | `_trigger_for_run` | 0 | 2 | ADDED |
       | `TRIGGER_TOKEN_MAX_AGE_S` | 0 | 3 | ADDED |
       | `config/last-trigger.json` | 0 | 1 | ADDED |
       | `"trigger": trigger` | 0 | 1 | ADDED |
       | `"run_id": run_id` | 0 | 1 | ADDED |
       | `run_pin` | 1 | 2 | CONTROL, both sides |
       | `_stratum_propagation` | 3 | 3 | CONTROL, both sides |

       **The last two rows are the control that makes the first seven mean something.** A reader
       that returned 0 for every token on the prior side -- because it failed to open that file, say
       -- would produce seven identical-looking ADDED verdicts. Two tokens present on BOTH sides
       prove the prior object was actually read.

## POST-STATE

| | value |
|---|---|
| Served runner | **173,482 B**, ETag `03298f0f5c2177335349ce053a744bc4`, VersionId `BUorf3uM3aGvDQRveDn8JvdMvWoPGVK6` |
| Identical to | `git show HEAD:infra/aws/ec2/estate-report-runner/estate_report_runner.py` |
| Grants, applied plane (census 22:41:56Z) | orchestrator `s3:PutObject` on `config/last-trigger.json` ONLY; runner `s3:GetObject` on the same ONE key |
| Carrier state | BOTH halves live: the orchestrator writes the token on every invoke from now; the served runner reads it |

## Rollback

One `copy-object` from VersionId `eg2KHrrDxdwdgZrpWYPudGBZ_ThwA.08` (168,853 B, the OS-s-22 runner),
in session, no Terraform. Versioning is Enabled. **Note the asymmetry, stated deliberately:** rolling
the runner back leaves the orchestrator still WRITING tokens, which is harmless -- an unread token is
inert -- but the reverse would not be, which is why the read half ships second.

## Close condition

All four legs checked. **The ACCEPT is not this entry** -- `O26-AC1`'s positive arm reads OS-s-24's
manual served day. This entry records that the read half is SERVED.
