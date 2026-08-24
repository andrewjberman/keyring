# Deploy Completion Record

**Date opened:** 2026-08-21T19:30Z (RETROACTIVE -- see "Why this was opened after the fact")
**Status:** CLOSED -- STAGED-NEVER-APPLIED, nothing stranded, nothing landed. Terminal at open.
**Deploy:** Portal DEV->PROD promote, OPAL_ADVIPOINTERS.P4-PROMOTE-49F (49F ADVI twin repoint),
intended tag portal-v2.1.165. **THE DEPLOY NEVER BEGAN: no push, no CI run, no artifact
movement, no tag.**
**Authored by:** 0.4.0_DT_ClientPlatform
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py)
**Window:** n/a -- terminal at open

---

## Why this entry leads with CLOSED rather than with its class name

1.0.0_SA_CTO (65484) directed this entry be "titled and classed STAGED-NEVER-APPLIED". It is,
in the Status line -- but the Status **leads with CLOSED**, deliberately.
`deploy_ledger.py check` sweeps `change_management/*.md` for an OPEN/non-terminal status carrying
no sentinel and escalates it as a BYPASS with a RED to COO. Its terminal test is
`head.startswith(tok)` over `TERMINAL_STATUS_TOKENS` (`:585`, tokens at `:92-95`: CLOSED,
COMPLETE, DONE, ROLLBACK, ROLLED, CANCEL, SUPERSEDED, ABANDONED, RESOLVED, VOID).
**"STAGED-NEVER-APPLIED" is not among them**, so a Status leading with that string would have
been read as a live un-sentinelled ledger and **manufactured a false RED alarm at COO** -- from
the entry written to close a gap, on a promote that never touched production. Leading with
CLOSED satisfies the sweep; the class is carried immediately after, unabbreviated.

## Why this was opened after the fact (the deviation, stated plainly)

**I did not open a ledger entry at deploy-start.** The v2.1.164 promote (20260820T1829Z) opened
one with a 6-leg manifest; I opened none and did not notice until teardown. Surfaced unprompted
to COO (65366) and CTO; CTO ruled (65484) to write it retroactively.
**NEVER#6's begun-deploy obligation never attached** -- nothing landed, so there was never a
half-landed deploy to finish or roll back. No alarm condition existed at any point
(`deploy_ledger.py check` returned rc=0 throughout, 1 of 1 sentinels scanned, the single OPEN
entry being `freshguard-leg4`, pre-existing and unrelated).
**The entry exists anyway because the ledger is the census of deploy ATTEMPTS, not only of
landings** (CTO: "an attempt that stood down is the most useful row in it"). A promote that was
built, gated, and deliberately stopped leaves no trace in git, in the tags, or in CI -- this file
is the only place it is recorded.

## Manifest -- what was staged, and where each leg actually stopped

| leg | kind | target | proof | state |
|---|---|---|---|---|
| L1 | verify | payload enumeration vs the TO's exactness fence | origin/PROD..origin/DEV = 3 commits, not DE's 2: 033ed3c7 (DE P4R-2), 82d3f28f (CTO portal CLAUDE.md, 1 file +13/-0), 9580e18b (DE P4R-3). Fence TRIPPED and ROUTED, not self-cleared. Cleared by COO 65211 on independent measurement; CTO 65200 author-attested but declined to self-clear; CVO 65208 + DE 65216 corroborated (DE strongest: 0 dist files carry the law's text, positive-controlled at 1 for "platinum/advi") | CLOSED 20260821T170458Z |
| L2 | verify | typecheck under the portal typecheck law, mutant-controlled | `bun run typecheck` = `tsc -b --noEmit` rc=0 pre-merge AND rc=0 post-merge. MUTANT CONTROL RUN FIRST AND FIRING: string-to-number injected into adviKeyRepoint.ts -> rc=2 naming file:line. Reverted byte-exact (git hash-object == HEAD blob; mutant token count 0) | CLOSED 20260821T170000Z |
| L3 | verify | merge DEV->PROD in ephemeral worktree + parity gate | merge 3ca099b1fd73c844937fb775d15fa71d86a5d136, `--no-ff`, message via `-F` (F-010), in .runtmp/portal-promote-20260821T165723Z on PROD 8a96c916; bun install FOREGROUND rc=0, 420 pkgs; **PARITY GATE `git diff origin/DEV HEAD` = 0 bytes** | CLOSED 20260821T170200Z |
| L4 | git | portal origin/PROD advance to the merge sha (MSTR integrator push) | **NEVER EXECUTED.** Handed to 0.0.0_AB_MSTR (65226) per the TO's GATE-5 integrator-only clause. MSTR HELD the push on DE's P4R-4 product-plane finding and verified from the remote that nothing was pushed (65262). DT independently asked for the same hold in the same minute (65247); the two crossed on the wire | **NOT RUN -- HELD, then STOOD DOWN** |
| L5 | activation | deploy.yml on the PROD headSha (build -> S3 -> CloudFront -> auto-tag) | **NEVER TRIGGERED.** No push occurred, so no workflow ran and no tag was minted | **NOT RUN** |
| L6 | verify | teardown + main tree on DEV + PROD unchanged | worktree pruned (`worktree list` = 1, main only; physical .runtmp dir persists -- Windows long-path class, gitignored, inert); **local PROD ref reset 3ca099b1 -> 8a96c916** to kill the dry-run-pollution class (/prod-deploy Step 3); main tree on DEV throughout, never left it (Rule 19); cwd returned to workspace root | CLOSED 20260821T172000Z |

## Terminal state, verified on the APPLIED plane

- `git ls-remote origin refs/heads/PROD` -> **8a96c91654ed282acbed04da1e9f0074dca42332**, i.e.
  UNCHANGED and identical to the rollback base. Read from the REMOTE, not a local ref.
- `portal-v2.1.164` peeled (`rev-parse ^{commit}`) == that same sha. **NO portal-v2.1.165 exists;
  none was minted.**
- `git branch -r --contains 3ca099b1` -> **0 branches.** The staged merge never left the machine,
  and the local ref has since been reset, so it is no longer a candidate anywhere.
- portal main tree on **DEV**; worktree list = 1.

## Why it stood down (cause of record)

Not a mechanical failure -- every gate above PASSED. 0.4.0_DE_ClientPlatform measured that the
flip carried a **client-visible product regression** that no seat had ruled on: history
truncation, dimension collapse, and population loss across the certified set. The complete
recursive pass found **9 of 10 certified keys carry material regressions**; only
`clients-tab-slim` is clean. Both never-widen halves (CTO 65333, COO) were WITHDRAWN on all six
portal-reachable keys, and CTO ruled the promote does not happen (65333) -- a PRODUCT-READINESS
finding, not an LD-0429 fire miss.
Subsequently ruled by **Andrew-direct 2026-08-21 19:18Z** (relayed COO 65460, documented
@ad8bb50e56): the flip is **HELD on TWO conditions -- source gaps AND schedule -- both required,
neither sufficient.** The schedule leg was independent of everything this promote verified:
`advi-49f-publisher` is **DISABLED**, so the twins have no enabled producer schedule and would
have been served frozen from day one.

**Final registry census at DEV: FLIP 1 / HELD 13 / STRUCTURAL 1. Consumer-visible flips = 0.
THE CUTOVER IS STAGED, NOT LANDED.**

## Log

- 20260821T165723Z worktree opened on PROD 8a96c916 (deploy-start -- NO ledger entry opened at this point; the deviation this record exists to close)
- 20260821T170000Z L2 closed: typecheck rc=0 both sides, mutant control fired and reverted byte-exact
- 20260821T170200Z L3 closed: merge 3ca099b1, parity gate 0 bytes
- 20260821T170458Z L1 closed: payload fence tripped, routed, cleared by COO 65211
- 20260821T170300Z L4 handed to MSTR (65226); HELD same minute on DE 65232
- 20260821T171759Z CTO 65333 ruled STAND DOWN
- 20260821T172000Z L6 closed: teardown, local PROD ref reset, main tree DEV, PROD remote-verified unchanged
- 20260821T191807Z Andrew-direct: flip HELD on two conditions (source gaps AND schedule)
- 20260821T1930Z OPENED RETROACTIVELY and CLOSED in the same act, per CTO 65484 -- STAGED-NEVER-APPLIED, nothing stranded
