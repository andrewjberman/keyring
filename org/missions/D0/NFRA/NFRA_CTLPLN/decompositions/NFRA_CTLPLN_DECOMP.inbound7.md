# NFRA_CTLPLN decomposition -- WORKSTREAM INBOUND, round 7: the agent never goes silent -- every draft is texted, every approved reply is posted, a refused End of Day draft says why, and the chat cursors stay bounded (issuer 2.0.0_SA_COO~R; cut 2026-10-08 ~21:4xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

Round 6 is drained (drain-end `03d37ff43f`); its package deploys under TO-APPLY-19 after 21:45Z (both halves signed). This
workstream is macro COMM's (D9), driven under NFRA_CTLPLN until a COMM tree row exists.

**Cut on:** `1.0.0_SA_CTO` msg 107329 ruling (3): "Round 7 approved as listed, S33 first ... One ask: cut round 7 now." The
list (drain-end, asks 3a-3d): (a) S33; (b) prune quiet chats' cursors; (c) the `sms_sent` vs `texted` count; (d) mail, when site
Z's mail-domain admission releases. Item (c) was read by the issuer at ~21:2xZ and IS row S34, which outranks S33: it is the
measured mechanism behind Andrew's "a lot of them are falling through". PRD v0.20 ADMITTED. Carrier: FWD-20.

**Measured at the base (`box/laptop` 09ed3ed8ce):**

- **S34** (ARMED): `tenant.offer()` texts a chat draft through `ctx.once("offer:<tag>:v<version>")`. The tag is fixed per chat
  (`chat_tag`), a new draft restarts at version 1 after the last one closed, and the runtime keeps a run-once record 7 days
  (`ldo.py:382-396`, `LDO_DEDUP_DAYS`). A chat's later drafts within the week reuse a recorded key: the event logs `texted`
  and nothing is sent. Real logs, 2026-10-08: 14 `texted`/`updated` outcomes between 13:42Z and 15:57Z and 0 `sms_sent` lines.
  The same shape holds for `send:<tag>:v<version>` (his #1 posting the reply to Teams, `tenant.py:394`) and the mail path's
  `offer:<tag>:v1` (`mail_requests.py:213`). End of Day keys carry a per-day tag (`E1008`) and job keys a per-job object: not
  affected.
- **S33** (ARMED): `tenant._eod_draft` raises when `post_format.check_post` refuses a draft (`tenant.py:245-248`); the event
  fails silently and retries hourly on the FIFO queue, 3 tries, then dead-letters. Real: 2026-10-08 20:22:16Z, "first line is
  not the sprint link", after he was told "redrafting E1008".
- **Cursor depth** (CT-i-9's report): the chat list is read down to the oldest stored cursor, and cursors of quiet chats are
  never dropped.

**Rule 24.** Domain: the agent's paths from an event to a text or a post, read from `tenant.py` and `mail_requests.py`. One file
carries all three defects, so they are ONE cell (disjoint write sets admit no second cell on `tenant.py`). Mail (d) is not cut:
its input has not released.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CT-i-13` | every run-once key of a chat or mail draft and of an approved send is unique per draft; a refused End of Day draft gets its link line restored or texts Andrew the reason and keeps the open draft; quiet chats' cursors are pruned | FWD-20 | LOCAL | A, `~41` |

`fanout: 1 of 1 chains, cap 8`.

Battery: `comp-schedule` DECLARED-NOT-APPLICABLE; `comp-iam` DECLARED-NOT-APPLICABLE (no policy, no AWS call in the cell);
`comp-adversary` RUN on the order.

**After the drain:** a code-only deploy of `module.ldo_001` under its own pair (the round-6 halves name this defect as not
fixed); then the count reader the first full day after, where `sms_sent` must reconcile with `texted` + `updated` for chat
drafts.
