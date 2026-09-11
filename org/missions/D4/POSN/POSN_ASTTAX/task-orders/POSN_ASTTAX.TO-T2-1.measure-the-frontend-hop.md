# TO POSN_ASTTAX.TO-T2-1 -- MEASURE the frontend hop that `TO-S7-1` disclosed it could not see, so "end to end" stops being a claim (AT3-s-2, FWD-1/FWD-3)

<to_id>POSN_ASTTAX.TO-T2-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~11</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>staged</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5**
@`49ddcc481d` · **Decomp cell:** `AT3-s-2` · **Issuance:** round 3. **GATES `AT3-s-6` (the retag).**

---

## THE CELL

`TO-S7-1` traced the allocation chain and **disclosed, in its own report, that the FRONTEND hop was
never measured**: `portal/` sat outside the worker's cone and its census printed
`29,577 UNREADABLE, NOT searched`. Its own order named "a frontend contract" as a distinct hop class.
So round 2's "end to end" stopped at the served artifact.

⭐ **THIS CELL EXISTS BECAUSE AN UNMEASURED HOP MUST NOT TRAVEL AS THOUGH IT WERE MEASURED.** The
finding can only STRENGTHEN the existing NO-GO, never weaken it -- but the retag is the irreversible
act, and measuring after it would be measuring the wrong world.

## THE ACT

1. **Enumerate the portal consumers of the served `asset_class` / `assetClass` fields** (`T2-AC1`) with
   a printed denominator. The census that failed before failed on READABILITY, so say how many files
   you actually read and how many you could not.
2. **Determine what each does with a five-class value** (`T2-AC2`): carries it, maps it through its own
   fixed list, or drops it. A frontend fixed-key map is the same defect one layer out.
3. **State whether `asset_class_recognized` / `assetClassRecognized` is consumed at all** (`T2-AC3`) --
   `AT2-s-1` added those flags and nobody has checked whether the surface reads them.
4. **Verdict** (`T2-AC4`): does the frontend carry five classes, or does it collapse them?
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **READ-ONLY, AND PORTAL IS FROZEN.** Andrew: nothing portal moves, both fabrics, PROD and DEV,
  until he names it. **Reading is not promoting** -- but you change NOTHING under `portal/`, stage
  nothing there, and commit nothing there. If a fix is needed that is a FINDING and a later cell.
- ⛔ **DO NOT TOUCH THE PORTAL SUBMODULE POINTER.** It is dirty in the worktree by design and must stay
  that way.
- ⛔ **DO NOT CONCLUDE FROM A PAGE.** Any census uses `--all` or paginates; an early stop and a true
  absence read identically, and a missed consumer is the whole failure mode.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W11-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="T2-AC1" cell_refs="AT3-s-2"><invocation>timeout 300 comp-find 'assetClass|asset_class' --all --files</invocation><expect>the printed DENOMINATOR and the file list; then the PORTAL subset named explicitly, with a stated count of files READ versus files UNREADABLE. If anything is unreadable, say so and say why -- an unreadable file is not an absent consumer.</expect></criterion> `T2-AC1` -- THE CONSUMER SET, WITH ITS READABILITY STATED. This is exactly where round 2 stopped.

<criterion id="T2-AC2" cell_refs="AT3-s-2"><invocation>timeout 180 python &lt;your per-consumer read&gt;</invocation><expect>one row per portal consumer: file:line, and whether a value of "Commodities" is CARRIED, MAPPED THROUGH A FIXED LIST, or DROPPED. Every consumer from AC1 accounted for; consumers examined == consumers enumerated.</expect></criterion> `T2-AC2` -- WHAT EACH ONE ACTUALLY DOES WITH A FIVE-CLASS VALUE.

<criterion id="T2-AC3" cell_refs="AT3-s-2"><invocation>timeout 120 comp-find 'assetClassRecognized|asset_class_recognized' --all --files</invocation><expect>the DENOMINATOR and every hit; then a stated answer to whether any PORTAL consumer reads the flag, named either way. "No consumer" is a legitimate and important answer -- state it positively.</expect></criterion> `T2-AC3` -- IS THE RECOGNISED FLAG CONSUMED, OR WAS IT ADDED INTO A VACUUM.

<criterion id="T2-AC4" cell_refs="AT3-s-2"><invocation>timeout 120 python -c "print('VERDICT RECORDED IN THE INSTANCE')"</invocation><expect>a stated verdict -- the frontend CARRIES five classes, or COLLAPSES them -- with the collapsing sites named, and an explicit statement of what remains unmeasured if anything does.</expect></criterion> `T2-AC4` -- THE VERDICT, WITH ITS OWN LIMITS NAMED.

<criterion id="T2-AC5" cell_refs="AT3-s-2" judgment="true"/> `T2-AC5` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether this measurement genuinely closes the gap `TO-S7-1` disclosed, or only moves it one layer further out. **Record the readings and offer NO verdict.**

<expected_criteria>T2-AC1, T2-AC2, T2-AC3, T2-AC4, T2-AC5</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-T2-1.measure-the-frontend-hop.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~11/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round3.md</decomp_doc> round 3, cell `AT3-s-2`.
<owned_cells>AT3-s-2</owned_cells>
Read-dependency, NOT claimed: `AT3-s-6` (the retag) waits on this cell being terminal. You do not retag.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only; no job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied: NOBODY has measured this hop. `TO-S7-1` declared it unmeasured and this is its first read, so
there is no prior figure to corroborate or contradict.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~11/POSN_ASTTAX.TO-T2-1.measure-the-frontend-hop.proof_of_spec.json
</proof_of_spec>
