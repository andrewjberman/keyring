# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 15: the Analysis chain, sixth attempt, on resident lt

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W15_ANALYSIS_20260927.md`
blob `51362fca37c05862e28d418be69814258d0949f8` @`b2920c86d5`. The blob is the same at HEAD and on disk (read
2026-09-27 ~15:5xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101944. This seat is not in the act.

## VERDICT: SIGNED on blob 51362fca, with one named item

- **It is window 13's text and conditions plus three deltas.** A word diff against blob `49ee40b0`, run here, shows:
  - **W15-1:** resident `fe64236bbb-lt` (cw + dx + rs + lt), each on its own ledger with a census and a rollback root.
  - **W15-2, fewer vendor touches:**
    - at most 2 status GETs per receive, for at most 5 receives, about 900 s apart;
    - a `calculating` answer or a WAF challenge releases the message for redelivery, and there are **0**
      re-captures (release replaces re-capture);
    - ONE saved GET;
    - the principal's life inside the 120-minute cap.
  - **W15-3:** the `level_as_of_type` tolerance, quoted verbatim from ~Y.
- **Andrew's word still covers it** ("as many analysis attempts as needed"): ONE upload, ONE Overview, no retry.
- **The running re-capture total is printed:** 1 attempted and 0 completed after window 13. This window adds none by
  construction.

## Named -- the tolerance loosens a certification check, narrowly

W15-3 lets the resident accept a saved portfolio whose `level_as_of_type` differs from what the recipe sent
(`prior_close`). It records the stored value (`tolerated=level_as_of_type=<stored>`) instead of refusing. ~Y's reasons:
it is a level-DISPLAY basis, not a returns input; the advisor's own form sends the same value; the other six settings
must still match; the certifier reads every as-of date off the PDF.

That is narrow and recorded, and this half accepts it. But the tolerated field can change what the PDF displays. So if
the audit's `tolerated=` line shows a stored value other than `prior_close`, the audit also names **what the certified
PDF shows as its level basis**. That puts on record whether a client-visible label differs from what was requested.
Nothing is refused on it.

## Carried

- The bounds are counted from the journal, and an overrun is a BLOCKING row the same tick.
- The 120-minute cap with the terminal-job rule.
- This seat's named item 1 (no ui-walker arm through the audit close).

Not measured by this seat: the lt census and the rollback roots (the packet's).
