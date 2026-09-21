# /self-drive LGIC -- tick 74 (2026-09-19 ~06:4xZ-07:1xZ)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_052xZ_LGIC_GOAL_AND_30M_SELF_DRIVE_ADJUDICATE.md`
**Scope:** `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM`. **Device:** laptop. **state: ARMED**

## Sequence and scope

Clean; CAPACITY **AT CAP 3/3**. **2 open of 155** at write time -- **both rounds re-cut off my two L10 analyses**:
`LGIC_ENFORCE` r13 `EN-p-37-r13.the-placeholder-population-measured` @`c2865743ed`, `LGIC_LGCTFM` r5
`LT-m-2-r5.which-producer-writes-a-bucketless-key` @`44fc14c183` -- **the measurement cell my r4 analysis
specified, cut as specified.** ⭐ **LD-0521 ORDERING HELD AND I CHECKED IT RATHER THAN ASSUMING:** r4 analysis
@`abea09f936` 02:32:55-04:00, both issuances strictly after. **No deadlock inherited. COMPLETION TEST: NOT DONE
-- 1 of 4. No open calls in scope.**

## ⛔ THE CENSUS RETURNED A **NULL**, AND MY OWN READER WOULD HAVE PRINTED IT AS A ZERO

`_open_tos_census` returned `(None, 25, '...TO-LT-m-2-r5... unreadable at HEAD (ABSENT)')` for `LGIC_LGCTFM` --
`2.0.0_SA_COO~G` had the round-5 order **STAGED and uncommitted** (HEAD 24, worktree 25). ⭐ **THE TOOL IS
CORRECT: it HAS a not-evaluated value and it USED one.**

⛔ **THE DEFECT WAS THE CALLER'S AND THE CALLER WAS MINE -- six consecutive ticks printing `len(o)` with no None
check.** ⭐ **THE CRASH WAS THE LUCKY FAILURE.** The defensive form every instinct reaches for -- `o or []`, or a
`try/except` -- **would have certified "0 open of 154" for a project whose order set could not be read, WITH A
PRINTED DENOMINATOR, which is exactly the shape that reads as MEASURED.** The window is as wide as any L6
stage-then-commit gap, so any tick overlapping a round cut can land in it. **Filed `LGIC_ENFORCE-S97`, broadcast to
five seats** -- it binds everyone who certifies an L10. Reader corrected in this tick.

## THE ANDREW-DIRECT -- ~06:3xZ, relayed by `2.0.0_SA_COO~B` (`98154`, acked)

VERBATIM: *"i cant get to the console right now, i am remote. have an AE deal with it. if they cant for whateve
rreason, proceed and note it for later."* **No ruling asked.** I wrote **ADDENDUM 1** to my own `IB-rtf-5` CTO half
anyway, because a later reader holding his word beside my s.4 has a contradiction to resolve alone.

⛔ **THE READING IS MECHANICAL, NOT DEFERENTIAL: "proceed" CANNOT mean "apply without step 4", because the apply
CANNOT RUN without step 4.** The attached policy is the `W3-S43` lockout with an **empty** exemption list; only the
account **ROOT** can remove a policy that denies the account; root is **deliberately outside** the exemption set
(verified at HEAD: three IAM users, root absent). **There is no branch where the apply proceeds and something
different happens -- only one where it fails louder.** So his word means **the ROUND proceeds and step 4 is
PARKED** -- exactly how `2.0.0_SA_COO~B` executed it. **Ratified without widening.**

⚠ **THE PART THAT OUTLIVES THE MEASUREMENT:** his words are safe **today** only because the apply is impossible.
⛔ **The moment any identity CAN remove that policy, THE SAME SEVEN WORDS WOULD READ AS AUTHORISING AN APPLY
NEITHER HALF SIGNED.** Binding and free, because arm (b) already runs both reads: s.2 and s.3 stand; any route to
step 4 other than Andrew at the console is a **NEW REACHABLE STATE** returning to BOTH halves before the apply.

⭐ **AND A TRAP FOR ANYONE ANSWERING "who can do step 4?" FROM THE REPO:** `exemptions.json` lists three IAM users
-- **those are the exemptions of the policy the apply WILL CREATE, not of the policy attached NOW.** A reader
checking the registry reads **DESIRED** state and concludes three identities can act; the **APPLIED** state is the
empty-list lockout and none of them can. **Rule 22's STATE axis at its sharpest: the registry is not wrong, it is
answering a different question than the one asked.** Executed on the face by `2.0.0_SA_COO~B` @`49520a031a`.

## L4-R -- REFUSED AND RE-SIGNED INSIDE ONE TICK

`3.0.0_SA_CVO` **REFUSED** my v0.7 ratified-text half @`b24f18a197` on **ONE SENTENCE**, exercised not reasoned.
**The refusal is right and I did not argue it.** My clause said *"absence of the key is a backend defect, NEVER a
no-partial signal"* -- true of the response envelope, **FALSE of `refuse()`**, which omits the key by design.
⛔ **The sharpest case is the CVO's: a refusal whose `public_reason_code` IS `UNPROJECTED_GRANT` carries no
`unprojected_grant` key -- so a literal absence guard fires HARDEST on exactly the response the clause exists to
make visible.**

**Corroborated on a DIFFERENT instrument, not taken on trust:** the CVO exercised the functions; I read the source
at HEAD (`served.py:293-296`, `:310`; `enforce.py:41`, `:48`, `:92`). Execution and source agree.
**v0.8** @`927e9ce70e` scopes the guard to the envelope shape, names the refusal shape, states the rule as **BRANCH
ON THE SHAPE FIRST**, and records the two-shape split as frozen v1 design. **SIGNED** @`ac8bd5c426` /
`fa0eec1cd5`; **status now ADMITTED, measured** -- both halves SIGNED/current.

⚠ **AND THE ORIGIN IS MINE TWICE OVER:** the two-shape split exists **because of this seat's ruling
@`61627f39f9`** (`enforce.py:41`). **I wrote the ruling that made two shapes necessary, then wrote a clause
covering one of them.** v0.8 says so in its own body.

⭐ **THE CVO'S NON-GROUND NOTE IS WORTH MORE THAN SOME GROUNDS:** `count` is the **WHOLE** gap, not the unprojected
slice -- **the field's NAME is narrower than its CONTENTS.** ⭐ **Which is the SAME SHAPE I wrote up six hours
earlier about `UNDER_INVESTIGATION` in the r12 analysis: a name is not its semantics. Two seats, two surfaces, one
night, one class** -- and neither found it by looking for the other.

## `LGIC_ENFORCE-S98` -- a standing failure mode of THIS SEAT, filed as ONE row rather than three

**Three unconditional claims about a population having exercised ONE member, in about six hours:** the `scopes.json`
forward list (caught by `2.0.0_SA_COO~B`); `S95`'s *"nothing in the repo states that baseline"* with **no sweep run
at all**; and the v0.7 absence guard above. ⛔ **In all three the instrument I DID run was sound and its output
TRUE -- of the member I ran it on. What failed is the step where that became an unqualified statement about the
set, AND THAT STEP LEAVES NO TRACE IN ANY OUTPUT**, so re-running the instrument never catches it.
⭐ **THE TELL IS GRAMMATICAL, NOT NUMERICAL: NEVER / ALWAYS / EVERY / NOTHING / ANY in a sentence whose evidence
line names ONE object.** Offered to the fabric as a usable tell, not as an apology.

## RESERVED cards at Andrew -- five, all unruled

Step 4 now carries an **AE attempt recorded as tried-and-failed** rather than untried -- `IB-rtf-7` cut by
`2.0.0_SA_COO~B`, every profile tried, `AccessDenied` on each, the measured expectation. **Parked with an owner and
an un-park condition, never as a defect.**

## Compiler Tools

`sequence-check.py` - `surprise-row-gate.py::_open_tos_census` (four runs; **None-aware after the first**) - raw
3-tuple inspection - `git cat-file -e` / `git status --porcelain` / `ls-tree` (the staged-order discriminator) -
native `Read` + `Grep` on `_authz/` (the rail routes a compound `grep` on `infra/`) - `exemptions.json` principal
enumeration - `prd-signoff.py status` x3 (before, after-refuse, after-sign) - `safe-commit.sh` x3 -
`ack_messages` - `send_message` (5 recipients, 5 DELIVERED / 0 QUEUED / 0 REFUSED).

**PUSH STATE at write time:** LOCAL @`fa0eec1cd5`+; `origin/CLOUD` `ac8bd5c426` (`ls-remote` read). **state: ARMED**
