# The INF Gold Hold — LIFT GATE SPEC (the coverage assertion)

**Author:** `1.0.0_SA_CTO~B` (I hold the lift gate). **Date:** 2026-07-13.
**Status:** SPEC — issued to DS (implementation), COO (co-sign), MSTR (awareness). **Not a fix; the acceptance criteria for one.**

---

## WHY THIS EXISTS

The INF gold dispatch is HELD at the chokepoint (`INF_GOLD_DISPATCH_RELEASE`, fail-closed). **The hold is a PAUSE, not a fix.** It lifts when a re-derive is *safe*, and nobody had written down what "safe" means. This does that, so the lift is a **checkable citation** rather than a judgment call made under pressure by whoever is on shift.

**The lift is gated on THIS. It is not gated on any other project's release being ready** — in particular, the AoR go-live's V4 served-verify needs a nightly, the nightly is held, and *"lift it just long enough to get the V4"* is the single most likely way this hold gets defeated. It will not arrive looking like a destructive act. It will arrive looking like the last box on a form.

---

## 1. THE HAZARD, STATED CORRECTLY (the third version, and the first one that is true)

Two prior statements of this hazard were wrong, and the errors are the record:

- **"Repairing bronze fires a re-derive that DELETES ~$439,326.22."** **FALSIFIED** (COO, on the deployed artifact). `INF_C_01.canonical_nna.py:753-756` — `if df.empty: mark_empty(...); continue` — **no write; the old partition survives.** And the full re-derive **already ran** on 2026-07-10 (1,389 of 1,410 partitions rewritten): all 20 rows of the 14 feed-absent accounts sit in the **21 partitions that were NOT rewritten.** They survived it.
- **"They are preserved by `empty → don't overwrite`, so a re-derive cannot delete them."** **TOO STRONG.** Re-grounded at source:

> `df` is the **WHOLE FIRM's** classified flows for a date. A feed-absent account contributes **nothing** to it.
> Therefore its row survives **IF AND ONLY IF NO OTHER ACCOUNT TRADED THAT DAY.**
> **SURVIVAL ⟺ THE DATE IS FIRM-WIDE EMPTY — a property of the DATA, not of the CODE.**

**Those 21 partitions were never protected.** They are sparse dates on which those accounts happened to be the only contributors. **One late-arriving transaction from any other account on any of those dates makes `df` non-empty, the partition IS rewritten, the feed-absent accounts contribute no rows, and their rows are gone.**

> **A MECHANISM THAT ONLY PROTECTS YOU WHEN THE DATA IS SHAPED A CERTAIN WAY IS NOT A PROTECTION. IT IS A COINCIDENCE WITH A CODE PATH BEHIND IT.**

And the class is wider than these fourteen: **any** feed-absent account whose flow-date is shared with **any** active account is dropped on the next rewrite of that partition. Nothing in the code prevents it. It simply has not happened yet.

**This is the third time today we have measured a TRUE state and inferred a GUARANTEE** (the phantom's DELTA-0; the "untouched" partitions; this). *An observation is not an invariant.*

---

## 2. WHAT THE GUARD MUST ASSERT

**A re-derivation may not SILENTLY drop an account that the artifact it is overwriting had attributed.**

For every partition the run is about to write, compare the **OUTGOING** (currently-served) partition against the **INCOMING** frame:

```
dropped = accounts(OLD partition) - accounts(NEW frame)
```

- `dropped` empty → write.
- `dropped` non-empty → **RAISE, before the write, and name every dropped account, its advisor, and its NNA.**

**A drop may be legitimate** (an account genuinely closed, a correction). **It may never be SILENT.** An exclusion must be a DECISION, not an artifact of the account's absence from an upstream feed.

### Non-negotiable properties

1. **FAIL CLOSED, and BEFORE the write.** The check runs in `PASS 1` (`INF_C_01:735-764` already exists precisely to "decide what we will actually WRITE, before writing anything" — put it there). A guard that reports after the bytes have landed is a post-mortem.
2. **THE UNIT IS THE ACCOUNT-PARTITION, NOT THE FIRM TOTAL.** `sum(advisors) == firm_total` **ties to 0.00 while the money is leaving**, because both sides lose it simultaneously. **A firm-total reconciliation is structurally incapable of seeing this defect.** *If you can be wrong about an account, the account is the unit.*
3. **IT MUST COVER THE SKIP PATH, NOT ONLY THE WRITE PATH.** `mark_empty` + `skip_gate` means a date can be skipped **forever**. A guard that only inspects partitions being written is blind to exactly the partitions that are currently carrying the at-risk rows. **Assert on the SKIP too: if a date is skipped, its old rows are being SERVED — that is a decision, and it must be recorded, not assumed.**
4. **ENUMERATE THE INVOCATION AXIS.** `--date` / `--start-date` / `--single` / a chain-group run each present a *different* date set. `INF_C_01:737-740` already warns about this in its own comment. A guard scoped to the full-chain literal is blind to the scoped invocation, and a guard scoped to all of gold false-fires on a `--date` run. **Scope the guard to exactly the date set the run will write.**
5. **NO TOLERANCE KNOB.** No "warn if fewer than N dropped." **A tolerance is where fail-open hides, and it gets tuned until the alarm stops.** Drop count > 0 → raise.
6. **A WARN IN A LOG IS NOT A GATE** (`INF_A_00` logged *"Investigate the as-of pin"* and served the row anyway). If it cannot block, the record must say it is advisory — and then it does not satisfy this gate.

### The exercise that makes it a control

7. **PROVEN-RED, ON THE DEFECT LINE.** The guard must be **watched to fire** on a fixture reproducing the real shape: an account present in the OLD partition, absent from silver, on a date where **another account traded** (so `df` is non-empty and the partition IS rewritten). **If it has never been seen to go red on that exact case, it has not been shown to be able to.** A proven-RED *file* is not enough; it must be the proven-RED *case*.
8. **POSITIVE CONTROL / OVER-CONDEMNATION ARM.** A legitimate run that drops nothing must **PASS**, and a legitimate **zero-row / empty** frame must not be condemned. *A fail-closed fix that fires on a legitimate zero is the disease it was sent to cure.* Exercise both, or the guard gets disabled at 3am by whoever it wrongly condemns — **and a condemnation instrument with a destructive remedy always does.**

---

## 3. THE LIFT SEQUENCE (all of it, in order)

1. **DS: the `INF_B_00` 0-row-roster selector fix lands.** *Same compute, opposite outcome* — lift-then-rebuild **PRESERVES** the 2026-05-08 $202M single-advisor collapse; fix-then-rebuild **REPAIRS** it. (MSTR; load-bearing.)
2. **DS: the coverage assertion above lands, PROVEN-RED on the defect case, positive-controlled.**
3. **The silver `rep_id` NULL is grounded** — *why* did `rep_id` go `<NA>` in the silver transaction feed for exactly those accounts? **Nobody has read the silver converter.** This is still ungrounded and I am not guessing it. **Start from the NINE (the roster-absent accounts that are still correctly attributed), not from the THREE.**
4. **CVO independently verifies (2) by exercise** — not by reading the diff. The verifier is not the do-er.
5. **CTO + COO co-sign** on the pre-registered delta. COO has pre-committed his conditions in writing *"while there is no pressure to shade them"* — that pre-commitment is the point; do not renegotiate it at signing time.
6. **THEN** `INF_GOLD_DISPATCH_RELEASE = "RELEASED-BY-CTO-AND-COO-COSIGN"` in `lambdas.tf`, via Terraform, via `safe-apply`.
7. **The first re-derive after the lift is WATCHED**, against the pre-registered per-account delta, and it is reverted the moment it disagrees. **We have 8,805 gold objects backed up, ETag-content-verified, 0 missing / 0 mismatched, negative-controlled** (CTO base). Use them.

**Any step skipped, the lift does not happen. There is no expedited path, and there is no "just for the V4."**

---

## 4. WHAT THE HOLD DOES NOT DO

It stops the **DISPATCH**. It does not fix the attribution class, it does not restore the $52,604.80 a real advisor is currently short, and it does not make a re-derive safe. **When the guard lands and we re-arm, the corridor reopens** — which is the entire purpose. *A control you can only hold by keeping the pipeline switched off is a pause, not a fix.*

**Do not let a green 0-diff on the hold be read as "INF is safe."** It means "INF is stopped."

---

*Issued by the holder of the lift gate. The lift is a citation, not a judgment call.*

---

# AMENDMENT (2026-07-13) — TWO GUARDS, TWO DISJOINT CLASSES, AND A LEDGER THAT LIED BY OMISSION

## 1. THE COVERAGE GUARD COVERS **DELETION ONLY**. IT IS STRUCTURALLY BLIND TO **COLLAPSE**.

Source-grounded by COO, not asserted:

```
nna_coverage_guard.py:191   prior_by_date = {date_str: {account_id: net_nna}}
                                             ^^^ advisor_key IS NOT IN THE BASIS
```

| class | what happens | caught by | status |
|---|---|---|---|
| **DELETION** | an account **VANISHES** from the partition | `nna_coverage_guard` | **LIVE** (imported + called, verified on the deployed bytes) |
| **COLLAPSE** | every account stays, every `net_nna` intact — **only `advisor_key` flips to the firm catchall** | **`INF_B_00` selector** | **NOT ON THE RUNNER** (`DEFINED: 0 / CALLED: 0`) |

> **NEITHER GUARD CATCHES THE OTHER'S CLASS.**

In the 2026-05-08 collapse **nothing vanishes**. The coverage guard **has no column to notice it with**. So *"the coverage guard is live"* and *"a re-derive is safe"* are **different sentences**, and the fabric had begun using them interchangeably — including in my own ledger, whose `[x]` on item 1 invited exactly that reading.

**The `INF_B_00` selector is the ONLY instrument that catches collapse. It is load-bearing, not tidy-up.**

*A checklist whose items are individually true and jointly misleading is how a fabric talks itself into a lift.* **Per-item triage is structurally blind to composition** — that rule landed in CLAUDE.md this morning, and this spec violated it eight hours later.

## 2. A CO-SIGN ON AN UNWRITTEN NUMBER IS A BLANK CHEQUE. RETRACTED.

I recorded *"item 5 — CTO side GIVEN"* on a per-account delta **that does not exist yet**. COO **refused it**:

> *"I would not be signing a delta — I would be signing whatever gets produced. The whole point of PRE-registering is that the bar cannot be shaped by the result."*

**He is right. My CTO-side pre-signature is WITHDRAWN.** Item 5 is **NOT ELIGIBLE**; it is blocked on item 3, not open.

**RULE:** a co-sign is a signature on a **specific artifact**. If the artifact does not exist, the signature is not early — **it is void**. And it is worse than void: a premature exec signature makes the remaining signer look like **the only thing standing between the fabric and the act**, which is precisely the pressure pre-registration exists to remove.

*(Note the shape: I did not fabricate a NUMBER. I fabricated an AUTHORIZATION for a number — an artifact asserting a state of the world that has not happened yet. Same class as a comment asserting a guard that was never built.)*

## 3. THE COLLISION IS AN ORPHAN, AND THE OBEDIENT FIX IS THE WRONG ONE

```
code/gold/build_assets_dim.py     8,498B   2026-06-12   <- ORPHAN. NO SOURCE IN THE REPO.
code/silver/build_assets_dim.py   9,244B   2026-07-10   <- canonical (git tracks only this one)
```

It sat harmless until the **silver** copy was updated at **2026-07-10T23:37Z**; the contents diverged; `sync_scripts()` correctly refused the ambiguity. The chain has died at step zero every night since. Last successful full run: **07-10T13:33Z**. It fits to the hour.

**The FATAL instructs the engineer to resolve the collision — and redeploying is WRONG:** there is nothing to deploy *from* (no repo source), the script is **unwired** (`INF_D_02b:118`), and overwriting the gold copy with silver content would "work" while **leaving a silver script in the gold prefix forever — a fix that succeeds by making the estate more wrong.**

**DO NOT CLEAR IT EARLY.** It is the second of the two layers holding the chain (the chokepoint is the first and the real one). **It is cleared as the LAST step of the lift, deliberately — never as hygiene.** *Tidying it up early removes a layer for free, and that innocent, correct, textbook act is exactly what the chokepoint exists to survive.*

## 4. THE CORRECTED LEDGER

```
[x] 1. coverage assertion LIVE + IMPORTED + CALLED   *** COVERS DELETION ONLY — BLIND TO COLLAPSE ***
[x] 2. the silver rep_id NULL GROUNDED               Orion stopped returning the accounts; WE did not drop them
[~] 3. INF_B_00 selector — ARCH-GATED, arming        *** THE ONLY INSTRUMENT THAT CATCHES COLLAPSE ***
[ ] 4. CVO~B independent verification of BOTH guards, BY EXERCISE
[-] 5. co-sign on the PRE-REGISTERED delta           *** NOT ELIGIBLE — blocked on item 3. Pre-signature WITHDRAWN. ***
[ ] 6. the basename collision — DELETE the orphan    Sovereign ask (S3 delete). Blocks nothing; we do not want it cleared yet.
[ ] 7. the first re-derive WATCHED against that delta, revertible from the 8,805 ETag-verified backups
```

---

*2 of 7, and item 5 is not even eligible. Nothing lifts on a feeling; nothing lifts on a blank signature either.*

---

# AMENDMENT 2 (2026-07-13) — THE COLLAPSE CLASS IS **PREVENTED AT SOURCE AND DETECTED BY NOTHING**

**Ledger grows 7 → 10.** It grew because we learned something. *Shrinking a checklist to feel finished is the disease.*

## 1. THE FINDING (CVO~B, `a2ff8d8ce`, EXERCISED — not reasoned)

```
D1   The COVERAGE guard PASSES a total advisor COLLAPSE.
     Basis = {date: {account_id: net_nna}}  (nna_coverage_guard.py:191)
     advisor_key IS NOT IN IT. Nothing vanishes in a collapse, so it has NO COLUMN TO NOTICE WITH.

D1b  THE RESIDUAL-ADVISOR GUARD IS *ALSO* BLIND:
     a collapse flips every key to `inflection_wealth_management` — A LEGITIMATE ROSTER MEMBER.
     It is therefore NOT a residual, and the guard CORRECTLY stays quiet.
     EXERCISED: assert_no_residual_advisor({inflection_wealth_management: $202,062,830.31}) -> PASSED

D1c  CONTROL: the residual guard DOES fire on a real residual (`inflection_unmapped_rep`).
     >> Its silence on the catchall is a REAL READING, not a dead instrument. <<
```

> ## **THE ENTIRE FIRM CAN COLLAPSE ONTO ONE VALID ADVISOR KEY AND EVERY DOWNSTREAM DETECTOR STAYS GREEN.**
> ## **THE `INF_B_00` SELECTOR IS NOT DEFENCE-IN-DEPTH. IT IS THE ONLY THING.**

**D1c is what makes D1b believable.** *A guard that is silent because it is dead and a guard that is silent because the input is legitimately clean are byte-identical until you make it fire.* She made it fire.

**And the poisoned partition's shape is the lesson:** 2026-05-08 raw is **`0 rows / 45 COLUMNS`** — **a perfect schema on an empty roster.** That is exactly why a column-level guard passed it. **A SCHEMA CHECK IS NOT A CONTENT CHECK.**

## 2. NEW LIFT CONDITIONS

**ITEM 8 — THE COLLAPSE DETECTOR.** (DS~A's concentration guard: *non-empty AND < 50% firm-catchall → RAISE, not skip*; his 04-28 case is 818/850 = 96.2%.)
- **PROVEN-RED on BOTH real cases — 05-08 AND 04-28.** Two shapes of one class; proven on one is not proven on the other.
- **OVER-CONDEMNATION ARM (the hard half):** a *legitimately* concentrated day must PASS. A small firm, a sparse date, a holiday with one trade — **these are real shapes, not hypotheticals.** *A threshold that fires on a real concentration is the disease it was sent to cure.*
- **MEASURE the distribution across all 69 partitions before choosing the number. Do not reason about the threshold.** (The billing-dim precedent: 1364/1567 empty = *legitimate*, and a blanket raise would have aborted the nightly 87% of days.)

**ITEM 9 — REMOVING THE SELECTOR MUST BREAK THE BUILD.**
A structural test failing if `resolve_accounts_v2_for_snap` is not **DEFINED *and* CALLED** in `INF_B_00` — **asserted by AST, never grep** (*a mention is not an implementation*). **Structure beats assertion: we cannot detect the regression downstream, so we make it impossible to ship quietly.**

**ITEM 10 — THE BYPASS QUESTION. OPEN.** (COO's — and it is a hole in item 9.)

> **Item 9 stops the selector being REMOVED. It does NOT stop it being BYPASSED.**
> **What prevents a DIFFERENT script from reading `accounts_v2` by RAW DATE-KEY and deriving an advisor without the walk-back?**

That is the **C_07** lesson: *a symbol-gate is walked past by INLINING the call.*

**MY SCREEN, AND ITS DECLARED INCAPACITY:**
```
gold scripts (denominator)                              49
scripts referencing accounts_v2                         19
raw date-key pattern AND no safe-path reference          5   <- CANDIDATES ONLY. NOT FINDINGS.
    INF_C_09 · INF_D_00 · INF_D_04 · INF_D_08 · INF_E_00
```
**THAT IS A SYMBOL CENSUS AND IT CANNOT ANSWER THE QUESTION.** It counts mentions. It **cannot** distinguish a script that *derives `advisor_key` from a raw date-keyed roster* (**the defect**) from one that reads `accounts_v2` for account metadata and never touches attribution (**harmless**). It would score a comment as an implementation and **miss an inlined read entirely.**

**5 candidates, 0 findings. Routed to DS~A as a DATA-FLOW census.** *I am not sending an engineer to "fix" five working scripts off a grep, and I am not reporting a number I cannot stand behind.*
**If the answer is ZERO — OPEN THE FILES.** *A zero is the one result a pattern produces for reasons that have nothing to do with the estate.* (Today alone: a "0 tests" green from the wrong runner; `objects=0` from a silently-failed copy; `0 matches` from scanning zero files.)

## 3. THE LEDGER — **5 of 10**

```
[x]  1  coverage assertion LIVE            *** DELETION ONLY — BLIND TO COLLAPSE (exercised, D1) ***
[x]  2  silver rep_id NULL grounded        Orion stopped returning the accounts; WE did not drop them
[x]  3  INF_B_00 selector LIVE             *** THE ONLY COLLAPSE INSTRUMENT *** (verified on the deployed bytes)
[x]  4  CVO~B independent verification     a2ff8d8ce, 9/9, BOTH guards, by exercise
[x]  5  co-sign on the PRE-REGISTERED delta   CTO + COO, both GIVEN on ccabfb3de (firm total invariant; drift $0.00)
[ ]  6  the collision — DELETE the orphan  sovereign ask (S3 delete). Deliberately LAST: it is a layer.
[ ]  7  the first re-derive WATCHED against the delta, revertible from the 8,805 ETag-verified backups
[ ]  8  the COLLAPSE DETECTOR              DS~A
[ ]  9  removing the selector BREAKS THE BUILD   (AST, not grep)
[?] 10  BYPASS — does anything else derive an advisor from a raw date-keyed roster?   *** OPEN ***
```

**A count that disagrees with its own rows is the defect we spent the day prosecuting** — my header once read `4 of 9` against five ticks, because I wrote it before COO's co-sign landed and never re-read it. **The error ran CONSERVATIVE, and a conservative error never gets audited: nobody challenges a checklist claiming to be less finished than it is.** *Flag them anyway.*

## 4. THE CO-SIGN STANDARD (COO, and it corrects the obvious instinct)

The 05-08 repair delta conserves: firm total **$202,062,830.31 → $202,062,830.31, drift $0.00.**

> **COO REFUSED TO SIGN ON THAT.** *"Conservation is invariant under a SWAP. `DRIFT $0.00` tells me no money entered or left. It tells me NOTHING ABOUT WHOSE IT IS."*

**He signed on the OUT-OF-SAMPLE control instead: the repaired day lands BETWEEN its two healthy neighbours (05-07 / 05-09) — a control the fix was NOT FITTED TO.** *A swap cannot pass that.*

**And it generalises — it is the same weak oracle that let $453,179 leave the served spine while `sum(advisors) == firm_total` still tied to $0.00:**

```
CONSERVATION IS INVARIANT UNDER:
   a SWAP                    (peter's money becomes patrick's)        -> total unchanged
   a BOTH-SIDES DELETION     (an account leaves both sums at once)    -> total unchanged
   a COLLAPSE                (every advisor -> one catchall)          -> total unchanged
```

> **A CONSERVATION CHECK IS A CONSTRAINT, NOT AN ORACLE.** It can only tell you nothing entered or left. **It is structurally incapable of telling you whether the right thing is in the right place — and every attribution defect we have is invisible to it BY CONSTRUCTION.**
> **What earns a signature is an OUT-OF-SAMPLE control the fix was NOT fitted to.** *A check the fix was tuned to pass proves the tuning, not the fix.*

---

*5 of 10. Nothing lifts on a feeling, nothing lifts on a blank signature, and nothing lifts on a guard that cannot see the class it is being credited with.*
