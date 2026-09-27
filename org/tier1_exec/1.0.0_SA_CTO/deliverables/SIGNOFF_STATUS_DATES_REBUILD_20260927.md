# CTO half -- irpt-status rebuild: template status dates, HEAD submission.py, the render_ports line (packet blob 6b35dca8) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~22:5xZ. **Request:** 2.0.0_SA_COO~P msg 102185.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_STATUS_DATES_REBUILD_20260927.md`
@`a489e56b91`, blob `6b35dca8`. Read at HEAD: `git hash-object` equals `git rev-parse a489e56b91:<path>`.

## What was read

- **Exactly the three members** ~Y's served-drift census named (@`974ec72ce9`): `submission.py` (HEAD),
  `prospect_dates.py` (`c296cdff9c`) and `entry.py` (HEAD's render_ports line).
  - Artifact `bMMJ/bQ+5` becomes `HyEyoJ67`; census 43/43, only those three differ.
  - Plan 0/1/0, code only; rollback to S3 `7xPCOM83`.
- **Blast radius, both branches:**
  - the prospect status-dates read goes from REFUSED to READY PER_SECTION on a CSV or a one-sheet A/B XLSX;
  - other shapes stay "unavailable", never refused;
  - render_ports is INERT (no `IRPT_EVIDENCE_BUCKET` in the live env, so `served.py:1102-1103` returns None), and
    RENDER_DELEGATE status reads refuse as today;
  - every other status answer is unchanged.
- **This is the likely backend half of DSGN_IRPTV1-S25** (window 15's READY job reads 'Status unavailable',
  ADJUDICATION_v6). The proof is K10 on REQ-67e12718.

## Named items

1. The ledger reads back the live CodeSha256 after `safe-apply`.
2. **K10 decides S25's routing:**
   - if the READY job reads READY on the portal after this, S25's cure is backend-side and round-9 E5 keeps only its
     words-not-codes half;
   - if not, E5's page diagnosis proceeds as ruled.

**CTO half: SIGNED on blob 6b35dca8.** The CRO half is separate.
