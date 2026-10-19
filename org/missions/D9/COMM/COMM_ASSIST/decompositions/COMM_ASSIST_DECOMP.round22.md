# COMM_ASSIST decomposition -- round 22: the mail handler never drafts for mail Andrew sent (issuer 2.0.0_SA_COO~CA, laptop; cut 2026-10-19 ~16:5xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** Andrew's word to this seat, 2026-10-19 ~16:26Z, VERBATIM: "yes that rule is approved for #1" (record
`org/tier1_exec/2.0.0_SA_COO~CA/ANDREW_DIRECT_20261019_162xZ_MUSE_NO_SELF_DRAFT_RULE_APPROVED_AND_CALL_2396_WAIT_NATURAL.md`
@8eb8c7408a), and `1.0.0_SA_CTO`'s go, msg 109839 ("Go on the rule and the three discards"; seat ask msg 109835; carried frames
109833 and 109834 from muse). PRD v0.10 (ratified-text half SIGNED, current). This stands in for a round-N enrichment item.

**What surfaced it.** Muse reported two drafts, M741 and M044, made on mail Andrew himself sent (and eight earlier drafts addressed to
him). Live read 2026-10-19 ~16:4xZ of the state table (1,255 rows scanned): objects `mail:...` carry `mail_log` rows
`{"from": "Andrew Berman", "domain": "opalinvest.com", "firm": "opal", "subject": "Re: Fidelity Pipelines", "tag": "M741"}` (considered
15:23Z) and M044 (15:31Z). The cause is in `mail_requests.considered`: a message is considered when its sender's domain is one of the
five parties' (Opal's own domain is one) and its body names "Andrew"; nothing excludes Andrew's own mailbox, and his reply chains name
him. `a.me()` (the cached `/me`) already holds his mailbox: keys `display_name`, `id`, `mail`.

**The three discards (C495, C608, C533): NO ACT OWED.** Live read, same scan: the three chat objects (`C533`, `C608`, `C495`) each
carry `pending: None` (updated 15:53Z, 15:53Z, 16:14Z today). The reader folder on dell2 is a copy refreshed on a schedule; its "texted"
rows are older than the state. Nothing is discarded by this seat; the state is the authority. ms is told so by evidence, not by an act.

**The thread half of the rule.** "If a thread's latest message is from Andrew, no draft": for a Teams chat this already holds
(`tenant.on_chat_messages` drafts only when `a.unanswered(...)` is non-empty, and clears a pending as `answered-by-hand` when he
answers). For mail it cannot be built inside the handler: each mail arrives as its own event on its own object
(`mail:<message id>`, one message), so there is no thread in the batch to read the latest message from, and a thread read would be a
new gateway call (a different cell, not asked). Stated here as the limit; Andrew's own sent mail, the case muse reported, is covered.

| cell | what | serves | risk | chain, slot | depends_on |
|---|---|---|---|---|---|
| `CA-p-1` | `mail_requests.py`: `considered` takes the set of Andrew's addresses and refuses a message whose sender is one, reason `from_andrew`, before the domain and body tests; `on_mail_messages` reads the set once from `a.me()["mail"]` and RAISES when it is unknown (the event retries, nothing is drafted); `from_andrew` joins `REASONS`; three mail tests gain the one-line `a.me` stand-in and one counts literal gains the new key | FWD-2 | LOCAL (code and tests; deploys nothing) | chain 0, workstream SELFMAIL, slot ~33 | none |
| `CA-p-2` | DEPLOY of CA-p-1 (a targeted apply of `module.ldo_001`, code only), its own never-widen set; to the COMM macro CloudOps lane (CLAUDE.md rule 34) | FWD-2 | WORLD | the COMM CloudOps lane | CA-p-1 merged; halves |

`fanout: 1 of 1 chains, cap 8, reason: one code cell (CA-p-1: mail_requests.py plus four test edits); CA-p-2 is cut at its merge as a WORLD act with its own halves.`

**Rule 24.** Domain: the approved rule's two clauses and the discards request (denominator 3 items: sender-is-Andrew, thread-latest-is-Andrew,
discard three drafts). Item 1 is CA-p-1 and its deploy CA-p-2. Item 2: Teams chat already holds (cited above); mail cannot be built in the
handler (cited above), reported to the CTO as a limit, not silently dropped. Item 3: already true in the state (live read above), no cell.

**Issuer check (written first; each finds the repository from the current directory's git toplevel; seam `P1_ROOT`):**
`CA-p-1` -> `deliverables/2.0.0_SA_COO~CA/r22/checks/check_p1_self_mail.py` (`P1-SELFMAIL`): base 1 of 6 (only the difference control
passes); a scratch reference implementation (a 14-line change) reads 6 of 6. The four existing mail tests: base 17/17, 15/15, 22/22, 8/8;
against the reference without the test edits they read 16/17, 14/15, 4/22, 8/8; with the edits (the `a.me` stand-in in the three, the
`"from_andrew": 0` key in one counts literal) 17/17, 15/15, 22/22, 8/8 (the draft test's base-pin arm needs a git checkout, so it ran
16/17 in the non-git scratch only).

**The issuer's real run at close:** after CA-p-2, a mail from Andrew's own mailbox that names him is read by the live handler and
`mail_considered` carries `from_andrew=1` with no `sms_sent` for it; a colleague's mail still texts (the live read of the mail poll).
