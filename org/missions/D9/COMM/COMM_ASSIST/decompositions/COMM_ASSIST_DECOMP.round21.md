# COMM_ASSIST decomposition -- round 21: the channel poller reads replies in older threads (issuer 2.0.0_SA_COO~CA, laptop; cut 2026-10-16 ~20:4xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO`'s ruling on call `laptop-20261016T195534Z-446a`,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_446A_COMM_ASSIST_TEAMS_THREAD_REPLY_MENTIONS_20261016.md` @f418537712
(msg 109753): ruled (a), fix it -- "one cell: the reader also reads replies on threads with recent activity, bounded to the 8
watched channels; then one retest: a real @mention as a reply inside an older thread is caught and alerted." PRD v0.10
(ratified-text half SIGNED, current). This ruling stands in for a round-20 enrichment item: the round-20 analysis
(@96694ae78e) parked the project with CA-k-5 named.

**What surfaced it.** Muse's alert exercise (CA-k-5) ran on 2026-10-16 off the repository, on Andrew's word (that exercise only;
the ruling above says this fix is ordinary repo work). Its mail half passed on Andrew's report. Its Teams half did not reach muse:
Alyssa Keith's real @mention in a watched channel was never seen by the assistant. The ingress `channel_poll` lines 12:00Z to
18:5xZ: 419 polls, `channels=8`, `mentions=0`. A gateway read of all 8 channels showed no new top-level post since 2026-10-14.
The poller reads the newest pages of top-level posts with their embedded replies and stops at the first page with nothing newer
than its cursor, so a reply under an older post is never read. The End of Day Updates channel keeps ONE parent post
(`assist.EOD_PARENT_ID`, 2026-08-07) that everyone replies under, so the most-used thread is exactly the one never read.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-n-1` | `channel_mentions.py` also reads, through the gateway's replies route, the replies of a bounded set of threads per channel (the pinned End of Day parent, and every post with activity in the last 14 days, at most 10 per channel), inside the existing per-poll call budget; one event per new reply that @mentions Andrew; the existing test's fake gateway gains a `replies` method | FWD-3, FWD-13 | LOCAL (code and tests; deploys nothing) | chain 0, workstream THREADREPLIES, slot ~32 | none |
| `CA-n-2` | DEPLOY of CA-n-1 (a targeted apply of `module.ldo_001`, code only), its own never-widen set; to the COMM macro CloudOps lane (CLAUDE.md rule 34) | FWD-3, FWD-13 | WORLD | the COMM CloudOps lane | CA-n-1 merged; halves |
| `CA-n-3` | the retest: one real @mention of Andrew posted as a REPLY inside an older thread of a watched channel is recorded (`mentions.json`) and reaches Andrew as a muse alert within 30 minutes | FWD-3, FWD-13 | SERVED | needs a person's post | CA-n-2 live; a colleague's reply |

`fanout: 1 of 1 chains, cap 8, reason: one code cell (CA-n-1, two files: channel_mentions.py and its test); CA-n-2 is cut at its merge as a WORLD act with its own halves; CA-n-3 needs a person's post after CA-n-2 is live.`

**Rule 24.** Domain: the ruling's two items (denominator 2). Item 1 (the fix) is CA-n-1 and its deploy CA-n-2; item 2 (the retest)
is CA-n-3. None uncovered.

**Issuer check (written first; each finds the repository from the current directory's git toplevel; seam `N1_ROOT`):**
`CA-n-1` -> `deliverables/2.0.0_SA_COO~CA/r21/checks/check_n1_threads.py` (`N1-THREADS`): base 1 of 7 (only `budget` passes); a
scratch reference implementation (65 added lines, removed afterwards) reads 7 of 7, and with the one test edit named in the order
`test_inbound_channel_mentions.py` reads 7 of 7 and 4 of 4 against that reference. Without that edit the existing test fails on
the reference (its fake gateway has no `replies` method, and its budget arm counts every call as a page read).

**The issuer's real run at close:** after CA-n-2, the live `channel_poll` lines carry reply reads within the call budget, and the
CA-n-3 retest is the outcome's real run.
