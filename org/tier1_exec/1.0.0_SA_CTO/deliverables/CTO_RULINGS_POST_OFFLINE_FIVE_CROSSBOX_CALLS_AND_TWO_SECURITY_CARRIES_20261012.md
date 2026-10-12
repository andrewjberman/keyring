# CTO rulings -- the five crossbox CALLs and two security carries that queued while the laptop was dark (2026-10-11 19:13Z - 2026-10-12 01:30Z)

From 1.0.0_SA_CTO (laptop, cluster lead), 2026-10-12 ~02:0xZ. Backlog file (every bus frame, verbatim):
`org/tier0_exec/0.0.0_AB_MSTR/logs/2026-10-12/LAPTOP_OFFLINE_BACKLOG_19Z_TO_0130Z_20261012.md` @e8cf8be925. All five calls ACKED
on the crossbox files at 01:52Z. Every read below is this seat's own, 01:5xZ, read-only; names of policies, principals, secrets
and functions are written in full; no secret value, token or person's address leaves the laptop (users rows by digest only).

## 1. XB-20261011T193844Z-2cce (dell2 COO~V2, TCKT_VNEXT R5-gr-1) -- who may read `opal/ticketing/svc-commentary` -- READ DONE, dell1 reach ACCEPTED

| item | answer (measured) |
|---|---|
| 1. secret | `opal/ticketing/svc-commentary`, ARN suffix `-pXsmuU`, Created 2026-10-09T01:13:37Z, LastChanged same second, LastAccessed 2026-10-12 (date grain), RotationEnabled null |
| 2. identity policies allowing `GetSecretValue` on it | ONE: `cloudops-dell-agent-platform-secrets-policy` v4, Sid `ReadPlatformKeys`, attached to group `cloudops-dell-agents-group` (members `cloudops-dell1-agent-user`, `cloudops-dell2-agent-user`). Denominator: 9 group policies read (8 carry no statement naming it), plus 2 attached policies per user (bus, ssm; 0 statements naming it), 0 inline. The laptop's identity `user/Andrew_Berman` reads it by `AdministratorAccessOpalCapital`, not by any statement naming it |
| 3. simulates | `cloudops-dell2-agent-user` allowed; `cloudops-dell1-agent-user` allowed; `user/Andrew_Berman` allowed; `role/agentbus-alyssa01-fleet-andrew-role` implicitDeny |
| 4. resource policy | ABSENT (`get-resource-policy` returns none) |

RULING on rows D2-S8/S9 (the dell1 reach the signed pair did not name): ACCEPTED as the standing design. The two dell agent users
are least-privilege and identical by Andrew's word (one group, one platform-key statement); a per-box split of that statement
would make the dells differ for one ARN and buy nothing (dell1 holds no process that reads it). The record names it; the rotation
runbook cites the ARN above. NOT a grant change. Laptop (`to`) side of 2cce closed on this file.

## 2. XB-20261012T004641Z-4c5d (site Z CTO, NFRA_OPLGTW OG-tb-1) -- drop `gateway/teams/bearer` from ReadPlatformKeys -- YES

0 reads by the group in a 90-day census; the bearer reads Andrew's Teams chats; both halves signed (COO @f9cb4c5dca, CTO
@fa2892a777). YES: site Z's applier edits the census source `infra/aws/terraform/nfra-ctlpln-identity/iam.tf` (laptop fabric
file; the applier's lane carries infra) under its pair, 31 -> 30 ARNs, plan showing that one statement and nothing else moved,
`safe-apply`, ledger, re-plan No changes; receipt to `2.0.0_SA_COO~C` (NFRA_CTLPLN's issuer, seated 19:09Z) and to this seat. The
same statement is the one section 1 names; after the apply the dells still read `svc-commentary`. Laptop side closed on this file.

## 3. XB-20261011T194408Z-e588 (dell2 CTO, NFRA_OPSWKF TO-OW-s1 worker read) -- four functions behind the portal authorizer examine no caller -- RULED

Record `.../0.9.0_WK_NFRA_OPSWKF~7/FOUR_FUNCTIONS_WHAT_A_NON_INTERNAL_CALLER_CAN_DO.md` @723a94955a (code read, nothing called).
Severity and owner per function, in the XB-74e2 pattern (one helper reads the authorizer context; 403 unless `tier == internal`):

| function | what a verified non-internal caller can do today | severity | owner of the one-cell fix |
|---|---|---|---|
| `trade-submission-handler` (`POST /api/general/trades/submit`) | create a PENDING_APPROVAL trade submission for any fund and have SES mail the approvers; cannot approve/execute | MEDIUM (abuse of Opal's trade queue + mail) | NFRA_OPSWKF (dell2) -- the XB-74e2 FWD widens to "every trade-* handler" |
| `opal-research-pull-enqueue` (`POST /api/private/research/pull`) | overwrite `packs/<ticker>/status.json` and enqueue a pull the box consumer turns into a Bloomberg draw | MEDIUM (vendor budget + harvest-state abuse) | AMGT_HARVST (dell1, COO~W1): the handler reads `tier`, else 403 |
| `opal-portal-data-proxy` (11 routes: market, AUM, positioning/model holdings, valuation, macro, news, sentiment) | read every dataset the proxy serves | MEDIUM (Opal research + model holdings to partner logins; no client data named) | NFRA_CTLPLN FWD-28 (laptop, COO~C) -- the proxy predates the tree |
| `opal-portal-content-api` (GET returns every stored content override; PUT/DELETE already fenced on `firmId == opal-capital`) | read content overrides | LOW | NFRA_CTLPLN FWD-28, same cell (GET gains the fence PUT has) |

Not a control and not to be built: a handler check that the event "came through API Gateway" (forgeable; see section 4).
Laptop side of e588 closed on this file; the owners are told through their managers.

## 4. XB-20261011T232055Z-c404 (dell2 CTO, TCKT_VNEXT-D2-S46 ARMED) -- who holds `lambda:InvokeFunction` on the functions behind the portal authorizer -- CENSUS DONE, RULED

Census (this seat, 01:5xZ): the 7 functions the shared portal API integrates (`shared-infra/apigateway-portal/integrations.tf`:
`opal-data-refresh-api`, `opal-partners-data`, `opalinvest-auth-handler`, `trade-dashboard-api`, `trade-identifier-cache`,
`trade-submission-handler`, `trade-workflow-handler`). `cloudops-dell1-agent-user`: allowed on 7 of 7. `cloudops-dell2-agent-user`:
allowed on 7 of 7. `role/agentbus-alyssa01-fleet-andrew-role`: 0 of 7. `user/Andrew_Berman`: all, by the administrator group.
NOT in this denominator: the functions behind the ticket, IRPT, harvest and data-proxy APIs (separate roots, same authorizer id
`naqxlm`); dell2's own simulate already reads `opal-ticket-api` allowed for its user.

RULING: the row is correct -- a direct invoke goes around the authorizer and a handler believes the event it is handed. The
control is the IAM grant, not the handler: NFRA_IAMROLES202609 (site Z, the least-privilege project) narrows the dell agents'
`lambda:InvokeFunction` to the functions a dell cell deploys or tests by name, and removes the portal-fronted set from the
standing grant (a cell that must invoke one re-adds it for its window under a pair). Disarm of D2-S46 stays with
`1.0.0_SA_CTO~DELL2` on that apply's receipt. The laptop admin identity is the standing finding already listed to Andrew
(XB-282e addendum). Laptop side of c404 closed on this file.

## 5. XB-20261011T211128Z-f139 (dell2 CTO, DSGN_IRPTV1-D2-W62-S3) -- are the Holdings tab's navy panel strips a C3 band? -- RULED: no restyle in DSGN_IRPTV1

`portal/DESIGN.md` C3 (Option A, Andrew-direct 2026-09-11): ONE deliberate full-bleed band per page; navy is never a container
fill. `portal/CLAUDE.md:40-44` records the applied divergence: `PanelHeader`, `DarkCard`, `NestedCard` and `Panel
variant="chart"/"mixed"` resolve to the band because 4,887 light-on-dark idioms in `src/pages/` depend on it (row
DSGN_REBRND-W2-S5). RULING: a `PanelHeader`/`PanelFooter` strip is NOT a C3 band and NOT a licence; it is the recorded divergence,
owned by the DSGN_REBRND successor (DSGN_REBRND is CLOSED, placement LAPTOP; the follow-on migration is a laptop-fabric project to
be briefed, not a DSGN_IRPTV1 cell). The Total Assets hero is the Holdings page's one band. DSGN_IRPTV1 restyles nothing for
this row; the row closes OBSERVATION/INERT citing this file. Laptop side of f139 closed on this file.

## 6. dell2 msg 6045 (carried 23:07Z) -- a public sign-in route in front of the portal's users table since January -- IDENTIFIED; the delete is Andrew's

Identified from the laptop: HTTP API `trade-submission-api` (`w8jnzvs21g`, created 2026-01-06T20:32Z, endpoint
`https://w8jnzvs21g.execute-api.us-east-1.amazonaws.com`): `POST /auth` with NO authorizer -> `trade-auth-handler` (email +
password checked against the portal's users table, no rate limit, no lockout, no origin check), and six CUSTOM-authorized routes
(authorizer `nfa51m`) to `trade-dashboard-api`, `trade-submission-handler`, `trade-workflow-handler`. The same three functions are
served to the portal through the shared portal API, so the legacy API adds a second, password-based door to them. 30-day
invocations: `trade-workflow-handler` 1, `trade-submission-handler` 7, `trade-dashboard-api` 687 (the portal path; the legacy API's
own share is not separable here). Reading: an unused door that accepts password guesses against every portal user.
Act for Andrew (listed once, section 8): delete HTTP API `w8jnzvs21g` (and `trade-auth-handler` with it, after one CloudTrail read
that nothing but the API invokes it). Reversible only by re-creating; no served page uses it (the portal calls `/api/general/...`
on the shared API).

## 7. dell2 msg 6260 (carried 01:34Z) -- one ACTIVE users row on an outside domain with the internal firm id and no firm list -- ANSWERED

Digest `1af514167abb` (dell2's own digest of the address) resolves on the users table to a PROFILE row on domain
`thewhitelabelcreative.com`: `firmId opal-capital`, `tier advisor` (not internal), `role user`, `allowedFirmIds` ABSENT,
`createdAt 2026-06-16T20:24:25Z`, `createdBy 0.5.0_AE_OpalETL (Andrew-direct 2026-06-16)`; a sibling row on
`whitelabelcreative.com`, same creation line. Denominator: 23 PROFILE rows with `firmId opal-capital` of 86 scanned; the only
outside domains among them are these two (plus one `opal.invalid` service row). Answer to dell2's one question: created by the
ETL seat on Andrew's word of 2026-06-16 (a design contractor's logins, by the domain). Whether an `opal-capital` firm id with no
firm list is still intended for them is Andrew's (section 8); nothing changed, no address written.

## 8. Listed to Andrew once (acts and one question)

1. Delete HTTP API `trade-submission-api` (`w8jnzvs21g`) and its `trade-auth-handler` -- the unused password door (section 6).
2. The two White Label Creative rows (digests `1af514167abb`, `04fc361f3802`): keep `opal-capital` standing, or move them to a
   firm list / disable (section 7).
3. Public key(s) for the SSH rollout (`ANDREW_DIRECT_20261012_015xZ_SSH_OVER_TAILNET_EXECUTE_COO_C.md`).
