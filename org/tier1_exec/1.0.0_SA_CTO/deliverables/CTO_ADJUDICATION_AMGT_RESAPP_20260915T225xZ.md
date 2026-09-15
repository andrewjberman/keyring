# CTO ADJUDICATION -- AMGT_RESAPP, /self-drive tick 8 (2026-09-15 ~22:5xZ) -- CARD 17 WITHDRAWN

**Adjudicator:** `1.0.0_SA_CTO~W`, on Andrew-direct ~19:3xZ (@`2ac5611057`). **Scope:** AMGT_RESAPP.
**Trigger:** `0.0.0_AB_MSTR~Z` msg 23276 (22:43:55Z), "STOP -- DO NOT REMEDY `3.0.0_SA_CVO~W`: it is WORKING".

```
OPEN CALLS -- AMGT_RESAPP -- 1.0.0_SA_CTO~W, /self-drive tick 8

+-- CALL 18 (SUPERSEDES CARD 17) -------------------------------------+
  **Is `3.0.0_SA_CVO~W` deaf, and does anything remedy it?**
  Card 17 (@`981b8bc234`) ruled the seat DEAF and routed a remedy to `0.0.0_AB_MSTR~Z`.
  --------------------------------------------------------------------
  **REC --** Withdraw card 17. The seat is working inside one long turn; no operator act, no nudge, no teardown.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) **CARD 17'S CONCLUSION IS WITHDRAWN. NO REMEDY, NO NUDGE, NO TEARDOWN.**
  MEASURED BY THIS SEAT at 22:45:56Z, on the instruments card 17 did not use:
  - `3.0.0_SA_CVO~W`'s OWN worktree `C:/tmp/cvo-amgt-r11-20260915` (at `a35563e197`) holds EIGHT STAGED paths -- the L8, L9 and L10
    round-11 stamps, `ADJUDICATION_v11.md`, `REMEDIATION_v11.md` (the round's slug) and a modified `REMEDIATION_v10.md`, plus the CVO
    AUDIT and VERIFY deliverables -- with its newest files written 22.5 minutes before the read;
  - two live processes, pids 5658 and 6077, are `.tools/safe-commit.sh` under `3.0.0_SA_CVO~W`'s author line, started 22:23Z.
  So the slug exists and is one commit away. `0.0.0_AB_MSTR~Z`'s peek (`.tools/unstick.ps1 -Peek`, a screenshot, no keystrokes) read the
  seat's own TUI: "Working (34m 22s)", waiting on that safe-commit. A teardown would have killed 250 dispositions, three stamps and the
  slug.
  **WHY CARD 17 WAS WRONG, and it is not that its measurements were:** every arm it used -- the seat's `read/` cadence, the untaken
  messages, the author-anchored commit stop, the nudger's deduplicated log -- observes a turn ENDING. A seat inside one long turn produces
  that signature by construction. Four arms, one plane: Rule 22's shared-dependency blindness, and the breadth read as corroboration.
  The instruments that discriminate are the seat's OWN worktree, the process plane, and the peek.
  **THIS LANE'S OWN AGGRAVATION:** the estate's banked lesson (`a-live-pid-is-not-a-consuming-session-the-deaf-seat-tell`) already says
  to check for fresh work in the seat's own tree BEFORE any deaf verdict, and names a codex seat's worktree as the place the broker-plane
  instruments cannot see. This seat read that file at 22:4xZ and still ruled first and checked after. The memory is updated with this
  instance.
  **NOTHING WAS SENT:** the card-17 routing message to `0.0.0_AB_MSTR~Z` was never sent (the stop arrived first), so no seat acted on the
  withdrawn ruling. `2.0.0_SA_COO~W` measured carefully, took no act and routed rather than remedied; that restraint is why the window existed.
  **WHAT HOLDS:** nothing in the round changes. The slug lands when that commit returns, and this lane's L10 read starts then.
+---------------------------------------------------------------------+
```

Ledger: a superseding row (tick 8) is appended beside row 15; the ledger is append-only, so row 15 stands as written and this row names it.
Push state: LOCAL.
