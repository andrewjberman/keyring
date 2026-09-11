# TO POSN_ASTTAX.TO-T5-1 -- MEASURE step (2)'s BAR: FOUR clauses, across EVERY SERVED SURFACE the retagged value reaches. It is a CONDITION, not a task (AT3-s-5, FWD-1/FWD-2). GATES THE RETAG

<to_id>POSN_ASTTAX.TO-T5-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~14</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5**
@`3832ac543c` · **Decomp cell:** `AT3-s-5` · **Issuance:** round 3.
**DEPENDS ON `AT3-s-1` (terminal @`425da33b79`). GATES `AT3-s-6` (the retag).**

> **RE-CUT 2026-09-11 ~22:3xZ, BEFORE ANY WORKER RAN THIS ORDER.** The first cut measured step (2) as
> it read at `49ddcc481d` -- TWO clauses against ONE artifact. L4 amended step (2) at `71a376b98e` to
> FOUR clauses across EVERY served surface, on this seat's own `Z-S6` pitch. **The order as first cut
> would have produced a TRUE-AND-INSUFFICIENT GO, which is the exact outcome the amendment exists to
> prevent.** L4 then amended AGAIN at `3832ac543c`, 20 minutes later: clause (b) now says
> **LABEL-GROUPED** weight, and step (3) requires BOTH stores. **This order is pinned to that second
> amendment, and the re-pin is the whole reason it was worth re-reading the PRD before spawning rather
> than after.** Nothing was spawned against either version; no work is discarded. The FILENAME carries the old
> narrow slug ("against the served artifact") and is left alone deliberately -- renaming it mid-round
> moves a path the issuance commit, the proof instance and the gate all reference, to fix a word.
> **The slug is stale; this document is the order.**

---

## THE CELL

PRD s.4 `C-RETAG-SAFETY`, step (2), **verbatim at `3832ac543c` -- this is your bar and the whole of it**:

> for EVERY ticker in the retag set, ACROSS **EVERY SERVED SURFACE THE RETAGGED VALUE REACHES**,
> (a) the served `asset_class` equals its ratified five-class label, (b) **its LABEL-GROUPED weight**
> is NON-ZERO and equal to its pre-retag weight, (c) **its row RENDERS** -- served row count equals
> DOM row count -- and (d) **the class subtotals sum to the grand total.**

⛔ **CLAUSE (b) SAYS "LABEL-GROUPED" AND THE WORD IS LOAD-BEARING. DO NOT READ THE ALLOCATION DICT.**
`AT3-s-1` measured it on the real `generate_positioning_data`, same input (row `W10-S1`):

| | served label | LABEL-GROUPED weight | `allocation['commodities']` |
|---|---|---|---|
| BEFORE | `'Unknown'` | **0.000** | 2.5 |
| AFTER | `'Commodities'` | **0.025** | 2.5 |

**THE ALLOCATION-DICT COLUMN DOES NOT MOVE** -- at base `651ffd4f16` the `if/elif` chains already
carried an `else` and the accumulator already served 2.5. A reader who satisfies (b) against that
column grades a number that reads IDENTICALLY in the healthy world and the broken one. ⛔ **That is
the `S2-AC5` shape for the THIRD time this project, and it was found INSIDE the bar that had just
been widened to fix the second instance. If your (b) evidence is a number that does not move between
BEFORE and AFTER, you are reading the wrong column.**

⛔ **STEP (2) IS CURRENTLY *NOT MET*.** `TO-S7-1` returned NO-GO in round 2 against the OLD two-clause
bar. `AT3-s-1` has since hardened the generator (terminal @`425da33b79`). **You measure whether the
FOUR-clause bar now holds -- across a surface set you DERIVE, not the one you inherit.**

⭐ **WHY THIS BAR IS WIDER THAN THE ONE THIS ORDER FIRST CARRIED.** Round 3's wave-1 cells measured
BOTH known collapse sites OUTSIDE `positioning_data.json`: a portal tab that never iterates the new
group, and a sibling lambda that zeroes its policy weight into a DIFFERENT artifact. A bar read
against one artifact returns GO while the page drops the row. **The grain is the finding.**

## THE ACT

1. **Name the retag set by MEMBER** (`T5-AC1`), not by description, with its ratified target label per
   ticker. Re-derive it; do not inherit it. Say so if your read differs from the issuer's seven.
2. **DERIVE THE SURFACE SET BY SUBTRACTION** (`T5-AC2`). ⛔ **THIS IS THE HEART OF THE CELL AND THE
   PART WITH NO PRIOR ART.** Enumerate every artifact and every rendered surface a retagged
   `asset_class` value can reach, print your DENOMINATOR, then SUBTRACT the ones you PROVE unreachable,
   naming the proof per subtraction. The PRD names three known sites; **they are examples, not the
   set.** Writing the enumeration from those three is the precise error this project keeps paying for.
3. **Build the SURFACE x CLAUSE table** (`T5-AC3`, `T5-AC4`, `T5-AC5`): for every surface in your set,
   grade (a), (b), (c) and (d) per member.
4. **State the EVIDENCE GRAIN of every cell in that table** (`T5-AC6`) -- MEASURED-EXERCISED,
   MEASURED-SOURCE-AT-PIN, or NOT-MEASURABLE-HERE, with one reason each.
5. **State GO or NO-GO** (`T5-AC7`), naming every failing (member, surface, clause) triple.
6. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **READ-ONLY. CHANGE NOTHING, ANYWHERE.** No registry write, no code edit, no deploy, no retag.
  This is the gate cell for an irreversible act; a cell that fixes what it measures cannot report on
  it cleanly.
- ⛔ **DO NOT EDIT, BUILD, RUN OR STAGE ANYTHING UNDER `portal/`. IT IS FROZEN BY ANDREW'S STANDING
  WORD, BOTH FABRICS.** You MAY READ portal source -- reading is not a write. Read it at the MAIN
  tree, `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/`, NOT in your worktree (the cone does
  not carry the submodule). A file you cannot open there is a ROW, never an inferred absence.
- ⛔ **DO NOT RETAG TO TEST.** Measure the CURRENT world. Do not move a live row to create a test case.
- ⛔ **CLAUSE (c) IS ALREADY KNOWN FALSE AT ONE SITE -- AND FINDING IT AGAIN IS NOT THIS CELL'S
  OUTPUT.** `W11-S1` measured `portal/src/pages/Positioning/tabs/HoldingsTab.tsx:1392-1394` iterating
  a hardcoded `assetClassOrder = ['Fixed Income','Equity']`. **Do not stop at it.** An early stop and
  a true absence read identically. The deliverable is the COMPLETE table, so a NO-GO names every
  surface that must change and not merely the first one anybody noticed.
- ⛔ **YOU CANNOT REACH A REAL DOM AND YOU MUST NOT PRETEND OTHERWISE.** You have no browser and the
  portal is frozen, so clause (c) is measurable here only at MEASURED-SOURCE-AT-PIN: does a render
  path exist that iterates this group key, and what does it do with one it lacks. **Grade it at that
  grain, SAY it is that grain, and name exactly what an EXERCISED reading would require.** A static
  read reported as EXERCISED is a worse outcome than an honest NOT-MEASURABLE-HERE.
- ⛔ **GO REQUIRES EVERY MEMBER TO PASS ALL FOUR CLAUSES ON EVERY SURFACE IN YOUR SET.** Not most. Not
  the held one. Not the artifact that was easy to read.
- ⛔ **DO NOT CONCLUDE FROM A PAGE.** Never `head` a census; a page is not an answer.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W14-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="T5-AC1" cell_refs="AT3-s-5"><invocation>timeout 180 .tools/aws dynamodb batch-get-item --request-items '{"etf-classifications":{"Keys":[{"ticker":{"S":"DBC"}},{"ticker":{"S":"GLD"}},{"ticker":{"S":"GSG"}},{"ticker":{"S":"IAU"}},{"ticker":{"S":"SLV"}},{"ticker":{"S":"USO"}},{"ticker":{"S":"VXX"}},{"ticker":{"S":"VIXY"}}]}}' --query 'Responses."etf-classifications"[].{t:ticker.S,a:asset_class.S,s:sub_asset_class.S,m:management_style.S}' --output json</invocation><expect>every key resolved and pasted verbatim, UnprocessedKeys named; then the RETAG SET stated BY MEMBER with each member's ratified five-class target label and a one-line reason per member. If your derived set differs from the issuer's seven, say so and state yours.</expect></criterion> `T5-AC1` -- THE SET, BY MEMBER, RE-DERIVED.

<criterion id="T5-AC2" cell_refs="AT3-s-5"><invocation>timeout 300 comp-find 'asset_class|assetClass' --all --files</invocation><expect>the printed DENOMINATOR (files scanned) and the full file list -- never a page. Then the SURFACE SET as a SUBTRACTION: start from every artifact and rendered surface this enumeration reaches, subtract each one you PROVE cannot carry a retagged value, and name the proof per subtraction. State the surviving set as a count and by name. The three sites the PRD names must appear as MEMBERS OF YOUR SET, never as its definition.</expect></criterion> `T5-AC2` -- ⭐ **THE SURFACE SET, BY SUBTRACTION, WITH ITS DENOMINATOR.** A denominator certifies the SWEEP, never the SET -- so state both.

<criterion id="T5-AC3" cell_refs="AT3-s-5"><invocation>timeout 180 python &lt;your served-artifact read, clauses (a) and (b)&gt;</invocation><expect>for EACH artifact-class surface in your AC2 set: its URI or path, LastModified and byte size pasted verbatim as the vintage; then per member, (a) served asset_class value vs ratified label PASS/FAIL and (b) LABEL-GROUPED weight NON-ZERO and equal to pre-retag PASS/FAIL. ⛔ Show THREE numbers per member, not two: the label-grouped weight BEFORE, the label-grouped weight AFTER, and the allocation-dict entry -- the last as a NEGATIVE CONTROL that is expected NOT to move. Grade (b) on the label-grouped column only; if the two columns disagree about whether anything changed, say so explicitly. A member passing (a) and failing (b) reads FAIL.</expect></criterion> `T5-AC3` -- CLAUSES (a) AND (b), WITH THE NON-DISCRIMINATING COLUMN SHOWN BESIDE THEM AS ITS OWN CONTROL.

<criterion id="T5-AC4" cell_refs="AT3-s-5"><invocation>timeout 300 python &lt;your render-path probe, clause (c)&gt;</invocation><expect>for EACH rendered surface in your AC2 set: the file:line of the code that decides WHICH groups render, quoted verbatim, and whether a group keyed with each ratified label is iterated or dropped. State served-row-count vs would-render-count per member. The grade must be labelled MEASURED-SOURCE-AT-PIN with its pin, and state in one line what an EXERCISED DOM reading would require that you do not have.</expect></criterion> `T5-AC4` -- CLAUSE (c), THE RENDER, AT AN HONESTLY-NAMED GRAIN.

<criterion id="T5-AC5" cell_refs="AT3-s-5"><invocation>timeout 300 python &lt;your subtotal arithmetic, clause (d)&gt;</invocation><expect>per surface: the class subtotals and the grand total as SERVED NUMBERS, and their difference. A weight counted in the grand total whose row does not render is the PROD v2.1.167 Cash failure reproduced -- show the arithmetic that would detect it, and state whether it is present now for each retag-set member.</expect></criterion> `T5-AC5` -- CLAUSE (d), THE ARITHMETIC THAT CAUGHT IT IN PROD.

<criterion id="T5-AC6" cell_refs="AT3-s-5"><invocation>timeout 120 python &lt;your grain table&gt;</invocation><expect>the full SURFACE x MEMBER x CLAUSE table with one grain label per cell -- MEASURED-EXERCISED, MEASURED-SOURCE-AT-PIN, or NOT-MEASURABLE-HERE -- each with a one-line reason. Count the cells at each grain and print the three counts. An ungraded cell is itself a finding and must be shown, never omitted.</expect></criterion> `T5-AC6` -- EVERY CELL CARRIES ITS OWN CLAIM. A value with no provenance may not be treated as measured.

<criterion id="T5-AC7" cell_refs="AT3-s-5"><invocation>timeout 120 python -c "print('BAR VERDICT RECORDED IN THE INSTANCE')"</invocation><expect>GO or NO-GO for AT3-s-6, stated as the CONDITION's truth value and not as "the harness ran". GO requires every member to pass all four clauses on every surface in the AC2 set. If NO-GO, list every failing (member, surface, clause) triple and, for each, the SMALLEST change that would make it pass -- that list is what the round carries to L8.</expect></criterion> `T5-AC7` -- THE GATE ON THE RETAG. A completed cell is not a passed one.

<criterion id="T5-AC8" cell_refs="AT3-s-5" judgment="true"/> `T5-AC8` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether the surface set derived in AC2 is genuinely the set the retagged value reaches, or merely the set that was reachable with the instruments at hand. **Record the readings and offer NO verdict.**

<expected_criteria>T5-AC1, T5-AC2, T5-AC3, T5-AC4, T5-AC5, T5-AC6, T5-AC7, T5-AC8</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-T5-1.the-bar-step-2-measured-against-the-served-artifact.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~14/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round3.md</decomp_doc> round 3, cell `AT3-s-5`.
<owned_cells>AT3-s-5</owned_cells>
Read-dependencies, NOT claimed: `AT3-s-1` terminal @`425da33b79` (it makes the bar meetable); `AT3-s-2` @`2da609c3cf` and `AT3-s-3` @`daa1a72fb8` supply the two known collapse sites -- READ their rows, do not re-run their cells. `AT3-s-6` is gated on YOUR verdict and is NOT yours.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only; no job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; DynamoDB and S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied, THREE items: (1) the issuer has NOT measured the four-clause bar at this vintage and is NOT
predicting its answer; (2) clause (c) is reachable here only at SOURCE-AT-PIN because the portal is
frozen and this worker has no browser -- the issuer knows this and cut the criterion to that grain
deliberately rather than cutting an unsatisfiable one; (3) round 2's 17/3/14 ratio is historical and
is not this cell's starting point.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~14/POSN_ASTTAX.TO-T5-1.the-bar-step-2-measured-against-the-served-artifact.proof_of_spec.json
</proof_of_spec>
