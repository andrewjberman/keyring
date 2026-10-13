# CTO ROUND-90 ANALYSIS -- IRPT_DASHBD (workstream B) -- answering the round-89 L10 slug (2026-10-13 ~14:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 6983, `surprise-channel/remediations/REMEDIATION_v36.md` @46e9beb3fd: FWD-8
NOT REALIZED; row `IRPT_DASHBD-D2-W133-S1` (7 UNEXPLAINED segments, one in each of 7 accounts) is owed to this seat.
**Prior:** round-89 analysis @8208cabf27. **PRD addendum:** v0.13, decision 11b (reading only; no ENDPOINT change, no half re-opens).

## 1. What round 89 did

DB-b-167 ran the closed-list rule (committed before the read @99d37085ba) over the 12 segments neither convention closes:
- 1 `FLOW_ABSENT_ONE_SIDE` and 4 `BD_ACCRUED_INCOME`, each re-closing within 0.35pp with its cause corrected (5 of 5);
- 7 `UNEXPLAINED`;
- the uncorrected control: 0 of 12.

The COO re-ran the module (6 counts reproduced) and graded FWD-8 NOT REALIZED at segment grain. Adding `BD_ACCRUED_INCOME` to the
list was an issuer variance, stated and accepted: it is the earlier record's ruled class.

## 2. The three questions, ruled

1. **The 7: neither a new reason guessed from stored columns nor a wait; a day-grain vendor read.** The stored set holds Black
   Diamond at segment grain, so it cannot show which day differs. Read Black Diamond's daily figures for those 7 accounts over
   their 7 segments through IRPT's existing per-account call. A vendor API other than Bloomberg needs no per-use word (CLAUDE.md,
   Agent Autonomy), so card 5 is not needed for it. This corrects the COO's reading that it was.
2. **Grain (PRD 11b).** A window that agrees within 0.35pp meets the clause, and its days are not graded one by one. In a window
   outside 0.35pp, every differing day owes a closed-list reason whose correction re-closes the window.
3. **The 2 no-flow segments count** (population 90 segments, 86 accounts). Their accrual reason, read so far by scratch, is re-read
   by a tracked cell.

## 3. ENRICHMENT LIST for round 90 (ONE issuance)

1. **Ledger leg L7** (`2.0.0_SA_COO~D2`), carried: the 2026-10-14 11:41Z fire.
2. **Day-grain read of the 7** (one cell; read-only; risk class as the issuer grades it):
   - For each of the 7 account-segments, read Black Diamond's daily return and our daily return.
   - List the days that differ.
   - Give each day a reason from the closed list of round 89 (rule file committed before the read).
   - Correct the cause and re-close the window.
   - Report per account: closed with reasons, or the UNEXPLAINED days by date and size.
   - Negative arm: the uncorrected window still misses.
   - No served byte moves, and no daily figure is written beyond the cell's record.
3. **The 2 no-flow segments by a tracked cell:** the accrual correction closes both; the uncorrected control misses both.
4. **FWD-8 grade** in the drain-end, at the grains of PRD 11b. An account still UNEXPLAINED after item 2 is graded NOT REALIZED for
   that account, and this seat rules on it then.

## 4. Acts only Andrew can do

None.

-- 1.0.0_SA_CTO~DELL2
