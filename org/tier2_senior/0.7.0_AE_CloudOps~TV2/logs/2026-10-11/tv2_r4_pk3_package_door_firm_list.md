# The package door's firm list goes from empty to three firms — 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-APPLY-R4-pk3.package-door-firm-list-env-dell2 (read at `8c27dc6f3d`, AMENDMENT 2)
**Status:** COMPLETE — branch A, 6 of 6 legs, AC1 `READ27 27/27` on the unchanged build

---

## Objective

ENV ONLY: set `PACKAGE_ALLOWED_FIRMS = "49financial,cottonwood,inflection"` on `opal-ticket-api`,
replacing the empty list this seat set four hours earlier under R4-pk-2. The artifact must **not** move.
Third write of IRPT_ANLREQ's packager-mint pair. Cell `R4-pk-3`.

---

## The order arrived, was withdrawn, and was restored — in twenty minutes

| time | event |
|------|-------|
| 16:57:56Z | order issued, queued behind the fifth run by its own ordering condition |
| 17:00:01Z | **AMENDMENT 1: GO WITHDRAWN** on a CTO ruling — the packager token's tier had not been read |
| 17:12:20Z | **AMENDMENT 2: hold LIFTED**, second GO; tier closed as `service`; the CTO half corrected |
| 18:0xZ | started, after the fifth run's process exited and its step-6 report was sent |

**Nothing had to be undone.** The ordering condition put this order behind the fifth run, so when the
withdrawal landed I had opened no ledger, planned nothing and changed nothing. Reading an order early is
free; *starting* it early is what the condition forbids, and that distinction is the whole value of the
condition.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` (6 legs) + 6× `close-leg` + `close` | PASS | union found 2 open ticket rows, both mine |
| git hash-object | on the mint packet | PASS | `5a202040cd` — **the packet I read is the one that was signed** |
| terraform show -json | on the saved planfile | PASS | artifact fields unchanged; caught the `null` rendering again |
| safe-apply.sh | `apply <planfile>`, no `MSYS_NO_PATHCONV` | PASS | 0 add / 1 change / 0 destroy in 6s |
| get-function + package download | before **and** after | PASS | `c4003667…` both times, by content |
| record-terraform-deploy.sh | `ticket-center --function opal-ticket-api` | PASS | "provenance refreshed, value unchanged" |
| clamp_precheck.py | `--out …/r4_pk3/…` | PASS | `READ27 27/27`, CLAMPED on `c4003667` at the **new** LastModified |

**What worked:** verifying the packet by **blob** rather than by path. The CTO half names
`blob 5a202040cd`, and `git hash-object` on the file returns exactly that — so the 115 lines I read are
the 115 lines that were signed, not a later edit at the same path.

**What failed:** two instrument errors of my own, both caught and neither reported as a result —
see Decisions 4 and 5.

**Gap found:** one row, `TCKT_VNEXT-D2-S43`.

---

## Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Both halves read; ledger; union at `17:55:20Z` | **60 trees** (grepped 60 == enumerated 60); 42 ticket rows, 11 distinct; **2 open, both mine** — this one and the fifth run's expected-open row |
| 1 | STOP 1, before my own edit | 0 changed paths at the two pinned files, against an **882-path** control |
| 2 | BEFORE | live `d2w1YJ8A…`; deployed handler `c4003667…` **by download**; 9 env keys as length+hash; `PACKAGE_ALLOWED_FIRMS` length 0; ItemCount 25; control ticket as a whole-item hash |
| — | *unasked check* | the value I was about to type hashes **identically** to the live `COMMENTARY_ALLOWED_FIRMS` |
| 3 | THE ONE EDIT | `743c4ccec6` — 1 file, 8 insertions, 6 deletions; anchor asserted to occur exactly once |
| 4 | Plan → one safe-apply | `0/1/0`; `source_code_hash`, `s3_object_version`, `s3_key` all **unchanged** in the planfile JSON |
| 5 | Five after-reads | all pass — (c) only after I fixed my own bad hostname |
| 6 | RECORD | `806da2adf6`; both halves one commit; STOP 3 did not fire |
| 7 | AC1 | `READ27 27/27`, `c4003667 CLAMPED` at `18:06:52Z` |
| 8 | Close, proof, flip, log, report | ledger 6/6; proof **VALID** in the deliverables root |

## Verification

```
(a) CodeSha256 d2w1YJ8AU7vvBufCXNvBcL/wXYAlNWbY3o85l6z0Qps=  UNCHANGED
    deployed member re-downloaded: c40036677aae...  UNCHANGED
    LastModified 15:18:51Z -> 18:06:52Z   <- config moved, code did not

(b) env key COUNT 9 / 9      ADDED []   REMOVED []
    the 8 OTHER values, by sha256        8 of 8 identical
    PACKAGE_ALLOWED_FIRMS = "49financial,cottonwood,inflection"  len 33
    sha256[:16] 66d47236daafbe12 == COMMENTARY_ALLOWED_FIRMS's
      -> "the two lists stay equal" MEASURED, not asserted

(c) POST .../package -> 401   POST .../report -> 401
    control GET /api/scoped/tickets -> 401
    NEGATIVE CONTROL: a route that does not exist -> 401 as well
      -> the authorizer answers BEFORE routing. This proves the host is reached
         and unsigned calls are refused. It does NOT prove the package route
         exists, and the handler never saw PACKAGE_ALLOWED_FIRMS.

(d) ItemCount 25, TableSizeBytes 31538 unchanged
    TCK-20261009-a1052909: 23 attrs, whole-item sha256 80ea57fceb215b73 == before

(e) No changes. Your infrastructure matches the configuration.
```

---

## Decisions Made

1. **Cited the corrected CTO half in the Terraform comment, not the pin the order names.** Step 3 says to
   cite `@65622fbcdc`; AMENDMENT 2 says `@7b039a456b` **replaces** it. The correction is substantive — two
   sentences the original signed were false ("the resident host's role and no other" reads the secret; "one
   door"). Baking the superseded pin into infrastructure code would age a citation at the instant it was
   written. The comment names the governing half **and** the pin it replaced, so nothing is lost either way.
   Reported as a departure rather than buried.
2. **Hash-compared the value before typing it.** `49financial,cottonwood,inflection` hashes identically to
   the already-live `COMMENTARY_ALLOWED_FIRMS`, which is what the signed half means by "the two lists stay
   equal". That turned the after-read from *reading a string back and eyeballing it* into a hash comparison
   against a value that was already in the world.
3. **Asserted the edit anchor occurred exactly once** before writing. The file carries a second
   DECLARED-EMPTY comment immediately below for the W-E mail slots — precisely the neighbour a loose anchor
   would hit.
4. **Did not report my first after-read (c) as a result.** I typed `portal.opalinvest.com`, a hostname I had
   invented; it does not resolve and curl returned `000` three times, including on the control. **A `000` is
   not a `401`** — it is the absence of an answer, and reporting it would have claimed a refusal that never
   happened. I read the real CloudFront host out of the runner that had just used it and re-ran.
5. **Read the recorder's usage instead of guessing twice.** My first call was `--function opal-ticket-api`
   with no pipeline; the script takes `PIPELINE` as `$1` *before* parsing flags, so `--function` was eaten as
   the pipeline name and the function fell through to `Unknown argument` at rc 1. Nothing was written.
6. **Let the recorder record less than a code deploy would.** It reported "provenance refreshed, value
   unchanged" and `1 already-in-parity`; `last_deployed_commit` correctly stays `596aaed93a` because that
   field tracks the last commit touching the **source** dir and this edit touched the terraform dir. The
   order says not to force it, and I did not.
7. **Named two silent-blind instruments in the recorder's own commit** rather than reading them as passes:
   its commit-gate reported "checked 0 of 2 file(s) — NOTHING WAS CHECKED", and client-data-check reports its
   hashed account-id list **ABSENT**. Absent is not empty.

---

## Files Modified

| File | Commit |
|------|--------|
| `infra/aws/terraform/ticket-center/main.tf` (the one edit) | `743c4ccec6` |
| source map + `CHANGELOG.json` | `806da2adf6` (by the recorder) |
| ledger + row, proof_of_spec, AC1 table, surprise row S43, this log, TO status | this commit |

---

## Blockers

None owed by this seat.

**Carried, not mine:** row **S40**, the creator's unbound write, until `2.0.0_SA_COO~Y2`'s binding cell
lands. The **two-change rollback** asymmetry recorded under pk2 is now moot for the env key — the rollback
for *this* apply is one change (the list back to empty), and the mint packet's section 5 orders it first,
because a minted token stays valid until 2027-01-09.

---

## Current State

The package door reads a firm list naming three firms for one service subject, `svc-irpt-packager`.
**Nothing has walked through it and nothing can yet:** the resident is not bound to the packager, no caller
holds the token's reader, this seat holds no token and called the door with no identity. Its admission, its
five coded 409s, its 200 body and its conditional write all read **APPLIED, UNEXERCISED**. What changed is
only that an admission is now *possible* for a body firm on the list.

The only immediate disarm is this list going back to empty. The minted token stays valid until its expiry,
which is why the signed rollback puts the list first.

---

## Next Steps

1. The fifth run's step 7 (`TO-RUN-R4-tr1`): one `--finish-cleanup` no earlier than **19:09:43Z**, then a
   ConsistentRead ABSENT, then that ledger closes. Its L3 is open by design until then.
2. IRPT_ANLREQ cell 4 binds the resident to the packager — the act that makes the door reachable, and not
   this seat's.
