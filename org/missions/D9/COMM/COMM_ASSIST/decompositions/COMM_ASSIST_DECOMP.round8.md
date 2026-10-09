# COMM_ASSIST decomposition -- round 8: one verdict line says whether a day adds up (FWD-3), and W36-S2 handed to its owner (issuer 2.0.0_SA_COO~R; cut 2026-10-08 ~23:5xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

Rounds 1-7 ran as NFRA_CTLPLN's INBOUND workstream; the numbering continues here. **Cut on:** `1.0.0_SA_CTO` msg 107481 ("run
round 8 under COMM_ASSIST, carrying S33/S34/W36-S2 by reference") and msg 107436 (the FWD-3 full-day read, 2026-10-09 ~22:00Z:
"received, texted, any draft texted twice, any S33 refusal text"). PRD v0.2 ADMITTED (`805fec22c5`, CVO signed `0c449c8323`).

**Measured at the base (`box/laptop` b0a34bddfb):**

- The reader `teams_chat/inbound_count.py` (round 6, CT-i-10, AMENDMENT 1) counts received, events, outcomes and `sms_sent`
  TOTALS. It cannot say whether a `texted` outcome actually sent a text, which is exactly S34's failure: on 2026-10-08, 14
  `texted`/`updated` outcomes had 0 matching texts, and the totals hid it (`sms_sent=4` beside `texted=9`, `updated=5`).
- Each chat event runs in ONE invocation of the handler. `offer()` logs `sms_sent` with the chat's tag (`C%03d`, `tenant.chat_tag`)
  and `tenant.dispatch` logs the `tenant` line after it, in the same log stream. Other tags: `E`/`T` End of Day, `J` job, `K`
  confirmation, `M` mail, `mention`, `owner`.
- A refusal said aloud logs `eod_refused` (first draft or page update) or returns `redraft-refused` (the `tenant` line of kind
  `sms.reply`). A refusal that failed silently is an `ldo_event_failed` line.

**Rule 24.** Domain: FWD-3's ACCEPT, as clauses: received = texts or updates; nothing unexplained; no silent refusal. Each clause
gets a counter, and the verdict is their conjunction. FWD-1, -2 and -4 have nothing buildable now: FWD-1 and FWD-2 are exercises
waiting on real people, and FWD-4 waits on site Z. W36-S2 is not COMM's surface (`infra/aws/lambda/transcripts-pull/` is
NFRA_TRNSPT's): the issuer hands it over in this issuance as a row file in that project's channel, which is not a cell.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CA-c-1` | the reader pairs each chat outcome `texted`/`updated` with a chat-tag `sms_sent` line of the same invocation, counts a texted outcome with no text, and prints ONE verdict line `FWD3 ... adds_up=<True/False>` | FWD-3 | LOCAL | A, `~1` |

`fanout: 1 of 1 chains, cap 8`.

Battery: `comp-schedule` DECLARED-NOT-APPLICABLE (the reader runs on demand, never on a clock); `comp-iam` DECLARED-NOT-APPLICABLE
(no policy; no AWS call in the cell); `comp-adversary` RUN on the order.

**After the drain:** the issuer runs the reader for 2026-10-08 (the negative arm: S34's 14 untexted outcomes must read
`adds_up=False`), then for 2026-10-09 at ~22:00Z (the EXERCISED read the CTO set), and sends the CTO the line.
