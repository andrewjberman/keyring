# LGIC_CANON -- surprise channel, INVESTIGATION v1

**Opened by:** `1.0.0_SA_CTO`, 2026-09-14, after LGIC_CANON's L4-R. **Home:** the project tree's channel. Lane `ANY`;
the gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project).
**Append-only.**

**Why it is opened before L5.** The first row comes from a ruling on a sibling project's schema (LGIC_NAMING-S7): the
canon's R1 text now lags the schema it governs. That is a surprise against this project's canon, so it is a row here,
not a message.

**Denominator at this write: 1 row** -- `LGIC_CANON-S1`, 1.0.0_SA_CTO.

```json
[
  {
    "id": "LGIC_CANON-S1",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-14T10:38Z",
    "one_line": "Doctrine R1's non-application list still exempts 'code/ prefixes (R16)' from the grammar, but LGIC_NAMING v1.3 (row LGIC_NAMING-S7, ruled) places every NEW code home in the grammar's code tier, {source}/{scope}/code/{built_tier}/{file}; the canon's words and the schema disagree until R1's code/ entry is narrowed to the LEGACY root homes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CANON: infra/logic/02_DOCTRINE.md:103 R1 non-application 'code/ prefixes (R16), _backup/ roots (R17), the shared serving bucket's non-tier prefixes'; :275-283 R16, with its Lambda-artifact non-application and 'Their KEY's grammar is still graded (R1)'.",
        "RULING: org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_LGIC_NAMING_20260914T103xZ_S6_S7_S8_ENTITY_PARTITION_CODE_TIER_LEGACY_SERVED_PATHS.md call 2, RULING (a): the ratified code tier stands; the carve-out narrows to legacy root homes.",
        "DATA: org/standards/NAMING_SCHEMA.json v1.3 key.code (this seat's same-hour revision)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Doctrine R1: code/ prefixes (R16) sit outside the tier-plane grammar.",
    "world_is": "The naming schema, as ruled at LGIC_NAMING v1.3, puts every new code home inside the grammar (the code tier) and keeps the root code/ homes only as legacy. INERT because every new key is produced by key(), which reads the schema, never the canon's prose; the remedy is one line of R1's non-application at LGIC_CANON's next canon edit.",
    "notes": "Opened by 1.0.0_SA_CTO. The first row of this channel: LGIC_CANON is ADMITTED at v1.1 (56608aadd4) with no COO lane seated, so the row waits for its L5/L6 or an L10 addendum, whichever edits the canon first."
  },
  {
    "id": "LGIC_CANON-S2",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "4.0.0_SA_CRO",
    "surfaced_at": "2026-09-14T18:38Z",
    "one_line": "The L5 decomposition's DEC-2 tree pairs a rule-breaking row in opal-data-etfs (ledger :102) with exception X4, which the ledger registers to Pathfinder/TrueShares in the monolith (:52-54, :133); the opal-data-etfs tree's own exceptions X3 and X5 are OWED, so the chosen pairing may cross pipelines while DEC-2 asks for one tree carrying both.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D14/LGIC/LGIC_CANON/prd/LGIC_CANON_PRD.md@d9977a0f40:168-174 DEC-2, 'the same real pipeline tree' chosen so that 'it carries at least one row where the tree breaks a canon rule ... and one DECLARED EXCEPTION'.",
        "DECOMP: org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md:59-65 and :333-334 choose the ETFs tree, citing ledger :102 and X4 at :133.",
        "LEDGER: infra/logic/06_CONFORMANCE_LEDGER.md@d9977a0f40 :52-54 pathfinder/ and trueshares/ planes under section 1 THE MONOLITH; :101-103 opal-data-etfs silver/gold/platinum; :132 X3 ETFs OWED; :133 X4 'Pathfinder, TrueShares' GRANTED; :134 X5 ETFs platinum OWED; :98 and :100 MDPF MIGRATE with :130 X1 MDPF GRANTED."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "DEC-2: one real pipeline tree carries at least one rule-breaking ledger row and one DECLARED EXCEPTION.",
    "world_is": "The chosen ETFs tree's granted exception X4 is registered to Pathfinder/TrueShares, not to opal-data-etfs, whose own exceptions X3 and X5 are OWED. MDPF meets the bar inside one pipeline (MIGRATE :98 and :100, X1 GRANTED :130). INERT because LGIC_CANON has no issuer seated, so no order has been cut on this choice; the owner is the decomposition's author at its next L5/L6 edit.",
    "notes": "Surfaced by 4.0.0_SA_CRO during the v1.2 L4-R brief review, which refused on a separate ground (R1, C2 at v1.2:272). Not a brief-half ground: choosing the tree is the decomposition's and grading it is L9's. Whether 'the ETFs pipeline' spans Pathfinder/TrueShares ingest was not measured; the ledger registers them as separate pipelines. Review: docs/briefs/sources/LGIC_CANON_L4_BRIEF_REVIEW_v1_2_20260914.md."
  },
  {
    "id": "LGIC_CANON-W8-S1",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~8",
    "surfaced_at": "2026-09-15T18:39Z",
    "one_line": "For naming item n3, lib/opal_naming.py address() writes the platinum key advi/49financial/platinum/advisors/advisor_id=A123, and grade() in the same library calls that exact key OUT-OF-PATTERN, giving advisor-id=a123 as canonical. The grader reads an entity partition that ends a key as the file leaf and rewrites it in kebab-case lowercase, contradicting both the builder and NAMING_SCHEMA key.partition's own example, advisor_id=A123.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BUILDER: lib/opal_naming.py:1287-1300 key() and :1303-1316 address() @f95470f384 write {source}/{scope}/{tier}/{table}/{partition} with the partition verbatim and no object; address('advi','49financial','platinum','advisors','advisor_id=A123') returned s3://opal-data-49financial/advi/49financial/platinum/advisors/advisor_id=A123.",
        "GRADER: lib/opal_naming.py:1102-1111 _new_served @f95470f384 sets leaf = len(rest) - 1 whenever the key is not a prefix, and rewrites a leaf that is not kebab .json as s.lower().replace('_', '-'). The platinum branch reaches it at :1215-1221 when the key is not on the legacy list.",
        "SCHEMA: org/standards/NAMING_SCHEMA.json:46 key.partition @f95470f384 says '{entity}={id} -- an entity partition; {entity} is the KEY COLUMN's name as the table carries it (advisor_id=A123) ... the file is the object under it (doctrine R2; P1, v1.5)'.",
        "MEASURED 2026-09-15T18:39Z in worktree wk-lgic-canon-1-8 @f95470f384, grade(k, 'S3Key'): 'advi/49financial/platinum/advisors/advisor_id=A123' gave OUT-OF-PATTERN, canonical 'advi/49financial/platinum/advisors/advisor-id=a123'. The same key with a trailing '/' gave CONFORMANT, and with '/profile.json' appended also CONFORMANT. The gold key 'mdpf/49financial/gold/category_views/date=2026-09-15' (n2) gave CONFORMANT, because gold never reaches _new_served."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-n-1: 'Look it up; do not decide it ... every S3 address is lib/opal_naming.py address() output ... The check is slot-aware: each spelling is sanctioned in its own slot, so write what the builders write.'",
    "world_is": "The builder and the grader in lib/opal_naming.py give different answers for n3. address() writes advisor_id=A123, and grade() calls that key OUT-OF-PATTERN with advisor-id=a123 as canonical. So a seat reading the grader's canonical form and a seat following the builder write different names for one item. This worker wrote the builder's output. ARMED because a pipeline built to Rule 30 gets every platinum key that ends in an entity partition graded OUT-OF-PATTERN by the naming grade, and the canonical form it prints rewrites the entity id's bytes (A123 to a123).",
    "notes": "Filed by 0.9.0_WK_LGIC_CANON~8 on LGIC_CANON.TO-CN-n-1 (naming worker A). The builder outputs for the other five items (n1, n2, n4, n5, n6) all grade CONFORMANT. Nothing was fixed: lib/opal_naming.py is LGIC_ENFORCE's builder and lies outside this order's <paths>. The disarm owner is named as the seat that rules the schema and LGIC_ENFORCE's round analysis. This worker judges the row's form, not its significance."
  }
]
```
