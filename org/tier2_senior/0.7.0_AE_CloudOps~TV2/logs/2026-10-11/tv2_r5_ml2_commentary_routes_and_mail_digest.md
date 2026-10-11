# Two commentary routes and the mail digest — 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-APPLY-R5-ml2.commentary-routes-and-mail-digest-dell2 (read at `579de1cd17`)
**Status:** COMPLETE — branch A, 7 of 7 legs, AC1 `READ27 27/27`, row `S45` filed

---

## Objective

Deploy `opal-ticket-api` at pin `33d165b4ef` (handler `7113a749`) **and add two API routes** in one `safe-apply`:
`commentary-draft` for the service subject `svc-commentary`, `commentary-sent` for an internal person. No env
change. First order in this series to create a **route**, so the rollback trigger is new in kind: a new path
answering anything but 401 unauthenticated means a route without the authorizer in front of it.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` (7 legs) + 7× `close-leg` + `close` | PASS | union: 65 trees, 1 open entry (mine) |
| sha256 over the packet's **first 112 lines** | vs the sha the CTO half names | PASS | **proves AMENDMENT 1 only appended** |
| build-and-upload.sh | `BUILD_ONLY=1`, then the real build | PASS | identical member hash both times |
| terraform show -json | the saved planfile | PASS | routes' `authorization_type`; **zero env keys changing** |
| aws apigatewayv2 get-authorizer / get-routes | resolve `naqxlm`; census before and after | PASS | 9 → 11 ticket routes |
| safe-apply.sh | `apply <planfile>`, no `MSYS_NO_PATHCONV` | PASS | 2 add / 1 change / 0 destroy |
| curl through CloudFront | 4 unauthenticated POSTs, before **and** after | PASS | 401 ×4; trigger did not fire |
| record-terraform-deploy.sh | `ticket-center --function …` | PASS | both halves one commit |
| clamp_precheck.py | `--out …/r5_ml2/…` | PASS | `READ27 27/27` — **and a finding** |

**What worked:** hashing the packet's **first 112 lines**. The CTO half binds itself to a sha256 over 112 lines;
the amended packet is 140. Hashing the first 112 returned that exact sha, which proves AMENDMENT 1 *appended*
and altered nothing signed. Otherwise "the text above is unchanged" would have been the issuer's word alone.

**What failed:** two instrument errors of mine, both caught and neither reported as a result (Decisions 6, 7).

**Gap found:** one row, `TCKT_VNEXT-D2-S45`.

---

## Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Both halves + amendment; ledger; union at `21:01:59Z` | **65 trees** (grepped 65 == enumerated 65); 30 rows, 11 distinct; **1 open, mine** |
| 1 | STOP 1 | 0 changed paths at the two pinned files vs an **882→93**-path control over that range |
| 2a | BEFORE, code | live `d2w1YJ8A`, deployed handler `c4003667` **by download** |
| 2b | BEFORE, env | 9 keys as length + sha256; `PACKAGE_ALLOWED_FIRMS` still my pk3 value |
| **2c** | **BEFORE, the client-mail safety read** | **no commentary member can reach a client's mail** — see below |
| 2d | BEFORE, the new paths | 401 — **and so were the existing ones**, so this baseline proves nothing about existence |
| 2e | BEFORE, the table | ItemCount 27; control ticket 23 attrs, `commentary_sent` absent |
| 3 | THE ONE EDIT | `1067cc5449` — 1 file, 5 insertions, anchor asserted unique |
| 4 | Build + upload | `BUILD_ONLY` first; object re-downloaded and opened: `7113a749` |
| 5 | Plan → one safe-apply | `2/1/0`; both routes `CUSTOM`/`naqxlm`; **zero env keys changing** |
| 6 | Six after-reads | all pass; **four 401s**, trigger did not fire |
| 7 | RECORD | `b93aedaa72`; both halves one commit; STOP 3 did not fire |
| 8 | AC1 | `READ27 27/27` — **plus the row the order and the CTO half both asked for** |
| 9 | Close, proof, flip, log, report | ledger 7/7; proof **VALID** first pass |

## Verification

```
(a) CodeSha256 e1ZHjf21aXbkjDD2CJab4oTxdCIed08bQ5/pKL/37Dw= == uploaded zip
    deployed member, fresh download: 7113a749...   LastModified 21:27:13Z
    the handler's identity on FOUR planes: pin, working tree, uploaded object, deployed package

(b) env 9 / 9 keys, ADDED [] REMOVED [], 9 of 9 values hash-identical  -> untouched

(c) POST .../commentary-draft -> 401     POST .../commentary-sent -> 401
    POST .../report          -> 401     POST .../package         -> 401
    rollback trigger fired: NO
    BUT: both new paths also answered 401 BEFORE they existed (step 2d), because the
    authorizer answers before routing. So EXISTENCE comes from the route census:
      119 -> 121 routes on the API; 9 -> 11 ticket routes; both new keys present;
      all 11 CUSTOM/naqxlm; naqxlm = portal-jwt-authorizer (opal-portal-authorizer)
    Three claims, three instruments, none carrying another's weight.

(d) ItemCount 27 / 34549 unchanged; control ticket sha256 80ea57fceb215b73 == before
    commentary_sent still ABSENT -> the apply wrote to no ticket

(e) No changes. Your infrastructure matches the configuration.
```

### Step 2c — the read that carried a STOP

`CLIENT_NOTICE_FIELDS` (line 973) is an allow-list of three: `ticket_id`, `created_at`, `title`.
`client_notice()` (line 994) builds its body from a **fixed four-line list** and **never iterates the item** —
no `for`, no `.items()`, no `**item`, no `dict()` anywhere in 994–1022. That is what makes the allow-list
structural rather than advisory: an unlisted member cannot be swept in by a loop that does not exist.
`CLIENT_NOTICE_PROHIBITED` (978–979) now also names all three members, so a later widening of the allow-list
meets a named refusal. A census of the three names across the build found 63 occurrences, none in the client
mail path. **Answer: no, none of the three could reach a client's mail.** Verified from the build, not adopted.

---

## The finding: AC1's number does not cover what it looks like it covers

The order anticipated two readings — the census "does not take in the two new routes", or "the total changes".
**The world is neither.** The total stayed `27/27` *and* neither route name appears in the output or the table.

The precheck's own first line says it reads *"which of the **27 formerly-MORE_THAN_ONE** routes run the firm
clamp LIVE"*. Its denominator is a **frozen round-3 set**, not a live census of scoped routes — so it could
never take in a route created afterwards, and the total was never going to move. `27/27` is true of its
declared domain and says nothing whatever about the two new routes. That is the tell rule 24(i) names: a
denominator whose scope **in time** is narrower than the sentence beside it.

So I answered the substantive question directly, from the **deployed** bytes:

- `commentary_draft_ticket` (deployed line 1532) refuses at **1552** with one folded check —
  `cur is None or requester.firm not in COMMENTARY_ALLOWED_FIRMS` → the same `_deny`. That is AMENDMENT 1's
  first requirement confirmed in the shipped bytes, not merely in a diff.
- `commentary_sent_ticket` (1575) runs `_resolve_scope` (1583) and `_in_profile_scope` (1587) → 404 out of
  scope — the report route's own check.

**There is no unclamped scoped route.** There is an acceptance instrument that cannot see two live ones. Filed
as `S45`; the CTO half asked for exactly this row, within the hour.

---

## Decisions Made

1. **Hashed the packet's first 112 lines** rather than trusting "the text above is unchanged".
2. **Resolved the authorizer's identity, not just its type.** `CUSTOM` is not the claim "the portal
   authorizer"; `get-authorizer` gave `portal-jwt-authorizer`, and all 9 live ticket routes use the same
   `naqxlm`, so the new routes take an identical pair rather than merely a custom one.
3. **Did not let the 401s carry the existence claim.** They cannot: an absent route answers 401 too, which my
   own step-2d baseline demonstrated. Existence came from the route census.
4. **Verified step 2c myself** instead of adopting the CTO half's read, since it is the one check standing
   between a client and an internal draft.
5. **Answered the AC1 question beyond "the instrument is blind"**, by reading the firm checks out of the
   deployed bytes — a row that says "and here is the answer it would have given" is worth more than one that
   says only "it cannot see".
6. **Resolved the MSYS `/tmp` trap rather than concluding the zip was missing.** Windows python threw
   `FileNotFoundError` on a path bash could see at 30986 bytes; `pwd -W` gave the real one.
7. **Widened my own census regex mid-read.** My first pattern matched only double-quoted keys and missed
   `item.get('created_at')` at line 1018, understating what `client_notice` reads by one member.
8. **Read both headings and JSON ids for the row id.** Headings showed 16 ids, the JSON 44, and seven ids
   appear more than twice — including the `S43` I filed myself hours earlier. Heading-only would have collided
   again.
9. **Left the source map dirty for the recorder**, which owns that file, rather than committing it separately.

---

## Files Modified

| File | Commit |
|------|--------|
| `infra/aws/terraform/ticket-center/main.tf` (the one edit) | `1067cc5449` |
| source map + `CHANGELOG.json` | `b93aedaa72` (by the recorder) |
| ledger + row, proof_of_spec, AC1 table, row `S45`, this log, TO status | this commit |

---

## Blockers

None owed by this seat. **Carried, not mine:** row `S40` (the creator's unbound write, pending
`2.0.0_SA_COO~Y2`); row `S45`'s disposition and any amendment of AC1's expectation (the CTO's and the
issuer's). **Named but unswept:** whether any *other* scoped route added since the round-3 set was frozen sits
outside the clamp — a different read over the API's 121 routes, stated in `S45` rather than implied.

---

## Current State

`opal-ticket-api` runs `7113a749` and the API carries two new ticket routes, both behind the portal
authorizer. Both routes' **admissions, every coded refusal, and the recipient digest on a real send are
UNEXERCISED**: nothing calls either route today — the drafter still creates a new ticket, no page calls the
sent route — this seat minted no identity and called neither route with any, and the apply sent no mail, so
the 12-hex digest has never been computed on a live address.

**FWD-6 is built in the service and not live end to end**, exactly as both halves state. The first clause
waits on the drafter's owner changing its call; the second waits on a portal cell, since the ticket panel does
not know `commentary_sent`.

---

## Next Steps

1. `1.0.0_SA_CTO~DELL2` reads row `S45` (its half asked for it the same hour).
2. The drafter's owner (`2.0.0_SA_COO~T2`) points the drafter at the new route; a portal cell surfaces
   `commentary_sent`. Only then is FWD-6 live.
