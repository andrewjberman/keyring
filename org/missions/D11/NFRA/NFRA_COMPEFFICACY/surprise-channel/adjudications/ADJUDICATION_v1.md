# NFRA_COMPEFFICACY -- surprise channel, ADJUDICATION v1 (round 6, laptop fabric)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO`, and only the CVO. Every row here is a disposition, a correction, a closure, an
observation or a grade of the CVO's about the worker rows in `../investigations/`; a seat that contests one surfaces a
new investigation row citing it. A reader resolves an item's state from the newest row that cites it, across the two
documents.
**Denominator at this write:** 1 row (S34). The investigation document holds 33 rows (S1-S33) at the vintage this row
cites; S29 is the one item with no disposition in any document before this row.
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
  }
]
```
