# TO NFRA_CLDGRPH.TO-CG-D-2 -- the GATEWAY TRAVERSAL: the served projection reached THROUGH the opal gateway as a THIN PROXY -- (a) an `IntegrationSpec` integration `globgrph` (AuthKind.NONE, read-only, `graph_` tools) built and registered DORMANT through the framework's 5-step checklist with the framework UNMODIFIED, and (b) a static-capability-bearer HTTP path `/graph/cypher` + `/graph/health` (the `/ms/*` precedent) so a NON-gateway seat -- a laptop CLI with AWS credentials -- gets the service's answer over HTTPS; deployed on the box, exercised from this seat; the MCP integration's ENABLE flip left to the CTO's arch-gate (G8)

<to_id>NFRA_CLDGRPH.TO-CG-D-2</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~2</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO = the spawn itself (spine v3 L6/L7). ROUND 4 of NFRA_CLDGRPH (the ONE issuance covering every open cell, Andrew's word via CRO record @aff3bfb7bf), slot ~2's FIRST order; STAGE 2's second cell, released by CG-s-4 DONE (@028be96aef: the service answers at `projection.opal-globgrph.local:8181`) and CG-s-13 DONE (@9b59f39114: `AuthKind.NONE`). Marked HARD by the issuer (a live deploy of the employee-facing gateway; opus). The assignee commits its own status flip after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (FWD-1, FWD-5; s.7 row S5; R3 "the gateway is NEVER the host") · **Decomp cell:** `CG-s-5` (v0.2 @`70918d5d2b`) · **Lane:** `infra/aws/ec2/opal-gateway/` (the gateway app + its deploy script), `infra/aws/terraform/opal-gateway/` (the secret, the role grant, the ALB rule), the change-management ledger · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~2`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~2;`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~2 <0.9.0_WK_NFRA_CLDGRPH~2@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/`.** A path you need that the block lacks is a BLOCKING row on that criterion, never an override.
- **Surprise = ONE ROW, never a message.** Append to `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` a new `## <id> -- <title>` section with a fenced json array holding one object (copy the S28 row's field set in that file); id `NFRA_CLDGRPH-W2-S<k>`, `<k>` next unused within W2 (start at 1); restate the header denominator line; never edit an existing row; keep working.
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most. The deploy script's own SSM poll is a deliverable step, not a criterion: run it with `timeout 600`, and if it times out, finish the read with `.tools/aws ssm get-command-invocation` (the box completes regardless of your shell).
- **NEVER:** `terraform apply` bare (use `bash .tools/safe-apply` -- read its header first); `git commit` bare; put a secret VALUE in the repo, a log, a message or a commit; write to a firm data bucket; build an alarm/SNS/monitor; touch `GATEWAY_WORKERS=1` / `--workers 1`; add `globgrph` to `ENABLED_INTEGRATIONS` (G8 is the CTO's, see below); non-ASCII in code/logs; `2>/dev/null` a read whose emptiness is a verdict.
- **Rule 12 (EC2 code delivery):** code reaches the box ONLY through `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (local -> S3 -> SSM pull). No SSH, no inline Python in SSM, no file written by hand on the box.
- **NEVER-2 BINDS:** open a deploy ledger (`python .tools/deploy_ledger.py open ...`, name `cldgrph-cgd2-gateway-graph-path`) BEFORE the first apply/deploy act with every leg; close each leg with proof; close the entry.
- **Search rail:** `python .tools/comp-read <file> --for "..."` / `--enumerate '<regex>'`; `python .tools/comp-find '<pattern>' <pathspec>`; raw recursive grep/find in Bash is refused. AWS CLI = `.tools/aws`.

## THE CELL (verbatim, decomposition v0.2 s.1a)

> **CG-s-5** | S5 gateway traversal registered via `IntegrationSpec` | FWD-1, FWD-5 (acc 1, 5) | claim: absent | status: OPEN | evidence: `registry.py` 67 @`2781aac326` (2 live integrations, `ENABLED_INTEGRATIONS` CTO-arch-gated `:34`); `opal-gateway-role` (10 statements, DESIRED) holds NOTHING on the globgrph bucket and no ECS/service-discovery action -- so either the proxy needs no new grant (pure HTTP inside the VPC) or S12 names the delta; the deliverable says which | lane `0.7.0_AE_CloudOps` | placement laptop | depends_on: CG-s-4 -> the service answers; CG-s-13 -> the AuthKind named | **closes on:** a seat that is not the gateway host issues one traversal through the gateway and gets the service's answer; the framework file diff is the 5-step checklist only (the bound that can fail)

**PRD s.7 row S5 (the manifest):** "gateway traversal registered via `IntegrationSpec` (existing framework) | absent | framework proven by 2 live integrations (`opal_portal`, `ycharts`): `infra/aws/ec2/opal-gateway/app/integrations/registry.py:23-35` | wire | depends S4, S13 | **The framework is NOT modified** -- a new integration through its 5-step checklist. Gateway `i-07dccb1615503ac99` t4g.nano, `--workers 1` MANDATORY: thin proxy only. `ENABLED_INTEGRATIONS` flip is CTO-arch-gated (`registry.py:34`)".

## MEASURED BY THE ISSUER AT THE CUT (2026-09-04 06:2xZ), so you do not re-derive it

- **The service (CG-s-4, DONE):** `http://projection.opal-globgrph.local:8181`, in-VPC only (`sg-0e85dd853fbe5584e`: tcp/8181 from `172.31.0.0/16`), `AuthKind.NONE`. `POST /cypher` with `Content-Type: text/plain` and ONE Cypher statement as the body (JSON `{"statement": "..."}` also accepted; body 1..1048576 bytes) -> `{"rows":[...],"vintage":"...","age_line":"Built from the estate as of YYYY-MM-DD HH:MM:SS UTC.","manifest_sha256":"...","artifact_prefix":"..."}`; `GET /health` -> the manager's health dict (vintage, last_swap, pointer_read_at ...). Source `infra/aws/globgrph/projection_server.py:477-500` @`8f0dff109f`. The gateway host `i-07dccb1615503ac99` (`172.31.89.135`, same VPC `vpc-0cc0c6a75e54605e3`) reached it with HTTP 200 in 0.026 s (C-1 SSM `2e708112-9eec-44ef-9e65-4eeded137343`). **CG-s-11: REACHABLE, no SG/route change needed. CG-s-12: the gateway IAM delta is EMPTY by design -- "the moment `opal-gateway-role` needs `s3:GetObject` on the globgrph bucket, R3 has been broken" (V-2 result B.3(iii)).** So the proxy holds NO S3 grant; the ONLY IAM this order adds is `secretsmanager:GetSecretValue` on ONE new secret ARN (the bearer), the exact shape `infra/aws/terraform/opal-gateway/ms-ingest.tf:16-17,47` uses for `opal/mcp/ms-ingest-token`.
- **The framework:** `infra/aws/ec2/opal-gateway/app/integrations/base.py` (`AuthKind.NONE` at `:44`; `IntegrationSpec` `:47-67`; `run_integration_tool` `:93-139`; `validate_integration_spec` `:142-169` -- **`hosts` MUST be non-empty or the spec is skip-registered silently**, V-2 result C; declare `hosts=("projection.opal-globgrph.local",)`); `registry.py:37` holds the pre-written slot `# Future (read-only in-estate graph surfaces): kuzu / nessie / iceberg -> register here.`; the two live integrations at `app/integrations/ycharts/` and `app/integrations/opal_portal/` are your specimens (`comp-read` each package's `integration.py --for "the IntegrationSpec, register(mcp), and how tools route through run_integration_tool"`). **sha256 of `base.py` at the cut (via `git show HEAD:`): `718246435530d59e853ed7dca99791d59e1b629e2df516b6a98c3146902cf616` -- byte-identical after, D2-AC2.** The standard: `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` s.5 (the 5-step checklist, `:86-102`), s.6 (fail-closed enablement), s.8.1 (the arch-gate G1-G8, `:151-182`).
- **The capability-path precedent (what a NON-MCP caller uses):** `app/ms_ingest.py` (`check_bearer`: `hmac.compare_digest` over the `.env` bearer list; `configured()`), routes in `app/server.py:605-613` (`/otp/fetch`, `/otp/health`, `/ms/*`) mounted OUTSIDE the `/mcp` guard (a static bearer is not a JWT; `server.py:521-535`), and the ALB listener rule that admits those paths (`infra/aws/terraform/opal-gateway/alb.tf:219-234` `otp_capability` priority 30, `path_pattern values = ["/otp/fetch","/otp/health"]`; locate the `/ms/*` rule with `python .tools/comp-find '/ms/' infra/aws/terraform/opal-gateway --limit 8` and copy its shape: a new rule `graph_capability`, next free priority, values `["/graph/cypher","/graph/health"]`). The bearer reaches the box through `deploy-to-ec2.sh`: an `aws secretsmanager get-secret-value` line into the `.env` printf (see `MS_INGEST_BEARER` there), never in the SSM command text.
- **The deploy path:** `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (S3 -> SSM; restarts the unit; bounded health wait; on-box md5s). `PUBLIC_BASE_URL=https://mcp.opalinvest.dev`; the ALB in front authenticates `/mcp` by OIDC and forwards the capability paths by listener rule. The deploy script's current `ENABLED_INTEGRATIONS=ycharts opal_portal` line (exactly ONE occurrence at the cut) stays byte-identical -- D2-AC5.

## DELIVERABLE -- in this order

1. **MEASURE FIRST (read-only):** the two specimen integrations; `ms_ingest.check_bearer` + the `/ms/*` routes + the `/ms/*` ALB rule + the `ms-ingest.tf` secret/grant; the deploy script's secret-fetch lines. Quote `file:line` for each in the deliverable.
2. **(a) The integration** `app/integrations/globgrph/{__init__.py,integration.py}`: `IntegrationSpec(id="globgrph", display_name="Estate graph (Kuzu projection)", auth_kind=AuthKind.NONE, tool_prefix="graph_", read_only=True, min_tier="read_only", hosts=("projection.opal-globgrph.local",))`; ONE proxy function `query(statement: str) -> dict` that POSTs the statement as `text/plain` to `http://projection.opal-globgrph.local:8181/cypher` with a 20 s timeout and returns the service's JSON verbatim (rows, vintage, age_line, manifest_sha256, artifact_prefix), and `health() -> dict` for `GET /health`; `register(mcp)` adds exactly two tools, `graph_cypher(statement)` and `graph_status()`, each routed through `run_integration_tool(...)` with a credential provider that returns `None` (NONE has no WHICH; WHO is still audited). The proxy never reads S3, never caches an artifact, never rewrites a statement. Register the factory in `registry.py` at the pre-written slot (`register_factory("globgrph", GlobgrphIntegration)`).
3. **(b) The capability path** `app/graph_read.py` (bearer check copied from `ms_ingest.check_bearer`, env `GRAPH_READ_BEARER`; `configured()`), routes `POST /graph/cypher` and `GET /graph/health` in `server.py` beside the `/ms/*` routes, calling the SAME proxy function from (a) (one implementation, two surfaces); a missing/wrong bearer -> 401 JSON `{"error":"unauthorized"}`; a misconfigured box -> 503. The ALB rule `graph_capability` in `alb.tf`. `config.py` gains `GRAPH_READ_BEARER` the way `MS_INGEST_BEARER` is read.
4. **The secret + grant (Terraform, `infra/aws/terraform/opal-gateway/graph-read.tf`, new):** `random_password` (48 chars, no special) -> `aws_secretsmanager_secret` `opal/mcp/graph-read-token` + `aws_secretsmanager_secret_version`; an `aws_iam_role_policy` on the gateway instance role granting `secretsmanager:GetSecretValue` on EXACTLY that ARN (copy `ms-ingest.tf`'s grant shape; the role name is in `main.tf`). **Targeted `safe-apply` on exactly your new addresses + the ALB rule** (list them in the ledger); then ONE unscoped `terraform plan` saved to a file and asserted BY ADDRESS LIST to contain none of your addresses (the C-1 method); the value is never printed.
5. **`deploy-to-ec2.sh`:** add the `GRAPH_READ_BEARER=$(aws secretsmanager get-secret-value --secret-id opal/mcp/graph-read-token ...)` fetch beside `MS_INGEST_BEARER`, and `GRAPH_READ_BEARER=%s` into the `.env` printf. Do NOT touch the `ENABLED_INTEGRATIONS=` value (the `globgrph` id is built and registered DORMANT: `validate_integration_spec == []` proven locally, ZERO `graph_` tools added to the live MCP surface -- G7).
6. **Deploy** via `safe-ec2-deploy.sh`; box-verify by SSM (bounded): the unit active, `/health` 200, `/graph/health` from the box `curl -sS -H "Authorization: Bearer $(grep GRAPH_READ_BEARER /opt/opal-gateway/.env | cut -d= -f2-)" http://localhost:8080/graph/health` -> 200 with `vintage`; the journal's startup integration report lists `ycharts` and `opal_portal` and NOT `globgrph` (dormant); `ps` shows `--workers 1`.
7. **THE EXERCISE (the closes-on): from THIS seat, not the box** -- `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/graph_query.sh` (yours): reads the bearer from Secrets Manager with the seat's AWS credentials into a shell variable (never echoed), POSTs `MATCH (n) RETURN count(n) AS nodes` to `https://mcp.opalinvest.dev/graph/cypher`, prints the response JSON whole. Then the negative control: the same POST with no `Authorization` header -> HTTP 401.
8. **Arch-gate record G1-G8** (`NFRA_INTEGRATIONS_STANDARD.md:151-182`) as a table in the deliverable, each item with its grounded evidence (G1 validator `[]` + tools read-only; G2 `hosts` exact; G3 the two `graph_` tools enumerated; G4 the live `get-role-policy` on exactly the one ARN; G5 `min_tier` + the below-tier deny is N/A for `read_only` (say so); G6 the audit record for one ok and one denied call read from the box's `audit.jsonl`; G7 dormant proven on the deployed bytes; G8 = the CTO's signature, which is NOT yours: record "AWAITING the round-N analysis" -- the COO carries it in the drain-end read). Then the deliverable `CG-s-5.gateway-traversal.result.md`, close the ledger, the proof instance, validate, flip, commit.

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="D2-AC1" cell_refs="CG-s-5"><invocation>cd infra/aws/ec2/opal-gateway && python -c "from app.integrations.globgrph.integration import GlobgrphIntegration; from app.integrations.base import validate_integration_spec; print('VALIDATE', validate_integration_spec(GlobgrphIntegration().spec))"</invocation><expect>VALIDATE \[\]</expect></criterion>
`D2-AC1` -- THE SPEC VALIDATES (the machine half of G1-G4): `validate_integration_spec` returns `[]`.

<criterion id="D2-AC2" cell_refs="CG-s-5"><invocation>git show HEAD:infra/aws/ec2/opal-gateway/app/integrations/base.py | sha256sum | cut -d' ' -f1</invocation><expect>718246435530d59e853ed7dca99791d59e1b629e2df516b6a98c3146902cf616</expect></criterion>
`D2-AC2` -- THE FRAMEWORK IS NOT MODIFIED: `base.py` byte-identical to the cut (hashed through `git show`, never the worktree path -- an autocrlf checkout hashes the checkout, not the record). The bound that can fail.

<criterion id="D2-AC3" cell_refs="CG-s-5"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/graph_query.sh</invocation><expect>"rows":\s*\[\{"nodes":\s*[1-9][0-9]*\}\].*"vintage":\s*"20[0-9]{2}-</expect></criterion>
`D2-AC3` -- A NON-GATEWAY SEAT GETS THE SERVICE'S ANSWER THROUGH THE GATEWAY: this seat's HTTPS call returns rows AND the vintage the service stamped.

<criterion id="D2-AC4" cell_refs="CG-s-5"><invocation>curl -sS -m 20 -o /dev/null -w '%{http_code}' -X POST -H 'Content-Type: text/plain' --data 'MATCH (n) RETURN count(n) AS nodes' https://mcp.opalinvest.dev/graph/cypher</invocation><expect>^401$</expect></criterion>
`D2-AC4` -- NO BEARER, NO ANSWER: the same path without `Authorization` is refused with 401 (the fail-closed control).

<criterion id="D2-AC5" cell_refs="CG-s-5"><invocation>python .tools/comp-read infra/aws/ec2/opal-gateway/deploy-to-ec2.sh --enumerate 'ENABLED_INTEGRATIONS=ycharts opal_portal' --limit 3</invocation><expect>ENUMERATE: 1 hit\(s\)</expect></criterion>
`D2-AC5` -- THE MCP INTEGRATION LANDS DORMANT: the deploy script's `ENABLED_INTEGRATIONS` value is unchanged (exactly one occurrence, `globgrph` absent from it); G7/G8 hold.

<criterion id="D2-AC6" cell_refs="CG-s-5"><invocation>.tools/aws iam list-role-policies --role-name opal-gateway-role --output text</invocation><expect>graph</expect></criterion>
`D2-AC6` -- THE ONE NEW GRANT IS APPLIED (not merely declared): the gateway role carries the new inline policy for the graph-read secret; the deliverable quotes `get-role-policy` showing `secretsmanager:GetSecretValue` on EXACTLY that secret's ARN and nothing on any globgrph S3/ECS resource (the R3 control from V-2 B.3(iii)). If the role name differs from `opal-gateway-role`, resolve it from `infra/aws/terraform/opal-gateway/main.tf` and say so in the row you file.

<criterion id="D2-AC7" cell_refs="CG-s-5"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/box_workers.sh</invocation><expect>--workers 1</expect></criterion>
`D2-AC7` -- `--workers 1` UNTOUCHED on the deployed box (`box_workers.sh`, yours: an SSM `ps -o args -C python3.11` on `i-07dccb1615503ac99`, output printed whole).

<criterion id="D2-AC8" cell_refs="CG-s-5"><invocation>bash .tools/commit-gate.sh infra/aws/ec2/opal-gateway/app/integrations/globgrph/integration.py infra/aws/ec2/opal-gateway/app/graph_read.py infra/aws/ec2/opal-gateway/app/server.py infra/aws/ec2/opal-gateway/app/integrations/registry.py infra/aws/ec2/opal-gateway/app/config.py</invocation><expect>pre-commit gate clean</expect></criterion>
`D2-AC8` -- COMMIT GATE clean on every `.py` this order touches.

<criterion id="D2-AC9" cell_refs="CG-s-5"><invocation>python .tools/deploy_ledger.py list</invocation><expect>cldgrph-cgd2-gateway-graph-path.*CLOSED</expect></criterion>
`D2-AC9` -- THE LEDGER CLOSED with every leg proven (NEVER-2).

<criterion id="D2-AC10" cell_refs="CG-s-5" judgment="true"/> `D2-AC10` -- THE ARCH-GATE RECORD G1-G8 with its grounding, and the framework DIFF read as "the 5-step checklist only" (the new package + the one `register_factory` line + the capability path files -- state whether the capability path is inside or beside the checklist, with the `/ms/*` precedent cited). A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9; G8's signature is the CTO's at L10.

<expected_criteria>D2-AC1, D2-AC2, D2-AC3, D2-AC4, D2-AC5, D2-AC6, D2-AC7, D2-AC8, D2-AC9, D2-AC10</expected_criteria>

## SURFACES

`infra/aws/ec2/opal-gateway/app/integrations/{base.py (READ ONLY), registry.py, ycharts/, opal_portal/}` · `infra/aws/ec2/opal-gateway/app/{server.py, config.py, ms_ingest.py (READ), graph_read.py (NEW)}` · `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` · `infra/aws/ec2/safe-ec2-deploy.sh` (READ; the wrapper) · `infra/aws/terraform/opal-gateway/{alb.tf, ms-ingest.tf (READ), main.tf (READ), graph-read.tf (NEW)}` · `infra/aws/globgrph/projection_server.py:477-500` (READ: the API) · `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` (READ) · `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~P/CG-s-11-12-13.reachability-iam-authkind.result.md` (READ: sections B.3(iii) and C) · `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/CG-s-4.serving-service.result.md` (READ: "CG-s-5 handoff").

## BOUNDS

- **The framework is NOT modified** (`base.py` byte-identical; `registry.py` gains one factory line at the pre-written slot; nothing in `tools.py`, `guard.py`, `tier.py`, `audit.py`).
- **The gateway is a THIN PROXY:** no S3/ECS/service-discovery grant on the gateway role; no artifact cached on the box; no statement rewriting; `--workers 1`.
- **`ENABLED_INTEGRATIONS` is NOT flipped** (G8: the CTO's arch-gate; a flip here is a violation of `NFRA_INTEGRATIONS_STANDARD.md` s.6/s.8). The capability path is live on deploy by construction of its class (the `/otp/*` and `/ms/*` precedents); D2-AC10 records that reading for the CVO.
- **One deploy.** If the health wait fails, read the journal (the deploy script prints it), file a BLOCKING row, and report -- do not re-deploy blind, do not edit the unit by hand.
- **No secret value anywhere but Secrets Manager and the box's `.env`.**
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
infra/aws/ec2/opal-gateway/app/integrations/globgrph/
infra/aws/ec2/opal-gateway/app/integrations/registry.py
infra/aws/ec2/opal-gateway/app/graph_read.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/terraform/opal-gateway/graph-read.tf
infra/aws/terraform/opal-gateway/alb.tf
org/critical_paths/change_management/
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-2.gateway-traversal-integration.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> @70918d5d2b (v0.2), cell CG-s-5 (s.1a; STAGE 2, "the serving plane + the reach").
<owned_cells>CG-s-5</owned_cells>
Read-dependencies, NOT claimed: CG-s-4 (DONE @028be96aef), CG-s-11 (DONE @9b59f39114, REACHABLE), CG-s-12 (DONE, the empty gateway delta), CG-s-13 (DONE, AuthKind.NONE). Downstream, NOT yours: CG-s-6 (the thin client consumes `/graph/cypher`), CG-x-1, CG-x-5.
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-04 06:2xZ at the cut: GATES ARMED 21 across 5 carriers (C1 21 -> 5, C2 4, C3 12, C4 20, C5 337); NEEDS-READ 138 prose fields (a reading list, never counted); the standing moratoria (C3) bind this face's BOUNDS.
comp-iam: RUN -- V-2's census (2026-09-03T06:46:12Z, 216 roles; refreshed 18:43:46Z by C-1, 221 roles): `opal-gateway-role` 10 statements DESIRED, 0 drift on 9 resolved, 1 attached-managed UNRESOLVED (AmazonSSMManagedInstanceCore), 0 of 10 on globgrph on BOTH planes. The delta this order adds is ONE `secretsmanager:GetSecretValue` statement on ONE new secret ARN. comp-iam cannot answer "is this denied?" -- the APPLIED read (`get-role-policy`) is D2-AC6's own act. Run `python .tools/comp-iam refresh-census` before any APPLIED read (24 h TTL).
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5, 22/22 cited commits VERIFIED); the deliverable's validator context is the L9 seat's compose, not the cut's.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `D2-AC1`..`D2-AC10`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-D-2.gateway-traversal-integration.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> D2-AC1,D2-AC2,D2-AC3,D2-AC4,D2-AC5,D2-AC6,D2-AC7,D2-AC8,D2-AC9,D2-AC10` BEFORE the complete flip, which the WORKER commits itself on its own branch with the instance and the deliverable. `D2-AC2` (byte-identical framework), `D2-AC4` (401) and `D2-AC5` (dormant) are the controls that must be able to FAIL. `D2-AC10` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.**
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `python .tools/comp-read infra/aws/ec2/opal-gateway/app/integrations/ycharts/integration.py --for "the IntegrationSpec, register(mcp), the credential provider and how each tool routes through run_integration_tool"`; `python .tools/comp-read infra/aws/ec2/opal-gateway/app/server.py --for "how the /ms/* and /otp/* capability routes are mounted outside the /mcp guard and how their bearer gate is applied"`; `python .tools/comp-read infra/aws/ec2/opal-gateway/deploy-to-ec2.sh --for "every secret fetched into the .env and the printf that writes it"`; `python .tools/comp-find '/ms/' infra/aws/terraform/opal-gateway --limit 8`. BEFORE COMMIT: `bash .tools/commit-gate.sh` on every `.py` touched (D2-AC8); `terraform fmt -check` on the new `.tf`. AFTER DEPLOY: the box-verify SSM reads quoted whole.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the spawn itself.**
