# NFRA_OPLGTW task order -- `OG-en-34` -- correct one wrong code comment in `app/probe_listener.py` (round 44; candidates item 12, the CVO's finding on `OG-ap-44`, relayed by the CTO msg 35785)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-34</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-34</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~160</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a comment edit; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; no AWS call is needed.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-43 analysis, list item 5 (the one-line comment correction rides the eleventh release).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-34` (decomposition addendum R3-T.121 amendment A1, round 44, workstream ENRICH-R44-A)

WHY. `infra/aws/ec2/opal-gateway/app/probe_listener.py` carries this comment block (lines 358 to 361 at the cut):

```
# uvicorn's Config configures PROCESS-WIDE logging: the uvicorn, uvicorn.error, uvicorn.access and uvicorn.asgi loggers
# (level, handlers, propagate, disabled, filters) and, for access_log=False, uvicorn.access's handlers and propagate. The
# probe's Config silenced the service's own access log (OG-pr-5, round 43), so the four loggers are snapshotted before the
# Config is built and restored after it, on error too. The probe still writes no access line of its own.
```

The last sentence is WRONG. Row `Z-S397` measured the opposite: with the service's handlers restored, uvicorn writes an access line for the listener's OWN requests too, because `uvicorn/protocols/http/h11_impl.py` (line 57) and `httptools_impl.py` (line 61) decide per connection by `access_logger.hasHandlers()`, whatever `Config.access_log` says. The gateway's journal therefore shows the listener's `/probe/` requests (as the release `eff517546e` was proven to do: 3 listener lines for 3 requests made).

DO: replace ONLY that last sentence (`The probe still writes no access line of its own.`) with a correct one, still a `#` comment, in the same block, that says: with the handlers restored uvicorn logs the listener's own requests too (it gates on `access_logger.hasHandlers()`, not on `Config.access_log`; row `Z-S397`), so a `/probe/` request leaves a journal line. At most three comment lines may change (the sentence may wrap onto a second `#` line). No other line of the file may change: not one character of code, no docstring, no import.

## 2. BOUNDS

- Write only `infra/aws/ec2/opal-gateway/app/probe_listener.py` (the comment lines named above), and, if a row is needed, the channel. No other product file, no test, no release, no deploy.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret, an email address or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/probe_listener.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~160/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W160-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-34"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/en34.AC1.sh; echo "exit=$?"</invocation><expect>(?s)changed lines \(either side\) [1-6] \(want 1 to 6, i\.e\. at most 3 replaced\); every changed line is a comment yes; AST equal to the base blob yes; the stale sentence gone yes; the new comment names hasHandlers yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-34"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/en34.AC2.sh; echo "exit=$?"</invocation><expect>(?s)test_og_pr1\.py and test_og_pr5\.py together: passed \d+; failed 0; pytest rc=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: only comment lines of `probe_listener.py` changed (at most three replaced), the AST equals the base blob's, the stale sentence is gone and the new one names `hasHandlers`. `AC2` (a control): the listener's two test files still pass.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-34.round-44-correct-the-probe-listener-access-line-comment.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hash, the AC lines, the new sentence).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 44, workstream ENRICH-R44-A, a seventh cell added by the issuer (decomposition amendment A1): the CTO's list puts the comment correction inside `OG-ap-46`, but a release may take only files already on trunk (`ap46.AC1` byte-equal to trunk), so the edit needs its own order first. It has no ruling-sized content; it is gated by `to-pipeline-gate` as a newly added tree order.
- The base blob is `85ce5027cc8bd84dc93aa00bc71130e2c09c0795` (`git rev-parse HEAD:infra/aws/ec2/opal-gateway/app/probe_listener.py` at the cut); `AC1` compares to it. Base: `AC1` FAIL as expected (no change, the stale sentence stands); `AC2` base PASS as expected (a control, 16 passed); a temporary edit of the sentence passed `AC1` (2 changed lines) and was restored byte-equal.
- Risk `WORLD` is the gateway-path floor.

<status>complete</status>
<round>44</round>
<workstream>ENRICH-R44-A</workstream>
<slot>~160</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
