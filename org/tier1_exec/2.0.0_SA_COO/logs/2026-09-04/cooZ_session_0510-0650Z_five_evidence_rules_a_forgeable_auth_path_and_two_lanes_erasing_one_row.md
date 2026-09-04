# COO~Z session log 05:10-06:50Z -- five evidence rules, a forgeable auth path, and two lanes erasing one row from opposite directions

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Seat:** `2.0.0_SA_COO~Z` - **Project:** `NFRA_OPSEC202609` - **Limbs:** L5 + L6 - **Lanes:** 7. **Delta since `95fa110ea6`.** **Push state: LOCAL, not read against origin.**

---

## 1. LEDGER -- UNCHANGED AT ELEVEN, AND THAT IS THE HONEST NUMBER

**11 of 18 served** (`FWD-1,2,3,5,6,7,8,9,11,16,18`). **Cells: 35 -- 20 COMPLETE, 6 HELD, 5 OPEN, 1 PARTIAL, 3 CLOSED.** Six cells left HELD this window; **no outcome flipped**, because the ones that moved were mid-chain rather than terminal.

**Every remaining outcome has a named reason and none is "nobody is working on it":** `FWD-4` waits on Andrew's SNS click - `FWD-10` the rotation has not run (both blockers now discharged) - `FWD-12` a 5-caller observation window that is multi-session **by construction** - `FWD-13` two items with Andrew - `FWD-14/15` the BLOCK arm chained behind an allow list that **cannot be built** - `FWD-17` the reconciler and unblock path, in flight.

## 2. `Z-S136` CLOSED ON THE AXIS THAT MATTERED

**The fix committed @`3758b14afc`, 4 of 4 sets, verified AT HEAD via `git show HEAD:` rather than a working copy** -- a guard living only in a worktree protects nobody planning from HEAD.

⭐ **AND THE STATE-AXIS GAP WAS NAMED BY A SEAT AGAINST ITS OWN EARLIER VERIFICATION: `ignore_changes` IS A PLAN-TIME DIRECTIVE, SO A CLEAN PLAN IS WHAT A CORRECT GUARD AND A SILENTLY-FAILING GUARD BOTH PRODUCE.** Two seats had verified it independently and **both were DESIRED-plane**. ⛔ **I had banked the wrong proof method myself** -- "populate, re-plan, show no removal" -- **and corrected it: the proof is an APPLY.**

**The apply MODIFIED both sets and the addresses SURVIVED**, which is stronger than the skip I expected: **a skip is consistent with Terraform never reaching the resource; an active write that leaves the attribute intact shows the guard working ON it.**

**`OP-s-18` now RECORDS the defect its own artifact carried. `TO-OP-S-4-18` is NOT reopened** -- reopening an accepted certified round is a rewind; the repair lives forward as `S15-AC5`.

## 3. THE SECURITY FINDING, SIZED AND ROUTED

**`Z-S127`/`140`/`141`: a symmetric signing secret in cleartext Lambda env vars, FORGEABLE AND REACHABLE.** Validates AND mints, read in the **deployed bytes**; both functions carry a hardcoded fallback so an absent env var **fails OPEN onto a string committed in the repo**; not a JWT (two parts, no `alg`). **Six of seven routes bound to that authorizer; the seventh is the mint endpoint with no auth.** ⭐ **The 129-day-dormant authorizer WOKE on a probe -- 401 unauth, 403 on a junk bearer (it EVALUATED the signature), 404 control.**

**IT HAS BEEN SUCCESSFULLY AUTHENTICATED AGAINST** -- 18 ALLOW on one January day, **marked as an INFERENCE from two metrics rather than dressed as a log read.** ⛔ **WHETHER IT WAS ABUSED IS UNCOMPUTABLE: stage access logging was NEVER enabled, account-wide.** ⭐ **So the verdict is A FINDING, NOT A DEMONSTRATED INCIDENT -- AND NOT A DEMONSTRATED NON-INCIDENT.** *"No evidence of misuse"* would be literally true and would read as an all-clear.

**A FOURTH BRANCH the traffic shape opened: RETIRE THE API.** 272 lifetime requests, build-and-test in January, one burst in April, nothing since. ⛔ **Rotating spends a consumer census to preserve something that may have no consumers.** **The CVO added a SECOND read path -- Terraform state records the resolved value, needing no lambda permission -- so a remediation verified only against the Lambda config would PASS while state still carries it.**

## 4. TWO LANES ERASED ONE ROW, FROM OPPOSITE DIRECTIONS, WITHIN MINUTES

**Both disclosed immediately and precisely.** One overwrote a `notes` field from a **stale read**, having **printed the row's true owner and written anyway** -- an attention failure, not a knowledge one, and it said so. The other's exercise re-run **silently replaced the whole item** via `put_item` on the same key: **no error, no warning, no diff.**

⛔ **THE CAUSE IS STRUCTURAL AND IS MINE: `S19-AC2` MANDATES AN EXERCISE THAT DESTROYS THE OBSERVATION OF ITSELF.** It requires a real edge refusal; the only originating address is our own egress; the sentinel necessarily observes it; **the address IS the partition key.** **PROJECT RULE: no exercise may write a key a live system also writes, and `put_item` on a shared key is barred -- THE SILENCE IS THE HAZARD.**

⭐ **The evidence survived on a different store (case file intact), and the sentinel's independent observation of `BlockedIPs` firing is the strongest corroboration in the chain -- a SECOND system watching, which no single-face exercise could have produced.**

## 5. MY OWN ERRORS THIS WINDOW

- ⛔ **I RULED FROM A REPORT THAT WAS ALREADY FALSE.** "Leave the WATCH row, it is the strongest evidence" -- **it had been destroyed 90 seconds earlier.** I did not re-read the object before ruling on its disposition.
- ⛔ **I RULED FIVE TIMES INTO INBOXES while ruling that findings need durable carriers.** Fixed at `27dfb32ad2`.
- ⛔ **Then did it AGAIN twelve minutes later** -- made `RULE 1a` and let two lanes amend for twelve minutes without telling them.
- ⛔ **I accepted a better instrument and never said it could ENTER THE RECORD**, leaving it in two inboxes; a lane asked rather than assumed.
- **Corrected: my "breaks PERMANENTLY" on `session-analytics`.** Measured over 107 container lifetimes: **median 5.6 min, max 143 min** -- ⭐ **a PARTIAL, SILENT, SELF-CLEARING outage, which is WORSE because permanent breakage gets noticed.**

## 6. THE FIVE EVIDENCE RULES @`27dfb32ad2` + `f89dda7cbe`

**1** an accepted instance MAY be amended to carry a better instrument (verdict unchanged) - **1a** the note OPENS with `EVIDENCE AMENDED, VERDICT UNCHANGED:` or `VERDICT REOPENED:` - **2** writer-scoped beats global - **3** forward pointers on superseded proofs - **4** the STALE-PROCEDURE test - **5** no exercise writes a live system's partition key.

⭐ **Rule 4 came from a worker and is sharper than my ruling: a stale STATE misleads a grader; a stale PROCEDURE RECRUITS THE NEXT ACTOR INTO A FORBIDDEN PATH.** ⭐ **Rule 1a came from the CVO: an amended instance and a partially-disarmed row are ONE reading problem in two artifacts, and the estate already solved it with a CONVENTION rather than a schema change.**

**PROOF SWEEP: 23 of 23 instances, 129 of 129 limbs, 3 STALE-BUT-SOUND, 0 ACTUALLY-UNSUPPORTED** -- the six I accepted survive. ⭐ **35 screen candidates, all read individually, ~two thirds innocent: a screen is a filter, not a finding.**

## 7. NEXT

**`/open-calls` put THREE decisions to Andrew** (the `/wp-admin` control, the trade pipeline's future, the apex) **plus two acts he already approved** (the SNS click, the GoDaddy CNAME). **At L4: C-4's premise, C-2's wording, `Z-S127`'s placement -- all with measurements, none blocking.** **`TO-OP-S-23` unstartable before 2026-10-04.**
