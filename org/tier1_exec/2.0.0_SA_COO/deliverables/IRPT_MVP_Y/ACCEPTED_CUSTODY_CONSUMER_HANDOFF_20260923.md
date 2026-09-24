# Accepted custody consumer handoff

Current local source `10627906f24aa42db4c08fd66105599f35bf7819`, on Y base `819c9e3990`.
Ruling `999998e448`; paired P interface `75bbe9cc2d`, implemented reader at
`8845b7ef23cabfe9c73a3f8109f0c1c2c829e3af`. P replacement `e36b007fa1a85414e8453608dc2803b8c947c290` has identical
`accepted_custody.py` and `custody_binding.py` blobs. No method mismatch found.

## Installation

`custody_submission.build_accepted_custody_entry(reader, **existing_ports)`
binds the supplied reader's `authorize_snapshot(principal, owner)` and
`AcceptedCustodyNormalizer(reader).load_normalized(browser, principal, owner)`
to the existing guarded custody factory. Do not pass competing source callbacks.
No global entry or production source default is installed.

The new flat package member is `intake/custody_portfolio.py` ->
`custody_portfolio.py`. P owns final package assembly and must include it alongside
the changed `portfolio.py` and `custody_submission.py`. Exact five changed files
and hashes are in `ACCEPTED_CUSTODY_CONSUMER_EVIDENCE_20260923.json`.

## Behavior and evidence

Every original is checked before aggregation: exact text dollars and original
recipe bounds, native quantity sign, side, cash/security consistency, sourced
accrual equation, duplicate facts, original/position correspondence, complete
account census and independent same-date USD reconciliation. Unknown or
unsupported originals refuse the whole portfolio. Relationship duplicates remain
in retained evidence but contribute only once per economic position; subsequent
canonical-security consolidation uses the existing freezer.

The retained source embeds the complete selected-only accepted contract and
projects exact snapshot revision, selection fingerprint, date, accounts and
snapshot identity. `verify_frozen_portfolio` reconstructs this branch from its
retained evidence and compares the entire normalized document, so rehashing
altered holdings, detached provenance or removed evidence does not validate it.
Historical inputs without this branch retain their existing behavior. Current
authorization still belongs to the guarded reader/factory/repository, not hashes.

Separate runs passed **306 tests and 50 subtests**: generation 212/32 and intake
94/18. The real P reader/store feeds the actual guarded Y factory through
retention, retry and revoked-capability refusal; exact normalized bytes are
asserted in the synthetic object store. The final added stored-byte assertion
passed both profile variants. All economics/publication/storage transports are
synthetic. No actual upstream economic capability is proved. P's actual M replay
115-test report is separate evidence, not included in Y's counts.

One combined collection attempt had 292 passing tests and 13 missing-world-fixture
setup errors. Separate suite invocations resolved collection. The first commit
attempt failed E701/E702 test formatting; fixes were AST-identical and the final
canonical five-file commit gates passed. No overrides used.

## Remaining boundary

Original/position lists are capped at 10000. The source transport cap is 1100
characters, 1000 coefficient digits and absolute exponent 1000; original recipe
limits remain 28 digits and exponent 18. This branch requires same-day dates,
explicit accrual arithmetic and equal native/resolved quantity where SHARES is
present. It performs no conversion or invented zero. Those are conservative
consumer refusals, not new upstream policies or source facts.

P must compose this exact source into its integrated candidate/package for CTO
direct review. Source interpretation and economic evidence validation still have
no production defaults. No cloud action, producer invocation, vendor call,
deployment, runtime attachment or full-product completion is claimed.
