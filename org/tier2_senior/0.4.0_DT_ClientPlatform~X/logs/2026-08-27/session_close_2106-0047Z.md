# Nine landings, eleven findings, and four of them against my own instruments -- 0.4.0_DT_ClientPlatform~X

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Date:** 2026-08-27 / 2026-08-28
**Task Order:** D11 ISCK adversarial pass (round 2) + L0 Rework 4 (Andrew-released ~21:4xZ) -- ad-hoc, scoped
**Status:** COMPLETE -- stood down on Andrew-direct 00:44Z ("now is the time to take a /log and stop"), device reboot imminent

---

## Objective

Second log of this session; the first (`isck_r12_adversarial_pass.md`) covers 18:42-21:06Z. This
covers 21:06Z-00:47Z: the L0 Rework 4 execution Andrew released, its R4-6 rework, and ISCK round 2
through the boundary and two post-boundary amendments.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| commit-gate.sh | on every .py before each commit | PASS | 7 invocations, all clean |
| safe-commit.sh | `-F <msgfile>` + `GIT_COMMIT_AUTHOR_OVERRIDE=ANY_EXEC` | PASS | 7 landings, 7 SEPARATELY-REQUESTED overrides; msg-verify MATCH each time |
| run_gates.sh | `run_gates.sh <commit>` | PASS | the atomic-extract runner; the only source of citable gate numbers |
| git worktree | `add --detach` + `remove --force` | PASS | clean-room verification for R4-6; torn down, `worktree list` confirmed |
| git show / git archive | `<commit>:<path>` into an empty dir | PASS | the decisive instrument all night; positive control before every ABSENT verdict |
| isck_coverage_probes.py | self-test | PASS | my own suite: 22 self-controls at close |
| controls_receipt.py | full battery | PASS | 57/59 -> 73/73 -> 75/75 clean-worktree, 76/76 shared |

**What worked:** `run_gates.sh` (landed mid-session as the remedy to my own DT-R2-3) made every
number citable against a named commit. A detached worktree + external `ls` was the only vantage that
could see the R4-6 self-blindness.
**What failed:** nothing in the tools. My own `rc=$?` after a pipe read `tail`'s status once and
nearly became a filed finding; a case-sensitive grep returned a false zero on the boundary record.
**Gap found:** none new -- the gap I opened at 21:06 (no comp-tool answers "what does this schema NOT
constrain?") is what the committed probe suite now fills.

---

## Work Completed

### 1. L0 REWORK 4 -- released by Andrew, executed, ACCEPTED
`2ccda14e4a` (ON ORIGIN). Six-part receipt-contract/schema/control source tranche. Controls
57/59 -> **73/73 exit 0**.
**BOTH STANDING FAILURES WERE ARMS AIMED AT THE WRONG INSTRUMENT, NOT MISSING LAWS.** R4-2's mutant
redirected the registry pin to HEAD, which carries the registry file at the SAME BLOB -- inert in
effect, so nothing refused it. R4-3 ran schema-only against a cross-field temporal bound JSON Schema
cannot express; the verifier enforces it. Both would have been "fixed" by adding laws that existed.
I also wrote and reverted a binding in the same sitting: `registry.commit == ratified_at_commit`
fired on the CLEAN receipt. Pin and ratification are different axes by design. The positive arm
caught it; without running the clean receipt first I would have shipped a verifier that refuses
every honest receipt.

### 2. R4-6 -- CRO~X found my no-debris arm was SELF-BLIND; repaired and ACCEPTED
`2feca185e7` (ON ORIGIN). My baseline sat ~440 lines AFTER the `_load()` calls that create
`__pycache__`, so the "before" set already held the debris. External boundary measured 17 -> 18
while my arm reported PASS.
Fixed by SUPPRESSION not cleanup (`sys.dont_write_bytecode` before any load), baseline captured
immediately after, and a planted-`__pycache__` positive control that runs in a TEMP dir so proving
the arm can fail never writes into the guarded tree.
**A SECOND DEFECT SURFACED IN THE REQUIRED ENVIRONMENT:** both NO-PAIR-TOUCH arms asserted the
preserved ids as LITERALS and failed by construction in a clean checkout (working-tree pair; the
receipt half is untracked and simply absent there). Repaired to a process-start baseline where
absence is a legal value. Clean worktree 75/75, shared tree 76/76, external listing IDENTICAL in
both.

### 3. ISCK round 2 -- five landings
| commit | what | state |
|---|---|---|
| `c7fb383f50` | ARMs 1-3 + self-controls (the round-1 deliverable) | ON ORIGIN |
| `c3be1721d9` | ARM 4 paired-arm gate + census debt | ON ORIGIN |
| `f66685346e` | ARM 1 disjunctive `if.anyOf` parsing | ON ORIGIN |
| `db4062c3a7` | ARM-3 repairs (census 94/95, 0 open) | ON ORIGIN |
| `9fb81b743a` | ARM-4 consume gate + generated sidecar | ON ORIGIN |

### 4. Findings filed this window
DT-R2-1..R2-6 plus the ARM-4 adjudication input. **DT-R2-6** is the one with the longest chain:
`bridge_assertion` `candidate` x `contradicted` was STRUCTURALLY UNINHABITABLE (one arm forbids
`adjudicated_by`, the other requires it). CTO~X re-ruled the axis split; COO~X corroborated by a
6,144-instance exhaustive sweep and found mine was the ONLY dead cell of 24 -- their first two
attempts (24/24 and 10/24) were both killed by the positive control I had supplied for my own
finding. Census now 95/95.

### 5. Post-boundary amendments -- two attacks on my own gate
`6245dc0a3d` (ON ORIGIN) -- duplicate-key loader guard. **I found this myself** by testing one of
three vectors CTO~X had handed CRO~X against my own artifact, and reported it rather than keeping
the attack elegant.
`bb7444a08e` (**LOCAL**) -- consumption-time entry validation. **CRO~X's superset-values attack.**
The sidecar encodes the ruled value set TWICE (key + payload) and my loader matched one without
reading the other, so a widened payload still suppressed. ACCEPTED by CRO~X on a three-vector
regression.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Asked for each override SEPARATELY (7 of them) | A grant is singular; "build it" is not "land it". Confirmed correct by the granting seat every time. |
| Held commits through TWO merge windows | MSTR's broadcast; I measured `MERGE_HEAD`/`index.lock` absent myself before each commit rather than trusting the CLOSE frame. |
| Routed the CRO~X L0 order instead of complying or refusing | It was wider than Andrew's scope on my seat; CLAUDE.md forbids adjudicating wider OR narrower. It was superseded 8 min later -- nothing started. |
| DECOUPLED the ARM-3 repairs from the consume design | A tidiness preference (one commit not two) had become a boundary-blocking dependency: 6 of the 15 open items the boundary was being assessed against were already fixed in my uncommitted file. |
| Left 2 of 3 attack vectors untouched | A self-report removes a finding from the attacker's pile; it does not substitute for an independent attack. |
| Generated the adjudication sidecar rather than hand-listing it | The generator's count (18) disagreeing with the arm's (20) is what exposed the non-unique key. A hand-typed list would have looked complete and been short by two. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/standards/isck/isck_coverage_probes.py` | ARMs 1-4, consume gate, loader + entry guards, 22 self-controls | Yes -- `c7fb383f50` `c3be1721d9` `f66685346e` `db4062c3a7` `9fb81b743a` `6245dc0a3d` `bb7444a08e` |
| `org/standards/isck/ARM4_ADJUDICATION.json` | new, generated 20/20 | Yes -- `9fb81b743a` |
| `.../D11_MANIFEST/{MANIFEST_RECEIPT.v1.schema.json,controls_receipt.py,verify_receipt.py,l0_compile_w3.py}` | Rework 4 tranche + R4-6 repair | Yes -- `2ccda14e4a` `2feca185e7` |
| memory: `feedback_a_control_downstream_of_the_corruption_cannot_see_it.md` + MEMORY.md pointer | new | No -- memory dir, not repo |

---

## Blockers

**NONE.** Every item raised this window was closed. Three arose and cleared: a fabric-wide
`index.lock` outage (~10 min, not mine, surfaced at 76529-76532); an `ANY_EXEC` lane refusal on
`org/standards/` (resolved by explicit authorization, seven times); and CRO~X's L0 hold (discharged
by their own acceptance).

---

## Current State

> Written for a successor with zero context.

**Everything I produced is landed and accepted except one commit, and that one is LOCAL.**
`bb7444a08e` -- the ARM-4 entry guard -- is committed at my seat and NOT on origin
(origin/CLOUD was `3fbb493cda` at 00:47Z). It is ACCEPTED by `4.0.0_SA_CRO~X` on an independent
three-vector regression; it needs only an integration window. **A successor should confirm it rode
the first post-reboot window before assuming the ISCK suite is whole** -- without it the consume
gate accepts a widened payload.
All eight other commits are ON ORIGIN: `2ccda14e4a` `2feca185e7` `c7fb383f50` `c3be1721d9`
`f66685346e` `db4062c3a7` `9fb81b743a` `6245dc0a3d`.
**THE PRESERVED L0 EVIDENCE PAIR IS INTACT AND MUST STAY THAT WAY.**
`org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/graph_object_manifest.json`
(tracked-modified, blob `db684f932995d519a9087725b2d2539d249ea533`) and
`graph_object_manifest.receipt.json` (**UNTRACKED**, blob `3da49495aa16c5f92563c9c955bbd888d4f85072`).
It is a WORKING-TREE pair -- the receipt half exists on disk and in NO commit, so **a reboot that
loses the working tree loses it**, and `git clean` destroys it. It is under my own seat's
deliverables directory, which makes me the seat most able to destroy it. Preservation is ordered by
`4.0.0_SA_CRO~X`; the L0 release hold otherwise stands and no run/emission/cleanup is authorized.
**ISCK round 2 is CLOSED** at `1.0.0_SA_CTO~X` (BOUNDARY_ROUND2.md, three amendments; exit
condition 1 MET, 2 MET-and-EXERCISED, 3 NOT RUN -- the contract is v0.2-candidate, attacked not
frozen, and does NOT exit to operational use). Owed at that seat, not mine: the deduplicated finding
register, then ARM-1's 9 candidates.

---

## Next Steps

1. **Confirm `bb7444a08e` reached origin** -- the only LOCAL artifact of mine; the ISCK suite is
   incomplete without it.
2. **Do not clean or commit the evidence pair** -- [`4.0.0_SA_CRO~X`] owns it; it is untracked and
   one careless command from gone.
3. **Re-arm ARM-1 + ARM-4 per-batch differencing** on the next cited ISCK landing -- ratified standing
   units at this seat.
4. **[`1.0.0_SA_CTO~X`]** holds the finding register and ARM-1's 9; **[`2.0.0_SA_COO~X`]** holds the
   superseded-consumer census gating the R2-2 landing.

---

## MCP Traffic

~60 messages this window, all ACKed via `ack_messages`. Significant: Andrew's Rework-4 release
(relayed 76800), seven override grants, CRO~X's R4-6 NOT-ACCEPTED verdict and both later
ACCEPTANCEs, COO~X's self-blindness source-verification and 6,144-instance sweep, the boundary cut
and its three amendments, and the 00:44Z Andrew-direct stand-down. Outbound: ~20 substantive
reports including one fabric-wide BLOCKING escalation.

---

## Self-Corrections (the load-bearing half)

1. **Two defects with the SAME GEOMETRY, both mine:** the R4-6 baseline sat downstream of the debris
   it measured; the class-D control sat downstream of a loader that had already collapsed its input.
   Both passed with full confidence. **A control downstream of the corruption cannot see it.**
2. **NAMING A CLASS DOES NOT DISCHARGE IT.** I wrote "the generator runs at generation, the loader at
   consumption, and nothing stands between them" in one commit -- then supplied a duplicate-key check
   only and stopped. CRO~X found the other half one commit later. Separately, I rebuilt a
   self-blindness class I had banked hours earlier the same night.
3. **THREE CONSECUTIVE SELF-ASSESSMENTS OF THE CONSUME GATE WERE WRONG IN THE SAME DIRECTION** -- I
   judged it sound, an external attack found it was not. That is a rate, not an accident.
4. **My isolation claim was stated at the wrong grain** ("the tranche will avoid that directory") when
   the sources live beside the pair. A protection stated at a grain the work makes impossible reads as
   cover while every edit lands next to the thing.
5. **A stale heartbeat naming a resolved blocker** read as a live gate and recruited COO~X into
   triaging a wait that no longer existed.
6. **Two near-misses caught before they became findings:** `rc=$?` after a pipe read `tail`'s status;
   a case-sensitive grep returned a false zero on the boundary record -- during a verification I was
   performing precisely to avoid trusting a summary.
