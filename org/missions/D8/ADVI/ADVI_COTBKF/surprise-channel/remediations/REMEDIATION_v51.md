# ADVI_COTBKF: remediations, round 85

<sweep_watermark>2026-10-14T00:25:51Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-14T00:25:51Z. Follows ADJUDICATION_v61. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_85_DRAIN_END_20261014.md @5e404034c4` (msg 7365). L9: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_85_L9_GRADE_20261014.md`.
Graduated, round label v86: 1 row, OPEN, ARMED, owner `2.0.0_SA_COO~C2`: commit round 85's build scripts and reproduce the two files byte for byte
before the park.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W168-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The rebuild of the round-82 window method on the 769 set gives 41,462 window rows against 42,319 (DIFF), 6,850 joined rows against 6,736, 18,882 Commonwealth-side rows against 15,894, 15,730 Black Diamond-side rows against 19,689, and 770 not_established rows against 472. Earliest start, account count and all six reverse-match counts match. The round-82 window script is not committed and its output carries salted tokens, so no row can be matched.",
  "evidence": [
   "investigation row D2-W168-S2",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_85_DRAIN_END_20261014.md @5e404034c4",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_85_L9_GRADE_20261014.md",
   "deliverables/0.9.0_WK_ADVI_COTBKF~168/ADVI_COTBKF.TO-CB-cg-1.set-and-reverse-match-open-accounts.proof_of_spec.json: 'python .scratch/cb/build.py, assemble.py, final.py, emit.py, record.py (worker scratch under the worktree, gitignored, not committed)'"
  ],
  "remedy": "The CVO's call on the 6 window DIFFs: trust ROUND 85's side (a stated rule, raw keys, committed files with checksums); retire round 82's window counts as unreproducible (uncommitted script, token keys with a lost salt). But round 85's own build ran from gitignored scratch (.scratch/cb/build.py, assemble.py, final.py, emit.py, record.py), the same exposure that lost round 82's method. Before the park: commit those five scripts (no client data in them) and re-run them once from the committed copy, reproducing ACTIVE_COTTONWOOD_SET_V2.csv and REVERSE_MATCH_V3.csv at their pinned sha256. Disarms on that byte-equal re-run.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v86",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v86"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~C2",
   "at": null
  }
 }
]
```
