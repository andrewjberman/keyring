# 1.0.0_SA_CTO~X -- SESSION CLOSE 19:00Z-01:40Z (D11 ~X fabric wind-down, Andrew-direct)

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE, COORDINATE

Design lane for Directive 11 (Substrate Analysis), laptop fabric. Session closed on an Andrew-direct
wind-down at ~01:25Z. This log is the HANDOFF SURFACE -- Current State below assumes zero prior context.

## The wind-down (the last act of the session)

**Andrew-direct at this terminal, VERBATIM AND ENTIRE:** *"i want to wind down your fabric, (the ~X D11
fabric). Have everyone record /log and then once they're all in, you write a /log and /handoff save"*

Relayed verbatim to the five ~X D11 seats (89757-89761, 5 of 5 DELIVERED). ⛔ **SCOPE HELD EXACTLY AS
GIVEN, neither wider nor narrower:** the ~Y fabric (`1.0.0_SA_CTO~Y`, `1.1.0_SA_KJ~Y`, `1.2.0_SA_A0~Y`,
`4.0.0_SA_CRO~Y`) is OUT OF SCOPE and the ~X seats were told not to relay to it; `0.0.0_AB_MSTR` is the
SHARED INTEGRATOR across both fabrics and was **NOTIFIED, NOT INSTRUCTED** -- converting a word about one
fabric into a stop on the integrator is the act CLAUDE.md forbids by name.

**ALL FIVE LOGS IN -- 5 of 5, AND EVERY ONE VERIFIED AT THE OBJECT (author + subject + placement), never
taken on the seat's self-report:**

| seat | log commit | placement (measured here) |
|---|---|---|
| `0.8.0_AE_CloudComp~X` | `3382ee6e57` | ON_ORIGIN |
| `2.0.0_SA_COO~X` | `08d72777e3` | ON_ORIGIN |
| `4.0.0_SA_CRO~X` | `d4808fd4a5` | ON_ORIGIN |
| `3.0.0_SA_CVO~X` | `50458244e0` | LOCAL -- matches its own report exactly |
| `0.7.0_AE_CloudOps~X` | `5334a3019a` | ON_ORIGIN |

Null control `ffffffffff` ABSENT, so the positives are real positives. ⚠ **THREE SEATS REPORTED LOCAL AND
MEASURED ON_ORIGIN** -- `0.0.0_AB_MSTR` ran a window at 01:33Z (7 commits) between their writes and my
reads. **Their reports were TRUE WHEN MADE and stale by the time I checked; that is perishability, not a
seat's error**, and it is the third time today a placement claim aged inside one exchange.

## What this lane produced this session

1. **RULE 3 ARMED in the shared card checker @`510a84ab23`** (`.tools/substrate-card-check.py`, this lane's
   tool). **A NULL VALUE CANNOT CARRY A NON-NULL BASIS** -- a consumer rejecting on `basis != measured`
   was accepting fields whose entire value is the word `unmeasured`. Censused at pin `47954ef3de`: **12 of
   102 basis-carrying cards across three seats, none of them card 7**, which is the measured answer to
   "an arm shaped to the last defect". Mutation-tested from a passing base; 7/7 tests; three negative
   controls clean; corpus regression exactly +12. ⛔ **NOT RETROACTIVE** -- binds the NEXT cut; the 12 are
   a routed finding. **The gap it closed was in RULE 2, which I authored two commits earlier.**
2. **Addendum 1w @`a9c7a2616c` + FIVE amendments** -- the conservation shape for multi-carrier claim
   repairs, and how prose discovery is bounded. **Every amendment was a certifier-found defect in my own
   work.** See "Errors" below; the rulings themselves are in the design record.
3. **Six rulings earlier in the window** (`861c379619`, `61d975d1d5`, `a01ae5ca2a`, `a3f6f2fb22`,
   `3ef0f401c3`, plus 1s and its two amendments): the acceptance sentence's home, the extraction contract,
   the blocked_on grain, 1i's self-defeating pre-registration, and the 1p blocker correction.

## Errors I made, all found by readers, none self-caught

⛔ **ONE DIAGNOSIS UNDER THE WHOLE SET: I published a DERIVED SUMMARY of a measurement instead of the
measurement.** Three faces of it, and **two of the three landed INSIDE a correction**, which is the least
audited place in the fabric because a corrected paragraph reads as freshly verified:
- **Quoted, not measured (twice):** 1,488 when my own instrument had printed 1,487; then **29** when the
  true figure was **660**. The second was the same class as the first, one hour later. **The lesson had
  been RECORDED and not INSTRUMENTED.**
- **Substituted a number and left its breakdown** (Amendment 2 into Amendment 1's site) -- 1w's own
  conservation failure, by 1w's author, inside the amendment correcting an instance of it.
- **Published `most_common(6)` as a complete distribution** -- 618 of 660, short by 42.
- **Instrument failures reported because both fail toward ABSENCE:** `git ls-tree` is CWD-PREFIX-SENSITIVE
  and returned 0 files / 0 leaves with no error from a persisted subdirectory; and my own recorded
  heredoc-backslash trap gave a fixture a syntax error so a control arm fired for the wrong reason.
- **A near-miss I caught before acting:** I briefly read `2.0.0_SA_COO~X`'s "29,735" (a transport-stall
  retry count) as a third sweep figure while reconciling numbers. Caught on reading the body, not the
  subject line.

**THE MECHANICAL REMEDY, ruled at Amendment 4 and binding this lane:** every published distribution
carries its OWN SUM beside the headline count, asserted equal. **None of the three failures survives it.**
Amendment 5 extends it: the four declared parameters bind a CORRECTION as hard as the claim it corrects,
because **a correction is a census too and nobody audits it -- it arrives wearing a confession.**

## Current State (for a reader with ZERO context)

**Directive 11 -- NOT DONE, 0 of 2 projects `complete`, both REACHABLE.** Register: 12 live directives;
D11 device LAPTOP, open TOs 2, flags `[]`.

- **`NFRA_SUBSTRATECARDING`** (`org/projects/NFRA_SUBSTRATECARDING.json`, status `active`, dep_stage
  `EXECUTING`). Card 7 (ms_heat_snap) **JOINTLY CERTIFIED AND CLOSED @`47954ef3de`** (CVO PASS 00:28:42Z,
  CRO PASS 01:17:04Z, same pin). Count **6 -> 7 of 7**. ⛔ **THE DENOMINATOR MUST TRAVEL WITH THAT NUMBER:
  it is 7 of 7 CELLS-ONLY of 12 wave-4 REMOTE, with 5 double-carded in W2/W3 and out of this face BY
  CONSTRUCTION, not by omission.** ⛔ **7 of 7 IS NOT THE CLASS CLOSE** -- the face's own line 22 fires the
  class close on THE FACE'S joint PASS, never on a card count, and `2.0.0_SA_COO~X` explicitly declined to
  make it. Face `<status>` PENDING. **The face proof was CUT at the very end of the window by
  `0.7.0_AE_CloudOps~X` (in its log `5334a3019a`) -- it is NOT yet jointly passed and this lane has NOT
  read it.** Predecessor pins `6379c948fc`, `c531605da5`, `b72dd9cbaf` remain STOPPED: history, not state.
- **`NFRA_C3MATERIALIZE`** (status `active`, dep_stage `EXECUTING`). The 7A determination is DELIVERED and
  typed **`B-NO-DECLARED-RELATION-YET`** @`d8a53aba9e`, blocked on **condition 3, firm carry** --
  conditions 1 / 2a / 2b / 2c / 4 all MET. Measured: 30 distinct attribute keys over 11,232 nodes and
  16,397 edges, **ZERO naming a firm, tenant or client**. Gate `after-bridge-declared` **STAYS OPEN**;
  only OUTCOME_A discharges it. Edge-vocabulary finding CLOSED @`e6a6e781ed`.
- **RULE 3 Class A remainder:** `0.8.0_AE_CloudComp~X`'s 8 closed at the producer @`dc68d5cab7` ->
  `fe0cffd38b` (no card re-cut; grandfathering honored). **Outstanding: 2 at `0.7.0_AE_CloudOps~X`, 2 at
  `0.8.0_AE_CloudComp~Y`** (that seat was DARK, its notice QUEUED not delivered).
- **HALTGT** (`.tools/halt-gate-check.sh:213`): the push gate measures FILE POSITION -- the EMITTED clock,
  which 22a names unsound. ASSIGNED by `0.0.0_AB_MSTR` to lane owner `0.7.0_AE_CloudOps`; **this lane holds
  the five-clause design ruling that BINDS the repair**; sequenced shape (a) behind the W4-COX face close;
  **NOT started**. Its re-evaluation trigger did NOT fire (card 7 certified in time).
- **v3.1 emitter for the 21 W4 cards:** typed **DORMANT with a wake condition** by the issuer -- NEW WORK,
  not the repair of the RULE 3 finding, and not urgent since RULE 3 binds the next cut.
- **Transport:** both codex seats stalled tonight on OPPOSITE modes and both recovered --
  `3.0.0_SA_CVO~X` 12,729 systemError / 0 x 1009; `4.0.0_SA_CRO~X` 29,735 x 1009 / 0 systemError. ⛔ **The
  modes take DIFFERENT remedies, which is why the signature is COUNTED and never pattern-matched.**
  **Nothing was substituted for the missing verdict while CRO was down.**

**Push state, MEASURED at close:** `origin/CLOUD` = `d4808fd4a5` (ls-remote); a window ran 01:33Z. All of
this lane's commits including `fd1eb7e109` and `e41ede0180` are **ON ORIGIN**. Push on `CLOUD` is
**INTEGRATOR-ONLY** and the gate refuses this seat by name -- a LOCAL commit is the correct terminal state
for a lane seat, not a failure.

## Blockers

**NONE claimed as BLOCKED by this lane.** The one open question is carried to Andrew, not asserted:
⚠ **whether the wind-down also strikes the `org/XXX.md` Step 1b-F `/self-drive D11` carrier clause and its
cron `31950a5f`.** His word names the logs and the handoff and does NOT name the clause; **D11 is NOT done
(0 of 2)**, so the skill's own stop-condition is unmet. **I have NEITHER struck it NOR claimed it stands**
-- the clause is the only thing a successor session may re-arm from, so a wrong guess in either direction
has a real consequence.

## Next Steps

1. **[Andrew]** the carrier-clause question above -- strike, or leave armed for a successor.
2. **[`0.7.0_AE_CloudOps~X`]** the W4-COX face proof is cut and needs its joint PASS; then the class close
   is **[`2.0.0_SA_COO~X`]**'s act and no one else's.
3. **[`1.0.0_SA_CTO~X` successor]** design read of the face proof on presentation, and of any successor a
   certifier stops. RULE 3 binds at the next card cut.
4. **[`0.7.0_AE_CloudOps~X`]** HALTGT repair after the face close, under this lane's five binding clauses.
5. **[`0.8.0_AE_CloudComp~Y`]** 2 RULE 3 Class A hits, notice QUEUED while dark -- re-deliver on respawn.

## MCP traffic

~40 messages handled in the window. Significant: five broadcasts of this lane's rulings (89660-89666,
89673-89678, 89700-89704, 89722-89725, 89742-89744); the wind-down relay (89757-89761) and the integrator
notification; issuer disposition 89752 (count 7 of 7); `2.0.0_SA_COO~X` 89651 (the two-face diagnosis that
produced 1w). ACKs recorded for every message carrying a broker id; CVO frames carry NONE
(Sender-unverified) and are cited by timestamp+subject -- **never a fabricated number**.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `.tools/substrate-card-check.py` (RULE 3 + tests) | **PASS** | 7/7 pytest; mutation-tested (neuter guard -> exactly 1 red); corpus regression 132 -> 144, delta exactly +12 |
| `.tools/commit-gate.sh` | **PASS** | 2 of 2 py files; py_compile + ds-precommit + ruff py39 |
| `.tools/safe-commit.sh -F` | **PASS** | every commit, non-shell-written message file, msg-verify MATCH each time |
| `python .tools/directives-check.py --json` / `to-check.py` | **PASS** | 12 live; D11 2 members, open TOs 2 |
| pinned carrier sweep (`git ls-tree` + `git show` at a pin) | **PARTIAL** | correct once cwd was pinned explicitly -- see the CWD-prefix failure below |
| `git merge-base --is-ancestor` + `cat-file -e` (3-state, null control) | **PASS** | every placement claim in this log |

**What worked:** mutation-testing the new arm from a PASSING base -- it proved the arms were live rather
than decorative, and one mutant turned exactly one test red. Pinning a census instead of sweeping the
worktree, after the worktree moved under me mid-measurement.
**What failed:** `git ls-tree` run from a persisted subdirectory returned **0 files with no error** -- a
silent false ABSENCE that was available to be reported as a finding. My harness also loaded the wrong
schema, inflating both sides of a regression to meaningless numbers; caught because the CLI disagreed.
**Gap found:** ⛔ **an instrument that fails toward ABSENCE returns a clean answer to a question it never
asked**, and tonight it happened on THREE different instruments across two seats (`ls-tree` cwd prefix, a
lane-foreign `*.card.json` glob, a four-token sweep reported against a five-token signature). **The
dangerous direction is always ABSENCE.** Remedy now standing on this lane: pin `cwd` in every subprocess
call, declare SET + LEAF UNIVERSE + EXCLUSION + MATCH TARGET on every sweep, and make every published
distribution sum to its own headline.
