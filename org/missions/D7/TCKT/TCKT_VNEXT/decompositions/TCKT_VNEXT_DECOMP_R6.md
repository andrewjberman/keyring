# TCKT_VNEXT decomposition -- ROUND 6, 2026-10-11, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** the CTO's round-6 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_6_20261011.md`
@0b932076f0 (msg 5987), section 3, answering the round-5 slug `ledger/L10_SLUG_R5.md` @d598ca8dae. No PRD addendum. FWD-1 is NOT
REALIZED; the vendor path stays stopped; this is not a thread round, and **no cell of it is a worker build**.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R6-sr-1` | STAGED read: the commentary-draft route's first real call | 1 | FWD-6 | STAGED, NOT RUN | ISSUER | LOCAL (a log read) | -- | `2.0.0_SA_COO~T2`'s report that the drafter's switch is live |
| `R6-sr-2` | STAGED read: the commentary-sent route's first real call | 1 | FWD-6 | STAGED, NOT RUN | ISSUER | LOCAL | -- | a page that calls it, or a staff click, reported |
| `R6-sr-3` | STAGED read: the package door's first real attach | 1 | (C-PACKAGE) | STAGED, NOT RUN | ISSUER | LOCAL | -- | `2.0.0_SA_COO~G2`'s report that the packager is bound |
| `R6-sr-4` | STAGED read: the creator's record by the FORM | 1 | FWD-1 | STAGED, NOT RUN | ISSUER | LOCAL | -- | a real one-step filing reported |
| `R6-fn-1` | FWD-2's live proof by DIRECT INVOKE of the deployed function with constructed contexts: five GETs, no write, no identity, no grant | 2 | FWD-2 | the pair's COO half signed; NOT CUT | ISSUER + applier seat | WORLD (it reads a ticket around the authorizer) | -- | the CTO half; no apply of the function in flight |
| `R6-pg-1` | `commentary_sent` shown on the ticket page | 3 | FWD-6 | PASSED as one line to `2.0.0_SA_COO~Y2`, whose page it is | another project's | -- | -- | that seat's issuance |
| carried | the secret's readers (the laptop's return); run 3's request id; the crawl and the staff notification list (Andrew) | 4 | -- | each on its named event | -- | -- | -- | -- |

**Chains (M = 6):** each staged read is a chain of one; {`R6-fn-1`}; {`R6-pg-1`}. **Fan-out now: 0 workers of 6 chains.** Nothing
here is a build; a staged read is a paragraph until its trigger, and `R6-fn-1` is an applier act under a pair.

## Rule 24 record

- **MECE over the analysis's section 3.** Domain: its four numbered items. By subtraction: 1 -> `R6-sr-1` to `R6-sr-4` (one per
  writer; the mail digest rides whichever read first covers a client notice, stated in the staged file); 2 -> `R6-fn-1`; 3 ->
  `R6-pg-1`; 4 -> the carried line. Nothing of section 3 is uncovered.
- **The domain of "the four writers", falsified before use.** Section 4 of the round-5 slug listed what is applied and
  unexercised: the draft route, the sent route, the mail digest, the package door, and the creator branch's refusals. That is
  FIVE things on FOUR routes plus a log line. The CTO's item says four reads, one per writer: the four are the four ROUTES whose
  admission changed; the digest is a log field with no caller of its own and is placed on the first read that sees a notice.
- **Same grain:** one read per route, one act for FWD-2. **State:** no cell moves the vendor path, and none writes a ticket.

## Where `R6-fn-1` differs from the ruling, stated before the cut

The ruling expects the twin (a client of the ticket's own firm) to be SERVED. Read by this seat in the deployed handler's rule
(`get_ticket`, lines 1233-1244; the matrix admits INTERNAL only for GET): a client of ANY firm is refused by class, so the twin
answers 403 too. The pair (`deliverables/2.0.0_SA_COO~V2/R6_RUN/R6_FN1_DIRECT_INVOKE_PAIR.md`) says so, keeps the twin as its
first arm with 403 expected, and adds a fourth arm (an internal caller with no users row, expected 200, key names only) as the
control that a served answer can be read. The internal firm fence needs a users row to exercise and is left to the tests and to
the runs' census.

## Battery

comp-schedule: DECLARED-NOT-APPLICABLE (no schedule; a staged read is run once by hand on a reported trigger and is NOT a
monitor: nothing polls, alerts or notifies). comp-iam: `R6-fn-1` reads who may invoke the function (its resource policy and this
box's own simulate) and adds no grant. comp-adversary: `R6-fn-1` IS the adversarial act.
