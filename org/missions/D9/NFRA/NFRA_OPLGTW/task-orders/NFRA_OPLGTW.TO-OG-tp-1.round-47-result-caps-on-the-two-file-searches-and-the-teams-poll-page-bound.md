# NFRA_OPLGTW task order -- `OG-tp-1` -- result caps on `search_files` and `search_site_files` (Z-S424) and the `top` bound of `poll_addressed_teams_messages` (Z-S423 T1): three functions of `app/tools.py` and one test file (round 47; round-46 analysis items 2 and 8; queued behind `OG-mg-3` on the same worker)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tp-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-tp-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~169</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code and test change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the Graph scopes of the three tools are unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429): item 2 (Z-S424: the other oversize tools fold into the size-cap fix) and item 8 (Z-S423, the `top` of the Teams poll).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-tp-1` (decomposition addendum R3-T.124, round 47, workstream ENRICH-R47-A)

WHY. Row Z-S424: `search_files` answers 75.9 KB and `search_site_files` 80.9 KB (neither takes a result cap), over the client's tool-result limit and a load risk on the host. Row Z-S423 T1: `poll_addressed_teams_messages(since_iso, top=2)` answered `count 4`: `top` reaches the Graph request (`$top: max(top, 50)`) but never bounds the answer. This order starts AFTER `OG-mg-3` is drained on your branch (the same worktree): `OG-mg-3` already edited `app/tools.py` (the `call_tool` hunk); keep that hunk exactly as it is.

READ FIRST (under `infra/aws/ec2/opal-gateway/`): `app/tools.py` `search_files` (about line 657), `search_site_files` (about line 916), `poll_addressed_impl` (about line 1824) and `poll_addressed_teams_messages` (about line 1873); `app/harvest_typed.py` `project()` (the 50 KB projection; `OG-sz-1` is changing its internals in parallel, so call it only through its signature `project(out: dict, limit: int = 51200) -> dict`).

DO, in `app/tools.py` ONLY (plus the new test file):

1. **`search_files(query, top=25)` and `search_site_files(site_id, query, top=25)`.** Add the parameter `top: int = 25` (clamp it to the range 1 to 100; a value outside is clamped, never an error). The Graph answer is a dict with a `value` list. When `len(value) > top`, keep the first `top` items in Graph's order, set `truncated: true`, `total` = the number Graph returned and `returned` = the number served. THEN apply the 50 KB projection to the whole answer with `harvest_typed.project(answer, 51200)` (import it the way `tools.py` imports its sibling modules), because 100 large items can still exceed the limit; after projection `returned` must equal the length of the `value` list actually served (recompute it) and `truncated` is true if anything was cut. An answer that fits and has at most `top` items is returned exactly as Graph answered, with no `truncated`, `total` or `returned` key. Update both docstrings in one sentence to name `top`. Do not change the Graph request, its `$select` or the `_run` call shape beyond passing the new argument into the audited args if the pattern of the file does so for other `top` arguments.
2. **`poll_addressed_impl(token, since_iso, top=50)` honours `top`.** After the existing oldest-first sort, if `len(out) > top`: keep the first `top` messages (the OLDEST), set the cursor to the `timestamp_utc` of the LAST kept message (so the next poll, passing that cursor, returns the rest: nothing is skipped and nothing repeats), and add `truncated: true` to the answer; otherwise the answer is exactly as before (no `truncated` key; the cursor is the newest timestamp seen). `top` below 1 is treated as 1. The REST route `/teams/poll` shares this function and gets the same behaviour; do not edit `server.py`. `count` equals the number of messages served.
3. **The new test file `tests/test_og_tp1.py`** with at least these tests (names fixed): `test_ogtp1_search_default_top`, `test_ogtp1_search_top_clamp`, `test_ogtp1_search_projection_fits`, `test_ogtp1_search_small_unchanged`, `test_ogtp1_poll_top_oldest_first_and_cursor`, `test_ogtp1_poll_three_pages_no_loss`. Fakes only (replace `tools._run` with a runner that calls the lambda, `tools.graph.call` with a fake, and for the poll fake the sender helpers `_SenderIds`, `_sender_fields`, `get_current_email` and `identity_scope.is_opal_users_only`); use no real-looking email address, tenant or account number in the file.

## 2. BOUNDS

- Write only `app/tools.py` (the three functions above), `tests/test_og_tp1.py`, `W/` and, if a row is needed, the channel. NO other product file, no other test, no release, no deploy, no Terraform, no AWS or Graph call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, email address or client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/tests/test_og_tp1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~169/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W169-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/tp1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)search_files default: 25 kept in order, truncated, total 400, returned 25: ok.*search_site_files default: 25 kept in order, truncated, total 400, returned 25: ok.*top=100 keeps 100 \(both tools\): ok.*top=500 is capped to 100 \(both tools\): ok.*top=0 is capped to 1 \(both tools\): ok.*100 large items still fit 51200 bytes indented: ok.*control: 5 items returned equal to Graph's answer, no truncated key: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-tp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/tp1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)top=2: the two oldest new messages, oldest first, count 2: ok.*top=2: cursor is the second message, truncated true: ok.*three polls of 2 return all six once, in order: ok.*the third poll is not truncated: ok.*default top: all six, cursor 10:06, no truncated key: ok.*nothing new: count 0, the given cursor kept: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-tp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/tp1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_tp1.py: [1-9]\d* passed, 0 failed.*neighbours \(\d+\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the two searches' cap and projection. `AC2`: the Teams poll's page bound with a cursor that loses nothing. `AC3`: your test file and the five existing files that import `tools.py`'s search, poll and gate paths.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-tp-1.round-47-result-caps-on-the-two-file-searches-and-the-teams-poll-page-bound.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Flip the ONE `<status>` tag to `complete` only if all three PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-A, `<risk>WORLD</risk>` is the gateway-path floor. Source: the CTO's round-46 analysis (msg 36165) items 2 and 8. It is cut as its own order because `app/tools.py` is also written by `OG-mg-3`; one worker holds both, in sequence, so the file has one writer at a time (C10).
- READINGS DISCLOSED TO THE CTO: (1) the default `top` of 25 for the file searches is the issuer's (a person scanning search hits reads about that many); a caller that wants more passes `top` up to 100. (2) `total` is what Graph returned (Graph pages at its own size), not the count of every match in the drive. (3) The poll cursor moves only as far as the last message served, so a capped poll never skips a message; a message from a dropped (external) sender after the cut is re-evaluated, and re-dropped, by the next poll.
- Pre-cut: `AC1` base FAIL as expected (the answers carry all 400 items; `top` is not a parameter), `AC2` base FAIL as expected (`top=2` returns six messages; the sequence and control lines pass trivially), `AC3` base FAIL as expected (no test file). The five neighbour files pass at the base.

<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-A</workstream>
<slot>~169</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
