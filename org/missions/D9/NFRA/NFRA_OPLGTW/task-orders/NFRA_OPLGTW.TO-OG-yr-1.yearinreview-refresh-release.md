# NFRA_OPLGTW task order -- `OG-yr-1` -- APPLY: the refreshed /yearinreview page ships as its own one-file gateway release (Andrew-direct ~21:4xZ, CTO msg 34233)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-yr-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-yr-1</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one static file, no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- one static file inside the release; no tool, no IAM, no grant, no route, no `.env` key.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew's word in 4.0.0_SA_CRO~Z's session ("once thats done push it live to mcp.opalinvest.dev/yearinreview"), relayed by the CRO (msg 34231) and decided by 1.0.0_SA_CTO~Z (msg 34233): "Ship it as its own one-file release right after ap-18 deploys, on ap-18's release as base."
EGRESS CLASS, declared: NONE beyond Opal's own AWS and one HTTPS GET of mcp.opalinvest.dev/yearinreview (the proof).
</preflight>

## 1. THE CELL -- `OG-yr-1` (decomposition addendum R3-T.56, workstream YEARINREVIEW)

The gateway serves `/yearinreview` from one self-contained file shipped INSIDE the release (`infra/aws/ec2/opal-gateway/app/static/yearinreview/index.html`, 48,022 bytes today; module `app/yearinreview_view.py`).
The CRO rebuilt the page through 2026-10-14; the FINAL pin is `org/tier1_exec/4.0.0_SA_CRO/deliverables/BRIEF1_YEAR_ONE_20261004/YEAR_ONE_ONE_PAGER.html` at commit `947fc522a8`
(48,235 bytes, md5 `0d828b51d433a24f7e2ef2e6ea7967ee`, carries the data date `"until": "2026-10-11"`). Earlier pins `1db3d8d0aa` and `a0e00489b0` are SUPERSEDED: never copy them.

### PHASE A (A1: NOW, on the host's running commit; it no longer waits for `OG-ap-18`): cut, ask. NO deploy

1. **Live ref** (the host's running commit, read at the act). Read `services.opal-gateway.deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` at HEAD, then one SSM md5 read of the host against it, walking `app/`, `deploy/` and `dashboard/`. A mismatch is a STOP and a BLOCKING row.
2. **Cut** a worktree `C:/tmp/og-rel-yr`, new branch `rel-nfra-oplgtw-yr`, at that live ref. Write `app/static/yearinreview/index.html` BYTE FOR BYTE from the pin:
   `MSYS_NO_PATHCONV=1 git show 947fc522a8:org/tier1_exec/4.0.0_SA_CRO/deliverables/BRIEF1_YEAR_ONE_20261004/YEAR_ONE_ONE_PAGER.html > <the file>` and print the md5 (want `0d828b51d433a24f7e2ef2e6ea7967ee` for the CRLF pin blob). A2: write the page in its LF form (`| tr -d '\r'`), md5 `3bbd5ab2d325657020357003c3ea387d`, which is what the release blob and the served body carry.
   A2: ALSO edit `app/yearinreview_view.py` `_allowed()` EXACTLY as `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/YEARINREVIEW_OPEN_TO_ALL_OPAL_20261014.md` @c8f3a38f43 gives it (any non-guest Opal identity is admitted on `tools._is_opal_user`, or a roster entry), and add to `tests/test_yearinreview_view.py` the three tests `test_yr1_opal_admitted_on_empty_roster`, `test_yr1_guest_refused` (an `#EXT#` guest), `test_yr1_outside_domain_refused`. Touch NO other file.
   Commit with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only. Write `W/yr_release.json` = `{"base_sha", "release_sha"}` (FULL 40-character shas). Run the gateway tests whose names mention yearinreview.
3. **The ask**, `W/NEVER_WIDEN_ASK_OG-yr-1.md`, for TWO halves (`1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`). It carries, each under a heading containing its word: (1) the `diff` (three files: the page, the view gate, its test file; bytes before and after, md5s); (2) the `widening`, stated plainly:
   no tool, no IAM, no route, no `.env`; the SAME page route now serves newer content, AND (A2, Andrew-direct "I need it viewable by all opal employees") the viewer set WIDENS from the owner roster (`YEARINREVIEW_VIEW_ALLOWED_EMAILS`) to every non-guest Opal identity; state who could read before (the roster) and after (any signed-in `@opalinvest` identity that is not `#EXT#`; the ALB authenticate-oidc action and GuardMiddleware are unchanged; non-Opal and guest identities still get 403); (3) the `order` of acts (one deploy under a ledger);
   (4) the `rollback` (redeploy the base, parity with the host measured); the ask CITES `1.0.0_SA_CTO~Z` msg 34244 (his half is pre-stated there: blast radius one file, no tool, IAM or route change, rollback the redeploy of the running base) and is sent to him; (5) the `triggers` (`/health`, the registry count unchanged, `.env` key names unchanged, the host md5 of the file equals the LF source `3bbd5ab2d325657020357003c3ea387d`; an Opal address is admitted and a guest refused in the served read). Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names both halves signed at `release_sha`)

4. Ledger `nfra-oplgtw-gateway-release-yr`, entry AND sentinel first. Deploy from `C:/tmp/og-rel-yr` through `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<base_sha>`; the deploy tree's `git rev-parse HEAD` must equal the signed `release_sha` in full and its parent must equal live `deployed_commit` at the act
   (a mismatch is a STOP; print both). No `HALT_OVERRIDE`. Read back against the triggers; on any trigger redeploy the base and file an ARMED row naming `2.0.0_SA_COO~O`.
5. **The served read.** On the host through the INSTALLED code (one SSM call): the md5 of the served `/yearinreview` body equals the source md5, and the body carries `"until": "2026-10-11"`. Then one unauthenticated GET of `https://mcp.opalinvest.dev/yearinreview`
   and record its md5 (or its status and why it is gated). Write `W/YR_SERVED.json` = `{"body": {"md5_source": "0d828b51d433a24f7e2ef2e6ea7967ee", "md5_served_host": "<32 hex>", "contains_until_2026_10_11": true, "opal_user_admitted": true, "guest_refused": true, "public_md5_equal": true|false, "public_note": "<why, when false>"}}`; the two arms are read on the host through the INSTALLED code (an Opal stand-in identity is served 200, an `#EXT#` guest 403).
6. **Standing release clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and `file_checksums` come from the release blobs. Close the ledger, commit, run AC2, send `4.0.0_SA_CRO~Z` the release id (one message, so the CRO can confirm the served page), and report once to `2.0.0_SA_COO~O`.

## 2. BOUNDS

- The release's three files only (A2). No IAM or Terraform change, no catalog edit, no `.env` change, no object written to any bucket.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform`; print an `.env` value or a person's name or email; override a gate other than the one audited lane escape in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-yr.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-yr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/yr1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)base [0-9a-f]+ is the live ref before this release: yes.*files differing 3 \(want 3\); they are the page, the view gate and its test file: yes; release page equals the CRO page at 947fc522a8 in LF form: yes.*the gate admits Opal users on an empty roster: yes; tests defined 3 of 3.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-yr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/yr1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*landed=(?:current|superseded).*served page: host md5 equals the source yes; carries the data date 2026-10-11 yes; an Opal user is admitted and a guest refused yes; public endpoint recorded yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the re-cut is exactly one file, byte-equal to the CRO's final page, on the live ref. `AC2`: the deploy landed and closed, and the installed host serves the page with the source's md5 and the data date.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-yr-1.yearinreview-refresh-release.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once to `2.0.0_SA_COO~O`.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream YEARINREVIEW (decomposition addendum R3-T.56). Never-widen halves: CTO and COO (one static file, no reach change). The CTO: "I sign my half the moment it lands" (msg 34233). The GO is the issuer's message citing this order.
- Queue: staged until OG-ap-18 closes; then this release, then OG-ap-17's re-cut and OG-ap-19.
- Pre-cut: yr1.AC1 and yr1.AC2 base FAIL as expected (the two records are absent). The pin 947fc522a8 resolves here: 48,235 bytes, md5 0d828b51d433a24f7e2ef2e6ea7967ee, `"until": "2026-10-11"` present once.


- A1 (issuer, 2026-10-14 ~22:1xZ, Andrew-direct "i need it live now" via CRO msg 34242 and CTO msg 34244): this release goes NOW, ahead of the `OG-ap-18` re-cut, on the host's running commit (live `bacec95ccd` today). The queue is yr-1 -> ap-18 (re-cut on yr-1's release) -> ap-19. The CTO pre-stated his half in msg 34244; the issuer signs the COO half on the ask's arrival.
  Gate limb: GATE (viii) on the modified order (placeholders NONE).


- A2 (issuer, 2026-10-14 ~22:3xZ, Andrew-direct "I need it viewable by all opal employees", CTO msg 34266): the SAME release also widens the viewer gate (`_allowed()`, spec @c8f3a38f43) and its three tests; the ask names the WIDENING (roster -> every non-guest Opal identity) and the CTO signs on that. The page is graded in its LF form (`3bbd5ab2d325657020357003c3ea387d`; the pin blob is CRLF and its md5 is `0d828b51`). yr1.AC1 reads three files, the LF md5, the gate line and the three tests; yr1.AC2 adds the admitted and refused arms. Gate limb: GATE (viii) on the modified order (placeholders NONE).


- A3 (issuer, 2026-10-14 ~22:5xZ, msg 34270): the oracle for the SERVED page is the checked-out form `0d828b51d433a24f7e2ef2e6ea7967ee` (the path's `eol=lf` makes the blob LF, `3bbd5ab2`, but the deploy tars the checkout, which re-materialises the 344 CRLFs; measured by `~Z`). `YR_SERVED.json` `md5_source` and `md5_served_host` are `0d828b51`; yr1.AC1 still grades the BLOB in LF form. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>YEARINREVIEW</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
