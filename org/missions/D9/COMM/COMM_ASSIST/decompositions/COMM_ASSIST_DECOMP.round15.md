# COMM_ASSIST decomposition -- round 15: D2 as a read, on un-park condition 1 (issuer 2.0.0_SA_COO~ZZ; cut 2026-10-11 ~19:2xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO~Z`'s round-14 analysis `ledger/ROUND_ANALYSIS.round14.md` @7aeb5a42e4. The project PARKED with three
un-park conditions. **Condition 1 fired:** NFRA_OPLGTW `TO-OG-ap-7` released CT-i-11, and the gateway now serves `/hx/teams/teams`.
That condition's cell is "ONE read cell, D2". PRD v0.4 ADMITTED. FWD-3.

**Measured at the base (`box/sitez`, ~19:1xZ), read from the live logs:**

- `channel_poll` flipped from `failed=1` (`route=teams status=404`) to `failed=0` between 18:48:50Z and 18:49:22Z. Since then it
  lists 8 channels, reads up to 7 a poll, and fails 0 times. 0 channel mentions so far.
- `r15/checks/d2_channel_read.py` at 19:19Z: HOUR `channel_poll=59 failed>0=29` (the pre-flip half of the window) ok=False;
  TEXTED `channel_mention_events=0` ok=False -> FAIL as expected. Control: `--minutes 120` reads `failed>0=89`, so the arm
  discriminates by window.
- **The mention arm cannot be driven by a seat:** the gateway's `send_channel_message` (`infra/aws/ec2/opal-gateway/app/tools.py`
  :1337-1353) posts HTML with no `mentions` array. `channel_mentions._mentions_me` counts only a mention entity carrying Andrew's
  user id, and it skips his own posts. So one colleague typing an @mention of him in any of the 8 channels is the driven act. It is
  a human act, asked of Andrew together with E1's held email.

**Rule 24.** Domain: condition 1's cell, one item. It is a read with no code and no write surface, so no worker order. Z-S9 (the
import-test shadowing) is meant to ride the first cell cut as a batch repair. It is a defect in the COO half's text, not in code,
and this cell has no deploy half to repair. So it is carried to the next deploy half, which will run its import test from a
directory holding no `data/`, and not cut here.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CA-g-1` (D2) | The issuer reads `r15/checks/d2_channel_read.py`: an hour of `channel_poll` with 0 failures (passes at ~19:50Z), and at least one `teams.channel_mention` event texted (needs one real channel @mention of Andrew). PASS closes FWD-3's channel coverage and rows Z-S6, Z-W7-S1, Z-S10, Z-S11 | FWD-3 | LOCAL (a read) | chain 0 (the issuer) |

`fanout: 0 of 1 chains, cap 8, reason: one read cell, run by the issuer; no code, so no worker.`

**The issuer's real run at close:** that read. Then the FWD-3 full-day read, which closes S1 (S2 at r29's read-back), per the
round-14 analysis.
