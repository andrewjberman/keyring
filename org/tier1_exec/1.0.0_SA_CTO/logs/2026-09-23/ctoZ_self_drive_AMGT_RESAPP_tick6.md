# /self-drive AMGT_RESAPP -- log covering ticks 5-6, 2026-09-23

**Arming record:** `ANDREW_DIRECT_20260923_193xZ_SELF_DRIVE_AMGT_ALL_THREE_CLOSER_LOOPS.md` @`a8a62f4f5c`.
**state: ARMED** · 30m · cron `a6c97d57`. Previous log: ticks 3-4 @`a762d35088`.

## THE HEADLINE: THE SERVED-OUTPUT INCIDENT'S GUARD HALF IS CLOSED, MEASURED LIVE

**179 sentences served in violation of `C-VERBATIM-GATE v0.12` are now HELD on the deployed plane.**
12 of 12 securities by direct invoke against the real S3 data plane: **210 served / 179 held_no_span /
389 total / 12 of 12 HTTP 200 / SPANLESS SERVED = 0 on every one.**

⛔ **AND THE INCIDENT IS NOT CLOSED. C4 DISCHARGES THE GUARD HALF ONLY.** `ADJUDICATION_v45` classified
this an INCIDENT, not an exposure, and Rule 22's negative mirror makes an incident's remedy **DOUBLE**:
build the guard AND re-open what the gap admitted. `v46` amended the blast radius **UPWARD** -- the
authorizer accepts ordinary verified portal JWTs, so those sentences reached a **SERVED** audience.
Nothing yet addresses the window opening at/after 2026-09-19. **That half is `3.0.0_SA_CVO~Z`'s.**
⭐ **CLOSING THE GUARD AND CLOSING THE INCIDENT ARE TWO DIFFERENT FACTS, AND A GREEN DEPLOY IS EXACTLY
WHEN THE SECOND ONE GETS LOST.**

## THE DEPLOY, AND THE TRAP IT AVOIDED

**C1 was the blocker and it was a NEVER violation that SELF-REVERTS.** `opal-amgt-scoped-api` is
Terraform-managed and **the artifact of record is the S3 object, not the function's code**, so changing
the function without changing `research/opal-amgt-scoped-api.zip` would have left the next
`terraform apply` on the harvest stack -- for any unrelated reason -- silently restoring the defective
package. Amendment 2 closed the deliberate rollback path; **this was the same class one plane out.**

**Two additions this seat measured on top of CVO's finding, both of which would have voided the
binding:**
1. **`build-and-upload-scoped-amgt.sh` IS A BUILDER, NOT AN UPLOADER.** It packages from REPO SOURCE by
   AST closure; `candidate.zip` came from the DEPLOYED BASELINE plus a two-function patch. Running it
   would have uploaded **bytes nobody signed.**
2. **Terraform reads the object's `content-sha256` METADATA as `source_code_hash`, not its bytes.** A
   correct byte copy with absent metadata leaves Terraform reading the wrong hash.

**Verified arithmetically with a negative control:** candidate's hex sha256 `0c44108821fe...`
base64-encodes to `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`, exactly the CodeSha256 required
afterwards -- so the pair's two numbers describe ONE object.

**Executed by `2.0.0_SA_COO~Z` at `895873fe4c`:** ledger `b0f33e7821` opened **21:52:56Z before any
cloud write**, upload verified three ways including independently downloaded bytes, baseline re-read
before upload AND after plan review, **`safe-apply` exit 0 -- 0 added, 1 changed, 0 destroyed**, and the
**untargeted post-plan at ZERO resource changes.**

**INDEPENDENTLY CONFIRMED AT THIS SEAT** (CLAUDE.md: never trust a producer's self-report on a served
artifact): live `CodeSha256 DEQQiCH+...`, `CodeSize 807904`, S3 `ETag cb90ed8636c79c9dbc29120923349bc5`
with matching `content-sha256` metadata. ⭐ **S3 LastModified 21:58:26Z PRECEDES function 22:02:35Z --
the artifact of record moved FIRST, so a future apply now restores the REPAIR.**

## BOTH GATES CLOSED; FIVE AMENDMENTS; THE BRIEF HALF NEVER MOVED

`7737` REFUSED (R5/R6/R7) -> `c851` REFUSED (R8) -> `73e3` SIGNED -> `4efe` SIGNED (4a) -> `fa42` SIGNED
(4b). **Brief half byte-unchanged at `12aa73e8bb31` throughout, so `4.0.0_SA_CRO~Z`'s signature was
never once re-opened.**

**THE SAME GAP CLASS THREE TIMES, and it is the session's most reusable finding:**
- **R5** -- clauses named the enum and were silent on the READER: relabelling would have reported an
  uncovered window as `complete=True` for **1,595 of 1,596 rows**.
- **H-a** -- clauses 1-4 named the COUNTER and were silent on the SCORE: those days would have been
  **removed from the `counts` series entirely.**
- **clause 6** -- clauses 1-5 named the FUTURE and were silent on the RETAINED CORPUS: a literal
  implementer would have destroyed the migration invariance **while passing every test.**

⛔ **A CONTRACT THAT SPECIFIES ONLY THE FORWARD PATH LEAVES THE EXISTING CORPUS TO THE IMPLEMENTATION.**
And R5/H-a are one class from opposite sides: **R5 served a silent CLEAN READ, H-a a silent GAP.**

⭐ **THE FIX CAME OUT STRONGER THAN CONFORMANCE:** `DENIED` and `NO_COVERAGE` now produce IDENTICAL
`states`, `counts` and `complete`, so **the 1,595-row relabel is a NO-OP for every caller.** Both
findings close **PERMANENTLY rather than conditionally** -- a reader that cannot tell the labels apart
has no transition to get wrong.

## THREE CONTROLS ADOPTED FROM `3.0.0_SA_CVO~Z`

1. **ZERO-DELETION as the additivity proof** (`+37/-0`) -- mechanical, cheaper and stronger than
   re-reading. ⚠ **With its own bound, which that seat supplied unprompted: it proves nothing was
   REMOVED and says NOTHING about an addition that CONTRADICTS retained text -- R8 was exactly that
   shape. Both questions are owed.**
2. **ROW-BY-ROW over AGGREGATE.** Four per-security replay pairs reproduced EXACTLY on the live plane.
   **An aggregate of 210 could come from many distributions; four pinned pairs could not. The aggregate
   is the weaker claim and it is the one usually reported.**
3. **SPAN FROM YOUR OWN STAMP, never the author's last commit** -- already banked, applied twice more.

## WHERE THIS SEAT WAS OUT-MEASURED, RECORDED AGAINST ITSELF

**The 401 control.** This seat probed the edge and got an IDENTICAL 401 on a nonexistent path, correctly
reporting that it shows only that auth fires before path resolution. At the Lambda, header PRESENT with
a bogus route returns **404, not 401** -- so the 401 is demonstrably about the MISSING HEADER. **Same
question; a control that actually discriminates.**

**And a near-miss of this seat's own:** `--is-ancestor` is DIRECTIONAL. Tested "is mine an ancestor of
CVO's", got False because mine was NEWER, read it as DIVERGENCE, and **nearly escalated a force-push
alarm** over a commit that was reachable the whole time. Banked.

## LANE STATE

`~Z` EXPERIENCE+RUNTIME: half signed, C1 executed, ledger closed. `~Y` HARVST: reader delta
`4dc4b667f3` PASS, clauses 1/2/3/5 MET, H-a closed; Price handback `1b6cd9d4e0` returned under R-9.
`~X` CORPUS: B08 `4599b05795` PASS, **stale-base qualifier DISCHARGED** by re-running at merged runtime
`30102a6905` for 216 PASS, with CVO verifying the ancestry and byte-identity that make the number count.

## COMPLETION TEST: NOT DONE

**0 of 3 D5 members `complete`.** `E0` and the live thread remain **UNGRADED** -- C4 was a BACKEND
acceptance by direct invoke, **not an authenticated browser trace**, and the API Gateway CUSTOM
authorizer was never exercised. Under CONTRACT s.2 LIVE FIRST, `H1`-`H4` and `C1`-`C3` stand
NOT_EVALUATED. **The single human-only item is unchanged: an authenticated tab-by-tab readout at
`localhost:5174`.** Playwright's context is clean-slate and lands on `/login`; MFA needs a person.

**PARKED** (`dc3f8a0b75`): two `opal_ai` items -- the RCN-0014 brief and Andrew's ~22:0xZ GitOps split
spec. His word went to `4.0.0_SA_CRO~X`, **not to this seat, and is not read as re-tasking it.**

## Compiler Tools

`prd_signoff_lib.half_hashes`/`top_sections` · `safe-commit.sh` (6) · `.tools/aws lambda
get-function-configuration` + `s3api head-object` (independent live verification) · native `Grep --glob`
for the blast-radius census · `git diff --numstat` for the deletion count · `merge-base --is-ancestor`
with both directions.
**Rail note:** a `comp-find` pathspec that matched nothing printed **`0 hit(s) across 0 file(s)
scanned`** -- **OUT-OF-CORPUS, NOT ABSENCE.** Reading that zero as an answer would have reported a blast
radius of nothing.

## NEXT

The incident's SECOND half, owed by `3.0.0_SA_CVO~Z`. `E0`, owed to a human sign-in. Nothing at this
seat is blocked-and-actionable.
