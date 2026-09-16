# 0.0.0_AB_MSTR~Z — 2026-09-16 00:15–03:10Z — launch, POSN_AGGFIX close, the ARGV cliff, and /integrate parity to a measured fixed point

**archetype:** MIXED (COORDINATE-dominant; DIAGNOSE and DEPLOY legs inside it)

## Current State

`/integrate parity` reached its terminal state **PARITY**, measured at this seat from the remote and
not from the peer's report: `origin/CLOUD == origin/SITEZ == 585d8b4e23`, both `is-ancestor` legs YES,
0 ahead in both directions, local HEAD the same object, clean tree.

POSN_AGGFIX is CLOSED (`status: closed` / `dep_stage: CLOSED`, R6 exercised on the real close path,
0 violations). Portal **v2.1.179** is live on PROD `@ff542d0a`. The ~32 KB ARGV cliff is closed on
both devices **including its generator**.

Live on this device at close: this seat and `0.1.0_DS_MarketIntelligence`. Nothing queued to push;
no holds owed by or to this seat.

## What happened, in the order it mattered

**Launch.** `/watcher` (two staggered Monitors), `/agentbus` (device measured `sitez`), `/integrate`
assess-only, `org/XXX.md` Step 1b A–F. Zero crons, per the Step 1b-F MSTR row. Device note worth
carrying: the drive prefix here is **`/c`** — `/cygdrive/c` is NOT mounted, and both the watcher skill
and `org/XXX.md` Step C tell you to prefer it. A wrong prefix arms nothing and returns a task id anyway.

**POSN_AGGFIX** closed on Andrew's word through three seats, none of which adjudicated another's lane.
`2.0.0_SA_COO~Z` flipped `status` but deliberately NOT `dep_stage` until the grades landed — R6 fires
only on `dep_stage == CLOSED` and `pre-commit:109` denies on its rc 1, so a premature flip would have
**blocked every seat's commit on this clone** across 18 projects and 367 index rows. That restraint is
the single best call anyone made tonight and it was made by the seat that would have looked fastest
by not making it.

**The ARGV cliff.** `/integrate parity` leg 1 resolved cleanly, every gate PASSED on the merged index,
and the commit then died at `pre-commit:124` — `$STAGED` expanded UNQUOTED into argv, 2537 paths /
230,037 bytes against an MSYS limit near 32,767. **The gate did not refuse; it never ran.** Andrew:
*"GOWITH YOUR REC"* → fixed rather than bypassed. Detail in
`deliverables/ARGV_CLIFF_INSTALLER_HALF_20260916_Z.md` @`f512c3132f`.

**Parity.** Laptop merged leg 1 and resolved; this seat took the result and re-resolved NOTHING; the
fixed point closed on a **hold** this seat took because it was the side with nothing pending.

## Compiler Tools

| tool | invocation | result | read |
|---|---|---|---|
| `comp-which` | `comp-which "how do I grep the repo"` | forwarder RAN | Step 1b A.3's mandatory second half. `104 of 104` comp-tools resolve bare AND one executed — resolution is not execution, and the exercise is the half that proves it |
| `comp-find` | `'site-Z push hold' -i --limit 20` | **121 hits / 62819 files**; HEAD=1 SURFACED=1 CONFIG=4 **DOC=115** | The band split IS the finding: 115 DOC-band hits were seats RESTATING "Push state: LOCAL (site-Z push hold)" in `.scratch/` drafts. The single HEAD hit merely REFERENCES the hold. Restatement is not establishment |
| `comp-find` | `'SITEZ' --band HEAD --limit 15 org/tier0/ledger/` | **MEASURED ZERO** across 564 files (104 hits, all DOC) | No ledger entry establishes a site-Z push hold. Andrew confirmed independently: *"There is no push hold by the way"* |
| `comp-find` | `'site-Z push hold' -i \| head -5` | **RAIL DENIED** (twice) | **GAP/OPERATOR ERROR, mine:** piping a census into `head` erases its denominator, so the rail refuses. ⛔ AND THE DENIAL ABORTS THE WHOLE BASH CALL, so the *earlier* segment in that call silently no-opped. I made this error TWICE. Use `--limit`/`--page`/`--band`, never a pipe |
| `comp-secrets` / `comp-estate` / `comp-pipescript` | not run | n/a | No secret read, no estate query, no gold script touched. MSTR has no role minimum in the Step 1b table |

**Gap found, not a tool defect:** `to-check.py --all --assignee <serial>` returned other seats' orders
— the assignee filter did not apply. Consistent with `org/XXX.md` B.1's own warning that a zero or an
absence from that read tells you nothing. Cross-checked against `<issued_to>`; this seat holds none.

## Errors of mine, all caught before they landed

1. **Commit author lines read as a push oracle.** `a4ef8853`/`be8cf218` carried `0.0.0_AB_MSTR` as
   committer, so I drafted an amendment concluding the laptop pushed DEV and that the shared-branch
   law was SATISFIED — including a correction to `1.0.0_SA_CTO~Z` about its own act.
   `org/git-author-override-audit.log` settled it: that seat pushed under an audited override.
   **Commit identity answers "who wrote this object", never "who moved this ref."** The direction is
   what made it expensive: a **FALSE ALL-CLEAR** on a law question closes the question and nobody
   re-opens it. Caught only because a peer's account and my inference disagreed and the disagreement
   bought one more read instead of a correction sent to the peer.
2. **Second person in a multi-recipient message.** That withdrawn correction's replacement ran in
   second person to two seats, so "You pushed DEV under an audited override" resolved to
   `2.0.0_SA_COO~Z` in its inbox. It caught it and cited the CLAUDE.md line verbatim. Re-addressed
   naming serials.
3. **A union ORDER applied without naming it a decision.** I verified the five loop rows SURVIVED —
   which tests membership and is blind to sequence — and called it done. The laptop caught that two
   fabrics with the same content in different orders is a permanent diff. Settled chronological.
4. **`833` for `640`.** Conflated ahead-of-CLOUD with ahead-of-`origin/SITEZ`; caught by measuring
   before quoting, in the same message that was about being precise.
5. **`=== PUSH EXIT: 0 ===` after a pipe** — measured `tail`'s status, not git's. The push had failed.
6. **Generalised one device to two on shape, not bytes:** told the laptop "you will hit ARG_MAX too."
   It measured its own hook and falsified me. Its hook carried the env form; mine did not.

## Findings that outlived the session

- **A fix to a GENERATED artifact is not landed until the GENERATOR carries it.** `38a37be871`
  (2026-09-04) fixed the gates (tracked) and one box's hook BY HAND (untracked) and left
  `.tools/git-hooks/install-*.sh` — which MINT the hook — carrying the defect on BOTH boxes. Every
  fresh clone re-minted the cliff and the hand-patched box was fixed only until someone re-ran an
  installer. **Ask what mints the file you just corrected.**
- **The half-applied fix INVERTS the failure direction.** The argv cliff fails **CLOSED** (rc 126).
  Dropping argv on a box whose gates could not read env fails **OPEN** — rc 0, `denominator: 0`,
  byte-identical to a healthy pass. Named by `0.0.0_AB_MSTR`; verified here at this seat's own ref
  before touching anything, because a fail-open hazard is the worst place to accept a peer's read.
- **A vintage move can ADD a conflicted path, not only change known ones.** Overlap went 6→7 and the
  new member was the portal gitlink. The cheap partial re-run would have returned CLEAN and been WRONG.
- **A zero-count identical hunk range is an APPEND collision, not one defect corrected twice.** PICK
  would have deleted one fabric's Step 1b-F loop-authorization rows. Landed as the laptop's `LD-0572`
  Step-4 qualifier, re-derived there with a negative control.
- **`branch -r --contains` is the control a gitlink turns on** — ancestry proves "loses nothing",
  only publication proves every other clone can fetch the object. `1.0.0_SA_CTO~Z`'s, and the half
  this seat would have missed.
- **`heartbeat()`'s piggyback footer claims EMITTED-not-READ without reading delivery state** — wrong
  on 5 of 5 rows across three observations tonight.

## Blockers

None at this seat.

## Next Steps

1. **[`1.0.0_SA_CTO~Z`]** D12 WS-3, the 30-day remembered device — Andrew's *"first and foremost"*,
   asked twice because the owner was down. Relayed verbatim with the source-verified finding (msg
   23347). ⚠ That seat was NOT live at close, so the relay is sitting in its inbox rather than being
   worked. The binding constraint is the **30-minute idle logout**, not the 7-day refresh cookie —
   lengthening the cookie moves nothing.
2. **[DS/AE lane]** Four first-mint 404 scripts skipped by the deploy gate across tonight's two
   pushes. A first-mint is an explicit act in the owning lane, never the push gate.
3. **[`safe-merge.sh`'s owner]** Its refusal text reads *"a hook saw something the merged-index grade
   above did not."* On an ARG_MAX death the hook saw NOTHING — it died before reading a path. A crash
   and a refusal are different objects and this reports one in the other's vocabulary, sending the
   reader to hunt the branch.
4. **[either MSTR]** Parity is perishable and was true at ~02:5xZ. Do not quote tonight's both-YES
   tomorrow; re-measure in the same breath as any claim.

## Push state

`origin/SITEZ` `585d8b4e23` (`ls-remote` read) — **ON ORIGIN**, identical to `origin/CLOUD`. Nothing
local unpushed. Two pushes this session: `34575aaded` (643 commits; ceiling 3 → scope 2 → **deployed
0**, both first-mint 404) and `585d8b4e23` (ceiling 8 → **4 shipped**: 2 loose + 2 inside the
`investor-reporting` bundle, 4 first-mint skipped). ⚠ The gate's success line read *"2 deployed and
verified"* and **understates by the two bundle-routed files** — the denominator trap the laptop handed
me an hour before it fired on my own leg.
