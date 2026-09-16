# LGIC_LGCTFM -- surprise channel, INVESTIGATION v1

**Opened by:** `2.0.0_SA_COO~G`, 2026-09-16, at the project's L5. **Home:** the project tree's channel. Lane `ANY`;
the gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project).
**Append-only.**

**Why it is opened at L5.** The first row is a count disagreement between three carriers of ONE fixture's
denominator, found while building the decomposition's fixed inputs. It is a surprise against this project's own
PRD, so it is a row here, not a message.

**Denominator at this write: 1 row** -- `LGIC_LGCTFM-S1`, 2.0.0_SA_COO~G.

```json
[
  {
    "id": "LGIC_LGCTFM-S1",
    "project": "LGIC_LGCTFM",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-16T17:20Z",
    "one_line": "THE FORK FIXTURE'S DENOMINATOR DISAGREES ACROSS THREE CARRIERS. PRD v1.1's cell candidate T4 says 'IV.5's FOUR positive forks'; the brief's IV.5, which is the carrier that ENUMERATES them, lists FIVE, each stated to be a positive control for O2; the brief's Part III O2 bar names THREE by way of example. A fixed input built on the PRD's four would under-cover the control set by one member and the fork cell's coverage claim would read clean while missing it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ENUMERATED BY SUBTRACTION FROM THE CARRIER THAT LISTS THEM, not by recall. Brief docs/briefs/d14-legacy-transform-brief-20260916.md section IV.5 states the rule ('A fork is two current resources whose DESIRED canonical form is ONE string') and then lists its measured members as SEMICOLON-SEPARATED clauses, closing with 'Each is a positive control for O2: a run over its subject that does not return it as a FORK row has a defect.' Splitting that sentence on its semicolons gives FIVE members.",
        "THE FIVE: (1) schwab/08335338/gold/ -- 2,108 json / 2,108 parquet, R18, the dual-write twin; (2) blackdiamond/49financial/{bronze,silver}_legacy/ beside {bronze,silver}/ -- 8,852 objects, dead 17d at census; (3) opal-data-assets/gold/mdpf_revamp/ (492) and portal/gold/ (415) -- both live, both JSON, one product; (4) opal-data-bd/canonical/schwab/{silver,gold} beside the monolith's schwab/08242234/silver/; (5) the naming census's bd / 49f / 49financial spellings of one firm across every resource type -- Lambda 20/9/1, role 20/12/1.",
        "THE NEGATIVE CONTROL IS UNAMBIGUOUS AND ALL THREE CARRIERS AGREE ON IT: smartx/platform/ beside smartx/account/{uuid}/ is NOT a fork (different jobs, one conformant, one R2-violating) and must grade as a TENSION. It is the whole discriminator -- a fork detector that fires on everything that looks alike passes every positive arm and is worthless.",
        "THE THREE CARRIERS, read at HEAD: PRD v1.1 @92154e0b63 cell-candidate row T4 fixtures column reads 'IV.5's four positive forks and the SmartX negative'. Brief IV.5 enumerates five. Brief Part III O2 names three inside em-dashes -- 'the Schwab gold twin, the two MDPF gold trees, the _legacy pairs' -- which reads as ILLUSTRATIVE rather than as a count, so O2 is not in conflict; the conflict is PRD four against IV.5 five.",
        "THIS SEAT PROPAGATED THE FOUR BEFORE MEASURING IT. The decomposition committed at 686d196fa1 says in section 3a 'IV.5's four POSITIVE forks (the Schwab twin, the two MDPF gold trees, the _legacy pairs)' -- which is the PRD's count welded to O2's three examples, a forward list assembled from two carriers and checked against neither. Rule 24(i) names exactly this shape: a forward list covers what its author had in mind and omits silently."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v1.1 T4: the fork fixture is IV.5's FOUR positive forks plus the SmartX negative.",
    "world_is": "The brief's IV.5 enumerates FIVE positive members and states that each is a positive control. Four would omit one.",
    "notes": "ARMED, disarm_owner 2.0.0_SA_COO~G -- this seat's, because the artifact that carries the defect is this seat's own decomposition and the fixed input that has not been written yet. NOT ADJUDICABLE and not routed: nothing in the PRD's RATIFIED text is touched, the cell-candidate table is explicitly the COO lane's to split, merge and re-sequence, and no other seat is blocked. THE ACT: FORK_CONTROLS.json is built with FIVE positives and the one negative, its denominator printed and this row cited, and the decomposition's section 3a is amended to five in the same commit. DISARM WHEN both land. * If 1.0.0_SA_CTO reads IV.5's fifth member -- the bd/49f/49financial spelling set -- as a NAMING tension rather than a fork, the count returns to four and this row disarms the other way; on the bytes it satisfies IV.5's own rule (several current spellings whose desired canonical form is one string) and IV.5 makes no exception for it, so five is what the carrier says. I am recording that reading rather than resolving it silently, because the fifth member is the only one of the five that is not a pair of PATHS."
  }
]
```
