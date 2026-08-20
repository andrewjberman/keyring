# /drive — 2.0.0_SA_COO~Z, D-family scoped loop, 2026-08-20T20:3xZ (day tick 24)

**archetype:** COORDINATE

**A P0 in my own decomposition, caught before a line was built.** CVO~Z timed a pre-cut schema read
(2817 @3c29c35122) deliberately ahead of the W-lane builds; it landed one tick after TAC-2' closed
and one tick before AE~Z reaches W-A.

## The P0 — and it was mine

W-C's READ-OWN, as I wrote it, specified **only the ROW filter**. But `get_ticket`/`list_tickets`
return **UNPROJECTED WHOLE ROWS** — so the day `client-human` joins LIST/GET, a client fetching
*their own* ticket also receives `events[]` (the full internal audit trail: internal actor emails,
actions, free-text notes), `routing{}`, and the internal `resolution` close note.

**ROW-SCOPED IS NOT FIELD-SCOPED — two controls, and my cut named one.** Fixed @0968e3833f: a
server-side client **projection allowlist at the response boundary** (never the frontend — a UI
that does not render a field still shipped it over the wire), derived from Andrew's own C2/C3/C4
enumeration so it is faithful implementation rather than a narrowing; plus **WC-2b**, which makes
the mutants symmetric — a client response must provably **LACK** those fields **on a row where they
are populated**, as positively as it asserts it HAS the claimer identity.

*The general shape, worth carrying: a filter that selects the right ROWS says nothing about which
FIELDS ride along, and "the UI doesn't show it" is not a control.*

## Disposition of the rest — folded where it belongs, routed where it is not mine

| finding | disposition |
|---|---|
| P1-1 no requester-keyed GSI (client list would ride a Limit-bounded scan → a **client-facing completeness claim**) | → **W-A**, the table touch, per CVO's own sequencing; W-C's new WC-2c obligates a printed bound if the index is declined |
| P1-2 reopen/timing **grain collision** (`time_to_resolve_s` silently means LAST CYCLE while `reopened_count` says N) | → **ROUTED to CTO~Z, not ruled.** Andrew's day-one fields stay — I do not drop a sovereign field on a review finding; W-A carries the requirement that coherence is resolved **before** the Rule-24 record is written |
| P1-3 MATRIX has **no scope channel** — client READ-OWN is the estate's FIRST scoped grant | → **W-C** design-time resolution (Rule 22a's `(action)` vs `(action,resource)` one layer up) |
| P1-4 **single terminal state** (force-completed rejects become indistinguishable from real resolutions; `status` is the GSI hash key) | → **CARDED to CTO~Z**: a Rule-24 schema-enumeration act on a **client-visible** axis. Recommendation given (settle the set before W-D ships the summary); may be Andrew's word, his call |
| P2 `resolution` vs `resolution_summary` | → **W-D**: Rule-24 filing names which is internal vs client-visible; deny pairs assert the internal note never reaches a client |
| UU-1 `client_updates[]` growth vs the 400KB cap | → **W-A**: per-entry + per-ticket caps make the "designed-not-built" spill **unnecessary rather than deferred** — build-ladder rung 1, not rung 7 |
| UU-2 `_sod_block` forbids the requester acting on their own ticket — who is exactly the client-update author | → **W-A**: carve-out decided at design time, and **proven scoped** (can append; still cannot do anything else) |

New criteria minted: **WA-9**, **WC-2b**, **WC-2c**; id sets updated in both `<proof_of_spec>` blocks.

**One cross-schema flag raised back:** `WITHDRAWN` was adopted as a PROPOSED value in BG's
thread-memory contract this same hour (an exchange the **asker** ended); P1-4 names a
withdrawn-class **ticket** ending. Same word, two schemas, two grains — **one Rule-24 filing does
not cover the other**, and adopting one does not commit the other.

**CVO~Z's plane discipline carried into my record:** canonical tree @1fd9ef2750 + the TF, explicitly
NOT the deployed package, tree knowingly ahead of the laptop apply; and the 08-12 tenant-authz
finding flagged premises-superseded-IN-TREE so its severity read is not cited as current.

Dispatches: 2 (CVO~Z full disposition/RAVC close · CTO~Z + AE~Z amendment notice with the two
decision cards, one act, 2 DELIVERED / 0 QUEUED / 0 REFUSED). Gate: **PASS** — findings folded into
build-blocking criteria the same tick they arrived; nothing held, nothing deferred to "later".

## Compiler Tools
None new this tick: the work was reading a peer's grounded review and amending my own TOs. CVO~Z's
read carried its own plane declaration and citations, which is what made same-tick action safe
without re-deriving it.
