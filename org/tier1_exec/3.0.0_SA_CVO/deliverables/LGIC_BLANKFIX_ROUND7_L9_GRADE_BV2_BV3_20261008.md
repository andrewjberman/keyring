# LGIC_BLANKFIX round 7 -- L9 grades of BV2-AC2 and BV3-AC2 (on 1.0.0_SA_CTO msg 107449)

**archetype:** VALIDATE

Drain-end packet: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ROUND7_DRAIN_END.md` @666a8bf668. Runs by
this seat at HEAD `45e2856e41` (branch box/laptop), 2026-10-08 ~23:0xZ to 23:1xZ. Repository plane only.

## BV2-AC2 (FWD-5, a fresh seat from the written instructions): MET

Artifact: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~5/FRESH_RUN_round7.md`. Read against FWD-5's ACCEPT
(PRD lines 59-64) and the CTO's ruling that the check is `python lib/opal_naming.py census --all-roots`
(`ledger/ROUND_ANALYSIS.round6.md:9-15`).

- **Written instructions.** `infra/logic/README.md:67` "Run the naming check" names the command, says what each output line
  is, and explains the last line field by field. The seat reached the file through CLAUDE.md rule 30, which points into
  `infra/logic/`, plus the folder name. It did not find it from the root `README.md` or `AGENTS.md`, which name neither. That
  is a discoverability shortfall, not a failure of FWD-5: CLAUDE.md is a written instruction every seat loads.
- **A seat that had never run it.** The decomposition makes slot `~5` a new seat on a worktree cut after `BF-v-1` merged
  (`decompositions/LGIC_BLANKFIX_DECOMP.round7.md:24, 52, 77`). The record shows a real search: README, AGENTS, CLAUDE.md,
  `comp-which`, then `ls infra/logic`. This seat cannot see the spawn transcript, so the seat's freshness is the issuer's
  statement plus that trace. It is not something this seat measured.
- **It finishes.** The record has rc 0 in 13.8 s, ending `ALL-ROOTS ok=True ... mapped=13 ... hole=1 ... uncounted=301`. This seat
  re-ran it at `45e2856e41`: rc 0 in 29.5 s, 392 lines, empty stderr, `ALL-ROOTS ok=True roots_total=87 mapped=63 unmapped=24
  completed=63 stopped=0 items=1598 ... hole=285 ... uncounted=301`. The run reaches its totals at the larger map too.
- **Nothing written for the run.** The seat wrote two redirect files in the worktree root to read the output, deleted them, and
  disclosed it. Nothing the run needed was written: no skip list, card or configuration. BV2-AC1 reads `outside_writes=0`.

Residual for round 8: `infra/logic/README.md` types figures that the map's growth has already overtaken. It says "about 170
lines" (`:87`; 392 measured) and "about 15 seconds" (`:81`; 29.5 s measured), and that "the other 74 roots print `UNMAPPED`"
(`:154`; 24 measured). The field meanings are still right. The orders bar typed totals in tests for this reason, and the same
bar applies to the newcomer's text.

## BV3-AC2 (FWD-6, the repaired design): MET

Artifact: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/FWD6_DESIGN_round6.md` (repaired in place by
703f4fd634). Read against FWD-6's ACCEPT (PRD lines 67-73) and the three repairs of the round-6 grade
(`LGIC_BLANKFIX_ROUND6_L9_GRADE_BU6_BU7_20261008.md`).

1. **Arm C now agrees with the decision rule.** Step 1 calls `place()` for an unmapped root's TEXT while `grade()` keeps the
   verdict, so no well-formed name is refused for lacking a row (C-CREATE holds). The arm uses a name that has a `{system}` blank
   (a NEW Lambda `daily-pull`). Row W1-S17 is right that my suggested repair alone would not have rescued arm A's name, which has no
   `{system}` blank. This seat re-ran `armC_run.py`: `ARMC ok=True control=FIX c=HOLE c2=HOLE`, with the texts `no map entry
   for this root` (C) and `this root serves more than one firm` (C2).
2. **Arm D grows the HOLE count.** This seat re-ran `armD_run.py`: `ARMD ok=True holes_head=0 holes_scratch=1 grew=True`, and the new
   line is `{cadence}: minute field 0/7: not a single minute`. Only the cadence reader reads the scratch text; the file under
   `infra/` is untouched. A negative arm D-neg (a cron edit on a name that already carries its word gives FIX) is READ, not run.
   That matches the round-6 reading of the same branch.
3. **Every HOLE text is owned.** This seat re-ran `check_fwd6_design_round7.py`: `hole_texts=18 owned=18 unowned=0`. The checker
   reads the texts from the code with `ast`, so a later text fails it. Negative control by this seat: with the design's H13 row
   removed (in a scratch copy, since deleted), the checker printed `UNOWNED {cadence}: no cadence row for this name` and
   `ok=False ... owned=17 unowned=1`. **Correction to my round-6 grade (row W1-S18):** the code holds 18 texts, not 14. My
   subtraction read `decide()`, the card line and the collision, and missed the three reasons `_ruling_of` appends plus the frame
   line. The domain I subtracted from was narrower than the claim.

The negative arms from round 6 (B, E, F, G) are unchanged, and the new D-neg is a further one. The design states what it does
not cover. Each arm as written can produce its expected value, and each HOLE text has an owner.

## What the CTO should have asked but did not

**Does FWD-2's denominator now move faster than the round can grade it?** Round 7 took the map from 13 to 63 roots and FWD-2 from
`hole=0` to `hole=285` (205 carded-class), plus `uncounted=301` names the check finds but does not grade. FWD-5 and FWD-6 are now
graded on mechanisms, and both hold. FWD-2 and FWD-7 are breadth: every entry the registry's lane lands adds holes faster than a
round of cells clears them. Round 8's cut needs a stated ceiling (roots mapped per round), or an order of work by hole class with
its own exit. Otherwise the outcome reads NOT_REALIZED after every round that does real work.

-- 3.0.0_SA_CVO
