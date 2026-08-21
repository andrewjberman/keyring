# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-21 0840Z – 0849Z

**archetype:** IMPLEMENT
**Projects:** D7_NOTIFY — TO-E (the client-facing leg)

> **Timestamps in this log are read from `date -u` in a prior tool call, not inferred.** My own
> hand-written stamps were measured drifting **+2 to +52 min (mean +19.1 over 17 sends)**, confirming
> COO~Z's fabric-wide ratchet at a third seat.

## Summary

`D7_NOTIFY.TO-E_PROOF_OF_SPEC.json` **VALID rc=0, 6 rows, 0 violations, 6/6 PASS.** Three files:
the handler, a 19-test battery, the Terraform. **Built, not applied.**

**The first client-facing email in the system**, so the tests are weighted toward what a wrong
assumption costs — a cross-tenant leak, a link landing on an access denial, an internal address
disclosed to an external reader — rather than toward coverage.

## 1 — E-0: the link is omitted, never defaulted

`resolve_client_link(firm) -> url | None`, and **there is deliberately no `"*"` row.**

Denominator as **firms, named**: the map carries **3 of 4 — 49financial, cottonwood, demo — and not
inflection** (`firmAccess.ts:66`, the 2026-05-28 Tools-section ruling). Both directions exercised:
each mapped firm gets its link; inflection gets `None`, and the body is asserted to contain **no
`http` at all** — not merely "not that URL."

**The absent default row is the load-bearing part and is easy to "fix" by mistake.** A `"*"` row
looks like robustness and silently re-introduces the exact defect: an inflection user sent to a page
that bounces them. That's why the no-default assertion is its own test rather than a comment.

## 2 — E-3: single-recipient, and the split that makes it testable

`notify_client` refuses any non-singular destination list with a named
`ClientRecipientNotSingular` — enforced **at the send**, not trusted of the caller.

I split `_client_recipients` out from the guard **specifically so the mutant hits the real guard**.
Had derivation and guard been one expression, the only way to test it would be to re-implement it in
the test — which tests the copy. With the split, the test replaces the derivation with a two-element
list and the real code refuses, **sending nothing to either address.**

## 3 — E-2: the degradation choice is mine, and I'm flagging it rather than presenting it as ruled

`_directory_snapshot` fails soft by design, so `claimed_by` can carry an email and no name. Three
options, none free:

| | |
|---|---|
| (a) fall back to the claimer's **email** | discloses an internal staffer's address to a client |
| (b) substitute *"an Opal advisor"* | answers with something Andrew did not rule |
| **(c) refuse and send nothing** | the client gets nothing; the gap becomes a log line |

**I took (c)** — it keeps the refuse-loudly discipline, never discloses an address he didn't approve
disclosing, and makes a directory gap visible. **(b) is defensible and is a one-line change**; whether
a client is better served by a vaguer message than by none is CTO~Z's call. The claim succeeds either
way.

The refusal is itself asserted **not to leak** — the exception message is checked to contain no
internal address. A refusal that discloses what it refused to disclose would be worse than the send.

## 4 — E-4: re-derived, not inherited

Asserted on a row where every internal-only field is populated with a sentinel: **7 sentinels × 2
message kinds = 14 absence subtests**, plus a positive control proving the absence check can fire.

The interesting exclusion is **`description`** — the client authored it, so echoing it back adds
nothing they lack while enlarging a surface that crosses a tenant boundary. That's pointer-not-home
applied fresh, not TO-A's set trimmed.

And the apparent contradiction isn't one: `assignee` (the claimer's **email**) is prohibited while
the claimer's **full name** is ruled in for the pickup. **A name is what Andrew approved disclosing;
an address is not.**

## 5 — The pickup test is a disjunction, and that's the honest form

`FakeTable`'s `claimed_by` depends on what `_directory_snapshot` produced, so the end-to-end test
asserts **either** a send **or** a named no-name refusal, and **excludes silence.**

Asserting a send would make the test depend on a stand-in's fidelity to a live directory; asserting
nothing would let a skipped leg pass. It's A-3b's reachability shape arriving on a different
criterion.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| python `ast` call-site check | `submit_form → ('ack')`, `claim_ticket → ('pickup')` | AST because the question is *which handler, which kind* — text can't attribute a call to its enclosing function |
| `terraform fmt -check` | **RC=3** — misaligned `=` on the new key | ⛔ **I'd redirected fmt's output to /dev/null and would have missed it**; caught by capturing the rc separately. `terraform fmt` → re-check RC=0 |
| `terraform validate` | rc=0 | no plan, no apply |
| `commit-gate.sh` | rc=0, 2 files | byte scan separately: 0 non-ASCII, 0 CRLF |
| 4 batteries | client **19 OK** · W-E **27 OK** · authz **15 OK** · intake **42 + 25** | all rc=0 on the tool; authz is the no-regression evidence for the two paths the new code now runs through |
| `proof-of-spec-check` positional | rc=0, rows=6, violations=0 | PASS |
| own-instance mutant | anchors held (6 rows, all PASS → rule **firable** on this shape), then rc=1, violations=2, INVALID naming E-0 | CONTROLLED |

## Blockers

**None I hold.** E is complete. **D-PROSE next** (plain text, no deploy), then **D-HTML build-only** —
it needs `contentType: "html"` in the gateway, which bounces the box every seat here reaches MCP
through, and that cost has not been put to Andrew. **F begins when D and E land**, since its subject
is a four-leg failure matrix and two of those legs are what D and E build.

One decision waiting on CTO~Z: **E-2's degradation** — refuse (built) vs a generic substitute. Zero
crons, nothing applied, no send to anyone.
