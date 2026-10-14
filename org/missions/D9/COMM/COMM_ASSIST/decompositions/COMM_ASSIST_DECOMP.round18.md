# COMM_ASSIST decomposition -- round 18: the ingress mark, and one sitting for Andrew (issuer 2.0.0_SA_COO~CA, laptop; cut 2026-10-14 ~03:0xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO`'s round-17 analysis `ledger/ROUND_ANALYSIS.round17.md` (msg 109054), over PRD v0.7 (the ratified-text half SIGNED by `3.0.0_SA_CVO~L`, current by ENDPOINT hash). The CVO's L10 slug `REMEDIATION_v4.md` @bd4d7b90e4 (watermark 02:45Z) closed round 17:
14 of 14 orders complete, three rows graduate, one ARMED (`W10-S2`).

**Direction (binding):** muse replaces the Kimi text agent as Andrew's interface; the text path stays the fallback. Whether Kimi also stops drafting is held at Andrew (`87a2`).

**The analysis's five items and what the issuer does with each.**

1. `W10-S2` the SMS ingress mark (P1, a WORLD deploy under its own pair) -> cells CA-j-1, CA-j-2, CA-j-3, CA-j-5 below.
2. FWD-6 and `W18-S2` as ONE Andrew sitting -> not a cell: it is Andrew's act. The issuer rewrites the open call (`8fb2` and `cd2d` close as superseded by one new call) and the card (`r18/MUSE_SITTING_CARD.md`). The sitting needs a draft Andrew is content to drop.
3. J290's first real use, then the OPLGTW draft route -> Andrew's act (carried open call) and MSTR's, not a cell.
4. The agentbus read (no `unstamped sender=LDO-001` since CA-i-4) -> not a cell: the issuer asks `0.0.0_AB_MSTR` to read every box's consumer log and reads the laptop's own.
5. ONE batch cell: `D2-S1` (the forwarder creates `answers/` and its subfolders) -> CA-j-4.

**Why W10-S2 is five cells, not one.** The producers of the two text-driven kinds (`sms.reply`, `owner.text`) are FOUR sites in `tenant.py`: the ingress (`_route_commands`: one for `owner.text`, one for `sms.reply`) and the handler's own re-sends (`on_owner_text`, two `ctx.send` of `sms.reply`).
A mark that covers only the ingress would make the handler's own re-sends look forged, so all four are stamped together. A mark that is enforced the moment it is deployed would drop any text already in flight from the old ingress, so the rollout has a mode: `off`, `record` (check and count, act anyway), `enforce` (refuse).
The mark is an HMAC-SHA256 over the object id, the kind, the mark time and the canonical payload, keyed by a secret that only the assistant's two functions can read; an identity that can write to the queue but not read the secret cannot forge it, and reading the secret is a logged management event (the CTO's stated limit).

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-1` | `ingress_mark.py` (stamp, verify), the `dispatch` gate with the three modes, the four producer sites stamped, the `NAMES.json` row `secrets.ingress_mark`, tests | FWD-7 (every answer in his name) | LOCAL | chain 0, slot ~19 | none |
| `CA-j-4` | the forwarder creates `answers/`, `answers/done/`, `answers/rejected/` when absent (seat row D2-S1) | FWD-7, FWD-8 | LOCAL, DIRECT-ACT | chain 1, slot ~20 | none |
| `CA-j-2` | `chat_assist.tf`: the secret resource, the secret in `secret_arns`, the variable and environment key `INGRESS_MARK_MODE` defaulting to `record` | FWD-7 | WORLD (inferred floor; edit only) | after CA-j-1 | CA-j-1 merged |
| `CA-j-3` | DEPLOY 1: the targeted apply of `module.ldo_001` (code, the new secret, the environment key), and the secret's VALUE put out of band; never-widen set | FWD-7 | WORLD | the CloudOps seat | CA-j-1, CA-j-2 merged; halves |
| `CA-j-5` | DEPLOY 2: the variable's default flips `record` -> `enforce` (an environment-only change), after the record-mode read shows no unmarked legitimate event | FWD-7 | WORLD | the CloudOps seat | CA-j-3 closed; a stated observation window; halves |
| `CA-j-6` | FWD-12, muse's efficacy against the text path | FWD-12 | LOCAL / SERVED | next round | FWD-6 read (Andrew's sitting) |

`fanout: 2 of 2 chains, cap 8, reason: CA-j-1 writes tenant.py, ingress_mark.py, NAMES.json and tests; CA-j-4 writes forwarder.py; they share nothing. CA-j-2 waits on CA-j-1's NAMES.json row (Terraform reads it at plan time) and the deploys wait on both.`

**Rule 24.** Domain: the analysis's enrichment items 1 to 5. Uncovered member by subtraction from the printed denominator (5 items): item 1 is CA-j-1, 2, 3, 5; item 2 is Andrew's sitting; item 3 Andrew's act; item 4 the read; item 5 CA-j-4. None uncovered.

**The issuer's real runs at close:** the live `check_j3_live` and `check_j5_live` reads after each apply; one real text from Andrew's phone routed through the ingress and visible as a marked event with `unmarked_seen` still 0 in record mode (read from the state row, never from content); a forged `sms.reply` put on the queue by the issuer in enforce mode refused and recorded.
