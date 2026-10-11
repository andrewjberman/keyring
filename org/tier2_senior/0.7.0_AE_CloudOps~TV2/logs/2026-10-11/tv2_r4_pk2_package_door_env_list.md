# The package door now reads a firm list, and the list is empty — 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-APPLY-R4-pk2.package-door-env-list-code-dell2 (read at `471f12e2c7`)
**Status:** COMPLETE — branch A, 7 of 7 legs, deploy recorded, AC1 `READ27 27/27` on the new build

---

## Objective

Deploy `opal-ticket-api` at `f239b06ad8` **and one new env key** `PACKAGE_ALLOWED_FIRMS = ""`, then record
the deploy. The package door binds the packager's firm to that list; the list is empty, so the door admits
**nobody**. Two creator refusals of the report route gain a `code`. Cell `R4-pk-2`.

First order in this series to touch **env**, and the first where the applier makes the Terraform edit.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` (7 legs) + 7x `close-leg` + `close` | PASS | row read back ABSENT against a 19-row control |
| terraform show -json | on the saved planfile | PASS | **how the rendered `null` was resolved to `""` before applying** |
| terraform fmt -check | on main.tf after my edit | WARN | one hunk, pre-existing at the pin — left alone |
| safe-apply.sh | `-chdir=… apply <planfile>` | PASS | no `MSYS_NO_PATHCONV=1`; 0 add / 1 change / 0 destroy in 12s |
| build-and-upload.sh | `BUILD_ONLY=1` then real | PASS | identical content hash both times |
| record-terraform-deploy.sh | one function | PASS | both halves in one commit → STOP 3 did not fire |
| clamp_precheck.py | `--out …/r4_pk2/…` | PASS | `READ27 27/27`, ticket host CLAMPED on `c4003667` |
| aws lambda get-fn-config | env before/after, hashed **per value** | PASS | 8 → 9 keys, 8 of 8 old hashes identical, new key length 0 |

**What worked:** reading the **planfile JSON** instead of interpreting the rendered diff. The plan displayed
`+ "PACKAGE_ALLOWED_FIRMS" = null`, and `null` vs `""` is exactly the difference between a key AWS drops and
a key present-and-empty — which after-read (b) has to prove. The JSON said `''`. I flagged it before
applying and measured it after.

**What failed:** nothing.

**Gap found:** none new.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Ledger, then the union at `15:02:57Z` | **60 trees** (enumerated 60 == grepped 60), 32 ticket rows, 10 distinct; only this entry open, the other nine closed by my own commits today |
| 1 | STOP 1 — **before** my own edit | 0 changed paths vs a **93** control; 0 dirty; shipping handler `c4003667…` |
| 2 | STOP 2 + BEFORE | live member `dc0cd973…` (my R3-rf-2 build); 8 env keys recorded as name + **length + sha256**, no value printed for any key; `PACKAGE_ALLOWED_FIRMS` confirmed absent |
| 3 | **THE ONE EDIT** | `e9357d6ea0` — one file, 6 insertions; line 258 verified by reading, not by trusting the stated number |
| 4 | Build + upload | version `zNRLtm_x…`, downloaded back: 1 member `c4003667…`, no `tests/` |
| 5 | Plan, then ONE safe-apply | `0 add / 1 change / 0 destroy`, one resource, **one** env key added, 8 unchanged |
| 6 | Five after-reads | all pass — see Verification |
| 7 | RECORD + STOP 3 | `6f2182e539`: map entry **and** reconcile line in one commit |
| 8 | AC1 on the new build | `READ27 27/27`, `c4003667 CLAMPED` |
| 9 | Close, proof, flip, log, report | ledger 7/7; proof in the deliverables **root** |

## Verification

```
(a) CodeSha256 d2w1YJ8AU7vvBufCXNvBcL/wXYAlNWbY3o85l6z0Qps= == uploaded zip
    deployed package re-downloaded: 1 member, c40036677aae180cb362f89f2c2aecb62ef53fd0b1a285bb3bd2c813176c1026
    LastModified 2026-10-11T15:18:51Z | runtime/timeout/memory unchanged

(b) THE ENV -- the read this order turns on:
      key COUNT before/after      8 / 9
      ADDED ['PACKAGE_ALLOWED_FIRMS']   REMOVED []
      the 8 OLD values, by sha256       8 of 8 identical
      PACKAGE_ALLOWED_FIRMS  PRESENT: True   LENGTH: 0   == ""
      sha256[:16] e3b0c44298fc1c14  (the hash of the empty string)
    -> present-and-empty, NOT dropped. The door admits NOBODY.

(c) POST .../package -> 401   POST .../report -> 401
    control GET /api/scoped/tickets -> 401 (proves reachability, and only that)

(d) ItemCount 25, TableSizeBytes 31538 unchanged; control ticket 23/23 identical

(e) No changes. Your infrastructure matches the configuration.

STOP 3 -- both halves in ONE commit 6f2182e539:
    map entry artifact_sha256 d2w1YJ8A... == live; stamped 596aaed93a; 15:23:40Z
    reconcile line appended (+1); CHANGELOG 42 lines; three files, its pathspec
    235 entries before/after, 0 added, 0 removed, 1 CHANGED (counted)
    stamped 596aaed93a's handler == c4003667... == the deployed file
```

---

## Decisions Made

1. **Did not pick the list's value.** The packet offered branch L (three firms) and branch E (empty) and
   said the CTO names one. It named **E**, and signed "for BRANCH E ONLY". I added no firm — a list with a
   firm in it is outside this order. The CTO's reason is worth keeping: the list is an authorisation and is
   decided where the identity it authorises is decided, and an empty list is a narrowing against today for
   every possible caller, so this deploy cannot widen anything.
2. **Resolved `null` vs `""` by reading the planfile, not by reasoning about Terraform's display.** Then
   measured it after the apply. Flagging it *before* applying is the part that mattered.
3. **Verified the insertion point by reading main.tf** rather than trusting "line 258". It was 258.
4. **Added zero non-ASCII** to a file that already carries 19 em-dashes, and stripped none — CLAUDE.md
   allows all-out or every-reader-explicit, never a subset, and a full strip is out of scope here.
5. **Left the pre-existing `terraform fmt` drift alone** after proving it exists at the pin. Running fmt
   would have pulled an unrelated line into a commit the order says is one file, one change.
6. **Hashed every env value rather than printing any.** The order forbids echoing `TICKET_DL_MAP` and
   `CLIENT_LINK_MAP`; a length plus a hash answers the after-read for all eight without carrying any of it.
7. **Ran the mis-stamp content read the order doesn't ask for**, for the third time in this series.

---

## Files Modified

| File | Commit |
|------|--------|
| `infra/aws/terraform/ticket-center/main.tf` (the one edit) | `e9357d6ea0` |
| source map, reconcile audit log, `CHANGELOG.json` | `6f2182e539` (by the recorder) |
| ledger + row, proof_of_spec, AC1 table, this log, TO status | this commit |

---

## Blockers

None owed by this seat. **One asymmetry to carry:** this deploy's rollback is **two changes, not one** —
the order words it as re-applying the `8ef21584f8` build *with the env line removed*. Re-applying the
artifact alone would leave `PACKAGE_ALLOWED_FIRMS` present-and-empty against code that ignores it. Harmless,
but a future rollback should not be attempted as a single artifact re-apply.

Carried from R3-rf-2 and still another seat's: row **S40**, the creator's unbound write, until
`2.0.0_SA_COO~Y2`'s binding cell lands.

---

## Current State

The package door reads an env firm list and the list is empty, so every firm is refused and no identity
exists to try it. The door's five coded 409s, its 200 body and its conditional write are **UNEXERCISED**
and stay so until the packager's first real attach. The two new creator codes are **APPLIED, UNEXERCISED**.

Whether a users row or credential exists for `svc-irpt-packager` is **NOT DETERMINED** — the issuer's read
failed its own control and said so, which is the right way to report a blind instrument. CTO condition 2
routes that read to IRPT_YCDGEN's attach cell, before the mint's pair is written.

---

## Next Steps

1. The pair that mints the packager's token: it names the firms and sets this list in the same act.
2. IRPT_YCDGEN's attach cell answers the `svc-irpt-packager` existence question with a working control.
