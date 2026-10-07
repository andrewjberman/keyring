# NFRA_OPLGTW task order -- `OG-bi-3` -- the bun cache pre-check tests that each entry is complete (ruling R46)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-bi-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~33</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a change to one small program with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's ruling R46 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round27.md ADDENDUM 1 @f6fd7281cf).
EGRESS CLASS, declared: NONE. No network request of any kind.
</preflight>

## 1. THE CELL -- `OG-bi-3` (decomposition addendum R3-T.26, item 1)

`infra/aws/ec2/opal-gateway/ops/bun_cache_precheck.py` (your cell OG-bi-1) decides that a lockfile entry is cached when
its directory `<cache>/<name>@<version>@@@1` EXISTS (`_cached`). A directory that exists and is partial, or empty,
passes; `bun install` would then fetch that package. The pre-check must test that the entry is COMPLETE.

Do:
1. **Find what marks a finished entry**, read-only, on the real cache. Read a handful of entries and bun's own files in
   the cache root and record in `W/BI3_MARK.md` what you rely on and why. Candidates, in order of preference:
   - bun's own record of a finished entry, if the cache keeps one you can read without bun;
   - else the entry's own `package.json` existing, parsing, and naming the SAME package name and version as the
     lockfile entry (for a prerelease: the exact version string, which also closes OG-bi-1's prefix weakness).
   The lockfile's integrity value is a hash of the tarball; the cache holds the extracted tree, so say plainly whether
   the integrity value can be checked against anything in the cache, and do not pretend it can if it cannot.
2. **Make `_cached` require that mark.** An entry failing it is reported missing with a reason word after the name
   (`absent`, `empty`, `no-manifest`, `version-mismatch`), so the list sent to the laptop's intake says what is wrong.
   The output's first line stays `<present> of <total>` and the exit codes stay as they are.
3. **Tests:** `infra/aws/ec2/opal-gateway/tests/test_deploy_install_no_fetch_complete.py`, the four tests the header of
   `bi3.AC1.sh` lists, named EXACTLY `test_ogbi3_ac01` to `test_ogbi3_ac04`. The first cell's
   `tests/test_deploy_install_no_fetch.py` uses caches of EMPTY marker folders: update its fixtures to complete
   entries so its four tests still pass for the right reason, and name each change.
4. **The real read**, recorded in `W/BI3_REAL_READ.md`: the new pre-check against the real lockfile (read with
   `git -C "<main repo>/mcportal" show <commit>:bun.lock`, the commit being `services.opal-gateway.mcportal_commit` in
   `infra/aws/ec2/EC2_MANIFEST.json`) and the real cache. State `<present> of <total>` and every entry reported
   missing with its reason. A real entry reported missing is a FINDING: list it, do not weaken the rule to pass it.
5. **One more read-only question, answered in `W/BI3_METADATA.md`:** is there a read that decides, WITHOUT any network
   request and without running `bun install`, whether a frozen install with every entry cached contacts the registry?
   For example bun's own files in the cache root (a manifest cache with modified times), or the installed bun's
   documentation shipped on this box. If such a read exists, do it and state the answer with the file read. If none
   exists, write UNDETERMINED and the reason. Do not observe the network.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~33/`.

## 2. BOUNDS

- **Fetch nothing.** No `bun install`, `bun add`, `bun x`, `bun run`, `npm`, `pip install`, `curl`, `wget` or any
  command that can reach the internet. `bun --version` and `bun <command> --help` are allowed.
- Never delete, move or edit anything in bun's real cache. Tests use temp directories.
- No deploy, no host act, no AWS call. `deploy-to-ec2.sh` is not run and not edited.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/ops/bun_cache_precheck.py
infra/aws/ec2/opal-gateway/tests/test_deploy_install_no_fetch.py
infra/aws/ec2/opal-gateway/tests/test_deploy_install_no_fetch_complete.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~33/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W33-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-bi-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r29/checks/bi3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-bi-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r28/checks/bi1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: an empty or incomplete entry is reported missing; complete entries pass; the real read is recorded.
- `AC2`: the first cell's four tests still pass on complete fixtures.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-bi-3.bun-cache-precheck-complete.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the mark you rely on and why; whether the integrity value is checkable; the diff of
   `_cached`; each fixture change in the first cell's tests; the real read's count and every missing entry with its
   reason; the metadata question's answer or UNDETERMINED; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 29 (R3-T.26, item 1), cut on R46 of `ledger/ROUND_ANALYSIS.round27.md` ADDENDUM 1 @f6fd7281cf. The limit was
  found by `3.0.0_SA_CVO~Z` (slug msg 31258); the issuer's re-grade of OG-bi-1 ran the tests and did not read
  `_cached`.
- Item 5 answers the fourth item of that addendum's list, "the metadata-request measurement, if a read exists that
  decides it without a fetch".
- Chain: -> `OG-rl-14` (the r28 release ships the pre-check as changed here).
- Pre-cut 18:5xZ: `bi3.AC1` FAIL (the test file is absent); `bi1.AC1` PASS 4 of 4 (the first cell, unchanged).

<status>complete</status>
<round>29</round>
<slot>~33</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
