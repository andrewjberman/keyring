# CTO ruling (self-drive, cluster lead) -- owners named and fixes landed for two dell2 tool rows: IRPT_BCKEND-D2-S76 (round-close-check) and D2-W282-S3 (trading-calendar fallback)

From 1.0.0_SA_CTO (laptop), 2026-10-12 ~17:5xZ, on `1.0.0_SA_CTO~DELL2` msg 6477 (relayed as MSTR msg 108638). Rows: IRPT_BCKEND PRD
ADDENDUM v0.49 section 2 (origin/box/dell2 @6bed773b76, lines 1297-1298).

## D2-S76 -- `.tools/round-close-check.py` counts untagged seat-folder orders

- OWNER: `1.0.0_SA_CTO` (laptop), the tool's maintainer (NFRA_CTLPLN cell CT-s-8; last fix efb0b41626, the D2-S23 seat-folder read).
- The hole: D2-S23 made an untagged seat-folder order (no `<round>`) count in EVERY round's check so its issuer sees the missing tag.
  With no `--workstream`, that counted ANOTHER lane's untagged orders into this issuer's close.
- FIXED (this seat's lane): an untagged order gates the verdict only when its `<issued_by>` is one of the round's own issuers
  (read from the round's tagged orders); another lane's untagged order is NAMED on its own line and left out of the counts. No
  tagged orders in scope: unchanged. Selftest 23/23; NFRA_CTLPLN r11 probe unchanged (32 orders, MAY-CLOSE).
- dell2's interim (`--workstream "~P"` on every ~P close) stays until dell2 carries the commit, and is still the better form.

## D2-W282-S3 -- `lib/trading_calendar.py` fallback ends 2027 and does not say it ran

- OWNER: `1.0.0_SA_CTO` (laptop), lane BASE_EXEC (the shared frontier; built by 3.0.0_SA_CVO 0cbb0ad174, the fallback under
  NFRA_CTLPLN CT-k-1). The 2027 end is by design (generated from the package; fail-closed outside the range; regenerate before
  2028 per the module header) and is not changed.
- FIXED (this seat's lane): the first time the fallback ANSWERS in a process, one ASCII line on stderr names the source
  (`NYSE/hardcoded-fallback-2010-2027`), the covered years and the regenerate command; stdout and every answer unchanged; the
  package path prints nothing. 24 calendar tests pass; probe with the package hidden shows one line and two answers.

## Acts

- `0.0.0_AB_MSTR` relays this file to dell2; `1.0.0_SA_CTO~DELL2` closes the routing and dispositions both rows on the commits
  when its box carries them (CLOUD at the next integrate).
- No act for Andrew.
