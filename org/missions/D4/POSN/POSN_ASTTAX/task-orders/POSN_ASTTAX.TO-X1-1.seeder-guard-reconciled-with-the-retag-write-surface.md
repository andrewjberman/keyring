# TO POSN_ASTTAX.TO-X1-1 -- THE SEEDER GUARD RECONCILED WITH THE RETAG'S WRITE SURFACE: the guard owns exactly the fields the seeder writes (3 of 3), `management_style` is outside the seeder's reach and VNQ is not a seeder record -- STATED in the file, ASSERTED at import, PROVED by exercise on the scratch harness (AT7-s-1; C-S177, FWD-5)

<to_id>POSN_ASTTAX.TO-X1-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~27</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.11** @`ab2ee8052a` (C-RETAG-SAFETY,
C-RETAG-SET; no addendum) - **Decomp cell:** `AT7-s-1` - **Issuance:** round 7, the only cell, cut after the 13:00Z promote (the CTO's
L10 @`e60bf6dca1`, msg 23119).

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~27`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~27;`. Your worktree is
`/c/tmp/wk-posn-7-27` (branch `wk-posn_asttax-7-27`, a sparse cone cut by the COO; do NOT re-create it). First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Commit ONLY via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~27 <0.9.0_WK_POSN_ASTTAX~27@opal.agent>" -F <msgfile> -- <paths>` (the msgfile
by the Write tool, PURE ASCII). Every `.py` edit passes `.tools/commit-gate.sh`. Never push, merge, rebase, `checkout --`, `clean`.
**NEVER run the seeder against the live tables: `--upload` is never passed in this cell; the scratch harness replaces boto3 before any
seeder byte executes** (V3's `deliverables/0.9.0_WK_POSN_ASTTAX~21/v3_mutant_control_re.py`, read it whole first).

## THE CELL

`3.0.0_SA_CVO~Z`'s L9 graded round 5's V3-AC7 FAIL -> `C-S177` (DECOMP_INVALIDATING): *"the V3 guard-owned field tuple does not equal the
R1 write surface: name is guard-only and management_style is R1-only."* The CTO's L10 cell: *"adds management_style to the owned tuple
(or states, measured, why a reseed cannot write it) and a criterion that runs the guard against a reseed changing ONLY VNQ's
management_style and reads the refusal."*

**Measured at HEAD by the issuer (~10:2xZ) -- read it back, never trust this text:** `data/black_diamond/scripts/classification/seed_canonical_securities.py`
(351 lines): `YANG_OWNED_FIELDS = ('asset_class', 'sub_asset_class', 'name')` :210; `_yang_conflicts()` :213-231; `seed()` :234-336;
**the seeder's ENTIRE Yang write is `yang_table.update_item(... UpdateExpression='SET asset_class = :ac, sub_asset_class = :sac, #n = :n,
last_updated = :ts, updated_by = :ub' ...)` :303-315** -- an UPDATE that SETS the three owned fields plus two audit fields and nothing
else; the docstring :14 says every unowned field (it names `management_style`) is preserved; the records :46-206 carry `ticker,
asset_class, sub_asset_class, name` and NO `management_style`; **VNQ is not a seeder record** (0 occurrences). Therefore a reseed cannot
write, clear or revert `management_style` and cannot touch VNQ; the guard's tuple equals the seeder's write surface 3 of 3. Adding
`management_style` to the tuple would `KeyError` on every record (or compare a live value against nothing) -- a vacuous check that
reads as protection. **This cell takes the CTO's parenthesis:** state it in the file, assert it at import, prove it by exercise.

**Your act:**
1. `seed_canonical_securities.py`, at :206-210: extend the comment above `YANG_OWNED_FIELDS` with the MEASURED write surface -- the SET
   clause's fields are exactly the owned tuple; `management_style` (R1's write, `TO-V8-1` V8-AC4 on VNQ) and every other field outside
   the clause are never written, cleared or compared by this seeder; VNQ is not a record here. Beside the tuple add ONE module-level
   assertion that fails loudly at import if the two surfaces ever diverge: parse the owned field names out of the `UpdateExpression`
   string (the identifiers before ` = :` in its `SET` list, `#n` resolved to `name` through `ExpressionAttributeNames`, the two audit
   fields `last_updated` / `updated_by` excluded by name) and `assert set(...) == set(YANG_OWNED_FIELDS)`. Implement it so the
   expression string is defined ONCE (a module constant the `update_item` call and the assertion both read) -- no second copy of the
   string. Nothing else in the file changes; no record changes; the seeder's behaviour on every input is byte-identical (X1-AC2's
   agree-arm proves the write still happens and X1-AC1 proves the surface).
2. The exercise `<SCRATCH_EXERCISE_X1>` (a script in your deliverables dir) on V3's harness (import its scratch table / fake boto3
   definitions by path, never re-derive them; assert the harness bytes' sha256 as V3 did): seed a scratch Yang table with
   (a) `QBER {asset_class: structured, sub_asset_class: Hedge, name: <the seeder's>, management_style: active}` (the seeder asserts
   `fixed_income / Volatility` -> the guard REFUSES), (b) a seeder ticker whose classes AGREE with the seeder's record, carrying
   `management_style: passive` (-> WRITTEN: `last_updated`/`updated_by` move), (c) `VNQ {alternatives, Real Estate, name, management_style
   passive}` (not a record -> never visited); run the seeder with `--yang --upload` against the SCRATCH table (the fake boto3 prints the
   intercepted table name) and print each row BEFORE and AFTER; then the NEGATIVE CONTROL: the same run with the harness's SET clause
   mutated to append `, management_style = :ms` (a scratch copy of the seeder bytes, never the working tree) -- the field MOVES on row (b),
   proving the instrument can see a management_style write. Never `--force`.
3. Record every criterion in the proof instance; file rows `POSN_ASTTAX-Z-W27-S<k>` for anything off-cell; keep working.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W27-S<k>` (start at S1; class OBSERVATION or BLOCKING only; pure ASCII), appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="X1-AC1" cell_refs="AT7-s-1"><invocation>timeout 120 bash -c "PYTHONUTF8=1 python3 -c \"import re,sys; src=open('data/black_diamond/scripts/classification/seed_canonical_securities.py',encoding='utf-8').read(); m=re.search(r'UpdateExpression=\\(?\\s*\\(?\\s*[\\'\\\"]SET ([^\\'\\\"]+)', src); print('SET clause:', m.group(1) if m else None); ns=re.findall(r'^YANG_OWNED_FIELDS\\s*=\\s*\\((.*?)\\)', src, re.M); print('tuple:', ns); print('management_style in SET:', 'management_style' in (m.group(1) if m else '')); print('management_style in records:', len(re.findall(r'\\'management_style\\'\\s*:', src)))\"; PYTHONUTF8=1 python3 -c \"import importlib.util,sys; spec=importlib.util.spec_from_file_location('s','data/black_diamond/scripts/classification/seed_canonical_securities.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); print('import OK; owned', m.YANG_OWNED_FIELDS)\""</invocation><expect>the SET clause names asset_class, sub_asset_class, #n (name), last_updated, updated_by and nothing else; the tuple reads ('asset_class', 'sub_asset_class', 'name'); management_style in SET: False; management_style in records: 0; the module IMPORTS (the assertion passes on HEAD's bytes) and prints the tuple. POSITIVE CONTROL for the assertion: a scratch copy of the file with the tuple reduced to two fields (or the SET clause given a fourth owned field) FAILS to import with the assertion's message -- printed.</expect></criterion> `X1-AC1` -- THE WRITE SURFACE EQUALS THE OWNED TUPLE, READ FROM THE BYTES; THE ASSERTION CAN FIRE.

<criterion id="X1-AC2" cell_refs="AT7-s-1"><invocation>timeout 600 bash -c "PYTHONUTF8=1 python3 <SCRATCH_EXERCISE_X1>"</invocation><expect>the scratch target's name PRINTED by the fake boto3 (the live tables never opened; no network client constructed); row (a) QBER: REFUSED ([PRESERVED] asset_class and sub_asset_class, rc 1 for the run) and its management_style 'active' byte-identical after; row (b): WRITTEN (last_updated and updated_by moved) and its management_style 'passive' byte-identical after; row (c) VNQ: never visited, bytes before == after; the NEGATIVE CONTROL (the mutated SET clause on a scratch copy of the seeder bytes) MOVES row (b)'s management_style -- the pair differs, so the equality above is a measurement. Every row printed before and after with its full item.</expect></criterion> `X1-AC2` -- A RESEED CANNOT MOVE management_style, PROVED ON BOTH ARMS, WITH AN INSTRUMENT THAT CAN SEE ONE.

<criterion id="X1-AC3" cell_refs="AT7-s-1"><invocation>timeout 180 bash .tools/commit-gate.sh data/black_diamond/scripts/classification/seed_canonical_securities.py</invocation><expect>clean on the ONE changed .py (py_compile + ds-precommit + ruff py39); the cross-firm limb's reading quoted (the file's home dir is data/black_diamond/ -- the limb fires on foreign bucket/prefix names only; state the count it printed).</expect></criterion> `X1-AC3` -- THE GATE ON THE CHANGED .PY.

<criterion id="X1-AC4" cell_refs="AT7-s-1"><invocation>timeout 60 bash -c "PYTHONUTF8=1 python3 -c \"p='data/black_diamond/scripts/classification/seed_canonical_securities.py'; b=open(p,'rb').read(); print(p, len(b)-len(b.decode('utf-8'))); c=open('CLAUDE.md','rb').read(); print('CLAUDE.md', len(c)-len(c.decode('utf-8')))\""</invocation><expect>the seeder prints 0 (pure ASCII) and CLAUDE.md prints a number greater than 0 -- the firing control (C-S92).</expect></criterion> `X1-AC4` -- ASCII, BY AN INSTRUMENT THAT CAN FIRE.

<criterion id="X1-AC5" cell_refs="AT7-s-1"><invocation>timeout 120 bash -c "for t in VNQ QBER; do .tools/aws dynamodb get-item --table-name etf-classifications --key '{\"ticker\":{\"S\":\"'\$t'\"}}' --projection-expression 'ticker, asset_class, sub_asset_class, management_style, last_updated' --output json; done"</invocation><expect>two items, each IDENTICAL to the same read taken BEFORE X1-AC2 ran (paste both reads): VNQ alternatives / Real Estate / management_style unchanged; QBER structured / Hedge / active -- the live table did not move during this cell (point reads under the operator identity; no scan).</expect></criterion> `X1-AC5` -- THE LIVE TABLE, UNTOUCHED, PROVED BY A BEFORE/AFTER POINT READ.

<criterion id="X1-AC6" cell_refs="AT7-s-1"><invocation>timeout 60 git diff --stat HEAD~1 -- data/black_diamond/scripts/classification/seed_canonical_securities.py</invocation><expect>ONE file; the diff carries the comment lines, the expression constant and the assertion ONLY -- no record changed, no behaviour line changed (print the diff; a changed record or a changed SET field is a refusal of this criterion, not a fix).</expect></criterion> `X1-AC6` -- THE CHANGE IS STATEMENT AND ASSERTION, NOTHING ELSE.

<criterion id="X1-AC7" cell_refs="AT7-s-1" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether "the guard owns exactly what the seeder writes, and management_style is outside the seeder's reach" is the reconciliation C-S177 asked for; and whether R1's management_style write (the retag script's, on VNQ) wants a guard of its own in THAT script -- a place no seeder can defend -- for the next retag. Record the readings and offer NO verdict.</expect></criterion> `X1-AC7` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>X1-AC1, X1-AC2, X1-AC3, X1-AC4, X1-AC5, X1-AC6, X1-AC7</expected_criteria>

<placeholders>SCRATCH_EXERCISE_X1</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-X1-1.seeder-guard-reconciled-with-the-retag-write-surface.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~27/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
data/black_diamond/scripts/classification/seed_canonical_securities.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round7.md</decomp_doc> round 7, cell `AT7-s-1`.
<owned_cells>AT7-s-1</owned_cells>
Read-dependencies, NOT claimed: `AT5-s-3` (V3's guard and scratch harness), `AT5-s-8` (R1's writes, the surface compared against).
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no deploy, no schedule, no served key; the seeder is never run against a live table in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy; X1-AC5's point reads run under the operator identity and write nothing.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer has not run V3's harness against a scratch row that carries fields outside the seeder's records -- if the fake table's update_item ignores SET semantics (replaces the item), the harness itself would clobber management_style and the negative control would not discriminate; measure the harness first and file a row; (2) whether ds-precommit's cross-firm limb objects to a module-level assertion that parses a string is unread -- the gate is the instrument; (3) the issuer's regex in X1-AC1 was written against the expression as it reads today at :305-307; if the constant you introduce changes its shape, run the same read against the constant and state it.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~27/POSN_ASTTAX.TO-X1-1.seeder-guard-reconciled-with-the-retag-write-surface.proof_of_spec.json
</proof_of_spec>
