# LGIC_BLANKFIX round 6 -- L9 grades of BU6-AC2 and BU7-AC2 (on 1.0.0_SA_CTO msg 107180, relayed by 0.0.0_AB_MSTR msg 107211)

**archetype:** VALIDATE

Drain-end packet: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ROUND6_DRAIN_END.md` @21953a8ea9.
Runs by this seat at HEAD `7b9efd885f` (branch box/laptop), 2026-10-08 ~20:2xZ to 20:4xZ. Repository plane only.

## BU6-AC2 (FWD-6 design): NOT MET as written -- two of eight exercise arms cannot produce their expected value

Artifact: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/FWD6_DESIGN_round6.md`.
Read against FWD-6 at PRD lines 67-73 (row W1-S16: the order's 66-71 stops mid-ACCEPT). BU6-AC1 re-run here:
`FWD6-DESIGN ok=True headings=7 paths=30 missing=0`.

The criterion asks three questions.

**1. Could it be built and exercised as written? Mostly yes, with two arms that fail as written.**
The building blocks exist as the design states: `decide()` at `lib/opal_naming_rootcheck.py:380` and `check_root()` at `:482`
(`place()` is an extraction of these two, not a second decision); `.tools/naming-gate.py` has the R20 waiver lookup the override arm
needs (`:114-123`, `:1306`); `.tools/naming-apply-gate.py` has plan mode for an ADDED resource (`:9-14`); the PRD cites hold
(C-CREATE at `:119`, arc item 2 at `:174`). The live lines quoted in the examples match this seat's run of
`python lib/opal_naming_rootcheck.py lines infra/aws/terraform/investor-reporting/directory --map infra/logic/registry/root_map.json`
(`FIX SCHEDULE irpt-directory-refresh -> irpt-directory-refresh-daily [...schedule.tf:389]`,
`RIGHT SCHEDULE irpt-directory-refresh-retry-daily [...:423]`, `ROOTCHECK ok=True ... hole=0`).

- **Arm C (refuse HOLE) contradicts the design's own decision rule.** The arm removes the root's map entry from a copy of the map and
  expects `{system}: no map entry for this root` from `place()`. The decision rule's step 1 says a name in an UNMAPPED root "uses
  `grade()` alone". With the entry removed, `resolve()` returns None (`lib/opal_naming_rootmap.py:136-138`), so the root is
  unmapped and step 1 routes it away from `place()`. The arm would print today's blank form, not the HOLE text. For the same reason
  the first row of the "what is owed" table (`no map entry`) can never be printed.
- **Arm D (the ratchet grows) uses an act that yields FIX, not HOLE.** Suppose a cron edit changes the word an EXISTING cadence name
  carries (for example `irpt-directory-refresh-retry-daily` to a weekly cron). `decide()` then rebuilds the name on the new word
  (`:417-423`, `_rebuild_on_word` at `:360-365`) and prints FIX `...-weekly`. If the name is ruled in `event_rules.json`,
  `decide()` returns the ruled form (`:414-416`). Neither path prints HOLE, so the HOLE count does not grow and the arm reads rc=0.
  Reading the code, an act that does grow the count: give a schedule whose name carries no cadence word (`irpt-directory-refresh`,
  FIX today) an expression the cadence reader cannot decide. `{cadence}` then stays blank, which is HOLE at `:458-459`. This seat
  did not run that act.

**2. Does it tell the person what they owe? Yes for FIX, and only partly for HOLE.** For FIX the person gets the exact name and
where each blank was filled from. For HOLE, `decide()` and its callers print 14 distinct texts: `decide()`'s returns and
`why` clauses at `:397-467`, the card line at `:303` and the collision at `:556`. The owed table's 6 rows cover 7 of them (its
cadence row covers both `:421` and `:457`). By subtraction, the table has no owner for these 7:
- `grade()` raised (`:409`)
- a stray brace (`:397`)
- a card that gives no name (`:303`)
- the role's system not resolved (`:445`)
- the inline policy (`:449`)
- the cadence reader's `basis` when it finds no word (`:459`, the arm-D replacement above)
- "a blank remains that no module fills" (`:467`)

The build needs an owner for each text, or a default owner such as `1.0.0_SA_CTO` for a rule defect, as the table's last row does.

**3. Does its exercise hold a negative arm? Yes.** B (right name passes), E (an existing wrong name touched passes with WARN),
F (a removed HOLE passes) and G (switch absent: same text, rc=0) are the negative and organic arms. Two controls run first.

**Repair, smallest first, for the round-7 analysis:**
- State whether step 1 calls `place()` for the HOLE text on an unmapped root (refusing only a wrong name), or re-target arm C to a
  HOLE a mapped root can print (a multi-firm root's missing `fills.system`, or an UNDECIDED key).
- Replace arm D's act with one that grows the HOLE count.
- Give every HOLE text an owner.

## BU7-AC2 (FWD-5 first run): NOT MET -- the seat did not reach the totals from the written instructions

Artifact: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/FRESH_RUN_round6.md` (raw outputs
`run1.out`, `run4.out`, `run5.out` beside it). Read against FWD-5 at PRD lines 59-64 and the PROVENANCE note at `:102-103`
(a repository-held skip list may be used).

- **The seat was fresh.** Slot `~5` carried only `BF-u-7` in the round (commits e7f04b2f9e, 905e2a6fbc). The order's
  `depends_on` says "a new slot and a new worktree at the trunk". The decomposition says the spawn prompt held no command.
- **The written instructions do not reach the totals on the repository plane.** This seat re-ran the two stops at `7b9efd885f`:
  - `python lib/opal_naming.py census --repo` gives rc 3:
    `CENSUS: STOPPED on the first RAISE after 2 judged (0 carded): repo IAM_POLICY 'F49ServedAndSourceRead'`.
  - With the repository's skip list `NOT_JUDGED_R13.json` it also gives rc 3:
    `STOPPED on the first RAISE after 1007 judged (75 carded): repo IAM_POLICY 'restricted-prefix-get-put-list'`. The worker read
    1006 judged; the estate moved by one name since.
  - The written commands (`infra/logic/10_ONBOARDING_CHECKLIST.md:344`, the brief's line 15) both carry `--live`.
    `infra/logic/README.md` names no command (0 occurrences of `opal_naming`).
- **The one mode that finished is not written anywhere a newcomer reads.** `census --all-roots` finished with totals over 13 of
  87 roots (74 unmapped). The seat found it only in the help text.
- **Nothing was written for the run.** BU7-AC1 is `outside_writes=0`. The record names the read-only skip lists it used.

## What the CTO should have asked but did not

**Which command is "the check" in FWD-5?** The PRD's FWD-5 inherits LGIC_ENFORCE's whole-estate `census --repo` (PROVENANCE `:104`,
FWD-9). Since round 2, this project's check is the root check, `census --all-roots`. The two answers cost very different amounts:
- **`census --all-roots`:** FWD-5 is one written paragraph from a pass, and "finishes" holds today, over the mapped roots.
- **`census --repo`:** FWD-5 needs every RAISE in the estate resolved or carded in a repository-held list. That is FWD-7's breadth,
  not a round-7 item.

Until the CTO rules which, a round-7 FWD-5 cell cannot be cut with a reachable expectation.

-- 3.0.0_SA_CVO
