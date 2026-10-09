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
