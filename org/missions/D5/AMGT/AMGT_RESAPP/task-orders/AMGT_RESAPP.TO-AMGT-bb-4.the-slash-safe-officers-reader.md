# AMGT_RESAPP task order -- `AMGT-bb-4` -- THE SLASH-SAFE OFFICERS READER: A STORED LIST FOR A SLASH NAME IS READ (ROW Z-S365)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~292</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_A_NOTES.md) -- The reader finds 89 of 91 stored folders; BP/ LN Equity and NG/ LN Equity are stored and never read. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-292` (branch `wk-AMGT_RESAPP-292`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-292`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-4` (round 78, decomposition s.86)

Repair ONE method in ONE existing file: `StoredBloombergInput.newest_key` in `lib/research/management/bloomberg_fallback.py`.
You are the only writer of that file this round.

Today it lists `bloomberg/harvest/bronze/exec_officers/security_key=<security with spaces turned to underscores>/`. The
writer stores a name through `lib.research.harvest.store.entity_partition`, which turns a slash into `-SLASH-`. So
`BP/ LN Equity` and `NG/ LN Equity` are stored under `security_key=BP-SLASH-_LN_Equity/` and
`security_key=NG-SLASH-_LN_Equity/` and are never read: `newest_key("BP/ LN Equity")` returns None.

1. Make `newest_key(security)` list the folder the writer writes: `BRONZE_PREFIX` +
   `store.entity_partition("security_key", security_key(security))` + `/`. The store module is already imported in this
   file's package as `hbloom.store`; `hbloom.bronze_fetched("exec_officers", security_key(security), client=...)` is the
   estate's own listing of that folder and may be used instead. Keep the return: the newest `.json` key, or None.
2. Do NOT change what `security_key()` returns (`"AMD US Equity"` gives `"AMD_US_Equity"`, `"BP/ LN Equity"` gives
   `"BP/_LN_Equity"`). `pull_exec_officers` hands that text to the writer, which makes it slash-safe once; a second
   encoding is refused by the store.
3. Change nothing else in the file: not `pull_exec_officers`, not the parse, not the status rule, not `reference_data`'s
   shape. Fix the stale line in the class docstring if you touch it.
4. Plant tests in a NEW file, `lib/research/management/tests/test_stored_officers_slash_key.py`, with a fake S3 client:
   an object stored under `security_key=BP-SLASH-_LN_Equity/` is found by `newest_key("BP/ LN Equity")` and read by
   `pull_exec_officers("BP/ LN Equity", blp=StoredBloombergInput(s3=fake))` with status OK; a plain name is found as before;
   the newest of two stamps wins; a name with nothing stored returns None.

**You do NOT edit `lib/research/api/scoped_amgt.py`, `lib/research/management/exec_roster_chain.py`,
`lib/research/management/fwd7_plan.py`, `lib/research/freshness/build_view.py` or `lib/research/harvest/*`.** No hookup is
needed: `exec_roster_chain` already calls `newest_key`. Say so in your report, and say that the page changes only with the
next redeploy of the function.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W292-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. bloomberg_fallback.security_key() keeps its return value: the writer is already slash-safe.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/management/bloomberg_fallback.py
lib/research/management/tests/test_stored_officers_slash_key.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~292/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb4.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>newest_key("BP/ LN Equity") and newest_key("NG/ LN Equity") each return the newest object in that name's folder; the control AMD US Equity still does; every stored officer folder is read (N of N); the chain serves officers for both slash names and the control; C1-C4 PASS; R78 BB4 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb4.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>every plant case in test_stored_officers_slash_key.py passes; R78 BB4 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb4.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>security_key() returns AMD_US_Equity and BP/_LN_Equity as before; the three existing test files of this reader pass; C1-C2 PASS; R78 BB4 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~292 <0.9.0_WK_AMGT_RESAPP~292@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~292/AMGT_RESAPP.TO-AMGT-bb-4.the-slash-safe-officers-reader.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 30847 (a round-78 cell), row Z-S365. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_A_NOTES.md` (cell A3), committed @643863854d before the cut. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~292</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @70d0d07c5f; proof VALID rc=0 on the worker's checker; every criterion re-run by the issuer on the shared tree reads exit 0 and SERVED: YES; served at the next redeploy</status>
