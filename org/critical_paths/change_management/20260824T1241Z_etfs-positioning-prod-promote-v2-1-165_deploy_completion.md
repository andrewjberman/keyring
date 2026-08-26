# Deploy Completion Record
**Date opened:** 2026-08-24T12:41:33.101921+00:00
**Status:** SUPERSEDED -- nothing stranded, nothing performed -- closed 20260826T160405Z by 0.4.0_DT_ClientPlatform~C
**Deploy:** portal DEV->PROD promote v2.1.165 -- ETFS_POSITIONING TO-3 (Models<->ETFs flip) + OPAL_ADVIPOINTERS repoint machinery landing DORMANT (flip 0/15)
**Authored by:** 0.4.0_DT_ClientPlatform
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

> ### ⛔ SUPERSEDED. READ THE LEG TABLE CAREFULLY: "closed" THERE MEANS *DISPOSED OF*, NOT *DONE*.
>
> Five of the six legs were **NEVER PERFORMED** and now never will be. Each carries its supersession
> evidence in the proof column and each leads with **NOT PERFORMED**. No leg was closed that was not
> performed-or-superseded, and no proof was manufactured.
>
> **WHY SUPERSEDED:** this promote was overtaken by the other fabric. `portal-v2.1.165` shipped
> **2026-08-25T01:47:35-04:00** at **d9a98bcc** (author `0.2.0_DT_PortfolioAnalytics~Z`, site Z,
> 41 commits / 43 files -- a LARGER cut than the 13/12 staged here), under its own ledger
> `20260825T0543Z_etfs-positioning-prod-promote-v2-1-165-sitez_deploy_completion.md`, **CLOSED with
> all six legs proven**. `origin/PROD` has since advanced through v2.1.166/167/168 to **73afaccd
> (v2.1.169)**. The merge staged here, `a239e4a9`, is an ancestor of **neither** remote branch
> (`merge-base --is-ancestor` FALSE against both, positive control `d9a98bcc -> 73afaccd` TRUE) and
> survives only as tag `parked/v2.1.165-etf-promote-held-20260824`.
>
> **NEVER#6 IS SATISFIED, NOT WAIVED: NO PRODUCTION WRITE EVER OCCURRED ON THIS LEG** (recorded
> 2026-08-24, verified independently by `3.0.0_SA_CVO` at 66080). The legs were UNDONE, never
> half-done -- there was never anything to finish or to roll back.
>
> **THE LOCAL-STATE CAUTION BELOW IS DISCHARGED** (verified 2026-08-26T15:4xZ): local
> `refs/heads/PROD` = 73afaccd == origin/PROD, `git worktree list` shows the main tree only, portal
> on DEV. No trap remains for the next promote seat.
>
> #### HOW THIS ENTRY NEARLY CAUSED A FIVE-RELEASE PRODUCTION REWIND
> On 2026-08-26 COO built a card to Andrew from *this entry* while it read `OPEN / 51.1h
> PAST-WINDOW / stranded=[all 6 legs]` -- every field TRUE ABOUT THE LEDGER and meaningless about the
> world -- obtained a sovereign RELEASE approval, and dispatched (72452) an instruction to push
> `a239e4a9`. Executing it would have **REWOUND PRODUCTION BY FIVE RELEASES.** The lane refused on
> measurement before acting (72492); COO withdrew the instruction (72497) and ratified the refusal.
> **An accurate record of a superseded act, left open, is an ACTIVE HAZARD: it reads as pending work
> and it recruits a sovereign approval to act on it.** CLAUDE.md NEVER#6 now carries the
> cross-fabric inversion clause because of this.
>
> #### RULE-24 FINDING FROM 2026-08-24 STANDS, WITH A SECOND INSTANCE
> The ledger vocabulary has no *reachable* state for a deploy that was OVERTAKEN, just as it had none
> for one HELD PENDING SOVEREIGN. Its `stranded` axis conflates NOT-YET-STARTED with PARTIALLY-DONE,
> which take opposite remedies. `SUPERSEDED` is an EXISTING token (`deploy_ledger.py:139`
> TERMINAL_STATUS_TOKENS) set on this line per the tool's documented path at `:850` -- **no new schema
> value was minted.** `close` cannot emit it: it demands per-leg proof and then hardcodes
> "CLOSED -- nothing stranded". Owner: `2.0.0_SA_COO` as convention owner.
>
> #### ⛔ AND A DEFECT MEASURED WHILE CLOSING THIS ENTRY
> `close-leg`/`close` call `_write_entry()`, which RE-RENDERS this .md from the sentinel JSON. The
> sentinel holds only legs/log/status -- **so every hand-authored section below was silently
> destroyed on the first `close-leg` call** (139 lines deleted, recovered here from git HEAD). That
> is severe for a convention whose own refusal path *instructs* seats to annotate in prose: the tool
> tells you to write prose it will later delete without warning. Routed to `2.0.0_SA_COO`.

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| merge | git | ephemeral-worktree merge --no-ff origin/DEV d43b88c5 onto PROD 8a96c916 | parity diff origin/DEV..HEAD EMPTY (0 bytes) | NOT PERFORMED AS A PRODUCTION ACT -- SUPERSEDED. Merge a239e4a9 was created in a local ephemeral worktree 2026-08-24 and NEVER pushed. Verified 2026-08-26T15:4xZ: git merge-base --is-ancestor a239e4a9 origin/PROD -> FALSE, and against origin/DEV -> FALSE. It is an ancestor of NO remote branch; it survives only as tag parked/v2.1.165-etf-promote-held-20260824. The payload shipped instead in d9a98bcc (portal-v2.1.165, author 0.2.0_DT_PortfolioAnalytics~Z, 2026-08-25T01:47:35-04:00, 41 commits/43 files -- a LARGER cut). | CLOSED 20260826T160404Z |
| prod-push | git | origin/PROD advances 8a96c916 -> merge sha | ls-remote read, not local ref | NOT PERFORMED -- SUPERSEDED, AND NOW IMPOSSIBLE. No production write ever occurred on this leg (CVO verified independently at 66080). origin/PROD never advanced 8a96c916 -> a239e4a9; it advanced 8a96c916 -> d9a98bcc (v2.1.165) and onward through v2.1.166/167/168 to 73afaccd (v2.1.169), by ls-remote at 2026-08-26T15:4xZ. Because a239e4a9 parents a superseded PROD head, pushing it would be a REWIND OF FIVE RELEASES, not a promote. COO 72497 WITHDREW the RELEASE instruction and stood 0.0.0_AB_MSTR down as push-holder. | CLOSED 20260826T160404Z |
| ci | verify | deploy.yml + every workflow for the merge headSha | gh run list --json filtered to headSha; conclusion=success on ALL, never the branch badge | NOT PERFORMED -- SUPERSEDED. No CI run exists or can exist for a239e4a9: it reached no remote branch, so no workflow was ever triggered on it. CI for the promote that DID ship is closed with proof under ledger 20260825T0543Z_etfs-positioning-prod-promote-v2-1-165-sitez (leg L3, incl. its amendment recording that a headSha-scoped check on a PROD merge structurally cannot see the DEV-only validating workflow). | CLOSED 20260826T160404Z |
| tag | verify | annotated tag portal-v2.1.165 | git rev-parse tag^{commit} PEELED == origin/PROD head | NOT PERFORMED BY THIS LEG -- SUPERSEDED. portal-v2.1.165 EXISTS but is NOT this merge: annotated tag object 8fd31fbb peels to d9a98bcc, not a239e4a9 (git ls-remote --tags, 2026-08-26T15:4xZ). The version number this ledger reserved was consumed by the site-Z promote. This merge instead carries the non-release tag parked/v2.1.165-etf-promote-held-20260824. | CLOSED 20260826T160405Z |
| pointer | git | workspace CLOUD submodule pointer -> portal d43b88c5 | commit + push state stated by ls-remote | NOT PERFORMED -- SUPERSEDED. The CLOUD submodule pointer was never moved to d43b88c5 by this leg. The pointer move for the promote that shipped was performed on the SITEZ branch and is closed with proof under the site-Z ledger leg L5 (gitlink content-verified on the pushed ref at 063ff4d7). | CLOSED 20260826T160405Z |
| teardown | verify | worktree pruned, portal main tree back on DEV | git -C portal branch --show-current == DEV | SATISFIED, though not by this leg -- state verified at 2026-08-26T15:4xZ. The DELIBERATE local state this ledger warned the next promote seat about is CLEARED: local refs/heads/PROD = 73afaccd == origin/PROD (no longer pinned to a239e4a9); git worktree list shows the MAIN TREE ONLY (the .runtmp/portal-promote-20260824T124621Z worktree is deregistered); portal main tree on DEV, Rule 19 intact. No trap remains for the next promote. | CLOSED 20260826T160405Z |

## Log

- 20260824T124133Z OPENED by 0.4.0_DT_ClientPlatform with 6 leg(s)
- 20260826T160404Z LEG merge closed: NOT PERFORMED AS A PRODUCTION ACT -- SUPERSEDED. Merge a239e4a9 was created in a local ephemeral worktree 2026-08-24 and
- 20260826T160404Z LEG prod-push closed: NOT PERFORMED -- SUPERSEDED, AND NOW IMPOSSIBLE. No production write ever occurred on this leg (CVO verified independent
- 20260826T160404Z LEG ci closed: NOT PERFORMED -- SUPERSEDED. No CI run exists or can exist for a239e4a9: it reached no remote branch, so no workflow was
- 20260826T160405Z LEG tag closed: NOT PERFORMED BY THIS LEG -- SUPERSEDED. portal-v2.1.165 EXISTS but is NOT this merge: annotated tag object 8fd31fbb pee
- 20260826T160405Z LEG pointer closed: NOT PERFORMED -- SUPERSEDED. The CLOUD submodule pointer was never moved to d43b88c5 by this leg. The pointer move for t
- 20260826T160405Z LEG teardown closed: SATISFIED, though not by this leg -- state verified at 2026-08-26T15:4xZ. The DELIBERATE local state this ledger warned 
- 20260826T160405Z CLOSED -- all 6 legs proven

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
