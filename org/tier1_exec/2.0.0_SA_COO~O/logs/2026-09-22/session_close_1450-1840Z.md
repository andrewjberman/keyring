# 2.0.0_SA_COO~O -- NFRA_OPLGTW session close, 2026-09-22 14:50Z - 18:40Z

**archetype:** COORDINATE
**secondary_archetypes:** EXPLORE, SCRIBE

Seated on Andrew-direct ~14:5xZ at the `1.0.0_SA_CTO` terminal (*"spawn COO~O and let's finish that out."*). Closed on
Andrew-direct ~18:2xZ at this terminal, VERBATIM: *"Finish your work and research on the OPLGTW project and do not go
further with it. Close out anything you are working on and write a /log on current state of the project."*

---

## 1. WHAT THIS SESSION DID

1. Startup: `/watcher` armed and re-armed on every 30-minute expiry (7 arms, each verified by a one-row process census);
   `org/XXX.md` Step 1b A-F; sequence check (`NFRA_OPLGTW` not WAITING, capacity AT CAP 3 of 3 COO lanes).
2. Measured the project at HEAD and found the blocker nobody had named as a blocker: **the walkthrough the last two
   orders grade cannot happen while the Schwab switch is off, and that switch is the same act as the held Act 2.**
3. Put ONE card to Andrew through `1.0.0_SA_CTO` and `0.0.0_AB_MSTR` (99531/99532, nudged 99544/99545): (A) a bounded
   walkthrough window, or (B) close round 1 without the walkthroughs. REC (A), and `1.0.0_SA_CTO` recommended (A) too.
4. **Andrew answered ~17:1xZ: *"Yes to Schwab"*** = option (A), relayed at 99557, recorded by `1.0.0_SA_CTO`
   @`465d591b25`.
5. Drove step (a) of (A) -- the `G-C` evidence order -- to the point of issue: routing corrected to the live lane,
   the seating constraint measured, the CTO's no-objection obtained and its own correction absorbed, `2.0.0_SA_COO~B`'s
   confirmation obtained, the order drafted and gate-checked. **It was NOT issued: Andrew's stop arrived first.**
6. Answered Andrew's status question in full (FWD-by-FWD, entitlements/IAM, tooling/indexing, internal-vs-vendor data
   sources), compiled from three read-only agents over the PRD, the decomposition, all 33 orders and the Gateway source.

## 2. THE PROJECT'S CURRENT STATE -- written for a reader with zero prior context

**`NFRA_OPLGTW` (the Opal Gateway), directive D9, tree `org/missions/D9/NFRA/NFRA_OPLGTW/`, `dep_stage: EXECUTING`,
round 1, PRD v0.9 @`8a63c77b51` ADMITTED with BOTH sign-off halves SIGNED and current.**

**Orders: 33 total -- 30 `complete`, 1 `superseded` (`OG-r-2`), 2 `pending` (`OG-v-4`, `OG-v-5`).**
**Outcomes: 0 of 8 FWDs graded.** There is no `surprise-channel/adjudications/` and no `remediations/` directory under
this project; no L9 has ever run on it. Every FWD-1..FWD-8 states `DONE WHEN: EXERCISED` and every PROOF line names a
human act, so the two pending orders are the ONLY route to all eight (row `NFRA_OPLGTW-S62`).

**The build is done and is real.** Identity (ALB OIDC against Entra, signature verified by the Gateway itself, five
providers coded and four deliberately dark, boot-refusal of any unverifiable provider), a two-key design (write
decisions on the verified email, DATA decisions on immutable `tid`/`oid`), three tiers, a versioned per-principal grant
model with revocation-as-tombstone, default-deny three ways over, a proper MCP error envelope on denial, assume-role-only
S3 access fenced to six named prefixes, a runtime/operator IAM split enforced by `dynamodb:LeadingKeys`, an allow-listed
audit with a stricter acknowledged-write path for Schwab releases.

**What is NOT done:**
- **The proving.** `OG-v-4` (controlled walkthrough, serves FWD-1 and FWD-3..FWD-8) is HELD on `G-C` + `G-D`.
  `OG-v-5` (pilot, serves FWD-1 and FWD-8) is HELD on `G-E` + `G-F` and depends on `OG-v-4`. All four gate records are
  ABSENT at HEAD.
- **Capacity.** `OG-r-2` RAN and measured INSUFFICIENT; closed `superseded` for round 1 with two unrepaired FAILs (export
  at contract scale peaked 270581760 against the 268435456 job cap; `OGR2-AC2`'s "never exceeds" bar missed at
  282021888). It re-cuts in round 2 behind `1.0.0_SA_CTO`'s open L4 question `R-OG-22` (is 250000 rows / 50 MiB a
  CONSUMER REQUIREMENT or an aspiration).
- **One ARMED security row this lane owns, deliberately not disarmed:** `W3-S9`/`S61` -- `resolve_tier(email, cfg)` keys
  `MASTER_ADMIN` off an EXACT EMAIL MATCH at FOUR live production sites, one of them `token_broker.py:143`, which mints
  token SCOPES. The module's entire root-of-trust defence answers FORGERY; the row's hazard is RE-ASSIGNMENT, which is
  signature-verified and genuine. It is an L4 item for `1.0.0_SA_CTO`, disclosed and accepted FOR THE WINDOW ONLY.

**The seal is intact and is NOT in `C:/tmp`.** `OG-v-4` phase 1 (the re-seal, `OGV4-AC8`) landed @`c1c3eeb7e0`, recording
the measured absence of `G-C` and `G-D` at commit `15edf9f07b` as its precondition. `C:/tmp/nfra-oplgtw-sealed/` is GONE
again (measured this session, `Test-Path` false), and that is harmless: the copy of record is SSM SecureString under
`/opal/nfra_oplgtw/ogv4/reseal_20260918/` -- **7 of 7 parameters present** (SALT + RQ1..RQ6), read this session by name
only, nothing decrypted. A successor restores from there; it does not re-seal.

**The Gateway is UP** (measured ~17:0xZ): instance `i-07dccb1615503ac99` running, target group `opal-gateway-tg` reports
it HEALTHY, the public ALB answered in 0.23 s, and 0 target-5xx / 0 ELB-5xx across 3 hours on 17 requests. The Schwab
switch is OFF: `ENABLED_INTEGRATIONS=ycharts opal_portal globgrph` (read @`e2f11d1e3d`, not re-read this session).

## 3. ANDREW'S WORD, AND EXACTLY WHAT IT AUTHORIZES

**~17:1xZ, VERBATIM: *"Model Portfolios looks good, visual smoke closed successfully. Yes to Schwab. Bright Data I will
provide the additional key shortly"***. Record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_171xZ_MDPF_SMOKE_CLOSED_AND_YES_TO_SCHWAB_WALKTHROUGH_WINDOW.md`
@`465d591b25`.

It authorizes option (A) AS WRITTEN and nothing wider. **The order of the remaining acts is load-bearing:**
`G-C` evidence -> `1.0.0_SA_CTO` records and closes `G-C` -> the never-widen sign-off, BOTH halves, MEASURING FRESH that
a principal with no grant is REFUSED -> the switch ON for the walkthrough window ONLY -> a person runs the controlled
walkthrough (`G-D`) -> the grader is spawned for `OG-v-4` -> the switch OFF. `OG-v-5` needs `G-E` and `G-F` beyond all of
that. **Act 2's five Schwab tools stay NOT enabled outside the window; a standing lift needs its own word.**

⚠ **THE ONE CALL ANDREW HAS NOT ANSWERED:** who operates the two walkthroughs. My card 2 proposed (a) Andrew for the
controlled one, Menachem for the pilot. No answer. `G-D` and `G-F` cannot be produced by any agent.

## 4. THE G-C ORDER: DRAFTED, GATE-READY, NOT ISSUED

`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/DRAFT_NOT_ISSUED_TO-OG-g-1_controlled_identity_and_grant.md`

Everything it needed was in hand when the stop arrived: Andrew's (A); `1.0.0_SA_CTO`'s no-objection to the seating
override, unconditional once its condition was met (99573, 99580); `2.0.0_SA_COO~B`'s confirmation that the recipient
lane's five IRPT_BCKEND orders are **terminal by a valid proof at HEAD, status word merely stale, 0 open ids** (99579).

⛔ **IT IS PARKED IN `deliverables/`, NOT IN `task-orders/`, ON PURPOSE.** A file in `task-orders/` with any non-terminal
status counts as an OPEN ORDER, and this project's L10 counts open orders PER PROJECT (LD-0521) -- parking it there would
have left a third open order behind me for a successor to trip over. A successor MOVES it, re-reads every pin at HEAD,
and hands it.

⛔ **AND ONE INSTRUMENT FAILED OPEN IN A WAY THE NEXT ISSUER MUST NOT INHERIT:** I ran `.tools/to-pipeline-gate.py` on the
draft and it printed `OK: MERGE COMMIT -- task-order checks exempt`. **THAT IS NOT A PASS OF MY ORDER.** The shared tree
was mid-merge for `2.0.0_SA_COO~B` (`.git/MERGE_HEAD` present, 6 of that seat's files staged), and the gate exempts
task-order checks entirely in that state. **The draft has therefore NEVER been graded by the L6 gate, and a reader who
sees the `rc=0` in my scrollback would believe it had.** Re-run it on a clean index before handing.

## 5. WHAT I TOUCHED IN THE SHARED TREE, AND THE ONE THING I ALMOST BROKE

I drafted the order inside the SHARED worktree while `2.0.0_SA_COO~B` held a merge in progress, and I ran
`git add -N` on it -- putting an intent-to-add entry for MY file into the index of ANOTHER SEAT'S UNFINISHED MERGE. A
commit by that seat would have carried my draft into its merge commit. **I removed it with a path-scoped
`git reset` and verified that seat's 6 staged paths were untouched (6 before, 6 after).** No harm landed. ⭐ The carry,
which is Rule 14b's own point measured the hard way: **CHECK `.git/MERGE_HEAD` BEFORE STAGING ANYTHING IN THE SHARED
TREE** -- the shared index is not yours, and `add -N` is a write to it. COST: one `ls .git/MERGE_HEAD`.
NON-APPLICATION: your own linked worktree, which is what I should have opened first and did open for this commit.

## 6. MCP TRAFFIC

11 messages handled, all acked by `ack_messages` from their own `Msg-ID` lines: 98926 (CTO accepting the prior session's
both-acts report), 99546, 99550, **99557 (Andrew's word, relayed)**, 99562/99564 (the base-vs-lane routing correction,
`1.0.0_SA_CTO` owning its own defect), 99573 (CTO no-objection), 99576 (CTO correcting its own "audited by construction"
line on `3.0.0_SA_CVO~B`'s reading), 99579 (`2.0.0_SA_COO~B`'s terminal-by-proof confirmation), 99580 (condition met).
Sent: 99531/99532, 99544/99545, 99571/99572.

⚠ One send of mine was REFUSED by the LD-0529 gate and the refusal was CORRECT: I addressed a proposed ACT to
`0.7.0_AE_CloudOps~V` with no task order cited. Nothing was written for ANY of the three named recipients -- the refusal
is all-or-nothing, which is worth knowing before composing a multi-recipient send.

## 7. COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `comp-surprise` | `--project NFRA_OPLGTW` | PASS | 155 items, 33 ARMED, 0 graduated, 176 files, 0 malformed, 0 duplicate ids |
| `comp-find` | `"ENABLED_INTEGRATIONS" --all` | FAIL | `git ls-files --ignored` timed out at 180 s on this repo; the `all` corpus is unusable here today |
| `comp-find` | `"ENABLED_INTEGRATIONS" --corpus default --band DEF` | PASS | 229 hits / 40369 files; DEF=1 -- the only definition line is a test fixture, so the live value is an ENV, not a repo constant |
| `comp-find` | `"IB-rtf-3" --corpus default --files` | PASS | located the comparable Tier-2 order shape to mirror |
| `comp-read` | `.tools/to-decomp-ref-lint.py --for "<the seating rule>"` | PASS | gave `seating_check:249` verbatim -- the rule reduces to one test, which is what I cited |
| `prd-signoff.py` | `status NFRA_OPLGTW` | PASS | v0.9 @8a63c77b51, both halves SIGNED and current |
| `to-check.py` | `--all --project NFRA_OPLGTW`, `--all --assignee 0.7.0_AE_CloudOps~V` | PARTIAL | correct for MY project; on the assignee query it printed 5 PENDING for orders a proof-bound reader calls terminal |
| `sequence-check.py` | `--project NFRA_OPLGTW` | PASS | not WAITING, not HELD; capacity AT CAP 3 of 3 |
| `to-pipeline-gate.py` | bare, on the staged draft | **VACUOUS** | exempted itself on `MERGE_HEAD`; see s.4 -- recorded as a NON-RESULT, not a pass |

**What worked:** `comp-read --for` answered a rule question in one call that a file read would have taken five to reach.
**What failed:** `comp-find --all` -- the gitignored-file enumeration times out on this tree; `--corpus default` is the
working path today.
**Gap found:** `to-pipeline-gate.py` returns `rc=0` with an OK line while grading NOTHING when a merge is in progress.
The text says so honestly, but the exit code does not, and `rc=0` is what a script or a hurried reader reads. This is the
same law-stronger-than-tool shape `1.0.0_SA_CTO` corrected in itself at 99576 the same hour, from a different direction.

## 8. BLOCKERS

- **BLOCKED (evidence-cited), `OG-v-4`:** `G-C` and `G-D` ABSENT at HEAD (`git ls-tree` of the deliverables dir returns
  worker slots plus this lane's folder only). `G-C`'s remaining two elements need the delegated administrator's act;
  `G-D` needs a PERSON at a work browser. Andrew's word (A) unblocks the path but does not perform either act.
- **BLOCKED (evidence-cited), `OG-v-5`:** `G-E` and `G-F` ABSENT; also depends on `OG-v-4`. `G-E` needs Menachem's
  verified `tid`/`oid` plus an approved concrete grant and its activation; `G-F` needs Menachem's own session.
- **AT ANDREW:** who operates the two walkthroughs (card 2, unanswered).
- **AT `1.0.0_SA_CTO`:** `R-OG-22` (the export cap question) gating `OG-r-2`'s round-2 re-cut; `G-C`'s recording; the CTO
  half of the never-widen sign-off; the `W3-S9`/`S61` email-keyed-tier L4 item.

## 9. NEXT STEPS

1. **[Andrew]** name the walkthrough operators. Nothing in the remaining chain moves without a person.
2. **[2.0.0_SA_COO~O, a successor lane]** move the parked draft into `task-orders/`, re-read its pins at HEAD, re-run
   `to-pipeline-gate.py` ON A CLEAN INDEX, and hand it to a live CloudOps lane -- with the seating override scoped to the
   SEATING finding alone and its audit row READ BACK, because the override is not audited by construction.
3. **[1.0.0_SA_CTO]** after the evidence lands: record and close `G-C`; then both halves of the never-widen sign-off,
   measuring the no-grant refusal FRESH.
4. **[2.0.0_SA_COO~O successor]** the switch ON for the window only; grader spawned for `OG-v-4`; switch OFF; then
   `G-E`/`G-F` for `OG-v-5`.
5. **[1.0.0_SA_CTO]** `R-OG-22`, which is what `OG-r-2`'s round-2 re-cut waits on.

## 10. WHAT I DID NOT DO, STATED SO NOBODY LOOKS FOR IT

No order issued. No seat spawned. No switch touched. No AWS write of any kind. No merge or push. Nothing was enabled,
and Act 2 stands exactly where the session found it.
