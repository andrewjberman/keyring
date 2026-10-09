# COMM_ASSIST decomposition -- round 10: a measure for FWD-2 -- how often Andrew sends a draft as written (issuer 2.0.0_SA_COO~R; cut 2026-10-09 ~01:2xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO` msg 107513 (drive every track the full-day read does not gate) and Andrew's ~00:0xZ word (an empty
tick runs `/next-calls` and proceeds). PRD v0.2 ADMITTED (`805fec22c5`). FWD-2 ACCEPT: "the drafts he is texted are written from
one collection of his own messages, sorted by the kind of thing he is doing, and he sends them with few or no changes". DONE
WHEN: "drafts written from his own past messages, read by him".

**Measured at the base (`box/laptop` 876b014ddc):** the first half of the ACCEPT is live (readiness read in `STATUS.md`:
`teams_reply` drafts read the voice file and the examples object). The second half has no instrument. Every reply he makes is
already logged: `tenant` lines of kind `sms.reply` with results such as `sent` (his 1 on a chat draft), `redrafted` (notes),
`dropped`/`cancelled` (0), `posted`/`approved` (End of Day). Since 2026-10-08 21:48Z each `tenant` line carries the object's hash,
so the lines of one draft (texted, redrafted k times, sent or dropped) can be joined.

**Rule 24.** Domain: FWD-2's "with few or no changes", read as: of the chat drafts he sent, how many he sent as first written (0
redrafts). One counter family over lines already written: one cell. It changes only the reader, which runs on the laptop: no
deploy.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CA-v-1` | the reader joins each chat draft's lines by object hash and prints one `FWD2` line: drafts offered, sent, sent as first written, sent after k redrafts, dropped, answered by hand | FWD-2 | LOCAL | A, `~4` |

`fanout: 1 of 1 chains, cap 8`.

Battery: `comp-schedule` DECLARED-NOT-APPLICABLE; `comp-iam` DECLARED-NOT-APPLICABLE (no policy, no AWS call); `comp-adversary`
RUN on the order.

**After the drain:** the issuer runs the reader for 2026-10-09 with the FWD-3 read, about 22:00Z, and the `FWD2` line goes to the
CTO beside it.
