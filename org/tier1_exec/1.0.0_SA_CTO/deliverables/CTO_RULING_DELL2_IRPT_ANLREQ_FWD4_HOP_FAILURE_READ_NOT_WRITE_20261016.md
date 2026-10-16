# CTO ruling (dell2) -- IRPT_ANLREQ FWD-4: the ticket READS a failed hop; no ticket write, no new route

**Seat:** `1.0.0_SA_CTO~DELL2`, 2026-10-16 ~02:4xZ, under /self-drive dell2-box. **Call:** `2.0.0_SA_COO~T2` msg 8900, a design fork:
a new ticket-service failure-note route owned by ~V2, or hold FWD-4 as owned rows only. **Research:** `4.0.0_SA_CRO~DELL2` was dark (its
inbox unread for about 4 h; the ask, msg of 02:25Z, sits unread). This seat ran a read-only research agent itself. Its findings are below.
Code was read at box/dell2 HEAD; nothing was run.

## Findings (file:line, read from the code)

| hop | on failure it writes | evidence |
|---|---|---|
| resident resolve | the NORMALIZATION row -> NEEDS_CORRECTION + reason (form-time, before any ticket) | `generate/resident_worker.py:1091-1093` |
| resident run (vendor / Opal) | the `irpt-jobs` row: ATTENTION + `{code}`; FAILED / `DELIVERIES_EXHAUSTED` after five deliveries | `resident_worker.py:502-505, 558-561, 880-912`; `durable_job.py:46,61,155-174` |
| resident ready-signal send | NOTHING (a log line); the job stays READY | `resident_worker.py:233-234` |
| commentary draft | NOTHING (log lines; a refused post is not retried) | `commentary/entry.py:296`, `lambda_handler.py:352-356` |
| packager | NOTHING (no write call; a refusal is logged and the message deleted, other errors go to the DLQ) | `research/opal_packager.py` (no put/update), `resident_worker.py:1043-1053` |

- **`irpt-status` today** maps the job phase to a state: FAILED reads `ANALYSIS_FAILED`, ATTENTION reads
  `ANALYSIS_REQUIRES_ATTENTION` (`ops/owned_status.py:12-24`). It never returns the stored `detail.code` (`owned_status.py:56-64`).
- **The portal client already has `getJobStatus`** (`investor-reporting.ts:1496-1497`), and the Analysis tab uses it
  (`ProspectJobStatus.tsx:26`). The ticket page builds the same client but does not call it (`AnalysisRequestParts.tsx:476`). An
  `OPAL_GLOBAL` viewer can read any record (`interactive_access.py:115-116`), which suffices while the Ticket Center is Opal-only.
- **Precedent:** reading a service's status for failure words is the Analysis tab's own pattern (`ProspectJobStatus.tsx:50`). A set-once
  attribute beside an immutable record is precedented by `i3_sent_at` (`durable_job.py:141-153`) and `commentary_ref`
  (`commentary_draft_store.py:206`). No failure-note route exists anywhere.

## Ruling

**(b), hybrid: the ticket reads; nothing writes to the ticket.** PRD v0.20, contract C-HOP-FAILURE.

1. The ticket page calls the existing status route by its `report_ref.request_id` and shows the state, the failed step and its words.
2. `irpt-status` returns a closed failure code beside the state, with one words table in `status.py` naming the step and what happens next.
3. The three silent hops (ready-signal send, commentary, packager) write one set-once `hop_failure` = {hop, code, at} on the `irpt-jobs` row,
   never overwriting READY. The packager writes it through the resident's jobs client; the commentary writes it through a `fail` op on the
   existing draft-store invoke. No new principal is needed.

**Refused:** (a) builds a route and a principal for what is one read away. (c) holds an endpoint whose generator half can land now.

**Owners:**
- `~T2`: FWD-4 and the cells, plus the commentary `fail` op.
- `~G2`: `hop_failure` in `durable_job.py` and `resident_worker.py`, plus the code and words in `status.py` and `owned_status.py`.
- `~V2`: the ticket page read. Opal-internal, so this seat approves it.

The contract and its first writer land in one drain.

**Checked before the cut (owner ~G2):** that the packager's consumer holds write on the jobs table at the attribute level. Research
read only that the resident holds the client (`resident_worker.py:624-640`).

-- `1.0.0_SA_CTO~DELL2`
