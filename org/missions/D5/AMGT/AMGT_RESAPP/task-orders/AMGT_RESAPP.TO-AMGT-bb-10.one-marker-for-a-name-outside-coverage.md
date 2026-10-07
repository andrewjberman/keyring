# AMGT_RESAPP task order -- `AMGT-bb-10` -- ONE SERVED MARKER FOR A NAME OUTSIDE COVERAGE (ROW Z-S364)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~296</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_B_NOTES.md) -- No marker is served on any of 97 overlays read; the pool holds 243 names, 95 covered and 148 outside. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-296` (branch `wk-AMGT_RESAPP-296`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-296`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-10` (round 78, decomposition s.86)

We serve a page for any company in our wider company list, but we cover (hold research and company figures for)
only some of them. For a company we do not cover, nothing served says so: the page shows seven header figures each
reading "We hold no stored company data for this name yet." Build the ONE marker that says it once.

Create `lib/research/api/coverage_marker.py` (standard library only) exporting ONE function:

`marker(security_key, covered_keys)` returns a dict with exactly these four keys: `status`, `covered`, `sentence`,
`covered_names`.
- `security_key` is the company's key as text, or `None`.
- `covered_keys` is the collection of keys we cover, or `None` when the caller could not read that list.

Rules:
1. `covered_keys` is `None`: `status: "not_known"`, `covered: None`, `covered_names: None`, `sentence` "We could not
   check just now whether we cover this company." A list that could not be read must never read as "not covered".
2. `security_key` is in `covered_keys`: `status: "covered"`, `covered: True`, `sentence: None`.
3. Anything else, including an empty or missing key: `status: "outside_coverage"`, `covered: False`, `sentence` "We
   do not cover this company yet, so we hold no company figures or research for it. Any news or comparable companies
   shown here come from our wider market data."
4. In rules 2 and 3 `covered_names` is the count of distinct keys in `covered_keys`.
5. The three statuses are the whole set; every input gets exactly one. Keys are compared exactly as given (no
   re-casing, no trimming).
6. No sentence uses: identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage,
   input ledger, bronze.

Plant tests in `lib/research/api/tests/test_coverage_marker.py`: one per rule, a key with a slash (`BP/_LN_Equity`),
a list with a repeated key (counted once), a `set` and a `list` argument.

You do NOT edit `lib/research/api/scoped_amgt.py`.

**The hookup the adapter cell makes:** a new top-level field `research_coverage` on both bundles:
`"research_coverage": coverage_marker.marker(resolved_key, covered)` in `read_security_overlay` (the bundle at
`scoped_amgt.py:3467-3496`) and `read_thesis_bundle` (`:3629`). `covered` is `covered_security_keys()` read as
`_covered_key_known` reads it (`:1064-1081`), and `None` when that read raises.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W296-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited: the round's adapter cell, AMGT-bb-17, makes every hookup. Name yours in your report.
3. Covered means a name in covered_security_keys(). The older covered_no_block field is not edited and not reused.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/coverage_marker.py
lib/research/api/tests/test_coverage_marker.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~296/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-10"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb10.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>a covered name reads "covered" with no sentence; a name outside the list and an empty key read "outside_coverage" with one plain sentence; an unread list reads "not_known", never "outside_coverage"; every answer carries the four fields and no system word; C1-C4 PASS; R78 BB10 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-10"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb10.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>against the real covered list every covered name reads "covered" (N of N); MSFT_US_Equity and ABNB_US_Equity read "outside_coverage" with the sentence and AMD_US_Equity reads "covered"; the pool's names split into the two statuses with nothing left over; C1-C3 PASS; R78 BB10 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~296 <0.9.0_WK_AMGT_RESAPP~296@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~296/AMGT_RESAPP.TO-AMGT-bb-10.one-marker-for-a-name-outside-coverage.proof_of_spec.json`.
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

**ISSUER NOTES:** CTO msgs 30812 and 31020, row Z-S364. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_B_NOTES.md` (cell B4), committed @643863854d before the cut. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~296</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @60a87724eb; proof VALID rc=0 on the worker's checker; every criterion re-run by the issuer on the shared tree reads SERVED: YES; served only after the adapter cell bb-17</status>
