# ANDREW-DIRECT 2026-09-10 ~02:5xZ, at the `1.0.0_SA_CTO` terminal -- VERBATIM

Answering the seven `/open-calls` cards rendered at this terminal 02:35Z. His words, entire:

> "Call 1, yeah try it but make sure no test run hits aj's email, that is not appropriate. 2.) no note for AJ i already messaged him.
> 3.) Sure these are fine but I must provide more clarification. 4.) A lot to cover here, i think we need to talk more before making
> calls 3 and 4. 5.) I'll do it at CVO terminal tonight. 6.) Hold on this. 7.) I'll ask for the push before I sign off."

Recorded 02:5xZ; broadcast the same turn (94909-94913) to `2.0.0_SA_COO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`, `2.0.0_SA_COO~A`,
`4.0.0_SA_CRO` -- sent BEFORE this file was written because ETFS_GUARDRAIL workers were live behind a send path that reaches aj@.

## THE STANDING CONSTRAINT (call 1's second clause, and it is not card-1-scoped)

> "make sure no test run hits aj's email, that is not appropriate"

**NO TEST RUN HITS `aj@opalinvest.com`.** Every project, every seat, every invocation that is not the real scheduled fire.

**The mechanical problem it creates, stated because a constraint without its mechanism is a wish:** ETFS_GUARDRAIL's mailer sends to
the JOINED recipients aj@ AND andrew@ (EG-s-9), and the recipient set is the PRODUCER's, not the invoker's. A test invocation of
`etfs-reports-orchestrator` therefore CANNOT satisfy his word as the code stands. **So: no further test invocation of the monthly
orchestrator, in any mode that can reach `_email_report`, until the send path PROVABLY cannot reach aj@** -- a recipient override
honoured on a test invocation, or no send at all on one, proven by a read of the DEPLOYED handler and not by intent. The CTO's
never-widen half 94775 does not cover a send to aj@ from here on, whatever it said before.

**Nothing is lost by it.** FWD-5 ("Andrew and AJ both receive the monthly report automatically") is ALREADY EXERCISED: the August
re-render delivered to both inboxes at 00:25:59Z, and this seat verified the recipient list in his own mailbox (AJ Graff
aj@opalinvest.com; Andrew Berman andrew@opalinvest.com). The outcome that needed a real joint delivery has one; everything after it
is a test.

## THE SEVEN DISPOSITIONS

| # | call | his word | disposition |
|---|---|---|---|
| 1 | manufacture one hole for the catch-up branch (a served delete) | **"yeah try it"** + the constraint | **APPROVED and UNAFFECTED by the constraint**: the catch-up branch exercises the DAILY producer (`cot-etf-ownership-daily`), which writes a slice and mails nobody. Archive-first, restored by the producer's own catch-up fire, as carded. The delete has his word |
| 2 | (a) leave the September keys (b) a note to AJ | **"no note for AJ i already messaged him"** | (b) CLOSED, he handled it himself. **(a) was NOT ruled on** -- and needs no ruling: nothing is deleted absent his explicit word, so the keys stay by the standing rule rather than by a decision. No act |
| 3 | the five D2 dispositions | **"Sure these are fine but I must provide more clarification"** | **FINE IN PRINCIPLE, HELD** -- his (4) makes the conversation gate BOTH 3 and 4. No re-home, no closure, no register edit on any of the five |
| 4 | the three bifurcation questions | **"we need to talk more before making calls 3 and 4"** | **HELD for the conversation.** Nothing cut; the Investor Reporting L2 stays where it was (behind his transcript) |
| 5 | the sitting + the Codex allocation | **"I'll do it at CVO terminal tonight"** | The SITTING is his, at the `3.0.0_SA_CVO` terminal, tonight -- the CVO runs `/estate-pull` on his go and FWD-4 grades on that record. **The CODEX ALLOCATION (CE-g-4 / FWD-9) was not answered and stays OPEN** |
| 6 | the ADVI_PERFRP distribution restriction | **"Hold on this"** | **HELD.** It stands exactly as written; `4.0.0_SA_CRO` receives nothing on that subject; no seat scopes it |
| 7 | a push window | **"I'll ask for the push before I sign off"** | No push. `0.0.0_AB_MSTR` stays ready and asks nothing |

## Push state
LOCAL on commit; origin/CLOUD @`c6bcb7b12b` (this seat's ls-remote 02:29Z).
