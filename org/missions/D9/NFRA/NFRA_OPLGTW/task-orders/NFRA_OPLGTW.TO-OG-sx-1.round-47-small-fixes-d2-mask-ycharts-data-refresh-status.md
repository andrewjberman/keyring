# NFRA_OPLGTW task order -- `OG-sx-1` -- the small-fix cell: the Cottonwood date parse (D2), the AWS error-text mask (Z-S407), the YCharts and data-refresh repairs (Y1, Y2, R1 and the fund-series cap): four product files and one test file (round 47; round-46 analysis items 4, 5 and 8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sx-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sx-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~167</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code and test change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429): item 4 (the Z-S407 mask), item 5 (D2, Z-S410), item 8 (Y2 Z-S422, Y1 and R1 Z-S423) and the YCharts part of item 2 (Z-S424).
EGRESS CLASS, declared: NONE (every probe uses fakes; no network).
</preflight>

## 1. THE CELL -- `OG-sx-1` (decomposition addendum R3-T.124, round 47, workstream ENRICH-R47-A)

Five independent small repairs, each in its own file. Read each file's named function first. The gateway folder is `infra/aws/ec2/opal-gateway/` (every path below is relative to it unless it starts with `org/`).

**R-D2 (row Z-S410, `app/client_adapter_bdcottonwood.py`, `_date`, about line 114).** `_date(value)` returns `date.fromisoformat(str(value)[:10])` and `None` on `ValueError`. The Black Diamond source stores `Trade Date` as the string `MM/DD/YYYY` (for example `10/12/2026`), so every row's date is `None` and `_window_rows` drops every row: `client_get_transactions` and `client_get_fees` answer an empty list for every Cottonwood account (a false zero). CHANGE `_date` so it also parses `M/D/YYYY` and `MM/DD/YYYY` (one or two digits for month and day, four for the year, month first), still returns `None` for a string that is not a real date (`13/45/2026`, `garbage`, the empty string) and for `None`, and still parses the ISO form and an ISO timestamp (`2026-10-12T04:05:06`) as before. Use `datetime.strptime` or a strict regex; no new dependency.

**R-MASK (row Z-S407, `app/family_depth.py`, `_why`, about line 67).** `_why(exc)` returns `"%s: %s" % (type(exc).__name__, str(exc)[:200])`. AWS error text can carry a role ARN, a twelve-digit account number and an instance id, and the route (owner-only) returns that text. CHANGE `_why` to scrub the exception text BEFORE the 200-character cut: every ARN-shaped token (`arn:aws` followed by the rest of the non-space token) becomes `<arn>`, every run of exactly twelve digits (not part of a longer digit run) becomes `<id12>`, every instance id (`i-` followed by 8 to 17 hex digits, at a word boundary) becomes `<instance>`. The exception class name is kept first; a text with none of these shapes is returned exactly as before. Do not change any other function of the file.

**R-Y1 (row Z-S423, `app/integrations/ycharts/integration.py`, `_parse_table`).** `_parse_table(rec, calc_name)` keys the value by `entry.get("security_id") or entry.get("id")`; when the entry carries neither key the symbol is `None` and the answer reads `{"None": 12.91}`. CHANGE the signature to `_parse_table(rec, calc_name, symbols=None)` and pass the tool's requested `symbols` list at its one call site (`ycharts_snapshot_metrics`). Rule: an entry that carries `security_id` or `id` keeps that key (as now). An entry that carries neither takes the requested symbol AT THE SAME POSITION, when the number of entries equals `len(symbols)`; otherwise it takes the key `unattributed_<position>` (zero-based). The string `"None"` and `None` are never a key.

**R-Y2 (row Z-S422, same file).** `ycharts_time_series`, `ycharts_risk_return_scatter`, `ycharts_fund_series` and `ycharts_snapshot_metrics` return `http_status` and an EMPTY result when the upstream answers 403: a caller reads "no data". CHANGE each of the four so that when `http_status` is 400 or above the answer also carries `absent_reason` = `"upstream_http_<status>"` (for example `upstream_http_403`); when the status is below 400 the key is absent or `None`. The existing keys and values are unchanged.

**R-CAP (row Z-S424, same file).** `ycharts_fund_series` (1,255 daily points, about 59 KB) and `ycharts_time_series` exceed the 50 KB answer. CHANGE both so that the answer serialised the way the server serialises it (`json.dumps(obj, indent=2, default=str)`, UTF-8 bytes) is at most 51200 bytes: when the series is too long keep the NEWEST points (the end of the list), set `truncated` to `true`, keep `points` as the TOTAL count the upstream returned, and add `returned_points` = the count served. A series that already fits is untouched (`truncated` false or absent, `returned_points` may be absent). Drop points from the front by a count found with a bisection or a loop; do not null a field.

**R-R1 (row Z-S423, `app/integrations/opal_portal/integration.py`, `opal_data_refresh_status`, about line 405).** The status route answers 404 for an id it does not know; the tool turns every non-200 into `status: "UNKNOWN"`, `terminal: false`, and its docstring tells a caller to poll until a terminal status, so a typo'd id is polled forever. CHANGE: a 404 from the status route yields `status: "NOT_FOUND"` and `terminal: true` (the `status_note` stays, for example `status HTTP 404`); any other non-200 stays `UNKNOWN` and non-terminal; a 200 is unchanged. Update the docstring's list of terminal statuses to name `NOT_FOUND`. Keep the existing `TERMINAL_STATUSES` tuple's four members; add the new status where the `terminal` flag is computed.

**The new test file `tests/test_og_sx1.py`** with at least one test per repair (names fixed): `test_ogsx1_d2_dates`, `test_ogsx1_mask`, `test_ogsx1_y1_keys`, `test_ogsx1_y2_absent_reason`, `test_ogsx1_cap_keeps_newest`, `test_ogsx1_r1_not_found`. Build the YCharts and portal cases with fakes as `tests/test_opal_portal_status_id_shape.py` does for the portal; build any fake identifier at run time (`"1" * 12`, `"i-" + "a" * 17`), never type a real-looking account number or ARN in the file.

## 2. BOUNDS

- Write only the four product files above, `tests/test_og_sx1.py`, `W/` and, if a row is needed, the channel. NO other product file, no other test, no release, no deploy, no Terraform, no AWS call, no network call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, ARN, email address or client value in a test, a record or a report.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_adapter_bdcottonwood.py
infra/aws/ec2/opal-gateway/app/family_depth.py
infra/aws/ec2/opal-gateway/app/integrations/ycharts/integration.py
infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py
infra/aws/ec2/opal-gateway/tests/test_og_sx1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~167/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W167-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sx-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sx1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)date cases 8 of 8.*masked text: class kept True; length \d+ \(want <= 230\); shapes left none.*plain text kept: .*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sx-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sx1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)Y1 one entry without an id key, one symbol: ok.*Y1 length mismatch never yields the key 'None': ok.*Y2 ycharts_snapshot_metrics on upstream 403: ok.*cap ycharts_time_series: 1255 points fit 51200 bytes indented, newest kept, totals honest: ok.*R1 a 404 id is NOT_FOUND and terminal, note kept: ok.*R1 a 200 RUNNING stays non-terminal: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-sx-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sx1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_sx1.py: [1-9]\d* passed, 0 failed.*neighbours \(\d+\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: D2's date parse and the mask. `AC2`: Y1, Y2, the YCharts cap and R1, each probed with fakes. `AC3`: your test file and the 11 existing test files of the touched modules (50 tests at the base).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sx-1.round-47-small-fixes-d2-mask-ycharts-data-refresh-status.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Flip the ONE `<status>` tag to `complete` only if all three PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-A, `<risk>WORLD</risk>` is the gateway-path floor. Source: the CTO's round-46 analysis (msg 36165) items 4, 5, 8 and the YCharts half of item 2. This is the batch repair cell (one worker, `worker-light`); the other Z-S424 cap (M365 search) is `OG-tp-1`, the other Z-S423 part (`top`) is `OG-tp-1` too.
- READINGS DISCLOSED TO THE CTO: (1) `NOT_FOUND` is a new terminal status value on `opal_data_refresh_status`, the issuer's; a caller that tests `status in (SUCCEEDED, FAILED, TIMED_OUT, ABORTED)` ignores it, one that tests `terminal` stops. (2) The YCharts cap keeps the newest points and says so (`truncated`, `points` total, `returned_points`). (3) The mask replaces three shapes with `<arn>`, `<id12>`, `<instance>`; the Z-S407 condition C1 (the route's response goes nowhere beyond the owner) is unchanged by it. (4) Y2 only names the upstream status; whether the 403 is an entitlement or an endpoint change is not decided here.
- Pre-cut: `AC1` base FAIL as expected (date cases 6 of 8; the mask leaves all three shapes), `AC2` base FAIL as expected (Y1 `TypeError`, Y2 absent_reason None, cap not applied, R1 `UNKNOWN`; the two controls hold), `AC3` base FAIL as expected (no test file). The 11 neighbour files pass at the base (50 tests).

<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-A</workstream>
<slot>~167</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
