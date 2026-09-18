# Startup, and the one pending TO measured dead: P4-PROMOTE-49F was carried 27 days ago

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, SCRIBE

**Date:** 2026-09-17
**Task Order:** OPAL_ADVIPOINTERS.P4-PROMOTE-49F (measured, NOT executed -- see below)
**Status:** COMPLETE for this session's scope; the TO's disposition is the issuer's call
**Window:** 2026-09-17 ~18:15Z -> ~18:50Z
**Seat:** `0.4.0_DT_ClientPlatform`, site Z, branch SITEZ

---

## Objective

`/watcher`, then the `org/XXX.md` startup protocol, then whatever work the seat actually holds.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-* PATH exercise | XXX.md A.3 two-half check | PASS | `104 of 104` resolve bare; `comp-which` forwarder EXERCISED, not merely resolved. |
| comp-schedule | `comp-schedule --drift` | PASS | 2 gates ARMED (G-3 CTO, G-7 POD4), neither mine. First attempt was DENIED by the rail for piping a census into `tail` -- the tool's own flags are the fix, and the denial was correct. |
| comp-find | `comp-find "PORTAL FREEZE" -i --files` | PASS | 369 hits / 64,893 files; located the 09-14/09-15 freeze records and the 09-16 FREEZE-HONORED message. |
| comp-find | `comp-find "OPAL_ADVIPOINTERS" --band HEAD --files` | PASS | 1,149 hits / 64,895 files, HEAD band = 41; found the project json and DE's P4R-5 handoff deliverable in one call. |
| comp-read | `comp-read portal/scripts/ui-smoke.mjs --enumerate '--(origin\|firm\|...)'` | **PASS -- and it CORRECTED ME** | See "What failed". |
| comp-read | `comp-read portal/src/App.tsx --enumerate 'advisor-intelligence' --limit 20` | PASS | Route at `:98` / `:445`. Tool WARNed that every hit is a substring fragment -- correct, and it is why an anchored probe would have read ZERO. |
| comp-freshness | `comp-freshness artifact s3://.../platinum/advi/49financial/ --raw` | PASS | Newest object 391.6h old, STATUS `RAW` -- **no registered cadence, so the tool refuses a FRESH/STALE verdict.** It declining to guess is the useful part. |
| git ancestry | `merge-base --is-ancestor` x3 + `tag --contains` | PASS | The decisive read. Two different instruments, same answer. |
| ui-smoke.mjs | `--origin https://opalinvest.dev --firm 49financial` | PARTIAL | LAYOUT pass, DATA plane inconclusive by construction -- see the deliverable. |
| to-check.py | `--all --assignee 0.4.0_DT_ClientPlatform` | PASS | 1 active TO of 2,855 faces scanned. `--all` is load-bearing and this TO proves it: the PRD is 30 days old, so the default view would have hidden it. |
| sequence-check.py | `--project OPAL_ADVIPOINTERS` | PASS | `UNPLACED` -- not sequenced, its own directive's rules govern. |

**What worked:** the ancestry walk. `merge-base --is-ancestor` against `origin/PROD` answered the
whole question in three calls, and `tag --contains` corroborated it from a **different** direction
(refs rather than commit graph) -- so the two are corroboration, not repetition (Rule 22
DISCRIMINATION). One of them alone would have been a single instrument on a claim that retires a P1
task order.

**What failed -- my own read, caught by a comp-tool.** I read `ui-smoke.mjs`'s usage header
(`:10-17`), saw `--port` and `--fixtures` and no `--origin`/`--firm`, and concluded the TO named an
invocation the instrument does not accept -- I was about to report that as a finding.
`comp-read --enumerate` printed 38 hits over a 375-line denominator and put `--firm` at `:51` and
`--origin` at `:55` in plain sight. **The usage header is stale relative to the argv parser**, and a
header is a DESCRIPTION while the parser is the STATE (Rule 22 STATE: a description is never a
state). Reading the top of a file is not reading the file. The cost of the tool call was 0.08s; the
cost of the wrong finding would have been a bogus defect report against another seat's script.

**Gap found:** `ui-smoke.mjs`'s usage block at `:10-17` documents 4 of the ~10 flags its parser
accepts. Not filed as a defect -- it is `portal/` and not my lane to edit unasked -- but noted here
because the next reader will make the same mistake I did.

---

## Work Completed

### 1. `/watcher` -- armed clean

Serial was **NOT REGISTERED** at start (the 2026-09-11 session skipped startup at Andrew's explicit
direction and disclosed the hole in its own log). Registered; armed the persistent Monitor at the
resolved prefix; `TaskOutput(begc3bmoa, block=false)` -> `running`, which is the only probe that
observes a CONSUMER. Arm banner reads `parent-tied: pid 3568449` -- armed, not orphan-capable.

`/cygdrive/c` does **not** exist on this box, so the prefix resolved to `/c`. Measured, not assumed;
a wrong prefix arms nothing and returns a task id anyway.

### 2. Startup protocol A -> F

A register / A.1 session-serial file / A.2 audit-archive / A.3 PATH / B.0 delivery ledger / B inbox
both probes / B.1 to-check / C watcher / D owned-paths hook (already wired) / E comp-graph context /
F **zero crons** (this seat's row: `/watcher` once, event-driven).

Inbox empty on both probes, `read/` empty, `get_delivery_state` 0 rows since 2026-08-01 -- reported
as "zero rows MATCHED, not zero delivered", which is the correct framing and I am repeating it rather
than flattening it to "no mail".

A.2 findings: 15, all in the classes `org/XXX.md` says to expect and not chase (the `rv0057-f001`
device-chain migration has not landed, so the tool compares this device's live logs against the other
device's baseline). Two `[COVERAGE/UNCOVERED-AUDIT-LOG]` rows name files
(`commit-msg-ascii-override-audit.log`, `opal-ipblock-audit.log`) other than the one XXX.md lists as
known-and-owned. Surfaced here, not chased, no row filed -- same class, different members, and the
remedy is landing the migration.

### 3. The actual work: the one pending TO is dead, and I measured it rather than executing it

`OPAL_ADVIPOINTERS.P4-PROMOTE-49F` (P1, issued 2026-08-18) orders a portal DEV->PROD promote of DE's
repoint commits. **All three payload commits are already ancestors of `origin/PROD`** -- they landed
in `d9a98bcc` / `portal-v2.1.165` as a rider on the ETFS_POSITIONING promote, and PROD has since moved
to v2.1.179. `origin/PROD..origin/DEV` today is 16 commits / 49 files / +19,822 of unrelated work, so
executing the order literally would be exactly the sweep its own **Do not** clause forbids.

Full measurement, carrier identification, the P4X-4 read and the recommendation:
`org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/OPAL_ADVIPOINTERS.P4-PROMOTE-49F_DISPOSITION_READ_20260917.md`

**I did not flip the TO's `<status>`.** `superseded` is set by the COO or the ISSUER, never the
assignee alone.

### 4. P4X-4 run, because it was the one criterion still carrying something

It was never delivered (no proof-of-spec instance exists) and the TO names it as row-4c close evidence
and a P5-gate input. Ran it against PROD as written. **LAYOUT: PASS** (screenshot READ; silver-canvas
law holds). **DATA: INCONCLUSIVE** -- every region is an empty state, but `ui-smoke.mjs` stubs
`/auth/refresh` with a synthetic session, so against a deployed origin an empty render is equally
consistent with a 401 on a stubbed identity and with genuinely absent data. The instrument cannot
separate them and I did not mint a real bearer, so it is reported as inconclusive rather than as a
defect I cannot support.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Measured the TO instead of executing it | The payload enumeration is the TO's own first gate and its own STOP condition. It failed at the gate. |
| Did not flip `<status>` to `superseded` | Assignee may not set a terminal status; that is the issuer's or COO's act. |
| Ran P4X-4 anyway | Unblocked, read-only, on Opal infrastructure, and the only criterion nothing else had produced (Rule 29: the turn ends when the work does). |
| Reported P4X-4 as INCONCLUSIVE, not FAIL | The stubbed session makes an empty render anti-correlated evidence. A defect claim I cannot discriminate is worse than an honest gap. |
| Did not mint a real bearer to force the discrimination | Outside a startup pass and not mine to do unasked; named as the instrument the re-cut needs. |
| Parked the finding on a carrier rather than messaging the issuer | `2.0.0_SA_COO` and `1.0.0_SA_CTO` are base serials with no live session on this device -- mail there is a silent hole. Relayed via the live integrator instead. |
| Did not chase the 391.6h served-artifact age | DS's surface, already flagged on the project's own `phase` field. Reported, not chased. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/.../deliverables/OPAL_ADVIPOINTERS.P4-PROMOTE-49F_DISPOSITION_READ_20260917.md` | new -- the measurement + recommendation | Yes |
| this log | the record | Yes |
| `org/mcp/sessions/<session>.serial`, `.comp-graph/.agent_context` | startup mechanics | per gate |

No portal source, infra or Terraform file was touched. **Nothing was deployed and nothing was
promoted.** The portal main tree is on `DEV` and was never checked out elsewhere; CWD returned to the
workspace root after the smoke run (it had lingered in `portal/`, which XXX.md Step 1a names as a
defect in itself).

---

## Blockers

None for this seat. One item is PARKED, not blocked: the disposition of P4-PROMOTE-49F needs the
issuer, and the issuer has no live session on this device.

---

## Current State

`0.4.0_DT_ClientPlatform` is LIVE, registered, watcher armed and parent-tied, zero crons, holding
**zero executable task orders**. Its only pending TO is measured dead and parked for its issuer. The
seat is event-driven and available.

---

## Next Steps

1. **[2.0.0_SA_COO / 1.0.0_SA_CTO -- laptop fabric]** Disposition P4-PROMOTE-49F: mark `superseded`
   naming `d9a98bcc` / `portal-v2.1.165`, and decide whether row 4c still needs a P4X-4 re-cut
   against the current bundle with a real bearer.
2. **[0.4.0_DT_ClientPlatform]** Carry `VITE_AUTH_API_URL=` into tracked `portal/.env.development` --
   still RECOMMENDED and still awaiting Andrew's word, carried forward unchanged from the 2026-09-11
   log. One line, reversible, aligns dev with prod.
3. **[0.4.0_DS_ClientPlatform]** `platinum/advi/49financial/` has no registered freshness cadence and
   a 16-day-old newest object behind a page whose footer says "refreshed daily". Surfaced, not chased.

-- `0.4.0_DT_ClientPlatform`, 2026-09-17
