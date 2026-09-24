# Accepted custody source handoff to P and Y

Seat `2.0.0_SA_COO~M`, 2026-09-23. **archetype:** TRACE
Authority: IRPT completion CONTRACT; Y messages 151157/151546 and P 151424.
This is the requested source/interface fact handoff, not an implementation or
ownership handback. P retains shared scope, integration and packaging.

## Finding

**The concrete production source adapter is missing in the inspected sources.**
Accepted publication retrieval and current retained-selection checks exist.
Neither is an implementation of the two required callbacks:
`authorize_snapshot(principal, owner)` and
`load_normalized(browser, principal, owner)`. Y's exact factory deliberately
injects both. No accepted three-firm security-level custody portfolio contract
can honestly be inferred from the existing holdings display tree.

Source pins:

- Workspace `a28305aefcf62589f0c1be3a076e73f5c64d5629`.
- Y factory `819c9e399086cffb2876a21fbc2cee01724b0bd7` in
  `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922`.
- Companion JSON records both pins, nine exact paths per pin, blob IDs, SHA-256
  and function signatures/lines. AST census of the committed non-test Python
  subtree `infra/aws/lambda/investor-reporting/` found zero definitions with the
  two callback names in 103 workspace files and 105 Y files. This bounded census
  does not rule out differently named adapters elsewhere; the actual candidate
  calls mandatory injected ports, not a located concrete adapter.
- Publication, snapshot reader, producer, published schema and selection source
  are byte-identical between those pins. Y's holdings Entry has P's request-local
  Opal roster repair; Y's portfolio freezer additionally admits the exact Opal
  custody owner. Those differing files must not be replaced by workspace copies.

## Existing reusable APIs and their limits

All paths below are relative to `infra/aws/lambda/investor-reporting/` except
the explicitly named Gold builder and published schema.

| Existing API | What it proves | What it does not prove |
|---|---|---|
| `holdings/publication.py:HoldingsPublication.load(*, as_of=None, account_ids=None)` | Reads the current index's date entry; exact manifest/version/hash/length and canonical firm locations; v1 document digest or v2 header/partition identities; full inventory metadata and selected-only part reads | Caller identity, selection ownership, an externally supplied snapshot ID, independent economic truth, or complete usable security rows |
| `holdings/snapshot.py:load_snapshot(firm_id, prefix=DEFAULT_PREFIX, as_of=None, s3_client=None, *, account_ids=None)` | Returns publication document with private `_accepted_publication` manifest; appends an `irpt-accepted-holdings` revision row | No `snapshot_id` argument, no current-owner authorization, no frozen normalized portfolio |
| `holdings/entry.py:_current_selection` and `holdings_snapshot` at Y pin | Fresh retained selection/current grants before and after read, firm binding, selected projection, reconciliation and clocks; request-local `ctx.opal_principal_ids` | No comparison of browser snapshot ID to publication revision; no security normalization |
| `_scope/selection.py:resolve_selection` | Resolves `sel_<64hex>` server record, current directory/grants, exact membership and directory revision; selected fingerprint is distinct from permitted fingerprint | A selection reference is not a snapshot identifier or publication authorization |
| `_scope/custody.py:CustodyAccess.current` at Y pin | Rebuilds full custody owner and selection, invokes snapshot callback, then rechecks current owner; includes home firm distinct from tenant | Mandatory snapshot callback remains an external port; constructor accepts only a nonblank snapshot string, not a defined publication-ID mapping |
| `intake/portfolio.py:freeze_parsed_portfolio` at Y pin | Pure normalization and frozen content identity from trusted parsed rows, resolution and optional dated prices; binds exact custody owner/source | Does not load holdings, derive authoritative security rows, authorize storage, or implement either source callback |
| `ycharts/generate/custody_submission.py:CustodySubmissionFactory` at Y pin | Verifies frozen hash, full owner, CUSTODY lane, exact snapshot/account IDs and current access before retention | Synthetic supplied source callbacks do not establish an actual producer binding |

Publication `revision` is SHA-256 of canonical bytes of the **whole original
snapshot**. It is distinct from the manifest object's own hash/version and the
source-receipt digest. V2 selected reconstruction is not the whole original
document; `load_snapshot` also adds metadata. Do not recompute either returned
slice's hash and call it the original publication revision. `as_of` selects the
current index's revision for a date; a same-day correction can change it. The
existing loader is not an API for reopening an arbitrary superseded revision.

## Actual source field contract today

Published schema:
`docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` at both pins.

| Field | Existing meaning and consumer constraint |
|---|---|
| `scope.account_ids` / ACCOUNT `node_id` | Canonical account population. Walk parent edges to account root; do not infer ownership from string prefixes. Publication header can retain full-firm census during selected part reads; use guarded projection before comparing selected rows. |
| `node_kind`, `basis` | Display hierarchy includes ACCOUNT, sleeves, models, SECURITY and unresolved nodes. TARGET/ASSIGNED are not actual security holdings; summing parent and child amounts double-counts money. A terminal node is not necessarily a security. |
| `amount.value`, `amount.units` | Schema allows USD, SHARES, WEIGHT_DECIMAL; current builder `_node` emits rounded numeric amounts and inspected builders emit USD. A USD amount is not a share count. No dedicated quantity, price, price date or price revision property exists; node additional properties are forbidden. |
| `security_id.namespace/value` | Optional namespaced identifier; namespace enum TICKER/CUSIP/ISIN/CASH/VENDOR/UNKNOWN. Schema permits an empty string and does not establish a resolved canonical security or vendor identity. Actual resolution must refuse unavailable/ambiguous identity. |
| `clocks.custody_as_of`, `overlay_as_of`, `source_as_of` | Preserve source clocks separately at header and nodes. Different custody/overlay dates must not be spliced into one valuation. Equal dates are possible; `clocks_are_distinct` checks separately carried values, not an inequality requirement. |
| `source_set_revision[]` | Per-source string revisions plus completion dates. General schema does not require every revision to be a content hash. `irpt-accepted-holdings` identifies manifest revision; `irpt-source-objects`, when supplied, binds source receipts separately. |
| `valuation_facts[]` | Optional allocation facts with individual clock/scope/revision. Not replacement custody securities, account totals, prices or permission to add allocation values to custody totals. |

Builder `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`:

- `build_49f`: SECURITY nodes come from SmartX allocation positions; IDs are
  position ordinals under allocation nodes, and source security identity uses
  ticker or UNKNOWN symbol ID. Missing market value currently falls through to
  zero in this branch. Roots are derived from allocation valuation, not a proved
  independent complete custody position census. Prior exact source evidence
  retains the custody/overlay date and population mismatch. These nodes cannot
  be relabeled as an accepted complete custody source for Y.
- `build_inf`: account values and managed/excluded/model/unresolved hierarchy;
  no SECURITY node construction in this function. No account security portfolio
  can be reconstructed from an Eclipse model assignment or shared portfolio total.
- `build_cot`: actual account totals from holdings plus TARGET model expansion;
  no SECURITY node construction in this function. Model target weights cannot
  supply actual securities, and unresolved/unknown value cannot become zero.

These are pinned static source findings, not claims about a newly fetched live
publication. No source object or cloud API was read for this handoff.

## Exact normalization boundary already present in Y

`freeze_parsed_portfolio(parsed, owner, source, resolve_security, *,
declared_currency=None, prices=None, price_date=None, reference_notional=None)`
expects real parsed-row provenance, reconciliation and correction status.
For CUSTODY, source requires nonempty `source_revision`,
`selected_set_fingerprint`, `as_of` and unique account IDs. The Y custody branch
also requires exact `source.snapshot_id == owner.snapshot_id`, full account
equality and `custody-owner-v1` OPAL_GLOBAL identity with null advisor. These
checks do not establish where the values came from.

Canonical resolver output is `security_key`, `canonical_identifier`,
`canonical_identifier_namespace` (TICKER/CUSIP/CASH), and
`resolution_revision`. CASH is explicitly `$:CASH`. The alternative historical
vendor branch requires an already established `P:`, `S:`, `M:` or `$:CASH`
identity. Do not prefix a ticker to manufacture one; UNKNOWN/VENDOR/ISIN input
needs an admitted resolver rather than coercion. Conflicting resolutions refuse.

USD rows preserve supplied dollars and need no invented price. SHARES require a
matching security-key/ID USD quote, exact `price_date`, positive price and source
revision. No such quote loader is implemented by the holdings reader. Weights
require explicit reference notional and are not actual custody AUM.

**Signed-value incompatibility remains:** `_number` and `_row_amount` reject
negative and zero amounts at both inspected pins. A correct signed custody
portfolio cannot be forced through this freezer by taking absolute values,
dropping short/cash rows or netting away their provenance. Y owns any explicit
normalization-policy change; producer and downstream recipe acceptance must be
paired. This finding is source-level, not a new tested failure claim.

## Missing adapter requirements and refusal rules

The following are requirements for the missing binding, not newly installed APIs:

1. P/Y must bind snapshot ID to a server-owned accepted manifest locator/revision
   for the concrete tenant and selected account set. Publication revision is a
   possible binding input; no current wire contract says that any arbitrary
   snapshot string equals it. Never infer equivalence or let the browser choose
   a bucket, key, version, rows or security mapping.
2. `authorize_snapshot` must check exact current owner/selection/account members,
   tenant, admitted snapshot identity, manifest metadata and current acceptance.
   Current source drift cannot silently advance an existing request. Rechecks
   must surround normalization/retention. Current authorization and retained
   report reopening remain distinct from choosing today's latest snapshot.
3. The producer must supply unique actual custody position rows, known-value
   coverage and explicit cash/signed semantics, full selected-account census,
   source object receipts and dated compatible security mapping. Reconcile every
   account and selected total against independently enumerated custody amounts,
   not an internally consistent model tree. Missing selected account, unknown
   value, duplicate position, incomplete leaf inventory, target-only membership,
   ambiguous security, incompatible currency/date or unaccepted economics refuses
   the whole normalization; no partial success or inferred remainder.
4. Freeze exact owner, account-set reference/fingerprint, snapshot identity,
   publication revision and source receipts/clocks with immutable normalized
   bytes. Retain original row identity, units and corrections. Security/price
   revisions must describe the actual resolver/quote source, not the snapshot's
   hash reused as unrelated evidence. A changed accepted source makes a new input
   revision; retries use the retained accepted input under current access checks.
5. Proposed controls: wrong tenant/actor/accounts/snapshot; revoked grants or
   changed selection; changed current manifest during normalization; malformed
   unselected inventory reference; missing security/price; incompatible clocks;
   target-only tree; cash/short/zero handling; duplicate parent-child counting;
   complete positive per-account reconciliation and retained-input retry. Actual
   producer and consumer integration must exercise these, not permissive stubs.

Recommendation: keep both production callbacks unconfigured/fail-closed until
the adapter and an accepted security-level custody source exist. P integrates
authorization/package wiring, Y implements its owned normalization consumer,
and M/DS source work needs the exact producer/cause scope already required by
CTO's inventory acceptance. Return this concrete missing seam to CTO instead of
silently substituting allocation or target data. No new source repair began here.

## Verification and compiler limits

`comp-which` preceded scoped inspection. Bare `comp-find HoldingsPublication`
completed with 210 hits across 195,603 scanned files, 8 unreadable; first-page
results include runtime copies, so it is not a complete production census.
The committed AST census above supplies the explicit narrower denominator.
Bare `comp-pipescript io holdings_snapshot --pipeline bd` returned script not
found; its suggested B_01 was not substituted. `holdings/projector.py` is absent;
the actual projection lives in `holdings/snapshot.py:project` and was read there.
Exact Git source/schema reads and cross-pin byte comparisons completed. No
production module, tests, producer, SDK/cloud read or write was invoked.
