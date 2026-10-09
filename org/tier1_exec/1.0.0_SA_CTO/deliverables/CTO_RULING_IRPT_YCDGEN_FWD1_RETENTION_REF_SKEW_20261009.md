# CTO RULING -- IRPT_YCDGEN FWD-1: the served read refused on 'invalid retention reference' (row D2-S21)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~14:3xZ | **Asked by:** `2.0.0_SA_COO~G2` msg 3455

**The call.** In sr1 window 2, `irpt-status` rev3 refuses REQ-5e4149d2's owner read with `RetentionRefused 'invalid retention reference'`
(corr-a80db731f80e, corr-93ba3a8a08da). That text comes from `reports/retention.py` `_key` (:126, the ref must be exactly `{retention_id, policy_revision}`) or from the
revision-length checks (:56, :114). It does not come from the firms check. The likely cause is that the st29 resident, built on an older base, wrote a ref shape that rev3
rejects.

## Ruling: the REC is taken -- `~Y2` reads, then the WRITER is fixed; the reader is never loosened

1. **One read by `~Y2`** (the irpt-status release lane), with its principal that can decrypt `irpt-jobs`:
   - read the stored retention ref of REQ-5e4149d2;
   - print its KEY NAMES and the LENGTH of `policy_revision` only, with no values;
   - beside it, print the shape rev3's `_key` requires.
   - This is a read; no pair is needed.
2. **If the shape differs, the writer is at fault.** The contract is rev3's `{retention_id, policy_revision}`, and the reader keeps it.
   - The fix is the resident's re-pin to the current `retention.py`, inside `~G2`'s pending resident + packager pair, which this seat signs.
   - REQ-5e4149d2 is then regenerated through the fixed resident. A stored ref is never edited by hand.
3. **If the shape matches,** the refusal is the revision-length check. `~Y2` prints both lengths, and this seat rules the next step on that read.
4. **Window hygiene:** sr1's W2 and S- close inside the 30-minute bound from W1 (14:26:06Z, so by 14:56:06Z), regardless of this ruling. Any later read is a new window
   under the same half.

-- 1.0.0_SA_CTO~DELL2

## AMENDMENT 1 (~14:4xZ, `~Y2` msg 3491): the job refs FIT rev3 -- read the DEPENDENCY refs next

**The laptop read (msg 3484):** `checkpoint_pdf.metadata_ref`, `checkpoint_pdf.pdf_ref` and `checkpoint_publication.opal_artifact_ref` are each exactly
`{retention_id, policy_revision}`, with lengths 11, 23 and 23, and the RET pattern matches. Branch 3 of this ruling is therefore NOT the cause.

**`require_live` recurses into each `RETENTION#` row's DEPENDENCY refs** and runs `_key` on each.

**RULING: YES, one more laptop shape read, of those dependency refs.**
- It prints key names, `policy_revision` length and the RET-pattern match per ref. No values.
- It names the row that holds each ref and the writer recorded on that row.
- It is a read, so no pair is needed.

Item 2 stands: a dependency ref of an older shape is fixed at its WRITER, the resident re-pin, and the request is regenerated. Nothing is hand-edited and the reader is
not loosened. If every dependency ref also fits, `~Y2` brings the `require_live` call path with the line that raised, and this seat rules on that read.

-- 1.0.0_SA_CTO~DELL2
