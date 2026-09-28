```json
{
  "project": "NFRA_OPLGTW",
  "directive": "D9",
  "fabric": "site-z",
  "prd_version": "v1.1",
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
    "FWD-8"
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

The first release covers the five Schwab tools, hosted Claude connection, per-principal authorization, two masters and three silver datasets, protected filtered CSVs, support and safe withdrawal. Original bronze/Parquet download, source mutation, arbitrary SQL/code/URLs, cross-master aggregation, security-reference enrichment joins, managed Enterprise Auth, private tunnels, and a new portal are outside v1. Original-file support requires a future version and whole-object grant; its allowed-operation enum is disabled in this version.

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

## CONTRACTS

The enumeration authority is `org/standards/NFRA_OPLGTW_CONTRACT.json`, version 1.0; its four typed names (the two reader roles, the Gateway's assume policy and the access-state table) move to builder output as version 1.1 in the rename applies below, with the Terraform declarations and the application's references moved in the same orders, before any further consumer binds. Version 1.1 also adds `tool_operations`, a total map from each of the five tools to a member of `operations` or `null`, where `null` means carried by every active grant, never grantable and reading no data object; `operations` stays the grantable set, and both code copies of the mapping are tested equal to it. All tools, fields, states, error codes, limits and surface IDs are closed there as data. Its `activation=DESIGN_ONLY_NOT_A_GRANT` is intentional: implementations consume its contract, never treat the proposed profile as an authorization record. Unknown enum values and extra request properties fail closed. No counterpart PRD exists; all interfaces below have one owner in this project.

### C1 - identity, OAuth and migration

Use the existing Gateway authorization-server issuer and resource. Entra is the upstream identity provider, not an alternative MCP audience. Carry validated `tid` and `oid` in signed principal context; email is display/audit metadata only. Validate token signature, issuer, audience, expiry, authorized tenant, nonce/state, client, PKCE S256, redirect and requested resource at every applicable exchange. Never accept caller-supplied email, identity headers, role or tenant as the authorization identity. Authentication must not require Graph mail/file consent; retain delegated Graph acquisition only for tools that use it.

Register and exactly match `https://claude.ai/api/mcp/auth_callback`. Preserve existing Code loopback redirects only for registered clients, with RFC loopback port handling and no arbitrary hosted redirects. Require the issued client ID in authorization-code redemption; remove the current unregistered-loopback/optional-client behavior through an explicit reconnect migration. DCR is JSON; token exchange is form encoded. Metadata must advertise the same resource, issuer, endpoints, scope and S256 behavior actually enforced. Discovery, registration and ordinary token/auth responses have a 10-second budget; refresh has 30 seconds. Browser interaction time is excluded from server processing latency. Preserve Streamable HTTP negotiation, Bearer challenge, cancellation and relevant proxy headers. These protocol details are verified against [Claude authentication requirements](https://claude.com/docs/connectors/building/authentication).

Store client registration, authorization codes and refresh families durably in the Gateway's access-state DynamoDB table, named by the builder (`name("gateway", None, "access-state", "table")`, today `gateway-access-state-table`; never typed here). The table applied under the earlier typed name is renamed to the builder's name in its own order in the same root, before any further consumer binds: the new table is created, every record is copied with the item count equal on both sides and the operator-audit namespace verified item by item, the application's table reference and the Terraform declaration move together, and the old table is retained until the copy is proven and then removed in the same order's rollback window. Codes are single use; refresh tokens are cryptographically random, stored only as hashes, bound to immutable principal/client/resource/scope and family. A conditional DynamoDB transaction consumes the current generation and installs the next. Reuse revokes the family; a concurrent loser receives invalid_grant and cannot mint a second valid successor. No grace period that leaves a replay usable. Logout/revocation invalidates the family. Use 15-minute access tokens, 30-day absolute and 7-day idle refresh expiry; check logical expiry even if TTL deletion is late. Record expiry explicitly and scope reductions on refresh; never remint a broader configured scope. Public-client refresh rotation and replay detection follow [OAuth security best practice](https://www.rfc-editor.org/rfc/rfc9700.html).

Legacy refresh tokens cannot be safely upgraded without a new authenticated connection. Cutover rejects them with invalid_grant, preserves registered Code client callbacks, and tells existing users to reconnect once. Inventory active client registrations and test the migration before cutover. Persist client records so restarting a worker does not forget clients. A client registration expires after a 30-day idle lifetime, counted from the later of its registration and the last exchange that used it, unless it holds a live refresh family, which keeps it until that family ends. Its record carries an explicit logical expiry, which every exchange checks even if the table's TTL deletion is late; an expired client is refused with invalid_client and must register again. (L10 addendum R-5, 2026-09-28, on row W3-S5.) Failure of durable state fails new/refresh exchanges closed; it must not silently select an old stateless branch.

At cutover, every protected MCP and REST route rejects legacy access JWTs lacking the new token-version and immutable principal claims, even while their old exp is still valid. Persist the pending upstream authorization state with a short logical expiry, state/nonce and client/resource bindings; a restart between authorize and callback either resumes that exact bound transaction or returns an explicit restart-login error, never guesses identity. Access tokens carry a family identifier; every protected request checks family status and principal revocation with the current grant. Family logout/reuse revocation therefore prevents later use of previously issued access tokens as well as refresh. A2/A17 include legacy access replay, restart mid-login and revoked-family access replay.

A missing or invalid MCP credential gets 401 with the advertised resource challenge. A valid token lacking an OAuth scope gets the specified 403 insufficient_scope response, not the current conversion back to 401. A denied data entitlement is a terminal tool authorization error, not an OAuth escalation or a login loop. The download browser uses a separate Gateway-owned OIDC callback, secure HttpOnly SameSite cookies, anti-CSRF state/nonce and exact issuer/audience/signature validation. It establishes the same tid/oid principal independently. Do not infer that match from the existing ALB email-only helper. Browser OIDC endpoints bypass ALB login only at those explicit paths; existing default browser authentication and unrelated routes remain intact.

### C2 - policy and complete access enforcement

DynamoDB stores durable `principal_profile` and versioned `data_entitlement` records. Key grants by tid/oid, not email. The one email-keyed record is denial-only: a principal made restricted also gets an `email_deny` record (key `POLICY#EMAILDENY#<sha256hex("og-email-deny/v1|" + email.strip().lower())>`, one per email alias; routes and the operator writer MUST compute the same function) in the same operator transaction. The browser routes that identify a caller only by the ALB email (`/login`, the `/sprint` paths, the legacy `/callback` and its consent redemption) refuse a denied email before any read or credential exchange; an unreadable store denies them. The record only ever adds denial, is kept on revoke, and is never used to grant. Status is pending, active or revoked; use optimistic revision checks for operator updates. A revoked restricted profile is a tombstone, never deletion that reactivates the legacy unlisted-user path. Unknown users see no Schwab tools and direct Schwab calls fail. A newly added tool is denied until classified. Preserve existing users' current tool access through explicit regression, without granting new data tools by default.

Every request strongly reads the current profile/grant; an unavailable or malformed store denies restricted access. Scope includes master, dataset, account IDs, dates, columns and operations separately. Apply it before filtering, projection, grouping, totals, cache lookup and export. Accounts are raw IDs internally only. Expose a versioned, keyed HMAC account_ref over master plus account ID; keep its key in the existing approved secret mechanism, and never log raw IDs. The same numeric account ID in two masters yields different aliases. An alias is usable only after resolution against the current authorized account set.

Enforce discovery and dispatch in the integration registry and native tool path. Inventory all 27 source-declared server routes and every non-MCP entry point, including /teams/poll and /query/v0. The new restricted profile is denied unrelated data tools and direct REST shortcuts before any credential fetch or read. Domain-suffix internality cannot bypass this policy. This is necessary to make a work-email identity a limited reader. Existing admin/Graph/portal routes retain their existing policy for other users, subject to regression coverage.

Entitlement updates are operator-only, through an audited repository/release-operated administration command using an authorized operator AWS identity. Validate a candidate, show the exact scope diff, then conditionally activate it against the old revision. Store approver, timestamp and source authorization reference. Reject empty/unknown identity, unapproved accounts/fields or malformed dates. Provide no MCP tool to mutate grants. All cache/cursor/ticket keys bind principal, revision, master, dataset, dates, projection and source versions. Before response emission or download start, re-read the revision; discard stale work. Already delivered bytes cannot be recalled.

### C3 - sources, closure and date semantics

Source bucket is `opal-data-assets`; masters are 08242234 SmartX and 08335338 BlackDiamond. Only their `silver/dim_position/`, `silver/dim_balance/` and `silver/dim_asset/` prefixes are data-readable. A date is a Schwab business-date label, not object LastModified or request time. For each master/dataset the rolling window includes the latest qualified complete business date and the previous 29 calendar days; do not silently fill missing dates from another master or dataset. The available dates and latest qualified date are returned explicitly. A fixed-date grant is an enumerated date set. Staleness is reported as days since the qualified business date and source observation time, without pretending a missing business-calendar feed defines a late arrival.

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

