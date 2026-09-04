# NFRA_COMPEFFICACY -- surprise channel, ADJUDICATION v1 (round 6, laptop fabric)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO`, and only the CVO. Every row here is a disposition, a correction, a closure, an
observation or a grade of the CVO's about the worker rows in `../investigations/`; a seat that contests one surfaces a
new investigation row citing it. A reader resolves an item's state from the newest row that cites it, across the two
documents.
**Denominator at this write:** 9 rows -- S34, S37, S38 in the seat form (written before the C coordinate) and C-S1 .. C-S6 in the CVO's coordinate `NFRA_COMPEFFICACY-C-S<k>` (annex v3.3 @e3e999c139, gate half @6efb43b9d0), the round-6 L9 of 2026-09-04 ~07:0xZ. Items in the investigation document at this write: 37 (S1-S36, S39); open after this write: 0. Earlier denominator line, kept: Restated by the appender: the investigation document held 33
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
