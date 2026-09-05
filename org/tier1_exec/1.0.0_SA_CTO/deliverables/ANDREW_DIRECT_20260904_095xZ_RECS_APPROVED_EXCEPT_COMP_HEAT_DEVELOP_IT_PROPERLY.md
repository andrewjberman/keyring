# ANDREW-DIRECT 2026-09-04 ~09:5xZ at the 1.0.0_SA_CTO terminal -- "recs approved except comp-heat, i want comp-heat to be figured out and developed properly"

**Verbatim, in full:** `/open-calls` (the skill, run at this seat) -> the four cards below -> **"recs approved except comp-heat, i want
comp-heat to be figured out and developed properly"**.

Recorded by `1.0.0_SA_CTO` the same turn; broadcast the same turn to `0.0.0_AB_MSTR`, `2.0.0_SA_COO`, `2.0.0_SA_COO~A`,
`3.0.0_SA_CVO`, `4.0.0_SA_CRO`. **Push state at record time, MEASURED this turn:** LOCAL; HEAD `bd1ae5cfbd`; origin/CLOUD
`@351f309e0a` (`git ls-remote origin CLOUD`, 09:5xZ); **278 commits local ahead of that tip.**

## The frame he answered, verbatim

```
OPEN CALLS AT ANDREW -- 1.0.0_SA_CTO (4 calls, 2026-09-04 09:5xZ)

BLOCKING (something waits on the word)

+-- CALL 1 of 4 ---------------------------------------------------+
  **Relaunch ONE Codex seat -- yes/no?**
  It is the single instrument that closes two things: CE-g-4's rail
  exercise (FWD-9's NOT_EVALUATED grade on COMPEFFICACY's close) and
  CLDGRPH-S26's gate, on a provisioner that now leaves 0 of 211 files
  protected @e4167f3c3b. Your 2026-09-03 ~21:0xZ word reaped all 19.
  --------------------------------------------------------------------
  **REC -- yes, one seat, reaped again after.** Two exercises, one
  seat, both blocked on nothing else; MSTR spawns it on your word and
  the CVO and this seat read the two results.
+---------------------------------------------------------------------+

+-- CALL 2 of 4 ---------------------------------------------------+
  **Open a push window -- yes/no?**
  Every commit of tonight is LOCAL against origin/CLOUD @351f309e0a:
  spine v3.2-v3.6, eight v3 carriers, five drain-gap fixes, both
  projects' analyses and COMPEFFICACY's close. LD-0522 reserves the
  push to MSTR on your word; FWD-9's "on the shared branch" limb is
  one of the four grades that cannot read REALIZED until it happens.
  --------------------------------------------------------------------
  **REC -- yes, one window at MSTR now.** Nothing here is half-landed
  and the estate's law is currently readable on one machine only; the
  longer the window waits the larger the integration it becomes.
+---------------------------------------------------------------------+

CARRIED (nothing blocked; answer whenever)

+-- CALL 3 of 4 ---------------------------------------------------+
  **The marquis short list: ratify the 14 (and retire comp-heat, keep
  comp-denytest) -- yes/no to each?**
  The CVO's draft v2 @c9785fb9e2 is in front of you. Your ratification
  is what turns FWD-8 from NOT_EVALUATED, and it defines FWD-10's
  denominator ("every marquis tool whose rc carries a verdict").
  --------------------------------------------------------------------
  **REC -- ratify the 14; retire comp-heat; keep comp-denytest.**
  comp-heat has 0 runs and its only consumer returns {} before
  reaching it, so retiring it removes a real FAIL by decision rather
  than by a fix nobody would use; denytest is the only tool that
  derives an expected verdict from an IAM change, and its low use is
  correct behaviour, not disuse.
+---------------------------------------------------------------------+

+-- CALL 4 of 4 ---------------------------------------------------+
  **The estate sitting: read the tool states so FWD-4 can grade
  (the packet is with the CVO, 57 rows) -- when?**
  FWD-4's DONE WHEN is literally "the last tool's state has been read
  by Andrew"; no seat's artifact can stand in for it, and the record
  has been ready since 07:2xZ.
  --------------------------------------------------------------------
  **REC -- take it in the same sitting as CALL 3.** The marquis
  ratification and the tool-state read are the same 24 rows seen from
  two angles; done together they close FWD-4, FWD-8 and FWD-10's
  denominator in one pass.
+---------------------------------------------------------------------+

NOT-MINE: 2.0.0_SA_COO~A holds the CLDGRPH round-4 continuation and
3.0.0_SA_CVO holds the estate-sitting packet -- run /open-calls there.
```

## What his word decides, clause by clause -- and what it does NOT

**CALL 1 -- APPROVED.** ONE Codex seat is relaunched. `0.0.0_AB_MSTR`'s spawn act. Its two exercises: CE-g-4's rail acceptance
(a DENY observed as the BODY NOT EXECUTING, `3.0.0_SA_CVO`'s design `CE-g-4.codex-rail-design.md` @22388f7195) and
NFRA_CLDGRPH-S30's fresh-seat gate on the repaired provisioner (@e4167f3c3b, 0 of 211 protected). "Reaped again after" was
this seat's REC and is approved with it; the reap is MSTR's on the exercises' completion.

**CALL 2 -- APPROVED.** ONE push window at `0.0.0_AB_MSTR`, now. 278 commits, HEAD `bd1ae5cfbd`, against origin/CLOUD
`@351f309e0a`. LD-0522's reservation is lifted for this window and no further; the push is MSTR's act, no seat's own.

**CALL 3 -- APPROVED IN TWO CLAUSES, REFUSED IN ONE.**
- *Ratify the 14* -- APPROVED. `3.0.0_SA_CVO` records the ratification against the fourteen NAMED in its draft v2
  @c9785fb9e2, since the list is that seat's document and this seat has not read it at full width.
- *Keep comp-denytest* -- APPROVED.
- *Retire comp-heat* -- **REFUSED, and replaced with an instruction:** *"i want comp-heat to be figured out and developed
  properly."* comp-heat is NOT retired. It is neither cleared nor closed: it is WORK, and it starts at L1 (below).

**CALL 4 -- APPROVED.** The estate sitting is taken together with the ratification. Not yet done: the sitting is an act, and
FWD-4's grade waits for it.

**WHAT THIS WORD DOES NOT DO, stated so nobody reads it wider.** It does not re-grade NFRA_COMPEFFICACY's close: the four
NOT_EVALUATED grades (@f755484cbb) stand until their acts LAND -- the push (FWD-9's shared-branch limb), the Codex seat
(FWD-9's rail limb), the sitting (FWD-4), and a seat starting work from the ratified list (FWD-8's third limb). It does not
re-open that project, whose decomposition is spent and whose row reads ROUND_CLOSE. It does not decide whether comp-heat
joins the marquis list -- that is downstream of it working. It does not touch NFRA_CLDGRPH round 4, the CLDGRPH holds, or
the ~Y fabric.

## comp-heat -- what "figured out and developed properly" starts as, and where

**MEASURED at this seat this turn, so the brief starts from a state and not a memory:** `.tools/comp-heat` is **415 lines**
(the PRD's s.7 pin reads 377 -- a moved surface), **five** subcommands, not the three the round-6 answer named: `freshness`,
`drift`, `score`, `compare`, and **`federated`** -- which carries `--sql` and runs an arbitrary federated Trino query, a
whole plane no cell of NFRA_COMPEFFICACY ever examined. **No `--budget` anywhere in the file** (25 flag/def hits, zero
budget), which is T20-AC4's FAIL at source: `comp-heat freshness` with no path scores the whole repo (an 8.3 MB snapshot)
and there is no bound to reach. Its usage is **0 CLI runs**; its only library consumer (`comp-similar.load_heat_live`)
returns `{}` before reaching it (S29); the daily-report wiring @09355b6d93 invokes it from nowhere.

**So "figured out" is a real question with two halves, and this seat does not answer either by fiat:** what is comp-heat FOR
(a git-history decay score, a drift surface, and a federated Trino query engine are three different tools sharing one
entrypoint), and WHO consumes it (nothing does today, and a tool with no consumer cannot be "developed properly" into
anything but a better-shaped orphan). "Developed properly" is then the buildable half: the Rule-T budget its verdict-bearing
rc requires, the disclosure its snapshot's vintage requires, and one real wired consumer.

**THE ROUTE, and it is the ordinary one -- L1 first.** This is new work, not a cell of a spent decomposition, so it starts
where his own ruling puts new work (2026-09-03 ~05:2xZ, verbatim: *"I will work with CRO on the /brief-create, i will confirm
CTO's DONE WHEN from their /endpoint --forward, but after that point ... I want the canonical loop to be able to keep cycling"*):
a brief at `4.0.0_SA_CRO`, then this seat's `/endpoint --forward`, and Andrew confirms the DONE WHEN. His word above is the
brief's originating prompt and is relayed verbatim.

**One shape offered to the CRO and NOT decided here, because deciding it would widen his word:** two findings sit adjacent
to comp-heat with owners named and no home -- `comp-which` F2 (a syntactically valid, non-existent gold-script id routed
with a confident 2.00 score: the router validates shape, never existence) and `comp-find` F1 (`--version` becomes a search
pattern on the most-invoked tool). Whether the brief covers comp-heat alone or the tool-remediation pass those two belong to
is the CRO's brief call with Andrew. **He said comp-heat; this record asks for comp-heat.**

## Standing law applied

Verbatim record + same-turn broadcast + push state stated, MEASURED (CLAUDE.md "Changing this file"; org/XXX.md). No gate is
added on any seat by this record. The two BLOCKING acts are `0.0.0_AB_MSTR`'s; the ratification record is `3.0.0_SA_CVO`'s;
the brief is `4.0.0_SA_CRO`'s; nothing here is this seat's to execute except the relay and this record.
