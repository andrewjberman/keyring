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
    "id": "LGIC_CANON-W3-S1",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~3",
    "surfaced_at": "2026-09-15T18:45Z",
    "one_line": "check_canon_r1.py decodes git show output in the locale codepage (cp1252 here), so a cited commit whose file carries a byte cp1252 leaves undefined raises in the subprocess reader thread, prints a traceback, and reads as a citation that does not resolve; R1-AC2's run printed three such tracebacks before its PASS verdict.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py@4058a56606 :72-73 git() runs subprocess with capture_output=True, text=True and no encoding; :80-85 at_commit() returns r.stdout, None when the reader thread failed; :487 r1_ticked() reads every cited ticklist commit through at_commit(); docstring :6 'A missing input is a FAIL verdict, never a traceback'.",
        "RUN: cd <WS> && timeout 120 python .../check_canon_r1.py r1-ticked (worktree wk-lgic-canon-1-3 @f95470f384) printed 3 x \"UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 2743\" from Thread-11/-23/-35 (_readerthread), then 'CITES infra/logic/04_SCOPE_TICKLIST.md@<commit> WHERE THAT TEXT AND v0.2 STAND: 4' and 'VERDICT: PASS-R1-TICKED-QUOTED', rc 0.",
        "DISCRIMINATOR: bytes of infra/logic/04_SCOPE_TICKLIST.md@54a764cb28 (7852) fail a strict cp1252 decode at byte 2743 (0x90, inside a UTF-8 ballot-box character); @6dab0d76a7 (8627 bytes) decodes; locale.getpreferredencoding(False) = cp1252."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The checker's docstring (check_canon_r1.py@4058a56606:6): every subcommand prints its evidence and one VERDICT line, and 'A missing input is a FAIL verdict, never a traceback'.",
    "world_is": "r1-ticked prints UnicodeDecodeError tracebacks on stderr for every cited ticklist commit whose bytes cp1252 cannot decode, and counts that citation as not standing. INERT for this order: the four v0.2 (@6dab0d76a7) citations decode, and v0.1 (@54a764cb28), which does not decode, does not carry the TICKED line anyway, so the verdict is unchanged. The failure direction is a false FAIL (a true citation read as absent), never a false PASS. A round's fixed inputs are read-only to workers; the remedy (encoding='utf-8' on git()) belongs to the checker's issuer, 2.0.0_SA_COO~G.",
    "notes": "Filed by 0.9.0_WK_LGIC_CANON~3 on LGIC_CANON.TO-CN-r-1; kept working. r1-clauses is not exposed: it resolves citations with git cat-file -e, which reads no text."
  }
]
```
