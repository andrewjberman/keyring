# /self-drive ticks 13-17 -- **two rulings, both VERIFIED AS EXECUTED**, and both lanes did better than the bounds I wrote

**Seat:** `1.0.0_SA_CTO` · laptop · CLOUD · **UTC** 2026-09-21 ~09:0xZ
**Arming record:** `ANDREW_DIRECT_20260921_005xZ_...md` @`07b8a03ec3`, §8 @`57751941a0`
**State:** ARMED · cadence 30m · job `a18b29c0`

---

## 0. HEADER FIGURES -- EACH FROM A CALL IN THIS TICK

| figure | value |
|---|---|
| `MDPF_TAXSMA` | **16 open of 27** (11 complete) |
| `NFRA_MCPINDEX` | **32 open of 38** -- ⭐ **NO over-count this tick, and I checked WHY** (§3) |
| live COO lanes / cap | 3 / 3 · unread **0** · both `EXECUTING`, flags `-` |
| disk (tick 15) | 34.56 GB free, two instruments agreeing |

## 1. `MDPF_TAXSMA` W2-S1 RULED @`5eef9bd41d` -- and the pair with `MX-c-1` is the keepable

`TXA1-AC2` names four levels; the script carries no SMA/ALT series. **Reading ACCEPTED** -- the
one-identity reading on Tax's single registered path is the only one satisfiable inside the cell's `<paths>`.

⭐ **THE MIRROR-IMAGE PAIR, FOUR HOURS APART, AND BOTH WORKERS GOT THEIR HALF RIGHT:**

| | situation | response |
|---|---|---|
| `MX-c-1` | the criterion **could not** run without writing outside the grant | **REFUSED**, filed a row |
| `TX-a-1` | the criterion **can** be graded inside the grant under a defensible reading | **PROCEEDED WITH DISCLOSURE** |

**THE DISCRIMINATOR IS WHETHER A READING EXISTS THAT SATISFIES THE CRITERION WITHOUT LEAVING THE GRANT.**
**Neither chose silently** -- the half that made both catchable.

**The field `aua_including_tax` is BOUNDED, not blessed:** a computed intermediate, 0 occurrences in a
43,127-byte contract (four positive controls present in the same read). It breaches no letter **provided it
never crosses the response boundary** -- and **becomes a second enumeration IN FACT the moment anything
publishes or depends on it.**

⚠ **I NEARLY RULED A BREACH AGAINST A PARAPHRASE.** The vocabulary bound did not appear on my first grep --
which had a **240-char cut**, the same truncation class convicted two hours earlier. Read in full at source
(order `:22`, PRD `:99`), `2.0.0_SA_COO~T` had **quoted it accurately.**

## 2. ⭐ BOTH LANES EXECUTED BETTER THAN MY BOUNDS, AND BOTH TIMES MY BOUND UNDERSTATED THE SURFACE

**Bound (4), mine: "a comment at its definition."** `2.0.0_SA_COO~T` measured **TWO definition sites** (the
49financial overlay and `apply_tax_to_global`) and marked both, *"a comment at only the first would have left
the Global site carrying the field unmarked."* **VERIFIED AT HEAD: 2 markers at `:3126` and `:3198`, each
directly above an `aua_including_tax: list = []` declaration.** ⛔ **MY BOUND SAID "ITS DEFINITION",
SINGULAR -- I SPECIFIED A REMEDY FROM AN ASSUMED SHAPE WITHOUT MEASURING THE ACTUAL ONE.**

**The `MX-c-1` bound, mine: "post-revert diff ASSERTED empty for both paths."** Read in full from the proof
(⚠ my first read truncated at 900 of 1,519 chars and I re-read rather than concluding):
- pre-exercise `git diff --stat` **empty on both**, original bytes saved with sha256;
- RUN A baseline → RUN B with a **byte-exact reversible insert at a named offset** → **RUN C on the reverted
  input returning RUN A's EXACT sha**;
- revert by **explicit byte-for-byte write, never `git checkout --`**;
- **POST-REVERT `git diff --stat`: `CAT='' RECT=''` (both empty).**

⭐ **RUN C IS A THIRD ARM NEITHER AC4 NOR MY BOUND REQUIRED** -- it proves the writer is deterministic on the
restored input, not merely that the diff is empty. **Two arms show a fix works; only three show the guard is
load-bearing**, applied by a worker unprompted.

## 3. ⛔ THE OVER-COUNT VANISHED -- AND I CHECKED WHETHER THAT WAS A FIX OR A SUPPRESSION

My own prompt warns that `_proof_terminal` **REFUSES when worktree and HEAD differ, suppressing the note**,
so a vanished note is NOT evidence of a fix. **Measured: `MX-c-1` now reads `<status>complete` at HEAD** --
the order is genuinely terminal, so the predicate does not run. **Not suppression.**

**And terminality reads the PROOF, so I read it: 6 PASS + 1 UNVERIFIABLE-BY-INSTRUMENT (`AC7`, the judgment
criterion for L9). `AC4` is PASS.** ⭐ **THE W1-S1 RULING CLOSED ITS OWN LOOP** -- grant amended to exactly
two paths → criterion exercised → PASS → terminal. **So `NFRA_MCPINDEX` 32 of 38 is an HONEST figure this
tick, the first since the L6 issuance that needed no over-count caveat.**

## 4. `NFRA_MCPINDEX-W4-S2`: THE DISARM IS VERIFIED AND UNRECORDABLE @`ccf51f6e47`

`2.0.0_SA_COO~M` filed a real drain loss (a merge named the worker commit as a parent; first-parent diff 1
file against the branch's 6; four deliverables absent at CLOUD, unrecoverable by any later merge).
`3.0.0_SA_CVO` **verified rather than took it**, then re-verified inside the write behind a guard.

⛔ **MY GATE THEN REFUSED THE CLOCK** -- *"NEW remediation row (the slug ...) while 33 of 38 task orders are
NOT terminal."* **A disarm clock is not a slug**, and the repair had already landed. **So the word lived in
three places a register cannot see** -- the G-C failure exactly. **This record is the carrier**, by the
precedent set at 01:0xZ: the row stays, the decision is recorded in a deliverable, the overstatement is
disclosed. **And the RELAY was the act** -- the CVO's lane permits one recipient, so the owner could not hear
it from that seat.

**`S149` now spans TWO PROJECTS AND TWO ACT-KINDS** (a slug in `LGIC_ENFORCE`; an R-15 clock here).
⭐ **A PROXY MERELY TOO WIDE ON ITS OWN ACT BECOMES A GENERAL REFUSAL ONCE OTHER ACT-KINDS SHARE ITS
CARRIER.** Still not patched -- it errs toward REFUSING, the safe direction, and `3.0.0_SA_CVO` declined the
audited override for the right reason: **overriding a correct-in-direction gate to land a convenience is the
trade this estate refuses.**

## 5. AFFIRMED, NOT DECIDED: `TX-r-2`'s BLAST RADIUS

A `TX-r-2` release cut from CLOUD after `MX-c-4`'s drain **carries `MX-c-4`**, so G-W's blast radius must
name it. ⭐ **Never-class, not a courtesy: a release from a shared branch carries EVERYTHING that landed on
that branch, not only the cell's own diff.** As a G-W co-signer I will refuse a half that does not name every
project in the release base at signing.

## 6. COMPLETION TEST

**NOT DONE -- 0 of 2.** Both `active`/`EXECUTING`, both **REACHABLE**, 0 UNREACHABLE. Open calls at Andrew:
**2**, unchanged and not re-asked. **No TO cut, no seat spawned, no apply** across ticks 13-17; the
no-new-seats hold is untouched. **Push state LOCAL** for `5eef9bd41d`, `ccf51f6e47` and this log.

## Compiler Tools

`_open_tos_for_project` (both roots) · `json` over two proof instances read **in full after a truncated first
pass** · `git show HEAD:` on contract, order and PRD with **full-line reads** after a 240-char cut misled me ·
a 5-token contract census with four positive controls · `git status --porcelain` to separate a real
terminality change from a worktree-suppression artifact · `Get-PSDrive`/`Get-Volume` with an agreement test.
