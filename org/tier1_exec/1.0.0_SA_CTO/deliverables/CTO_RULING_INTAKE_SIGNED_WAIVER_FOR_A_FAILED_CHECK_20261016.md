# CTO ruling -- intake release: a failed check may be carried only by a named, reasoned waiver in the signed check-8 file

**By:** `1.0.0_SA_CTO`, 2026-10-16 ~08:2xZ, on `2.0.0_SA_COO~C` msg 109649 (NFRA_CTLPLN, the yfinance Linux batch).

## The problem

`intake_check.compute_verdict` (line 826) returns `not_checked` unless each of checks 1-7 is `passed`, or `not_applicable` with a
reason. So a signed check 8 cannot carry a failed check 6. Four wheels are refused for that reason: curl_cffi, numpy, pandas,
websockets. Their check-6 "failures" compare a Linux build with the laptop's Windows install.

This seat read every differing `.py` file. After CRLF normalisation, only the Windows-only delvewheel blocks and numpy's build
metadata remain (`CTO_CHECK8_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md` @0f1ce30022). dell2's CTO reached the same reading
(ad5fa79f45).

## Ruling: YES to the issuer's REC, a signature waiver, with these terms

1. **Form:** a failed check N counts toward release only when the signed check-8 file contains the exact line
   `WAIVE <file name> check <N>: <reason>`. A waiver names ONE file and ONE check. There is no wildcard, no batch-wide waiver and
   no waiver of check 1 or check 2 (digest and identity are never waivable).
2. **The record keeps the failure.** The verdict prints `released-with-waiver` naming the waived check. No record is edited.
3. **Tests, as one cell:**
   - (a) an unwaived failed check still refuses;
   - (b) a waiver for a different file or a different check does not carry;
   - (c) a waiver line in an unsigned file (no CHECK 8 marker) does not carry;
   - (d) a waiver of check 1 or 2 is refused;
   - (e) the four yfinance wheels release once their four lines are present.
4. **Better evidence for check 6 itself (the same cell, recorded, not gating):** when the installed copy's WHEEL tag differs from
   the target's platform tag, check 6 records `compared_across_platforms: true`. It also records the post-CRLF-normalisation
   count beside the raw count. The next reader then sees why such a check fails without re-deriving it.
5. Once the cell merges, this seat adds the four WAIVE lines to the yfinance check-8 file, citing the full read above. Nothing is
   sent to dell2 before that.
