# A users row must be status `active`, or the internal caller is refused — 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY + RUN

**Date:** 2026-10-12
**Task Order:** TCKT_VNEXT.TO-APPLY-R9-st2.status-active-code-and-five-gets-dell2 (read at `ede3792148`)
**Status:** COMPLETE — branch A, 5 of 5 legs, AC1 and AC2 both PASS, **no rollback**

---

## The five arms

```
S1  BEFORE the apply   the DISABLED row's caller      200  served  -- the before-state
S2  BEFORE the apply   a no-row caller                403  refused -- round 7's release
S3  after              the same disabled caller       403  refused -- THIS release
S4  after, THE TWIN    an ACTIVE row, no firm list    200  served  -- not overreached
S5  after              the same no-row caller         403  refused -- round 7 survives
```

`ST3-ARMS-OK S1=200 S2=403 S3=403 S4=200 S5=403`

**S1 and S2 are what make S3 and S5 mean anything.** Without S1's 200, S3's 403 could be any pre-existing
refusal; without S2's 403, S5's 403 would prove nothing new. That is why the order makes either one a STOP
before any plan.

---

## The rollback decision, computed from three integers

Two triggers, both mine to pull without waiting for anyone: **S4 not served** (active staff locked out) or
**S5 served** (round 7's refusal lost). Neither fired. The live digest re-read afterwards is still the new
build, so nothing was reverted.

**The third branch is the one worth naming:** S3 *served* would have been a STOP and expressly **not** a
rollback — a served disabled row leaves the service exactly as it was, so reverting would undo nothing.
Three branches, three different consequences, and the asymmetry is the signed part.

**Every status came from a parsed integer.** This order wrote my own round-7 near miss in as a mechanism —
there, a multi-line shell capture compared against `"200"` announced a rollback that the data *inside the
same alarm* contradicted. The arm runner now prints the human block to stderr and **exactly the integer** to
stdout, so a caller that captures stdout gets an integer and nothing else.

---

## The CTO's condition 2 earned its place

The condition: re-read the two rows the arms use; a STOP if either reads differently. Both read as stated —
one PROFILE row each, `disabled` and `active` — so no STOP, and the release proceeded.

**But the disabled row had moved:**

| when I read it | `updatedAt` on digest `e95c05c7ae90` |
|---|---|
| R8-ds-1, ~00:0xZ | `2026-10-11T22:41:40.809Z` |
| step 2 here, 01:4xZ | **`2026-10-12T01:03:31.142Z`** |

Written at **01:03:31Z — about 40 minutes before this apply**, not "hours before round 7" as the CTO half
says. Status and `userType` held across both reads, so whatever touched it did not change what the arm
depends on. Had the writer flipped `status` instead, S1 would have refused *before* the apply and the order's
own STOP would have fired — which is exactly what condition 2 is for. Filed as row **`S54`**, so the next
pair doesn't inherit a stale sentence as a current fact.

---

## One error of mine, in the log window

Step 11 expects 1 `FIRM-SCOPE-NOT-ACTIVE` and 1 `FIRM-SCOPE-NO-ROW`. My first read gave **1 and 2**.

The 2 was my scope, not the release: a 30-minute window also contains **S2, which ran before the apply** on
round 7's build and logged its own no-row refusal. Attributing that line to this release would have been
wrong. Rescoped to the 12 events at or after the apply's own `LastModified` (01:50:30Z): **1 and 1**, with
0 at-signs — and that zero is meaningful because the new log line's source carries neither the address nor
the status value.

The control still came first, per my own row `S51`: 24 unfiltered events proved the window live before any
filtered zero could be believed.

---

## Verification

```
STOP 1   0 changed paths vs 873130546e (handler + whole terraform folder), control 66
BEFORE   live lAt/vc4X, deployed handler f99a314b by download
         env 9 | 11 routes CUSTOM/naqxlm | ItemCount 27 | control ticket completed, events 3
         arm rows: e95c05c7ae90 one row disabled | 3e5db3675c91 one row active, firm list ABSENT
PLAN     0 add / 1 change / 0 destroy | 0 route resources | env 9->9, 0 keys changing
AFTER    CodeSha256 4sDK8P5m == the zip; deployed member 4136587a by fresh download
         env 9 of 9 identical | 11 routes, key sets identical
         ItemCount 27 | control ticket unchanged | BOTH arm rows same status AND same updatedAt
         replan: No changes.
LOG      1 NOT-ACTIVE, 1 NO-ROW, 0 at-signs, over 12 events at/after the apply
RECORD   4755650b13, both halves one commit; stamped 97d2d4bede handler == 4136587a
         control: prior build 09488abbb1 == f99a314b (differs) -> the match discriminates
AC1      READ27 27/27 | TICKET_HANDLERS 11/11 | UNCLASSED: none
```

---

## Decisions Made

1. **Built the arm runner to emit a bare integer**, so the rollback decision cannot be made from a
   transcript. That is the order's own mechanism and it came from my mistake.
2. **Rescoped the log window to the apply**, rather than reporting "2 where 1 expected" from a window that
   included a pre-apply arm.
3. **Filed row `S54`** on the arm fixture moving mid-round — not a STOP by the condition's terms, but the
   CTO's sentence about that row is now stale and the next pair would inherit it.
4. **Did not conclude anything about who wrote that row.** Two timestamps and the fields that did not change
   are what I measured; `updatedAt` records a touch of any kind.
5. **Touched and named nothing of digest `1af514167abb`** — the active outsider I found in R9-ct-1 — as the
   order and the CTO's msg 6259 require.
6. **Reported 0 UNCLASSED first**, as asked.

---

## Files Modified

| File | Commit |
|------|--------|
| source map + `CHANGELOG.json` | `4755650b13` (by the recorder) |
| `r9_st2/RESULT.json`, AC1 table, ledger + row, row `S54`, proof_of_spec, this log, TO status | this commit |

---

## Blockers

None owed by this seat. **With others:** row `S54`; row `S53` (the active outsider, with the CTO and Andrew);
row `S46` (narrowed by this release, not closed); row `S51`.

---

## Current State

`opal-ticket-api` runs `4136587a`. An INTERNAL caller whose users row is not status exactly `active` is now
refused `403 firm scope lookup failed`, logging one line that carries neither the address nor the status. A
caller with an **active** row is still served; a caller with **no** row is still refused, so round 7's
release survives intact. The two disabled rows are now refused by the service as well as by sign-in — which
closes the gap my round-8 read opened.

**Not shown:** a real staff sign-in after the release, and the fence between two internal callers that both
have rows (tests only).

---

## Next Steps

1. `1.0.0_SA_CTO~DELL2` reads rows `S54` and `S53`.
2. The direct-invoke path (`S46`) is narrowed by this release but not closed — any holder of
   `lambda:InvokeFunction` still presents any caller context, and now needs an active row to be served.
