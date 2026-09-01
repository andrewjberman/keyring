# /self-drive D2 — tick 117

**Seat:** `1.0.0_SA_CTO` · **State:** ARMED · **Cron:** `e106e9c8` · **UTC:** 2026-09-01 ~13:4xZ
**Ticks covered:** 117 · **Carrier:** `org/XXX.md:633` @`e706f59f62` · **Paired:** `/drive` @ `2.0.0_SA_COO` (LIVE again)

```
COMPLETION: 2 of 10 -> NOT DONE            ledger: 34 -> 36
OPEN CALLS: 1 adjudicable + 1 RESERVED claim -> pitched @91567
VERDICTS: 2 landed (CVO 91590)             RE-CLASS COUNT: 1 of 1 reserved claims
register open_tos: 23 -> 19                (COO is back and closing)
```

**The all-RESERVED tell did NOT fire** — one card of each class. And the one reservation I did file was
**overturned**, which is the mechanism working exactly as Andrew specified it on 2026-08-27.

---

## CALL 1 — RIDE. And I did not decide it; a falsifier I published did.

I pitched RIDE with a REC, and I named the condition that would flip me: *"if ADVI_PERFRP's DONE
definition claims only that the figure EMITS and never that the weighting is CORRECT, DETACH is right.
**I DID NOT VERIFY THAT CLAUSE.**"*

`0.4.0_DS_ClientPlatform~G` read it and reported back inside 5 minutes, `DECOMP.md:71`:

```
  PRF-inv-3   parent $ = SUM child $ · parent denominator = SUM child denominators ·
              window % = geometric link of the PARENT daily return · NO SECOND COMPUTATION
  ORACLE      DS+DE - recompute each level from the level below on the served block
```

**A correctness invariant about the rollup, not an emission claim. The flip condition FAILS. RIDE
stands by my own construction, not by my preference.** CVO verified the same line independently.

⭐ **The best thing in the tick belongs to `0.4.0_DS_ClientPlatform~G`:** *"I hold no preference between
ride and detach and did not have one when I read; the clause decided it."* — **a seat reading a clause
that decides against the position it had been defending, and correctly saying it never held a
position.** It withdrew the *fusion* (commit-boundary vs project-boundary) without withdrawing the
*objection*, which stands and was never an argument for detach.

⚠ **Bound, named by the reading seat before anyone asked:** inv-3 and b-7 were read — **not all 36
cells**, not the stage-2 PRD's done section. A narrowing clause, if one exists, would sit *alongside*
inv-3 rather than replace it.

### And the call surfaced something better than its own answer

>> **inv-3's oracle is *recompute each level from the level below* — an INDEPENDENT DERIVATION.** So
   the vacuous-pass `0.4.0_DE_ClientPlatform~D` feared (producer's parent vs producer's own children,
   agreeing at **both** +2.01% and −5.68%) **is not what inv-3 specifies — it is what implementing
   inv-3 as an equality check would produce. The cell already authorizes the stronger form.** <<

**The harness is still not redundant:** inv-3's recompute tests rollup **arithmetic**; the emit-path
harness tests whether `_performance` calls the shared law **at all**. *A correct library reached
through a wrong call site passes a recompute.* Two planes — that strengthens RIDE rather than
substituting for it.

## CALL 2 — I RESERVED IT, CVO CHECKED THE CITATION AS ASKED, AND IT DID NOT REACH

I rested the reservation on `CLAUDE.md:63-67` and asked CVO to **check it rather than accept it**,
because I knew the failure runs the other way. It read the underlying Andrew-direct at source:

```
  THE RULE      do not manufacture a GATE ON ANOTHER SEAT out of a word given to one
  THIS QUESTION what semantics a deploy gate should have -- no word relayed, no seat stopped
  AND          the 23:4xZ discharge LIFTED a cap. A word that REMOVES friction is not
               what that limb protects; limb (b) protects against a word turned INTO friction
```

⛔ **The heading was the ruling: DO NOT MANUFACTURE FRICTION.** Reserving a call I own *adds* friction,
and the doc names the cost by example — a pipeline that did not get finished. **The over-reservation
defect and my reservation are the same failure with the sign flipped.**

### So I took it and ruled it — `CTO_RULING_20260901_1340Z_SERVE_RELEASE_SEMANTICS_...md`

**One-time-transition STANDS as the correct semantics.** Conflating *"may this file be served at all?"*
with *"is THIS VERSION right?"* into one gate is a **Rule-24 intent-coherence violation** — one axis,
one intent. A content-scoped grant would fire on **every deploy of every served file, forever**, and
⛔ **a gate that fires on everything protects nothing — it trains the seats it binds to override it.**

>> **The 91462 finding is UPHELD as a finding and REFUSED as a SERVE-RELEASE defect.** The 118,465
   bytes are not serving because the gate leaked — **they are serving because NOTHING WATCHES CONTENT
   VINTAGE AT ALL.** Repairing SERVE-RELEASE would close the finding on paper while installing the fix
   on the wrong carrier, and the real gap would be *harder* to see with a remediation row over it. <<

**The half that is NOT mine, per CVO's s.4 split:** whether a content-vintage control should exist is a
**new gate on work → Andrew's word.** Proposing is legal; implementing is not. **Nothing is being
built. The card is open.**

## Driver acts taken this tick

- **The R-2..R-5 rider is PLACED** (CVO declined to place it; I said I would this tick and did). It is
  now a **refusal condition**, not a caution — the ruling makes per-deploy semantics wrong on the
  merits, so a repair producing it incidentally produces a ruled-against state by accident.
- ⚠ **And placing it surfaced a finding I was not looking for: `R-2`..`R-5` HAVE NO REPO CARRIER.** A
  full-corpus `comp-find` returns them **only inside `org/mcp/inbox/**`** — the message stream. A repair
  set with acceptance criteria and owners lived only in messages, which scroll. **That is the loss
  class the verdict ledger closes, reappearing one layer up: the ledger captured the VERDICTS and
  nothing captured the WORK ITEMS those verdicts govern.** The ruling document is their first artifact.

## ⛔ On `0.4.0_DS_ClientPlatform~N`'s self-reported overstep — the ambiguity was MINE

That seat made the carrier-3 edit before COO's placement, read its authority from my ruling's own
disposition line (*"DS lane: carrier 3... This ruling is the authority for it"*), and surfaced the
overstep itself rather than letting it be found.

**NO REVERT.** My 91574 drew a distinction between *authority to edit* and *placement of the work* that
**my ruling did not carry** — a DS-lane seat holding that exact cell read a lane name plus a grant of
authority as go, which is what those words say. **A false self-attribution installs the fix on the
wrong carrier**, and the carrier here is my disposition wording.

**Verified on my own instrument before ruling it moot** (`git show c85701ebca`, diff parsed, not eyed):

```
  24 added · 2 removed · NON-COMMENT lines changed: 0
```

## Fabric state

- **`2.0.0_SA_COO` fully back and working** — issuing issuer rulings, seating, narrowing E2. Register
  `open_tos` **23 → 19** since it returned.
- **The integration window RAN.** `origin/CLOUD` = `c85701ebca`; both my commits **ON** (`9eecb8cb54`,
  `78c24f0936`), verified with a fabricated-sha negative control that correctly reads ABSENT.
- ⚠ **`0.4.0_DS_ClientPlatform~N` flagged a stale ETag in V-4's evidence and the 08-30 ledger** — the
  live a07 object is now `9202d701...` (34,289 B). Third instance of that carrier class on this cell in
  two days. **Verify by CONTENT against the index blob at the CURRENT pin, never a hash recorded for an
  earlier one.**

## RESERVED cards still at Andrew

- D3's order relative to D8.
- Whether the flow-ingestion defect widens the ruled 22.
- **NEW:** whether a content-vintage control should exist at all (a new gate — proposed, not built).

## Compiler Tools

`directives-check.py --json` + completion scan over 10 member JSONs (denominators printed) ·
`comp-find "R-2\b" --corpus all --files` (carrier census, message-stream-only result) · `git show` +
a **parsed** diff for the comment-only claim · `git merge-base --is-ancestor` with a fabricated-sha
negative control for every push-state claim · `git ls-remote`. No `head` on any census.

**PUSH STATE, MEASURED:** `9eecb8cb54` + `78c24f0936` **ON origin**; this log + ruling LOCAL.
`origin/CLOUD` = `c85701ebca` (fetch + rev-parse 13:4xZ).

**State:** `ARMED` · next tick on the cron.
