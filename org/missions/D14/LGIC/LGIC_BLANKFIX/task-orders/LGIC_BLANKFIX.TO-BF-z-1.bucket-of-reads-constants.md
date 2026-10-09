# TO LGIC_BLANKFIX.TO-BF-z-1 -- round 11 BF-z-1: bucket_of reads the bucket a Python file names in an s3:// URI constant or a named bucket constant

<to_id>LGIC_BLANKFIX.TO-BF-z-1</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>~B1</workstream>

**Directive:** D14 | **Fabric:** dell1 | **Decomp cell:** `BF-z-1` (`decompositions/LGIC_BLANKFIX_DECOMP.round11.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**Where the project stands.** `python lib/opal_naming.py census --all-roots` (the same as `python lib/opal_naming_rootcheck.py all
--map infra/logic/registry/root_map.json`) runs every Terraform root the root map covers and prints the denominator of roots
first; `infra/logic/README.md` "Run the naming check" explains its lines and fields. At this cut, on the base your worktree is
made from, it reads: `ALL-ROOTS ok=True roots_total=88 mapped=78 unmapped=10 completed=78 stopped=0 items=2271 right=566 fix=1460 not_asked=222 pattern=23 carded=0 refused=0 hole=0 carded_class_holes=0 source_bucket_holes=0 event_rule_holes=0 unknown_word_holes=0 other_holes=0 stale_hints=0 uncounted=1 counted_at_caller=17`. The round-10 close is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round10.txt`. The CTO's reading of round 10 is `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round10.md` -- read it first; its
ruling R1 is this cell. The round-10 drain end is `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~B1/ROUND10_DRAIN_END.md`.
Modules, under `lib/`: `opal_naming.py` (`grade`, `census_repo`, the `census` command), `opal_naming_scope.py` (the roots, their
names, `root_items`, the UNCOUNTED reader and `UNCOUNTED_REASONS`), `opal_naming_rootmap.py`, `opal_naming_cadence.py`,
`opal_naming_keyfill.py`, `opal_naming_policyrole.py`, `opal_naming_rootcheck.py` (`decide`, `place`, `check_root`, `_ruling_of`,
`all_roots`, `HOLE_OWED`, the `lines`, `keys` and `all` commands). The gates: `.tools/naming-gate.py` (commit time),
`.tools/naming-apply-gate.py` (plan time), called by `.tools/safe-commit.sh` and `.tools/safe-apply.sh`. The registry is
`infra/logic/registry/`; only `4.0.0_SA_CRO` writes it. Read the modules your cell touches or calls before you build. Import with
`sys.path.insert(0, "lib")`. Python 3.9 syntax only; ASCII only in code and output; no new dependency; no AWS call and no network
call. The bar: `python -m pytest lib/tests -q -p no:cacheprovider` passes whole at the base (193 passed, 1 skipped), and every
`lib/tests/test_opal_naming_*.py` script prints `ok=True` at the base except `test_opal_naming_rootcheck.py`, which reads
`ROOTCHECK-TEST ok=False` there on case 5 only (row S12; cell BF-x-2, first on slot ~1, repairs it). None may newly fail after your
build. A test you write
asserts relations and the rows it needs by name, never a typed total of repository names, roots or registry rows: those move
every day, and the registry's lane may add rows during this round. **The switch file `org/mcp/naming-place.enforce` is PRESENT since
@4d2bfc6dfd:** the placement refusal is live on every commit and apply. No cell deletes, moves or edits it; exercise the gates
only in a temporary copy, and never write a real override audit row.

### THE CELL

`BF-z-1` (ruling R1 in `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round10.md`; row LGIC_BLANKFIX-D1-W2-S4). `lib/opal_naming_keyfill.py` `bucket_of` / `_bucket_of_read` /
`_bucket_of_py` reads the WRONG bucket for four keys, so four correct drafted registry rows are dropped on the bucket mismatch. The four
are the `OWNED ... || 1.0.0_SA_CTO ||` lines of `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/HOLES_OWNED_round10.md` -- read them; each names the key, the bucket read today and the
bucket the code uses, with the file:line that decides it:
- `ec2/astn-wsjft/deploy.sh` and `ec2/etfs-reports`: the code's bucket is `opal-313476888478-lambda-artifacts`, in an `s3://` URI constant
  (`infra/aws/lambda/astn-wsjft-orchestrator/lambda_function.py:61`, `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py:53`);
- `contract_integrity/latest.json` and `warehouse/_branch_head.main.json`: the code's bucket is the constant
  `GLOBGRPH_BUCKET = opal-313476888478-globgrph` (`infra/aws/lambda/infrastructure_monitor/lambda_function.py:124-127`).
The drafted rows that drop are in `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/REGISTRY_ROWS_round10.json`.

**Build** in `lib/opal_naming_keyfill.py` (and its test) only:
1. The Python reader recognises a bucket given as the host of an `s3://<bucket>/...` string constant and a bucket held in a
   module-level name assigned a bucket literal (as `GLOBGRPH_BUCKET`), when that is the bucket the key is used with; the four keys
   then read their right bucket. A bucket the item already carries still comes first; the folder name is still never read.
2. Cases in `lib/tests/test_opal_naming_keyfill.py`: the four keys, each read from its real file, return their right bucket. The
   NEGATIVE arm: a key in a file that shows several bucket candidates and whose use picks none still returns None with the
   candidates listed -- never a guess.
3. Write `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_bucket_of_round11.py`: it reads the four OWNED lines, runs `bucket_of` on each key at its real file, merges the
   drafted rows of `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/REGISTRY_ROWS_round10.json` for those keys into a temporary copy of `infra/logic/registry/`, and prints one line per key
   (bucket before -> after) then last: `BUCKET-OF ok=True keys=4 right=4 rows_kept=N negative_held=True`.

### ACCEPTANCE

<criterion id="BZ1-AC1" cell_refs="BF-z-1"><invocation>python lib/tests/test_opal_naming_keyfill.py</invocation><expect>KEYFILL-TEST ok=True</expect></criterion>
`BZ1-AC1` -- the four keys read their right bucket; a key with several candidates and no pick still returns None.

<criterion id="BZ1-AC2" cell_refs="BF-z-1"><invocation>python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/check_bucket_of_round11.py</invocation><expect>BUCKET-OF ok=True</expect></criterion>
`BZ1-AC2` -- the four dropped rows now match their key's bucket on a registry copy.

<expected_criteria>BZ1-AC1,BZ1-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource;
  `org/mcp/naming-place.enforce` is never deleted or edited.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-D1-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; a row filed on dell1 carries the `-D1-` coordinate
  or the row gate refuses it) in the investigation file, and do not weaken the test or the expected value. A fact in this order that
  the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_keyfill.py
lib/tests/test_opal_naming_keyfill.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside the block: in particular every file under
`infra/logic/registry/`, the saved runs and traces, `org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round10.md`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round11.md`, and the `lib/` modules and `.tools/` scripts your block does
not name.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.round11.md</decomp_doc> (round 11), cell `BF-z-1`.
<owned_cells>BF-z-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BZ1-AC1, BZ1-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~1/LGIC_BLANKFIX.TO-BF-z-1.bucket-of-reads-constants.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BZ1-AC1,BZ1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines whole; each key's bucket before and after; rows kept; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE the cell grants, attaches and simulates nothing, and calls no AWS API.
comp-adversary: RUN -- a guessed bucket (the negative arm keeps several-candidates-no-pick at None); the folder name read as a bucket; an s3:// constant from another function taken for the key's (the four real files are the tests); BLIND: buckets built at run time from environment variables.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round10.md (`1.0.0_SA_CTO~DELL1`, msg 2207), item R1 (row D1-W2-S4); decomposition round 11. Base dry-run at the cut, by the
issuer at base 5c65160327: BZ1-AC1 base: PASS as expected (ran: KEYFILL-TEST ok=True cases=86; extended by the cell with the four keys and the negative arm); BZ1-AC2 base: FAIL as expected (file absent; the four keys read the wrong bucket per HOLES_OWNED_round10.md).
