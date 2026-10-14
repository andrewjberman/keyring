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

## AMENDMENT 1 (2.0.0_SA_COO~CA, 2026-10-14 ~03:5xZ): CA-j-1 merged, CA-j-2 cut

CA-j-1 merged @0ca94ce0b6 (worker ~19; `check_j1_mark` 9 of 9, `check_i2_regression` 64 of 64, `check_i13_fresh` 6 of 6, the whole flow-test set 544 of 544). Row W19-S2 (the sibling flow test compared the handler re-sends as exact payloads) was ruled by adding `test_teams_chat_natural.py` to that order's paths (its AMENDMENT 1, commit 53be82a3cd); rows W19-S1, S3, S4, S5, S6 are INERT.
CA-j-2 depends only on the `NAMES.json` row, now merged, so it is cut under workstream `INGRESSTF` (the gate admits a new order in an issued round only with a `<workstream>` element). The issuer amends its own decomposition without a CTO ruling; no gate limb is claimed for this paragraph, and the new order's own commit states the limb that graded it.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-2` | `chat_assist.tf`: the secret shell, the secret in `secret_arns`, the variable and environment key `INGRESS_MARK_MODE` defaulting to `record`; issuer check `r18/checks/check_j2_tf.py` (base 4 of 7, scratch reference 7 of 7) | FWD-7 | WORLD (inferred floor; edit only) | workstream INGRESSTF, slot ~21 | CA-j-1 merged |

`fanout (amendment 1): 1 of 1 chain, cap 8, reason: one file (chat_assist.tf); CA-j-3 and CA-j-5 wait on this merge and on their never-widen halves.`

For CA-j-5 (the flip to enforce): the mark's freshness bound is 15 minutes (`ingress_mark.verify`) and the handler refuses a replayed mark, so the record-mode read must show `unmarked_seen` 0 across a real text AND must look for `stale-mark` refusals from queue delay or redelivery before the flip is asked for.

## AMENDMENT 2 (2.0.0_SA_COO~CA, 2026-10-14 ~04:4xZ): CA-j-2 merged, CA-j-3 staged

CA-j-2 merged @38ce5a7981 (worker ~21; `check_j2_tf` 7 of 7, `check_i4a_tf` green; the first proof instance read INVALID at the worker's final head because its artifact row predated the instance commit, and a fresh worker pinned the row to 6cfb79f314; row W21-S1, the client-data list absent on this box, was measured by hand: no client id in the 130 added lines). The CloudOps seat `0.7.0_AE_CloudOps~CA` is given CA-j-3 as a STAGED order (`<status>staged</status>`, GO written when all three halves are SIGNED on the pin 38ce5a7981).

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-j-3` | DEPLOY in three steps: (1) the secret shell by a targeted apply, (2) its value out of band, (3) one targeted apply of `module.ldo_001` (code, environment `INGRESS_MARK_MODE=record`, the one policy ARN); issuer checks `check_j3_equiv.py` (before; pre-flight read 17 of 17, files=3, foreign=1), `check_j3_live.py` (after), `check_j3_ledger.sh` (NEVER-2) | FWD-7 | WORLD | workstream DEPLOY18, the CloudOps seat | CA-j-1, CA-j-2 merged; halves |

`fanout (amendment 2): 1 of 1 chain, cap 8, reason: one deploy act; CA-j-5 (the flip to enforce) waits on its close and on an observation window.`

## AMENDMENT 3 (2.0.0_SA_COO~CA, 2026-10-14 ~04:4xZ): CA-j-3 GO; two prerequisites carried to CA-j-5

All three halves for CA-j-3 are SIGNED on the pin 38ce5a7981 (CTO @fa9ad4302e, CVO @29f8d9d49f); the order is `pending` with GO. The CVO half names two things the enforce flip (CA-j-5) must settle BEFORE its own pair:
1. The Dell users `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user` can read the mark's key (`simulate-principal-policy`: `secretsmanager:GetSecretValue` ALLOWED), and W10-S2 named the Dell identities among those that can put `sms.reply` on the queue, so in enforce mode the mark does not stop them. CA-j-5 states this limit in the PRD's words, or narrows the key first (a resource policy on the secret denying `GetSecretValue` to every principal except the two function roles).
2. Whether a legitimate text can reach the handler more than 15 minutes after its mark (a mailbox backlog, a retried event) has not been read; in enforce it would be refused `stale-mark`. The record-mode read must look for `stale-mark` refusals.
