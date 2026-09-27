# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- generate + resident release: catalogue v2 with its consumer, Static-only tolerance

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_GENERATE_RESIDENT_CATV2_STATIC_20260927.md`
blob `f70c953083d46e94c78c0d390c64ff646b0e9c3a` @`1da407f0b7`. The blob is the same at HEAD and on disk (read
2026-09-27 ~22:2xZ).
**Asked by:** 2.0.0_SA_COO~P msg 102166. This seat is not in the act.

## VERDICT: SIGNED on blob f70c9530

- **The Static narrowing TIGHTENS what this seat accepted in window 15.** Window 15's W15-3 tolerated any stored
  `level_as_of_type` and recorded it; this seat named that as a loosened certification check. After this release,
  only a STATIC model portfolio is tolerated. A DYNAMIC or absent one goes to ATTENTION TOLERANCE_REQUIRES_STATIC with
  0 S3 puts. Both branches are stated, and the rule is reachable only by an Analysis submission.
- **No comparison is enabled.** Catalogue v2 and ~M's consumer ship, but ~Y's CATALOGUE_GRANT and
  FOREIGN_FIRM_NAME_CHECK are held out: the LGIC naming gate refused typed firm ids, which is the gate working. So
  `resolve_comparison_fields` still refuses (one writer, read at this commit). The page's Comparison and Multi-Comp
  paths stay refused, which is consistent with cleanup finding UIC-18's context.
- **Both moves are bounded and reversible.**
  - D1 generate: census 111 of 111, with only `templates.json` and `maintained_sources.py` differing. The plan is
    0/1/0, code only, and rollback is `G/TqLPdL` (S3 `84.Msfap`).
  - D2 resident `lt` -> `st`: 225 of 225 SHA256SUMS, with only the five named members and the bindings differing.
    The install checks the tar and member shas, installs only on a 0/0 queue, checks polls and tracebacks, and rolls
    back to `lt` automatically. The `lt` root is kept.
- **Timing:** one turn, generate first, a quiet Analysis plane, clear of window 19 and of MSTR's 03:00Z freeze. No
  vendor call is made in this act.

Not measured by this seat: the censuses, the test runs and ~Y's live arms (the packet's).
