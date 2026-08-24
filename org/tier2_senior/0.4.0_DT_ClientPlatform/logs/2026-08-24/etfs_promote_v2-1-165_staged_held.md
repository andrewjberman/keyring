# Session log -- 0.4.0_DT_ClientPlatform -- ETFS_POSITIONING promote v2.1.165 STAGED + HELD

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

Window: 2026-08-21 21:11Z seating -> 2026-08-24 13:10Z. (Session spans a ~63h idle gap; both
active stretches are covered here. No prior log exists for this seat in this session.)

## Summary

Seated for the ETFS_POSITIONING portal DEV->PROD promote leg. Ran all four cut gates at my own
measurement rather than off the briefs, found and routed TWO findings that changed what shipped,
staged the promote to the last reversible moment, and STOOD DOWN on Andrew's sovereign hold.

**THE PROMOTE DID NOT HAPPEN. NO PRODUCTION WRITE OCCURRED.** origin/PROD is unchanged at
8a96c916 (= portal-v2.1.164 peeled); merge a239e4a9 exists on ZERO remote branches. Verified
independently by 3.0.0_SA_CVO (66080) rather than resting on my own report.

## Work done

### 1. Startup (org/XXX.md Step 1b, complete)
- Serial NOT REGISTERED at load; registered fresh (PID 27480). A.1 session serial file written.
- **/watcher: no pre-existing process for my serial** (7 other seats had one) -- a genuine fresh
  arm, not the orphan case, and not the context-clear false-positive. Monitor **b533621n8** armed
  and CONFIRMED running by TaskOutput (the only probe that observes a consumer).
- A.3 PATH: **97 of 102** comp-tools resolve bare; EXERCISE half fired (a forwarder RAN, produced
  its banner) -- the half that can actually see a dead target.
- to-check.py --all --assignee: 2 TOs held (OPAL_ADVIPOINTERS.P4-PROMOTE-49F pending, under
  Andrew's ADVI hold; D7_TICKETING.WC-SITEZ joint, site-Z half, staged behind W-A).
- 19 messages read and ACKed on the READ clock across the window.

### 2. Gates -- all measured at my seat, none taken from a brief
MSTR's spawn brief pinned origin/DEV @ee90fa8e; **that pin was stale 45 minutes later** and MSTR
corrected it themselves (65892). I had already re-run ls-remote before their correction and again
after. The ref moved THREE times during the leg: ee90fa8e -> a60b558f -> d43b88c5.

Final battery at the pushed ref, 2026-08-24T12:39:00Z:
- **(i) FENCE** 3ade1aba ancestor of origin/DEV -> MET.
- **(ii) half 1** ee90fa8e (TO-3 flip) ancestor -> MET.
- **(ii) half 2** flip rows in adviKeyRepoint.ts: ran the file's OWN prescribed recipe (extract the
  state value, never match a literal). **15 rows against the ruled denominator 15; held 14 /
  structural 1 / FLIP 0.** Positive control 15, negative control 0.
  Guard input was **byte-identical across the re-pin** -- blob 0ae44992 at both ee90fa8e and
  a60b558f -- so the census transferred by IDENTITY, not re-derivation. Re-ran it anyway at each
  new tip.
- **(iii)** DE's serving-leg confirmation, cleared at 65981 and RAVC-validated at my seat.
- **unit item** (CTO ruling 65935 item 2): conversion tokens 0 at the cut ref, positive control 5
  at a7ff6dd4, negative control 0.

### 3. FINDING 1 -- payload scope: 9 of 13 commits are ADVI, not ETFS
adviKeyRepoint.ts is **ABSENT from origin/PROD 8a96c916** (git cat-file, positive-controlled
against advisor-intelligence.ts which IS present). So this promote is that machinery's FIRST
landing on PROD, carrying ADVI_ROUTE_LIVE=true.
It lands DORMANT: flip 0/15 and adviRead's conjunction gate serves legacy on every key regardless
of the global flag.
**Surfaced, NOT adjudicated** -- whether dormant machinery sits inside a sovereign hold is a scope
read and scope reads are not mine. CTO ruled it CLEARS (65935 item 1) and asked my sentence go in
the deploy ledger; it did, in his words.

### 4. FINDING 2 -- a 100x weight defect live in the push path
Doing /prod-deploy Step 1 (clean the DEV tree) I found an uncommitted 40-line etfAdapter.ts fix
off origin/DEV, mtime 3 minutes old. Routed it (65924). The situation then INVERTED: DS had fixed
the same bug producer-side 60 seconds after DE's file mtime, so the adapter conversion had to NOT
land -- both = every weight 100x too SMALL.

**The sharp form, and the one the estate kept: THE FIX WAS COMMITTED AND THE UN-FIX WAS NOT.**
a7ff6dd4 carried the conversion (3 tokens) on 0 remote branches while the deletion sat in a working
tree. **A push at that instant would have delivered the defect BY DOING THE THING EVERYONE WAS
WAITING FOR.** Flagged DO-NOT-PUSH to MSTR (65957); their own hold crossed mine, convergent.
Resolved by AE contract v1.2 (normative units; "an unlabelled example value in a data contract IS a
unit specification") + DE's deletion @d43b88c5.
I also noted to CTO that gate (iii) asks DE to confirm what was built while the build was still
moving -- COO called that the sharpest thing in the message and it was vindicated twice more.

### 5. Promote staged to the last reversible moment, then stood down
Freeze window declared and honored (MSTR + DE both MEASURED it empty rather than promising).
Andrew, asked directly by MSTR on CTO's own invitation, answered **HOLD FOR MY WORD ON ADVI**.
Stood down; **did not roll back**; ledger annotated HELD-PENDING-SOVEREIGN.
**Freeze RELEASED (my call, 66085)** -- the merge is already immutable, so a freeze from here buys
only "staged merge stays the latest DEV," which is convenience not safety, and not worth blocking a
lane for a wait of unknown length.

### 6. FINDING 3 -- the deploy ledger REFUSED the honest state (Rule-24, routed to COO)
`deploy_ledger.py hold --gate-type sovereign` REFUSED, verbatim:

    cannot HELD ... open APPLY/DEPLOY leg(s) ['merge','prod-push','pointer'] -- a half-landed
    deploy cannot be HELD (stays RED). A HELD/SOVEREIGN-GATED state requires ALL apply/deploy
    legs closed-with-proof and ONLY verify legs open.

**The HELD state EXISTS and is STRUCTURALLY UNREACHABLE HERE: its precondition can only be met by
APPLYING, which is the exact act the sovereign hold forbids.** Second, separable defect:
`check` prints stranded=[all 6 legs] for legs **never attempted** -- NOT-YET-STARTED and
PARTIALLY-DONE are opposite states taking opposite remedies (wait vs finish-or-roll-back under
NEVER#6), and the axis conflates them. **An alarm that cannot tell them apart would, at session
end, report a stranded production deploy where there is none -- and the reflex a stranded-deploy
alarm invites is "finish it," which here means pushing to PROD against a sovereign hold.**
Sharpens MSTR's and CVO's independently-reported gap: not only a missing VALUE, a CONFLATING AXIS.
Did not paper it and did not force a wrong state; annotated in prose, entry stays OPEN.

## Deployment Sequence + Verification (DT role addition -- ACTUAL output)

| step | result |
|---|---|
| Step 1 DEV tree | branch DEV; local == origin/DEV d43b88c5; 0 ahead / 0 behind; tracked-dirty 0 |
| Step 2 typecheck | `bun run typecheck` (tsc -b --noEmit) **rc=0** |
| **MUTANT CONTROL** | injected a string-to-number error into etfAdapter.ts -> **rc=2**, `src/pages/Positioning/shared/etfAdapter.ts(157,7): error TS2322: Type 'string' is not assignable to type 'number'`. **THE GATE FIRES.** Reverted BYTE-EXACT: post-revert blob 7940a205 == HEAD blob 7940a205, mutant tokens 0, tracked-dirty 0. Re-ran clean rc=0. |
| Step 3 local PROD re-assert | BEFORE 8a96c916, AFTER 8a96c916, == origin/PROD. No dry-run pollution inherited. |
| Step 4 worktree | `.runtmp/portal-promote-20260824T124621Z` at PROD 8a96c916; `bun install` FOREGROUND rc=0, 420 packages, 166.45s |
| Step 4 merge | `--no-ff origin/DEV`, message via **-F** (F-010, not -m) -> **a239e4a9023c8bc25c4d514735564f6a790a2a70** |
| **PARITY GATE** | `git diff origin/DEV HEAD` = **0 bytes**. Re-checked 0 after the mutant cycle. |
| Step 4 PROD push | **NOT EXECUTED** -- LD-0367 r2 (only the integrator pushes) + v2.1.158 precedent recorded its PROD push under an audited override. Requested of MSTR (66044); MSTR held on Andrew's word. |
| Steps 5-7 | NOT REACHED (CI / tag / pointer / teardown) |
| Rule 19 | portal main tree on **DEV** throughout, verified at every step |

Pre-verified WHILE HOLDING so nothing broke mid-deploy: bun 1.3.9 resolves; deploy_ledger.py
exercised (check rc=0 before I needed it); gh 2.87.0 authed, exact
`--json databaseId,headSha,workflowName,status,conclusion` query shape exercised and returning
real rows.

## Andrew-direct received (relayed, not at my terminal)

Relayed by 0.0.0_AB_MSTR (66067), who put the question to him directly:
**HOLD FOR MY WORD ON ADVI** -- on whether shipping DORMANT ADVI cutover machinery to PROD sits
inside his 2026-08-21T19:18Z two-condition ADVI flip hold.
Recorded here as RELAYED with its relayer named; I did not receive it at my terminal and I do not
adjudicate its scope. CTO 66073 concurred that his own ruling is SUPERSEDED PENDING HIS WORD.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| comp-which | `comp-which "how do I grep the repo"` | PASS | A.3 EXERCISE probe -- a forwarder RAN, not merely resolved |
| to-check.py | `--all --assignee 0.4.0_DT_ClientPlatform` | PASS | `--all` load-bearing; surfaced both held TOs |
| deploy_ledger.py | `open` (6 legs) / `hold --gate-type sovereign` / `check` | PARTIAL | open + check PASS; **hold REFUSED -- see Finding 3, routed to COO as a Rule-24 gap** |
| gh | `run list --branch PROD --json ...` | PASS | pre-verified against the CURRENT PROD head as a dry read, before I needed it |

**What worked:** the MUTANT CONTROL on the merged tree. `tsc -b` is incremental and the portal's
own law commit (82d3f28f) exists because a bare `tsc --noEmit` was a FALSE GREEN on this repo --
so a green from a gate I had not proven could go red is not evidence. It fired, named the exact
file:line, and reverted byte-exact.

**Second thing that worked, and it is the one I would keep:** re-running ls-remote at the moment of
each act rather than trusting a hash from a message. It caught a stale pin in a brief, and it is
the same habit that saved DE (they re-pulled the artifact before committing a fix they had ALREADY
VERIFIED BY RENDER twenty minutes earlier). **A verification does not announce its own expiry.**

**What failed -- GAP, tooling not mine:** the deploy ledger's HELD state is unreachable pre-apply
and its `check` output calls never-attempted legs "stranded" (Finding 3). Routed to COO as the
convention's owner; I did not mint a value, since that is a Rule-24 authoring act with its own
four-postulate record.

**Gap I did NOT hit but was warned of:** the long-subject send_message body-drop my predecessor
logged. Kept every subject short; all sends delivered with non-empty bodies (verified by `wc -c`
on the delivered files: 3979-3990 bytes for the URGENT), with the per-recipient result map's
denominator stated on every multi-recipient send.

## Blockers

**BLOCKED-SOVEREIGN, evidence-cited.** The promote is held on Andrew's word re ADVI machinery
scope (relayed MSTR 66067; CTO 66073 concurs his ruling is superseded pending it). Push-holder
0.0.0_AB_MSTR, decision-holder Andrew. This is NOT a manufactured gate: MSTR asked the principal to
interpret the principal's own standing hold, on the invitation CTO's own ruling extended.

**Nothing is stranded.** NEVER#6 binds a BEGUN deploy; no production write occurred. Verified
independently by CVO (66080), not on my report.

## Current State (zero-prior-context handoff)

- **portal origin/PROD = 8a96c91654ed282acbed04da1e9f0074dca42332** (ls-remote, APPLIED plane),
  == portal-v2.1.164 peeled. **NO v2.1.165 exists.**
- **portal origin/DEV = d43b88c5124c0b6a8ca0db49a1a8bb5826d0ea1c.** Freeze RELEASED -- DEV may move.
- **Merge a239e4a9023c8bc25c4d514735564f6a790a2a70 is STAGED, on 0 remote branches.** Parity 0
  bytes vs d43b88c5, typecheck rc=0 with a fired mutant control.
- **DELIBERATE LOCAL STATE, NOT POLLUTION-BY-ACCIDENT -- READ THIS BEFORE ANY OTHER PROMOTE:**
  `refs/heads/PROD` in the portal repo is INTENTIONALLY at a239e4a9 (not origin/PROD), and the
  worktree `.runtmp/portal-promote-20260824T124621Z` is INTENTIONALLY still checked out to PROD,
  because the merge is staged for an imminent push. **ANY OTHER PROMOTE MUST RUN /prod-deploy
  STEP 3 (`git update-ref refs/heads/PROD refs/remotes/origin/PROD`) AND `git worktree prune`
  FIRST**, or it silently bases on my staged merge -- the v2.1.114 dry-run-pollution class.
  Also recorded in the ledger entry.
- portal main tree on **DEV**; cwd returned to the workspace root.
- **Deploy ledger OPEN and annotated:**
  `org/critical_paths/change_management/20260824T1241Z_etfs-positioning-prod-promote-v2-1-165_deploy_completion.md`
  merge leg SATISFIED; 5 legs HELD-PENDING-SOVEREIGN; carries CTO's dormant-ADVI sentence, the
  100x near-miss, the local-state caution, and the tool-refusal evidence.
- **THE EXPIRY I BOUND MYSELF TO (66085):** a239e4a9 is only pushable-as-verified while origin/DEV
  == d43b88c5. If DEV has moved when the word arrives, I do NOT push the staged merge on today's
  evidence -- I re-gate and re-cut, or state explicitly that we are deliberately promoting an older
  tip and why. Four seats hit the stale-verification class on this thread since Friday; a staged
  merge sitting there looking green is exactly that shape.
- My inbox Monitor b533621n8 is live. Both background ref-watchers stopped (bqum4gc53 completed on
  the DEV push, bejjl1jlb TaskStopped when the PROD push was held).

## Next steps

- [0.4.0_DT_ClientPlatform] On Andrew's word: **re-run ls-remote FIRST**, then either push
  a239e4a9 (if DEV unmoved) or re-gate + re-cut. Then CI enumerated by headSha across EVERY
  workflow (not the branch badge -- the 7d544d27 case had one green and one red on one sha),
  tag portal-v2.1.165 verified PEELED, workspace pointer, teardown, ledger CLOSED, freeze report.
  If the word REFUSES: reset local PROD to origin/PROD, prune the worktree, close the ledger
  ROLLED BACK, and say so loudly.
- [2.0.0_SA_COO] Rule the ledger state vocabulary (Finding 3). Two separable defects: the missing
  HELD-PENDING-SOVEREIGN value AND the `stranded` axis conflating NOT-YET-STARTED with
  PARTIALLY-DONE. CVO 66080 proposes one vocabulary review covering their channel-schema gap too;
  I concur and add that fixing only the value leaves `stranded` still meaning both things.
- [0.0.0_AB_MSTR] Holds the PROD push; one command when the word lands.
- [1.0.0_SA_CTO] Carrying the one-line cost picture to Andrew (ADVI commits are ancestors of the
  ETF flip; excision is a shared-branch rewrite / NEVER#7, so "do not ship the machinery" holds the
  ETF page with it -- promote-with or do-not-promote is the real choice).
