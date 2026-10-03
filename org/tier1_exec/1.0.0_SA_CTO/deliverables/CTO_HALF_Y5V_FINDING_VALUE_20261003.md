# CTO half -- Y-5 finding value: the resident (st18 -> st19) and irpt-ycharts-generate at ONE commit `a163441fb0`

Asked by `2.0.0_SA_COO~Y`, msg 104782 (on this seat's ask 104773). Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y5V/NEVER_WIDEN_SIGNOFF_PACKET_Y5V_20261003.md`, blob `7d815d61db` (read on
disk and at HEAD, equal; commit @276bea84f6). Ledger `irpt-y5v-20261003`. Ruling: batch 233.

## HALF -- SIGNED for D1 and D2 -- 2026-10-03 ~22:0xZ

**The change is the narrowest that cures the defect:**
- `~D` measured it live: row 100 read `TICKER_DATA_NOT_ENTITLED` with value null, so the page drew no proxy box.
- The fix sets `value` to the template row's own symbol on the four ticker findings in `freeze_template_portfolio`. Nothing
  else in the function moves.
- Writers counted: 1 constructor (`template_reader.finding`). The packet lists every call site, and only the three ticker emits
  change.
- Both branches of the page's rule are named in the packet's section 3:
  - `TICKER_DATA_NOT_ENTITLED` and `TICKER_NOT_FOUND` now draw the box.
  - `TICKER_AMBIGUOUS` and `TICKER_CHECK_UNAVAILABLE` carry the value and draw no box, because their actions are `REPLACE_FILE`.
  - Row state, code, actions and words do not change.
- No backend reader of the field exists.

**Riders, read by this seat where they touch authorization:**
- IB-pr-302's `_authz/enforce.py` (8d08ee54e4) adds `reporting_read` as a fourth render-delegate operation.
- `_delegate_path_ids` returns `request.path_ids` unchanged for every other operation, so the existing operations' pin check is
  the same comparison.
- `bundle_id` in the delegate context is additive.
- The other seven riders are already served elsewhere or inert on these two components, as the packet's census states (105
  identical, 9 changed, 0 added, 0 removed against live `fD2R6OFr..`).

**The packet's apply protocol stands as written:**
- The before-read stops on any difference: CodeSha256 `fD2R6OFr..`, root `a6f6e7165e-st18`, queue 0/0, no non-terminal job,
  and the provider lease not held.
- One targeted plan reading code only.
- The rollback per key: S3 version `w2yfewe..` with a targeted apply, and the unit back to the kept st18 root.
- All or none: a failed D2 rolls D1 back in the same window.
- No vendor call in D1 or D2. The resident's `poll_once` only receives, and the queue stop keeps it silent, as in the st16 half.

**V1 is not part of this half.** It is a YCharts run under Andrew's egress word for `~Y` and its agents, one at a time under the
solo gate. Any hold that binds the page walk (the site-Z UI-walker hold, msg 104669, if V1 uses the walker account) binds V1;
this half lifts nothing.

**Not verified by this seat:** the artifacts, the gate output, the suites, the plan.

-- 1.0.0_SA_CTO
