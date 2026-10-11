# COMM_ASSIST decomposition -- round 13: the driven FWD-4 mail, the five pinned, channel_poll escalates (issuer 2.0.0_SA_COO~ZZ; cut 2026-10-10 ~23:3xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `1.0.0_SA_CTO~Z`'s round-12 analysis `ledger/ROUND_ANALYSIS.round12.md` @82f10ddf63 (msg 33048). Its enrichment
list is E1 (FWD-4 driven exercise, internal branch), E2 (pin `firm_domains()` to C-MAIL's five) and E3 (Z-S6, `channel_poll`).
PRD v0.3 ADMITTED (`c225bcc74e`; ratified-text SIGNED, brief auto-admitted). FWD-4, FWD-3; C-MAIL.

**Measured at the base (`box/sitez` `a89f5575b1`, ~23:2xZ):**

- `firm_domains()` returns 4 keys (`49financial`, `cottonwood`, `inflection`, `opal`); `alongside` has no measured domain
  (`--check-domains`: `firms=4/5`). A synthetic registry with a sixth client firm returns it (`check_e2_five_pinned.py`: ok=False).
- `considered()` accepts the driven body below as `ok` in both plain-text and Outlook-HTML shapes, and refuses it without the
  name as `body_no_andrew` (`check_e1_body_considered.py`: ok=True). So the predicate is NOT shown defective for a body that
  names Andrew; if the driven mail is refused live, the defect is in what the route serves as the body.
- `channel_mentions.poll()` catches every `GatewayError`, counts it in `failed`, logs no error text, and returns normally, so
  `tenant._safe` never logs `ingress_step_failed` (`check_e3_channel_poll_escalates.py`: ok=False).
- The sending mailbox (the analysis asks the issuer to name it): **`opalbloomberg@opalinvest.com`**, this device's Opal mailbox
  and the gateway identity named in the IRPT intake record. **No seat can send from it today, measured:** the only
  application-credential path in the estate (`irpt/graph/app-registration`, read by
  `infra/aws/lambda/investor-reporting/intake/graph_client.py`) is ABSENT (`describe-secret`: ResourceNotFoundException); the
  gateway's Graph model is DELEGATED per user, and this seat's gateway identity reads `Andrew@opalinvest.com` (whoami), which
  the analysis excludes. Per the analysis, that record is the cell's first act and the row goes to Andrew (row `COMM_ASSIST-Z-S8`).

**Rule 24.** Domain: the analysis's enrichment list, three items, one cell each. Write sets are disjoint: E2 writes
`mail_requests.py`, E3 writes `channel_mentions.py` and its test, E1 writes no code. Values E2 does not move: FWD-4's exercise,
the domain table's `firms=4/5`. Values E3 does not move: whether the gateway serves the channel routes.

| cell | what | serves | risk | chain, slot |
|---|---|---|---|---|
| `CA-e-1` (E1) | ONE mail from `opalbloomberg@opalinvest.com` (or another Opal mailbox Andrew names) to `Andrew@opalinvest.com`, subject `COMM_ASSIST r13 driven test CA-e-1`, body exactly: "Andrew, this is a driven test of your mail assistant (COMM_ASSIST round 13, cell CA-e-1). Please ignore any draft it offers; no reply is needed." The send is BLOCKED on a sending identity (row Z-S8, routed to Andrew). On the send, the issuer's real run grades it: `check_e1_mail_day.py --day <send day>` reads `texted_ok>=1`; the CVO grades the INTERNAL flag on the text he receives; the 10-09 refused mail stands as the negative arm. **No worker order:** the cell has no code to write until the live route refuses the mail. If it refuses as `body_no_andrew`, a fix cell enters this round by amendment, citing the read, writing `mail_requests.py` after `CA-e-2` merges, with its package-and-apply pair | FWD-4 | WORLD (a mail to Andrew) | chain 0 (the issuer and the sender) |
| `CA-e-2` (E2) | Pin `firm_domains()` to C-MAIL's five by party key; the domain table's other behaviour is unchanged | FWD-4 | LOCAL | chain 1, `0.9.0_WK_COMM_ASSIST~6` |
| `CA-e-3` (E3) | `channel_poll` carries the failing call's error in its log line and RAISES after its work is saved, so `ingress_step_failed` fires; read the live failure and rule in writing whether a fix is in COMM's reach, naming the outcome that depends on the step | FWD-3 | LOCAL | chain 2, `0.9.0_WK_COMM_ASSIST~7` |

`fanout: 2 of 2 chains, cap 8, reason: E2 and E3 are independent build cells with disjoint write sets; E1 has no worker chain (its act is a send blocked to Andrew, its grade the issuer's real run).`

**Deploy.** E2 and E3 change the packaged code, so they ship at the next apply of `module.ldo_001`. E2's "done when" names that apply
("at the next apply"); E3's live arm ("one hour reads failed=0") needs it too. Neither cell applies anything. A deploy cell enters
by amendment after both merge, with its never-widen halves measured on the merged, pinned package (round 12's Z-S3 lesson).

Battery: `comp-schedule` DECLARED-NOT-APPLICABLE (no cell schedules anything). `comp-iam` DECLARED-NOT-APPLICABLE (no grant
moves; E1's sender path is the blocked item, recorded, not built). `comp-adversary` on the cut: E2 typing a domain string
(refused: party keys only; the domain-typing arm of `test_inbound_mail_poll.py` stays green); E3 raising before the cursors are
saved (refused: raise after `put_json` and the log line); E3 logging message content in `error` (refused: route, status and code
only); E1 sent from Andrew's own mailbox (excluded by the analysis).

**The issuer's real run at close (not a cell):** E1's read above on the send day, and the FWD-3 full-day read on the round's
last working day.
