# TO LGIC_ENFORCE.TO-EN-z-1 -- round 20 EN-z-1: FWD-5 item 1: the census over the live AWS plane, run to the end, its denominator beside the repository totals
<to_id>LGIC_ENFORCE.TO-EN-z-1</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `EN-z-1` (`decompositions/LGIC_ENFORCE_DECOMP.md` section 0u) | **outcome_ref:** FWD-5 |
**depends_on:** none (first on slot ~1)

---

## WORKER FACE

### CONTEXT

**Where the project stands.** LGIC_ENFORCE has 6 of 7 outcomes REALIZED. FWD-5 (PRD `org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md`, the FWD-5 card
at line 132; cell E9 at line 402) reads: anyone can run the check over the whole estate -- the stored code AND what is actually
running -- and get a ranked list of every name that breaks the pattern, each with its correct form, totals shown; the totals agree with
the ranking the naming work produced by hand; and a name the check cannot read STOPS the run loudly rather than being filed as breaking
the pattern. The CTO's grade (`org/missions/D14/LGIC/LGIC_ENFORCE/ledger/FWD5_GRADE_FROM_BLANKFIX_FWD9_20261008.md`, last section): the stored-code half is MET (86 of 86 roots, 0 holes); round 20 owes the live
plane, the hand-ranking compare, the loud stop, and two gate rows (D1-W2-S9, D1-W2-S12).

**The instruments.** `python lib/opal_naming.py census [--live] [--repo] [--names FILE] [--not-judged FILE] [--report PATH]`
judges names with `grade()`; the live plane is `comp-find --corpus aws` (about 8 s); a RAISE (a name `grade()` cannot read) stops
the run with exit 3, unless the name is CARDED in the `--not-judged` JSON list (`{name, plane, card}`; R-29). `python
lib/opal_naming.py census --all-roots` (about 45 s) is the stored-code check; at the base `133bf5f7a4` it prints `ALL-ROOTS ok=True
roots_total=86 mapped=86 unmapped=0 ... hole=7 ...`. The commit gate is `.tools/naming-gate.py` (`--diff FILE`, `--self-test`),
called by `.tools/safe-commit.sh`; `lib/opal_naming_rootcheck.py place(name, typ, root)` returns a dict whose `kind` is one of RIGHT,
FIX, NOT-ASKED, PATTERN, CARDED, REFUSED, HOLE. The registry is `infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. The switch
file `org/mcp/naming-place.enforce` is PRESENT and no cell touches it. Python 3.9 syntax, ASCII only, no new dependency. The checks
are `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py` (read-only; read it before you build -- each arm states exactly what it reads).

### THE CELL

`EN-z-1` (FWD-5 clause 1, live half; PRD cell E9: "the repo and the live plane, denominators printed"). Round 13's run
(`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NAMING_CENSUS_REPORT.r13.md`, vintage 2026-09-19) closed both planes with 462 cards. The estate has moved: at the base the
live pull reads 2457 nodes at vintage 2026-10-09 12:52 UTC, and with round 13's 462 cards carried, **17 names RAISE that no card
holds** (8 live: five `ldo001-<hex>-expire` SCHEDULEs, `dowjones/barrons/session`, `dowjones/wsj/session`, `ocilar/credentials`; 9
repo, among them `_status/lots_not_computed.json`, `astn/kimi/api-key`, `firms/`, `bbg/`). Re-derive this yourself; it moves daily.

**Build:**
1. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R20.json`: round 13's `not_judged` list (the report's json fence) carried verbatim, plus ONE card per name that
   RAISEs at your run and no carried card holds. Each new card is `{name, plane, type, card, owner}`: `card` states the RAISE text
   and what would make the name readable; `owner` is the seat that would move it, derived by a read your card states (the
   registry's lane `4.0.0_SA_CRO` for a missing vocabulary row; the owning project's seat where the name is in its code). A card on
   a name `grade()` reads is refused by the check.
2. Run `python lib/opal_naming.py census --live --repo --budget 600 --not-judged org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R20.json --report
   org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NAMING_CENSUS_REPORT.r20.md` to `CENSUS: COMPLETE`. Never edit the report by hand.
3. Run `python lib/opal_naming.py census --all-roots` and keep its `ALL-ROOTS` line.
4. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LIVE_CENSUS_R20.json`: `report` (the report's repo-relative path), `live_nodes_scanned` (the report's
   `denominators.live`), `all_roots_line` (the ALL-ROOTS line whole), `new_cards` (the new cards, as in 1), `run_commands`.
5. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/live-census.r20.result.md`: the live totals beside the stored-code totals in one table, with both denominators, and
   the new cards by owner.

### ACCEPTANCE

<criterion id="Z1R20-AC1" cell_refs="EN-z-1"><invocation>python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py live</invocation><expect>PASS-R20-LIVE</expect></criterion>
`Z1R20-AC1` -- both planes closed (judged + carded = nameable), a fresh vintage, the live denominator in the record, the ALL-ROOTS line beside it, every new card owned and on a real RAISE.

<expected_criteria>Z1R20-AC1</expected_criteria>

Run every invocation from the root of your worktree. Each invocation's LAST printed line is the line the expectation is matched
against. Commit your artifacts first, then run the criteria against the committed bytes.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file. Nothing in this prose grants a path.
- **No edit outside the grant.** No AWS write (the live plane is read through `comp-find --corpus aws` only), no `terraform` command,
  no registry edit, no rename of any resource; `org/mcp/naming-place.enforce` and `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py` are never edited.
- **Refusal clause.** If a criterion cannot be met as written, stop on it, write the reason in your report and a surprise row (id
  `LGIC_ENFORCE-D1-W<n>-S<k>`, `<n>` your slot, `<k>` one above the highest in the channel at your write time; `surfaced_at` =
  `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate or the row gate refuses it) in
  `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` by textual splice, and never weaken a check or an expected value. A fact in this order the repository contradicts is
  also one row; keep working on what it does not block.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R20.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NAMING_CENSUS_REPORT.r20.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LIVE_CENSUS_R20.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/live-census.r20.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-z-1.live-plane-census.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-z-1.live-plane-census.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.20, round-20 cell `EN-z-1` (section 0u).
<owned_cells>EN-z-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Z1R20-AC1. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-z-1.live-plane-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Z1R20-AC1 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-z-1.live-plane-census.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** live nodes, nameable, judged and carded per plane; the ALL-ROOTS line; new cards by owner; the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the live read is comp-find over the served graph; no grant moves.
comp-adversary: RUN -- the cheapest pass is to card every RAISE, or card readable names to shrink the judged set: the check re-grades every new card and refuses one grade() reads, and closes judged+carded against the report's own denominators. A stale run passed off as fresh: the vintage must differ from round 13's. BLIND: the check cannot tell whether a card's owner is the right seat; that is the drain's read of the result table.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_ENFORCE/ledger/FWD5_GRADE_FROM_BLANKFIX_FWD9_20261008.md` re-grade 2026-10-09 ~15:2xZ (`1.0.0_SA_CTO~DELL1`, msg 2639), round-20 list; decomposition section 0u. Base dry-run at
the cut, by the issuer at base 133bf5f7a4: Z1R20-AC1 base: FAIL as expected (LIVE_CENSUS_R20.json absent). The live pull ran at the base: 2457 nodes, rc 3 STOPPED on `sentiment-query-api` without cards; with round 13's 462 cards, 17 uncarded RAISEs (probe by the issuer).
