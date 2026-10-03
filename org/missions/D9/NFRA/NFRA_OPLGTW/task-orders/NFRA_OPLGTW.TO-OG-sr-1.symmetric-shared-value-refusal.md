# NFRA_OPLGTW task order -- `OG-sr-1` -- the mail and transcript routes refuse a bearer value shared with another route (the symmetric refusal), built on CLOUD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~24</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change on CLOUD; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no AWS call; the routes read their bearers from .env.
comp-adversary: DECLARED-NOT-APPLICABLE -- the requirement is the CVO's finding (org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NEVER_WIDEN_OG-rl-3_POST_HOC_HALF_20261002.md section "Finding") adopted by the CTO (analysis round 13 addendum @b100b15b2e).
EGRESS CLASS, declared: NONE -- tests are local; no network.
</preflight>

## 1. THE CELL -- `OG-sr-1` (decomposition addendum R3-T.7, item 2)

**What is wrong today.** `infra/aws/ec2/opal-gateway/app/teams_route.py` refuses a presented `TEAMS_BEARER` whose value
also equals another route's credential. It does this with `OTHER_ROUTE_BEARERS` (:85) and `_shared_elsewhere` (:132),
called in `match_bearer` (:143-155).

`app/mail_route.py` `match_bearer` (:115) and `app/transcript_route.py` `match_bearer` (:102) compare only their own
bearer and refuse nothing shared. A rotation that made two routes' values equal would therefore let one value open both
routes.

1. **`mail_route.py`.** Mirror the teams pattern:
   - `match_bearer` returns `None` when the matched value is also the value of any of `OTP_BEARER`, `MS_INGEST_BEARER`,
     `GRAPH_READ_BEARER`, `TRANSCRIPT_BEARER`, `TEAMS_BEARER` or `TAXSMA_WORKBOOK_BEARER`;
   - compare in constant time (`hmac.compare_digest`); split multi-value config fields as the module already does;
   - treat an unset or empty other-route field as no match;
   - leave every other behaviour unchanged.
2. **`transcript_route.py`.** The same, with the other-route tuple `OTP_BEARER`, `MS_INGEST_BEARER`, `GRAPH_READ_BEARER`,
   `MAIL_BEARER`, `TEAMS_BEARER`, `TAXSMA_WORKBOOK_BEARER`.
3. **Tests**, one new test in each existing file, with synthetic config and no network:
   - `tests/test_mail_route.py::test_ogsr1_mail_refuses_shared_value` asserts three things:
     - a request presenting `MAIL_BEARER`'s value is refused (401, no Graph call) when `TEAMS_BEARER` holds the same
       value;
     - the same holds when `TRANSCRIPT_BEARER` holds it;
     - with all values distinct, the same request is admitted.
   - `tests/test_transcript_route.py::test_ogsr1_transcript_refuses_shared_value` makes the same three assertions, with
     `MAIL_BEARER` and `TEAMS_BEARER` as the sharers.
   - Every existing test in both files stays green.

## 2. BOUNDS

- **Edit ONLY:** the four files named in section 3's `<paths>`.
- **Out of scope here:** deploy and release tree (`OG-rl-4` ships this), and `teams_route.py` or `taxsma_workbook.py`
  (already symmetric).
- **Never:** push, merge, rebase, stash, `checkout --` or `clean`; override a gate.
- Every `.py` edit passes `.tools/commit-gate.sh`; commit with `.tools/safe-commit.sh`.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/mail_route.py
infra/aws/ec2/opal-gateway/app/transcript_route.py
infra/aws/ec2/opal-gateway/tests/test_mail_route.py
infra/aws/ec2/opal-gateway/tests/test_transcript_route.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~24/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W24-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/sr.AC1.sh; echo "exit=$?"</invocation><expect>(?s)mail rc=0; transcript rc=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/sr.AC2.sh; echo "exit=$?"</invocation><expect>(?s)outside the allowed four: 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: both named tests pass and both files' suites are green.
- `AC2`: the cell's commits touch only the four named gateway files.

## 5. WHEN YOU ARE DONE

Write the instance to `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~24/NFRA_OPLGTW.TO-OG-sr-1.symmetric-shared-value-refusal.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. If both criteria PASS, append a `complete` status
tag after the order's last status line, in the same commit. Report once: the diff summary, the literal AC output,
commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 14 (addendum R3-T.7, item 2); feeds `OG-rl-4` (the CTO's addendum @b100b15b2e puts the symmetric refusal in
  OG-rl-4's payload; it is built here on CLOUD so CLOUD and live stay equal for these four files, which they were at the
  cut: `git diff 4231bd2ddc -- app/mail_route.py app/transcript_route.py` is empty).
- Pre-cut 00:1xZ: `sr.AC1` FAIL (named tests 0 of 1 in each file; both suites rc 0); `sr.AC2` FAIL (0 files).

<status>complete</status>
<round>14</round>
<slot>~24</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
