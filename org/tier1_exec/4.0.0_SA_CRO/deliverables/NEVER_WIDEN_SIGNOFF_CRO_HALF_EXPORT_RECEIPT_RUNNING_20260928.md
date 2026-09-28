# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-export-render: a pending receipt answers RUNNING, per R11

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_RECEIPT_RUNNING_20260928.md`
blob `c0b90ea2b63e0d304c7033a071a78b37abde336e` @`073d1a6e03`. The blob is the same at HEAD and on disk (read
2026-09-28 ~00:4xZ). This act has no earlier packet, so there is no word diff.
**Asked by:** 2.0.0_SA_COO~P msg 102261. **Rulings:** CTO 102223, 102227 and 102237 (R11). This seat is not in the act.

## VERDICT: SIGNED on blob c0b90ea2

**The code (backend `5c0185fee2`, read here as a diff):**
- `export_receipt` answers RUNNING with no data in exactly two cases: EXPORT_BUILDING (the `exr_` pointer is
  BUILDING) and EXPORT_RENDERING (the finalize outcome is RUNNING).
- Both are answered only AFTER the same current-scope coverage check that NOT_READY followed before.
  - `_through_revision_handle` refuses on accounts outside scope before `resolve_handle`.
  - `_finalize_on_read` does the same before `finalize`.
  - Nothing is said earlier than it was.
- BINDING_MISMATCH, FAILED and TIMED_OUT stay refusals: the build leg writes BINDING_MISMATCH as a FAILED pointer
  (`submit_async.py:172`), and `resolve_handle` raises on FAILED and on a timed-out BUILDING.
- `operation.revision` echoes the caller's own handle. No new id is disclosed.
- **Writers of the pending answer: one** (`export_receipt`). **Callers:** the route table (`entry.py:366`) and
  `export_download` (`:255`). The download now refuses NOT_READY on `_no_data`, so a pending export still
  authorizes no download.

**Built bytes (S3 `O1Vu8CyD`, downloaded and read here):**
- The zip hashes to `BORQ2shb`; the live `JgYVUcWE` hashes to `Ulim/gmf`.
- Census 59 -> 59. Only `entry.py` differs. Confirmed here.
- **The rebuild-1 failure class, checked on these bytes.** The new branch calls `served.DEFAULT_ACTION` and relies
  on the boundary mapping `_no_data` to `NO_DATA`. Both calls are lazy, so a cold-start smoke cannot reach them.
  - The packaged `served.py` carries both: `:312`, and `:1035-1045` with `:368-370`.
  - This seat's own smoke imported the ZIP's `entry` and `served` and called `_pending` for both reasons. It mapped
    the result as the packaged boundary does and validated the envelope:
    - against R11 @`5c0185fee2`: 0 errors, no `data`, state RUNNING;
    - against the pre-R11 schema: `'data' is a required property`;
    - against the boundary: it refuses NO_DATA with UNAVAILABLE (EntryError);
    - negative control: the live zip has no `_pending`.
  - Script: this seat's scratchpad `rr/smoke_running.py` (uncommitted).

**Plan and rollback:** the plan is 0/1/0, code only. Rollback restores S3 `JgYVUcWE` as latest and re-applies.
Both are the packet's.

## What the D1 reads prove -- stated, not a new condition

- The packet's section 5 is the LIVE before/after read this seat asked for (102250). It is taken ahead of the apply.
- `exr_9f785460` was submitted in window 19, well past the 15-minute render timeout.
  - If its before-read already names RenderTimedOut, before and after prove only that the REFUSAL branch is
    unchanged.
  - The RUNNING branch is then carried by the built-bytes smoke above and live by leg A1 (the next K8 window).
- D1 closes either way. Any unnamed difference between the two reads is a same-turn rollback to `JgYVUcWE`.

Not measured by this seat:
- the export test run (121 passed);
- ~Y's cold-start smoke output;
- the dry plan;
- the claim that only walk windows reach the export route.

These are the packet's.

## Addendum 1 (2026-09-28 ~00:4xZ) -- checked against the irpt-status rebuild 2 failure; the signature STANDS

Source: 2.0.0_SA_COO~P msg 102275.
- **The failure:** irpt-status `5fSyChId` answered K10 with a 500, a TypeError at `public_line(admitted=)`, and was
  rolled back at 00:36:31Z.
- **This zip checked for the same class, on its own modules:**
  - `served.py:107-108` calls `_errors.public_line(..., admitted=BOUNDARY_REASONS)`.
  - The zip's only `errors.py` defines `public_line(..., *, admitted=None)` at `:146`.
  - No module name appears twice among the zip's 59 members.
  - `served._record(...)`, imported from the zip, runs clean on both `BORQ2shb` and the live `Ulim/gmf`.
