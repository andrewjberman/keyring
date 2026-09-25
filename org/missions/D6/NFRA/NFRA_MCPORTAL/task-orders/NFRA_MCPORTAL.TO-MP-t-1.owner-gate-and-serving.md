# NFRA_MCPORTAL task order -- `MP-t-1` -- HOP 2: only Andrew, checked on the server, and the dashboard served at /

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-t-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface is written; the ALB rules are untouched.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: NONE. Tests use stubs; no network.
</preflight>

## 1. THE CELL -- `MP-t-1` (round 1, decomposition s.2/s.3)

The gateway at `infra/aws/ec2/opal-gateway/` (Starlette; its routes are listed at `app/server.py:~826-873`) will serve
Andrew's dashboard at `/`. The load balancer already sends every non-bypassed path through Microsoft sign-in
(`infra/aws/terraform/opal-gateway/alb.tf:210`, "the future GUI path"), which admits ANY tenant account. So the gateway
must check, on the SERVER, on every page request and every admin write, that the verified identity is Andrew's (PRD
C2). A hidden menu never counts as access control. Build:
1. **`app/owner_gate.py`** (new):
   - a dashboard-owner list whose ONLY purpose is this dashboard, read from config key `DASHBOARD_OWNER_EMAILS` (add it
     to `app/config.py`). It is NOT `MASTER_ADMIN_EMAILS`, which `app/tier.py:74` documents as "andrew@ + systems
     allowlist";
   - the list may hold only `andrew@opalinvest.com`. **Any other entry refuses BOOT** with a clear error. An UNSET or
     empty list does NOT stop the gateway (the MCP serves colleagues); it makes the dashboard refuse every request
     (fail closed);
   - the identity comes ONLY from the ALB-signed `x-amzn-oidc-data` header, verified by the existing
     `_alb_oidc_identity` (`app/identity.py:50-62`, ES256 against the regional ELB key), and is exact-matched,
     case-insensitive, against the list;
   - a missing or failing header is refused. Refusals are 403 (or 401 for no identity) with no page body.
2. **`app/admin_api.py`** (new): the admin router under `/api/admin/`, every handler behind the owner gate. Its first
   route is `GET /api/admin/whoami`, which returns the verified owner email. Later cells add handlers to this router.
3. **`app/server.py`**:
   - mount the admin router;
   - serve the static dashboard bundle at `/` from a configured directory (config key `DASHBOARD_BUNDLE_DIR`, default
     `dashboard/` beside `app/`), behind the owner gate;
   - a missing bundle dir serves a plain 503 page to the owner, never a crash;
   - leave `/sprint*`, `/mcp`, the OAuth and well-known paths, `/health` and every existing route exactly as they are.
     `/sprint` stays open to any signed-in Opal account.
   **Route order matters**: a `/` mount must not shadow the existing routes.
4. **`tests/test_owner_gate.py`** (new), with stubs for the header verification (never the network), naming exactly:
   `test_owner_page_served`, `test_non_owner_refused_page_and_handler`, `test_missing_or_forged_header_refused`,
   `test_boot_refuses_extra_owner_entry`, `test_sprint_served_to_non_owner`.

## 2. BOUNDS

1. Nothing is deployed by this order. `deploy-to-ec2.sh` (which writes the host's `.env`) is NOT yours; the deploy cell
   adds `DASHBOARD_OWNER_EMAILS` there.
2. At the cut on this box: `tests/test_sprint_view.py` 8 passed; `tests/test_identity_scope.py` 5 passed, 1 failed
   (`test_scoped_deny_by_default`, red before you start). `moto` is not installed; do not install it.
3. Standing: no push, no install, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and report the
   refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/owner_gate.py
infra/aws/ec2/opal-gateway/app/admin_api.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/tests/test_owner_gate.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~2/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `app/identity.py`, `app/sprint_view.py`, `app/tier.py`, `app/guard.py`, `tests/conftest.py` (under
`infra/aws/ec2/opal-gateway/`).

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_MCPORTAL-Z-W2-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t1.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 5 of 5; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-t-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t1.AC2.sh; echo "exit=$?"</invocation><expect>sprint: 8 passed (no failure); identity_scope passed>=5, failures not present at the cut=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~2/NFRA_MCPORTAL.TO-MP-t-1.owner-gate-and-serving.proof_of_spec.json`. Report once: what you changed and where, the commit hash, how the `/` mount sits in the route order, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** S2 + S3. Merge HELD until NFRA_OPALAI's OA-t-6 deploy entry closes (decomp sequencing (b)). The second
signed-in account's live refusal is the close run's.

<status>complete</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
