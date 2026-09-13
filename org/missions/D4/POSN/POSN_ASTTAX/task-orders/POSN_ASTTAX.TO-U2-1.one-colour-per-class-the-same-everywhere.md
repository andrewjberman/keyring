# TO POSN_ASTTAX.TO-U2-1 -- ONE colour per class, the SAME colour across every reader AT4-s-1 derived (AT4-s-2, FWD-4). READ-ONLY. THE PORTAL IS FROZEN

<to_id>POSN_ASTTAX.TO-U2-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~18</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-13</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.6**
@`ae66157381` - **Decomp cell:** `AT4-s-2` - **Issuance:** round 4. **DEPENDS ON `AT4-s-1`.**

---

## THE CELL

> ⛔ **ISSUER CORRECTION BEFORE SPAWN (2026-09-13 ~06:4xZ), FOUND BY `0.9.0_WK_POSN_ASTTAX~15` ON THE
> SIBLING ORDER AND FIXED HERE BEFORE IT COULD BITE A SECOND WORKER.** The `<proof_of_spec>` block
> first named the SHORT form `POSN_ASTTAX.TO-U2-1.proof_of_spec.json`. **The convention is the FULL TO
> FILENAME STEM, measured 12 of 12 over every POSN proof instance at HEAD**, and it is what the L6
> gate derives. `~15` deviated from the written path deliberately and said so; that was correct and
> the order was wrong. `TO-U3-1` and `TO-U4-1` still carry the short form and are NOT edited, because
> their workers are LIVE and changing a face mid-read is a silent modification a worker never sees
> refused -- they are handled at the drain instead.


**FWD-4, verbatim from the PRD v0.6 endpoint block: "Each class has one color, the same everywhere."**
Zero cells in three rounds. This is that cell.

**DO NOT START UNTIL `AT4-s-1` IS TERMINAL, AND USE ITS READER SET AS YOUR DENOMINATOR.**
Enumerating colour over a surface list you guessed is the wrong-domain failure this project has
already banked twice: a subtraction over the wrong domain arrives carrying a printed denominator and
therefore reads as MEASURED. **Your domain is `AT4-s-1`'s census, cited by its proof instance.**

**THE PORTAL IS FROZEN. READ IT, DO NOT WRITE IT.** Your `<paths>` grant holds no portal path.

---

## CRITERIA -- one clause each

**AC1 -- Enumerate every per-class colour binding, over AT4-s-1's reader set.**
**INVOCATION:** for each reader in that census, every place a class maps to a colour token, cited
`file:line @ <commit-ish>`.
**EXPECTATION:** a (reader, class, colour token) table, with the denominator -- readers scanned --
printed beside it.

**AC2 -- ONE colour per class: grade uniqueness WITHIN a class.**
**INVOCATION:** for each of the five ratified classes, collect every colour token bound to it.
**EXPECTATION:** the count per class. A class carrying two different tokens FAILS this clause; name
both values and their pins. Round 3 recorded two candidates worth CHECKING rather than trusting: a
Commodities colour aliased to Alternatives, and `'Structured'` against `'Structured Credit'`.

**AC3 -- THE SAME colour everywhere: grade agreement ACROSS readers.**
**INVOCATION:** for each class, compare its token across every reader in the census.
**EXPECTATION:** agree / disagree per class, with both values wherever they differ.
**A class that NO reader can display is not agreeing -- report it ABSENT, never as agreeing.** Two
readers that both cannot show Commodities agree about nothing, and scoring that as a pass is the same
defect FWD-6 was nearly graded on.

**AC4 -- Price the smallest change per failing cell**, at `file:line`, each row marked FROZEN (under
`portal/`) or OWNED.

**DO NOT claim FWD-4 REALIZED.** This cell covers the outcome; it does not serve it.

## SURPRISE ROWS

Off-cell findings: ONE row as `POSN_ASTTAX-W18-S<k>`, then keep working.

## CRITERIA -- structured, one clause each

<criterion id="U2-AC1" cell_refs="AT4-s-2"><invocation>timeout 300 python &lt;your colour-binding enumeration over AT4-s-1 census&gt;</invocation><expect>the (reader, class, colour token) table, with the DENOMINATOR -- readers scanned -- printed beside it, and the AT4-s-1 proof instance cited as the source of that denominator. Each binding cited file:line @ &lt;commit-ish&gt;.</expect></criterion> `U2-AC1` -- EVERY BINDING, OVER A DOMAIN YOU INHERITED RATHER THAN GUESSED.

<criterion id="U2-AC2" cell_refs="AT4-s-2"><invocation>timeout 180 python &lt;your per-class uniqueness count&gt;</invocation><expect>for each of the five ratified classes, every colour token bound to it and the COUNT. A class carrying two different tokens FAILS this clause -- name both values and both pins. Two round-3 candidates are to be CHECKED, never confirmed: a Commodities colour aliased to Alternatives, and Structured against Structured Credit.</expect></criterion> `U2-AC2` -- ONE COLOUR PER CLASS -- uniqueness WITHIN a class.

<criterion id="U2-AC3" cell_refs="AT4-s-2"><invocation>timeout 180 python &lt;your cross-reader agreement grade&gt;</invocation><expect>for each class, its token compared across every reader in the census: AGREE or DISAGREE, with both values wherever they differ. A class NO reader can display is reported ABSENT, never as agreeing -- two readers that both cannot show Commodities agree about nothing, and scoring that as a pass is the defect FWD-6 was nearly graded on.</expect></criterion> `U2-AC3` -- THE SAME COLOUR EVERYWHERE -- agreement ACROSS readers, with ABSENT kept distinct from AGREE.

<criterion id="U2-AC4" cell_refs="AT4-s-2"><invocation>timeout 120 python &lt;your pricing table&gt;</invocation><expect>per failing cell, the smallest change at file:line, marked FROZEN (under portal/) or OWNED, with both totals printed. Plus one explicit line: this cell COVERS FWD-4 and does NOT serve it. Do NOT grade FWD-4 REALIZED.</expect></criterion> `U2-AC4` -- THE PRICE, AND THE HONEST GRAIN.

<criterion id="U2-AC5" cell_refs="AT4-s-2" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether one colour per class, held the same across readers, is sufficient for FWD-4 as the PRD states it, or whether the outcome also requires the colour to be legible to a person on the rendered page. Record the readings and offer NO verdict.</expect></criterion> `U2-AC5` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>U2-AC1, U2-AC2, U2-AC3, U2-AC4, U2-AC5</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-U2-1.one-colour-per-class-the-same-everywhere.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~18/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round4.md</decomp_doc> round 4, cell `AT4-s-2`.
<owned_cells>AT4-s-2</owned_cells>
HARD dependency: `AT4-s-1` must be TERMINAL and its reader census is YOUR denominator -- cite its proof instance. Do not re-derive the reader set and do not widen it.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only; no job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; repository source reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied, THREE items: (1) the issuer has NOT measured any colour binding, and names the two round-3
candidates as things to CHECK, never as findings to confirm; (2) the portal is FROZEN so all evidence
here is SOURCE-AT-PIN; (3) if `AT4-s-1`'s census comes back narrower than the analysis's "at least
three", that is a finding for a surprise row -- it is NOT licence to widen the domain yourself.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~18/POSN_ASTTAX.TO-U2-1.one-colour-per-class-the-same-everywhere.proof_of_spec.json
</proof_of_spec>
