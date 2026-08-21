# 0.8.0_AE_CloudComp~A (LANE) -- comp-adversary control 2: A3 discharged non-vacuously + mutant M3; the assigned positive control measured UNFIREABLE (0226-0310Z)
**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Window
2026-08-21 ~0226Z -> ~0310Z. Whole session -- this lane was spawned tonight on Andrew's explicit word ("give it to a new agent 0.8.0_AE_CloudComp~A") for ONE bounded job. No prior log for this lane instance; the older `~A` commits in git (NFRA_SCRIPTGEN TRIAL-1, @dbbe85a807 and earlier) are a DIFFERENT lane session from 08-06/07 and are not this window.

## What happened
1. **Startup.** `/watcher`: registered `0.8.0_AE_CloudComp~A` (PID 16352), armed the persistent inbox Monitor (task `bvzgrwmw5`) -- confirmed by the Monitor actually DRAINING two messages, an agent-side receipt rather than a `ps` inference (Rule 22b). No watcher existed for `~A`; the live `0.8.0_AE_CloudComp` base watcher was a PEER's and correctly left alone. Zero crons armed. `/cloud-ops` loaded.
2. **Read before building, and it changed the job.** MSTR's 64164 routed the full A1-A5 bar to this lane. But HEAD already carried @f5bbfaf66e -- base had landed the control-2 repair (A1+A5) AND run mutant A4-M1 before I spawned. Per MSTR's "coordinate rather than duplicate" I did NOT rebuild it; I opened coordination with base (64165) and took only the two arms base's evidence lacked: **A3** and **mutant M3**. Base confirmed the division (64166/64167).
3. **The measurement that reframed A3.** The defect lives between `self_test`'s HEAD read (`:260`) and `compose()`'s OWN HEAD read (`:171`). I timestamped both `rev-parse HEAD` calls in live runs: **median 205.2 ms** (range 55-364, n=5). A full `--self-test` is **~16,500 ms**. So a HEAD-before/after-the-RUN oracle measures a span **~80x wider than the defect occupies** -- MOVED-MID-RUN does not establish the advance fell in the gap. Consequence, MEASURED not argued: a background committer landed **10 commits in ~62s** (~1 per 6.2s) with HEAD advancing between EVERY iteration, and the window was crossed **0/4**. Ambient churn crosses at ~3% per iteration.
4. **The oracle + the matrix.** Replaced inference with direct measurement: `setup_head` vs the sha `compose` stamps into its own `read-vintage:` header -- the exact two reads the defect sits between. Both predicates (pre-fix @0d48f454f6, landed @f5bbfaf66e) evaluated on the SAME composed output. 5 cells, 2 tools x 2 window states:

   | # | tool | window | crossings | OLD c2 | NEW c2 |
   |---|---|---|---|---|---|
   | 1 | FIXED | quiet | 0/1 | PASS | PASS |
   | 2 | FIXED | injected | **3/3** | PASS | **PASS** |
   | 3 | **M3** | quiet | 0/2 | **PASS** | **FAIL** |
   | 4 | **M3** | injected | **2/2** | **FAIL** | **FAIL** |
   | 5 | FIXED | concurrent churn | 0/4 (10 commits) | PASS | PASS |

   M3 = the landed tool with ONLY the pre-fix printing guard restored; verifier untouched, so it breaks the OBSERVABILITY of the verification path, not its correctness -- byte-faithful to the pre-fix state. **Row 3 is load-bearing: same output, same run, OLD PASS / NEW FAIL** -- the rewritten control tells "verification healthy" from "verification invisible". **Row 4 reproduces MSTR's 02:07Z false-FAIL ON DEMAND**, which is what gives the FIXED greens their teeth (it proves the old predicate is ABLE to fail under the condition).
5. **THE FINDING, and it is against the BAR not the fix.** The positive control assigned to this lane -- *"old-c2 FAILS where new-c2 PASSES proves the crossing"* -- **CAN NEVER FIRE ON THE FIXED TOOL.** Row 2: crossed 3/3, OLD still PASS, because A5's VERIFIED line now puts the real sha in the output so `head in out` is satisfied by the verification path rather than only the header. **A5 incidentally repaired the old predicate's SYMPTOM while leaving its BLINDNESS intact.** Run as specified, I would have looped forever waiting for a failure that cannot occur and reported an A3 green that could not have failed -- an instrument-that-cannot-say-otherwise INSIDE the acceptance of a finding about exactly that class. Surfaced as a defect in the CONTROL; did NOT repair the bar unilaterally. MSTR recorded it as theirs (64228) and adopted the header-sha oracle as the specified control wherever the bar re-runs.
6. **Committed @d745b8a341** (record + matrix transcript + harness). Push REFUSED by the LD-0367 integrator-only gate and **NOT overridden**; MSTR swept it to `origin/CLOUD` at @fd4f9983b8. Base issued the close (64226); MSTR ACCEPTED Phase 1 (64228) and is putting the phase gate to Andrew rather than self-starting Phase 2.
7. **Surfaced, not absorbed.** Draining the lane inbox turned up **msg 59074 -- a CTO~D ruling dated 20260807T025931Z, unread 14 days** because no `~A` lane was live. It carries two live GOs plus CTO~D's finding that `org/compiler-tools-log.md` has not been written since 07-29 while `tool_activity_emit_local.sh:8` still names two partitions off it -- 2 of 5 (40%) of the COMPLEARN catalog fed by a file nobody writes. ACKed for an honest READ clock, routed to base + CTO (64222), NOT taken. Base accepted item 1 into queue behind the frozen-partition adjudication.

## Compiler Tools
| tool | invocation | result |
|---|---|---|
| comp-adversary (SUBJECT under test) | `--self-test` x ~14 across matrix cells + real-plane runs | PASS 4/4 on the fixed tool every time incl. 3/3 measured window crossings; FAIL on M3 as designed |
| comp-adversary | `compose()` via imported module, 13 composed outputs | PASS -- source-1 denominator `2 attempted / 1 verified / 1 UNVERIFIABLE` stable |
| commit-gate.sh | on the harness `.py`, 2 runs | **FAIL then PASS** -- correctly blocked on ruff E401 (multi-import line) + E741 (ambiguous `l`); fixed, re-ran clean. The gate did its job on my code. |
| safe-commit.sh | `--author "0.8.0_AE_CloudComp~A ..." -F <msgfile>` | PASS @d745b8a341; risk-reflex CLEAN (3 files vs 1817 danger nodes, denominator printed) |
| git push | bare | **BLOCKED (correct)** -- LD-0367 integrator-only on CLOUD; not overridden |

**What worked:** the commit-gate catching my own ruff violations, and the `-F` message-file form (Rule 14a F-010) -- my message body carries backticks and `$(`-adjacent text that a `-m` would have shell-evaluated.
**No comp-which / comp-find / comp-estate run, and the reason:** the entire subject was ONE file named in the task order with source lines already cited (`.tools/comp-adversary:253-266`) -- there was no search to route. Every claim here is grounded on reading that file and EXERCISING it, not on locating it.
**Gap found:** none in the comp-tooling. The gap found was in the ACCEPTANCE BAR (item 5 above), which no tool covers.

## Verification (AE addition -- no deploy in this window; this is the artifact-integrity proof)
No Terraform, no Lambda, no EC2, no S3 -- repo-local only. The verification that matters here is that I produced evidence WITHOUT touching the artifact under test. Actual output:

```
=== A4 RESTORE PROOF: shared .tools/comp-adversary byte-identical to baseline? ===
37a555aeeb2323e5dbc264ec0e7d496f6e9aaec7ecde2bafaf735d16b42fe459 *.tools/comp-adversary   <- after
37a555aeeb2323e5dbc264ec0e7d496f6e9aaec7ecde2bafaf735d16b42fe459 *.tools/comp-adversary   <- baseline
--- git says: ---
(empty = unmodified)

=== REAL-PLANE: actual --self-test on the SHARED worktree ===
control 1 (planted bogus commit flags UNVERIFIABLE): PASS
control 2 (real pin VERIFIED on the printed verification path; source-1 denominator 2/1/1 -- discriminates, HEAD-churn-immune): PASS
control 3 (--open emits empty-context declaration, no complement rows): PASS
control 4 (family-shape sections present): PASS
self-test: PASS 4/4
```

**Method choice, deliberate:** both mutants ran as a scratchpad COPY with cwd set to an isolated linked worktree (throwaway branch `scratch/adv-a3-023918`, never pushed, `worktree remove` + `branch -D` at teardown), so `repo_root()` resolved identically while the shared tree stayed clean. ~8 seats live in this worktree; a transiently-broken `.tools/comp-adversary` could be picked up by another seat's run or swept into an unrelated `safe-commit` pathspec (the @6d14f2d15 "test subject" class). Churn commits were `--allow-empty` scaffolding inside that worktree only, disclosed via `# never-override:` markers.

## MCP traffic
9 messages handled. Significant: **IN** -- MSTR 64164 (the assignment + A1-A5 bar), base 64166/64167 (division of arms + A3 loop transcript), MSTR 64193/64203 (law-edit broadcast on hand-appended `Z`, then its own STATUS retraction -- the gate refused the landing), base 64226 (CLOSE, A1-A5 MET both seats), MSTR 64228 (PHASE 1 ACCEPTED + owns the bar-design finding), CTO~D 59074 (14-day-unread, routed on). **OUT** -- 64165 coordination-not-duplication to base, RAVC 64218/64219/64220 to base/CTO/MSTR, 64222/64223 routing the orphaned COMPLEARN ruling. All READ-ACKed via `ack_messages` (D0_TIGHTENING T1).

## Blockers
None. The one dependency -- @d745b8a341 unpushed under LD-0367 -- resolved when MSTR swept it to `origin/CLOUD` @fd4f9983b8; confirmed by `git branch -r --contains d745b8a341` -> `origin/CLOUD`.

## Current State (zero-context handoff)
- **`.tools/comp-adversary` (FILE) is UNCHANGED BY THIS LANE.** sha256 `37a555aeeb...fe459`, identical before and after. The repair itself is base's @f5bbfaf66e; `:211` carries the finding in-code.
- **Bar A1-A5 MET across both seats**, closed by base (64226), ACCEPTED by MSTR (64228). Andrew's sequence steps (1) repair and (2) re-run across a live commit window are discharged.
- My evidence, all committed @d745b8a341 and published @fd4f9983b8, in DIR `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/`: `COMP_ADVERSARY_C2_A3_VACUOUSNESS_CONTROL_AND_M3_20260821.md` (the record + full matrix), `COMP_ADVERSARY_C2_A3_MATRIX_TRANSCRIPT_A.txt` (raw per-iteration output), `COMP_ADVERSARY_C2_A3_HARNESS_A.py` (re-runnable harness). Base's siblings: `COMP_ADVERSARY_C2_ACCEPTANCE_20260821.md` @fd4f9983b8, `..._A4_TRANSCRIPT.txt` (M1), `..._A3_LOOP.txt`.
- **Two instrument errors are written INTO the record, not around it** (base's own framing): base's A3 loop oracle was ~80x too wide, and the positive control base assigned cannot fire on the fixed tool.
- **Adopted for re-runs of this bar:** the direct header-sha oracle, and INJECT the crossing rather than wait for it.
- Scratch worktree + branch torn down; `git worktree list` shows no `adv-a3` entry.
- Scope fence held throughout: one control, not a rewrite. Compose path, declaration output, L0a boundary_report family shape, five stages, declared-exclusions contract -- untouched, not in question, no defect found.

## Next Steps
- [0.0.0_AB_MSTR] Phase 2 (skill + design home + comp-which vocabulary) is UNBLOCKED but MSTR is correctly putting the phase gate to **Andrew** rather than self-starting on their own read of "discharged". Nothing at this lane waits on it.
- [1.0.0_SA_CTO] My A4 design question stands: M1 (correctness regression) and M3 (observability regression) are DIFFERENT mutants and my read is the control must keep failing on BOTH -- a declaration whose verification path goes SILENT has broken the L0a contract even when the verifier is right. Base's read matches; yours is the arch call.
- [0.8.0_AE_CloudComp] Owns COMPLEARN item 1 (routing 6th emitter partition, on CTO~D's CHANGED acceptance: partition built AND the `load_corpus` private read deleted in the SAME change), staged behind the frozen-partition adjudication.
- [0.0.0_AB_MSTR / 2.0.0_SA_COO] The frozen-partition finding (2 of 5 COMPLEARN emitter partitions fed by a file unwritten since 07-29) sits UNOWNED. CTO~D wanted it looked at before anything else in COMPLEARN. Not mine, not base's to adjudicate -- flagging so the 14-day silence does not extend.
- [this lane] Bounded job complete. IDLE, reachable on the Monitor, no loop armed.
