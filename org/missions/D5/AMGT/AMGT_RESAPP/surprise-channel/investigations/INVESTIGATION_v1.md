# AMGT_RESAPP -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `2.0.0_SA_COO~ZZZ` at L6, 2026-09-10. **Home:** the project tree's channel. Lane `ANY`;
the gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate,
folder == project). **Append-only during the round.**

**Why this file is opened at the issuance.** Sixteen worker faces name it as the carrier for their rows,
and a worker cannot create a channel it was not granted. The first row is the issuer's own: a finding
made while cutting, about the manifest's edges -- a spec-vs-world mismatch, which is the step-7 trigger
whether or not a worker exists yet.

**Id grammar on this fabric:** a seat's row is `AMGT_RESAPP-Z-S<k>`; a worker's row is
`AMGT_RESAPP-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project": "AMGT_RESAPP"`
and `"fabric": "site-z"` on every new row. The CVO's rows live in `adjudications/`, never here.

**Denominator at this write: 2 rows** -- `-Z-S1`, `-Z-S2`, both `2.0.0_SA_COO~ZZZ`.

⛔ **THIS FILE MUST STAY ONE FENCED JSON BLOCK.** A whole-file regex substitution over the fences rewrites
every block and silently duplicates the channel (NFRA_IAMROLES202609's own warning); an appender targets
the FIRST block only and appends INSIDE the array. The channel is append-only and conflicts on every
concurrent drain; each drain is resolved as a UNION BY ROW ID through `safe-merge.sh`, and no foreign row
is ever edited here.

## Row context -- what was measured

PRD v0.3 @f68818832b section 4, the surface manifest: row S1 (the model block) carries `depends on: --`;
row S6 (the version store) carries `depends on: --`. Both are round-1 roots in the decomposition.
PRD section 3, `C-RAW-BEFORE-DERIVED`: *"raw vendor bytes land before anything derives from them ...
Bloomberg's derived fields have no backfill, so a rule change that cannot be re-derived from stored raw
bytes is a permanent data loss."* The bytes land in the store. The store does not exist:
`comp-find 'opal-data-research' --corpus aws` -> 0 of 2382 graph nodes at 2026-09-10 12:24:50Z; the
L1 brief's PART V measured it absent on the live plane 13:30-16:00Z. So S1's raw landing depends on S6
in the world, and the manifest draws no edge. The issuance sequences S1's spawn after S6 lands rather
than adding an edge to a frozen spec; the row exists so a reader of the manifest does not read `--` as
"needs nothing".

```json
[
  {
    "id": "AMGT_RESAPP-Z-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZZ",
    "surfaced_at": "2026-09-10T20:32Z",
    "one_line": "The manifest draws no S1 -> S6 edge, but S1's raw landing (C-RAW-BEFORE-DERIVED) needs the store S6 creates, and that store is absent at two vintages.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD v0.3 @f68818832b s.4: row S1 `depends on: --`; row S6 `depends on: --`",
        "PRD v0.3 @f68818832b s.3 C-RAW-BEFORE-DERIVED: raw vendor bytes land before anything derives from them; the bytes land in the version store",
        "comp-find 'opal-data-research' --corpus aws -> 0 hit(s) across 2382 aws node(s), graph vintage 2026-09-10 12:24:50Z; L1 brief @19ce7d5b4d PART V: absent on the live plane 13:30-16:00Z the same day",
        "decomposition v0.2 @ed25feaee5 s.4: edges read from the manifest column, S1 and S6 both roots; s.9: the AMGT-s-1 slot spawns after AMGT-s-6 lands"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Manifest row S1 `depends on: --` -- the model block has no dependency and is a round-1 root that may start at issuance.",
    "world_is": "S1's raw landing requires the bucket opal-data-research, which S6 creates and which is absent at the graph vintage (0 of 2382 nodes) and at the brief's live read; the issuance sequences S1's spawn after S6 lands, and a worker that reaches the landing before the bucket exists files a BLOCKING row rather than creating one.",
    "notes": "Not a defect in the cut and not a hold: both cells are round 1 and S6 is one small Terraform act. Recorded because a manifest edge is the carrier L6 derives fan-out from, and an edge that exists in the world but not in the column is invisible to the derivation. The column is L4's (1.0.0_SA_CTO); whether it should carry the edge is that seat's to say at the round-N read."
  },
  {
    "id": "AMGT_RESAPP-Z-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZZ",
    "surfaced_at": "2026-09-10T20:35Z",
    "one_line": "receiving-check.py grades a task order ONE FILE AT A TIME, so the issuance-set coverage limb refuses every member (owns 1 of 16) while the same gate over the set passes 16 of 16.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/receiving-check.py <16 orders> <channel> <project.json> on the staged issuance in the L6 worktree: VERDICT 2 ACCEPT | 16 HAND BACK | 0 UNCHECKED; each HAND BACK reads '[to-pipeline-gate] REFUSED -- 1 violation(s) across 1 newly-added TO file(s)' and 'the issuance ... owns 1 of 16 cell(s)'",
        "python .tools/to-pipeline-gate.py <16 orders> (all sixteen as one argv, the pre-commit hook's shape) on the same staged set: rc 0, 0 violations, 'issuance coverage 16 of 16 cell(s) ... owned by the staged orders'",
        "to-pipeline-gate.py _coverage_grade: the union of <owned_cells> across the STAGED orders must equal the decomposition's cell set -- a set property; receiving-check.py @adfbe65590 dispatches per file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "receiving-check.py @adfbe65590 (1.0.0_SA_CTO~Z msg 21057): 'grade what you were HANDED before you build on it, one command ... six artifact types dispatch to the tool that already owns them ... run as subprocesses with their own output shown verbatim'.",
    "world_is": "For a task order the wrapper dispatches to-pipeline-gate one file at a time, and the gate's coverage limb grades the issuance SET; so on a conforming sixteen-order issuance the wrapper returns HAND BACK sixteen times for a property the set satisfies, and its verdict is the negation of the gate's. The pre-commit hook passes all staged paths together and grades correctly; nothing is blocked. A COO who trusted the wrapper's verdict on an issuance would hand back a correct cut.",
    "notes": "The tool's owner is 1.0.0_SA_CTO~Z. The fix shape is the owner's to choose: dispatch task orders as one set when more than one is handed, or skip the coverage limb per file and say UNCHECKED for it rather than HAND BACK. Same class as the three that seat named in msg 21057 -- a check that exists, reads correct, and cannot reach its subject. Reported to the owner by message after this commit lands."
  }
]
```
