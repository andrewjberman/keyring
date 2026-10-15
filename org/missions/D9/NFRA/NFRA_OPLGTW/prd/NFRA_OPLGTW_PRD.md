```json
{
  "project": "NFRA_OPLGTW",
  "directive": "D9",
  "fabric": "site-z",
  "prd_version": "v3.8",
  "step": 4,
  "brief_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_1511ET_NFRA_OPLGTW_D9_REGISTRATION_AND_PRD.md@45ce4e5b73",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8",
    "FWD-10",
    "FWD-11",
    "FWD-12",
    "FWD-13",
    "FWD-14",
    "FWD-15",
    "FWD-16",
    "FWD-17",
    "FWD-18",
    "FWD-19",
    "FWD-20",
    "FWD-21",
    "FWD-22"
  ],
  "status": "RATIFIED"
}
```

# NFRA_OPLGTW - Opal Gateway Schwab access in Claude

## Authority and project arc

Author and accountable CTO: `1.0.0_SA_CTO~A`. Directive D9, Opal Workflows; macro NFRA; execution fabric laptop. Version v0.2, 2026-09-14. This purpose-level PRD corrects the brief-coverage omissions returned in the v0.1 L4-R review at docs/briefs/sources/NFRA_OPLGTW_L4_BRIEF_REVIEW_v0_1_20260914.md@51c7fc7f51. No counterpart project is created.

Andrew commissioned the supplied CloudOps SPEC as this project's brief and approved all eight endpoint bars at 15:24 EDT. The durable approval is `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_1524ET_NFRA_OPLGTW_ENDPOINT_APPROVED.md@4498e665cc3855184baf3d3a84d391d44af2e13a`. The endpoint's source cards are carried from `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_OPLGTW_ENDPOINT_PROPOSED_20260914.md@4498e665cc3855184baf3d3a84d391d44af2e13a`, committed with that approval before review. Their original pending-state wrapper is historical. Only the card heading layout is normalized to the canonical FWD definition syntax; DONE WHEN, ACCEPT, PROOF and SOURCE text remain verbatim. SOURCE line numbers inside the cards refer to the supplied SPEC at `39a8c5eeca03666d3ef81dbccce6859506b572af`.

The product lets Menachem use his Opal work Claude account to ask read-only Schwab questions and obtain filtered CSVs through the existing `https://mcp.opalinvest.dev/mcp` Gateway. SmartX and BlackDiamond remain separate master namespaces. An authorized operator can later revise scope or revoke access. Completion means every approved EXERCISED bar has its deliberate proof instance; producing a connector URL or deploying code alone does not complete the project.

The header stays DRAFT while independent ground-truth certification and the two canonical half reviews are pending. The author does not sign either half. Before L5, update the header to RATIFIED after the ground-truth review resolves its claims, and measure ADMITTED with `python .tools/prd-signoff.py status NFRA_OPLGTW`. The header-only promotion does not invalidate unchanged half signatures. COO owns subsequent decomposition, sequencing, task orders and worker placement.

## Scope and evidence boundary

The first release covers the five Schwab tools, hosted Claude connection, per-principal authorization, two masters and four silver datasets (v1.7), protected filtered CSVs, support and safe withdrawal. Original bronze/Parquet download, source mutation, arbitrary SQL/code/URLs, cross-master aggregation, security-reference enrichment joins, managed Enterprise Auth, private tunnels, and a new portal are outside v1. Original-file support requires a future version and whole-object grant; its allowed-operation enum is disabled in this version.

The proposed initial profile is not an active entitlement. The source brief proposes both masters, all accounts, its column lists and a 30-calendar-day window. Menachem's tenant/object IDs are null in the supplied record. An authorized identity/data administrator must verify the immutable identity and approve a concrete account/date/field grant at onboarding; until then the system has no active profile. This is a runtime input to an already specified approval mechanism, not an undecided design choice.

Repository source and supplied observations are separated in the ground-truth section. Existing public discovery responses and the original 41/41 policy-model results are not evidence of an authenticated Claude journey, deployed source parity, effective role trust, row filtering, or successful download. No production change or employee grant is made by this PRD.

## ENDPOINT (step 2, /endpoint --forward)

FWD-1  — Menachem uses Schwab data from his work Claude account

DONE WHEN: EXERCISED — a deliberate connection and reconnection walkthrough succeeds.

ACCEPT: Menachem signs in with his work account, asks a Schwab question in Claude, and can continue after signing out and back in without installing developer software.

PROOF: An observed owner-and-member walkthrough, including an expired sign-in and a fresh connection.

SOURCE: supplied brief lines 10–30, 101–125, 181–211.

FWD-2  — Schwab answers are accurate and keep the masters separate

DONE WHEN: EXERCISED — chosen questions and date comparisons are checked against independently prepared examples.

ACCEPT: Menachem gets understandable holdings and balance answers for the master and date he selected, with SmartX and BlackDiamond clearly separate and without adding overlapping balances or different days together.

PROOF: Deliberately chosen examples with independently known answers, including a comparison between masters and between dates.

SOURCE: supplied brief lines 14–18, 81–99, 127–147.

FWD-3  — Each person sees only the Schwab information granted to them

DONE WHEN: EXERCISED — allowed and forbidden requests are deliberately tried under different signed-in accounts.

ACCEPT: Menachem can see the approved accounts and information, while requests for hidden personal details, another person's access, or changes to source data are refused without revealing the protected information.

PROOF: Controlled allowed and denied examples, including misleading text inside a file and attempts to ask indirectly for hidden information.

SOURCE: supplied brief lines 32–99, 127–147, 163–179, 195–216.

FWD-4  — Menachem downloads the same approved information he can query

DONE WHEN: EXERCISED — the download journey and deliberate misuse attempts are run and the resulting file is opened.

ACCEPT: Menachem opens the download link, signs in, and receives a clearly labeled spreadsheet file containing the approved information. A copied or expired link does not give someone else access, and original source files remain unavailable in this first release.

PROOF: An opened filtered download, a copied-link attempt by another account, an expired-link attempt, and a refused original-file request.

SOURCE: supplied brief lines 20–30, 81–99, 149–161, 199–205.

FWD-5  — Answers disclose their scope, date, and limitations

DONE WHEN: EXERCISED — complete, missing, outdated, and oversized examples are deliberately requested.

ACCEPT: Menachem can tell which master and date an answer describes and whether information is missing or cut short. An incomplete result is never presented as a complete total, and unavailable information is not guessed.

PROOF: Read the actual answers for deliberately varied availability and size cases and compare their statements with the underlying examples.

SOURCE: supplied brief lines 32–45, 127–147, 201–213.

FWD-6  — Opal can change or revoke access without a new user setup

DONE WHEN: EXERCISED — an authorized operator changes and removes a controlled grant, then repeats prior requests and downloads.

ACCEPT: An authorized Opal operator can expand approved dates, accounts, or information separately, and can remove access so that later questions and old download links stop working. Menachem cannot change his own permissions, and files he already downloaded are not claimed to be recalled.

PROOF: Deliberate grant-change and revocation runs using a controlled account, with old requests and links repeated afterward.

SOURCE: supplied brief lines 71–99, 149–179, 195–209.

FWD-7  — Existing Gateway users retain their working experience

DONE WHEN: EXERCISED — existing workflows are repeated alongside deliberately busy Schwab use and a restart.

ACCEPT: Existing users can still complete their usual Gateway work while Schwab questions and downloads are running, and signing back in after a restart does not restore removed access or leave users repeatedly asking for permission they cannot receive.

PROOF: Repeat representative existing user journeys alongside controlled query and download load, expiry, and restart cases.

SOURCE: supplied brief lines 49–55, 101–125, 143–147, 185–215.

FWD-8  — Opal can support and withdraw the pilot without disturbing source data

DONE WHEN: EXERCISED — support and withdrawal walkthroughs are deliberately completed using the prepared operating instructions.

ACCEPT: An Opal operator can explain a failed connection or denied request, see who used which master without exposing private values in the support record, and turn off the new access while existing source data and collection continue unchanged.

PROOF: An operator follows the onboarding, troubleshooting, audit-read, and rollback instructions against controlled examples and records the result.

SOURCE: supplied brief lines 149–179, 181–219.

FWD-10  — Opal staff find a client by account number and name (v2.0)

DONE WHEN: EXERCISED — a named staff member looks up a client by account number, then by a name, in Claude.

ACCEPT: Andrew and Alyssa, each under their own grant, see every account's number and every name and title field Schwab records for it, so a sparse field has a fallback. Tax identifiers, mailing addresses, email addresses and phone numbers stay hidden. A principal whose grant does not carry the identity columns sees none of them.

PROOF: One lookup by number and one by name for a known account, read against the source; the same requests under a grant without the identity columns, refused; the audit record of each identity read, holding no value.

SOURCE: Andrew-direct 2026-10-08 ~17:4xZ, answer 2 (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261008_174xZ_GATEWAY_SCHWAB_FOUR_CALLS_ANSWERED.md` @116d52009d); `4.0.0_SA_CRO~Z` assessment @139c8d018e, G1.

FWD-11  — Opal staff read cost basis and realized gains (v2.0)

DONE WHEN: EXERCISED — lot-level cost basis and realized gain/loss for chosen accounts are asked and checked against source.

ACCEPT: For a granted account and date, staff can read open lots (acquired date, quantity, cost basis, unrealized gain/loss) and closed lots (closing date, proceeds, gain/loss, holding term), daily and year-to-date, with transaction flows carrying a readable label. The same scope, date and master rules as every other dataset apply.

PROOF: Independently chosen accounts and dates whose lot totals are recomputed from the silver rows and compared with the answer.

SOURCE: as FWD-10, G3 and G4; Andrew-direct 2026-10-08 ~17:0xZ, "Cost basis data absolutely exists in the aws bucket already".

FWD-12  — Thirteen months of history (v2.0)

DONE WHEN: EXERCISED — a quarter-start and a quarter-end date about a year apart are both answered for one account.

ACCEPT: A grant reaches back 13 months from the latest complete business date. A date in that span with no proven-complete source is reported as unavailable, never guessed.

PROOF: The two-date comparison, plus one deliberately requested date that lacks a completion record.

SOURCE: as FWD-10, answer 3: "13 months for now".

FWD-13  — The Tax SMA master is collected and served (v2.0)

DONE WHEN: EXERCISED — master 08403355's daily files land, convert and answer a question, after a list-only run proves Schwab returns them in the same shape as the two existing masters.

ACCEPT: Tax SMA accounts are collected every business day by the existing puller in the same structure as the other masters, kept as a separate master, and answer questions like SmartX and BlackDiamond. If Schwab returns no files for the master, the outcome reports that and stops.

PROOF: The list-only run beside a control master; then a day's files landed, converted and queried.

SOURCE: as FWD-10, answer 1: "WE should assess if this works and if so, and we get the data in the same shape (via running it exactly same structure), then it needs to be added to the daily job."

FWD-14  — Alyssa reads one Tax account's quarter end to end (v2.1, the thread)

DONE WHEN: EXERCISED — under Alyssa's own grant, one Tax account on master 08335338 answers its Q3 2026 reconciliation inputs, and each figure is read against the custodian's statement.

ACCEPT: For the account and quarter she names, she reads the value at quarter start and at quarter end, contributions, withdrawals, realized gain/loss for the quarter and the change in unrealized gain/loss. Each value names the source field it came from. A figure that does not tie to the statement says why.

PROOF: The one account's quarter, read through Claude under her principal, set beside its monthly statement and the workbook's figures.

SOURCE: Andrew-direct 2026-10-08 ~22:0xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_220xZ_ALYSSA_TAX_WORKFLOW_SINCE_INCEPTION_GL_LOTS_LAST4_KEY_SCHWAB_AND_BD.md` @618699ceeb): "We just have to be able to give her the right information"; brief `docs/briefs/oplgtw-tax-workflow-midstream-brief-20261008.md` @dae0456eb4, O1.

FWD-15  — Alyssa finds the account from the key her sheets hold (v2.1)

DONE WHEN: EXERCISED — lookups by last four digits plus a name, and by full number, each return exactly one account or an explicit ambiguity.

ACCEPT: A last-four-plus-name or full-number request resolves to one account. When it matches more than one, the answer says so and lists the candidates; it never picks one. Last four alone is never a key. The identity rule is the one MDPF_TAXSMA already holds (`00` + eight digits), reused, not re-derived.

PROOF: A unique key, a key that collides in 08335338, and a key that matches only a different client's account, each answered correctly.

SOURCE: as FWD-14: "making sure that we at least have the last 4 digits of the account in there for keying's sake"; brief O2 and G-2.

FWD-16  — Since-inception record as of the date she picks (v2.1)

DONE WHEN: EXERCISED — for two Tax accounts, the value at inception, every flow since and the value on a chosen date are read and checked against source.

ACCEPT: The inception date is the Tax SMA roster's, never the custodian's account-open date. Flows include contributions, withdrawals, securities transferred in or out at market value, and advisory fees, each labelled; an unlisted code stays `unclassified`. The gateway serves the inputs and computes no return.

PROOF: Two accounts whose roster inception falls inside the served window, recomputed from silver rows and compared with the answer.

SOURCE: as FWD-14: "being able to get that since inception value for every given tax account"; brief O3, G-3, G-9.

FWD-17  — Tax lots and gains as her report prints them (v2.1)

DONE WHEN: EXERCISED — for one quarter end, realized gain/loss in four buckets and the lots held on that date are read and tied to Schwab's totals.

ACCEPT: Realized gain/loss splits short-term and long-term, gains and losses, for the quarter and since inception, at lot grain. Lots are those held ON the quarter-end date, never today's lots repriced, including short positions, with unrealized gain/loss split the same four ways. A lot with no reported cost basis says so and is never read as zero. The top-10 holdings by weight as of quarter end are served from the positions data.

PROOF: One account-quarter's buckets tied to Schwab's totals line; one missing-basis lot shown as missing.

SOURCE: as FWD-14: "realized gains losses, unrealized gains losses, and any kind of tax slots or cost basis"; brief O4, O5, O9, G-7, G-8, G-10.

FWD-18  — The same answers for a Black Diamond Tax account (v2.1)

DONE WHEN: EXERCISED — one Tax account held through Black Diamond answers FWD-14 to FWD-17 in the same field shape as a Schwab account.

ACCEPT: Alyssa asks without naming the source; the answer names it. Her grant reaches any Black Diamond account (v2.2: Andrew-direct 2026-10-09 ~01:5xZ, "any account"); a Black Diamond answer is never joined with another firm's data in one response.

PROOF: One Black Diamond Tax account's quarter beside one Schwab Tax account's, same fields.

SOURCE: as FWD-14: "Alyssa is going to need to go to both of those places"; brief O6, G-1.

FWD-19  — The Tax SMA master's accounts reach back to their inception (v2.1)

DONE WHEN: EXERCISED — a 08403355 account answers FWD-14 for a date before collection began.

ACCEPT: The 08403355 history is backfilled to the earliest roster inception among its accounts, in the same structure as the other masters. If Schwab serves no files before a date, the outcome reports that date and stops there.

PROOF: The backfill's enumerate record, then one pre-collection date answered.

SOURCE: as FWD-14: "we will have to do a backfill uh, on whatever the contents are of this new Schwab master"; brief O7, IV.C, G-5.

FWD-20  — Each served family's poll cadence and backfill depth are one read (v2.6)

DONE WHEN: EXERCISED — one read lists every vendor family the deployed gateway serves. For each family it gives the
sweep's schedule, its last sweep, and its history depth (earliest served date), each with the date read. NFRA_MCPORTAL
can display the read.

ACCEPT: The family list comes from the deployed definitions, never a hand-kept list. The schedule is read live from
the AWS schedule, never typed. The depth comes from `backfill-status` and from the served data's earliest date. Every
value carries a claim (measured / inferred / absent). The read is read-only: no alert, alarm or monitor rides on it
(standing moratorium).

PROOF: One family's cadence against its live schedule. One family's depth against `backfill-status` and the served
data's earliest date.

SOURCE: Andrew's site Z voice memo 2026-10-13, "the depth and breadth of the polls available ... what backfill or scope
out those tools work", via direction XB-20261013T185926Z-4d72 Z3.

FWD-21  — An Opal asset manager reads the harvest bucket from their own Claude through the gateway (v2.6)

DONE WHEN: EXERCISED — a real Opal asset-manager principal's driven call returns one covered name's research pack and
chatter from `opal-data-harvest`. A non-Opal principal is refused on every prefix.

ACCEPT: Andrew-direct 2026-10-13 ~20:0xZ (call 8): ALL 24 prefixes of the servable list v4 @7e0da2dfee SERVE to Opal
principals, raw included. Non-Opal principals are refused on every prefix. V1 admits by IDENTITY, through OG-tg-1's
Opal-user predicate (the opalinvest domain, no #ext# guest); a non-Opal principal or an off-list prefix is refused
before any S3 call, and the grant writer writes nothing for V1. A per-person harvest grant comes with NFRA_MCPORTAL's
control outcome (direction Z2), through the one existing grant writer. Asset-manager principals are named from the
grant store, never guessed. An asset manager with no work Claude account is Andrew's act. NFRA_MCPINDEX catalogs the
prefixes.

PROOF: The driven call. A non-Opal principal refused on `packs/` and on `wsj/harvest/`. The same asset-manager
principal refused on one Schwab and one Black Diamond tool unless Andrew has admitted it to v2.2's connected set
(research data only by default, AMGT brief boundary). A census of the asset-manager principals, read from the
identity store that admission actually reads (the grant store holds no harvest record), denominator printed.

SOURCE: Andrew's AMGT voice memo 2026-10-13, "figure out the, open gateway mechanics for how to connect the ... open
dash data dash harvest folders ... so that the asset managers can use that with their cloud"; widened by his call 8.

FWD-22  — An Opal employee reaches every contracted bucket table through a typed gateway tool (v3.0)

DONE WHEN: EXERCISED — for each census group that lands (G1 harvest, G2 assets silver, G3 portal-v2, G4 mdpf gold delta,
G5 ETFs, G6 news), one real Opal principal's driven call to one of that group's typed tools returns rows carrying
`as_of`, `source_keys[]`, a denominator and `absent_reason`. REALIZED only at 6 of 6 groups; a group whose measured
delta is empty (G4 may be) lands with zero tools and counts. A client-data tool takes `firm`, `account_last4` and
`platform`, and a call that names no firm, or two firms, is refused before any read.

ACCEPT: The tools are the ones the census contracts propose (`4.0.0_SA_CRO~Z` deliverables
`GATEWAY_DATA_CONTRACTS_20261014/G<n>_*.md`), each marked keep / extend / retire against the deployed `tool_index`.
Admission is unchanged: the Opal-users-only gate (v2.3 item 4), C2, tier admission and C-PERSON run first. Every new
S3, Lambda or DynamoDB read by a gateway role is a widening with its never-widen sign-off (CLAUDE.md NEVER-1). No
resource name is typed (rule 30). Answers project to 50 KB by default (G1 section 3). A last-4 that is ambiguous within a firm returns
the candidates, never a guess. Freshness is stated in trading days.

PROOF: Per landed group, one driven call. Negative arms: a non-Opal principal refused; for a client-data group, a
no-firm call and a two-firm call refused; an ambiguous last-4 returns candidates.

SOURCE: Andrew-direct 2026-10-14 ~12:4xZ, verbatim in `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_124xZ_GATEWAY_DATA_CONTRACTS_CENSUS_CRO_FANOUT.md` ("we need these tables to be accessible with fluid
tooling"; "forking by firm and by last 4 digits account absolutely needs to be included in any kind of client data
bucket").

## CONTRACTS

The enumeration authority is `org/standards/NFRA_OPLGTW_CONTRACT.json`, version 1.0; its four typed names (the two reader roles, the Gateway's assume policy and the access-state table) move to builder output as version 1.1 in the rename applies below, with the Terraform declarations and the application's references moved in the same orders, before any further consumer binds. Version 1.1 also adds `tool_operations`, a total map from each of the five tools to a member of `operations` or `null`, where `null` means carried by every active grant, never grantable and reading no data object; `operations` stays the grantable set, and both code copies of the mapping are tested equal to it. All tools, fields, states, error codes, limits and surface IDs are closed there as data. Its `activation=DESIGN_ONLY_NOT_A_GRANT` is intentional: implementations consume its contract, never treat the proposed profile as an authorization record. Unknown enum values and extra request properties fail closed. No counterpart PRD exists; all interfaces below have one owner in this project.

### C1 - identity, OAuth and migration

Use the existing Gateway authorization-server issuer and resource. Entra is the upstream identity provider, not an alternative MCP audience. Carry validated `tid` and `oid` in signed principal context; email is display/audit metadata only. Validate token signature, issuer, audience, expiry, authorized tenant, nonce/state, client, PKCE S256, redirect and requested resource at every applicable exchange. Never accept caller-supplied email, identity headers, role or tenant as the authorization identity. Authentication must not require Graph mail/file consent; retain delegated Graph acquisition only for tools that use it.

Register and exactly match `https://claude.ai/api/mcp/auth_callback`. Preserve existing Code loopback redirects only for registered clients, with RFC loopback port handling and no arbitrary hosted redirects. Require the issued client ID in authorization-code redemption; remove the current unregistered-loopback/optional-client behavior through an explicit reconnect migration. DCR is JSON; token exchange is form encoded. Metadata must advertise the same resource, issuer, endpoints, scope and S256 behavior actually enforced. Discovery, registration and ordinary token/auth responses have a 10-second budget; refresh has 30 seconds. Browser interaction time is excluded from server processing latency. Preserve Streamable HTTP negotiation, Bearer challenge, cancellation and relevant proxy headers. These protocol details are verified against [Claude authentication requirements](https://claude.com/docs/connectors/building/authentication).

Store client registration, authorization codes and refresh families durably in the Gateway's access-state DynamoDB table, named by the builder (`name("gateway", None, "access-state", "table")`, today `gateway-access-state-table`; never typed here). The table applied under the earlier typed name is renamed to the builder's name in its own order in the same root, before any further consumer binds: the new table is created, every record is copied with the item count equal on both sides and the operator-audit namespace verified item by item, the application's table reference and the Terraform declaration move together, and the old table is retained until the copy is proven and then removed in the same order's rollback window. Codes are single use; refresh tokens are cryptographically random, stored only as hashes, bound to immutable principal/client/resource/scope and family. A conditional DynamoDB transaction consumes the current generation and installs the next. Reuse revokes the family; a concurrent loser receives invalid_grant and cannot mint a second valid successor. No grace period that leaves a replay usable. Logout/revocation invalidates the family. Use 15-minute access tokens, 30-day absolute and 7-day idle refresh expiry; check logical expiry even if TTL deletion is late. Record expiry explicitly and scope reductions on refresh; never remint a broader configured scope. Public-client refresh rotation and replay detection follow [OAuth security best practice](https://www.rfc-editor.org/rfc/rfc9700.html).

Legacy refresh tokens cannot be safely upgraded without a new authenticated connection. Cutover rejects them with invalid_grant, preserves registered Code client callbacks, and tells existing users to reconnect once. Inventory active client registrations and test the migration before cutover. Persist client records so restarting a worker does not forget clients. A client registration expires after a 30-day idle lifetime, counted from the later of its write to the durable table (a client migrated at cutover counts from that migration write, never from a legacy registration time) and the last exchange that used it, unless it holds a live refresh family, which keeps it until that family ends. Its record carries an explicit logical expiry, which every exchange checks even if the table's TTL deletion is late; an expired client is refused with invalid_client and must register again. (L10 addendum R-5, 2026-09-28, on row W3-S5.) Failure of durable state fails new/refresh exchanges closed; it must not silently select an old stateless branch.

At cutover, every protected MCP and REST route rejects legacy access JWTs lacking the new token-version and immutable principal claims, even while their old exp is still valid. Persist the pending upstream authorization state with a short logical expiry, state/nonce and client/resource bindings; a restart between authorize and callback either resumes that exact bound transaction or returns an explicit restart-login error, never guesses identity. Access tokens carry a family identifier; every protected request checks family status and principal revocation with the current grant. Family logout/reuse revocation therefore prevents later use of previously issued access tokens as well as refresh. A2/A17 include legacy access replay, restart mid-login and revoked-family access replay.

A missing or invalid MCP credential gets 401 with the advertised resource challenge. A valid token lacking an OAuth scope gets the specified 403 insufficient_scope response, not the current conversion back to 401. A denied data entitlement is a terminal tool authorization error, not an OAuth escalation or a login loop. The download browser uses a separate Gateway-owned OIDC callback, secure HttpOnly SameSite cookies, anti-CSRF state/nonce and exact issuer/audience/signature validation. It establishes the same tid/oid principal independently. Do not infer that match from the existing ALB email-only helper. Browser OIDC endpoints bypass ALB login only at those explicit paths; existing default browser authentication and unrelated routes remain intact.

### C2 - policy and complete access enforcement

DynamoDB stores durable `principal_profile` and versioned `data_entitlement` records. Key grants by tid/oid, not email. The one email-keyed record is denial-only: a principal made restricted also gets an `email_deny` record (key `POLICY#EMAILDENY#<sha256hex("og-email-deny/v1|" + email.strip().lower())>`, one per email alias; routes and the operator writer MUST compute the same function) in the same operator transaction. The browser routes that identify a caller only by the ALB email (`/login`, the `/sprint` paths, the legacy `/callback` and its consent redemption) refuse a denied email before any read or credential exchange; an unreadable store denies them. The record only ever adds denial, is kept on revoke, and is never used to grant. Status is pending, active or revoked; use optimistic revision checks for operator updates. A revoked restricted profile is a tombstone, never deletion that reactivates the legacy unlisted-user path. Unknown users see no Schwab tools and direct Schwab calls fail. A newly added tool is denied until classified. Preserve existing users' current tool access through explicit regression, without granting new data tools by default.

Every request strongly reads the current profile/grant; an unavailable or malformed store denies restricted access. Scope includes master, dataset, account IDs, dates, columns and operations separately. Apply it before filtering, projection, grouping, totals, cache lookup and export. Accounts are raw IDs internally only. Expose a versioned, keyed HMAC account_ref over master plus account ID; keep its key in the existing approved secret mechanism, and never log raw IDs. The same numeric account ID in two masters yields different aliases. An alias is usable only after resolution against the current authorized account set.

Enforce discovery and dispatch in the integration registry and native tool path. Inventory all 27 source-declared server routes and every non-MCP entry point, including /teams/poll and /query/v0. The new restricted profile is denied unrelated data tools and direct REST shortcuts before any credential fetch or read. Domain-suffix internality cannot bypass this policy. This is necessary to make a work-email identity a limited reader. Existing admin/Graph/portal routes retain their existing policy for other users, subject to regression coverage.

Entitlement updates are operator-only, through an audited repository/release-operated administration command using an authorized operator AWS identity. Validate a candidate, show the exact scope diff, then conditionally activate it against the old revision. Store approver, timestamp and source authorization reference. Reject empty/unknown identity, unapproved accounts/fields or malformed dates. Provide no MCP tool to mutate grants. All cache/cursor/ticket keys bind principal, revision, master, dataset, dates, projection and source versions. Before response emission or download start, re-read the revision; discard stale work. Already delivered bytes cannot be recalled.

### C3 - sources, closure and date semantics

Source bucket is `opal-data-assets`; masters are 08242234 SmartX and 08335338 BlackDiamond. Only their `silver/dim_position/`, `silver/dim_balance/`, `silver/dim_asset/` and `silver/dim_transaction/` (v1.7) prefixes are data-readable. A date is a Schwab business-date label, not object LastModified or request time. For each master/dataset the rolling window includes the latest qualified complete business date and the previous 29 calendar days; do not silently fill missing dates from another master or dataset. The available dates and latest qualified date are returned explicitly. A fixed-date grant is an enumerated date set. Staleness is reported as days since the qualified business date and source observation time, without pretending a missing business-calendar feed defines a late arrival.

The existing producer markers at `schwab/<master>/meta/complete/date=<date>.json` do not by themselves prove closure. Their declared fact tables and current-run written tables can differ and they do not pin VersionIds. Extend the producer's completion metadata contract, keeping legacy fields for existing consumers, to include a schema version, master/date, run identity, expected source partitions, explicit non-applicable/empty dispositions, expected table set, successful/failed outputs, counts and exact versioned silver objects. Publish qualified closure only after the complete expected set is reconciled. The allowed completion object must carry sufficient sanitized closure facts itself; the metadata role cannot follow references into meta/conversions or other prefixes. A missing output, failed conversion, unexplained empty day, inconsistent grain, or ambiguous inventory is incomplete. Do not repair source data or rewrite silver values as part of this extension.

Gateway catalog construction validates the closure record and independently HEADs every named silver object. It persists an immutable catalog snapshot with the closure version, table/master/date, object VersionIds, sizes, schema fingerprint, row counts, validation result and opaque authorized file IDs. GET every data object by that VersionId. Reject null/unversioned identities or changed/unavailable versions. Revalidate source membership and byte bounds; no marker may introduce another bucket/master/dataset. Legacy markers are nonqualifying until a controlled producer replay or metadata backfill reconciles against original inputs and exact current output versions. Thus no historical date is promised accessible merely because a silver prefix exists.

Positions/balances are snapshots at one date. Grouping never removes master/date identity and never sums snapshots across dates. Both-master questions use separate tool calls/results; date comparisons use separately authorized snapshots and exact decimal deltas. Vendor balance fields overlap: permit a named field's sum across approved accounts, never construct a cash/AUA total by adding different balance fields. Quantity sums require grouping by CUSIP and long/short indicator; price is nonadditive. Duplicate/conflicting source grains produce unavailable, not silent deduplication. Dataset description records grain, field type, unit, sign and null semantics from measured source plus independent fixtures. Unsupported/unverified metrics are refused.

The asset reference dataset carries only its approved security fields. For a partial-account grant restrict its CUSIPs to holdings of the authorized accounts for that same master/date, using a qualified position snapshot solely for policy selection. This internal policy filter is not a user-facing enrichment join. Its position objects count toward the same object/byte/deadline limits; absent qualification denies the asset read. No other cross-dataset join is enabled in v1.

### C4 - typed tools, query isolation and response integrity

Five tools only: schwab_get_access returns authorized capabilities/current revision and availability; schwab_list_files accepts one master/dataset and bounded dates and returns opaque catalog IDs/date/format/size/download mode; schwab_describe_dataset returns authorized fields/types/units/grain/metric definitions; schwab_query executes one master/dataset/date; schwab_prepare_download accepts an authorized catalog ID or normalized query definition and returns an identity-bound ticket link. Shared get_access metadata is itself scoped and contains no hidden account IDs, storage keys or signed credentials.

Query shape is a typed object with master, dataset, business_date, mode, columns, filters, group_by, aggregates, order_by, page_size and optional cursor. Require exactly one rows/aggregate mode. Validate every field reference against the grant, including filters/groups/sorts. Filter values must match measured types; is_null has no value, in is a bounded list, all other operators take one value. Limit 20 filters, 100 values in any in-list, 10 group fields, 10 aggregates and 10 order fields. An aggregate declares function/field/output alias; aliases must be unique and cannot shadow fields. Count rows or a named non-null field explicitly. No expressions, SQL fragments, regex evaluation, filesystem paths, code, external URLs or executable content are accepted.

Use PyArrow for Parquet projection and a local DuckDB engine for validated, parameterized relational operations after account/column policy is applied. Disable external access, extension loading, remote files and SQL supplied by callers; use explicit types and whitelisted generated operators. Run each job in a cancellable child process outside the Gateway event loop, with 256 MiB resident-memory cap and clean temporary files. The initial hard caps are design ceilings to benchmark, not measured capacity: 1 job per principal, 2 globally, no waiting queue; 30 seconds for query or export, 12 compressed source objects/64 MiB including policy dependencies. Return BUSY or LIMIT_EXCEEDED with a safe narrowing suggestion when limits would be exceeded. A killed/timed-out job produces no partial successful total.

Response envelope includes master ID/label, business date, dataset, opaque source/version references, scope summary/revision, matched row count, returned count, truncation, completeness and available-date/staleness metadata. Exact decimals are strings with schema-declared scale/unit, never lossy floating-point totals. Internal source keys and raw IDs remain server-side; externally supplied source references are opaque handles bound to the current grant. Aggregate totals are computed over the whole authorized match set before pagination. A row page may be truncated only with explicit counts and a cursor; an incompletely scanned aggregate is an error.

Limit the entire serialized MCP result to 500 rows, 100,000 Unicode codepoints and 131,072 UTF-8 bytes, including all content blocks, structuredContent and duplicated text. Serialize and measure before emission, reducing a rows page or failing if metadata alone exceeds the cap. Cursor lifetime is 5 minutes and binds identity/revision/query/source snapshots and stable order; it is opaque and authenticated, never caller-editable offset authority. Tie-break rows deterministically using a validated unique source grain. If a dataset lacks that grain, reject paging until the input is corrected. The Gateway's smaller deadline/response limits stay within [Claude's published runtime limits](https://claude.com/docs/connectors/building).

### C5 - authenticated exports

Return only a Gateway HTTPS URL with its random opaque ticket in the URL fragment, no raw S3 presigned URL. A minimal same-origin browser script removes the fragment from history and exchanges it in an anti-CSRF, Origin-checked POST body; no ticket is put in a request path/query, redirect URL or referrer. If login is needed, retain only a hashed pending ticket bound to the secure browser session while the separate OIDC flow completes. Redact this POST body from all application diagnostics, use a restrictive script policy, and verify with a synthetic ticket that ALB and application logs contain no ticket secret. Ticket state carries hashed ticket ID, tid/oid, current grant revision, source versions, normalized query/projection, creation/expiry and single-use state. The browser page authenticates independently, shows master/date/file scope and Download CSV, and checks identity and current grant before atomically consuming the ticket at download start. A copied, expired, replayed, revised-policy or revoked ticket fails. A consumed ticket that fails midstream requires a new preparation request. Logical expiry is checked even before DynamoDB TTL deletion.

Run the same projection/filter/decimal rules as the query. Generate and validate a bounded CSV completely before starting its response; then reauthorize and stream without buffering it on the event loop. At most 250,000 rows and 50 MiB UTF-8, within the export job deadline and shared source/resource caps. Over-limit exports fail and ask for narrower scope, never silently truncate. Include master, business date and field-definition metadata on the page on that same authenticated page. V1 has one downloadable artifact per ticket, the CSV; there is no second companion download that could reuse a consumed ticket. CSV headers identify units where necessary. Escape spreadsheet formula prefixes in text cells (including leading whitespace/control characters); numeric values remain numeric strings with correct signs and precision. Use safe filenames, attachment disposition, no-store/referrer policy and secure cookies; do not put tokens or data in access logs. Delete local export files on success, failure, cancellation and startup cleanup.

### C6 - AWS boundaries, state and rollback

All silver reads use a dedicated Gateway-assumable Schwab reader role, named by the builder for its data scope (`name("gateway", None, "schwab-read", "role")`, today `gateway-schwab-read-role`; never typed here), with trust restricted to opal-gateway-role plus a dedicated ExternalId per approved principal. The person a grant belongs to lives in the trust policy's ExternalId, the application's entitlement record and the role's tags, never in the role's name; a later principal whose approved prefixes differ gets a role named by that scope (a tier or table qualifier), never by the person. Allow GetObject/GetObjectVersion on the six exact prefixes and ListBucket only for those approved prefix forms. Attach explicit denies for other data paths/actions to this reader, not to the operational Gateway role. No fallback to Gateway instance credentials, broad opal-assets-read role, role selected by model, or role chaining. Application policy enforces the narrower dates/accounts/fields because IAM's prefix scope admits more.

Use a separate Gateway-assumable catalog reader role, named by the builder (`name("gateway", None, "schwab-catalog-read", "role")`, today `gateway-schwab-catalog-read-role`), for the two exact completion prefixes, with its own exact trust/ExternalId and deny-outside policy. The Gateway role's inline assume policy is likewise builder-named (`gateway-assume-schwab-readers-policy`). The two reader roles and the assume policy applied under earlier typed names are renamed to the builder's names in the next apply of the same root, before any runtime consumer binds to an ARN, with the contract JSON, the application's role reference and the Terraform declarations moved together. Catalog metadata remains server-side. The data role does not gain metadata access. Current AES256 observations do not justify a new KMS grant; if deployment discovers another encryption mode, prove an exact-key permission and return the changed condition through the normal workflow. Existing wildcard employee-role trust uses the Tax SMA ExternalId and must not be broadened or reused.

The one new DynamoDB table uses encryption, point-in-time recovery, on-demand capacity, logical expiry and conditional transactions. Its operational role grant is limited to needed Get/Put/Update/TransactWrite operations on that exact table; operator administration has separate authorization. Never grant source writes to either new reader. Pin Terraform, dependency lock and EC2 release artifacts using the existing Gateway release manifest/process. Measure declared/deployed parity on-instance via the normal SSM inspection before code absence becomes an implementation expected-value. Validate live trust/resource policies/SCP boundaries with safe read-only probes and isolated negative fixtures; the supplied 41 policy simulations do not replace that proof.

Feature flag defaults off and new grants default pending. Before rollout, record existing Gateway release/config digests and client journeys. Enable a controlled identity first, then the approved employee profile. Rollback disables the integration and keeps the restricted-profile denial and durable token revocation shim active; do not roll back to a binary that reopens the email-only path or accepts legacy refresh tokens. An older whole Gateway binary may be restored only while edge access for restricted identities remains denied and the security invariants still hold. Source ingesters and source contents remain intact. No source delete, rewrite or bucket-policy broadening is part of rollback.

The DynamoDB partition key separates POLICY#<tid>#<oid> records (profile, grant, approval, operator audit) and denial-only POLICY#EMAILDENY#<digest> records from RUNTIME# namespaces (client, pending auth, code, refresh family, ticket, catalog). Runtime may strongly read POLICY keys but its write actions are conditioned through dynamodb:LeadingKeys to the RUNTIME prefix only; all transaction items must satisfy the restriction. The operator role alone may conditionally update POLICY records and append the matching operator audit in one transaction. Ordinary runtime and operator roles have no policy DeleteItem or table-admin permission. Profile, grant, approval and revocation tombstones have no TTL attribute; cleanup applies only to expiring RUNTIME records. A13 includes a runtime attempt to write POLICY and an operator revision race using isolated records. Exact-table permission alone is insufficient.

### C7 - NFRA_TRNSPT dependency tools and headless content routes (v1.2)

These tools and routes serve NFRA_TRNSPT's outcomes (its FWD-1 hops 1-2 and FWD-7) and are graded there. This project
builds them because it owns the gateway, and it grades only each order's own criteria. This ENDPOINT does not change.

**Interactive tools (orders O1, O4).**
- Every tool is read class: it is registered in both `destructive_ops` SAFE_TOOLS and `data_entitlement` NATIVE_TOOLS,
  runs through `_run`, and uses the caller's own delegated token.
- No new Graph scope. `Mail.Read`, `OnlineMeetingTranscript.Read.All` and `OnlineMeetings.ReadWrite` are already held.
- A scoped identity and a restricted (Schwab-profile) principal keep today's deny-by-default.
- **Transcript tools (O1)** are exactly `docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md`
  sections 4-5: `find_online_meeting`, `list_meeting_transcripts` (it follows `@odata.nextLink`) and
  `read_meeting_transcript` (`text/vtt` through an optional `accept` argument on `graph.call`, never a second client).
  - `innerError.code` is surfaced, with `GraphAccessToTranscriptsDisabled` and `SpeakerAttributionNotAllowed`
    distinct.
  - There is no fallback to an unattributed transcript.
  - Transcript text is untrusted content. The audit record carries meeting and transcript ids, never text.
- **Mail tools (O4):** `read_email`'s `$select` gains `ccRecipients`, `bccRecipients`, `internetMessageId`,
  `conversationId`, `hasAttachments` and `sentDateTime` (v1.5: the six fields shipped since OG-rl-1, read at
  `3a7d6a7dc8` `app/tools.py`; `bccRecipients` is populated only on the sender's own copy). A filtered, paged list filters on sender, received window and has-attachment; its page token is
  opaque, and a Graph URL is never returned or accepted.
- **Attachments on MCP:** the attachment tool on MCP stays INSPECT-only. It returns metadata, sha256, magic bytes,
  and for a PDF the page count and at most 1500 characters of page-1 text. No MCP tool returns attachment bytes.

**Headless content routes (orders O2, O5).**
- **A new capability, never a widening of `/ms/*`.** The `/ms/*` route's contract is structure-only and it "can NEVER
  echo file content, a body/preview, or any comms field" (`app/ms_ingest.py`). That stays true for the generic `/ms/*`
  routes. The one exception is `GET /ms/taxsma-workbook` (v1.5; Andrew-direct 2026-10-01 ~17:2xZ-17:4xZ, released
  OG-tr-1 `3a7d6a7dc8`). It is a separately guarded route, with its own bearer and its own guard, registered ahead of the
  generic `/ms/*` guard and edge-exposed by its own exact-path ALB rule. It is not a widening of `/ms/*`, and its spec
  is MDPF_TAXSMA's. Transcripts, mail
  bodies and attachment bytes are served ONLY on two new prefixes, one for transcripts and one for mail: the fixed
  literals `/hx/transcripts` and `/hx/mail` (v1.3). A third prefix, `/hx/teams` (v1.6), serves the laptop's LDO-001
  Teams assistant. A route path is not a `lib/opal_naming.py` kind (`name()` refuses `route`; NAMING_SCHEMA marks
  API_ROUTE NOT GRADED), so the three are graded only for distinctness: none is under `/ms/`, none is a prefix of
  another, and none collides with a route already mounted in `app/server.py`.
- **Bearers.** Each prefix has its own static capability bearer:
  - stored in Secrets Manager under a `lib/opal_naming.py` SECRET-grammar name;
  - compared in constant time;
  - accepted ONLY on its own prefix, so one leaked bearer reaches one prefix.
- **Access.** The routes read with the server-held delegated token of ONE fixed identity, Andrew's (his route ruling:
  "the daily pull runs through the EXISTING Opal gateway under Andrew's account; no new app registration, no IT").
  - Graph calls are GET only on `/hx/transcripts` and `/hx/mail`.
  - The Graph paths each route may reach are a server-side allowlist that fails closed.
  - Those two prefixes have no write, send or reply verb. `/hx/teams` is the ONE write exception (v1.6, Andrew-direct
    2026-10-02): its two POST verbs send a chat message and a channel reply AS ANDREW. Send approval lives in its only
    caller (LDO-001's reply-of-1), never in the route.
- **Allow-by-key output.** Each response is built from an explicit output allowlist, so a new Graph field cannot leak:
  - **Transcripts:** meeting id, transcript id, `createdDateTime`, `endDateTime`, the `text/vtt` body, its byte count
    and its sha256. ONLY meetings on a configured meeting allowlist are reachable. That list starts with the four
    meetings of the spec's section 6.4.
  - **Mail:** the message fields of O4's `$select` plus the body. ONLY messages whose sender is on NFRA_TRNSPT's
    sender table are reachable: Manav's addresses, and Yang's once her addresses are supplied (the table is a data
    asset). A message from any other sender is refused, including a message in the same thread as a table
    sender's: NFRA_TRNSPT ingests by sender, so no need reaches past the table. Attachment bytes (`$value`) are returned ONLY for a non-inline
    `application/pdf` within a configured size cap, with their sha256. Every other attachment returns metadata only.
  - **Mail listing (v1.4):** `GET /hx/mail/messages` lists ONE table sender's messages in a bounded received window,
    so an unattended pull can learn ids. Each row carries ONLY `message_id`, `receivedDateTime`, `sentDateTime`,
    `internetMessageId` and `hasAttachments`. Every row's own sender is re-checked against the table before it is
    listed. The page token is the gateway's opaque value and never a Graph URL. Window and page caps are set by the
    gateway (v1.4 addendum).
- **Audit.** It records the route, ids, byte counts and the caller's bearer label. It never records content.
- **No alert.** A refusal or `NeedsLogin` is returned to the caller, which records it in its own run record
  (CLAUDE.md moratorium).

**Stored sign-in lifetime (order O3).** O3 is a measurement, not a change. It measures how long the server-held token
refreshes unattended before `NeedsLogin` (`app/token_broker.py:171-183`), with its instrument and timestamps. A
lifetime under one day comes back to this seat before any `token_broker` change.

**Preconditions and dependencies.**
- The Teams transcript settings (`EnableGraphTranscriptAccess`, `EnableAttributedTranscripts`) are gate G-TEAMS-TX,
  held by Andrew via IT.
- The inspect tool's PDF facts need `pypdf` pinned in the gateway `requirements.txt`. Without it the tool returns
  `parse_error`, never an empty success.

## SURFACE MANIFEST

One row per engine, with explicit physical dependencies and no worker assignment. Stable IDs are S1 through S10; these are specification surfaces, not the six evidence axes. All run-cell references are documentary evidence, not an assertion that a new engine is deployed.

| ID | Engine and physical referent | Input -> output / proof boundary | Depends on | Endpoint / run evidence |
| --- | --- | --- | --- | --- |
| S1 | Gateway OAuth/principal and browser OIDC engine; infra/aws/ec2/opal-gateway/app/{server,oauth_as,token_broker,context,identity}.py | Verified work identity and registered client -> bound access/refresh/session principal; migration and replay proof | S3, S9 | FWD-1/3/7; S1-auth.* |
| S2 | Persistent policy guard and administration; app/identity_scope.py, app/tools.py, app/integrations/base.py, new data-entitlement module | Current profile/grant -> scoped discovery and every MCP/REST invocation; audited operator revision | S1, S3 | FWD-3/6/7; S2-authorization.* |
| S3 | Durable Gateway state; new opal-gateway-access-state DynamoDB table and adapter | Conditional profile/token/ticket/catalog state transitions -> restart-safe authoritative reads | S9 | FWD-1/3/4/6/7; S1-auth.*, S5-download.*, S6-operations.* |
| S4 | Schwab producer completion contract; existing conversion_manifest producer and entry paths | Expected source/day/table closure -> versioned qualified completion record preserving legacy fields | Existing Schwab producer | FWD-2/5/8; S3-data.* |
| S5 | Authorized Schwab catalog; new app/integrations/schwab catalog module | Qualified markers plus exact silver HEADs -> immutable scoped opaque file/snapshot IDs | S2, S3, S4, S9 | FWD-2/3/5; S3-data.* |
| S6 | Bounded Schwab tool/query engine; new app/integrations/schwab and registry/dispatcher wiring | Validated single-master/date request -> full-match counts and measured-size result | S2, S5 | FWD-2/3/5/7; S4-query.* |
| S7 | Filtered CSV/browser delivery engine; new Gateway download routes and isolated export process | Authorized query + authenticated ticket -> complete bounded CSV and metadata | S1, S2, S3, S5, S6 | FWD-4/6/7; S5-download.* |
| S8 | Audit and operator runbook engine; existing opal-mcp-audit plus new classifications/status summaries | Sanitized decision/outcome and correlation -> operator-readable support/revocation evidence | S1-S7 | FWD-6/8; S6-operations.* |
| S9 | AWS permissions, front door and release configuration; existing Gateway ALB/role/release plus two reader roles/table grants | Exact desired policies/routes/artifacts -> measured effective deployment, A16 IPv4/DNS/WAF/Host/Origin/egress checks, A19 60-second ALB idle handling, preserved source-bucket settings and old journeys | Existing infrastructure | FWD-1/3/7/8; S6-operations.*, compiler probes |
| S10 | Acceptance and onboarding harness/runbooks; synthetic fixtures, MCP Inspector and owner/member walkthrough | A1-A20 independent expected examples -> deliberate endpoint proof and safe pilot report | S1-S9 | FWD-1 through FWD-8; all six evidence axes |

S4 changes completion metadata rather than silver dataset values. The original brief's preference to reuse existing completion semantics is preserved where those semantics qualify; its fail-closed requirement requires this explicitly bounded extension where they do not. No decomposition or task order is issued here. COO may decompose only the admitted manifest and ground-truth rows; unknown deployment cells first require measurement, not a presumed absence build.

## Ground truth and compiler evidence

Authoring run: `workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/run.json@4498e665cc3855184baf3d3a84d391d44af2e13a`; component manifest beside it. Run evidence is pinned in a separate evidence commit before this PRD is committed; the exact pin is recorded in `evidence_ref.txt` beside the PRD. The six entities are S1-auth, S2-authorization, S3-data, S4-query, S5-download, S6-operations, each with source_contract, recorded_observation and unverified_boundary: expected set exactly 18 cells. No positional range larger than that is claimed.

The initial rectangle was created UNMEASURED before two disjoint source-review missions. Their patches merge through the package's ssot_validate.py. A zero-hole documentary rectangle is not production readiness or CVO certification. The run remains OPEN until the standing CVO performs the independent semantic/mutant review; no certified filename or sign-off is synthesized by this author. Pending unverified-boundary cells name the CloudOps/identity-owner probe and scope required. This prevents an unknown deployment fact from entering a task order as a measured expected-value.

Source review is pinned to `5dd24300f77e1b46cb257ba0a226a0e6c5adc2ad` with exact path/line references in the patches. Recorded package observations are pinned to `39a8c5eeca03666d3ef81dbccce6859506b572af` (metadata/readback subfiles may have earlier last-touch pins stated per cell). The key findings that drive C1-C6 are reusable refresh JWTs, incomplete client/resource binding, email-only identity, unlisted-profile fallthrough, direct REST bypasses, absent source-declared Schwab download, source completion/policy mismatch and incomplete closure semantics. They are source findings, not live exploit assertions.

The bounded original HTTP record measured /mcp 401 and two metadata 200s at 18:43:46Z on 2026-09-14. Original footer observations cover six master/dataset combinations; they are schema evidence, not every row/day/account. The original simulation file reports 41/41 custom-policy cases, including broader-allow negative overlays; it does not exercise the newly specified catalog-role policy. No authenticated Claude or download result has been measured in this authoring pass.

Bare comp-build completed with 1,992/1,992 source SHAs indexed. comp-iam service opal-gateway is desired Terraform analysis: 3 source operations unresolved-resource, so it establishes no effective grant. comp-routes trace /mcp resolves the portal CloudFront catchall, not this ALB; its Gateway blindness is explicit. comp-blast on the exact EC2 ARN reports at least 47 extracted downstream nodes from graph snapshot 2026-09-14T12:13:53.330672+00:00 (27,982 nodes/60,133 edges); dynamic edges are excluded. Raw compiler outputs and source reviewers' findings travel in the run, including EC2 manifest/release evidence. These results forbid assuming a small unrelated-user blast radius. The PRD has no schedule engine; its new work is request driven, with existing producer trigger observations in S3-data rather than a fabricated schedule census.

## BRIEF COVERAGE

The machine header cites the three-section Andrew-direct commission at @45ce4e5b73. This map carries all three sections' content: Andrew's word becomes the D9/NFRA identity and CTO ownership; Supplied brief supplies the SPEC at @39a8c5eeca03666d3ef81dbccce6859506b572af and the supplement map below; Receipt and scope supplies singular /endpoint --forward, canonical-flow, UNCHECKED receiving-check, and the registration/PRD-only commission. Header/title/preamble are identity context, not omitted requirements.

The supplied SPEC has ten level-2 headings; all ten are enumerated below, at its exact pin. There is no counterpart PRD. Paths, fields, limits and gaps are carried in the consuming contracts and data, not left for a worker to infer from a link.

| Brief heading (10/10) | Content carried into this PRD | Consuming surfaces |
| --- | --- | --- |
| Recommended experience | Work Claude account, existing Gateway URL, two independent masters, read-only questions, filtered CSV first, owner/member walkthrough | C1/C5, S1/S7/S10, FWD-1/2/4 |
| Observations and gaps | Six-prefix source metadata, existing front door and identity behavior, proposed rather than deployed grant, missing authenticated proof; preserve observed source-bucket versioning enabled, AES256 encryption, all four public-access blocks enabled and non-public bucket policy | Ground truth, C1/C3/C6, S1/S4/S5/S9; S9 release/rollback verification below |
| Architecture and authorization | Verified tenant/object identity, per-user policy before all operations, persistent restricted profile, Graph-independent dispatch, role boundary | C1/C2/C6, S1/S2/S3/S9 |
| Proposed first entitlement | menachem@opalinvest.com label, both named masters, three datasets, exact allowed field lists, 30-calendar-day window, all-account proposal pending operator approval, originals off | Contract JSON, C2/C3, S2/S5 |
| Claude application login | Exact hosted callback and preserved registered loopback clients, discovery/challenge, resource/client/scope binding, durable one-use refresh, restart/reconnect and invalid_grant | C1, S1/S3/S10 |
| Network and front-door contract | Existing public MCP endpoint and ALB, explicit auth routes and preserved browser default; actual Claude public IPv4 DNS/global-routing/no-cross-host-redirect and WAF/proxy preservation checks; where filters apply, Anthropic egress 160.79.104.0/21 as recorded in the SPEC, reverified at rollout; work-browser reachability; Host/Origin validation, clientInfo telemetry only; measured 60-second ALB idle timeout constrains query/export preparation and streaming gaps, despite Claude's longer timeout; no private tunnel | C1/C6, S9, A16/A19; operator verification below |
| Tool and query contract | Five named tools, logical IDs, pinned versions, typed fields, separate snapshot totals, exact decimals, 30 seconds/12 objects/64 MiB, 500 rows/100k chars/128 KiB, 250k rows/50 MiB exports | C3/C4/C5, S5/S6/S7 |
| Downloads and revocation | Authenticated 5-minute link, identity/revision/source binding, CSV escaping, originals disabled, no bearer S3 URL, future reads denied after revoke, already delivered bytes unrecalled; selected results enter the organization's Claude chat environment and retention settings, and commercial training defaults do not mean zero transfer | C2/C5, S2/S3/S7; S8/S10 onboarding disclosure, A20 |
| AWS permissions and validation | Exact assumed reader role, dedicated ExternalId, six-prefix allows and explicit denies, no operational-role fallback, observed AES256, 41 model cases limited, safe live-policy proof | C6, S9; added catalog-role/closure fix C3 |
| Implementation and acceptance | Existing Gateway implementation, owner form/reconnect steps, no directory requirement, optional managed auth deferred, 20 acceptance criteria including filtering before caching, actual Claude network checks, ALB idle behavior, and tool/UTC/connector-URL/correlation records, old 4-7 day estimate not committed, measured pilot capacity/cost | S1-S10, A1-A20, operations below |

Original acceptance item 11 includes later original-file success. This first version intentionally exercises original-file denial only, matching the same brief's explicit v1 original-file exclusion and Andrew's filtered-CSV choice. Whole-object success belongs to the future version, and does not silently expand this grant.

## Acceptance matrix and independent proof

Every row starts NOT EXERCISED. Expected set is A1-A20 as data in the contract. The test author must construct independent expected fixtures rather than calculate expectations with the query under test. CVO's validation compares that full set before trusting any green test exit code. Record tool, UTC time, connector URL, principal class, source/code/config version, request, expected result, actual result, and sanitized server correlation; collect an ofid_ reference if Claude supplies one. The connector URL is the public configured MCP endpoint, without credentials, ticket fragments or private query parameters; never tokens/customer data in repository evidence.

| ID | Deliberate proof required | Surface / endpoint |
| --- | --- | --- |
| A1 | Real hosted Claude work-account connect, expiry, refresh, reconnect and logout without CLI | S1/S10; FWD-1 |
| A2 | Registered Code loopback and representative existing Gateway clients, including explicit one-time migration and restart | S1/S9/S10; FWD-7 |
| A3 | Unknown/revoked/null-identity profiles and forged headers denied; tid/oid mismatch denied even with same email | S1/S2; FWD-3 |
| A4 | Discovery hides forbidden tools; direct MCP, /teams/poll and /query/v0 calls cannot bypass restricted profile | S2; FWD-3/7 |
| A5 | Same account ID in two masters gives different aliases; requests/caches/cursors/tickets cannot mix masters | S2/S5/S6/S7; FWD-2/3 |
| A6 | Account/column filtering precedes queries, aggregates, caching and export; deliberately warm caches under another or a broader grant, then verify filtered cache reads and writes under the current narrower grant and denied cache access after revocation; hidden filter/group/sort/injection fields refused | S2/S6/S7; FWD-3 |
| A7 | Independently chosen holdings/balance questions and full authorized CSV opened by a controlled employee | S6/S7/S10; FWD-2/4 |
| A8 | Decimal snapshot totals, null/sign behavior, overlapping balance fields and separate date deltas match independent fixtures | S4/S5/S6; FWD-2 |
| A9 | Missing/partial/failed/stale closures, non-versioned objects and schema/grain mismatch fail accurately; complete fixture succeeds | S4/S5; FWD-5 |
| A10 | Other-principal copied link, expired/replayed ticket and changed/revoked revision all fail; same authorized browser succeeds | S3/S7; FWD-4/6 |
| A11 | Original Parquet/bronze requests fail for every v1 profile; no successful-original pathway is exposed | S2/S7; FWD-3/4 |
| A12 | Prompt-like text in data remains data and cannot invoke another tool, widen filters or mutate policy | S2/S6; FWD-3 |
| A13 | Exact deployed IAM/trust/policy and assumed identity measured; safe negative fixtures for out-of-prefix reads/list/writes/role-chain; new catalog role tested separately | S9; FWD-3 |
| A14 | Max/concurrent Unicode queries and CSVs meet memory/deadline caps; existing workflows remain within recorded baseline; audit contains only allowed metadata | S6/S7/S8/S9; FWD-7/8 |
| A15 | Grant expansion/revocation/rollback walkthrough rejects old work and tickets; original source contents and ingester operation persist; S9 before/after readbacks preserve source versioning enabled, AES256, all four public-access blocks enabled and non-public bucket policy | S2/S8/S9; FWD-6/8 |
| A16 | MCP Inspector then actual Claude web/desktop connection verifies public IPv4 DNS with globally routable answers, no cross-host redirect, WAF/proxy preservation of Authorization/Bearer challenge/protocol/session headers and streaming transport; where filters apply verify the SPEC-recorded Anthropic 160.79.104.0/21 against current published egress and required MCP/OAuth reachability, plus work-browser login/download reachability; verify Host/Origin behavior while retaining applicable origin validation and treating clientInfo names/versions as telemetry only | S1/S9/S10; FWD-1 |
| A17 | Old refresh reuse, wrong/missing client, wrong resource, scope expansion, concurrent race and restart all uphold atomic family rules | S1/S3; FWD-1/3/7 |
| A18 | Full serialized response counts Unicode and duplicated representations; full-match totals stay correct over pages, including empty/last page | S6; FWD-2/5 |
| A19 | Auth endpoints meet 10s/refresh30s deadlines under load; query/export traffic respects the SPEC-measured 60-second ALB idle timeout with the 30-second query/export preparation deadline and no idle streaming gaps; deliberately exercise slow preparation/streaming and cancellation through the ALB, without assuming Claude's longer timeout overrides it; cancel disconnects terminate jobs and denied grants do not produce an OAuth loop | S1/S6/S7/S9; FWD-5/7 |
| A20 | Owner/member support walkthrough covers connector setting reuse, external-link confirmation, reconnect, denial/revocation and the Claude chat/retention disclosure below; record tool, UTC timestamp, public connector URL and sanitized server correlation, plus ofid_ if supplied | S8/S10; FWD-1/4/8 |

## Operator journey, audit and release

A CloudOps operator begins onboarding by reading the current deployment parity/health record, resolving the immutable principal with the identity administrator, and validating the proposed scope against an actual authorization record. Use the existing organization connector where compatible; otherwise the supplied prefilled Claude connector form names Opal Gateway and its MCP URL. The form grants no data access. An owner adds/enables the custom connector; Menachem connects his work identity, enables it in chat, asks a sample single-master/date question, opens the link (including Claude external-link confirmation), signs into the browser and clicks Download CSV. Do not silently recreate shared connector credentials or headers; plan and test any required reconnect migration. Managed Enterprise Auth is future work and is not implied by DCR or Entra login. During onboarding, the operator tells Menachem that selected results enter the organization's Claude chat environment and its retention settings. Commercial training defaults do not mean zero transfer; this disclosure accompanies the existing limitation that returned data and downloaded bytes cannot be recalled.

S9's deployment operator verifies the following from the actual Claude connection before enablement and after a relevant routing change: public IPv4 DNS with globally routable answers, no cross-host redirect, and WAF/proxy preservation of MCP/OAuth headers and streaming responses. Where filters apply, reverify the SPEC-recorded Anthropic outbound range 160.79.104.0/21 against the provider's current published egress before allowing the required MCP/OAuth paths; preserve work-browser login/download reachability. The IP range is never user identity. Verify Host/Origin behavior with Claude while retaining applicable origin validation; clientInfo names and versions are telemetry only. The SPEC's 18:43:46Z evidence records a 60-second ALB idle timeout: keep the 30-second query and export preparation deadlines and avoid idle streaming gaps. Claude's longer tool timeout does not override the load balancer. A16 and A19 record the actual connection and timeout results; these authoring clauses do not claim those tests ran.

S9's deployment operator also reads the source-bucket settings before and after enablement and rollback, preserving the SPEC-observed versioning enabled, AES256 encryption, all four public-access blocks enabled, and non-public bucket policy. The four controls are BlockPublicAcls, IgnorePublicAcls, BlockPublicPolicy and RestrictPublicBuckets. Record those readbacks in A15, including any mismatch as a failed preservation check, rather than weakening them to enable access. This is preservation of the supplied baseline, not a fresh cloud measurement.

Audit fields: timestamp/correlation, hashed principal identifier, operation/tool, master/dataset/date, grant revision, opaque snapshot/version reference, input/output counts and bytes, duration, policy decision/outcome/error code, and operator change actor/reference. Exclude raw account IDs, customer values, prompts, OAuth credentials, cookies, ticket secrets and complete URLs. Use the existing audit sink; add bounded classifications, not another general alarm service. If the durable authorization audit write cannot be acknowledged, deny a new data release and return DEPENDENCY_UNAVAILABLE; auth availability for unrelated Gateway users must not depend on a Schwab sink. Operator grant/revocation writes have their own durable audit transaction.

Implement a Schwab-specific acknowledged audit entry point: await successful PutObject of the sanitized authorization/denial record under the existing opal-mcp-audit sink's dedicated Schwab prefix and retain the response receipt/correlation before releasing data. The existing best-effort audit._emit/log_call return is not this acknowledgment. Name events release_authorized and delivery_finished separately; record planned versus actually delivered counts, and cancellation/failure, without claiming that authorization proves delivery. A14/A19 deliberately fail the sink before release, cancel after authorization, inspect sanitized errors as well as arguments, and verify that unrelated legacy authentication still works. Operator policy/audit atomicity is provided by the POLICY transaction described in C6.

Named readers and moments: the assigned CloudOps operator reads health/closure/error summaries before each onboarding or grant change, on each support incident and immediately after every rollout/rollback. The deployment operator reads the parity/negative-policy and regression reports before enablement. The identity/data administrator reads the exact scope diff at every grant revision. CVO reads A1-A20 and its expected-ID census at every project validation. COO reads the admitted PRD/run at L5 and runtime evidence at round close. A record without one of these consuming moments cannot count as support coverage. Pilot observation includes latency, CPU/RSS, export bytes, S3 calls and AWS operating cost, with an explicit sampled workload and window, not an unqualified health assertion.

The declared existing t4g.nano/one-worker deployment is not presumed to have capacity for this workload. S9 targets t4g.small (ARM64, 2 GiB) for the pilot, still on the existing Gateway service, and pins compatible PyArrow/DuckDB dependencies; this is a design target, not a deployed measurement. Benchmark the actual candidate before enablement. Admission must reserve the measured existing Gateway peak RSS plus 25 percent and 128 MiB operating headroom before starting a child, even below the global job cap; insufficient headroom returns BUSY. A14 compares a declared identical existing-user workload before/after: no failures and no more than 20 percent p95 latency regression, with workload, sample counts and measured window recorded. If the target cannot satisfy the caps, return measured evidence for a PRD revision rather than activating with weakened guarantees.

No committed delivery date is derived from the source's original 4-7 engineering days; that estimate predates durable auth migration and stronger closure work. COO re-estimates from the admitted S1-S10 decomposition. Initial limits are hard ceilings; lowering them safely is configuration, raising them or widening source/grant operations requires a measured PRD/contract revision through the normal path.

## Canonical handoff

L1 is the pinned Andrew commission carrying the supplied brief; L2 is the eight unchanged cards plus direct approval; L3 is the tree row/generated index/D9 member/macro registration; L4 is this PRD, contract data and pinned run. CVO reviews the ratified-text half plus the independently pending ground-truth certification; CRO reviews the brief half and both coverage maps. The post-commit notifier routes both half reviews and withholds COO delivery until the current half hashes are signed. No author signature or worker task order substitutes for that review. L5/L6 are the COO's subsequent acts; no live round is opened by this document.

### v1.2 addendum (2026-09-30 ~23:4xZ, 1.0.0_SA_CTO~O) -- the NFRA_TRNSPT orders

Input: laptop `1.0.0_SA_CTO` msg 103268 (relay
`org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/RELAY_20260930_1454Z_LAPTOP_CTO_103268_NFRA_TRNSPT_GATEWAY_ORDERS.md`),
`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_GATEWAY_DEPENDENCIES_FOR_SITE_Z_20260930.md`, and
`2.0.0_SA_COO~O`'s triage `deliverables/2.0.0_SA_COO~O/LAPTOP_MAIL_BRANCHES_TRIAGE_20260930.md` @6d41bd25ec. These
orders run as their own WORKSTREAM, `TRNSPT-DEPS`, under this project's issuer `2.0.0_SA_COO~O`. Its write surface is
disjoint from the Schwab cells except `app/tools.py`, `app/destructive_ops.py`, `app/data_entitlement.py` and the ac08
tool count, so it is cut after OG-t-2's release lands on those files, or rebased onto it.

| order | what | contract | notes |
|---|---|---|---|
| O1 | transcript read tools | C7 interactive | Its live REACH arm needs G-TEAMS-TX. |
| O2 | headless transcripts route | C7 headless | Meeting allowlist. Its bearer is a new Secrets Manager entry, under the ledger. |
| O3 | stored sign-in lifetime | C7 O3 | A measurement. Under one day returns here. |
| O4 | mail tools | C7 interactive | ADOPT `gw-mail-tools-int` 6a7b9e78fa, minus the LD-0613 hunk, per the triage. The ac08 count is re-read at the cut. It takes the three f-branch test files. Supersedes f1-f3. |
| O5 | headless mail route | C7 headless | The sender-table bound, with no thread reach, and PDF bytes only. This is the byte-returning `$value` download NFRA_TRNSPT needs for bronze. |

Every O2/O5 release is NARROW from the deployed commit re-read at the cut, under a change-ledger entry, with
never-widen halves: the release adds a content surface. Each route's first criterion is a negative arm run on demand:
a bearer from the other prefix refused; a meeting off the allowlist refused; a message from a sender off the table
refused, including an off-table sender in a table sender's thread; a non-PDF attachment returns metadata only.

### v1.3 addendum (2026-10-01 ~03:5xZ, 1.0.0_SA_CTO~O) -- C7 headless prefixes are fixed literals

Input: `2.0.0_SA_COO~O` msg 27476 (row NFRA_OPLGTW-Z-W16-S1, OG-hr-1 stopped at step 1). Authority: Andrew-direct
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_035xZ_NEXT_CALLS_GO_NO_TAXSMA_CRO_O_RESOURCE.md`
(OPTION 1).

- **Why v1.2 could not be met.** v1.2 said the two route names "come from the builder". The builder has no route kind:
  `name("gateway", None, "transcripts", k)` raises `ValueError` for `route`, `API_ROUTE` and `api_route` (re-run
  here at HEAD). A criterion asking for builder output that cannot exist can never pass.
- **The change (C7, one bullet).** The prefixes are the literals `/hx/transcripts` and `/hx/mail`. They are graded for
  distinctness only (not under `/ms/`, not a prefix of each other, no collision with a mounted route). `/hx` is unused
  in `app/server.py` at HEAD.
- **Unchanged.** Bearer secrets keep the SECRET grammar and are graded with `grade(<name>, "SECRET")`
  (`gateway/transcripts/bearer` reads CONFORMANT). Every other C7 clause stands: one bearer per prefix, the
  allowlists, GET only, allow-by-key output, and the negative arms in the v1.2 addendum.
- **Sign-off.** This edits CONTRACTS text, so the ratified-text half re-opens for `3.0.0_SA_CVO~O`. ENDPOINT is
  unchanged. The issuer amends OG-hr-1, OG-hr-2 and OG-rl-1 itself.

### v1.4 addendum (2026-10-01 ~13:0xZ, 1.0.0_SA_CTO~O) -- C7 headless MAIL LISTING route

Input: laptop `2.0.0_SA_COO~D` order msg 103750 (NFRA_TRNSPT FWD-7: "the ordinary daily run, no person starting
it"), ruled by laptop `1.0.0_SA_CTO` msg 103743. Relay:
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAY_20261001_1252Z_LAPTOP_COO_D_103750_HX_MAIL_LISTING_ROUTE_ORDER.md`
@6963658f49. Accepted in principle by this seat at the `/hx/mail` request contract @3a05db059a. The OG-rl-1 route serves
a message by id; without a listing an unattended pull has no ids. Today's one landed message used an id this fabric
supplied by hand.

**The route.** `GET /hx/mail/messages`, under the same prefix, bearer (`gateway/mail/bearer`, constant-time) and sender
table as v1.2, GET only, with no storage written by the gateway.

**Parameters:**
- `sender` (ONE address, on the table, case-insensitive);
- `received_from` and `received_to` (UTC ISO 8601, half-open, both required);
- `has_attachment` (`true` or omitted);
- `page_token` and `page_size`.

**Rules (each one is a test):**
- **Sender-bound, no thread reach.** The Graph query filters on the sender's address, and every returned row's OWN
  `from` is re-checked against the table before it is listed. A row that fails is dropped and counted in the audit,
  never listed. An off-table or empty-table sender is refused 403 before any Graph call.
- **Minimal rows.** Each row has exactly `message_id`, `receivedDateTime`, `sentDateTime`, `internetMessageId`,
  `hasAttachments`. Nothing else: no subject, body, recipient or attachment name.
- **Caps (this seat's values).**
  - The window is at most **31 days**; a longer or inverted window is refused 400 `invalid_window`.
  - `page_size` defaults to 25 and is capped at **50**; a value outside 1..50 is refused 400.
  - At most 200 pages are followed per request, the same bound as the transcript route.
- **The opaque page token.** It is the gateway's own value. A decoded token is honored only when it names the
  `/me/messages` path allowlisted for this route and carries the SAME sender and window as the request. Anything else
  is refused 400 `invalid_page_token`. A Graph URL is never returned or accepted (the OG-ml-1 rule).
- **Ordering.** `receivedDateTime` ascending, stable across pages, no repeats. An empty window is 200 with `rows: []`,
  `count: 0`, `next_page_token: null`.
- **The Graph path allowlist** gains `^/me/messages$` with `$filter`/`$select`/`$orderby`/`$top` built server-side
  only. Graph calls stay GET-only and fail closed.
- **Audit and alerts.** The audit carries the route, sender hash, window, row count and bearer label; never an
  address or content. Refusals and `needs_login` are returned to the caller, with no alert.

**Release.** One build cell plus one narrow release, issued by `2.0.0_SA_COO~O` as its own round label. It joins the
release train after the MX-r-8 slot-4 release as **slot 5**, under the C1-C6 surface rules, with CTO and CVO never-widen
halves (it adds a served surface).
- Acceptance is the laptop's four checks in the order, run from site Z on the released host:
  1. a listed row equals the message route's `internetMessageId`;
  2. an off-table sender is refused 403, and an empty window returns 200 with zero rows;
  3. paging with `page_size=1` continues without a repeated row;
  4. the transcripts and `/ms/*` bearers are refused.
- Plus two negative arms of this seat's:
  1. a page token with an altered sender or window is refused 400;
  2. a token carrying a raw Graph URL is refused 400.

**Sign-off.** CONTRACTS text changes and ENDPOINT does not.


### v1.6 addendum (2026-10-02 ~20:1xZ, 1.0.0_SA_CTO~O) -- C7 headless TEAMS route, the one write exception

Input: Andrew-direct, relayed by `0.0.0_AB_MSTR~Z` msg 28592 (laptop bus d38d682f, 17:17Z): "release the gateway /hx/teams
route TODAY". Build authority: laptop record `ANDREW_DIRECT_20261002_020xZ_EOD_UPDATE_AUTOMATION.md` ("you just build
it"). Request: `org/tier1_exec/4.0.0_SA_CRO/deliverables/SITEZ_GATEWAY_RELEASE_REQUEST_HX_TEAMS_20261002.md` @a53c8452b4.
Released by OG-rl-3 (opal-gateway `4231bd2ddc`, live 2026-10-02 19:23:40Z; ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261002_NFRA_OPLGTW_HX_TEAMS_RELEASE.md` @6b6bccb300).

**The change (C7).** A third headless prefix, the fixed literal `/hx/teams`, graded for distinctness like the other two.
It serves the laptop's LDO-001 (Andrew's Teams assistant) and is graded there; this project grades only its own release.

**Routes.**
- `GET /hx/teams/me`
- `GET /hx/teams/chats`
- `GET` and `POST /hx/teams/chats/{chat_id}/messages`
- `GET` and `POST /hx/teams/channels/{team_id}/{channel_id}/messages/{message_id}/replies`

**Rules that carry over from v1.2, unchanged.**
- An own static bearer (`gateway/teams/bearer`, label `teamsassist`), compared in constant time and accepted ONLY on
  this prefix.
- ONE fixed identity: MS_INGEST_IDENTITY's server-held delegated token (Andrew's). No caller-supplied identity.
- One Graph path allowlist per verb, failing closed; allow-by-key output; opaque page tokens; audit without content.

**The exception, stated plainly.** C7's "Graph calls are GET only" and "There is no write, send or reply verb" stay true
for `/hx/transcripts` and `/hx/mail`. They are NOT true for `/hx/teams`: its two POST verbs send a chat message and a
channel reply AS ANDREW. This is Andrew's word, not a widening of the other two prefixes.
- Send approval lives in the caller (LDO-001's reply-of-1 from Andrew), never in the route.
- The bearer's only holder is that caller.

**Graph scopes.** Chat.ReadWrite, ChannelMessage.Read.All and ChannelMessage.Send on MS_INGEST_IDENTITY. They were not
read at release.
- The two GET reads (`me`, `chats`) passed at OG-rl-3's ht.AC3.
- The two POST verbs stay UNEXERCISED until the first real send, which is Andrew's first End of Day post.
- A 502 carrying `graph_status` 403 is a missing scope. That is a row to Andrew, not a code change.

**Sign-off.** CONTRACTS text changes and ENDPOINT does not. The ratified-text half re-opens for `3.0.0_SA_CVO~O`.
- **Disclosed defect.** Round 12's enrichment list (item 2) requires a CVO never-widen half for any capability
  change. OG-rl-3 adds a served surface with write verbs, and it ran on the CTO and COO halves only. This seat's
  ruling named only its own half, so the omission is this seat's.
- **Remedy.** The CVO grades the live release post hoc against `4231bd2ddc` and this addendum. A REFUSED half
  routes the rollback named in the ruling (redeploy `3a7d6a7dc8`; revert the IAM ARN and the ALB path).

### v1.7 addendum (2026-10-03 ~19:5xZ, 1.0.0_SA_CTO~O) -- C3 records the fourth dataset, `dim_transaction`

Input: `3.0.0_SA_CVO~O`'s finding in its OG-gw-2 half (msg 28974,
`org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NEVER_WIDEN_OG-gw-2_HALF_20261003.md` @0cfe31652e). The ratified text named
three datasets (:37, :155, :309). The contract it governs has carried four since @32ebe6bee6. That change was written by
NFRA_MCPINDEX MX-r-6 step 0 under this seat's ruling B4
(`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be), released on
the gateway 2026-09-30 18:33Z under never-widen halves, with no OPLGTW addendum. This is that addendum.

**The change (C3).**
- The data-readable prefixes are `silver/dim_position/`, `silver/dim_balance/`, `silver/dim_asset/` and
  `silver/dim_transaction/`.
- `org/standards/NFRA_OPLGTW_CONTRACT.json` `fields.dim_transaction` is exactly 15 columns: `account_ref`,
  `business_date`, `trade_date`, `settlmnt_date`, `tr_cd`, `sb_cd`, `transaction_category`, `tran_srcde`,
  `debit_credit`, `cusip`, `ticker_symbol`, `quantity`, `price`, `gross_amount`, `net_amount` (read at `af2d762970`).
- C3's date semantics, closure and master rules apply to it unchanged.
- :37's "three silver datasets" reads "four" from v1.7.
- :309, the proposed first entitlement, is unchanged: Menachem's proposal names three datasets. Adding the fourth to it
  is its own act, below.

**Grants -- capability is not authorization.**
- From OG-gw-2, the grant writer ADMITS a verified-owner candidate naming `dim_transaction` over a non-empty subset of
  the 15 columns. This aligns the second writer with the contract the gateway serves.
- **Authorized today:** exactly ONE grant change. Andrew-direct 2026-09-30 ~13:0xZ, "Regarding schwab, sure." (record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_13xxZ_R20_ETFS_BDFEES_YES_SCHWAB_GRANT_YES_ADVI_LIFTED.md`
  @1eba868308) widens ONE existing Opal principal's Schwab grant to add `dim_transaction`, through the grant admin tool,
  with "no other grant change". That act is executed under its own record, not by a round-15 cell; it is not barred by
  this seat's G1 on OG-gw-2.
- **Every other `dim_transaction` grant** needs its own word from Andrew (the CVO's W1). FWD-9 (Andrew admits staff one
  at a time) stays DEFERRED.

**Sign-off.** CONTRACTS text changes (C3) and ENDPOINT does not. The ratified-text half re-opens for `3.0.0_SA_CVO~O`.
`prd-signoff` binds the ENDPOINT hash only, so this seat sends the request itself.

### v1.8 addendum (2026-10-08 ~15:5xZ, 1.0.0_SA_CTO~Z) -- C7 headless MAIL route admits by sender DOMAIN

Input: a cross-fabric request (CLAUDE.md rule 32) from the laptop `1.0.0_SA_CTO`, relayed by `0.0.0_AB_MSTR~Z` msgs 31615 and
31619 (laptop bus c544f4d5 and 418ddcfe). The laptop's measurement: `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~31/MAIL_ROUTE_MEASURED.md`.
Site Z's code read: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/MAIL_ROUTE_DOMAIN_READ_FACTS_20261008.md` @834beaddab.

**Whose words, and whose reading.** As the laptop carries them (NFRA_CTLPLN C-SEATS clause 9; this seat did not read the
record), Andrew asked on 2026-10-07 for his own mailbox to be read for work requests, a message considered only when its
sender's domain is one of the firms he named and its body names him. The route's shape below is this fabric's design to
serve that. It was stated to him at the `1.0.0_SA_CTO~Z` terminal on 2026-10-08 (~07:4xZ, ~15:3xZ). The firms are his: the
gateway admits a domain only from the table named below, and adding a firm is his word, never a seat's.

**The mailbox.** The route's one fixed identity, MS_INGEST_IDENTITY, is Andrew's own mailbox: `2.0.0_SA_COO~O` read the live
configuration on r28 `aa75078e1b` by a digest compare against the signed-in user's `whoami` and it reads EQUAL (msg 31840; one
comparison, no negative control, no address printed). No other mailbox is reachable by this route, before or after.

**The change (C7), two things.**
1. **Admission.** A message is admitted when its OWN sender is on the sender table (as today) OR its own sender's domain is
   on the DOMAIN TABLE. The domain is the text after the last `@`, compared case-insensitively and whole: no subdomain
   match, no suffix match. No thread is consulted. The message-by-id route applies the same rule.
2. **Listing.** `GET /hx/mail/messages` takes EXACTLY ONE of `sender` (as v1.4) or `sender_domain` (ONE domain, on the domain
   table). With `sender_domain` the Graph query filters on the received window only, and the gateway judges each row's own
   `from` against the requested domain: a row that fails is dropped and counted in the audit, never listed. A Graph filter
   on an address suffix is NOT used; it is untested.

**Rules that do not move.** GET only. The same prefix and bearer. Rows are v1.4's five fields exactly: no subject, body,
recipient or attachment name. The window is at most 31 days, `page_size` 1..50, 200 pages a request; a page of a domain
listing may hold fewer rows than `page_size`, and an empty page with a `next_page_token` is legal. The opaque token now
binds the sender OR the domain, and the window. The audit carries a hash of the domain, the rows listed and the rows
dropped; never an address or content.

**The body test is the caller's.** Whether the body names him (a whole word, the subject, signature and quoted text apart)
is judged by the laptop's caller on the message it fetches by id. The gateway does not read a body to decide a listing.

**The domain table.** One configured value read at start, like the sender table. **It holds the domains of the five parties
Andrew named and no other row's** (his 2026-10-07 ~18:3xZ record, item 6, read by `3.0.0_SA_CVO~Z`; not read by this seat).
The two registry files, `infra/logic/registry/scopes.json` (`tenant.email_domain`) and `infra/logic/registry/mail_parties.json`,
are where a party's domain is LOOKED UP, never a list to copy whole: `scopes.json` also carries the demo tenant's `demo.test`,
which is not one of the five and is not admitted. The release's own record lists each entry beside the party it belongs to,
five parties at most, and the never-widen halves read that list (v1.9, on the L4-R REFUSE of v1.8, msg 31862). An empty or unset table refuses every `sender_domain` request 403 before any Graph call, and
admits nothing by domain. A firm with no domain recorded is not considered.

**What this widens, stated plainly.** Today three exact addresses can be read. After this, every message from every
address at a listed firm can be listed and fetched by the bearer's holders. That is a widening of a served read: it
carries CTO, COO and CVO never-widen halves (round 12's enrichment item 2), and the halves name the table's entries.
**v2.4 addendum (`1.0.0_SA_CTO~Z`, 2026-10-09):** the mail bearer has TWO holders, each with its own value and its own audited label:
`msgpull` (the original holder) and `commassist` (the laptop Teams agent, added in r29 by issuer amendment A1 and ruling D4, on the
laptop's COMM_ASSIST ask relayed in msg 32212). Both read Andrew's own mailbox only, with the same five fields and the same domain table.
The r29 halves signed `commassist` as a named widening of who may read (CVO half
`deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-rl-15_r29_20261009.md` @c348b51df9). A third holder is a new widening and needs its own halves.

**Acceptance, run on the released host.**
1. A message from a listed domain, from an address NOT on the sender table, is listed and fetched.
2. Negative arms: an unlisted domain is refused 403; `sub.<listed domain>` is refused; a request with both `sender` and
   `sender_domain`, or neither, is refused 400; a token with an altered domain is refused 400; with the table empty every
   domain request is refused.
3. v1.4's four checks and two negative arms read as before (the three addresses still work).

**Release.** One build cell and one narrow release by `2.0.0_SA_COO~O`. The restart falls under row Z-S67: not inside the
12 hours before a 07:00 America/New_York send, and after the one-session question on `opal-gateway-bbg` is settled by
Andrew, who has said that sign-in is his to handle (2026-10-08 ~13:2xZ).

**Sign-off.** CONTRACTS text changes (C7) and ENDPOINT does not. The ratified-text half re-opens for `3.0.0_SA_CVO~O`.
`prd-signoff` binds the ENDPOINT hash only, so this seat sends the request itself.

### v2.0 addendum (2026-10-08 ~19:3xZ, 1.0.0_SA_CTO~O) -- staff usability: account identity, lots and realized gains, 13 months, the Tax SMA master; refresh answers once sent

Input: Andrew-direct 2026-10-08 ~17:4xZ at the `4.0.0_SA_CRO~Z` terminal, his four answers verbatim in
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261008_174xZ_GATEWAY_SCHWAB_FOUR_CALLS_ANSWERED.md` @116d52009d,
on the assessment `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/OPLGTW_SCHWAB_USABILITY_AND_TAX_MASTER_ASSESSMENT_20261008.md`
@139c8d018e (the brief for this addendum). Rulings: `ledger/ROUND_ANALYSIS.round31.md` R50-R55. Endpoint: FWD-10 to FWD-13 above.

**What this reverses, stated plainly.** v1 kept every raw account number and title out of every response (C2 :151,
`forbidden_field_classes`). From v2.0 those are GRANTABLE columns for named internal principals. Andrew's ground: "There are
only two mcp users at this time, me and alyssa".

1. **Account identity (C2, FWD-10).** `raw_account_id` and `account_title` leave `forbidden_field_classes` and become the
   grantable column class `account_identity`. It holds the account number and EVERY name and title field the source records
   (account title lines, taxpayer first, middle and last name and suffix, taxpayer title, alias, organization name, and any
   other name or title column the measurement finds); the exact list is round 32 item 4's printed schema, never typed here.
   - Stay forbidden, as named classes: `tax_identifier`, `mailing_address`, `email_address`, `phone_number`, and the three
     hidden-operand classes. A column whose class is not decided is forbidden.
   - `account_ref` stays the join key in every dataset. `account_identity` columns are returned beside it, never in place of it.
   - Every response that carries an `account_identity` column writes one audit record: principal, dataset, master, the
     count of accounts returned. No value, number or name is logged (C2's "never log raw IDs" stands for the audit).
   - **Authorized grants:** Andrew's and Alyssa's principals only, by his answer. Any other principal needs his own word.
2. **New datasets (C3/C4, FWD-11).** `fact_acc` (as `dim_account`: the account list, `account_identity` columns plus
   registration, type and date opened, no forbidden class), open lots (`fact_uln`, `fact_ult`), closed lots (`fact_rld`
   daily, `fact_rly`, `fact_rty` year-to-date). Each dataset's grain, types, units, sign and null semantics are recorded from
   the measured source as C3 requires; the contract's `fields` lists are written from round 32 item 4, and a column with no
   measured meaning is not served. C3's closure rule applies: a dataset is served for a date only when the completion
   record names it.
3. **Flow labels (C4, FWD-11).** `dim_transaction` carries a `flow_label` derived from `tr_cd`/`sb_cd` by a table in the
   contract, written from the vendor code list. An unlisted code labels `unclassified`, never guessed.
4. **History (C3, FWD-12).** A grant may set `calendar_months` (1 to 13) in place of `calendar_days`; exactly one is set.
   The window is the latest qualified complete business date and every business date on or after the same calendar day 13
   months earlier (month-end clamped). A date with no qualified completion record is reported unavailable (C3 unchanged).
   Measured 2026-10-08: master 08335338 holds 27 completion markers, 2026-08-31 to 2026-10-07, so the producer's metadata
   backfill (C3, surface S4) is the precondition for most of the 13 months; it reconciles against original inputs and
   repairs no source data. The query and export caps (A14) are not raised by this addendum; a measured run over 13 months
   decides whether any cap moves, as its own ruling.
5. **The Tax SMA master (C3, FWD-13).** Master `08403355` joins `masters` only after: (a) one list-only run returns files
   whose types and vendor filename grammar equal those of a control master over the same window (round 32 item 3); (b) the
   daily puller, its schedule (at least 30 minutes from the other two), the box's write grant and the silver conversion
   carry it in the SAME structure as the other two masters; (c) a day lands, converts and qualifies. If (a) returns zero
   files, the outcome stops there and reports a Schwab-side entitlement. (b) is infrastructure under CLAUDE.md rule 13 and
   is placed with an AE lane by the issuer's order; it is a never-widen act with halves.
6. **Refresh and code redemption answer once sent (C1, R50).** C1's "refresh has 30 seconds" now reads: the budget bounds
   the START of the conditional transaction that consumes a generation or a code. Once that transaction is sent, the handler
   awaits its result and answers it, even past the budget. A budget that elapses before it is sent answers 503 with nothing
   consumed. Ground: row Z-W35-S1 (`server.py:367-382`).

**Rules that do not move.** One master per call, never summed across masters or dates; prompt-like text in data stays
data; no grant mutation from MCP; original Parquet and bronze stay unavailable; FWD-1 to FWD-8 are unchanged.

**Acceptance (added to the matrix).**
- A21 (FWD-10): number and name lookups under a granted principal; the same under a grant without `account_identity`,
  refused; a request for a forbidden class, refused; the audit record holds counts only.
- A22 (FWD-11): lot totals recomputed from silver for independently chosen accounts and dates equal the answer; an
  unlisted transaction code labels `unclassified`.
- A23 (FWD-12): two dates a year apart answered; a date with no completion record reported unavailable.
- A24 (FWD-13): the list-only run beside its control; then one landed, converted, qualified and queried day.
- A25 (C1 item 6): a rotation slowed past the budget returns the new pair and the family stays live; a deadline before the
  transaction answers 503 and the stored generation is unchanged; the same two arms for code redemption.

**Sign-off.** ENDPOINT (FWD-10 to FWD-13) and CONTRACTS (C1, C2, C3, C4) change. The ratified-text half re-opens for
`3.0.0_SA_CVO~Z` (signing for the ~O CVO seat until it is seated, msg 31856). The brief half: the brief is
`4.0.0_SA_CRO~Z`'s assessment, accepted as written by the CRO (CLAUDE.md rule 27, PROPORTIONATE SIGN-OFF).

### v2.1 addendum (2026-10-08 ~23:2xZ, 1.0.0_SA_CTO~O) -- Alyssa's Tax SMA quarter: the thread, the key, since inception, lots as of quarter end, Black Diamond, the 08403355 backfill

Input: Andrew-direct 2026-10-08 ~22:0xZ, verbatim in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_220xZ_ALYSSA_TAX_WORKFLOW_SINCE_INCEPTION_GL_LOTS_LAST4_KEY_SCHWAB_AND_BD.md`
@618699ceeb, and his ~21:2xZ "asap" (`ANDREW_DIRECT_20261008_212xZ_ALYSSA_13M_AND_TAX_SMA_MASTER_ASAP.md` @6233bae5de). Brief:
`docs/briefs/oplgtw-tax-workflow-midstream-brief-20261008.md` @dae0456eb4 (`4.0.0_SA_CRO~Z`, midstream). Endpoint: FWD-14 to
FWD-19 above; FWD-14 is the thread and every other outcome widens it. Round 32 is issued and frozen: this addendum is cut
from round 33 on.

**Scope bound, his words:** "We don't have to do the whole workflow for her. We just have to be able to give her the right
information." Every outcome is a read. The gateway computes no return (QTD, YTD or annualized); Alyssa's report and its
scripts stay hers.

1. **The Tax population and its grant (C2, FWD-14, FWD-18).** The Tax SMA roster (MDPF_TAXSMA's reader, reused) is the
   account list. Alyssa's grant carries `account_identity`, every Tax account in each of the three sources (masters 08335338
   and 08403355, and Black Diamond), a window reaching each account's roster inception, and the datasets below. It carries
   no download operation: Andrew at the laptop, 2026-10-08 ~19:2xZ, "no downloads needed yet"
   (`ANDREW_DIRECT_20261008_184xZ_FIVE_POINTS_KIMMY_EFFICIENCY_ALYSSA_MCPORTAL_OPEN_CALLS_AGGREGATE.md` line 105). The hidden
   classes of v2.0 item 1 stay hidden.
2. **v2.0 item 1's last line is struck** ("Any other principal needs his own word"): his 17:4xZ answer was (a), named Opal
   staff, and set no further gate (`3.0.0_SA_CVO~Z` review note 1, msg 32002). Each grant is still an operator act under C2.
3. **Black Diamond (C3, C4, FWD-18).** The Cottonwood RIA's Black Diamond silver (`blackdiamond/cottonwood/silver/`:
   `fact_holdings`, `fact_realized`, `fact_unrealized`, `fact_transactions`) is a source for the roster's Black Diamond Tax
   accounts only, read only, scoped by account in the grant. This reads his ~22:0xZ words ("there are the ones that are in
   Black Diamond", "Alyssa is going to need to go to both of those places") as covering those accounts and nothing wider in
   that firm's data. The producer is OPAL_TAXSMA_PT2 (laptop fabric); its table addresses and freshness are its owner's
   answer, asked cross-fabric 2026-10-08 ~22:0xZ. The answer shape is the Schwab one, with the source named.
4. **The account key (C4, FWD-15).** A lookup tool takes a full number, or last four plus a name. Measured: in 08335338,
   1,831 of 5,320 distinct last-fours belong to more than one account, so last four alone is refused as a key. An ambiguous
   match returns its candidates and picks none.
5. **Since inception (C3, FWD-16).** The window floor for a Tax account is its roster inception date. The completion-marker
   backfill (v2.0 item 4) reaches back to the earliest roster inception among the granted accounts; 13 calendar months
   remains the cap. Flow labels add `security_transfer_in`, `security_transfer_out` (at market value) and `advisory_fee` as
   required members of the v2.0 item 3 table.
6. **The value field (C4, FWD-14).** The quarter-end value is served as `eqty_incl_option` (9 of 9 tie to the workbook within
   $1 at 2026-09-30; `net_mv_plus_cash` ties 0 of 9). `net_mv_plus_cash` may be served beside it, each named; neither is
   substituted for the other. MDPF_TAXSMA's contract values Tax accounts on `net_mv_plus_cash`; that difference is surfaced to
   its owner, not resolved here.
7. **Lots and gains (C4, FWD-17).** Realized gain/loss in four buckets (short/long term x gain/loss) from `fact_rld`,
   `fact_rly`, `fact_rty`, and Black Diamond `fact_realized`. Unrealized gain/loss and cost basis from the lots held on the
   requested date (`fact_ult`; Black Diamond `fact_unrealized`), short positions included. A lot whose basis the source marks
   missing returns `cost_basis: null` with `basis_status: missing`, never zero. Top-10 holdings from `dim_position`/`fact_rps`
   and Black Diamond `fact_holdings`. Sector allocation is NOT served: no source exists in either custodian's silver.
8. **The 08403355 backfill (C3, FWD-19).** After v2.0 item 5 admits the master, the existing backfill script
   (`infra/aws/ec2/canonical-schwab-si2/sdd-backfill-08335338.ps1`, master parameterized or copied) runs from the earliest
   roster inception among the master's accounts. Infrastructure under CLAUDE.md rule 13, placed with the AE lane by the
   issuer's order; a never-widen act with halves.

**Rules that do not move.** One master or source per call, never summed across sources or dates; prompt-like text in data
stays data; no grant mutation from MCP; FWD-1 to FWD-13 are unchanged.

**Acceptance (added to the matrix).**
- A26 (FWD-14): the thread account's quarter under Alyssa's principal, beside its statement.
- A27 (FWD-15): a unique key, a colliding key and a wrong-client key, each answered as item 4 says; last four alone refused.
- A28 (FWD-16): two accounts' since-inception records recomputed from silver; the floor is the roster date.
- A29 (FWD-17): one account-quarter's four buckets tied to Schwab's totals line; a missing-basis lot reads missing.
- A30 (FWD-18): one Black Diamond Tax account beside one Schwab Tax account, same fields (v2.2: the non-roster refusal arm is
  struck; see the v2.2 addendum).
- A31 (FWD-19): the backfill enumerate record; one pre-collection date answered.

**Sign-off.** ENDPOINT (FWD-14 to FWD-19) and CONTRACTS (C2, C3, C4) change. The ratified-text half re-opens for
`3.0.0_SA_CVO~Z`. The brief half: the brief is `4.0.0_SA_CRO~Z`'s, accepted as written by the CRO (rule 27, PROPORTIONATE
SIGN-OFF).

### v2.2 addendum (2026-10-09 ~02:0xZ, 1.0.0_SA_CTO~O) -- any account, any source, for the connected users; per-user scoping deferred

**Input.** Andrew-direct 2026-10-09 ~01:5xZ at the `4.0.0_SA_CRO~Z` terminal. His words are verbatim in
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261009_015xZ_OPAL_STAFF_MAY_READ_BLACK_DIAMOND_THROUGH_GATEWAY.md`
@0035550443:
- "yes they can do so (the opal staff reading BD data through opalgateway)";
- "any account";
- "any account at black diamond, orion, eclipse, bloomberg, ycharts, schwab, smartx, eclipse, any vendor any everything";
- "we can always work on per user entitlements later, nobody uses mcp right now aside from alyssa and she's fine";
- "do not hold up progress or work about theoretical users that arent even connected and we'd apply entitlement scoping at
  that time, not now".

**What this changes:**

1. **Item 3 of v2.1 widens.** Black Diamond is a source for ANY Black Diamond account, not only the Tax roster's. FWD-18's
   ACCEPT and A30 are amended above. The roster still names which accounts are Tax accounts (FWD-14 to FWD-17). It no longer
   bounds the grant.
2. **Andrew's and Alyssa's grants reach every account in every source the gateway serves.** Today the sources are Schwab
   masters 08242234, 08335338 and 08403355, and Black Diamond. A source the gateway adds later joins these grants without a
   new word. His words name Alyssa as the one user ("nobody uses mcp right now aside from alyssa"). The Bloomberg concierge
   account `opalbloomberg`, which answers Teams requests from other people, gets NO data grant from this addendum. It gets
   only item 5's five tool rows. A data grant for it needs its own word. (Corrected before the ratified-text signature, on
   `4.0.0_SA_CRO~Z`'s v2.2 note: the first text named `opalbloomberg` as a connected principal, which was this seat's
   reading, not his words.)
3. **Per-user scoping is DEFERRED, not removed.** The C2 machinery stays: per-principal grants, the revision check, the audit
   record and the hidden field classes. Each grant is still an operator act. The scoping is applied when a further user
   connects, on that user's own word.
4. **Unchanged, because his words do not reach them:**
   - the hidden classes (tax identifiers, mailing address, email, phone);
   - Alyssa's no-download (his ~19:2xZ "no downloads needed yet"; downloads were not mentioned at ~01:5xZ);
   - one master or source per call, never summed, and never joined across firms in one response;
   - no grant mutation from MCP.
5. **The identity tool allowlist** (`infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt`) gains five read tools for
   `opalbloomberg`: opal_discover, opal_describe, blackdiamond_list_fees, find_sharepoint_site and search_files. Each row
   cites the record above, and they ride release r29.
6. **Egress.** "infinite egress on all channels now (aside from BBG which goes through its queue logic)" is a CLAUDE.md law
   edit, asked of `0.0.0_AB_MSTR~Z`. This PRD does not restate it and builds no vendor call on it.

**Sign-off.** ENDPOINT changes: FWD-18's ACCEPT. CONTRACTS change: C2 grant width and A30. The ratified-text half re-opens
for `3.0.0_SA_CVO~Z`. The brief half carries no new brief: the input is Andrew's word, recorded by the CRO.

### v2.3 addendum (2026-10-09 ~03:3xZ, 1.0.0_SA_CTO~O) -- the Bloomberg account mirrors Andrew's principal

**Input.** Andrew-direct 2026-10-09 ~03:2xZ at this seat's terminal, verbatim in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_032xZ_OPAL_GATEWAY_BBG_MIRRORS_OPALGATEWAY.md`:
"opal-gateway-bbg should be an exact copy of opal-gateway for now, just make it mirror whatever is on opalgateway for
consistency, eventually we will make rules but not yet".

**What this changes:**

1. **v2.2 item 2's last sentences are reversed.** `opalbloomberg@opalinvest.com` now holds the same grants as Andrew's
   principal. That covers every account in every served source, the same hidden classes and the same operations.
2. **v2.2 item 5 is superseded.** `opalbloomberg` leaves identity scoping. Its `_SEED` entry in `app/identity_scope.py` and its
   overlay rows in `identity_tool_allowlist.txt` are removed, so it is UNSCOPED, as Andrew's identity is. Its tool set is
   whatever Andrew's is.
3. **"for now".** This is today's state, not a design. Per-identity rules for this account are deferred until he names them.
4. **The Opal-users-only gate. It ships with item 1 or neither ships.** Andrew-direct ~03:3xZ
   (`ANDREW_DIRECT_20261009_033xZ_BBG_CONCIERGE_OPAL_USERS_ONLY_GATE.md`): "it should only accept inquiries from opal capital
   users however, no external users, should not even respond at all". For the `opalbloomberg` principal:
   - Teams reads return no message whose sender's Entra UPN is not `@opalinvest.com`.
   - The sends refuse any chat or channel holding a member outside `@opalinvest.com`.
   - Identity comes from Graph records, never display names. Unreadable counts as external.
   - Acceptance A32 covers three arms: an external sender's message is absent from the poll; a send into a mixed chat is
     refused; an all-Opal chat is served.

**Unchanged.** Every rule of v2.2 that his words do not reach:
- Alyssa's grant and her no-download;
- the hidden classes;
- never joined across firms;
- no grant mutation from MCP.

**Consequence carried to r29's read-back.** An unscoped identity's consent asks the full `GRAPH_SCOPES` envelope. If the
Microsoft 365 tools refuse on the current token, the act is a fresh sign-in in the BG seat's window. It is named then, with
the evidence.

**Sign-off.** The CONTRACTS change: C2 for one principal. The ENDPOINT is untouched. The ratified-text half re-opens for
`3.0.0_SA_CVO~Z`. The brief half is his word, recorded by this seat.

### v2.4 addendum (2026-10-09 ~08:2xZ, 1.0.0_SA_CTO~Z) -- C7 names the mail bearer's two holders

**Input.** `3.0.0_SA_CVO~Z`'s r29 half @c348b51df9 signed `commassist` as a second mail-bearer holder and carried one item:
C7 `:694` still read "the bearer's one holder" (msg 32522, re-sent after `1.0.0_SA_CTO~O`'s retirement). C7 now names `msgpull`
and `commassist`, so the ratified text matches what r29 serves. The site-Z CTO lane is `1.0.0_SA_CTO~Z` from 2026-10-09 ~07:4xZ
(Andrew-direct "we don't need CTO~O anymore, you just lead the fabric here").

**Sign-off.** CONTRACTS wording only (C7), recording a widening the three r29 halves already signed. The ENDPOINT is untouched,
so under proportionate sign-off no half re-opens.

### v2.5 addendum (2026-10-09 ~18:5xZ, 1.0.0_SA_CTO~Z) -- C4 names the E2 write tool `copy_site_file_to_s3`

**Input.** `3.0.0_SA_CVO~Z` signed the OG-rl-16 CVO half @9b6003cd3b as a named widening on this seat's ruling (msg 32663). It
carried one item (msg 32942): v2.4 names no `copy_site_file_to_s3` and no `fee_statement` write. This addendum records it.
The CTO Half 1 is @5e258448d2.

**C4 (typed tools), one write tool added.** `copy_site_file_to_s3`, served from release r30-E2 (`a88661b145`):
- **Caller:** only a principal that already holds `write_files`. It copies ONE `.xlsx` SharePoint item that the caller can
  already read with their own Graph token.
- **Destination:** exactly ONE prefix, `opal-data-assets/smartx/49financial/bronze/fee_statement/quarter=<q>/`, the output of
  `lib/opal_naming.py address()`. The caller chooses neither the bucket nor the prefix.
- **Write rule:** a conditional put (`IfNoneMatch="*"`). An existing key is refused and never overwritten, and each call is
  capped at 50 MiB.
- **Grant:** the gateway role's one PutObject policy on that prefix. Its name and path are builder output (rule 30), and the
  prefix had 0 writers in the gateway before this.
- **Who can call it, as a denominator:** the release's Phase C prints the count of `write_files` holders (no ids), so the
  widening carries its population at release.

**Not this addendum.** The `.pptx` market_update writer on `opal-data-transcripts` (OG-ab-2, rows W49-S3 and W49-S4) is a
separate tool with its own grant. It is not admitted here.

**Sign-off.** This adds CONTRACTS text (C4) for a widening that the three OG-rl-16 halves already signed. The ENDPOINT is
untouched. Under proportionate sign-off the CVO's ratified-text half reads this wording; no delivery is withheld.

### v2.6 addendum (2026-10-13 ~20:3xZ, 1.0.0_SA_CTO~Z) -- the panel's cadence and depth read (FWD-20), and harvest for Opal asset managers (FWD-21)

**Input.**
- Andrew's site Z and AMGT voice memos, 2026-10-13, verbatim in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_SITEZ_20261013.md` sections 1.1-1.2
  (cross-box ORDER XB-20261013T185926Z-4d72, outcomes Z3 and Z5).
- Andrew-direct ~20:0xZ (call 8, relayed by MSTR~Z msg 33727): all 24 harvest prefixes SERVE to Opal principals, raw
  included. This widens the direction's V1 rule (derived layers and links only) on his own word.
- Brief: the CRO's site Z and AMGT alignment reports, section 7 of the direction.

**Contract changes:**
1. **FWD-20 is a read for NFRA_MCPORTAL, not a panel of this project's own.** It adds no second panel, alert or
   monitor. Display and control are MC Portal's FWD-20 and FWD-21.
2. **FWD-21 widens the gateway's reach to `opal-data-harvest`, for Opal principals only.** The C2 owner gate and the
   Opal-users-only rule (v2.3 item 4, Andrew 10-09: "should not even respond at all" outside Opal) apply unchanged. No
   new resource name is typed: any new name is `lib/opal_naming.py` output (CLAUDE.md rule 30). The grant is written by
   the existing grant writer.
3. **Order.** Both come after the r30 release (OG-pf-1 + OG-tg-1 + OG-bd-2 + OG-sh-1;
   `ledger/CTO_RULING_R37_ONE_RELEASE_PF1_TG1_BD2_SH1_20261013.md`), which follows NFRA_MCPORTAL MP-z-5. The project
   closes only after Andrew reads MC Portal FWD-20 (his 10-12 condition).

**Sign-off.**
- ENDPOINT changes, so the ratified-text half re-opens for `3.0.0_SA_CVO~Z`.
- The brief half is the CRO's alignment reports on Andrew's memos, accepted as written (rule 27, PROPORTIONATE
  SIGN-OFF).

### v2.7 addendum (2026-10-13 ~20:5xZ, 1.0.0_SA_CTO~Z) -- FWD-21 V1 admits by identity

On `2.0.0_SA_COO~O` msg 33760. v2.6's FWD-21 ACCEPT said both "Opal principals" (Andrew's call 8) and "Grants go through
the existing grant writer". The writer has no harvest scope today; its records cover the Schwab/BD data-grant family.
Ruled for V1:
- Admission is by IDENTITY (OG-tg-1's Opal-user predicate), which is Andrew's words exactly. No grant-writer build is
  needed.
- The one-writer rule binds once a per-person harvest grant exists, at MC Portal's control outcome.

ENDPOINT text changes, so the ratified-text half re-opens for `3.0.0_SA_CVO~Z`. The brief half is unchanged in
substance.

### v2.8 addendum (2026-10-13 ~21:0xZ, 1.0.0_SA_CTO~Z) -- FWD-21 PROOF: the research-only arm and the census's store

On two notes delivered with the v2.7 signatures:
- **`2.0.0_SA_COO~ZB` F1** (msg 33767): restores the AMGT brief's "research data only" boundary as a proof arm. An
  asset manager is refused a Schwab and a Black Diamond tool unless Andrew admits it to v2.2's connected set.
- **`3.0.0_SA_CVO~Z`** (msg 33770): the principal census reads the identity store that admission uses, never the grant
  store. Also carried for R4's release pair: the internal reader role's S3 read on `opal-data-harvest` (`gateway-global-internal-reader-role`, which
  `harvest_read.py` assumes; corrected 2026-10-14 per row Z-S107, never `opal-gateway-role`) is a widening and is
  named as one in that pair.

PROOF text changes, so both halves re-open at these bytes.

### v2.9 addendum (2026-10-14 ~03:0xZ, 1.0.0_SA_CTO~Z) -- C-PERSON: the gateway honours MC Portal's per-person access records (NFRA_MCPORTAL C18)

On `3.0.0_SA_CVO~Z`'s note with the NFRA_MCPORTAL v0.8 signature (msg 33950): MC Portal's C18 needs the gateway to honour
a new per-person record kind, and this PRD still admits tools and tiers from the deploy-time files only.

**C-PERSON -- the gateway reads per-person tool, channel and tier records from the grant store.**
- `decide()` reads a person's per-person record from `gateway-access-state-table`. MC Portal C18 writes it, through the
  ONE existing grant writer.
- The deploy-time files (`identity_tool_allowlist.txt`, the `deploy-to-ec2.sh` rosters) stay the FLOOR. A record narrows
  what the floor admits for that person. It widens only to a tool the floor already lists for some principal, and never
  to a tool the deployed gateway does not serve.
- A record is honoured on that person's next call.
- With no record present, behaviour is exactly as today: the floor governs.
- The Opal-users-only gate (v2.3 item 4), the C2 owner gate and tier admission (msg 33940) are unchanged and evaluated
  first. A record can never admit a non-Opal principal.
- **Rollback:** delete the record kind, and the floor governs.

**Whose cell:** NFRA_OPLGTW cuts the gateway reader as its own cell, in the round after r30 and the tier-admission
release. NFRA_MCPORTAL's first FWD-21 write cell (F2) waits on it. MC Portal's read-only cell (F1) does not.

ENDPOINT unchanged; CONTRACTS change, so the ratified-text half re-reads under proportionate sign-off (no delivery
withheld).

### v3.0 addendum (2026-10-14 ~13:1xZ, 1.0.0_SA_CTO~Z) -- FWD-22: typed tools over every contracted bucket table; G1 harvest is the first enrichment

**Input.** Andrew-direct 2026-10-14 ~12:4xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_124xZ_GATEWAY_DATA_CONTRACTS_CENSUS_CRO_FANOUT.md`): the gateway is live with these tables by Friday 2026-10-16,
harvest first. Directive to `4.0.0_SA_CRO~Z`: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` @06ae2a3485. G1 delivered: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md` @0d7c29b3c5 (58,639 of
58,639 keys, 78 datasets, 78 contracts, 12 typed tools).

**One new outcome, FWD-22, enriched per group.** Each later group (G2-G6) lands as an enrichment list in an addendum.
The outcome text does not change per group, so the ratified-text half is signed once for FWD-22.

**G1 enrichment list (harvest; Opal principals only, admitted as FWD-21 admits; no firm fork -- Opal's own research):**
1. Build the typed tools of G1 section 3 in the gateway app beside `harvest_read.py`, reusing `harvest_read.admit()`
   and its audit row: `harvest_resolve_security`, `harvest_security_coverage`, `harvest_get_chatter`,
   `harvest_search_articles`, `harvest_get_article`, `harvest_get_fundamentals`, `harvest_get_research`,
   `harvest_get_filing_analysis`, `harvest_get_peers_and_scores`, `harvest_query_columns`.
2. **`harvest_describe_dataset` is NOT built.** `opal_describe` / `opal_discover` already serve the one catalog; they
   reach table grain through NFRA_MCPINDEX FWD-22, and the contracts live in the catalog rows (one carrier, no second
   registry).
3. **`harvest_get_published_analysis` invokes `opal-amgt-scoped-api`.** That invoke is a NEW widening for the gateway
   role. It ships only with its own never-widen ask (both halves name the invoke and its rollback). If the ask is not
   signed by the cut, the cell ships the other tools and this one follows.
4. Bloomberg bronze tables (bestdata, refdata, histdata, segments, price history, identity, exec_officers) are read
   from the bucket only, under call 8's "all 24 prefixes SERVE to Opal principals". No tool calls Bloomberg.
5. Retired as tool targets (they stay in the bucket): `publication-links/v1/`, `publications/v1/`. The hyphen
   `amgt/harvest/gold/research-dossier/` is retired only after the cell reads that `research_dossier` supersedes it
   (G1 marks it inferred).

**Order.** OG-hv-2 (the grant) lands first, since every typed tool reads through it. The G1 tools cell is cut next,
ahead of OG-ap-17 and MX-r-13, on Andrew's priority ("I would prioritize that as number one"). `2.0.0_SA_COO~O` sets
the fan-out.

**Sign-off.** ENDPOINT changes (FWD-22 added), so the ratified-text half re-opens for `3.0.0_SA_CVO~Z`. The brief half
is the CRO's G1 census, written by the CRO (proportionate sign-off). Later group enrichments are CONTRACTS-only.

### v3.1 addendum (2026-10-14 ~14:1xZ, 1.0.0_SA_CTO~Z) -- FWD-22 enrichment for G2, G3, G5, G6; the client-data tool shape

**Input.** `4.0.0_SA_CRO~Z` census, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/INDEX.md` (commits 339a2804d7, 35f45893a7): G2 assets silver (131 contracts),
G3 portal-v2 (42), G5 ETFs (36), G6 news (12). G4 (mdpf gold delta) is still running. `3.0.0_SA_CVO~Z` msg 34081 notes:
FWD-22 DONE WHEN now says REALIZED at 6 of 6, and the 50 KB default cites G1 section 3.

**Ruling 1 -- client data is served by ONE set of question-shaped tools, not one tool per vendor table.** G2 proposes 40
vendor-specific tools. Andrew's word is "We need to be able to decide what accounts and what firm we are looking for and
what platform we are looking for", so firm and platform are INPUTS and the vendor is an adapter behind the tool:
- `client_resolve_account(firm, account_last4, platform?)` -> candidate list (last-4 is never unique: 49F BD 2,741 of
  6,186 collide, Schwab about 54%, SmartX 2,692 of 5,999). Every other client tool takes a resolved account id.
- `client_get_holdings`, `client_get_transactions`, `client_get_allocation` (model assignment + targets),
  `client_get_lots` (unrealized + realized), `client_get_performance`, `client_get_fees`, `client_get_profile`; BD-only
  `client_get_insurance`. Each takes `firm` (one), `account`, `platform?`, `as_of`.
- The adapters are the G2 contracts (BD 30, Orion/Eclipse 9, SmartX 13, Schwab 57, Commonwealth 12, Tax SMA 1). A table no
  question reaches is catalogued (MCPINDEX) but gets no adapter this round.
- `blackdiamond_list_fees` is kept (it reads live 49F fees); `client_get_fees` wraps it and adds Cottonwood behind a
  one-firm fence. The existing `schwab_*` family is kept; its `dim_*` views become the Schwab adapter.

**Ruling 2 -- admission for client data is the DATA-GRANT class.** Every `client_*` tool goes in `DATA_GRANT_TOOLS`,
never `NATIVE_TOOLS`. A principal reads a firm only with that firm's data grant (as `schwab_*` today). Being an Opal
user is not enough for client data. The harvest, portal, ETF and news tools stay in the read class.

**Ruling 3 -- the firm fence, per vendor (G2 finding 2).** Where the firm is a key segment (BD, Orion, Eclipse, Schwab,
Commonwealth), the adapter reads only that firm's prefix. Where it is a ROW column (SmartX, four firms per object, Z-S109;
Tax SMA's RIA column), the adapter filters rows in code before anything is returned, and the cell proves it with a
two-firm negative arm. Firm spellings map to one canonical input: `49financial` (= `49f`, Schwab masters
08242234/08335338/08403355), `cottonwood`, `inflection` (= `orion/4698`). Schwab masters overlap (7,534 accounts of
08242234 and all 30 of 08403355 also sit under 08335338): the adapter dedupes by account and never sums across masters.

**Ruling 4 -- the platform input matches the source's own label.** The labels conflict across SmartX/BlackDiamond, Tax
SMA and MAM (G2 finding 8). No crosswalk is guessed: each answer carries `platform_label` and `platform_label_source`, and
`platform` filters on the source's own label. A crosswalk is a later enrichment once one is declared.

**Ruling 5 -- read where the data is live.** Live 49F BD silver is `s3://opal-data-bd/silver/`, not
`opal-data-assets/blackdiamond/49financial/` (G2 finding 4). The adapter reads the live store. The `49-schwab-conv`
skill tables in `opal-data-bd` stopped on 2026-07-23 and are NOT served. Snapshot-in-every-partition tables (Orion
`fact_transactions`/`fact_performance`, BD `dim_advisor_fee_role`) are read from the newest partition only. 08403355 is
added to `NFRA_OPLGTW_CONTRACT.json` and `infra/logic/registry/scopes.json` in the same cell (G2 finding 5).

**G3 portal-v2 (no firm fork except mdpf scopes):** keep the five `portal_index` tools; build the 9 purpose-built tools of
G3 section 3.4 (`mdpf_get_category_views`, `portal_get_model_positioning`, `portal_get_model_attribution`,
`portal_get_market_returns`, `portal_get_market_regime`, `portal_get_macro`, `portal_get_valuation`,
`portal_get_security_scan`, `portal_get_pipeline_freshness`). The internal reader already reads `json/*` and `platinum/*`.
`json-tiered/*` (market returns) is a widening and goes in the G3 ask. ADVI perfrp, tickets and trade submissions are NOT
served (catalog holds and PII, unchanged). Row Z-S114 (`/json-tiered/*` public at the edge) is ruled separately: close it
(msg to `2.0.0_SA_COO~O` 13:53Z).

**G5 ETFs (Opal funds and partner ownership):** wave A = `etfs_get_partner_ownership` (firm REQUIRED),
`etfs_get_ownership_rollup` (returns the platinum dashboard's own totals; the tool sums nothing across firms),
`etfs_get_monthly_report`, `etfs_get_fund_holdings`, `etfs_get_fund_nav_history`, and `etfs_get_positioning` EXTENDED with
`as_of` and `fund_ticker`. Wave B = the rival-fund tools (peer group, trades, flows, compare, who-holds, security reference,
coverage, research notes; each passes the row's `claim` through) and `etfs_get_new_securities`,
`etfs_get_fund_bloomberg_profile`. Rule: re-run parts supersede, so read the newest part per date and never sum parts.

**G6 news:** build the 5 tools of G6 (c) (`news_search_articles` with a 14-day window cap, `news_trending_topics`,
`news_keyword_intelligence`, `news_market_mood`, `news_for_security`: harvest mention index first, then a text match
labelled `match: text`). The frozen semantic chain, the Seeking Alpha URL ledger, the empty `opal-harvest-articles` and
`market-updates` are NOT served. Nothing is deleted: whether to revive or retire those pipelines is outside this
project.

**Widenings: ONE never-widen ask per group, not per tool.** Each ask lists every prefix or table the group's tools read,
the role and the rollback per key: G2 (`opal-data-assets` silver prefixes and `opal-data-bd/silver/`), G3
(`opal-data-portal-v2/json-tiered/*`), G5 (`opal-data-etfs` prefixes), G6 (the four live news DynamoDB tables + the two
portal singletons). The reads go through `gateway-global-internal-reader-role`, as OG-hv-2 does.

**Order to Friday 2026-10-16** (`2.0.0_SA_COO~O` sets the fan-out; up to 8 workers):
1. G1 harvest tools (cut on v3.0).
2. G3 portal tools (almost no widening) and the G2 core: `client_resolve_account`, `client_get_holdings`,
   `client_get_transactions`, `client_get_allocation`, `client_get_fees`.
3. G6 news tools and G5 wave A.
4. G2 rest (lots, performance, profile, insurance), G5 wave B.
Pipeline defects the census found (49f converter OOM Z-S110, Eclipse stall Z-S111, ETF canon fan-in Z-S112, Sept report
coverage Z-S113) are not gateway work: each tool states the freshness it reads, in trading days.

**Sign-off.** ENDPOINT changes (FWD-22 DONE WHEN and the ACCEPT citation), so the ratified-text half re-opens for
`3.0.0_SA_CVO~Z`. The brief half is the CRO's census (proportionate sign-off).

### v3.2 addendum (2026-10-14 ~14:0xZ, 1.0.0_SA_CTO~Z) -- G2 client data reads through firm-scoped roles, never the global internal reader

On `3.0.0_SA_CVO~Z` msg 34104 (v3.1 review `org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_REVIEW_NFRA_OPLGTW_v3.1_RATIFIED_TEXT_20261014_Z.md`).
It amends v3.1's widening paragraph for G2 only:
- **Key-segment vendors (BD, Orion, Eclipse, Schwab, Commonwealth) read through firm- or vendor-scoped reader roles**
  whose S3 grant is prefix-conditioned to ONE firm. The existing Schwab / Black Diamond / firm reader roles are used first
  (build ladder step 2). A missing one is a new role named by `lib/opal_naming.py`. The fence holds at IAM, not only in
  code.
- **Only the mixed-firm objects (SmartX, four firms per object; Tax SMA's RIA column) rely on the code row filter.** G2's ask
  names the role that reads them and states that the fence there is code, with its two-firm negative arm.
- `gateway-global-internal-reader-role` NEVER gains a G2 client-data read. G1, G3, G5 and G6 (Opal's own data) still read
  through it.

CONTRACTS-side; ENDPOINT unchanged.

**CRO~Z brief-half corrections (msg 34106, review `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/L4R_REVIEW_NFRA_OPLGTW_v3.1_BRIEF_20261014.md@9a10f91cf8`), adopted as contract text:**
1. **G1 (binds the first cut):** `chatter_daily`, `article_security_mention` and `chatter_window` are read from the NEWEST
   part of the newest date partition only. `harvest_get_chatter` returns `data_status` per day, so 0 articles never reads
   as "no chatter". `harvest_resolve_security` answers a CUSIP with `not_held`.
2. **G5 `etfs_get_monthly_report`:** each partner's coverage comes from that partner's report CSV (`# coverage:` line),
   never from `coverage_verdict.json`. For September the verdict says 21/21; the CSVs say Cottonwood 20/21 and Inflection
   18/21 (Z-S113). Z-S113 is a correctness defect, not a freshness one.
3. **G2 firm inputs:** SmartX rows whose firm has no canonical input (Titleist, Canopy, Parable: no `firm_id` in
   `partner_roster.json`) are never returned until that firm is registered. An unknown `advisor_id` is never mapped to
   the nearest firm.

### v3.3 addendum (2026-10-14 ~14:3xZ, 1.0.0_SA_CTO~Z) -- FWD-22 enrichment for G4 (mdpf gold delta); census 6 of 6 landed

**Input.** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G4_mdpf_delta.md` @7ec87a87e5 (msg 34112). Every gold table in `opal-data-mdpf` equals what portal-v2
serves, leaf for leaf (aum_metrics 173/173, account_distribution 550/550, aggregate_aua 17,360/17,360 cells). The delta
is the feed layer: account-grain model AUA, per-model composition, and the AI security-classification index.

**G4 enrichment list:**
1. The four existing `mdpf_get_*` tools are KEPT unchanged this week.
2. **Account-grain model AUA is client data.** It is NOT a separate `mdpf_get_account_model_aua` tool. It becomes the
   MDPF adapter of `client_get_allocation` (Ruling 1): the canonical Opal `model_key`, `cohort_class` and
   `model_value` per account. It is read from `opal-data-mdpf/mdpf/feeds/model_aua_positions/<firm>/` through a
   one-firm reader role (v3.2), newest partition only. Feed label D carries served period D-1, and the tool states it.
3. **`mdpf_get_model_composition(firm, model_key)`**: firm-level, no account. It returns the as-implemented model holdings
   (ticker, target_weight, product_class, is_opal_etf) from `mdpf/feeds/model_composition/<firm>/`. Wave 3.
4. **Not served:** `partner_held_etf/49financial` (rolls a 2026-07-23 value forward) and `non_model_aua/49financial` (the
   superseded v0_9 method, about 69M USD off the served figure). G5 `etfs_get_partner_ownership` and
   `mdpf_get_aggregate_aua` answer those questions with current values. `etf_net_assets` gets no tool (G5 reads the
   upstream issuer silver).
5. **Wave B:** `mdpf_get_security_classification` against the canonical DynamoDB `etf-classifications`
   (`org/standards/MDPF_SECCLASS_CONTRACT.json`), with the G4 index as provenance; `as_of` history on
   `mdpf_get_aum_metrics` / `mdpf_get_account_distribution`, read from the dated per-firm gold
   (`opal-data-{49financial,inflection,cottonwood}/mdpf/<firm>/gold/`). That gold is OVERLAP on its latest date (G4 3.1).

**Coverage gap ruling (G4 3.1):** no G7. `opal-data-assets/portal/gold/mdpf/` and the per-firm `mdpf/<firm>/gold/`
are the producer side of what portal-v2 serves, and are equal on the latest date. They matter only as dated history,
which is item 5. The uncensused `taxsma_assets/` gold in `opal-data-49financial` and `opal-data-cottonwood` (14 keys
each) is client data. `4.0.0_SA_CRO~Z` contracts it as a G2 part, as the Tax SMA adapter's served form.

CONTRACTS-only; ENDPOINT unchanged. The census has landed 6 of 6 groups.

**G2e (Tax SMA assets gold, `parts/G2e_taxsma_assets_gold.md` @2a78786dda, msg 34122):** the table is
`mdpf/<firm>/gold/taxsma_assets/` in the per-firm buckets (49F 13 accounts, Cottonwood 2, 0 behind, 0 last-4 collisions).
It is the Tax SMA adapter's served form behind `client_get_holdings` / `client_get_profile` (Ruling 1). There is no separate
`client_get_taxsma_accounts` tool. The census totals 308 contracts.

### v3.4 addendum (2026-10-14 ~15:1xZ, 1.0.0_SA_CTO~Z) -- client data comes ONLY from the opal-data-assets vendor silver folders (Andrew-direct)

**Andrew-direct ~15:0xZ, verbatim in `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_150xZ_CLIENT_DATA_ONLY_OPAL_DATA_ASSETS_VENDOR_SILVER.md`:** "opal-data-bd is not a bucket we want to use for this at all, the only
client-data we want to be using explicitly at this time is the silver vendor folders in opal-data-assets".

**Contract change (supersedes the clauses named):**
1. Every `client_*` tool and its adapters read client data ONLY from `s3://opal-data-assets/<vendor>/<firm>/silver/`
   (blackdiamond, orion, eclipse, smartx, schwab, commonwealth, and the Tax SMA table censused there).
2. **Struck:** v3.1 Ruling 5's live read of `opal-data-bd/silver/` (the BD adapter reads `blackdiamond/<firm>/silver/`);
   CRO~Z G2f (opal-data-bd map) is superseded; v3.3 G4 item 2 (account-grain MDPF feed as an adapter of
   `client_get_allocation`) is struck -- that feed is not served; the G2e note (per-firm buckets' `taxsma_assets` gold)
   is struck -- not served.
3. **Freshness, stated, not fixed here:** 49F BD silver in `opal-data-assets` runs behind (converter OOM, row Z-S110;
   `49financial/silver_legacy` frozen 2026-08-25). The BD adapter answers from the newest partition it holds and states
   the lag in trading days. Repairing the converter is outside this project.
4. The G2 never-widen ask names `opal-data-assets` vendor silver prefixes only. No grant on `opal-data-bd`,
   `opal-data-mdpf/mdpf/feeds/` or the per-firm buckets is asked.
5. Not client data under this word, so unchanged: portal-v2 `platinum/mdpf/<scope>/` firm aggregates (existing mdpf
   tools) and `opal-data-etfs` partner ownership totals (G5).

CONTRACTS-side; ENDPOINT unchanged.

### v3.5 addendum (2026-10-14 ~16:4xZ, 1.0.0_SA_CTO~Z) -- vendor-silver producer defects ride this project as defect cells

On `2.0.0_SA_COO~O` msg 34150 (row Z-S117, citing Z-S111). FWD-22's client data is ONLY the `opal-data-assets` vendor silver
folders (v3.4). Their converters were built under OPAL_ASSETS, now `complete-as-superseded`, so no live project owns them.
The ruling:
- **A defect in a vendor-silver converter that keeps a FWD-22 client table from landing is cut by this project as a
  DEFECT CELL** (the D8 precedent: a defect item, never a re-open of OPAL_ASSETS). The cell is `<risk>WORLD</risk>`, the Lambda
  is changed through Terraform only (no `update-function-code`), with a ledger entry, and a re-drive of the missed objects
  follows.
- **Z-S117 (Eclipse):** admit `defaultTradingEngineId` to the eclipse schema, then re-drive the bronze objects from
  2026-10-10. Measured at ruling: `infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/mirror_schemas.py` DIFFERS from
  `data/assets/scripts/silver/mirror_schemas.py` (first at line 52), as does the orion copy, while the blackdiamond and etf
  copies are equal. The cell reads that divergence before it edits and names which copy the Lambda builds from.
- **Z-S110 (49F BD converter out of memory)** takes the same route once its cause is read.
- This is not a widening: the converter already writes these folders. The fix moves the folder's freshness, not who
  can read it.

CONTRACTS-side; ENDPOINT unchanged.

### v3.6 addendum (2026-10-14 ~18:5xZ, 1.0.0_SA_CTO~Z) -- 49F Black Diamond reads opal-data-bd (Andrew-direct); the G2 order

**Andrew-direct ~18:3xZ, verbatim in `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_183xZ_49F_BLACK_DIAMOND_FROM_OPAL_DATA_BD_AND_THE_TARGET_LAYOUT.md`:** "We can allow 49F Black Diamond pulls from opal-data-bd, you're right
that's fine." It amends v3.4 for 49F Black Diamond ONLY.

**Contract change:**
1. The 49F BD adapter of the `client_*` tools reads `s3://opal-data-bd/silver/<table>/YYYY-MM-DD.parquet`, per CRO~Z G2f
   (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/parts/G2f_bd_live_prefixes.md` @5e5d312ada: 8 tables, 49F only; schemas 4 equal, 3 live-subset, 0 differ). G2f is restored for this
   adapter. Increment vs snapshot is measured before any tool sums or spans dates.
2. The read goes through a role scoped to `opal-data-bd/silver/`, with its own never-widen ask (v3.2: never the global
   internal reader).
3. `assets` (80 trading days behind) and `transactions_enriched` (122 behind) answer with their lag stated and are never
   presented as current.
4. Every other client source stays the `opal-data-assets` vendor silver folders (v3.4 unchanged). `opal-data-mdpf`
   feeds and the per-firm buckets stay not served.

**The target layout is NOT this project's act.** 49F BD moves into `opal-data-assets/blackdiamond/` in LGIC_NAMING form,
and 49F's BD and Schwab gold land in `opal-data-49financial`. That is a pipeline migration (rule 30 / R19). When it lands,
the 49F BD adapter re-points to `opal-data-assets/blackdiamond/<49F>/silver/` in one cell, and the opal-data-bd read is
retired.

**G2 order (ruling to `2.0.0_SA_COO~O`, msg 34174 answered):**
1. Schwab (existing role; 49F's custodian data).
2. 49F Black Diamond (opal-data-bd).
3. Orion/Inflection (Eclipse after Z-S117).
4. BD Cottonwood.
5. SmartX (row filter).
6. Commonwealth.
Friday 2026-10-16 = G1, G3, G5 wave A, G6, and Schwab if it fits.

CONTRACTS-side; ENDPOINT unchanged.

### v3.7 addendum (2026-10-14 ~19:3xZ, 1.0.0_SA_CTO~Z) -- FWD-22 enrichment G5r: rival funds through the gateway (Andrew-direct, XB-eda5)

**Input.** Andrew-direct ~19:0xZ at the laptop (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_190xZ_RIVALFUNDS_INDEXED_INTO_OPALGATEWAY.md`, on CLOUD): "we should also have the rivalfunds indexed out and
available too". Order XB-20261014T185521Z-eda5 went to `4.0.0_SA_CRO~Z`, whose spec is `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5r_rivalfunds_spec.md` @e1b9937129.

**G5r enrichment list:**
1. The nine G5 rival tools stand (`etfs_get_peer_group`, `etfs_get_fund_holdings`, `etfs_who_holds`,
   `etfs_get_fund_trades`, `etfs_get_fund_flows`, `etfs_compare_peers`, `etfs_get_research_notes`,
   `etfs_get_security_reference`, `etfs_get_coverage`). Every one reads GOLD under `opal-data-etfs/rivalfunds/etfs/gold/`,
   newest part per date partition, never summing parts, and passes `claim` through on the inferred tables.
2. One new tool, `etfs_get_rival_page_status(page_day?)`, reads the platinum `manifest.json` (newest revision): what was
   PUBLISHED and whether it passed its checks. Its `latest_report` is shown beside the gold value, both labelled.
3. **Z-S124 binds:** a fund's latest report comes from `canonical_shape` only, never from `holdings_coverage` or the
   manifest. Both understate 9 funds today.
4. Security search by CUSIP/ISIN works here (unlike the harvest), within G5r section 2's fill rates.
5. Read class (Opal users), no firm fork: this is Opal fund research.
6. **One never-widen ask for all of G5:** the G5 wave-A ask also names `opal-data-etfs/rivalfunds/etfs/gold/*` and the
   platinum page prefix, so the rival tools need no second ask.
7. **Order:** after Friday's set (G1, G3, G5 wave A, G6, and Schwab if it fits), ahead of the remaining G2 vendors.
   Priority stays P4, site Z in the background.

CONTRACTS-side; ENDPOINT unchanged.

### v3.8 addendum (2026-10-14 ~20:3xZ, 1.0.0_SA_CTO~Z) -- the site Z harvest cycle runner without Seeking Alpha (Security Analysis gap G6) is a defect cell here

On `0.0.0_AB_MSTR~Z` msg 34214 (relay of the laptop CTO and `1.0.0_SA_CTO~DELL1`,
`CTO_RULING_DELL1_SECURITY_ANALYSIS_G1_G6_HOMES_20261014.md` @ce117ec6cb on box/dell1): G6 is site Z's.

**The one check, read:** the 2026-10-13T23:53Z stop was NOT on Andrew's word. It was AMGT_HARVST `HVST-bz-10`'s own stop and
re-registration under a task order (`fcfb0cec38`, `887a47f05e`). That order kept the existing publisher set
`bbg wsj barrons` on purpose: its adversary forbade changing the publishers. `sa` was already absent before it. Andrew's
standing word on Seeking Alpha is to keep it ("also seeking alpha will renew, we're keeping that",
`ANDREW_DIRECT_20260929_204xZ_OPEN_CALLS_ALL_FINE_SEEKING_ALPHA_RENEWS.md`). Live at ~20:3xZ: task "Opal Data Harvest -
Continuous Cycle" is Running, with `--publishers bbg wsj barrons --refresh-once`.

**Ruling.** AMGT_HARVST is PARKED (dell1's allocation). `seeking-alpha/harvest/silver/*` is a G1 table this project serves
(FWD-22). So v3.5's rule extends to it: a harvest producer defect on site Z that keeps a FWD-22 table from landing is a
DEFECT CELL cut here, WORLD, with a ledger entry. The cell, in order:
1. Read Seeking Alpha access first (row AMGT_HARVST-Z-W37-S4: HTTP 402, "renewal pending, at the account holder"). If it
   still refuses, stop and report. The renewal is Andrew's act, and no capture runs against a refusing account.
2. If access holds, stop the runner by its own STOP file at a cycle boundary (zero pairs lost, as bz-10 proved), then
   re-register through `install-cycle-schedule.ps1 -Publishers bbg,wsj,barrons,sa -Windowless -RefreshOnce`, with `-Plan` read
   first. State dir and runtime root are unchanged.
3. Place the trading-day trigger for the four SA tables that the CRO findings name
   (`org/tier1_exec/4.0.0_SA_CRO/deliverables/SECURITY_ANALYSIS_DAILY_PULLS_DEMQUE_DOSSIER_FINDINGS_20261014.md` lines 661-666).
No new vendor use: the capture resumes under the use already worded for the harvester.

CONTRACTS-side; ENDPOINT unchanged.
