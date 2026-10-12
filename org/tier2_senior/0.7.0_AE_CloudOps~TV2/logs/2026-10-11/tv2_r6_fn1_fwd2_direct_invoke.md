# FWD-2 by direct invoke: another firm's person is refused — by class, not by firm — 0.7.0_AE_CloudOps~TV2

**archetype:** RUN (adversarial read)

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-RUN-R6-fn1.fwd2-direct-invoke-five-gets-dell2 (read at `99d6638059`)
**Status:** COMPLETE — **branch A**, AC1 `FN1-ARMS-OK`, AC2 left to the CVO

---

## Objective

Five read-only invocations of the **deployed** `opal-ticket-api`, made **directly, around the portal
authorizer**, with constructed caller contexts — to show on the live function that a person at another firm
cannot open a ticket or see it in a list. Every call a GET. Nothing written, no identity minted, no deploy,
**no ledger** (nothing is applied).

The instrument is the bypass itself: *a direct invoke means the function believes whatever the event says
about the caller.* That is why every payload is written to disk before it is sent.

---

## The result

```
arm  caller                                        call              served
A1   CLIENT  firmId 49financial (the ticket's own)  GET the ticket    403  client-human / GET
A2   CLIENT  firmId cottonwood                      GET the ticket    403  client-human / GET
A3   CLIENT  firmId cottonwood                      GET the list      403  client-human / LIST
A4   INTERNAL firmId opal-capital, no users row     GET the ticket    200  27 keys, status completed
A5   CLIENT  firmId cottonwood                      GET a missing id  403  client-human / GET

AWS StatusCode 200 and NO FunctionError on all five -- every answer is the function's own reply
BRANCH A: all five exactly as the pair's section 3 predicted from the handler's rule
```

**Two comparisons, measured rather than asserted:**

- **A1 == A2** in status, error, action and `principal_class`. A client of the ticket's *own* firm is refused
  exactly as the other firm's client is. So the refusal is **by class** (`client-human` on GET), **not by
  firm** — the precise, and narrower, claim FWD-2 may make from this act.
- **A2 == A5** in all four fields. A client **cannot tell an existing ticket from a missing one**.

All four refusal bodies name no ticket id (measured with a scan, not repeated from the pair).

---

## The CTO's own prediction was wrong, and the pair caught it

Its ruling (msg 5987) expected a client of the ticket's own firm to be **served**. The issuer read the
handler's rule before signing and found the matrix admits INTERNAL only on GET, so that client is refused
too. The CTO half says so plainly and names the error: *"This seat predicted an answer from the caller's
shape and did not read the rule, the same error as the data-refresh read this morning."*

A1's 403 confirms the pair, not the ruling. This is why the expectations in section 3 were each read from the
code rather than inferred from the caller's shape.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| git worktree + ls-tree | the open-deploy union | PASS | 68 trees, 21 open fabric-wide, **0** naming the ticket service |
| sts get-caller-identity / get-function-configuration | identity and the function ARN | PASS | **existence read before the simulate** |
| iam simulate-principal-policy | ONE action, ONE resource ARN | `allowed` | no grant asked |
| sha256 over the pair | whole, 104 lines | PASS | `d5601efe…` exact |
| aws lambda invoke | five RequestResponse calls | PASS | branch-C halt was **mechanical** |
| dynamodb get-item `--projection-expression` | status + events, before and after | PASS | keeps event content out of the read |

**What worked:** making the branch-C halt mechanical. The loop tested each of A2, A3 and A5 for 403 and
would have stopped at that arm without running the rest — the STOP did not depend on me noticing.

**What failed:** one proof-instance error of mine — five payload paths in a single `path_or_key`, which the
checker refused as a dead path. Split into five rows; the same mistake class I hit on an earlier order.

**Gap found:** none new. A4 re-confirms row `S20` (an internal caller with no users row is unscoped), which
the pair itself predicts.

---

## Verification

```
step 0  union at 22:48:37Z -- 68 trees (grepped 68 == enumerated 68), 1411 rows, 124 distinct,
        21 with no deleting commit, ZERO naming the ticket service -> no STOP
        simulate: lambda:InvokeFunction on the function ARN -> allowed (one resource per call,
        ARN read from the live service FIRST, since an allowed on a non-existent resource
        proves only that the policy pattern matched the string typed)

step 1  live CodeSha256 Ob/MZBEOVR98bV5IvkpS15NAHekVAKNvStb8J0syY6Y=, 22:16:38Z
        -- the build I deployed 30 minutes earlier under R5-cm-4

step 2  ItemCount 27 | TCK-20261011-e6433610: status completed, events LENGTH 3

step 3  five payloads written and READ BACK: version 2.0, method GET, exactly five
        authorizer keys, no body, no query string, three top-level keys

step 7  ItemCount 27 -> 27 | status completed -> completed | events 3 -> 3
        -> five GETs wrote nothing. Measured, not assumed.
        response files deleted from scratch; RESULT.json re-read: no TCK- id, no client value
```

---

## Decisions Made

1. **Read the function's ARN from the live service before simulating against it.** An `allowed` proves the
   policy pattern matched the string typed, not that the resource exists — so existence comes first.
2. **Made the branch-C halt mechanical rather than attentional**, since a client being served or being able
   to tell an existing ticket from a missing one is the one outcome that stops everything.
3. **Kept A4 to key names and `status`.** A4 is internal, so the function served the *whole* ticket — and
   that ticket is the journey item my own fifth run filed under `49financial`, carrying a portfolio upload
   reference, a title, requester fields and answers. Nothing but the key names and the status left the read,
   the response files were deleted, and I re-read the finished `RESULT.json` to confirm no ticket id or
   client value rode into it.
4. **Computed the A1/A2 and A2/A5 comparisons** rather than restating the pair's expectations. "Refused by
   class, not by firm" is a stronger and narrower claim than the outcome's own wording, and it is now
   measured.
5. **Scanned the refusal bodies for a ticket id** instead of taking the pair's word that they carry none.
6. **Used a projection expression on both table reads**, so event *content* never entered the read — only
   the list's length, which is what the order asks for.
7. **Filed no surprise row.** Everything matched; the one estate-level fact worth recording (any holder of
   `lambda:InvokeFunction` can be any caller to a function behind the authorizer) is already the CTO's own
   row by its half, so a duplicate would be noise.

---

## Files Modified

| File | Commit |
|------|--------|
| `deliverables/r6_fn1/A1..A5.json`, `RESULT.json` | this commit |
| proof_of_spec, this log, TO status | this commit |

No AWS write, no deploy, no ledger entry.

---

## Blockers

None owed by this seat.

**Named limits, not mine to close:**

- **FWD-2 reads MET FOR THE TICKET, NOT READ FOR THE FILE.** The ACCEPT has two halves — the ticket and its
  attached file — and this pair has an arm only for the first. CTO condition 1 requires the issuer to name
  where a ticket's attached file is served and add that arm by an amendment the CTO signs.
- **The internal firm fence is not shown by this act** and was never going to be: it needs a users row with a
  firm list for a constructed email, which is an identity written to a table. It rests on tests (13 + 4) and
  the synthetic filer's census in runs 1 to 5. A4 is explicitly *not* a proof of it.

---

## Current State

On the live function, no client — of any firm, including the ticket's own — can open this ticket or see it in
a list, and cannot distinguish it from a ticket that does not exist. An internal caller is served, which is
what makes those refusals readable rather than the silence of a dead route. Five GETs wrote nothing.

---

## Next Steps

1. `3.0.0_SA_CVO` grades AC2 at L9 on `RESULT.json`.
2. The issuer names where a ticket's **attached file** is served and adds that arm by an amendment; only then
   can FWD-2 be offered to the reviewer as met.
