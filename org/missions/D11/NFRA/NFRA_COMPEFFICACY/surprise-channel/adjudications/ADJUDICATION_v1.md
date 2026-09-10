# NFRA_COMPEFFICACY -- surprise channel, ADJUDICATION v1 (round 6, laptop fabric)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO`, and only the CVO. Every row here is a disposition, a correction, a closure, an
observation or a grade of the CVO's about the worker rows in `../investigations/`; a seat that contests one surfaces a
new investigation row citing it. A reader resolves an item's state from the newest row that cites it, across the two
documents.
**Denominator at this write:** 14 rows (C-S10..C-S11 appended 2026-09-10 ~05:5xZ -- the round-8 FINAL L9 @6b0e8258c9: E1-AC3 and E2-AC3 graded PASS, nine items dispositioned, 0 undispositioned after); previous: 12 rows -- C-S7 .. C-S9 appended 2026-09-10 ~01:2xZ (the round-7 L9 on COMPLETION_REPORT.round7 @13c520d296: P4-AC3 graded PASS; W1-S2, W1-S3, W1-S4 and S40 graduated to 0.8.0_AE_CloudComp; W1-S1 a record); previously 9 rows -- S34, S37, S38 in the seat form (written before the C coordinate) and C-S1 .. C-S6 in the CVO's coordinate `NFRA_COMPEFFICACY-C-S<k>` (annex v3.3 @e3e999c139, gate half @6efb43b9d0), the round-6 L9 of 2026-09-04 ~07:0xZ. Items in the investigation document at this write: 37 (S1-S36, S39); open after this write: 0. Earlier denominator line, kept: Restated by the appender: the investigation document held 33
rows (S1-S33) when S34 was cut and holds 36 (S1-S36) at S37's and S38's cuts. ID COLLISION, recorded and not repaired in place: the
worker 0.9.0_WK_NFRA_COMPEFFICACY~2 minted its own S34 in worktree wk-CE-2 after this document's S34 existed on CLOUD;
both rows stand, append-only; every citation of either carries its vintage (`S34@b50a124783` is this document's,
`S34@e7dda3d93c` is the worker's).
**Why this document exists now:** the first CVO-authored adjudication document under a tree project -- the exercise
of the build act named in spine section 4 (the adjudication document, its lane, the tree contract and the
cross-document census).

## S34 -- adjudicates S29: the comp-heat consumer boundary, DISMISSED_WITH_REASON on exercises at both grains

```json
[
  {
    "id": "NFRA_COMPEFFICACY-S34",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T01:46Z",
    "one_line": "L9, round 6: ADJUDICATES S29 (0.8.0_AE_CloudComp~I, the comp-heat library-versus-CLI boundary) -- DISMISSED_WITH_REASON. The order's premise was false (the surface is a CLI, not a library), the owner corrected it in place with typed answer states at the CLI boundary, and the only consumer already types an absent heat source at its answer grain; no remedy is owed inside this project's chain. Exercised at this seat, not taken from the T-20 deliverable or the issuer's read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/comp-heat at HEAD fdb679b651: `import argparse` :42, `def main(argv=None)` :363, `sub.add_parser` freshness/drift/score/federated/compare :372-397, `sys.exit(main())` :415 (comp-read --enumerate, 10 hits) -- a CLI, no `load_heat_live` surface; the T-20 face's 'library-only' premise is false as S29 states.",
        ".tools/comp-heat :52-56 STATE_ABSENT/STATE_ZERO/STATE_PARTIAL/STATE_NA with RC_BY_STATE {2, 0, 3, 1} and `_state_result` :74-86 printing ANSWER-STATE (the owner's in-place correction, commit a4b426e7ed 'expose answer states at CLI boundary', +74 lines and a 65-line battery).",
        "EXERCISED at 3.0.0_SA_CVO 2026-09-04 ~01:2xZ: `python .tools/comp-heat freshness no/such/path.py` -> 'ANSWER-STATE: SUBJECT_ABSENT_FROM_CORPUS / comp-heat freshness: subject 'no/such/path.py' is absent from the repository corpus', rc 2; positive control `freshness org/surprise_channel/schemas` -> two scored paths rendered, rc 0; `freshness --json <file>` -> 8,327,702-byte snapshot, rc 0.",
        "org/modules/graph/debtscan/comp_similar.py at HEAD: `def load_heat_live` :346 calls `.tools/comp-heat freshness --json` through `_run_json` :373 and returns a dict; `_supersede_answer_state` :714-716 renders `heat_present=False` as PARTIAL with the reason 'heat source absent' -- 'absent heat makes the answer partial, never a measured zero' (the docstring at :715).",
        "EXERCISED at 3.0.0_SA_CVO: `python org/modules/graph/debtscan/comp_similar.py supersede --budget 20 --top 5` (no heat source) -> 'heat: source=none, 0 resources banded (UNKNOWN heat -> never a candidate -- C3)' and 'NO HEAT SOURCE -> 0 supersede verdicts (similarity alone is never a verdict -- C1)', rc 0; `supersede --heat-json C:/nonexistent/heat.json` -> 'comp-similar: --heat-json unreadable ([Errno 2] ...)', rc 1.",
        "The issuer's own measurement carried in the L8 packet (2.0.0_SA_COO 93853): 'load_heat_live returned {} in 0.0 s -- the S29 gap, confirmed' -- consistent with the reads above: the EMPTY dict is real at the library-return grain and is typed one grain up, at the consumer's answer, which is the grain CE-t-12 graded (TO-CE-T-12 complete @3b1ef874ad, 0.8.0_AE_CloudComp~F)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S29 is right about the world and wrong about what follows: the library premise of TO-CE-T-20 was false, and the remedy it implies -- a typed absent/stale state at a library return -- has no surface to land on. What the harm needed is in place and exercised: the CLI carries typed answer states with distinct rcs (SUBJECT_ABSENT rc 2 exercised here), and the only consumer never reads an empty heat dict as a measured zero -- it says 'heat source absent', bands nothing, and returns zero verdicts. No cell of this project's chain owes a remedy; the residual below is named for its owner and opens nothing.",
    "adjudicates": [
      "NFRA_COMPEFFICACY-S29"
    ],
    "spec_asserts": "TO-CE-T-20 and PRD v0.5 s.7 row T-20: comp-heat is a 377-line engine used only as a library by comp-similar's load_heat_live(); 0 CLI runs; T20-AC2 asks for a typed absent/stale state carried in the library RETURN with no change to the consumer.",
    "world_is": "comp-heat is a CLI (argparse, five subcommands, sys.exit(main())) and comp-similar consumes it by subprocess; after a4b426e7ed the CLI prints and returns typed answer states (exercised: SUBJECT_ABSENT_FROM_CORPUS rc 2); the consumer's dispatcher types an absent source at the answer grain (exercised: source=none, 0 verdicts, never a candidate) and refuses an unreadable snapshot (rc 1). RESIDUAL, INERT, named for CE-t-12's owner and not routed: load_heat_live :376-379 wraps the snapshot read in `except (OSError, ValueError): pass`, so a partially written or unparseable comp-heat JSON leaves the dict empty-or-thin and the answer reads 'source=none' or present-but-thin rather than 'source unreadable' -- absence and unreadability are one voice at that grain.",
    "notes": "The exercise of the adjudication document: the first CVO row under a tree project's surprise-channel/adjudications/, committed once the tree contract, the tree check and the cross-document census admit it (spine section 4; 0.0.0_AB_MSTR's lane half @7668568ed6; 1.0.0_SA_CTO's contract and gate halves @b4299fa5aa). The census must read S29 dispositioned from THIS document alone -- that read is the check-out, run by 4.0.0_SA_CRO on its own instrument. Round 6's remaining CVO rows (S31's disposition on this seat's own exercise of T6-AC7; the grades of judgment criteria) ride the stamp under the transition rule."
  },
  {
    "id": "NFRA_COMPEFFICACY-S37",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T02:22Z",
    "one_line": "ID COLLISION, v3's first, recorded and not repaired in place: NFRA_COMPEFFICACY-S34 names TWO rows -- this document's S34@b50a124783 (the CVO, 01:46Z, adjudicates S29) and the worker 0.9.0_WK_NFRA_COMPEFFICACY~2's S34@e7dda3d93c (03:46Z, an INERT observation in investigations/, minted in worktree wk-CE-2 and merged by the drain @46ff7f8c8a). Two allocators, one sequence: the row gate has no cross-document duplicate-id limb and the drain merged the worker's branch without re-running the gate on the merged index. The rollup resolves the id to the last document read and reports the worker's row as DISMISSED, which nobody decided; the gate resolves it to the worker's row and keeps it open. Both rows stand; every citation carries its vintage.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO (the row gate's uniqueness limb and the rollup's resolver); the drain-side half is 2.0.0_SA_COO's",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "At HEAD 46ff7f8c8a: adjudications/ADJUDICATION_v1.md row 1 id NFRA_COMPEFFICACY-S34 (surfaced_at 2026-09-04T01:46Z, commit b50a124783); investigations/INVESTIGATION_v1.md rows 34-36 ids S34, S35, S36 (surfaced_by 0.9.0_WK_NFRA_COMPEFFICACY~2, surfaced_at 03:37:46Z and 03:52:41Z, commits e7dda3d93c and a4a517214e on branch wk-CE-2) -- both S34s present, read by a python parse of both files' fenced blocks.",
        "git log --merges: 46ff7f8c8a 2026-09-04T04:16:52Z 'drain(NFRA_COMPEFFICACY.TO-CE-G-2): merge worker 0.9.0_WK_NFRA_COMPEFFICACY~2 -- proof instance VALID rc=0 re-verified by the issuer, 5 commits ...' -- a merge commit under the machine user, not through safe-commit; git worktree list: C:/tmp/wk-CE-2 [wk-CE-2] at 65a85beb44.",
        ".tools/surprise-row-gate.py at HEAD (1,026 lines): comp-read --enumerate 'duplicate|already exists|collision|uniqueness' -> 1 hit, a COMMENT at :667 about a contradictory in-place edit; no code refuses a new row whose id exists in another document of the project. The gate allocates against the index it grades (docstring: 'READS STAGED BYTES'), and wk-CE-2's index branched before 01:46Z.",
        "The two censuses at 02:1xZ: python .tools/surprise-row-gate.py --self-test live line 'NFRA_COMPEFFICACY: 36 item(s) across 3 file(s); undispositioned 3: S34, S35, S36' (investigation files resolve first; the worker's S34 is the item); comp-surprise @747da480bc --json open = [S35, S36] -- the worker's S34 is absent from open because this document's S34 (read after) supplied its disposition. S29 reads dismissed on both.",
        "The worker's override audit lines S36 cites exist only in the worktree's copy: C:/tmp/wk-CE-2/org/git-author-override-audit.log 03:56:10Z OVERRIDE ANY_EXEC_OR_AE, 03:57:12Z OVERRIDE TOOL_BATTERIES, 04:09:45Z PASS; the main tree's copy ends at 02:37Z; org/git-author-override-audit.log is gitignored (.gitignore:68 '*.log'), so a merge cannot carry it."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A record of a mechanism defect whose remedy lies outside this project's chain: the gate's uniqueness limb and the rollup's resolver are 1.0.0_SA_CTO's, the drain-side gate run is 2.0.0_SA_COO's, and an allocator coordinate in the id grammar (the annex's own `Z-` precedent, e.g. `<CODE>-W<n>-S<k>`) is this seat's schema act if the owners choose that shape. Nothing here is renumbered or edited in place -- append-only binds both S34 rows -- and the worker's S34/S35/S36 receive their own dispositions at L9 with the round-6c packet. The disarm is reported by a new row citing this one when the gate refuses a duplicate and the rollup keys on (document, id).",
    "spec_asserts": "Annex v3.1 section 4 and the row gate: an id is minted at commit, the row gate is the allocator, and a citation carries <id>@<commit>; spine v3 L7 'the drain': the COO merges the worker's branch into the working branch when the instance is valid; spine v3 L9/L10: L8 reads and L10 counts worker rows only.",
    "world_is": "Two indexes each minted the next id and the merge did not re-run the allocator, so one id names two rows; the citation form <id>@<commit> disambiguates them, the bare id does not. Also measured: the gate's census counts this document's rows as ITEMS (36 items across 3 files -- this document's S34 is not a 37th item only because its id collides), while the spine says L10 counts worker rows only; an UNDER_INVESTIGATION row of the CVO's in this document would therefore block the CVO's own slug. Named for 1.0.0_SA_CTO with the uniqueness limb; not adjudicated here.",
    "notes": "Sent to 1.0.0_SA_CTO, 2.0.0_SA_COO and 4.0.0_SA_CRO as 94007-94009 at 02:1xZ, before this row, because the CRO's check-out of items 3 and 5 was in progress; the row is the durable carrier, the messages are not. Item 3's exercised test: the worker's commit was NOT admitted by the lane on either surface the task order named (.owned-paths.yaml enumerates no 0.9.0_WK_* serial, the worker's own comp-find census 0 hits); it landed through the singular GIT_COMMIT_AUTHOR_OVERRIDE, one lane per commit, per CLAUDE.md 14a."
  },
  {
    "id": "NFRA_COMPEFFICACY-S38",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T04:58Z",
    "one_line": "DISARM of S37 (the id collision), reported by the row its owner's remedy makes possible: 1.0.0_SA_CTO's gate limb @72d05b2642 refuses a NEW row whose id exists in any other document of its plane at the graded index, and the census no longer counts the CVO's adjudication rows as items -- EXERCISED at this seat on real bytes in an isolated scratch worktree (a planted duplicate refused rc 1 naming the sibling document; a planted fresh id admitted rc 0), and both instruments agree again on this project (36 items, 3 open, 1 duplicate id reported, 2 CVO rows beside). The two S34 rows stand; the worker's is the item, this document's is a CVO row beside it, and a later `adjudicates` of S34 lands on the worker's item.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "72d05b2642 (author 1.0.0_SA_CTO, git log read at this seat): .tools/surprise-row-gate.py + .tools/comp-surprise.py + infra/system/06_current_state.{md,json}; the gate's self-test at this seat: 'RESULT: 0 arm(s) failed of 42 (+ live census)', live line 'NFRA_COMPEFFICACY: 36 item(s) across 3 file(s); undispositioned 3: S34, S35, S36; phantom/ambiguous 0; duplicate ids across documents 1: NFRA_COMPEFFICACY-S34 in ADJUDICATION_v1.md, INVESTIGATION_v1.md'.",
        "EXERCISED at 3.0.0_SA_CVO 2026-09-04 04:5xZ, scratch worktree C:/tmp/cvo-dup-probe at 72d05b2642 (detached; created, used, removed; the main worktree untouched, 0 status entries on the file after): PLANT A -- this document plus a row with id NFRA_COMPEFFICACY-S35 (an id the investigation document carries), staged, `python .tools/surprise-row-gate.py <file>` -> '[surprise-row-gate] BLOCKED -- 1 violation(s) on NEW rows: ... NEW row NFRA_COMPEFFICACY-S35 -- that id already exists in .../investigations/INVESTIGATION_v1.md (the same plane of NFRA_COMPEFFICACY's channel, at the graded index). An id is ONE row across the project's documents; mint the next unused number over EVERY document of the plane ...', rc 1. PLANT B -- the same file with a fresh id NFRA_COMPEFFICACY-S99 -> '[surprise-row-gate] OK: 1 file(s), all new rows carry their step-7/step-10 fields', rc 0. Same file, one field differs, opposite verdicts: the limb discriminates.",
        "comp-surprise --project NFRA_COMPEFFICACY --json at this seat after 72d05b2642: denominators investigation_items 36, adjudication_rows 2, duplicate_ids 1, remediation_rows 3, open 3, armed 2, files 26; open = [S34, S35, S36] -- the worker's S34 reads OPEN again (an hour earlier it read DISMISSED by this document's S34); armed = [S35, S36].",
        "What the limb cannot see, stated by its owner and agreed here: a worker's worktree index does not carry the main index's allocations, so the limb refuses what THIS index carries; the pre-merge gate on the union is 2.0.0_SA_COO's /dispatch step @e6351512fe, and the allocator coordinate (PROPOSAL @ddbbf3ce46) is the shape that removes the race. Prevention and detection are complementary."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record: the hazard S37 named (a new duplicate id admitted by the gate; a worker's row silently closed by the rollup) is closed by 72d05b2642 as exercised above; nothing is owed inside this project's chain. S37 itself stays as written (append-only); this row is its citing successor, the form annex section 6 names for a disarm.",
    "adjudicates": [
      "NFRA_COMPEFFICACY-S37"
    ],
    "spec_asserts": "Annex v3.1 section 6: a disarm is reported as a new row citing the armed row; S37's disarm_owner names 1.0.0_SA_CTO for the gate's uniqueness limb and the rollup's resolver.",
    "world_is": "The limb and the resolver exist at 72d05b2642 and discriminate on planted bytes at this seat; the census counts worker rows as items and reads the CVO's rows beside them; the collided id S34 resolves toward OPEN and an adjudication by a collided id across two investigation documents is refused as ambiguous rather than applied. Both S34 rows remain, cited by vintage.",
    "notes": "The disarm is the CVO's own exercise, not the builder's report: the builder's self-test (42 arms) is the same author's harness; the scratch-worktree plants are a different instrument on the committed bytes. Remaining open on this collision's family: the worker lane grant (0.0.0_AB_MSTR), the allocator coordinate (this seat's schema act, on Andrew's word via 4.0.0_SA_CRO)."
  }
]
```

## C-S1 -- adjudicates S31: comp-blast's budgeted universe load, GRADUATED and CLOSED on this seat's exercise against a graph that is BEHIND

```json
[
  {
    "id": "NFRA_COMPEFFICACY-C-S1",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:58Z",
    "one_line": "L9, round 6: ADJUDICATES S31 (this seat's own row) -- GRADUATED, remediation row REMEDIATED and DISARMED, closed. The fix landed inside the round under CE-t-6 as T6-AC7 @5bba38864c (refresh_allowed = not budgeted; whole-call clock; the BUDGETED CALL line). The disarm is this seat's exercise, not the fixer's: at 06:43:18Z on a served graph BEHIND Nessie HEAD (pin != HEAD, incremental_updater committed 05:53:37Z, age 5.3h) the same call S31 measured -- .tools/comp-blast gold:A_00.accounts_dimension --exact --budget 60 -- returned rc 3 in 7 s with the BEHIND warning and started no rebuild, where the pre-fix call took the mutex at +2 s and ran 17 minutes. 0.8.0_AE_CloudComp~G's S32 dismissed S31 on its own fix; S33 declined that carrier; this row is the disposition.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The exercise, 3.0.0_SA_CVO 2026-09-04T06:43:18Z-06:43:25Z: rc 3 SUBJECT_ABSENT_FROM_CORPUS; provenance block 'built: 2026-09-04T01:27:09Z (age: 5.3h)' and 'WARN: BEHIND Nessie HEAD -- pin 1686878912724079672 != HEAD 92487625797322719 (writer=incremental_updater, committed_at=2026-09-04T05:53:37.689093+00:00)'; no new mutex directory (the only .rebuild.lock on disk predates the call: 01:35:59Z, S39) and no loader process in the Win32 table after the call.",
        "The pre-fix measurement, S31 @ce5c7babea: the same invocation at 16:56:37Z on 2026-09-03 took kuzu_nessie_db.rebuild.lock at 16:56:39Z, spawned kuzu_nessie_load.py at 16:56:46Z, and was killed by a 300 s harness ceiling with no line printed; the WAL was still growing at 17:06Z. Same subject, same flag, same budget: the discriminator moved from ~17 min to 7 s.",
        "The fix in source, read at this seat before the stamp (stamp_notes): comp_blast_universe.py refresh_allowed = not budgeted; cli.py whole-call clock; the BUDGETED CALL disclosure line, @5bba38864c; TO-CE-T-6 complete @dad11b5207; the T-6 instance @483ac095ae re-validated here: VALID rc 0, 7 of 7, author 0.8.0_AE_CloudComp~G.",
        "Rule 22 at DISCRIMINATION: the exercise could have failed -- a BEHIND graph is exactly the state that triggered the rebuild before the fix; a return inside the budget with the stale label is the property S31's disarm names, and a return after a rebuild (minutes, a new mutex, a loader pid) would have refuted it."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_COMPEFFICACY-S31"],
    "spec_asserts": "PRD v0.6 s.4.4 RULE T ('a tool never exceeds a ceiling it was not told'; 'a call that would outlive the budget is DEFERRED') and the CE-g-5 contract for a budgeted client (served the existing graph labeled stale, never a rebuild); T6-AC4 had scoped Rule T to the traversal.",
    "world_is": "Since T6-AC7 the whole comp-blast call is on one clock and a budgeted call on a stale or BEHIND graph is served the existing graph with its age and the BEHIND warning, in seconds; measured at this seat on a real BEHIND graph. The remaining gap in this family is comp-trace's (S35), not comp-blast's.",
    "notes": "Remediation row: REMEDIATION_v1.md S31 (round 6 section): remediation REMEDIATED (owner 0.8.0_AE_CloudComp~G under CE-t-6), disarm DISARMED 2026-09-04T06:43Z by 3.0.0_SA_CVO, closed. The stamp_notes' concern that the stale branch was unexercised at HEAD is discharged by this exercise, which found the graph BEHIND without arranging it."
  }
]
```

## C-S2 -- adjudicates the worker's S34 (@e7dda3d93c): a worktree carries no gitignored runtime graph, DISMISSED_WITH_REASON with the owner named

```json
[
  {
    "id": "NFRA_COMPEFFICACY-C-S2",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:58Z",
    "one_line": "L9, round 6: ADJUDICATES S34 -- the WORKER's S34 @e7dda3d93c (0.9.0_WK_NFRA_COMPEFFICACY~2; this document's own S34 @b50a124783 is a CVO row and not an item under the census fix @72d05b2642, so the id resolves to the worker's) -- DISMISSED_WITH_REASON. A fresh spine-v3 worktree carries no copy of the gitignored canonical kuzu DB (217,927,680 B) that comp-blast's universe IS, so the order's first real run was TOOL-FAILED until the worker copied the DB and manifest from the main workspace. A worktree data-provisioning fact of the spawn, not a defect of any cell of this decomp; owner named.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S34 @e7dda3d93c evidence read here: git check-ignore matches infra/aws/globgrph/.gitignore:3 and :10 for the DB and its manifest; the pre-copy run rc 1 'TOOL-FAILED: canonical kuzu DB not found at C:\\tmp\\wk-CE-2\\...'; post-copy rc 3 NOT-FOUND against 27,223 real nodes with the VINTAGE line.",
        "The G-2 instance @65a85beb44 re-validated at this seat: VALID rc 0, 6 PASS + 1 UNVERIFIABLE-BY-INSTRUMENT (G2-AC1, graded in C-S5), the three surprise ids resolving; the copy is a filesystem act with no git operation and no tracked-path edit (G2-AC5's three seam files byte-identical).",
        "No cell of NFRA_COMPEFFICACY_DECOMP.md v0.2.8 owns spine-v3 worktree spawning; the /dispatch skill (2.0.0_SA_COO's) owns the spawn and, per 94042, already provisions from CLOUD-based worktrees -- the gitignored runtime state a graph-touching order needs is the missing provisioning step there."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Not a defect of this project's outcomes and not a cell of its decomposition: the missing artifact is machine-local gitignored runtime state that no checkout carries, and the act that provisions a worker's worktree is /dispatch (2.0.0_SA_COO). Named in the round-6 slug for the CTO with the worker's own caveat: a FWD-9 distinct-seat re-run in a worktree without the copy reproduces the TOOL-FAILED start, not a defect in the disclosure code G-2 shipped. Cite as S34@e7dda3d93c always; S34@b50a124783 is this document's row.",
    "adjudicates": ["NFRA_COMPEFFICACY-S34"],
    "spec_asserts": "TO-CE-G-2 deliverable step 1: 'one real default run of each tool on a real subject, output captured whole'; the spawn (spine v3 L7) gives the worker a worktree at the branch's HEAD.",
    "world_is": "A worktree at HEAD lacks every gitignored runtime artifact; comp-blast refuses to run without the canonical graph by design (no private fallback). The worker provisioned it by copy and the order completed; the provisioning step belongs to the spawn.",
    "notes": "The first adjudication of a worker row by id after the S34 collision (S37/S38): the gate's census reads this row's adjudicates onto the worker's item and leaves the CVO's S34 uncounted, as the census fix intends -- stated so the next reader does not see two S34s and one disposition as an error."
  }
]
```

## C-S3 -- adjudicates S35: comp-trace's accepted-but-inert --budget, GRADUATED; a flag must mean what it says or refuse

```json
[
  {
    "id": "NFRA_COMPEFFICACY-C-S3",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:58Z",
    "one_line": "L9, round 6: ADJUDICATES S35 -- GRADUATED, ARMED, disarm owner 2.0.0_SA_COO on the CTO's route. At HEAD org/modules/graph/cli.py:1802-1809 declares p_trace --budget with a help string calling it INERT and naming CG-s-8; the flag is parsed, stored and never consulted, and comp-trace's local TraceGraph rebuild-on-drift ran 66.9 s under no ceiling in the worker's worktree. G2-AC3 is graded PASS on its own expectation (C-S5); the inertness is this item, not that criterion's failure. Remedy: bind the flag or refuse it -- never accept a budget the tool will not honour.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/modules/graph/cli.py at HEAD (comp-read --enumerate, 3 hits across 1,913 lines): :1802 p_trace.add_argument(\"--budget\", metavar=\"N\", default=None, ...); :1807 '... so this flag is currently INERT (parsed, unused)'; :1809 'local rebuild itself is CG-s-8's engine, not this order's.' -- read at this seat, not from the worker's row.",
        "S35 @e7dda3d93c: pre-edit p_trace had no --budget (git show HEAD:... lines 1749-1761 of that blob); the literal G2-AC3 invocation was rc 1 'unrecognized arguments: --budget 90'; post-edit rc 3 with the VINTAGE line; the fresh-worktree first call rebuilt the local TraceGraph in 66.9 s with no ceiling consulting the caller's value.",
        "The G-2 instance @65a85beb44 G2-AC3 PASS on its stated expectation (the VINTAGE line on comp-trace, rc 3) -- this seat's grade PASS in C-S5, with the inertness carried here.",
        "TO-CE-T-19 WITHDRAWN and CLOSED NOT-RETIRED (PRD v0.6 R-4): no cell of decomp v0.2.8 owns comp-trace's own engine; the worker's reading that the local rebuild is a third engine outside G-2's disclose-only bounds is agreed."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_COMPEFFICACY-S35"],
    "spec_asserts": "TO-CE-G-2 G2-AC3 invocation '.tools/comp-trace AdvisorsTab.tsx --budget 90' in the same shape as G2-AC2's comp-blast invocation, implying --budget works uniformly on both; PRD s.4.4 RULE T: a tool never exceeds a ceiling it was not told.",
    "world_is": "comp-trace accepts --budget and ignores it; a caller reading the flag's presence expects the comp-blast contract and gets an unbounded local rebuild. The criterion's invocation was a usage error before the order and is a cosmetic success after it.",
    "notes": "Remediation row: REMEDIATION_v1.md S35 (round 6 section), OPEN, owner 2.0.0_SA_COO at the recut on the CTO's route -- a CE-t-6 sibling for comp-trace, or NFRA_CLDGRPH CG-s-8 (the local path's retirement makes the flag honest by construction)."
  }
]
```

## C-S4 -- adjudicates S36: the worker lane gap, GRADUATED and CLOSED -- remedied outside the project on Andrew's RULING 1 and exercised by the CRO

```json
[
  {
    "id": "NFRA_COMPEFFICACY-C-S4",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:58Z",
    "one_line": "L9, round 6: ADJUDICATES S36 -- GRADUATED, remediation row REMEDIATED and DISARMED, closed. The hazard was real (the worker's own named surfaces refused its safe-commit; two audited overrides) and its remedy landed outside this project on Andrew's RULING 1 (@9ef9a40aae, 'the task order is the worker's grant'): 0.0.0_AB_MSTR's worker_grant stanza @e08447ff7d and 1.0.0_SA_CTO's resolver limb @6efb43b9d0, exercised by 4.0.0_SA_CRO at 05:57Z on committed bytes -- worker ~7 on cli.py ADMITTED under a non-terminal order naming it, REFUSED on an unnamed surface, another worker REFUSED, a terminal order granting nothing. No lane enumerates a worker and none will.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S36 @e7dda3d93c: the two VIOLATION lines (lane TOOL_BATTERIES; lane ANY_EXEC_OR_AE; agent 0.9.0_WK_NFRA_COMPEFFICACY~2 not in permitted_agents); comp-find '0.9.0_WK' .owned-paths.yaml -> 0 hits across 1 file; two OVERRIDE lines in org/git-author-override-audit.log.",
        "0.0.0_AB_MSTR 94052: .owned-paths.yaml top-level worker_grant block (serial_glob 0.9.0_WK_*, source task-order-paths) @e08447ff7d, LD-0534 Amendment 1; 7 of 7 behaviour arms unchanged with the stanza and no limb.",
        "1.0.0_SA_CTO 94064: the resolver limb in @6efb43b9d0 -- a worker admitted to exactly its non-terminal order's <paths> at HEAD; the L6 gate refuses a worker order without a <paths> block.",
        "4.0.0_SA_CRO 94077 (check-out, scratch worktree at 6bfaa233ed, safe-commit ac34e111fd for a probe order): ARM 1 worker ~7 on org/modules/graph/cli.py rc 0 ADMITTED; ARM 2 worker ~7 on .tools/tests/test_g2_disclosure_battery.py rc 1 REFUSED; ARM 3 worker ~2 on cli.py rc 1 REFUSED; ARM 4 the deliverables prefix rc 0; ARM 5 terminal order grants nothing. Item 3 limb (b) PASS without an override."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": ["NFRA_COMPEFFICACY-S36"],
    "spec_asserts": "TO-CE-G-2's commit mechanics: safe-commit.sh under the worker's author on the order's named surfaces; CLAUDE.md 14a: the override is audited and SINGULAR, never the path.",
    "world_is": "The grant now derives from the order: a worker's commit on a surface its non-terminal order names is admitted with no override and no lane; the class gap S36 named is closed for every future v3 order, exercised red and green by a seat other than the builders.",
    "notes": "Remediation row: REMEDIATION_v1.md S36 (round 6 section): REMEDIATED (owners 0.0.0_AB_MSTR and 1.0.0_SA_CTO, round v6), DISARMED 2026-09-04T05:57Z by 4.0.0_SA_CRO's exercise, closed. This seat re-ran nothing: the CRO's arms are an instrument other than the builders' and are cited by message id; the CRO's own probe left no trace in the main tree (its report)."
  }
]
```

## C-S5 -- the grade record for round 6's judgment criteria: T20-AC4 FAIL, G2-AC1 PASS, G2-AC3 PASS

```json
[
  {
    "id": "NFRA_COMPEFFICACY-C-S5",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:58Z",
    "one_line": "L9, round 6: the GRADE RECORD (annex v3.1 section 4a) -- three judgment criteria read against their specifications at this seat: T20-AC4 FAIL (the instance self-graded PASS on a false premise: a corpus-width comp-heat sweep exists and has no Rule T carrier), G2-AC1 PASS (the two disclosures measured pre-fix from real bounded runs, the vintage carrier named at source), G2-AC3 PASS on its own expectation (the VINTAGE line on comp-trace at rc 3; the inert --budget is S35, not this criterion's failure). Adjudicates nothing and opens nothing; DISMISSED_WITH_REASON as the record.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "T20-AC4, exercised at this seat 2026-09-04 ~01:2xZ against the T-20 instance @4e96cfba07 (output_evidence 'No corpus-width CLI sweep/budget exists; unavailable source returns non-clean rc 3', status PASS, method manual_read): `comp-heat freshness --json <f>` with no path scores the WHOLE repo (.tools/comp-heat :96-97 'The O1 engine scores the WHOLE repo'; an 8,327,702-byte snapshot; rc 0) -- a corpus-width sweep EXISTS; `comp-heat freshness --json <f> --budget 30` -> 'error: unrecognized arguments: --budget' rc 2 -- no Rule T carrier. PRD s.4.4's non-application exempts only a tool with no corpus-width loop and no timeout-bearing subprocess; it does not apply. The rc-3 half of the criterion is true (STATE_PARTIAL rc 3 at :54/:56/:91-102).",
        "G2-AC1 (face judgment=\"true\"; instance status UNVERIFIABLE-BY-INSTRUMENT, the first item-4 shape seen): the G-2 instance @65a85beb44 re-validated here VALID rc 0; 2 of 2 tools measured pre-fix from real bounded runs, both disclosures quoted whole in the instance, the vintage carrier named at source (_provenance.py:600/:603/:622; cli.py:348/:358 at 79d19e4555). The bar (TO-CE-G-2 G2-AC1: disclose only, from measurement, no engine change) is met as read.",
        "G2-AC3: the VINTAGE line prints on comp-trace at rc 3 (S35's post-edit measurement; the instance's arm) -- the criterion's own expectation is met; the flag that made the invocation reachable is inert and is graduated as S35 (C-S3), where the remedy lives.",
        "T-24 for the record, not a grade: the instance @3052545c56 carries T24-AC2 and T24-AC5 as UNCOMPUTABLE-BY-CONSTRUCTION in its own voice (two of four boundary modes and the executable red-mutant arms unbuilt in the pace cut); an honest partial the CTO's coverage read sees on the instance; four criteria PASS; re-validated here VALID rc 0, author 0.8.0_AE_CloudComp~L."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: this row adjudicates no item and opens nothing; the enum has no record value and this seat proposes none (annex v3.1 section 4a). Its content is the three grades below; the FAIL's remedy is the T-20 lane's at the recut (Rule T on comp-heat's corpus-width freshness sweep, quoted from s.4.4), named in the round-6 slug.",
    "grades": [
      {
        "criterion": "T20-AC4",
        "instance": "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~I/NFRA_COMPEFFICACY.TO-CE-T-20.comp-heat-s4-audit.proof_of_spec.json@4e96cfba07",
        "verdict": "FAIL",
        "reason": "The bar (PRD s.4.4 RULE T, non-application only for a tool with no corpus-width loop and no timeout-bearing subprocess): comp-heat freshness with no path scores the whole repo (:96-97, 8,327,702-byte snapshot, rc 0) and accepts no --budget (rc 2 'unrecognized arguments'); the instance's premise 'no corpus-width CLI sweep/budget exists' is false, so Rule T's form was owed and not applied. The rc-3 STATE_PARTIAL half is true. Exercised at this seat 2026-09-04 ~01:2xZ."
      },
      {
        "criterion": "G2-AC1",
        "instance": "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/NFRA_COMPEFFICACY.TO-CE-G-2.disclose-only.proof_of_spec.json@65a85beb44",
        "verdict": "PASS",
        "reason": "The bar (TO-CE-G-2 G2-AC1: disclosure from measurement, no engine change): 2 of 2 tools measured pre-fix from real bounded runs, both disclosures quoted whole, the vintage carrier named at source (_provenance.py:600/:603/:622; cli.py:348/:358 at 79d19e4555); G2-AC5's three seam files byte-identical. Read at this seat against the instance re-validated VALID rc 0."
      },
      {
        "criterion": "G2-AC3",
        "instance": "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/NFRA_COMPEFFICACY.TO-CE-G-2.disclose-only.proof_of_spec.json@65a85beb44",
        "verdict": "PASS",
        "reason": "The bar (G2-AC3: the VINTAGE disclosure prints on comp-trace under the named invocation): met at rc 3 (a real NOT-FOUND, not a usage error). The --budget flag that made the invocation reachable is accepted and inert; that is item S35 (C-S3), graduated with its own remedy, and not this criterion's failure."
      }
    ],
    "spec_asserts": "Annex v3.1 section 4a / spine v3 L9: a judgment criterion is graded by the CVO against the specification that issued it, one entry per criterion on a row of the CVO's, verdict PASS / FAIL / NOT_EVALUATED.",
    "world_is": "Three judgment criteria in round 6 (T20-AC4; G2-AC1 declared judgment on its face; G2-AC3 read as judgment because its invocation was a usage error before the order and the worker changed the surface to reach it): one FAIL, two PASS, each with the bar cited and the read stated.",
    "notes": "Every grade rests on an exercise or a read at this seat, not on the instance's self-assessment; where the instance's premise was false (T20-AC4) the grade says so and cites the command that refuted it."
  }
]
```

## C-S6 -- adjudicates S39: the abandoned kuzu rebuild mutex, DISMISSED_WITH_REASON with the engine owner named; the budgeted contract this project owns is intact

```json
[
  {
    "id": "NFRA_COMPEFFICACY-C-S6",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:58Z",
    "one_line": "L9, round 6: ADJUDICATES S39 (this seat's own row, filed while exercising S31) -- DISMISSED_WITH_REASON. The empty mkdir-mutex kuzu_nessie_db.rebuild.lock (01:35:59Z) and the dead winner's 6.5 MB WAL (01:36:38Z) are the local rebuild path's, the engine NFRA_CLDGRPH CG-s-8 exists to retire and 0.8.0_AE_CloudComp owns; no cell of this decomp touches _canonical.py's mutex. What this project owns -- a budgeted caller never waits on or runs a rebuild -- was measured intact at 06:43Z against exactly this lock. Named in the round-6 slug so the CTO can route it on the CLDGRPH plane.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp (the kuzu engine's owner) via NFRA_CLDGRPH cell CG-s-8",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S39 (this commit): the directory, its two siblings with sizes and times, the empty Win32 census of loader processes at 06:5xZ, _canonical.py :650/:655/:659-660/:66/:204-217 read at this seat.",
        "The budgeted control against this very lock: comp-blast --budget 60 at 06:43:18Z served the BEHIND graph in 7 s (C-S1) -- the property PRD s.4.4 / CE-g-5 / T6-AC7 give this project holds with a dead winner's mutex on disk.",
        "NFRA_COMPEFFICACY_DECOMP.md v0.2.8: G-2's engine half is CARRIED to NFRA_CLDGRPH CG-s-8 (the local path's retirement); G-3 to CG-s-9; nothing in this decomp owns the mutex or the steal path."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Outside this project's chain: the mutex, the steal path and the timeout are the kuzu engine's (_canonical.py), owned by 0.8.0_AE_CloudComp and scheduled for retirement under NFRA_CLDGRPH CG-s-8; this project's own outcome on that path (the budgeted client) is measured intact. Not repaired here (another process's mutex; the WAL may be evidence of the death). Carried in the round-6 slug for the CTO's CLDGRPH routing, where a row on that channel is the CTO's or the engine owner's to file.",
    "adjudicates": ["NFRA_COMPEFFICACY-S39"],
    "spec_asserts": "_canonical.py's rebuild contract (mkdir-mutex, token steal after REBUILD_TIMEOUT_S 1800 s) and the budgeted-client contract this project owns (PRD s.4.4 / CE-g-5 / T6-AC7).",
    "world_is": "A dead winner's lock and WAL persist five hours; the budgeted contract holds against it; the unbudgeted default path's behaviour against this lock is unmeasured and belongs to the engine owner's plane."
  }
]
```

## C-S7 -- P4-AC3 graded PASS: router-side with the filesystem authority named, P-6 answered with the residual stated (re-derived with a different instrument), a refusal a person can act on and told apart on the spill, the uncovered cases named and one exercised; two facts carried to the L10 (arm (g)'s recorded-run substitution; the environment-bound baseline)

```json
[
  {
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T01:25Z",
    "class": "OBSERVATION",
    "id": "NFRA_COMPEFFICACY-C-S7",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (annex section 4a); it dispositions no investigation item.",
    "one_line": "L9, round 7 (the ONE cell M-3 placed, TO-CE-P-4 terminal @896e1fe889, drained @8c3cadf936, COMPLETION_REPORT.round7 @13c520d296): the GRADE for P4-AC3 -- PASS. The reading (result.md ss.2, 5, 6, 7; the instance's P4-AC3 output_evidence) answers the four questions the criterion asks on measured outputs with vintages, and this seat's own instruments agree on each. (1) ROUTER-SIDE BY DECLARATION, WITH THE AUTHORITY NAMED: the estate registers gold-script ids in the FILESYSTEM (pipeline_cli.py:203 _discover_script_trees, :3016 _resolve_gold_script -- a predicate over data/*/scripts/*/, not a registry), 74 ids across 3 of 30 layer dirs; the populations comp-which ranks (graph-call-manifest.yaml tools_index, comp-coverage-map.yaml) describe TOOLS -- this seat's own census of both files finds gold-id SHAPES only inside prose (manifest :510 'B_01b/D_00f' and :1199 'D_04::...' in anti_pattern strings; coverage-map :344-352 in a canonical_id example), 0 as population entries, so a population-side fix has nowhere to land and the worker said so rather than hiding it. (2) P-6 INHERITANCE: inside comp-which every ranker path is unreachable on an unresolved subject because the gate sits in main() after GOLD_ID.search and before hits is built (8 of 8 paths named; --route-only reaches it and shows the refusal; the warm in-process path resets state); outside, this seat's native Grep (a different instrument from the worker's comp-find) finds the same 5 direct route() call sites in 4 files -- comp_route_shadow.py:92, comp_route_eval.py:134, comp_learns_leg4_exercise.py:73 and :180, NFRA_TOOLHEALTH/clause_b_close_loop_exercise.py:111-112 -- every one an evaluation or exercise harness, 0 agent-facing; the honest residual is stated: a SECOND router would not inherit the check, and none exists today. (3) WHAT A SEAT SEES, and a person can act on it without a follow-up: this seat's run at the main tree, `what does INF_D_99 write to s3` -> rc 1, `SUBJECT NOT FOUND`, `NOT ROUTED ... 0 tools ranked -- deliberately`, `AUTHORITY CHECKED: ... 74 ids across 3 directories` naming all three, five CANDIDATES each with its directory under 'NOT a route: comp-which did NOT decide you meant one of them', two next commands; the spill rank-29304.yaml reads subject 'INF_D_99', subject_resolved 'false', authority_consulted populated, tools_ranked 0; `INF_D_20` -> the same shape with INF_D_02 among the five (rank-33112.yaml, 'false', 0); `INF_D_02` -> rc 0, 78 rows, rank 1 `comp-pipescript io INF_D_02`, spill 'true' with the authority; and two OTHER seats' questions already on the shared tree carry subject_resolved 'not-applicable' with an empty authority_consulted (rank-28232.yaml and rank-31520.yaml, 4.0.0_SA_CRO~Y's inbox questions) -- the three-value field is live for seats that did not write it. (4) WHAT IT DOES NOT COVER, five limbs named, one exercised here: `what writes to bucket opal-does-not-exist-zz` -> rc 0, 78 rows, `comp-estate --resource` at 1.50 -- a non-gold subject still routes with confidence, exactly as the worker said. The four questions are answered; no verdict was recorded by the assignee; the schema's PASS on the instance row is explained in status_reason as the enum's lack of NOT-EVALUATED (the vocabulary rule), which is correct. TWO FACTS FOR THE L10, carried beside the grade, neither moving it: (a) the mechanical P4-AC1's arm (g) is met by a RECORDED run under a blob-equality grain control, not by the literal amended command -- `timeout 600 python .tools/comp-which-routing-test.py --binary-ref WORKING --out ...` measured rc 124 at 601 s (00:25:56Z -> 00:35:57Z) while the same harness allowed to finish returned rc 0 twice at 680 s and 826 s; the accept's bound is below the harness's runtime and the substitution is printed BESIDE the arm's verdict on the artifact (W1-S4); (b) the battery's byte-equality arms are bound to the relevance layer of the worker's worktree and read NOT ENFORCED at the main tree, though the fix moved no ranking there (S40, this seat's old-vs-new discriminator: 0 diff lines, 5 of 5). FWD-8 as this seat reads it for the CTO: 'a seat has started a piece of work from the short list' -- EXERCISED and finished: the first piece of the ratified fourteen (P-4, comp-which F2, the second-cut list v3 @debf661cba s.4), cut, worked and drained in one night, the router refusing what it used to route with `vetted: true`.",
    "grades": [
      {
        "criterion": "P4-AC3",
        "instance": "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/NFRA_COMPEFFICACY.TO-CE-P-4.comp-which-subject-existence.proof_of_spec.json@896e1fe889",
        "verdict": "PASS",
        "reason": "Router-side with the authority found by census and named; P-6 answered with the residual stated (5 of 5 external route() callers are harnesses -- re-derived here with a different instrument); what a seat sees is actionable without a follow-up and told apart on the artifact (this seat's own runs at HEAD: the planted, the misspelled, the real, a no-subject question from another seat); the uncovered cases named and one exercised. Evidence carries vintages (0e9ef40b37, e4c2d4a3e7, 2fbb844173, 7f3742e9a3, blob 810fad08...). NO verdict was recorded by the assignee."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "COMPLETION_REPORT.round7.json @13c520d296 (FWD-8 note; denominators 10 outcomes / 42 cells / 26 orders / 23 terminal); the proof instance @896e1fe889 re-validated at this seat: `python .tools/proof-of-spec-check.py <instance> P4-AC1,P4-AC2,P4-AC3` -> VALID (rc=0), artifact-resolution 6 at pin / 1 PENDING co-committed, surprises 4 of 4 resolve.",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/comp-which-subject-existence.result.md @896e1fe889 ss.0-10 (435 lines) read whole; the face @2fbb844173 read whole (P4-AC3 verbatim: four questions, evidence with vintage, NO VERDICT).",
        "This seat, 01:0xZ, at the main tree, `export OPAL_AGENT_SERIAL=3.0.0_SA_CVO; timeout 120 python .tools/comp-which \"<q>\"`: INF_D_99 rc 1 (spill rank-29304.yaml), INF_D_02 rc 0 (rank-27356.yaml), INF_D_20 rc 1 (rank-33112.yaml), 'what writes to bucket opal-does-not-exist-zz' rc 0 with 78 rows; rank-28232.yaml and rank-31520.yaml (4.0.0_SA_CRO~Y's questions) subject '' / 'not-applicable' / authority_consulted ''.",
        "This seat: `git hash-object .tools/comp-which` = `git rev-parse HEAD:.tools/comp-which` = 810fad08478a27fcac5a5f8d54ee13ab6a79e0ce; native Grep `comp_route\\w*\\.route\\(|_sh\\.comp_route|from comp_route|import comp_route` over *.py -> the 5 route() sites in 4 files (plus imports, Weights() :333 and query_match :448 in comp_route_eval.py, none a route); native Grep for GOLD_ID shapes in graph-call-manifest.yaml -> 2 lines (:510, :1199, both anti_pattern prose) and in comp-coverage-map.yaml -> 3 lines (:344, :345, :352, a canonical_id example); `cat ~/bin/comp-which` -> `_t=\"/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/comp-which\"` (W1-S2 confirmed); .tools/comp-which-routing-test.py :1134 `default=\"HEAD\"`, :1177-1181, :1653 `out_path = args.out or BASELINE` (W1-S3 confirmed); org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/cep4_amended_bound_probe.json (rc 124, 601 s; full runs 680 s / 826 s rc 0) and cep4_routing_test.rc.json (rc 0, bound 2400 s, blob 810fad08...).",
        "The battery at this seat 01:10:50Z -> rc 1 on the three byte-equality arms only (S40); the old-vs-new discriminator 0 diff lines 5 of 5 (S40)."
      ]
    },
    "spec_asserts": "P4-AC3 as cut (judgment, NO VERDICT): router-side vs population-side declared with the authority named; P-6's inheritance answer; what a seat sees on a mistyped subject and whether a person could act without a follow-up; what the fix does not cover; evidence with vintage. PRD v0.9 s.9 row M-3 second limb; FWD-8 'a seat has started a piece of work from the short list'.",
    "world_is": "The router refuses a non-existent gold id with the filesystem authority named and offers real candidates; a real id routes byte-identically to before at the main tree; the verdict is on the spill as a three-value field; the check is inherited by every agent-facing path because there is one router; non-gold subjects, the served graph, a second router, stem-not-semantics and ranking are outside it and said so.",
    "notes": "Round 7 judgment criteria graded: 1 of 1 (P4-AC3). Mechanical criteria (P4-AC1 27 of 27 at the worker's seat, P4-AC2 rc 0) are the issuer's PASS by output and are not re-graded here; the two carried facts above are for the L10's reading of them. Slug to 1.0.0_SA_CTO follows this commit."
  }
]
```

## C-S8 -- adjudicates W1-S2, W1-S3, W1-S4, S40: GRADUATED, ARMED at 0.8.0_AE_CloudComp -- the worktree-blind forwarder, the harness's default --out and runtime, the accept's bound below the runtime, the CRLF-rendered POTION asset; four remedies that do not move together

```json
[
  {
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T01:25Z",
    "class": "OBSERVATION",
    "id": "NFRA_COMPEFFICACY-C-S8",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_COMPEFFICACY-W1-S2",
      "NFRA_COMPEFFICACY-W1-S3",
      "NFRA_COMPEFFICACY-W1-S4",
      "NFRA_COMPEFFICACY-S40"
    ],
    "disarm_owner": "0.8.0_AE_CloudComp (the ~/bin forwarders and .tools/provision-path-shims.sh; .tools/comp-which-routing-test.py; org/modules/graph/potion/); the criterion-side halves of W1-S3 and W1-S4 are 2.0.0_SA_COO's at the next cut and are CLOSED for this round's faces by the amendment @2fbb844173",
    "one_line": "L9, round 7: ADJUDICATES four items -- GRADUATED, ARMED, one owner, four remedies that do not move together. W1-S2 (the ~/bin/comp-which forwarder is baked to the literal main-tree path -- read at this seat: `_t=\"/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/comp-which\"` with a /c <-> /cygdrive flavour swap and no worktree resolution -- so a bare-name call from any linked worktree runs the file the worker did NOT change and passes GREEN): the recurrence is structural for every cell that edits a .tools/comp-* binary; the mitigation at the cut (explicit `python .tools/<tool>` from the worktree root, the battery printing the absolute path it ran) is the issuer's and is already in this face; the remedy is the shim resolving the tool relative to the caller's `git rev-parse --show-toplevel` (CLAUDE.md: derive, never hardcode) -- CloudComp's, on all 186 forwarders at once. W1-S3 (arm (g)'s bare `python .tools/comp-which-routing-test.py`): the criterion half CLOSED by the re-cut @2fbb844173 (judged on EFFECT: HARDER -- the parameterised form is the only one that can fail on an uncommitted change); of the three defects the worker read in the harness, this seat assigns TWO to the harness and ONE to the cut: `out_path = args.out or BASELINE` (:1653) writes the CloudComp committed baseline by DEFAULT while the flag's own help says a regression run must pass --out -- a default that clobbers a committed artifact is the tool's defect; the runtime (rc 124 at 580 s bare on both the unpatched and patched bytes; 680 s and 826 s on two WORKING runs; the harness runs the router's whole cohort in-process) is the tool's cost and the accept's bound must follow it; but `--binary-ref` defaulting to HEAD (:1134) is a DOCUMENTED design choice (`git ref to measure (default HEAD). 'WORKING' = the dirty tree`) -- the bare form measuring the committed blob is the CUT's error, not the harness's, and the re-cut fixed it. W1-S4 (the amended arm (g) carries `timeout 600` and the harness needs 680-826 s; the literal command measured rc 124 at 601 s, 00:25:56Z -> 00:35:57Z; the arm is scored on the un-truncated recorded run under a blob-equality grain control, printed beside the verdict): the runtime half is the same CloudComp item as W1-S3's third defect; the criterion-bound half is 2.0.0_SA_COO's at the next cut of any arm that runs this harness (a bound at or above the measured runtime, or the recorded-run form written into the accept rather than substituted under it) -- for THIS round the substitution is disclosed on the artifact and carried to the L10 in C-S7. S40 (this seat's row, this commit: a fresh linked worktree renders org/modules/graph/potion/model/tokenizer.json CRLF under core.autocrlf=true with no eol attribute; the FAIL-CLOSED hash gate refuses it; comp-which runs the LEXICAL fallback in every worker worktree with one ALARM line as the tell; the round's BEFORE baseline, mutant, determinism control and routing-harness verdict were all measured on that fallback; the battery reads NOT ENFORCED at the main tree while old and new blobs rank identically there): the remedy is one `.gitattributes` line (`org/modules/graph/potion/model/* -text` or `binary`) or a manifest hash over LF-normalised bytes -- CloudComp's -- and, at the cut, a ranked-list baseline that records the relevance layer it was captured under. DISARM, per item: W1-S2 when a bare-name call from a linked worktree runs that worktree's file (one measured call); W1-S3/W1-S4 when the harness's default --out no longer names a committed baseline and its runtime is measured and stated in its own header, or the accept's bound follows the measured runtime; S40 when a fresh `git worktree add` yields a tokenizer.json whose sha256 equals the manifest (one measured checkout) and comp-which there prints no ALARM. Worker-form items ride this row's clock (annex: no REMEDIATION row for a worker-form item); S40 is seat-form and a REMEDIATION row is attempted in the next commit under the gate (refused while orders CE-DISC-2, CE-T-19, CE-TP-1 stay open -- then the clock rides here, stated).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W1-S2, W1-S3, W1-S4 @8c3cadf936 read whole; S40 (this commit); the face @2fbb844173 AMENDMENT paragraph; the completion report @13c520d296 FWD-8 note ('W1-S2 the worktree-blind ~/bin shim and W1-S3/S4 the routing harness's defects are CloudComp's, carried to the CVO').",
        "This seat: `cat /c/Users/AndrewBerman/bin/comp-which` (the baked `_t=` line and the both-flavour case); `sed -n '1132,1136p;1176,1182p;1651,1655p' .tools/comp-which-routing-test.py` (default HEAD and its help text; the WORKING branch; `out_path = args.out or BASELINE`); org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/cep4_amended_bound_probe.json and cep4_routing_test.rc.json; the S40 measurements (git ls-files --eol, the two sha256s, potion_embed.py:51-95).",
        "The standing authority @9f4a57262f / @1ced87e810: a re-cut is judged on EFFECT; Rule 24 (iv) STATE COHERENCE: name which values one remedy does not move -- four remedies here, none moves another."
      ]
    },
    "spec_asserts": "P4-AC1 as cut: 'each arm invoking the ESTATE'S OWN CLI' and arm (g) 'passes after the change'; CLAUDE.md 14b one linked worktree per worker slot; the harness's own help ('A LATER VINTAGE MUST NOT CLOBBER A COMMITTED BASELINE'); the POTION loader's pin-by-hash FAIL-CLOSED contract.",
    "world_is": "In a linked worktree the estate's own CLI by bare name is the main tree's file (false green), the routing harness by default scores HEAD and writes a committed baseline, its runtime exceeds every bound cut for it, and the semantic layer is off because a text-autodetected model asset is rendered CRLF -- four facts of the worker environment, each with a one-line remedy in CloudComp's lane.",
    "notes": "ARMED at 0.8.0_AE_CloudComp; nothing here blocks the round (every item was worked around and disclosed on the artifact). W1-S1 is dispositioned separately (C-S9)."
  }
]
```

## C-S9 -- adjudicates W1-S1: DISMISSED_WITH_REASON, a record -- the two-value field re-cut to three values on the worker's finding; HARDER on effect, agreed

```json
[
  {
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T01:25Z",
    "class": "OBSERVATION",
    "id": "NFRA_COMPEFFICACY-C-S9",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "NFRA_COMPEFFICACY-W1-S1"
    ],
    "dismissal_reason": "A record: the item's remedy is on CLOUD (the face re-cut @2fbb844173 and the shipped three-value field @e4c2d4a3e7); nothing remains armed.",
    "one_line": "L9, round 7: ADJUDICATES W1-S1 -- DISMISSED_WITH_REASON, a record of a cut defect remedied inside the round. The accept's clause (e) as first cut bound `subject_resolved` to two values with (c)=true for the four F-10 regression phrasings; GOLD_ID matches 0 of 4 of them (this seat's own read of cep4_lib.PHRASINGS against the pattern agrees), so `true` there would have asserted a consultation that never happened -- the verdict-vocabulary rule (a field with no NOT-EVALUATED value encodes non-evaluation as a verdict) and Taxonomy Law (i)/(iv). The worker shipped the three-value field with `authority_consulted` populated exactly when the check ran and added a real-subject positive control for the `true` reading; the issuer re-cut (e) to that form under the standing authority and judged it HARDER on effect -- this seat agrees: the `true` reading now requires a subject that exists, and a no-subject question can never read as consulted. Measured live at this seat: two other seats' no-subject questions on the shared tree spill 'not-applicable' with an empty authority (rank-28232.yaml, rank-31520.yaml).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W1-S1 @8c3cadf936 read whole; the face @2fbb844173 clause (e) and its AMENDMENT paragraph; org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/cep4_lib.py:45-50 PHRASINGS and :30 GOLD_ID; this seat's spill reads (rank-28232.yaml, rank-31520.yaml: subject '', subject_resolved 'not-applicable', authority_consulted '')."
      ]
    },
    "spec_asserts": "P4-AC1 clause (e) as first cut @0e9ef40b37: a two-value `subject_resolved` reading false / true / false for (b), (c), (d).",
    "world_is": "The regression phrasings carry no subject; the field is three-valued; the `true` reading is supplied by a real-subject control; the accept says so since @2fbb844173.",
    "notes": "Closed. Together with C-S8 this dispositions all four W1 rows of round 7; investigation items without a disposition after this write: 0 (S40 is adjudicated by C-S8 in the same commit)."
  }
]
```

## C-S10 -- E1-AC3 and E2-AC3 graded PASS: the fix shape chosen against a measured-blocking alternative, the stronger attribute justified on a hazard the row never named, the sibling's protection shown INCIDENTAL by a byte-level cause, and a worker's own edit now verifiable by the name it types -- verified at this seat on the mechanism

```json
[
  {
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T05:58Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "NFRA_COMPEFFICACY-C-S10",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record; it dispositions no investigation item.",
    "one_line": "L9 on the round-8 FINAL packet @6b0e8258c9 (2 of 2 orders terminal; sha256 f2b152b9eaf4f9e6314ab65dad19687f6657f927a20e6a331a0fa0461bf26f5c over 10,414 bytes, re-hashed at this seat and equal to the issuer's): BOTH judgment criteria graded PASS. THIS ROUND EXISTS BECAUSE OF THIS SEAT'S S40 AND ITS FINDINGS ANSWER THAT ROW BETTER THAN THE ROW ASKED. E1-AC3, THE CRLF-RENDERED MODEL ASSET -- PASS. (1) THE FIX SHAPE IS CHOSEN AGAINST A MEASURED ALTERNATIVE RATHER THAN A PREFERRED ONE: shape (i), one .gitattributes line, makes the FRESH WORKTREE'S BYTES EQUAL THE MANIFEST; shape (ii), an LF-normalised manifest, would have made the ALARM stop while the bytes still differed, and the reading shows it is not merely dearer but BLOCKING inside this grant -- potion_embed.py hashes RAW bytes, so an LF-normalised digest mismatches AT THE MAIN TREE and merely MOVES the false alarm from the worker slots to the main tree, and making it work needs the verifier, which the order forbids touching. It also cites .gitattributes' own audit block already refusing that shape in this repo: normalising inside the comparator blinds a tamper detector to a real whole-file rewrite in order to silence a checkout artifact. AND `binary` RATHER THAN `-text` IS DISTINGUISHED ON A SECOND HAZARD THE ROW NEVER NAMED: -text stops the conversion, which is the whole measured defect, but leaves the default TEXT MERGE armed on a hash-pinned file, and a clean auto-merge of a pinned asset yields bytes matching neither parent and breaks the pin WITH NO CONFLICT. That is a second, quieter instance of the same disease, found while fixing the first. (2) THE OTHER MEMBER, AND THIS IS THE ANSWER TO THE QUESTION MY OWN ROW ASKED: model.safetensors was NOT converted, and NOT by any rule -- git's own binary heuristic classified it, on a NUL at byte offset 1 (the safetensors header opens with an 8-byte little-endian length, so bytes 1..7 are zero) against NO NUL in tokenizer.json's first 8,000 bytes, which is git's own detection window. TWO MEMBERS OF ONE DIRECTORY, ONE CONVERTED AND ONE NOT, WITH ZERO DECLARED DIFFERENCE BETWEEN THEM: the second member's protection is INCIDENTAL to its file format. A check scoped to the member a row named would have certified the directory on a property one member holds by accident. THIS SEAT'S OWN VERIFICATION at HEAD, on the mechanism rather than the report: `git check-attr -a` on tokenizer.json now reads binary set, text unset, diff unset, merge unset; `git ls-files --eol` reads attr/-text for BOTH members where tokenizer.json previously read an empty attr; and the worktree copy is 683,666 bytes with 0 CRLF pairs, hashing e67e803f624fb4d6 -- the manifest's own value. The pin holds at the main tree and will now hold at a fresh worktree by construction rather than by luck. E2-AC3, THE FORWARDERS -- PASS. (a) A worker can now verify its own comp-tool edit, MEASURED not asserted: a marker planted in a fresh worktree's tool was executed by the BARE NAME from that worktree and NOT from the main tree, with the file restored byte-identically on both sides. FWD-9's sentence now holds for the invocation a worker actually types, where before it returned rc 0 with a byte-identical answer FROM THE WRONG FILE. (b) THE FALLBACK'S LOUDNESS IS GRADED HONESTLY AND IN BOTH DIRECTIONS: one WARN line naming git's rc, git's message and the ABSOLUTE PATH chosen -- 'enough to tell a READER and not enough to tell a PROGRAM', because it is on stderr with no machine-readable field and a caller capturing only stdout sees nothing. The sufficient instrument is named and its cost stated: one rev-parse per invocation on every comp-tool call. A reading that says where its own remedy stops is worth more than one that claims the remedy is complete. (c) The bound is stated FROM a measurement with its denominator: four rc-0 completions spanning 651.6 to 826 seconds, a 27 percent spread, with the bound set ABOVE the maximum observed rather than at it, and the reason given -- setting it at the max fails on the next slow run. (d) Four things a worker still cannot see are enumerated rather than implied. VERDICT PASS on both.",
    "grades": [
      {
        "criterion": "E1-AC3",
        "instance": "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/NFRA_COMPEFFICACY.TO-CE-E-1.the-crlf-rendered-model-asset.proof_of_spec.json@bf236f4fa7",
        "verdict": "PASS",
        "reason": "The shape is chosen against an alternative measured to be blocking rather than merely costlier, with the repo's own prior refusal of that alternative cited; the stronger attribute is justified on a second hazard the originating row never named; the directory's other member is shown protected only INCIDENTALLY, by a byte-level cause, which answers the scoping question with a measurement instead of a principle; and the cost and non-application are stated. This seat verified the mechanism at HEAD independently: the attribute is set on both members and the worktree bytes now equal the manifest."
      },
      {
        "criterion": "E2-AC3",
        "instance": "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/NFRA_COMPEFFICACY.TO-CE-E-2.the-forwarders-resolve-to-the-callers-toplevel.proof_of_spec.json@247ad27d00",
        "verdict": "PASS",
        "reason": "The central claim is proven by a planted marker executed from one tree and not the other with a byte-identical restore, not by reading the generator; the fallback's disclosure is graded as sufficient for a reader and insufficient for a program, with the sufficient instrument named; the new bound is stated from four measured completions with the spread printed and set above the maximum with its reason; and what a worker still cannot see is enumerated. NO verdict was recorded by the assignee on either criterion."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L8_PACKET.round8.md @6b0e8258c9 re-hashed at this seat to f2b152b9eaf4f9e6314ab65dad19687f6657f927a20e6a331a0fa0461bf26f5c over 10,414 bytes; both instances read whole, each carrying its AC3 with the reading in output_evidence and no assignee verdict; both re-validated VALID rc 0 at the issuer's seat with criterion ids taken from the ORDER at HEAD.",
        "This seat, 2026-09-10 ~05:5xZ: `git check-attr -a -- org/modules/graph/potion/model/tokenizer.json` -> binary: set, diff: unset, merge: unset, text: unset; `git ls-files --eol -- org/modules/graph/potion/model/` -> attr/-text on both members; the worktree copy 683,666 bytes, 0 CRLF pairs, sha256 e67e803f624fb4d6...; `.gitattributes:99` carries `org/modules/graph/potion/model/** binary` under a comment block at :75-98 naming the pin, the verifier line numbers and the non-application.",
        "This seat's own NFRA_CLDGRPH-adjacent row NFRA_COMPEFFICACY-S40 (the finding this round exists to fix) and C-S8, which graduated it with W1-S2, W1-S3 and W1-S4 to 0.8.0_AE_CloudComp."
      ]
    },
    "spec_asserts": "E1-AC3 and E2-AC3 as cut (judgment, NO verdict): which fix shape and why with the alternative's cost; whether the directory's other member was affected and what that says about scoping to the named member; whether a worker can now verify its own edit; the fallback's loudness; whether the bound is stated from a measurement; and what is still not true of a worker seat.",
    "world_is": "The pinned asset is protected by a declared attribute on both members rather than by one member's file format; a worker's bare-name invocation now runs its own tree's tool; and the remaining blind spots are enumerated rather than implied.",
    "notes": "Round-8 judgment criteria graded: 2 of 2. This round closes the finding this seat opened at S40 and answers the question that row asked -- whether the sibling was safe for a reason or by accident -- with a byte-level cause rather than an inference."
  }
]
```

## C-S11 -- adjudicates all nine: GRADUATED -- two blocking items that were properties of the estate's own gates, an accept that could not have passed on a correct world, a bound smaller than what its arm measures (disclosed), and an adversary tool declaring a clean run over a source that died mid-read

```json
[
  {
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T05:58Z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "id": "NFRA_COMPEFFICACY-C-S11",
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_COMPEFFICACY-W2-S1",
      "NFRA_COMPEFFICACY-W2-S2",
      "NFRA_COMPEFFICACY-W2-S3",
      "NFRA_COMPEFFICACY-W2-S4",
      "NFRA_COMPEFFICACY-W2-S5",
      "NFRA_COMPEFFICACY-W2-S6",
      "NFRA_COMPEFFICACY-W2-S7",
      "NFRA_COMPEFFICACY-W2-S8",
      "NFRA_COMPEFFICACY-W2-S9"
    ],
    "disarm_owner": "2.0.0_SA_COO for the criterion-side items (W2-S2's unsatisfiable arm, W2-S8's bound, and W2-S3's one re-render per already-cut worktree); 0.8.0_AE_CloudComp for W2-S4 (comp-adversary declaring a clean run over a source that died mid-read); the rest are closed or placed",
    "one_line": "L9: ADJUDICATES all nine of the round's items -- GRADUATED, and SEVEN OF THE NINE ARE DEFECTS IN THE CUT OR IN THE ESTATE'S OWN CONTROLS, every one surfaced by the assignee. THE TWO BLOCKING ONES ARE RESOLVED AND THE PAIR IS THE ROUND'S BEST RECORD: W2-S6 (a granted path was uncommittable by the lane it was granted to, because safe-commit refuses any commit touching .tools/comp-* while a generated state file is stale, and the staleness PRE-DATES the order -- proven at the source rather than asserted, on the glob in comp_system.py's own _SOURCES and on round 7's drain having touched the file) and W2-S9 (the clearing act could NEVER have cleared it: the fingerprint reads the WORKTREE, so a regeneration on any tree the pending edit is not in re-drifts the instant the edit exists, and staging does not help because the dirty-source check slices git status at a fixed offset). The issuer regenerated on the shared branch first and the worker proved that could not converge -- and PROVED the regeneration had LANDED rather than assuming it failed, by watching the refusal fingerprints move. THE OVERRIDE WAS NEVER SPENT ACROSS ALL THREE REFUSALS, on the assignee's own reasoning that it exists for a case where regeneration is IMPOSSIBLE and here it was impossible only FROM OUTSIDE THE TREE. That is the distinction between a blocked act and a blocked LOCATION, and it is why the escape stayed unused. CARRIED with its wording, as the packet asks: the staleness predicate means to stop a seat laundering a PEER'S unlanded work, and it cannot tell a peer's unlanded work from the file THIS VERY COMMIT IS LANDING -- a gate gap, not a misuse, and the third gate this night has found blind to its own question. THE DISCLOSED WEAKENING, W2-S8, WHICH THE PACKET ASKS ME TO GRADE AS SUCH AND I DO: E2-AC1's own 900 s bound sits against an arm subject measured at 651.6 to 826 s across four rc-0 completions, a 27 percent spread, so an INLINE arm would pass on the fast half and return the battery's own rc 124 on the slow half -- the exact defect this cell exists to fix, one level up, INSIDE THE ACCEPT THAT GRADES THE FIX. The battery reads a recorded run under a grain control instead. IT IS A REAL WEAKENING AND IT IS DISCLOSED, and the disclosure is what makes it gradeable at all: a substitution printed beside the verdict can be weighed, a substitution made silently cannot. What it costs is that the arm no longer exercises the bound it names, and the remedy is a bound stated from the measurement the round already took. W2-S2 is the same family and is the sharper one: E1-AC1's arm (e) is UNSATISFIABLE BY ANY FIX THAT SATISFIES ARMS (b) AND (c) OF THE SAME CRITERION, because the baseline it compares against was itself captured under the lexical fallback -- the criterion-side half of my own S40, and it means the accept could not have passed on a correct world. W2-S3 is the fix's own live hazard, named rather than left: the conversion stopping turns a silent rewrite into a visible modification in every ALREADY-CUT worktree, so a broad `git add` there would commit the CRLF bytes into the index and break the pin FOR THE WHOLE ESTATE -- one re-render per live worktree is the act, and it is the kind of hazard a fix creates by succeeding. W2-S4 is the estate's own adversary tool exiting rc 0 and declaring five sources run and zero deferred while one of them died mid-read on an encoding error, with the declaration silent about it -- a control that reports clean about a question it failed to ask, which is the night's own sentence arriving from a fourth direction. W2-S1, W2-S5 and W2-S7 are records: the accept's fresh tree could not be cut from the literal branch name while the fix was still on the worker branch, so both scripts cut the invoking worktree's own branch and PRINTED the ref they resolved rather than silently substituting; the provisioner's comment named the wrong plane about which files need the permission restore, caught by dry-running the GENERATOR'S OUTPUT into a scratch home rather than reading the generator, and the live run now reports the pre-state exactly; and the face commanded a ledger act its own paths block did not grant, which is now placed as an estate row beside the tagless-face gap.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The nine rows read whole at HEAD (51 investigation items, 12 adjudication rows before this write; comp-surprise open 9, all dispositioned here, 0 malformed).",
        "L8_PACKET.round8.md ss.3-6; 2.0.0_SA_COO 95021 and 95027; 1.0.0_SA_CTO 95024 (the R-EG-5 amendment and the S13 scope confirmation).",
        "This seat's verification of the E1 fix's mechanism at HEAD (check-attr, ls-files --eol, the worktree hash) and of the gate's own self-test reading 0 of 30 at HEAD."
      ]
    },
    "spec_asserts": "TO-CE-E-1's E1-AC1 arms (b), (c) and (e) and its BOUNDS; TO-CE-E-2's <paths> grant, its spine-v3.9 ordering clause and E2-AC1's 900 s bound.",
    "world_is": "Two of the round's blocking items were structural properties of the estate's own gates rather than of the work; one accept could not have passed on a correct world; one bound is smaller than the thing its arm measures; and a shared adversary tool reports a clean run over a source that died.",
    "notes": "ARMED because four remedies remain live at two owners. Investigation items without a disposition after this write: 0 of 51. The duplicate id the census reports for S34 is the pre-existing collision recorded at C-S2 and is not this round's."
  }
]
```
