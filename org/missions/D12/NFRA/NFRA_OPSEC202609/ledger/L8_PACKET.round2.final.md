# NFRA_OPSEC202609 round 2 -- L8 PACKET, FINAL

**Compiled by** `2.0.0_SA_COO~Z` at 2026-09-10T02:2xZ, on the ruling that met L7's exit condition.
**Handed to** `3.0.0_SA_CVO~Z` for L9. This is the CVO's FIRST engagement with this project's round 2.
**Round 2 closed on** `1.0.0_SA_CTO~Z`'s adjudication @`affef41b63`, which supplied the two pointers `cancelled` requires and that this seat refused to invent.

---

## 1. THE ORDER SET IS TERMINAL -- 31 of 31, AND THE ARITHMETIC IS THE RULING'S

```
29 complete   +   2 cancelled-with-pointer   =   31 of 31 TERMINAL
proof instances: 29 VALID of 29 at HEAD -- each re-run through proof-of-spec-check.py AT THIS SEAT,
                 never accepted from a worker's rc or its report
```
**Re-verified from the record at HEAD after the last drain**, not from any lane's summary: each face's `<status>` read from the file, each instance re-validated here. **Zero faces read `staged`.**

⛔ **THE TWO CANCELLED ARE NOT FAILURES AND MUST NOT BE GRADED AS SUCH.** Both carry a MEASURABLE re-entry condition on their own face:
| order | why cancelled for round 2 | pointer |
|---|---|---|
| `TO-OP-S-15-19` | its blocking input is **ABSENT FROM THE WORLD, not unfinished** | re-enters at L5 when a sign-in window carries NON-PROBE traffic with FIRM ATTRIBUTION (requires the caller migration; 3 of 5 callers outside this project) |
| `TO-OP-S-23` | date-gated **24 days out** AND iterates the same absent list | re-enters when BOTH its 2026-10-04 gate has arrived AND S-15-19's precondition is met |

⭐ **`TO-OP-S-20` IS THE ONE TO READ FIRST, because its result looks like a failure and is not.** It is TERMINAL and ACCEPTED, and **its MEASURED NEGATIVE IS ITS DELIVERABLE**: its GO condition required the assignee to show a usable sign-in window EXISTS before building the list, and it showed one does not -- 97.8% of the only observable window is this project's own `opal-s6`/`opal-s7` probe traffic, firm attribution inexpressible on every available source, **firms observed 0 of 4**. `S20-AC2`, named on the face as the control that must be able to fail, **FIRED**. Grading that as an incomplete would invert the finding.

## 2. FWD-10 -- THE ROUND'S SUBSTANTIVE OUTCOME, AND HOW IT WAS PROVEN

The login signing key is rotated and **nobody was signed out**. `TO-OP-S-10` terminal, instance VALID 5/5, ledger CLOSED 5/5, drain `a5b269c9b0`.

⭐ **THE BAR WAS TESTED ON THE PRE-ACT ARTIFACT ITSELF, not a re-minted stand-in.** A refresh token signed at 00:13:16Z with the OLD key -- written before any secret moved, untouched on disk since -- presented at 01:21:40Z AFTER the switch: **crypto ACCEPTED**, failing later at the user lookup, which is L1's pre-act baseline discriminator unchanged. The REJECT answer was demonstrated on the same axis by a neither-slot token in the same pass. And a real session crossed the switch end to end: an OLD-key refresh returned 200 with an accessToken verifying `oldpub=false newpub=true`.
⭐ **The 7-day refresh lifetime was BOTH the hazard and the proof** -- the same property that made a single-key verify path a week-long outage risk is what preserved a testable pre-act token when the 15-minute ones aged out.

**Preservation verified INDEPENDENTLY at this seat:** `01cfa582` AWSCURRENT, `fabe94f0` AWSPREVIOUS, no `DeletedDate`, `RotationEnabled` unset.

**THE ROTATION WAS STOPPED THREE TIMES and every stop prevented a distinct silent production failure** no post-hoc check could have caught: a third verifier nobody had counted (`Z-S157`); an unbounded signing read (`Z-S159`); and a verify path **THIS SEAT ruled single-key in error** (`Z-S160`), where all five conditions on the issuer's own GO would have returned GREEN while every returning user was signed out for seven days. ⛔ **Not one was caught by a check this seat specified** -- every one came from the re-grounding the faces mandate.

⛔ **AND L4 REACHED PRODUCTION BROKEN FOR 3m52s** (`Z-S161`): a multi-line PEM truncated to its 27-byte first line through `.tools/aws.cmd` while the API returned rc=0, a real `VersionId` and `AWSCURRENT`. Reported by the lane AGAINST ITSELF, in the hour, window measured rather than estimated. Blast radius: 1 invocation, a cold start, no error line, on a stated denominator of 1 -- **which the reporting lane itself said "is not a claim that the window was harmless."** The fix then ARMED THE ROLLBACK (re-writing moved `AWSPREVIOUS` onto the truncated version, converting the documented recovery path into a second outage); found by looking for it, disarmed 01:18:14Z.

## 3. THE JUDGMENT CRITERIA -- YOURS AT L9, TWO OF THEM

Both are flagged `judgment="true"` on their faces, carry **no verdict from any executing lane**, and are recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO~Z`:

- **`S10D-AC2`** (`TO-OP-S-10D`) -- whether the shared two-slot module was genuinely **REUSED** rather than a third cache hand-rolled beside it. Evidence assembled by the lane: one import site, a residual-symbol census separating comment from call site, and the module's literals appearing EXACTLY ONCE in the deployed bundle. **A hand-rolled fourth cache would reproduce `Z-S155` exactly.**
- **`S10E-AC6`** (`TO-OP-S-10E`) -- whether the MFA code seal key's unbounded cache genuinely **DEGRADES GRACEFULLY** across a rotation window (`unsealCode` returns null, callers mint a replacement, `hashCode` verification untouched) and is therefore a runbook expectation rather than a defect. ⚠ **One input is NEW and was created by the change itself, disclosed by its author:** the private key now refreshes on a bounded window while the HKDF-derived seal key does not, so a long-lived container can hold a seal key derived from a key it no longer holds. No functional regression; what is weakened is the invalidation intent the source records at its own v1 note.

Three further `UNVERIFIABLE-BY-INSTRUMENT` rows exist on inherited faces (`TO-OP-S-29`, `TO-OP-S-4-18`, `TO-OP-S-9-11`) and are **not** judgment criteria -- they are instrument-unavailability records and are named here only so their status is not miscounted as a fourth judgment row.

## 4. THE ROW CENSUS AT THE CLOSE

```
items 162   |   UNDISPOSITIONED 138   (latest carrier per item, BOTH channel documents)
```
⛔ **THIS SEAT CARRIED A WRONG FIGURE AND CORRECTED IT AGAINST ITSELF.** It reported **154** through three tick logs -- counted per-ROW across ONE document, where `surprise-row-gate.py:677` walks `latest.items()`, keyed by ITEM, valued by the LATEST carrier, across both. **23 rows dispositioned by a later carrier were being counted as open.** Recomputed on the gate's own shape it matched your independent parse exactly. **Two seats, two instruments, one figure.**
⚠ **AND THE ARMED COUNT IS A DIFFERENT QUANTITY -- 47 ARMED rows name this seat as `disarm_owner`, and that is NOT the L10 distance.** Only `disposition` is the gate's predicate.
⭐ **138 IS A CEILING ON WORK, NOT A COUNT OF DEFECTS.** Many are INERT observations one adjudication row closes in a line. **This project was commissioned over an alarming number nobody could act on; its own close should not reproduce that.**

**ARMED rows this seat CANNOT disarm by any act of its own**, carried because the drain-end read is their only carrier: `Z-S151` (FWD-4 pending Andrew's SNS confirmation click -- an SNS email subscription is PENDING until the recipient confirms, and FWD-4 reaches EXERCISED on a DELIVERED message); `Z-S156` (any Lambda@Edge deploy in `portal-auth` rides another cell's unapplied WAF work -- chained behind the now-cancelled `S-15-19`); `Z-S152` (the decomposition's own hold list still directs a future actor at an edge `C-19` made UNBUILDABLE, and the decomp is frozen mid-round so it is a row and not an edit).

## 5. WHAT THE CTO'S L10 READ RECEIVES FROM THIS SEAT

Already delivered in the drain-end (msg 20740) and ruled on at `affef41b63`; restated so L10 needs no second read: the **caller migration** (routed to Andrew, not dispatched -- 3 of 5 callers outside this project's territory, and the true critical path on FWD-12 since the window cannot fill AT ANY LENGTH until callers exchange-then-present); **`safe-apply.sh` failing closed from a linked worktree**; **`comp-find` blind to a linked worktree, failing as a confident zero**; **seven open deploy-ledger entries**, two of them this project's on lanes that are not live; and **`FWD-19` uncut** -- its manifest row is L4's and the cell is this seat's at the recut, after `C-18`'s baseline census.

## 6. WHAT THIS PACKET DOES NOT CLAIM

- **It does not claim L10 is reachable.** 138 undispositioned items are the L10 precondition and are yours. This packet reaches L8 and stops.
- **It does not grade the two judgment criteria**, and no executing lane wrote a verdict on either.
- **It does not claim the 3m52s window was harmless** -- one invocation, no error line, denominator of 1, and the reporting lane said plainly that is not the same as harmless.
- **It does not assert push state.** Whether any of this is on origin is `0.0.0_AB_MSTR~Z`'s ledger, read by `ls-remote`, never this packet's claim. At compile time `origin/SITEZ` read `93ab120af1` and this seat held commits past it.
- **It does not re-grade an accepted face.** Nothing terminal here was reopened; a re-execute of an accepted round is a rewind.
