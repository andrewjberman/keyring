# NFRA_OPLGTW task order -- `OG-en-14` -- the email-deny guard takes a route class: a restricted master_admin passes the Opal-internal browser routes, a denied non-admin stays refused (round 39 E4; CTO ruling @e511fa0194 shape a)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-14</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-14</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~127</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the guard reads the same deny record it reads today.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_EMAIL_DENY_SIDE_EFFECT_OF_OG_MG_1_20261016_Z.md` item 2 (shape a) and the CRO's cause note `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_BROWSER_DENY_LIST_CAUSE_20261016.md`.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-14` (decomposition addendum R3-T.99, round 39 item E4, workstream ENRICH-R39-B)

THE GAP. `app/data_entitlement.py` `email_denial(email, store=None)` (line ~879) answers 403 when an `email_deny` record exists for the normalised email, 503 when the store is unreadable, else None. The browser routes `/login`, `/sprint*`, `/rivalfunds*` and `/yearinreview*` (`app/server.py`, the branch near line 206; they call `_email_denied(email)`, line ~436) refuse a denied email BEFORE anything else. The record carries no scope, so a principal made restricted for DATA reasons (a Schwab data-grant profile) is also refused the Opal-internal pages. That cut the two Opal owners off their own browser apps at 11:22Z (CRO cause note). The four routes serve Opal-internal pages, not restricted client data.

THE FIX (code only; read the code first). Give the guard a ROUTE CLASS and an OWNER EXEMPTION:
- In `app/data_entitlement.py` add a small module table `BROWSER_ROUTE_CLASSES` mapping each of the four route families to the class `"internal_page"` (and the legacy `/callback` consent branch to its existing behaviour: it stays exactly as today), and extend `email_denial(email, store=None, route_class=None)`: when `route_class == "internal_page"` AND the normalised email is in `cfg.MASTER_ADMIN_EMAILS` (read through the module's existing config access; case-insensitive, exact match, never a substring), return None BEFORE the store read (no read for an owner on these routes). Every other case is unchanged: a denied email that is not a master admin is refused (403) on all four routes; an unreadable store still fails closed (503) for a non-admin; `route_class=None` (every existing caller, including `app/token_broker.py`) behaves EXACTLY as today.
- In `app/server.py` pass `route_class="internal_page"` from the single browser branch (`_email_denied` gains the argument and forwards it), and from nowhere else.
- Change nothing in the MCP tool admission, in `access_state.py` or in the deny record's shape. The restricted PROFILE and grants of a master_admin stay as written; only the browser guard changes.

TESTS (new file `tests/test_og_en14.py`; read `tests/test_owner_gate.py` and `tests/test_login_admit_r24.py` for the fake store and request fixtures):
- `test_ogen14_ac01`: for each of the four route families, a master_admin email (from `MASTER_ADMIN_EMAILS`) WITH an active deny record passes (None), and the fake store records ZERO reads for it.
- `test_ogen14_ac02`: for each of the four route families, an email that is NOT a master admin (use `alyssa@opalinvest.com`) WITH an active deny record is refused 403, and the same email with an unreadable store is 503.
- `test_ogen14_ac03`: `email_denial(email)` with no `route_class` is byte-for-byte today's behaviour for a master_admin with a deny record (403) and for an email with no record (None); a lookalike (`andrew@opalinvest.com.evil`, `xandrew@opalinvest.com`) is NOT exempt.
If an existing test pins the old call signature or the master admin's refusal on a browser route, update it to the new truth with the smallest edit and name it in your report; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no registry change, no change to any deny record.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_og_en14.py
infra/aws/ec2/opal-gateway/tests/test_owner_gate.py
infra/aws/ec2/opal-gateway/tests/test_login_admit_r24.py
infra/aws/ec2/opal-gateway/tests/test_scoped_consent_r253.py
infra/aws/ec2/opal-gateway/tests/test_og_en8.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/data_entitlement.py`, `app/server.py` (the one branch and `_email_denied`), `tests/test_og_en14.py` and, only to follow the new truth, the existing tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~127/`. Rows: id `NFRA_OPLGTW-Z-W127-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-14"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en14.py test_ogen14_ac01 test_ogen14_ac02 test_ogen14_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-14"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~127 '^infra/aws/ec2/opal-gateway/(app/(data_entitlement|server)\.py|tests/(test_og_en14|test_og_en8|test_owner_gate|test_login_admit_r24|test_scoped_consent_r253)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~127: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass. `AC2`: the commits of this serial touch only the listed files.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-14.email-deny-route-class-guard.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 39 E4, workstream ENRICH-R39-B (decomposition addendum R3-T.99). Risk WORLD by the L6 floor (a gateway infrastructure path); no deploy in this cell; it rides the next batched gateway release with `OG-en-13`, `OG-en-15` and `MX-c-24`.
- Reading of the CTO's ruling: the four browser routes serve Opal-internal pages, so the route class is `internal_page` and the exemption is the owner roster (`MASTER_ADMIN_EMAILS`); Alyssa (restricted since 09-27, intended deny) stays refused. `opalbloomberg@` is write-capable, not master admin: after `OG-ap-30` it has no deny record, and the guard does not exempt it.
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

<status>complete</status>
<round>39</round>
<workstream>ENRICH-R39-B</workstream>
<slot>~127</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
