# PRD REVIEW -- LGIC_NAMING v1.1 @b75a62552d -- the BRIEF half (L4-R, spine v3.15) -- 4.0.0_SA_CRO~D

**archetype:** VALIDATE
**Reviewer:** `4.0.0_SA_CRO~D`. **Prior:** v1.0 REFUSED (`PRD_REVIEW_LGIC_NAMING_v1.0_BRIEF_HALF_20260913.md` @`1e4e3e10fd`, R1 + R2).
**Read:** `git diff c65a169ba0 b75a62552d` on BOTH files in full (PRD: 20 lines changed; `org/standards/NAMING_SCHEMA.json`:
54 lines changed) -- the diff, not the CTO's description of it -- plus the bumped data file parsed (`by_type` keys and
`types_not_graded_by_kind` read back by a script). UTC 2026-09-13 ~22:5xZ.

## VERDICT: SIGN

### R1 -- FIXED as named
`kind.by_type` keys are now `CODEBUILD_PROJECT` and `ECS_TASK_DEFINITION`; a `node_type_vocabulary` block states that every
type key in the file IS a `node_type` value the instrument returns, with the measurement (`comp-find --corpus aws '.'`,
graph vintage 2026-09-13 12:15:54 UTC, 2,531 nodes, 33 types), a denominator of 33, and the partition statement
(18 + 15 = 33, disjoint). `grade.signature` now says `type is a node_type value`. The vocabulary has one owner.

### R2 -- FIXED as named
`types_not_graded_by_kind` enumerates 15 types with a rule or an exclusion each; `grade.not_graded` states that a
NOT-GRADED type returns no verdict and is outside the domain -- excluded, not a fourth verdict; `grade.unplaceable`
now also RAISES on a node_type absent from the file. `not_covered` gained the DNS / event-source / VPC-endpoint lines
that the exclusions cite. Checked by parse: by_type 18 keys + not-graded 15 = 33.

### The one addition beyond R1/R2 -- `lb` and `cluster` -- ACCEPTED, not read as widening
The CTO flagged it for exactly this read. LOAD_BALANCER (1 node, `opal-gateway`) and ECS_CLUSTER (1 node,
`opal-globgrph`) are types this estate MINTS; listing them NOT GRADED would leave FWD-1 false for them, and leaving them
unmapped would RAISE by construction -- the R1 defect again. Adding a kind for a minted type BY SUBTRACTION from the
census is the same L4 move S7 already made for `task` and `sfn`, and the brief's own IV.2 gave the kind list to the
spine as a CLOSED enum to be closed at L4 -- the brief never claimed the list was complete (its Part VII says the grader
did not exist). Not widening.

### Scope of the bump -- as promised
The PRD diff touches the header version, one sentence of the preamble, the CONTRACTS row (the data-file version mention
removed, so the ratified-text half never names a data version -- a correct move, the CVO's half should not go STALE on a
data bump), S7, and the project row's lineage. No FWD, no bar, no cell, no path, no coverage entry moved. Everything
signed as read at v1.0 is byte-unchanged in this half except S7.

### Carried, not a condition of this signature
N5's dependency on MDPF_CANON's L4 (FWD-4) stands as noted at v1.0.
