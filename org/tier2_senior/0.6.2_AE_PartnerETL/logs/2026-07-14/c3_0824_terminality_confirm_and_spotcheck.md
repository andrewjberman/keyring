# 0.6.2_AE_PartnerETL -- OPAL_ASSETS C3: 0824 wide-pull TERMINALITY CONFIRMED + full-parity spot-check (post-crash session)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE
**Date:** 2026-07-14 | **Window:** ~06:5xZ -> 07:4xZ (fresh session after the ~06:49Z fabric crash) | **Serial:** 0.6.2_AE_PartnerETL

## Andrew-direct (VERBATIM -- the durable record, per XXX.md record+broadcast law)

Received mid-hold on the direct session channel, ~07:0xZ, scope = the 0824 wide pull / my C3 lane:

> "confirm 0824 terminality via the manifest while you hold, spot check the files, make sure they are in
> the correct locations and are clean and clear"

Broadcast same turn: COO (073506Z), CTO (073536Z), MSTR (073542Z). Preceding instruction, same channel
~06:5xZ: "finish your startup and hold for more information from the tier 1 agents." -- held; the Tier-1
word arrived 070402Z (CTO re-task confirm) + 070931Z (COO HOLD RELEASED).

## Summary

Startup (watcher armed task bh9vfpfqc, LD-0290 serial file, zero crons) -> held per Andrew -> executed the
Andrew-direct verification. **Verdict: the 0824 wide pull is TERMINAL and the landed estate is CLEAN in the
correct locations on BOTH buckets** -- and the queue picture Tier 1 carried was stale: **the 0824 remap
already ran in my crashed session (06:00Z) and is COMPLETE**, which I verified 3-tier from fresh inventories
rather than re-launching (a re-launch would have been harmless-idempotent, but verification of landed state
is the sharper instrument and does not touch the estate).

## Findings (all grounded on live S3 listings/bytes; denominators printed)

1. **TERMINALITY: CONFIRMED.** Staging `opal-data-schwab/08242234/bronze/` = **5,966 objects = the
   enumerated terminal denominator exactly**; one continuous write window 07-13 23:00Z -> 07-14 05:53:15Z
   (hour histogram 53+847+1122+1068+1009+990+877 = 5,966); quiescent >1h at measurement.
2. **The wide pull wrote NO manifest of its own** -- it ran the pre-manifest puller version; with
   `-Target staging` its OPSROOT (`08242234/_ops/`) does not exist. The sound manifest instrument is the
   POST-pull daily run `opal-data-assets/schwab/08242234/_ops/daily_pull/runs/20260714T064730Z.json`:
   window 06-14->07-14, trading_frontier 2026-07-13, **enumerated 212 / skipped 208 / downloaded 4 /
   failed 0 / ok:true** -- SDD offers nothing in the recent window the wide pull missed.
3. **REMAP ALREADY COMPLETE (stale-queue correction to CTO/COO).** Monolith
   `opal-data-assets/schwab/08242234/bronze/` = **5,970 = 5,966 remapped (writes 06:00Z->06:0xZ, crashed
   session) + 4 daily-pulled 20260713 files (acc/rps/sec/trn, 06:47Z)**. Independent 3-tier from fresh
   inventories: set 5,966/5,966 (0 missing, 4 accounted extras), size 0 mismatches, ETag 0 mismatches on
   5,321 comparable pairs, 645 multipart-ETag keys covered by the size tier (the F-2/13c doctrine).
4. **SPOT-CHECK: CLEAN 21/21 (+ the daily file).** Sample = earliest+latest per type (9 types incl. tcf/
   tcfx/tnn) + 3 random multipart-ETag keys, downloaded from BOTH buckets: md5 byte-identical 21/21;
   outer AND nested-inner zip integrity clean; H1 master = 08242234 in every file, 08335338 in none; firm
   `49 WEALTH MANAGEMENT LLC`; date alignment partition == outer name == inner member name == H1-embedded
   date 21/21. Grammar violations 0/5,966 staging + 0/5,970 monolith; zero-byte 0; all `.zip`.
5. **Product-layout note (banked):** TNN (1099 feed, `BD1099DF`) headers are `H01|`, not `H1|` -- a
   product variant, verified correct master+date by inspection. Same class as the TCF field-position
   lesson: per-product header layouts differ; a literal `H1` prefix assert is too narrow.
6. **0833 channel also proven:** runs 061125Z + 064919Z, latest enumerated 246 / failed 0 / ok:true.
   The 064919Z run completed ~06:49:33 -- the moment of the fabric crash; box work survived (detached).

## Instruments that lied THIS session (each caught by a control, none by care)

- **CRLF poisoning:** python-on-Windows wrote sample keys with `\r\n`; `read -r` kept the `\r`; all 42
  downloads 404'd on `...zip\r` with the `\r` invisible in the error text. The discriminating control: a
  hardcoded-literal key downloaded fine. Fix: `tr -d '\r'`. (Put the control on the RETRIEVAL.)
- **Zip-in-zip, AGAIN:** my second (date-alignment) script read nested-zip bytes as text -- the exact 0833
  census trap, re-walked by its own author within days. Battery 1 (nested-aware) was the sound instrument;
  battery 2's "MISALIGNED" wall was the checker, not the data. Knowing a failure mode by name does not
  immunize you against writing it.
- **`--query 'KeyCount'` does not aggregate across pages** (prints per-page); `length(Contents)` on the
  merged JSON does.

## Housekeeping

- **AD doc state RESOLVED deliberately** (CTO 070402Z ask): `docs/architecture/SCHWAB_AUTO_PULL_DESIGN.md`
  was a phantom pre-relocation staged-add (content tracked at `data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md`
  since a97402e89; old path not in HEAD) -- unstaged; path clean.
- Crashed-session commits confirmed landed: 94597e588 (SYSTEM->Administrator identity), e0810ae9a (line-12
  stderr kill), 0364fcca2 (doc correction), 2d2b13705 (C2-orphan-reap grant, AUTHORED-NOT-APPLIED, still
  gated COO->CTO).

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `aws s3api list-objects-v2` (full JSON inventories, both buckets) | terminality denominator, write quiescence, full 3-tier parity | PASS -- produced findings 1/3/4 |
| `aws s3 cp` (21x2 sample + manifests) | byte-level spot check + manifest reads | PASS after CRLF fix |
| python zipfile/hashlib (nested-aware) | md5 parity, zip integrity, H1 master, date alignment | PASS 21/21 |

No comp-* routed: the task was live-artifact verification of my own lane's just-landed state -- Rule 20/22a
grounds this class on live primitives (comp tools model DESIRED state; the landed bytes are the question).
Operational `aws` (listing/cp verification) is off-rail per CLAUDE.md Rule 21.

## Next Steps

- **[0.6.2 self, armed]** First SCHEDULED fires: 0833 09:45Z, 0824 10:15Z -- manifest watch Monitor armed
  (new runs/*.json after the fire times, failure fields surfaced, deadline-miss emits). Report both to
  COO/CTO/Andrew (this closes the C3(c) acceptance).
- **[0.6.2 self, queued]** Docs -> 2,269 deletion chain (Andrew placement nod -> temp-grant plan to COO ->
  CTO gate -> delete -> grant removal proven). Glacier 257: background, on thaw-complete -> 01raw
  copy+verify -> AC5 grant removal + implicitDeny evidence.
- **[0.4.0_DS_ClientPlatform]** terminal 0824 count (5,966 staging / 5,970 monolith incl. 20260713) -- in
  my COO report; DS can proceed on W4 with the real denominator.

## MCP traffic

CTO 070402Z (re-task confirm) + COO 070931Z (hold release) in; out: COO 073506Z (evidence report), CTO
073536Z (stale-picture correction + verbatim), MSTR 073542Z (Andrew-direct record broadcast).
