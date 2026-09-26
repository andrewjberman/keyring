# AMGT_CORPUS task order -- `CRPS-i-4` -- ROUND 7: a standing census proves no glob or fnmatch pattern under lib/research is built from a security key, so the literal `*` in WALMEX*_MM_Equity cannot silently widen one

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-i-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~4</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a static code census.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~4`**, slot `~4` of round 7. Serves the key-space exposure in row `Z-S39`.

## 1. THE CELL -- `CRPS-i-4`

**Where this came from.** Three of the 89 Base-case security keys carry a shell/glob metacharacter: `BP/_LN_Equity` and
`NG/_LN_Equity` (a literal `/`) and `WALMEX*_MM_Equity` (a literal `*`). The `/` is escaped as `-SLASH-` on the S3 paths
(`lib/research/identity/crosswalk.py`, `slash_safe_key`); nothing escapes the `*`. A `*` fails silently rather than loudly: any
`glob`, `fnmatch` or shell path built by interpolating that key WIDENS to other keys. When the row was filed there were zero
such call sites; nothing keeps it that way.

**RULED -- what you build:**
- `lib/research/corpus/key_glob_census.py` (new, read-only, standard library `ast` only): walk every `.py` file under
  `lib/research/`, find each call to `glob.glob`, `glob.iglob`, `fnmatch.fnmatch`, `fnmatch.fnmatchcase`, `fnmatch.filter`,
  `<Path>.glob` and `<Path>.rglob`, and flag a call whose PATTERN argument is built from a security key: a name or attribute
  containing `security_key` or ending `_key`, directly or through an f-string, `%`, `+`, `.format` or `os.path.join` that
  contains one. Print `glob_sites <n> key_derived <k> files_scanned <f>`, then one line
  `key_derived_site <path>:<line> <call>` per flagged call. Exit 0 only when `key_derived` is 0.
- `--plant` writes one module with a key-derived `glob.glob(f"{security_key}*.json")` into a temporary directory, scans it, and
  prints `plant_flagged 1` (0 is a failed control); it never writes inside the repository.
- `lib/research/corpus/tests/test_key_glob_census.py` (new): a key-derived pattern is flagged for each call form; a constant
  pattern is not; the plant control flags.

## 3. SURFACES

<paths>
lib/research/corpus/key_glob_census.py
lib/research/corpus/tests/test_key_glob_census.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-i-4.key-glob-census.md
</paths>

READ-ONLY: every other module. Scratch `.scratch/i4/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible, standard library only. No key is renamed or re-escaped; if the live census finds a
  key-derived site, report it and file a row rather than editing the site.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W4-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-i-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i4_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-i-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i4_AC2.sh</invocation><expect>(?m)^glob_sites \d+ key_derived 0 files_scanned [1-9]\d*$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-i-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i4_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: the live census over `lib/research` prints zero key-derived patterns with its
  denominator; AC3 the bound: the corpus suite still passes.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/AMGT_CORPUS.TO-CRPS-i-4.key-glob-census.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's line and the `--plant` line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-6 analysis s.6 item 5 @`1e53f322f3`; row Z-S39 (the CVO's) and its note that the remedy is a guard, not
a re-open. The key space itself is the identity layer's (shared with AMGT_RESAPP); this cell guards the use site only.
Checks dry-run at the base: AC1 FAIL (no such file), AC2 FAIL (no such module), AC3 bound.

<risk>LOCAL</risk>
<status>pending</status>
<round>7</round>
<slot>~4</slot>
<fabric>site-z</fabric>
