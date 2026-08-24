# Deploy Completion Record
**Date opened:** 2026-08-24T12:41:33.101921+00:00
**Status:** OPEN
**Deploy:** portal DEV->PROD promote v2.1.165 -- ETFS_POSITIONING TO-3 (Models<->ETFs flip) + OPAL_ADVIPOINTERS repoint machinery landing DORMANT (flip 0/15)
**Authored by:** 0.4.0_DT_ClientPlatform
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| merge | git | ephemeral-worktree merge --no-ff origin/DEV d43b88c5 onto PROD 8a96c916 | parity diff origin/DEV..HEAD EMPTY (0 bytes) |  | OPEN |
| prod-push | git | origin/PROD advances 8a96c916 -> merge sha | ls-remote read, not local ref |  | OPEN |
| ci | verify | deploy.yml + every workflow for the merge headSha | gh run list --json filtered to headSha; conclusion=success on ALL, never the branch badge |  | OPEN |
| tag | verify | annotated tag portal-v2.1.165 | git rev-parse tag^{commit} PEELED == origin/PROD head |  | OPEN |
| pointer | git | workspace CLOUD submodule pointer -> portal d43b88c5 | commit + push state stated by ls-remote |  | OPEN |
| teardown | verify | worktree pruned, portal main tree back on DEV | git -C portal branch --show-current == DEV |  | OPEN |

## Log

- 20260824T124133Z OPENED by 0.4.0_DT_ClientPlatform with 6 leg(s)

## Scope decision recorded at deploy-START (CTO ruling 65935 item (1))

**WE ARE SHIPPING THE ADVI CUTOVER CODE TO PROD, DORMANT, INSIDE AN ETFS TICKET.**
Recorded here deliberately so it is DECIDED NOW rather than DISCOVERED LATER.

- Payload is 13 commits (origin/PROD 8a96c916 .. origin/DEV d43b88c5), 12 files. **9 of them are
  OPAL_ADVIPOINTERS**, not ETFS.
- `src/api/endpoints/adviKeyRepoint.ts` is **ABSENT from origin/PROD 8a96c916** (verified by
  `git cat-file -e`, positive-controlled against `advisor-intelligence.ts` which IS present).
  So this promote is that machinery's FIRST landing on PROD, and it lands with
  `ADVI_ROUTE_LIVE = true`.
- **It lands DORMANT.** Registry census at the cut ref: 15 brace-opened rows against the ruled
  denominator of 15 -- **held 14 / structural 1 / FLIP 0** (positive control 15, negative control 0).
  `adviRead` gates on a conjunction, `if (!ADVI_ROUTE_LIVE || entry.state !== 'flip')`, so every
  ADVI key serves legacy regardless of the global flag. **PROD ADVI behavior is unchanged.**
- **RULED BY CTO (65935 item 1):** the promote CLEARS. Andrew's 2026-08-21 19:18Z two-condition
  hold binds FLIPPING; dormant machinery landing together with its own never-widen enforcement
  point is the correct order, not a breach. CTO carried it to Andrew at their terminal the same
  turn; his word overrules.
- Surfaced by 0.4.0_DT_ClientPlatform (65908) as a scope fact, NOT adjudicated at this seat.

## Second item closed before the cut, recorded because it nearly rode in

A 100x ETF weight defect was **committed** (a7ff6dd4, adapter converts percent->fraction) while its
**deletion sat uncommitted in a working tree**. DS had already fixed the same bug producer-side
60 seconds after DE's file mtime, so both landing = every weight 100x TOO SMALL -- the plausible
direction that gets believed, not the absurd 995% that got caught. A push at that moment would
have delivered the defect BY DOING THE THING EVERYONE WAS WAITING FOR.
Resolved: AE contract v1.2 (normative units), DE deleted the conversion @d43b88c5.
**VERIFIED AT THE CUT REF:** conversion tokens = 0, positive control at a7ff6dd4 = 5 (the probe
discriminates), negative control = 0. Net effect on `etfAdapter.ts` vs a60b558f is a doc comment
plus a cosmetic reflow -- functionally identical, pass-through, as ruled.

---

## STATE AS OF 2026-08-24T13:0xZ -- HELD-PENDING-SOVEREIGN (annotated in prose; the tool REFUSED the state)

**NOT COMPLETED. NOT ABORTED. NEITHER TERMINAL IS TRUE OF THIS ENTRY.**

- **push-holder:** `0.0.0_AB_MSTR` (integrator; the push is one command, staged and ready)
- **decision-holder:** **Andrew** -- does shipping DORMANT ADVI cutover machinery to PROD sit inside
  his 2026-08-21T19:18Z two-condition ADVI flip hold? Put to him by MSTR on CTO 65935's own
  invitation ("his one word overrules mine"). His answer: HOLD FOR MY WORD ON ADVI.
- **CTO 66073:** ruling 65935 stands AS CTO'S READ, SUPERSEDED PENDING HIS WORD.

### Leg state
| leg | state |
|---|---|
| merge | **SATISFIED** -- a239e4a9023c8bc25c4d514735564f6a790a2a70, parity diff vs origin/DEV = 0 BYTES, typecheck rc=0 with a MUTANT CONTROL that FIRED (rc=2, etfAdapter.ts(157,7) TS2322) and a byte-exact revert (blob 7940a205 == HEAD blob). LOCAL ONLY. |
| prod-push | HELD-PENDING-SOVEREIGN |
| ci | HELD-PENDING-SOVEREIGN |
| tag | HELD-PENDING-SOVEREIGN |
| pointer | HELD-PENDING-SOVEREIGN |
| teardown | HELD-PENDING-SOVEREIGN |

### NEVER#6: NOTHING IS STRANDED. NO PRODUCTION WRITE OCCURRED.
Verified independently by `3.0.0_SA_CVO` (66080) rather than resting on this seat's own report:
`origin/PROD` = 8a96c916 UNCHANGED (= portal-v2.1.164 peeled) · merge a239e4a9 on **0 remote
branches** · `origin/DEV` = d43b88c5, freeze intact. The deploy has NOT BEGUN in NEVER#6's sense --
it is parked at the last reversible moment. **Staged-and-intact and half-landed are the whole
question, and this is unambiguously the first.**

### ⚠ LOCAL-STATE CAUTION FOR THE NEXT PROMOTE SEAT (dry-run-pollution class, DELIBERATE not accidental)
`refs/heads/PROD` in the portal repo is **INTENTIONALLY at a239e4a9**, not at origin/PROD, and the
ephemeral worktree `.runtmp/portal-promote-20260824T124621Z` is **INTENTIONALLY still checked out**
to PROD -- because the merge is staged for an imminent push, not abandoned.
**ANY OTHER PROMOTE MUST RUN /prod-deploy STEP 3 (`git update-ref refs/heads/PROD
refs/remotes/origin/PROD`) AND `git worktree prune` FIRST**, or it silently bases on this staged
merge. Recorded here so a documented state cannot become a silent trap -- which is exactly the
class Step 3 exists to kill (v2.1.114, stale 47b3d5d7).

### ⛔ THE TOOL REFUSED THE HONEST STATE -- MEASURED, AND IT IS A RULE-24 FINDING (routed to COO)
`deploy_ledger.py hold --gate-type sovereign` was run and REFUSED, verbatim:
> REFUSED: cannot HELD ... open APPLY/DEPLOY leg(s) ['merge', 'prod-push', 'pointer'] -- a
> half-landed deploy cannot be HELD (stays RED). A HELD/SOVEREIGN-GATED state requires ALL
> apply/deploy legs closed-with-proof and ONLY verify legs open.

**The HELD state EXISTS and is STRUCTURALLY UNREACHABLE HERE: its precondition (all apply legs
closed-with-proof) can only be met by APPLYING, which is the exact act the sovereign hold forbids.**
And the tool classifies a PRE-APPLY promote as "half-landed" -- `check` prints
`stranded=['merge','prod-push','ci','tag','pointer','teardown']` for legs that were **never
attempted**. NOT-YET-STARTED and PARTIALLY-DONE are opposite states taking opposite remedies
(wait vs finish-or-roll-back), and the axis conflates them.
Hence this prose annotation: the entry stays OPEN in the tool and carries its true state in words.

---

## ADJUDICATED **KNOWN-HELD / SOVEREIGN-GATED** by 2.0.0_SA_COO, out-of-band (msg 66102, 2026-08-24T13:16Z)

**The RED this entry emits is a DECLARED FALSE POSITIVE for the duration of the gate, and it is
COO's, not this seat's.** Recorded here because the tool cannot hold the state -- **disclosed as a
tool limitation, not presented as a tool state.**

- **gate:** sovereign
- **gate-ref:** "Andrew: does shipping dormant ADVI cutover machinery (flip 0/15, behavior
  byte-unchanged) to PROD sit inside his two-condition hold"
- **COO ruling, verbatim in effect:** DO NOT RETRY THE HOLD (it is designed to refuse, and is right
  to given what it can see) · DO NOT FORCE A WRONG STATE · DO NOT CLOSE AS ABORTED.
- This seat is **NOT carrying an unowned alarm into session end.**

### The finding, sharpened by COO at source -- and it is sharper than "no HELD value"
`deploy_ledger.py:654-664`, `_qualifies_as_held` clause (a), its own docstring:

    every APPLY/DEPLOY leg (kind != 'verify') is CLOSED-WITH-PROOF -- AN OPEN APPLY LEG IS A
    GENUINELY HALF-LANDED DEPLOY -> DISQUALIFIED (stays RED). THIS is the anti-escape-hatch.

**That sentence states the conflation AS A DEFINITION, and it is false for a never-started leg.**
The predicate asks *"does any apply leg LACK PROOF?"* when the safety question is *"did any apply
leg PARTIALLY WRITE?"* Those diverge at exactly one place: a staged, intact, never-begun deploy.

⛔ **AND THE TOOL DISAGREES WITH THE LAW IT ENFORCES.** NEVER#6 binds a BEGUN deploy. `0.0.0_AB_MSTR`
(66067) and `3.0.0_SA_CVO` (66080) INDEPENDENTLY determined this one has NOT BEGUN in NEVER#6's
sense -- origin/PROD unchanged, merge on a local ref, 0 remote branches, no production write.
**THE LAW SAYS NOT-BEGUN AND THE TOOL SAYS HALF-LANDED.**

### The two findings are ONE (0.0.0_AB_MSTR 66098, source-confirmed)
The HELD state is unreachable **BECAUSE** the predicate cannot separate NEVER-ATTEMPTED from
ATTEMPTED-AND-INCOMPLETE. **Fixing the conflation fixes the reachability for free; fixing
reachability alone -- by relaxing clause (a) -- WOULD BREAK THE ANTI-ESCAPE-HATCH and let a
genuinely half-landed deploy hide. That is the worst available repair and it is the one that looks
most direct.**

### Remedy shape named by COO (routed to CTO, who authored the guardrails) -- NOT built here
A THIRD leg state the ACTING SEAT DECLARES: **NOT-STARTED** (no write attempted), distinct from
**OPEN** (attempted, unproven). A hold then qualifies when every non-verify leg is
CLOSED-WITH-PROOF **or** actor-declared NOT-STARTED. **The anti-escape-hatch must survive any fix.**
That moves the failure mode from "the tool was fooled" to "an actor lied in the record" -- a better
class, already covered by the audit trail. Rule-24: a value ADDED to an existing axis is an
authoring act (four-postulate test; CE half against the declared layer).
**Not urgent (MSTR 66098): the failure mode is at the session-end sweep, not the next ten minutes.
Ruling it during a live promote is how a good fix becomes a second incident.**
