# TO NFRA_OPSWKF.TO-OW-p1 -- the trade request form: one ticket, then one engine submit carrying its id

<to_id>NFRA_OPSWKF.TO-OW-p1</to_id>
<project>NFRA_OPSWKF</project>
<issued_to>0.9.0_WK_NFRA_OPSWKF~5</issued_to>
<issued_by>2.0.0_SA_COO~O2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal component landing on DEV; CTO review route: product file) | **Decomp cell:**
`OW-p-1` | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_NFRA_OPSWKF~5`. Your worktree is `C:/tmp/opswkf-r1-5`, on branch `wk-NFRA_OPSWKF-5`, cut from box/dell2 at the
issuance commit. Its `portal/` is a nested worktree based on portal `origin/DEV` @2d42e9b7, with `node_modules` linked. Write the
portal files inside `C:/tmp/opswkf-r1-5/portal/` and commit them IN THAT NESTED REPO on its own branch with plain `git -C
C:/tmp/opswkf-r1-5/portal commit` (the portal has no safe-commit). Use author `0.9.0_WK_NFRA_OPSWKF~5
<0.9.0_WK_NFRA_OPSWKF~5@opal.agent>` and write the message with the Write tool, passed with `-F`. Do not push. Commit your
proof-of-spec instance in the outer worktree with `bash .tools/safe-commit.sh --author "..." -F <msgfile> -- <paths>`.

### THE CELL

`OW-p-1`. A new component, `portal/src/pages/TicketCenter/TradeRequestParts.tsx`, that lets a signed-in user file a trade request
as a Ticket Center ticket. **READ first:**
- `TicketCenter.tsx` (how the create form branches on type, around `:219-229`);
- `AnalysisRequestParts.tsx` and `analysisRequest.ts` (the existing typed-ticket pattern);
- `portal/src/api/endpoints/tickets.ts` (ticket create with `answers`);
- `portal/src/api/endpoints/trade-submission.ts` (`submitTrade` and the securities types, `:239-241`);
- the TradeSubmission page under `portal/src/pages/` (its securities entry).

**AMENDMENT 1 (issuer, ~06:0xZ, row NFRA_OPSWKF-D2-W1-S1):** the ticket type now also requires `answers.firm` (a firm id,
server-checked against the filer's allowed firms). The form carries a firm field defaulting to the signed-in user's firm (read it the
way `AnalysisRequestParts.tsx` fills its `firm` answer), and call 1's `answers` includes `firm`. The engine body is unchanged.

**Fields:** firm; fund; weights as-of date; a securities grid (symbol, weight, action), reusing the TradeSubmission page's securities
types and, if it is importable as-is, its entry component, READ only; trade comments; one attestation checkbox.

**One submit does two calls, in order:**
1. Ticket create, with `type: "trade_request"`, a title (`Trade request: <fund>`) and
   `answers: {firm, fund, weights_as_of, trade_comments, attestations_confirmed: true}`.
2. `POST /api/general/trades/submit`, with `{fund, weights_as_of, securities, trade_comments, attestations, ticket_id: <the new
   ticket id>}` and NO `initiator_email` or `initiator_name`, because the engine now reads the submitter from the token. If
   `submitTrade`'s TypeScript type demands those fields, declare your own body type in your file and call the same endpoint
   through the shared API client. Do NOT edit `trade-submission.ts`.

If call 2 fails, show the error and keep the created ticket visible; never re-create it. Submit stays disabled until fund,
weights date, at least one security and the attestation are filled.

Export the component. **Do NOT edit `TicketCenter.tsx`.** The issuer mounts your component there at the merge. Your report names
the props the mount must pass. Follow the portal colour law: the light `#F4F6FA` canvas and white panels with a 1px `#C4CBDB`
hairline, with navy ink only on the canvas (`portal/src/lib/designTokens.ts:8-13`).

**Test:** `portal/src/pages/TicketCenter/__tests__/trade-request.test.tsx` (new), in the style of `__tests__/analysis-request.test.tsx`,
with the two API calls mocked. Use these exact test titles:
- `submits one ticket then one engine submit carrying the ticket id`
- `sends no initiator identity in the engine body`
- `blocks submit until every required field and the attestation are filled`

### ACCEPTANCE

<criterion id="OW-p1-AC1" cell_refs="OW-p-1"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/R1_CHECKS/ow_checks.py p1-form --portal C:/tmp/opswkf-r1-5/portal</invocation><expect>OW-P1-FORM-OK</expect></criterion>
`OW-p1-AC1`: the three named tests exist and pass under `bun test`.

<expected_criteria>OW-p1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~5/`,
  and this order's file (status flip only). Every other portal file is READ only. `TicketCenter.tsx` is TCKT_VNEXT's, and its
  mount is the issuer's.
- Never push. Never run `bun install` (no registry egress); `node_modules` is linked. Never call a live API.
- No non-ASCII. Rows go in as `NFRA_OPSWKF-D2-W5-S<k>`, appended in BINARY mode.

<paths>
portal/src/pages/TicketCenter/TradeRequestParts.tsx
portal/src/pages/TicketCenter/__tests__/trade-request.test.tsx
org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPSWKF/decompositions/NFRA_OPSWKF_DECOMP.md</decomp_doc> (round 1), cell `OW-p-1`.
<owned_cells>OW-p-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: OW-p1-AC1. The instance is at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~5/NFRA_OPSWKF.TO-OW-p1.trade-request-form.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> OW-p1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** the check line verbatim, the portal commit hash(es), the outer commit, the mount line you need, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, hold or gate is created or consumed by this cell
comp-iam: DECLARED-NOT-APPLICABLE a portal component; no IAM surface
comp-adversary: DECLARED-NOT-APPLICABLE the identity half lives in the engine (OW-e-1); the no-initiator-in-body test is its client mirror
lane: portal DEV, two new files; the drain runs typecheck + lint and lands on DEV (a product file: CTO review route).
portal_ref: origin/DEV @2d42e9b7 (fetched 05:2xZ).
</preflight>
