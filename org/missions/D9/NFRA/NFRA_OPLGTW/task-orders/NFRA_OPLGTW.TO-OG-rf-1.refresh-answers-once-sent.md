# NFRA_OPLGTW task order -- `OG-rf-1` -- refresh rotation and code redemption answer once their transaction is sent (R50)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~38</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; the durable store is faked in the tests.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is ruling R50 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round31.md @e43ee663be) and PRD v2.0 item 6 (org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @e43ee663be), both halves signed @5924aaedbe.
EGRESS CLASS, declared: NONE. No network request of any kind.
</preflight>

## 1. THE CELL -- `OG-rf-1` (decomposition addendum R3-T.30, round 32 item 2)

**The defect (row NFRA_OPLGTW-Z-W35-S1).** `infra/aws/ec2/opal-gateway/app/server.py:375-382`, `_within_budget`, runs
the whole OAuth exchange on a thread pool inside `asyncio.wait_for(..., timeout=seconds)`. When the budget elapses it
answers 503, but the pool thread keeps going. For a refresh (`oauth_as.exchange_refresh`, `oauth_as.py:887`) the thread
can still send the conditional DynamoDB transaction that consumes generation N and installs N+1. The client then holds
a 503 and the OLD token, which the server has already retired; its correct retry presents generation N, which reads as
REUSE and revokes the whole family. Code redemption (`oauth_as.exchange_code`, `oauth_as.py:795`, called from
`server.py:681`) has the same shape over a single-use code.

**The rule (PRD v2.0 item 6, C1).** The budget bounds the START of the conditional transaction that consumes a
generation or a code. Once that transaction is SENT, the handler awaits its result and answers it, even past the
budget. A budget that elapses BEFORE it is sent answers 503 with nothing consumed.

Do:
1. Make "sent" an explicit, race-free point. In `exchange_refresh` and `exchange_code`, immediately before
   `st.transact_runtime(ops)`, the work must check, atomically with marking itself sent, whether the handler has
   already given up. Suggested shape (yours to choose, the rule is not): pass a small token object (a lock plus two
   flags, `abandoned` and `sent`) from `server.py` into the two functions, defaulting to `None` so every other caller
   is unchanged. Under the lock: if `abandoned`, raise the 503 `temporarily_unavailable` OAuthError and send nothing;
   else set `sent` and proceed to the transaction.
2. In `server.py`, for the two token grants only: wait for the work within the budget. On timeout, take the lock: if
   the work has NOT been sent, mark it abandoned and answer 503 exactly as today; if it HAS been sent, keep awaiting the
   same future (no second budget) and answer its result, success or OAuthError. Every other `_within_budget` caller
   (discovery, registration, authorize, callback, `_email_denied`) keeps today's behaviour.
3. Update the comment above `_OAUTH_POOL` (`server.py:366-369`) so it states the new rule; it currently says the
   abandoned work "can at most consume what it was given", which is the defect.
4. Do NOT change the budget constants (`oauth_as.AUTH_ENDPOINT_SECONDS` 10, `REFRESH_ENDPOINT_SECONDS` 30), the
   token rules, reuse detection, family revocation or any response shape. R48 stands: no grace window for a previous
   generation.
5. **Tests**, offline, in a new file `infra/aws/ec2/opal-gateway/tests/test_oauth_send_budget.py`, named EXACTLY
   `test_ogrf1_ac01` .. `test_ogrf1_ac04`, driving the real `/token` route (the `TestClient` of
   `tests/test_oauth_durable.py`, whose fake store you reuse), with the budget SHORTENED in the test only (monkeypatch
   the constant to a fraction of a second) and the fake store's `transact_runtime` slowed or gated with an event:
   - `ac01` refresh, slowed AFTER the send past the budget: 200 with the new pair; the family is `active`; the NEW
     refresh token then refreshes successfully.
   - `ac02` refresh, the budget elapses BEFORE the send (block the work before it reaches the send): 503
     `temporarily_unavailable`; let the abandoned work finish; the fake records ZERO transactions; the stored
     generation and hash are unchanged; the SAME refresh token then refreshes successfully.
   - `ac03` code redemption, as `ac01`: 200, the code consumed once, the family `active`.
   - `ac04` code redemption, as `ac02`: 503, the code NOT consumed; redeeming the same code then succeeds.
6. Run, each in its own process, and state totals: `tests/test_oauth_send_budget.py`, `tests/test_oauth_durable.py`,
   and every other `tests/test_*.py` whose name contains `oauth`, `token` or `refresh`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~38/`.

## 2. BOUNDS

- No release, no deploy, no host act, no AWS call. This cell is BUILT and HELD on your branch.
- Delete or rename no existing test; if an existing assertion pinned the defect, change ONLY that assertion and name it.
- Fetch nothing from the internet. Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/oauth_as.py
infra/aws/ec2/opal-gateway/tests/test_oauth_send_budget.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~38/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W38-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/rf1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/rf1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)test_oauth_durable\.py: pytest rc=0 passed \d+ .*removed or renamed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: both grants answer once sent and refuse cleanly before the send (PRD acceptance A25).
- `AC2`: the durable OAuth suite passes whole and lost no test.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rf-1.refresh-answers-once-sent.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the diff of `server.py` and `oauth_as.py`; where "sent" is decided and why it is
   race-free; every test file run with its totals; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32 (R3-T.30), item 2, ruling R50; row Z-W35-S1 (ARMED) disarms when this is live (r29). R51 closed OG-dr-1
  undrained; R52 does not require the 21:49Z audit-lake read.
- Ships in the r29 release (`OG-rl-15`, R55), not cut in this issuance.
- Pre-cut: see the issuance commit.

<status>complete</status>
<round>32</round>
<slot>~38</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
