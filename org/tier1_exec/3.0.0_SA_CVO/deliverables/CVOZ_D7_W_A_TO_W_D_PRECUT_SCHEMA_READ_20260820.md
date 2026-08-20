# CVO~Z pre-cut read -- the Ticket Lifecycle v2 field set + the W-C read widening
**Date:** 2026-08-20 ~2045Z | **Reader:** 3.0.0_SA_CVO~Z (lane 4 of the spawn frame: "the Ticket
Lifecycle v2 record @942d4d885c as COO~Z decomposes W-A..W-D")
**Read against:** the v2 record @942d4d885c + CTO~Z 2776's DAY-ONE field set.
**Timing is the point:** the v2 record says "Rule-24 record on the field schema rides W-A" --
so the schema lands WITH its own test rather than before it. Andrew's word on this cut is
*"don't want to have to be retroactively adding stuff"*; a schema read is cheapest BEFORE
the TO is written. Findings, not holds -- nothing here blocks dep-2/dep-3.

## PLANE (stated first, because every claim below depends on it)
I read the **canonical repo tree** -- `infra/aws/lambda/ticket_center/lambda_function.py`
**@1fd9ef2750** and `infra/aws/terraform/ticket-center/main.tf`. That is the correct plane
for a question about what W-A..W-D must ADD. **I did not read the deployed package and claim
nothing about running bytes** (Rule 22a CODE layer) -- and note the tree is knowingly AHEAD
of the applied Lambda: 1fd9ef2750's own message records the laptop applying
**@4bede18189 (ticket-center-v1.1.0)** BEFORE that commit, so it rides the next apply touch.

**Correction carried in passing:** `ctoZ_SECURITY_FINDING_20260812_TICKET_API_MISSING_TENANT_AUTHORIZATION.md`
reads "caller identity is STAMPED, never CHECKED" and "not in this repo (0 hits)". **In the
tree today both halves are superseded:** the handler IS in-repo and carries a deny-by-default
`MATRIX` (:authorize), `_sod_block` segregation-of-duties, and `tests/test_authz_matrix.py`.
Whether those bytes are APPLIED is the plane I did not read. Flagged so nobody cites the
08-12 severity read as current.

## Ground truth measured this read (source-confirmed, @1fd9ef2750)
| Fact | Evidence |
|---|---|
| status enum = exactly THREE values | `VALID_STATUSES = ("open","in_progress","completed")` :62; literal frequency open=4 / in_progress=4 / completed=6, no other value present |
| NO reopen path exists | case-insensitive "reopen" count = **0** in the handler |
| responses return WHOLE ROWS | `get_ticket` -> `{"ticket": r["Item"]}`; `list_tickets` -> `{"tickets": items}` -- **no field projection anywhere** |
| ONE GSI, keyed on status | `status-index`, hash `status`, range `created_at`, `projection_type = ALL` (main.tf:65-69); pk `ticket_id`. **No requester-keyed index** |
| authorization is action-only | `MATRIX = {action -> frozenset(principal_class)}`; `authorize()` returns `(allowed, pc)` -- no scope channel |
| `resolution` already deployed | written at complete from `body.get("resolution")`, 2000 chars (:358-363) -- the INTERNAL close note |

---

## P0 -- W-C's READ-OWN is specified as ROW scope; the row is returned UNPROJECTED, so it also widens FIELD scope
The v2 record scopes C2 correctly at the row grain: *"list/get scoped to rows where the
requester matches the session identity -- server-side filter, never a client parameter."*
**That control is necessary and insufficient, because the handler returns the entire item.**
On the day CLIENT is added to `LIST`/`GET`, a client fetching **their own** ticket receives:
`events[]` (the full internal audit trail -- every internal actor's email, action, from/to
and free-text notes), `routing{primary,secondary,visibility}` (internal team assignment),
`resolution` (the internal close note), `created_by`, plus everything W-A adds
(`time_to_*`, `completed_by{}`, internal `category`/`tags[]`, `priority`).
**Row-scoped is not field-scoped -- two different controls, and only one is named in the
ruling.** Andrew's own C2/C3/C4 word enumerates what the client sees: their ticket in a
tab, the claimer's **name and email**, and the **AI summary**. Everything else is internal
by his own framing.
**Remedy direction (owner's):** W-C carries an explicit **client projection** -- an allowlist
of client-visible fields applied at the response boundary, not a denylist, and not left to
the frontend (a UI that "doesn't render" a field still shipped it over the wire). The
D7F-4-class mutant set extends: assert a client response **lacks** `events`/`routing`/
`resolution` as positively as it asserts it **has** the claimer identity.

## P1 -- a client "My Requests" completeness claim cannot be served by the current key schema
There is no requester-keyed index; the only GSI is `status-index`. So a requester filter
must ride either `_table.scan(Limit=limit)` or a `status-index` query with `Limit`, then an
**in-memory** filter -- the shape `list_tickets` already uses for `assignee`/`ticket_type`
(:275-279). **That is the estate's own truncated-page class** (CLAUDE.md: a filtered query
over a truncated page is indistinguishable from a real absence), and W-C changes what it
costs: an internal convenience filter becomes a **client-facing completeness claim**. A
client who filed 12 tickets can be shown 8, with nothing in the response saying so.
**Remedy direction:** a requester-keyed GSI (hash on the requester identity, range
`created_at`) so "my requests" is a KEY QUERY with a real denominator -- decided at W-A
(the table touch) rather than discovered at W-C. If it is deferred, the view must state its
own bound rather than imply completeness.

## P1 -- `reopened_count`/`reopened_at[]` are ruled in with NO writer, and they collide in grain with the timing fields
Two distinct defects in one field pair:
1. **No writer exists.** There is no reopen action in `MATRIX` and no reopen handler (0
   occurrences). A REOPEN action is a **matrix widening** -- its own action row, its own SoD
   question (may the requester reopen their own ticket? `_sod_block` currently forbids the
   requester acting on their own ticket, which would forbid the natural reopener), and its
   own Rule-24 filing. Shipping the fields without the action is the alarm-shaped half.
2. **Grain collision, Rule 24(ii).** `reopened_count` is a **ticket-lifetime aggregate**;
   `claimed_at`, `completed_at`, `time_to_claim_s`, `time_to_resolve_s`, `first_response_at`
   are **single-valued per row** and the transition handlers `SET` them unconditionally. On
   reopen -> reclaim -> recomplete they are **overwritten**, so `time_to_resolve_s` on a
   reopened ticket silently means *the last cycle*, while `reopened_count` says there were
   N. A metric that reads perfectly and means something other than its name is the LD-0012
   naming-vs-semantic class, and it lands in the analytics Andrew asked to be native.
   **Remedy direction:** either timings become per-cycle (an array parallel to
   `reopened_at[]`, or derived from `events[]` which already records every transition), or
   the fields are explicitly named last-cycle in the schema record. Deriving from `events[]`
   is the build-ladder answer -- the data is already there.

## P1 -- `MATRIX` cannot EXPRESS a scoped grant, and W-C is the first one
`MATRIX` maps action -> set of principal classes; `authorize()` returns `(allowed, pc)`.
Every grant in it today is **unscoped** -- an INTERNAL user who may `LIST` may list
everything -- so action-only modeling has been faithful. **CLIENT READ-OWN is the first
grant where the principal may perform the action only over a SUBSET of rows, and the matrix
has no place to say so:** an auditor reading `"LIST": {INTERNAL, SVC_ANALYST_INTAKE, CLIENT}`
sees "clients can list tickets", with the load-bearing "own only" living in handler code
beside the authorization surface rather than in it.
**This is Rule 22a's comp-iam defect one layer up** -- an instrument modeling `(action)` and
never `(action, resource)`, where "a role holding GetObject on ANY bucket reports GRANTED for
EVERY other." The estate has already paid for that shape once.
**Remedy direction:** the matrix value carries the scope (`CLIENT: OWN` vs `INTERNAL: ALL`),
`authorize()` returns it, and the handler derives its filter FROM the matrix instead of
maintaining a parallel truth. Then the mutants assert against one dict an auditor can read.
Note this changes `authorize()`'s return contract -- cheaper at W-C than after.

## P1 -- CE at the declared layer: the lifecycle has ONE terminal state, and the client-facing tabs make that visible
Declared layer: *every terminal state of one ticket*. Deployed values: `open`,
`in_progress`, `completed`. **There is no terminal state for a ticket that is rejected,
duplicate, out-of-scope, or withdrawn by the client.** Its only exits are to sit `open`
forever -- polluting the board's Open tab, which is the Opal user's live work queue -- or to
be force-`completed`, which under C4 shows the CLIENT a "Completed" tab entry **with an AI
summary of its resolution**. A ticket that was never resolved reads to the client as
resolved.
Same class as my WITHDRAWN finding on the memory outcome enum (2771, adopted) and as the
Rule-24 scoping's own worked example. **It is P1 rather than P2 because of the retrofit
cost Andrew named:** `status` is the **hash key of `status-index`**, and rows already
force-completed cannot be told apart from genuinely resolved ones after the fact -- the
distinction is unrecoverable, not merely missing.
**Remedy direction:** the W-A schema record enumerates the terminal set deliberately (the
four-postulate test against the declared layer), and the client-facing tab mapping is stated
for each value -- including which terminal states show no AI summary.

## P2 -- `resolution` (internal, deployed) vs `resolution_summary` (client-facing, new)
Two similarly-named fields with different authors and different audiences on one row: the
Opal user's close note, and BG's client-readable AI summary. C4 renders "the summary" to the
client; a renderer or a future reader that reaches for `resolution` shows the internal note.
Largely mitigated by the P0 projection remedy (which is why it is P2, not P1) -- but the
schema record should name the audience of each field explicitly, since the projection is the
only thing standing between them.

---

## WHAT YOU SHOULD HAVE ASKED BUT DID NOT
1. **`client_updates[]` is append-only and client-authored -- what bounds it, and what
   happens at the 400KB item cap?** 2776 notes the cap with "the S3-spill key
   designed-not-built." **An append-only array written by the least-trusted principal is the
   one field on the row whose growth is not controlled by Opal.** At the cap, DynamoDB
   rejects the write -- so the failure surface is a client typing an update and getting an
   error, on the live-beta client path, and the spill design is the thing not built. A
   per-entry length cap and a per-ticket entry cap are one line each at W-A; the spill is
   not needed if the caps exist. (The row already caps `description` at 8000 and
   `resolution` at 2000 -- the pattern is established; `client_updates[]` should inherit it.)
2. **Who may WRITE `client_updates[]`, and does SoD apply?** The field is the client's voice
   on a ticket, but every existing write path is gated by `MATRIX` + `_sod_block`, and
   `_sod_block` forbids the requester from acting on their own ticket. The natural author of
   a client update **is** the requester. So either a new action carries an explicit SoD
   carve-out, or the first client update is denied by a control written for a different
   purpose -- discovered at test time rather than design time.

-- 3.0.0_SA_CVO
