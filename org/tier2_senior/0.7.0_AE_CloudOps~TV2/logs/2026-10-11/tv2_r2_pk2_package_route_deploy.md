# The package route no longer hands the packager the ticket — 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-APPLY-R2-pk2.package-route-narrows-code-dell2 — first GO `dbb7aa26cf`, second GO `c492e616f6`
**Status:** COMPLETE — applied on the second GO, branch A, after a correct STOP on the first

---

## Objective

Deploy `opal-ticket-api` at `be67d1fd38` so `POST /api/scoped/tickets/{ticketId}/package` stops returning
the ticket (on its 200 and its changed-under-write 409) and its five 409s gain a `code`. Cell `R2-pk-2`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | two entries, `open` + 5x `close-leg` + `close` each | PASS | both opened before any write; attempt 1 closed on the STOP, attempt 2 closed 5/5 proven; each row read back ABSENT against a printed control |
| r2_checks.py | `pk-200` (AC1), `pk-codes` — both attempts | PASS | 2/2 and 5/5 each time |
| safe-apply.sh | `-chdir=… apply <planfile>` | PASS | attempt 2 only; **no `MSYS_NO_PATHCONV=1`** — the ban this order carries by name |
| terraform plan / replan | `-out=<planfile>`, then plan again | PASS | branch A exactly; replan `No changes.` |
| build-and-upload.sh | `BUILD_ONLY=1` then the real run | PASS | both builds produced the identical content hash |
| comp-find | `opal_packager` unscoped, `--band SURFACED --all`, `--corpus aws … LAMBDA` | PASS | attempt 1's domain falsifier and graph corroboration |
| comp-which | asked for a "which package contains this file" tool | WARN | none exists; sweep hand-rolled and its scope stated |
| aws lambda get-function + download | the live package before and after; 17 packages on attempt 1 | PASS | rollback target and deployed bytes both by content |
| safe-commit.sh | one commit per act, `-F` by a non-shell writer | PASS | `msg-verify MATCH` each time |

**What worked:** re-reading STOPs 1 and 2 **live** on the second attempt rather than carrying attempt 1's
readings. The positive control moved 301 → 389 over the same two commits, which is the proof it is a live
control and not a memoised number, while the ticket-tree diff stayed 0 both times.

**What failed:** nothing in this order's execution. The first attempt's STOP was correct but my row S34
overstated its own denominator — see Decisions 1.

**Gap found:** none new. S34 stands, now resolved by the amendment.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Ledger first, union at `09:40:20Z` | **48 trees** (enumerated 48 == grepped 48), 26 ticket rows, 9 distinct; only this entry open; attempt 1's own entry reads closed-by `a2a7201fbe` |
| 1 | STOP 1, re-read live | 0 changed paths vs a **389** control (301 on attempt 1 — it moves); 0 dirty; shipping file `cf10e19e…` |
| 2 | STOP 2, re-read live | live package: 1 member `ca3be343…`, package b64 == live `CodeSha256` → the object read IS the running artifact |
| 3 | STOP 3 | met **by the record**, both reads side by side, no deployed caller claimed — see Verification |
| — | AC1 | `PK-200-OK 2 of 2`; `PK-CODES-OK 5 of 5` |
| 4 | BEFORE | `W03VREoM…`, 8 env keys, ItemCount 21, control ticket 23 attrs / open / NULL / svc-commentary |
| 5 | Build + upload | version `dywIwIVGlgblMDmK3fvi3IWlkxzMV3cm`, 29314 B; downloaded back: 1 member `cf10e19e…`, no `tests/` |
| 6 | Plan, then ONE safe-apply | `0 to add, 1 to change, 0 to destroy`; `Apply complete! 0 added, 1 changed, 0 destroyed` |
| 7 | Five after-reads | all pass — see Verification |
| 8 | Close, report once | ledger CLOSED 5/5; deployed hash reported FIRST so the issuer can update `TICKET_OK` |

## Verification

```
STOP 3, met by the record (AMENDMENT 1) -- both reads, no deployed caller claimed:
  (i)  mine            N=17 Lambdas swept by content, 0 carry opal_packager.py,
                       17 do not, 0 unreadable; control finds served.py in irpt-status.
                       POPULATION WAS LAMBDAS -> silent about a non-Lambda host.
  (ii) 2.0.0_SA_COO~G2 running resident root e606008994-st27.tar.gz,
       (msg 4594)      sha256 20916261074c356a..., 270 members:
                       ycharts/research/opal_packager.py ABSENT, 0 "packager" members,
                       no packager binding.
                       ITS OWN LIMIT: build input of the running root, host bytes not listed.
  CTO msg 4587 ruled PROCEED on that basis. Not my ruling.

(a) CodeSha256 t1EoiJRZWXBsSc0HPw+61IP+zdQxyYGfWEi+8L6lej4=  == uploaded zip
    deployed package re-downloaded from Code.Location:
      members: 1 ['lambda_function.py']
      deployed member : cf10e19e423b25b7b74ce43efd24e73b90a8a90850094697f3f79ec7145e6e74
      required (pin)  : cf10e19e423b25b7b74ce43efd24e73b90a8a90850094697f3f79ec7145e6e74
    LastModified 2026-10-11T09:47:09Z | runtime/timeout/memory unchanged

(b) env  before 8 | after 8 | key names identical: True | VALUES identical: True

(c) POST https://opalinvest.dev/api/scoped/tickets/TCK-20261009-a1052909/package (no auth)
    HTTP 401 {"error":"Missing or invalid Authorization header"}
    control GET /api/scoped/tickets -> 401 (non-000 proves the client reached CloudFront,
    and proves ONLY that; the authorizer fronts the whole /api/scoped prefix)

(d) ItemCount 21, TableSizeBytes 25398 -- unchanged
    TCK-20261009-a1052909: 23/23 attributes, WHOLE ITEM identical -> no ticket written

(e) No changes. Your infrastructure matches the configuration.

NOT exercised: the two live arms (a 409 carrying its code; a 200 without `ticket`).
They need the service principal's token -- the packager's next attach, or AR-g-32.
```

---

## Decisions Made

1. **My first attempt's row S34 claimed more than it measured, and I said so rather than let it stand.**
   S34 reads "the route's ONE caller is not deployed at all: no live Lambda carries opal_packager.py."
   The second clause is what I measured; the first generalises past the swept population, which was
   *Lambdas from the source map*. I falsified the domain for **source references** but never tested the
   order's premise that the host must be a Lambda — and the resident is exactly the uncovered member a
   node-type-scoped subtraction cannot see. The STOP was right to fire; the row should have read "no
   Lambda carries it; a non-Lambda host is not ruled out by this read."
2. **Stopped on attempt 1 rather than reasoning past the gate, and let the owners resolve it.** An absent
   caller plausibly made the apply safer, but the CTO had made step 1b a pre-plan gate with a named STOP.
   `1.0.0_SA_CTO~DELL2` then ruled PROCEED on the right-population read. That ruling is cited, not
   reconstructed.
3. **Re-read STOPs 1 and 2 live on attempt 2** instead of carrying attempt 1's readings — which is how
   the control's 301 → 389 movement became visible, and therefore how I know it is a control.
4. **Did not ride `MSYS_NO_PATHCONV=1` on safe-apply.** My own lapse from R2-rr-2 is now a standing
   instruction in this order's context; every gate limb evaluated.
5. **Reported the deployed file hash first.** The issuer owes `TICKET_OK` the new hash in the same
   sitting — the exact inverse of what I told them on the stopped attempt, when the live build was
   unchanged and the hash had to stay out.

---

## Files Modified

| File | Commit |
|------|--------|
| attempt 1 ledger + row, proof (STOP), log, row S34 | `a2a7201fbe` |
| attempt 2 ledger + row | this commit |
| `TCKT_VNEXT.TO-APPLY-R2-pk2…proof_of_spec.json` (second revision) | this commit |
| this log | this commit |
| task order `pending` → `complete` | this commit |

---

## Blockers

None owed by this seat. **One act owed by the issuer, same sitting:** add
`cf10e19e423b25b7b74ce43efd24e73b90a8a90850094697f3f79ec7145e6e74` to `reread_27.py`'s `TICKET_OK`, or
the next run's precheck reads `NOT-RELEASED` on this host exactly as it did for the R2-rr-2 build (row
S28).

---

## Current State

The package route is narrowed and live: its 200 and its changed-under-write 409 no longer return the
ticket, and its five 409s carry codes. Verified by content against the pinned build input. Env, table and
control ticket all untouched; rollback retained as a non-latest S3 version.

**Live arms still unexercised.** The narrowing is proven at the build (pk-200 2/2, pk-codes 5/5) and in
the deployed bytes — never against a live call. First real exercise is the packager's next attach or
AR-g-32.

---

## Next Steps

1. Issuer: `TICKET_OK` gains the new hash this sitting.
2. AC2 to `3.0.0_SA_CVO` at L9 on the ledger entry and the after-reads.
3. The live arms land with AR-g-32 or the packager's own deploy — not this seat's.
