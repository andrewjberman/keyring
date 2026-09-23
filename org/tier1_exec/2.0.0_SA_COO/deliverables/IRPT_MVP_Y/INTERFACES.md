# IRPT Y -- current interfaces

Owner `2.0.0_SA_COO~Y`. Contract v1.3. Current Y source `85af5eb95d72051c363727229981c4dc1a35cad9`.
P reports prior custody source `10627906f2` integrated at `411256e41c` and packaged at `e3ad48ca23`.
This is the current schema/consumer record; historical proposals and prior
examples are retained unchanged in `INTERFACES_HISTORY.md`.

## Controlling access requirement

Ruling `5ad99c7d30` supersedes Opal custody-only, owner-only and mandatory-single-firm
permission ceilings. Verified Opal actors retain all IRPT functions across firms.
Y consumed P's verified viewer/prospect interface `9a3ec2a11f`; exact new read,
upload, placement and Entry ports are in `OPAL_ACCESS_HANDOFF_20260923.md`.
Current source supports the real viewer separately from retained owner and
explicit `data_firm` lookups. P's shared Entry and cross-firm repository wiring
remain pending. Preserve real actor and each input/report firm/account/source
attribution. No browser field grants access; offline tests do not prove live access.

## Versioned contracts and owners

| Interface | Current definition | Owner |
|---|---|---|
| Frozen normalized input | `irpt-normalized-portfolio.v1`, `intake/portfolio.py` at the Y source pin above | Y |
| Accepted custody input | `accepted-custody-input-v1`, P `75bbe9cc2d` output preserved by concrete reader `e36b007fa1` | P reader; M publication/economic source; Y consumer |
| Custody owner | `custody-owner-v1`, exact actor/home/report firm, account set, revisions and snapshot | P/M current scope authority |
| Public submission/composition/status/report wires | Canonical `docs/contracts/investor-reporting/v1/` schemas in P's integrated candidate; Y adds no public fields | P shared schemas, Y generation semantics |
| Retained report/artifact and export interfaces | P's current repository/package; no alternative Y store | P |

## S3 normalized schema and private custody projection

`freeze_parsed_portfolio(parsed, owner, source, resolve_security, *,
declared_currency=None, prices=None, price_date=None, reference_notional=None)`
returns `{input_id, content_sha256, document}`. The identity is `portfolio_` plus
SHA256 of sorted compact UTF-8 canonical document bytes. The document preserves
owner/source, parser and currency evidence, original contribution rows, findings,
explicit skips, reconciliation, valuation basis and consolidated dollar holdings.
Canonical-security holdings carry `security_key`, `canonical_identifier`,
`canonical_identifier_namespace`, `resolution_revision` and decimal-text dollars.
Shares require dated compatible prices; weight inputs need the declared notional
basis. No fabricated vendor identity or client AUM.

The private custody branch uses `freeze_accepted_custody(accepted, owner)`.
The accepted result has exactly `schema_version`, `owner`, `snapshot_id`,
`snapshot_revision`, `binding_revision`, `selected_account_set_fingerprint`,
`actual_custody`, `original_rows`. The complete nested contract is the paired
P reader specification at `e36b007fa1` and executable closed-field consumer
`intake/custody_portfolio.py` at the Y pin; this record does not fork that schema.

`document.source` maps CUSTODY lane; original snapshot digest to source_revision;
verified selected fingerprint to selected_set_fingerprint; custody date to as_of;
exact sorted owner accounts and snapshot; and a full deep copy of accepted input
to accepted_custody. Every original must pass eligibility/correspondence before
one money contribution per economic position. Security consolidation happens
only afterward. The existing positive-only recipe bounds remain in force.
`verify_frozen_portfolio` reconstructs this branch from retained evidence and
compares the complete document; current authorization is separately mandatory.

## Factory and replay call signatures

`AcceptedCustodyReader.read(principal, owner)` and
`authorize_snapshot(principal, owner)` are P-owned installed server ports.
`AcceptedCustodyNormalizer(reader).load_normalized(browser, principal, owner)`
provides Y's existing normalized loader. `build_accepted_custody_entry(reader,
**existing_ports)` binds those ports to the guarded factory; competing callbacks
refuse. It neither creates a reader nor installs a module-global entry.

S4 acceptance precedes dispatch; retries use retained input/configuration and
current authority. `FrozenCompositionWorker` consumes retained composition and
normalized artifacts under the existing request/retention guards. `prepare_normalized_upload`
uses canonical identifiers and exact dollar text without source refresh. Report
sections and job status remain separate responses under P's canonical schemas.
The new package member is flat `custody_portfolio.py`; packaging remains P-owned.

## One paired example (synthetic, executable)

The fixture `intake/tests/test_custody_portfolio.py::accepted` at `10627906f24aa42db4c08fd66105599f35bf7819`
contains two equal relationship originals, each market value `"100.00"`, with
distinct physical row coordinates, one economic position, complete census and
an independent `"100.00"` account total. With synthetic admitted security/economic
evidence, the actual P reader feeds Y's consumer: both originals remain inside
source.accepted_custody, one contribution is emitted, and holdings.total_dollars
is `"100.00"`, never `"200.00"`. Its exact snapshot revision, binding revision and
verified selected fingerprint survive retention. Changing an original to zero,
negative value, SHORT or negative native quantity refuses before aggregation.

Executable paired factory example:
`ycharts/generate/tests/test_custody_retained.py::test_p_reader_consumer_factory_retention_retry_and_revocation`
at the same pin. `IRPT_ACCEPTED_READER_TEST_ROOT` enables the exact pinned P reader
extraction described in `ACCEPTED_CUSTODY_CONSUMER_EVIDENCE_20260923.json`.
This is offline consumer evidence, not a real economic-source or live-thread claim.
