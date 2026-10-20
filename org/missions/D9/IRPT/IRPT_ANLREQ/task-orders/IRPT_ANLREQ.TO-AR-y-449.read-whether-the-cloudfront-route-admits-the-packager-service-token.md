# TO IRPT_ANLREQ.TO-AR-y-449.read-whether-the-cloudfront-route-admits-the-packager-service-token -- READ ONLY: from the source files, decide whether a package POST made with the packager's service Bearer token through the CloudFront alias of the portal (the route the portal itself uses) passes the edge function and the API authorizer; nothing is run, called or changed

<to_id>IRPT_ANLREQ.TO-AR-y-449.read-whether-the-cloudfront-route-admits-the-packager-service-token</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~321</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ108</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (no repository write beyond the worker's deliverables) | **Decomp cell:** `AR-y-449` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the packager attaches the four pointers; its direct execute-api call is refused 403 ORIGIN_VERIFICATION_FAILED) | **depends_on:** IB2 read A_PACKAGER_403.txt (the direct call is refused by the authorizer: ORIGIN_VERIFICATION_FAILED; the token is valid: sub svc-irpt-packager, userType service, tier service, exp 2027-01-09); CTO msg 11292 (route the packager through the same CloudFront route the portal uses; the authorizer is not changed; the origin secret is not handed to the resident)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~321`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-321` (branch `wk-IRPT_ANLREQ-321`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~321 <0.9.0_WK_IRPT_ANLREQ~321@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W321-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-449`, inlined)

*Context.* The packager (`infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py`, `live_ticket_ports`) sends `POST <api_base>/api/scoped/tickets/<id>/package` with `Authorization: Bearer <service token>` (a JWT: claims aud, exp, iat, iss, name, sub = `svc-irpt-packager`, tier = `service`, userType = `service`). Today `api_base` is the direct API Gateway host and the authorizer `opal-portal-authorizer` (REQUEST type, identity source `$request.header.Authorization`) answers 403 with the reason `ORIGIN_VERIFICATION_FAILED`, because the request did not come through CloudFront (CloudFront adds the custom origin header `X-Opal-Origin-Verify` on the origin `APIGateway-portal`). The CTO ruled the packager must call the ticket service through CloudFront, at the alias `https://opalinvest.dev` (the distribution's `aliases` list, `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` line 110). The behaviour for the path `/api/scoped/tickets/*` (same file, near line 539) allows POST, forwards all viewer headers except Host, and attaches a viewer-request Lambda@Edge function `auth-validator-edge` (`infra/aws/terraform/portal-auth/lambda-edge.tf`, function_name at line 86; find its source folder from that file).

*The question.* Would a request from a server process (no browser, no cookie, no session) with ONLY the headers `Content-Type: application/json` and `Authorization: Bearer <service token>` pass the edge function and then the API authorizer for that path? Read the sources, do not guess:
1. The edge function's source: what does it require on a viewer request for an `/api/scoped/*` path (a cookie, a bearer header, an origin or referer check, a particular user agent)? Does it accept an `Authorization: Bearer` JWT of tier `service`, and what does it do with a token it cannot verify or whose `tier` it does not know? Quote the decision lines as `file:line`.
2. The API authorizer's source (`opal-portal-authorizer`; find its source folder from the Terraform that declares it, `infra/aws/terraform/portal-auth/` or the API's Terraform): which reasons can it return, in what order (origin verification, then token), and what does it need beyond the header `X-Opal-Origin-Verify` (which CloudFront supplies) to admit a service-tier token? Quote `file:line`.
3. The ticket Lambda's route `package_ticket` (`infra/aws/lambda/ticket_center/lambda_function.py`): does it read any header or claim that CloudFront could change or strip (for example the client IP, a forwarded header, the origin)?
4. Decide. Write the four lines below; if a point cannot be decided from source, say `UNDECIDED` and name the one live read that would decide it (a single package POST to a bogus ticket id through the alias, which an operator can send).

*Record.* Create `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~321/` (the folder first) and write `A_EDGE_READ.txt` in it with EXACTLY four lines, ASCII only, no token or secret value:
`E1 edge function: <admits|refuses|conditional> a bearer service token for /api/scoped/tickets: <one clause> (<file:line>)`
`E2 authorizer: <admits|refuses|conditional> a service-tier bearer once the origin header is present: <one clause> (<file:line>)`
`E3 ticket Lambda: <nothing CloudFront alters|reads <header or claim>>: <one clause> (<file:line>)`
`E4 PACKAGER-VIA-CF-<ADMITTED|REFUSED|UNDECIDED> <one clause; for REFUSED or UNDECIDED the next live read or the change it needs>`
Commit the file. Write the proof instance (shape in your worker definition; `controls.mutant`: a copy of the record with the E4 word changed to MAYBE must make criterion AR449-y-AC3 NOT match; `controls.determinism`: run AC1 twice, same output).

---

## ACCEPTANCE

<criterion id="AR449-y-AC1" cell_refs="AR-y-449"><invocation>grep -c -E '^(E1|E2|E3|E4) ' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~321/A_EDGE_READ.txt</invocation><expect>^4$</expect></criterion>
<criterion id="AR449-y-AC2" cell_refs="AR-y-449"><invocation>grep -c -P '[^\x00-\x7F]' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~321/A_EDGE_READ.txt</invocation><expect>^0$</expect></criterion>
<criterion id="AR449-y-AC3" cell_refs="AR-y-449"><invocation>grep -c -E '^E4 PACKAGER-VIA-CF-(ADMITTED|REFUSED|UNDECIDED) ' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~321/A_EDGE_READ.txt</invocation><expect>^1$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~321/IRPT_ANLREQ.TO-AR-y-449.read-whether-the-cloudfront-route-admits-the-packager-service-token.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-449.read-whether-the-cloudfront-route-admits-the-packager-service-token`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR449-y-AC1,AR449-y-AC2,AR449-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-449</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~321/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-449.read-whether-the-cloudfront-route-admits-the-packager-service-token.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source files and one record file in the worker deliverables; nothing is run, called, built or changed.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CTO ruling, IB2's A_PACKAGER_403.txt and the CloudFront file against this cell; the lens: a guess presented as a reading (every E line quotes file:line), a printed token or secret, a claim about the LIVE edge function version from the Terraform alone (the file says `:13` when edge is not enabled: say which applies). NOT seen (blind): the live edge function and authorizer versions; denominator: three criteria.
</preflight>
