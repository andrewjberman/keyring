# TO LGIC_BLANKFIX.TO-BF-q-3 -- round 4 BF-q-3: a filled name passes the same cross-firm check as a read name

<to_id>LGIC_BLANKFIX.TO-BF-q-3</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-q-3` (`decompositions/LGIC_BLANKFIX_DECOMP.round4.md`) | **outcome_ref:** FWD-1, FWD-4 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --root ROOT` prints one line per name of a Terraform root:
`KIND type current -> detail  [where]`, kinds `RIGHT`, `FIX`, `NOT-ASKED`, `PATTERN`, `CARDED`, `REFUSED`, `HOLE`; it exits 1 while
any line is a `HOLE`. Round 3's runs are saved: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round3_bd-pipeline.txt` (140 names: 114 fix, 12 not
asked, 9 right, 3 pattern, 2 refused, 0 holes) and `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/SECOND_ROOT_TRACE_round3_investor-reporting-directory.txt`
(17 names: 13 right, 2 fix, 2 holes). The CTO's reading of both is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round3.md` -- read it first.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the source-literal classifier), `opal_naming_scope.py`,
`opal_naming_rootmap.py`, `opal_naming_cadence.py`, `opal_naming_keyfill.py` (`fill_keys`, `bucket_of`),
`opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `check_root`, `map_key`; it reads
`infra/logic/registry/key_rulings.json`). The registry is `infra/logic/registry/`; the root map is `infra/logic/registry/root_map.json`.
Read the modules your cell touches or calls before you build. Import with `sys.path.insert(0, "lib")`. Python 3.9 syntax only;
ASCII only in code and output; no new dependency; no AWS call and no network call. The bar for the library:
`python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (194 passed); no test may fail after your build.

### THE CELL

`BF-q-3`. Row `LGIC_BLANKFIX-W1-S8`: when a root's map entry carries `fills` (it serves more than one firm, so the entry may
supply a system and never a firm), round 3's `fill_keys` SKIPS the two cross-firm checks for that root -- the bucket's firm
against the root's, and a path word naming another firm -- on the reasoning that there is no home firm to compare with.
`1.0.0_SA_CTO`: a filled name passes the same cross-firm check as a read name.

**Build** in `lib/opal_naming_keyfill.py`:
1. The cross-firm checks no longer depend on `fills`. What a stored file's firm is compared WITH is the firm of its own bucket
   (read from the registry, as today), not the root entry's scope: a key whose path word names a firm other than its bucket's
   firm is `REFUSED-CROSS-FIRM` on any root; and an address the reader FILLS (class `ADDRESS`) is checked the same way after
   the fill -- the firm written into the filled address must be the firm of the key's bucket, or the row is
   `REFUSED-CROSS-FIRM` with both firms named.
2. Where the key's bucket was not read, the path-word check falls back to the root entry's scope when the entry may give one
   (no `fills`, or `fills` lists `scope`), and otherwise the row keeps its class with a `basis` that says the firm could not be
   checked and why.
3. Extend `lib/tests/test_opal_naming_keyfill.py`: the DIFFERENCE CONTROL: under an entry with `fills: ["system"]`, a key whose
   path names a firm other than its bucket's firm is `REFUSED-CROSS-FIRM`, and the same key whose path names the bucket's own
   firm is not; a filled address whose firm differs from its bucket's firm is refused. Last line `KEYFILL-TEST ok=True cases=N`.
4. A command `python lib/opal_naming_keyfill.py crossfirm --map PATH`: over every root the map covers, each stored file with its
   bucket, the firm of that bucket, the firm its path or filled address names, and the verdict; last line
   `KEYFILL-CROSSFIRM ok=True roots=N keys=N checked=N unchecked=N refused=N`, `ok=True` when `checked + unchecked == keys` and
   every unchecked key carries its reason.
The two `bd-pipeline` lines for `code/bronze/cot_bronze_ingest.py` must still print `REFUSED` after your build (another cell
changes them on a registry ruling): report what they print.

### ACCEPTANCE

<criterion id="BQ3-AC1" cell_refs="BF-q-3"><invocation>python lib/tests/test_opal_naming_keyfill.py</invocation><expect>KEYFILL-TEST ok=True</expect></criterion>
`BQ3-AC1` -- the cross-firm check holds under `fills`, and a filled firm is checked against the bucket's.

<criterion id="BQ3-AC2" cell_refs="BF-q-3"><invocation>python lib/opal_naming_keyfill.py crossfirm --map infra/logic/registry/root_map.json</invocation><expect>KEYFILL-CROSSFIRM ok=True</expect></criterion>
`BQ3-AC2` -- every stored file of every mapped root is checked or says why it could not be.

<expected_criteria>BQ3-AC1,BQ3-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_keyfill.py
lib/tests/test_opal_naming_keyfill.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under `infra/logic/`, the two saved traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round3.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md`, and the `lib/` modules your block does not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round4.md</decomp_doc> (round 4), cell `BF-q-3`.
<owned_cells>BF-q-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BQ3-AC1, BQ3-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-q-3.filled-name-cross-firm.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BQ3-AC1,BQ3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; per root the keys refused and unchecked with reasons; what the two bd-pipeline lines print; the suite's last line; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a multi-firm root's keys silently unchecked (the crossfirm command counts unchecked and requires a reason for each); a 49 Financial key refused because the ROOT serves two firms (the comparison is with the key's own bucket); a check that reads AWS (the face forbids it); BLIND: a bucket passed in at run time, which another cell of this round reads.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round3.md @f0e6411e53 (the CTO's enrichment list); decomposition round 4. Base dry-run at the cut: BQ3-AC1 base PASS as expected (ran: KEYFILL-TEST ok=True cases=28; extended by the cell); BQ3-AC2 base FAIL as expected (ran: no such command).
