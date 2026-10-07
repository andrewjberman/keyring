# AMGT_RESAPP task order -- `AMGT-ba-15` -- THE IDENTITY GRADING READ (KEYED N OF 89, EVERY RESIDUAL NAMED, CORPUS AS THE ONE RESOLVER) AND THE ONE PAGER PRECEDENCE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-15</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~281</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; two pure modules, their tests and one read.
comp-iam: DECLARED-NOT-APPLICABLE -- reads the served crosswalk object and the holdings plane this seat already reads, and the research library on this device; no write to any store.
comp-adversary: RUN by the issuer at the cut -- the premise "33 of 89 keyed" is the 2026-09-10 coverage SNAPSHOT's ticker cell (34 MEASURED, 55 UNRESOLVED of 89 at the cut). The SERVED crosswalk (`s3://opal-data-harvest/crosswalk/v1/2026-09-29.json`: 237 records, 96 with a folder, all 96 keyed) already keys 89 of 89 coverage folders. CORPUS's `_registered_security_keys()` returns 96; `covered_security_keys()` returns 95. So this cell MEASURES and names; it does not resolve a second time. r77_ba15 AC1, AC2 and AC3 FAIL at the base (neither module exists).
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r77-281` (branch `wk-AMGT_RESAPP-281`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-281`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-15` (round 77, decomposition s.85)

The CTO's ruling (`ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` @4a89bef967, section A; rows Z-S117, Z-W7-S3, Z-W19-S6, Z-W20-S12, Z-W21-S4), in its words:

1. The grading denominator is the 89 covered crosswalk records. The keyed count is printed beside it. The 256-name union is
   NOT a grading denominator. Its unkeyed members read UNRESOLVED with a reason.
2. ONE resolving cell. It joins the unkeyed covered records to AMGT_CORPUS's registered security keys
   (`model_block_pull._registered_security_keys()`), by research folder and name. CORPUS already resolved these folders, so
   RESAPP reads that answer and does not resolve a second time. No vendor call. Proof: keyed N of 89 printed, and every
   residual named with its reason. Control: a name CORPUS does not hold stays UNRESOLVED.
3. Holdings identifiers (167 of 170 with no CUSIP/FIGI/SEDOL join, row Z-W19-S6): the tri-state stays (`held None`). After
   the resolving cell, membership is re-read. A residual that needs a vendor identifier map comes back as ONE row with its
   count. It is not built speculatively.
4. DE (row Z-W20-S12) resolves if CORPUS holds it. Otherwise it stays with its plain reason.

And section E, row Z-W3-S1 (two ONE PAGER workbooks in one folder, no precedence): the workbook with the newer stored
modified date is read. The other is listed as superseded, with its date, on the same line.

**What the issuer measured at the cut, which sets the size of this cell:** the served crosswalk already keys 89 of 89
coverage folders (see the preflight). The "33 of 89" is the stale snapshot. So build the READ that prints the ruled
denominator and proves it, and resolve through CORPUS only what the served crosswalk does not key.

**Build, with these names (the checks call them):**

1. **`lib/research/identity/covered_keyed.py`, new.**
   - `grade(crosswalk_document, coverage_document, corpus_records) -> dict`, pure. The denominator is
     `len(coverage_document["names"])`. A coverage folder is keyed when the crosswalk holds a record whose
     `source_row.folder` is that folder and which carries a `security_key`. A folder the crosswalk does not key is keyed
     ONLY when `corpus_records` (a list of `{folder, security_key}`; `None` means CORPUS was not read) holds a record for
     that same folder with a key; it is then counted with basis `corpus`. Anything else is a residual
     `{folder, reason}` in plain words. Return `denominator`, `keyed`, `keyed_by` (`{crosswalk: n, corpus: n}`),
     `residual`, and `corpus` (`{read: bool, records: n, reason}`). keyed + len(residual) == denominator, always.
   - `run() -> dict`: the same grade over the SERVED crosswalk (`crosswalk.load_crosswalk()`), the coverage list
     (`crosswalk.coverage_path()`) and CORPUS's own answer (`lib.research.corpus.backlog.build(library.library_root())`
     records, the function `integrations/bloomberg/research/model_block_pull.py:_registered_security_keys` reads; READ it,
     do not copy or edit it). It adds `crosswalk_loaded_from`. If the research library cannot be read on this device,
     `corpus.read` is False with the reason and nothing is resolved through it.
   - `python -m lib.research.identity.covered_keyed` prints `keyed N of 89 (crosswalk n, corpus n)`, then one line per
     residual, then whether `DE_US_Equity` is among CORPUS's keys (ruling item 4).
2. **The holdings re-read (ruling item 3), a reported figure, no build.** After `run()`, read the U-1 universe the way
   `lib/research/posture/membership.py` reads it and count holding rows that carry no resolved key. Write the count and
   the denominator into `GRADING_READ.md` in your deliverables. If a residual remains that only a vendor identifier map
   could join, file ONE row with its count. Do not build a map.
3. **`lib/research/identity/one_pager_precedence.py`, new, pure.**
   - `ordered(folder_path, filenames) -> list`: the same filenames, the one with the NEWEST stored modified date
     (the file's own modified time in the research library) first. One file is returned as it is.
   - `line(folder, folder_path, filenames) -> str`: ONE line naming the workbook that is read with its modified date
     (YYYY-MM-DD), then every other workbook as superseded, each with its date.
   - Do NOT edit `lib/research/identity/build_universe.py`. Its `_find_one_pager_files` returns the files in name order
     today (`:135-145`); the one-line hookup that makes it return `one_pager_precedence.ordered(...)` is added by the issuer
     at the merge. Name that hookup in your report. Then list, in `GRADING_READ.md`, every coverage folder that carries two
     or more ONE PAGER workbooks today, each with the line `line()` gives it (the row measured 5 of 89).
4. **Plant tests** beside the modules: `tests/test_covered_keyed.py` and `tests/test_one_pager_precedence.py`.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W281-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No pool write, no crosswalk build or publish, no edit to `registrations.json`, `crosswalk.py` or `build_universe.py`. No deploy, no vendor, SEC or model call, no portal write.
2. No second resolver: a folder is keyed by the served crosswalk or by CORPUS's own record for that folder, and by nothing else. No name matching of your own.
3. Read-only on the research library. Do not open, move or rewrite a workbook; the modified date is read from the file system.
4. Any reason you write is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger in a reason a page could show.
5. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/identity/covered_keyed.py
lib/research/identity/one_pager_precedence.py
lib/research/identity/tests/test_covered_keyed.py
lib/research/identity/tests/test_one_pager_precedence.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~281/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-15"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba15.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>C0-C4 PASS: the denominator is the coverage list, keyed 3 of 4 with one through CORPUS, the folder CORPUS does not hold stays out with its reason, and nothing resolves through an unread CORPUS; R77 BA15 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-15"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba15.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>on the served crosswalk: the denominator is 89, keyed + residual = 89 with keyed 33 or more, every residual named with a reason; C0-C3 PASS; R77 BA15 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-15"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba15.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>C0-C3 PASS: the newer stored modified date is read first whatever the names say, and the other workbook is on the same line as superseded with its date; R77 BA15 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~281 <0.9.0_WK_AMGT_RESAPP~281@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~281/AMGT_RESAPP.TO-AMGT-ba-15.identity-grading-read-and-one-pager-precedence.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- keyed N of 89 with the split (crosswalk, corpus), every residual, and DE's state;
- the holdings count (rows with no resolved key, of how many);
- the folders with two or more ONE PAGER workbooks and their lines; the build_universe hookup you need;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Z):** ROUND_ANALYSIS.round76.md @c8bbeeac10 section 4 item 10 (the identity resolving cell; the ONE PAGER precedence rides it per the CTO's section E). Decomposition s.85. Chain `~281`, wave 0, no inbound edge. Checks dry-run at the base: ba-15 AC1 base: FAIL as expected; ba-15 AC2 base: FAIL as expected; ba-15 AC3 base: FAIL as expected. SCOPE NOTE: the served crosswalk already keys 89 of 89, so the cell is the grading read, not a second resolver; the five identity rows close on its printed figure. MERGE HOOKUP (issuer, one line): `lib/research/identity/build_universe.py:145` returns `one_pager_precedence.ordered(folder_path, matches)`. `crosswalk.py:79` and `build_universe.py:56,81` name a worker deliverables folder (row Z-W37-S2's cell moves those).

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~281</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @dbfa9f5b1c; proof VALID (worktree checker); identity/covered_keyed.py and one_pager_precedence.py; keyed 89 of 89 (residual 0); 5 of 89 folders carry two workbooks, each with its superseded line; AC1, AC2, AC3 YES; row Z-W281-S1 (60 of 167 holding rows unkeyed, a vendor identifier map)</status>
