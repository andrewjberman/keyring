# TO LGIC_ENFORCE.TO-EN-z-3 -- round 20 EN-z-3: FWD-5 item 3: one planted unreadable name STOPS the run; a readable name passes
<to_id>LGIC_ENFORCE.TO-EN-z-3</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `EN-z-3` (`decompositions/LGIC_ENFORCE_DECOMP.md` section 0u) | **outcome_ref:** FWD-5 |
**depends_on:** none (slot ~3)

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

`EN-z-3` (FWD-5 clause 4: "a name the check cannot read stops the run loudly rather than being filed as breaking the
pattern"). Every census run so far had `stopped=0`, so the stop was never exercised. This cell plants one.

**Build:**
1. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/stop_planted_r20.tsv`: ONE line `TYPE<TAB>NAME`, a name `grade()` cannot read (it RAISEs; for example a first token in no
   vocabulary). Show the RAISE text in your result.
2. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/stop_readable_r20.tsv`: ONE line, a readable name of the same type (the negative control).
3. Run `python lib/opal_naming.py census --names <file>` on each; record both exit codes and last lines.
4. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LOUD_STOP_R20.json`: `planted_file`, `readable_file` (repo-relative), `planted_name`, `planted_rc`, `readable_rc`,
   `planted_last_line`, `readable_last_line`.
5. `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/loud-stop.r20.result.md`: both runs, whole.

### ACCEPTANCE

<criterion id="Z3R20-AC1" cell_refs="EN-z-3"><invocation>python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~B1/fixed_inputs/r20/check_en_r20.py stop</invocation><expect>PASS-R20-STOP</expect></criterion>
`Z3R20-AC1` -- the check re-runs both files: the planted name exits 3 with a STOPPED line naming it and no verdict row; the readable control exits 0 COMPLETE.

<expected_criteria>Z3R20-AC1</expected_criteria>

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
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/stop_planted_r20.tsv
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/stop_readable_r20.tsv
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LOUD_STOP_R20.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/loud-stop.r20.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-z-3.loud-stop.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-z-3.loud-stop.md
</paths>

The block is your WRITE grant. You read and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.20, round-20 cell `EN-z-3` (section 0u).
<owned_cells>EN-z-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Z3R20-AC1. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-z-3.loud-stop.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Z3R20-AC1 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-z-3.loud-stop.md` BEFORE the
`complete` flip. Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.
</proof_of_spec>

**REPORT:** both runs' exit codes and last lines; the last line of every criterion whole; your commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no grant, no AWS call.
comp-adversary: RUN -- a recorded result never run: the check re-runs both files itself and matches the recorded exit codes. A planted name that is merely OUT-OF-PATTERN: the check refuses any verdict row for it and requires exit 3. BLIND: one planted name exercises the stop path once; it does not prove every unreadable shape stops.
lane: the <paths> block IS the grant (worker RULING 1); nothing in the prose grants a path.
</preflight>

Source: `org/missions/D14/LGIC/LGIC_ENFORCE/ledger/FWD5_GRADE_FROM_BLANKFIX_FWD9_20261008.md` re-grade 2026-10-09 ~15:2xZ (`1.0.0_SA_CTO~DELL1`, msg 2639), round-20 list; decomposition section 0u. Base dry-run at
the cut, by the issuer at base 133bf5f7a4: Z3R20-AC1 base: FAIL as expected (LOUD_STOP_R20.json absent). Positive control by the issuer: a hand-built correct record (planted `zqxv-frobnicate-wibble`, readable `mdpf-cot-publisher-lambda`) PASSES the arm; files removed, never committed.
