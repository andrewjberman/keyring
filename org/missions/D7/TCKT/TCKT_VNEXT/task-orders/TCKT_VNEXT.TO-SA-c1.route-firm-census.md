# TO TCKT_VNEXT.TO-SA-c1 -- census every portal /api/scoped route: what firm reach would a one-firm test filer token get

<to_id>TCKT_VNEXT.TO-SA-c1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~6</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SA</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL (read-only census of source; no AWS call) | **Decomp cell:** `SA-c-1`
(`decompositions/TCKT_VNEXT_DECOMP_SA.md`) | **outcome_ref:** FWD-1 (seat-driven arm, CTO msg 2327) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~6`. Your worktree is `C:/tmp/tckt-sa-1` (branch `wk-tckt_vnext-sa-1`, cut from box/dell2 at the issuance
commit). Commit there with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~6 <0.9.0_WK_TCKT_VNEXT~6@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool.

### THE CELL

`SA-c-1`. TCKT_VNEXT must run FWD-1 once as a seat: one Analysis Request filed, claimed, generated and opened from its ticket, all
through the real portal API.

**The principal.** The run needs a synthetic INTERNAL test filer with ONE signed token (2 hours). The CTO refused any token whose
reach is more than ONE firm on ANY `/api/scoped/*` route (msg 2342): "the synthetic test-filer row is clamped to ONE firm (49financial)
on every /api/scoped route it can reach ... Print the route census (N) with another firm refused on each."

**Your job is the census, READ-ONLY, from source.**

1. **Enumerate every route on the portal API Gateway.**
   - Collect every `aws_apigatewayv2_route` (and any `for_each` route map) whose `api_id` is the portal API, across ALL Terraform
     roots under `infra/`.
   - The portal API id is `local.portal_api_id` / the `opal-portal-api` HTTP API; find how each root names it.
   - `comp-routes api-routes` lists only some roots; do not trust it for completeness.
   - Record `roots_scanned` (every Terraform root you read) and `routes_found` (N).
2. **For each route, name its function** (the integration's Lambda) **and find WHERE in that function's source it derives a caller's
   firm reach.** That means the authorizer context fields it reads: `firmId`, `allowedFirmIds`, `tier`, `userType`, `role`, and any
   "internal = all" rule. Cite it as `path:line`. The authorizer is `infra/aws/users/lambda/portal-authorizer/index.mjs`; its
   `computeAllowedFirms` is at `:293-322`.
3. **For each of these candidate tokens, decide the route's verdict.** `allowedFirmIds` is computed by the authorizer from the claims:

   | name | claims |
   |---|---|
   | `T_ADVISOR_OPAL` | `firmId opal-capital`, `tier advisor`, `role user`, no `userType` |
   | `T_SERVICE_TIER_OPAL` | `firmId opal-capital`, `tier service`, `role user`, no `userType` |

   Verdict per route per token:
   - `ONE_FIRM`: reach is exactly one firm; name it in `firms`.
   - `NO_FIRM`
   - `MORE_THAN_ONE`: for example, the function treats `firmId opal-capital` as internal and therefore all firms.
   - `UNRESOLVED`: you cannot tell from source; say why in `note`.

   Also record `other_firm_refused`: true if a request naming a firm other than the reachable one is refused by the code you cited,
   false if not, null if not applicable.
4. **Write `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.json`:**
   ```json
   {"denominator": {"roots_scanned": ["infra/aws/terraform/..."], "routes_found": N},
    "candidate_tokens": [{"name": "T_ADVISOR_OPAL", "claims": {...}}, {"name": "T_SERVICE_TIER_OPAL", "claims": {...}}],
    "rows": [{"route": "/api/scoped/...", "method": "GET", "function": "<lambda name>", "firm_source": "path:line",
              "per_token": {"T_ADVISOR_OPAL": {"verdict": "...", "firms": [...], "other_firm_refused": true, "note": "..."},
                            "T_SERVICE_TIER_OPAL": {...}}}]}
   ```
   Also write a short `SA_ROUTE_CENSUS.md` beside it. It must say:
   - which token, if any, is ONE_FIRM or NO_FIRM on every route;
   - which routes break it, and the smallest code clamp that would fix each one, in the `COMMENTARY_ALLOWED_FIRMS` pattern.
   - The FWD-1 hops need the ticket service to treat the filer as INTERNAL (`firmId == opal-capital`). Say whether each token
     achieves that, and whether its ticket CREATE for firm `49financial` passes `_firm_allowed`.

### ACCEPTANCE

<criterion id="SA-c1-AC1" cell_refs="SA-c-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/SA_CHECKS/sa_checks.py sa-census</invocation><expect>SA-CENSUS-OK</expect></criterion>
`SA-c1-AC1`: the census is well formed and grounded. Rows equal N, and every `firm_source` path:line exists.

<criterion id="SA-c1-AC2" cell_refs="SA-c-1" judgment="true"/>
`SA-c1-AC2` (JUDGMENT, graded at L9, never self-graded): the census covers EVERY portal route (no root missed), and each verdict follows
from its cited line.

<expected_criteria>SA-c1-AC1 SA-c1-AC2</expected_criteria>

## BOUNDS

- READ-ONLY. No AWS call, no token, no deploy. Write only the `<paths>` below.
- No non-ASCII. If you need a row, append it in BINARY mode as `TCKT_VNEXT-D2-W6-S<k>`, as its own fenced block at the end of the file,
  keeping the file's line endings.

<paths>
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.json
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.md
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_SA.md</decomp_doc> (workstream SA, round 1), cell `SA-c-1`.
<owned_cells>SA-c-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SA-c1-AC1 SA-c1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/TCKT_VNEXT.TO-SA-c1.route-firm-census.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> SA-c1-AC1 SA-c1-AC2` before the flip. AC2 is recorded as judgment,
ungraded.
</proof_of_spec>

**REPORT (once):** the check line verbatim, N, the per-token verdict counts, the routes that break one-firm, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM; the census itself is the authorization read the CTO ordered.
comp-adversary: DECLARED-NOT-APPLICABLE -- the census IS the adversarial read of the token's reach.
</preflight>

Source: CTO msgs 2327 (seat arm approved) and 2342 (refusal: one firm on every route, with a census); the plan
`deliverables/2.0.0_SA_COO~V2/R1_RUN/TV_R1_SEAT_ARM_PLAN_AND_PAIR.md` @956788a328.

# pipeline-override: the mint and the run are issuer and applier acts after the census and any clamp cell; this issuance covers workstream SA round 1's one worker cell (SA-c-1).
