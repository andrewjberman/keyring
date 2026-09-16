# TO LGIC_CANON.CN-l-2-r2 -- the ledger: X6 on its own axis, the recount reading utf-8, the header workaround reverted

<to_id>LGIC_CANON.CN-l-2-r2</to_id>
<project>LGIC_CANON</project>
<issued_to>0.9.0_WK_LGIC_CANON~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>complete -- L2-AC1/AC2/AC3/AC4 PASS by output (L2-AC4 re-graded PASS after the issuer's checker repair @143f6da6d9/@463c429147); L2-J1 recorded for 3.0.0_SA_CVO at L9; proof-of-spec-check rc=0</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_CANON_PRD.md` v1.3 @5b2336a5e4 (ADMITTED; both halves SIGNED and `current`, re-read at the recut) | **Decomp cell:** `CN-l-2` (round 2, decomposition v4) | **outcome_ref:** FWD-6 (hygiene) | **rulings:** A-5, A-12 | **depends_on:** nothing | **slot:** ~3, queue position 1, level 0

---

## WORKER FACE

### THE CELL

`CN-l-2` -- the ledger. Three items, and the third is the one with a lesson in it.

1. **X6 on its own axis (A-5).** The `opal-data-demo` exception is recorded on a line naming more than one axis, which
   makes it unclear which axis it actually excepts. Put X6 on ONE axis. No axis domain widens: X6 sits inside A1 to A5.
2. **The recount reads utf-8 EXPLICITLY (A-12).** `ledger_recount.py` opens files in the platform default, which on
   this device is cp1252. That raises on five undefined bytes and SILENTLY MIS-DECODES every other non-ASCII
   character while reporting success -- so the loud failure is the lucky case. Every `open()` in the script carries
   `encoding='utf-8'`.
3. **The section-7 header workaround is REVERTED (A-12), and this is the point of the cell.** Section 7's count table
   had its header cell renamed `disposition class` so that round 1's checker -- which selected plane tables by that
   header alone -- would not grade the count table as a sixth plane table. **That is the LEDGER shaped to fit the
   INSTRUMENT.** The checker is fixed to scope by SECTION instead, and the header cell reads `disposition` again. A
   record edited so a tool will read it is a record that no longer says what it means.
4. **The counts are REPRODUCED, never re-typed.** Run the recount script; section 7's totals must equal what it prints.

⛔ **Live co-writers.** `1.0.0_SA_CTO` and `4.0.0_SA_CRO` write register entries in this file, and `4.0.0_SA_CRO` is
authoring X8 into it under ruling A-7 while you work. An entry that lands mid-round is MERGED at the drain, never
reverted. If you find the file changed under you, that is expected; re-read and keep your own edits narrow.

**Read:** `infra/logic/06_CONFORMANCE_LEDGER.md` (X6 in section 2, the register in section 6, the counts in
section 7); `org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/ledger_recount.py`; rows `LGIC_CANON-W1-S2`, `W2-S1` and `W3-S1` in the
channel.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="L2-AC1" cell_refs="CN-l-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py l2-x6-axis</invocation><expect>PASS-L2-X6-ON-ITS-AXIS</expect></criterion>
`L2-AC1` -- X6's line names exactly one axis.
<criterion id="L2-AC2" cell_refs="CN-l-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py l2-utf8</invocation><expect>PASS-L2-RECOUNT-READS-UTF8</expect></criterion>
`L2-AC2` -- every open() in the recount script reads utf-8 explicitly.
<criterion id="L2-AC3" cell_refs="CN-l-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py l2-header</invocation><expect>PASS-L2-HEADER-REVERTED</expect></criterion>
`L2-AC3` -- section 7's header cell reads disposition, not disposition class.
<criterion id="L2-AC4" cell_refs="CN-l-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py l2-recount</invocation><expect>PASS-L2-COUNTS-REPRODUCED</expect></criterion>
`L2-AC4` -- the section's totals are reproduced by the instrument.
<criterion id="L2-J1" cell_refs="CN-l-2" judgment="true"/>
`L2-J1` -- graded at L9 by 3.0.0_SA_CVO: X6 is on the axis it actually excepts, and the header revert did not re-break the checker. RECORD; NO VERDICT.

<expected_criteria>L2-AC1, L2-AC2, L2-AC3, L2-AC4, L2-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_CANON/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are READ-ONLY.** `org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` holds round 2's checker `check_canon_r2.py` (every mechanical criterion calls it) and its inputs. Never edit any of them. ⚠ If a fixed input is itself DEFECTIVE, that is a BLOCKING surprise row and you keep your hands off it -- LGIC_ENFORCE round 2 lost an hour to a corrupt fixture, and the worker that filed a row instead of editing around it is the reason the defect was found in the fixture rather than papered over in the code.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure. Every `.py` you touch passes `.tools/commit-gate.sh` (safe-commit runs it).
- **Surprises** go to `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_CANON-W3-S<k>`. Keep working after filing. **Re-read the channel immediately before you write** -- rows land from other cells and an id minted from an earlier read collides silently. **`class` takes exactly TWO values, `OBSERVATION` or `BLOCKING`**; a third is refused by the corpus limb at `/class`, measured 2026-09-16.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it: commit the artifact first, then the proof in a later commit. Never `PENDING-THIS-COMMIT`.

<paths>
infra/logic/06_CONFORMANCE_LEDGER.md
org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/ledger_recount.py
org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md</decomp_doc> v4, cell `CN-l-2`, round 2 (section 0d).
<owned_cells>CN-l-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `L2-AC1`, `L2-AC2`, `L2-AC3`, `L2-AC4`, `L2-J1`. Instance at
`org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/LGIC_CANON.CN-l-2-r2.ledger-hygiene.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> L2-AC1,L2-AC2,L2-AC3,L2-AC4,L2-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `ledger-hygiene.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-2 cut 2026-09-16 -- --budget 540, WITHIN BUDGET, scanned 5 of 5 carriers in 300.7 s; REACHED-DENOMINATORS C1=276 C2=7 C3=12 C4=21 C5=334; GATES ARMED 26, and 0 of them names LGIC_CANON (grep count 0 over the run). Round 2's own gates are G-C (worker admission, checked at each spawn) and, for `CN-k-4` only, LGIC_NAMING's schema cell. NOT COUNTED, and the tool says so itself: C4 is SEMI-DECIDABLE and C5 NOT-DECIDABLE, so the 21 scope_guards and the 136 non-null `blocking` prose fields are a READING LIST rather than gates.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (the canon, the renderer, the checklist, the ledger, the recount script and records under deliverables/): no operation, policy, principal or resource is added.
comp-adversary: RUN at the recut on the round-1 analysis @26ae876d23 -- the analysis's cited commits and paths verified at the cut; blindness stated: the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). `infra/logic/**` is lane PLATFORM_LOGIC_DOCS and admits no COO by enumeration; a worker reaches it ONLY through this block, which is why every canon, renderer, checklist and ledger path this cell touches is named here explicitly.
write-surface: MEASURED at the cut. The `<paths>` of every non-terminal LGIC_NAMING and LGIC_ENFORCE order (15 orders, printed denominator) were intersected with this round's four write surfaces; the intersection is EMPTY. Internal contention is `CN-k-2` and `CN-k-4` on the canon, which share ONE slot sequenced.
</preflight>

Seating: slot ~3, queue position 1. Round 2 of LGIC_CANON, the recut of `1.0.0_SA_CTO`'s round-1 ANALYSIS (`org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23`, msg 97317) on `3.0.0_SA_CVO`'s L10 slug; issued by `2.0.0_SA_COO~G`, which holds LGIC_CANON under Andrew-direct 2026-09-16 ~05:2xZ. Decomposition v4 @2b987c131d, section 0d. Distinct-worker constraints: the three judges are blind to each other and to `CN-k-2`'s author; `CN-j-7` judged nothing; `CN-o-4`'s worker did not write `CN-o-3`.
