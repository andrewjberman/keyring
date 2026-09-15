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
  },
  {
    "id": "LGIC_CANON-W2-S1",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~2",
    "surfaced_at": "2026-09-15T18:51Z",
    "one_line": "The fixed checker's l1-column grades every ledger table whose header has a cell exactly 'disposition', and section 7's count table has one, so the count table would be graded as a sixth plane table although TO-CN-l-1 2d scopes plane tables to sections 1 to 5; v1.0 renames that one header cell 'disposition class'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CHECKER: org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py@f95470f384 :849-851 -- l1_column iterates table_rows() over the WHOLE ledger and skips a table only when 'disposition' is not one of its header cells; the section is never read.",
        "LEDGER: infra/logic/06_CONFORMANCE_LEDGER.md@c9048873d1 :145 -- section 7's header '| disposition | rows | note |'.",
        "RUN on the unedited ledger at f95470f384: check_canon_r1.py l1-column printed 'PLANE TABLES: 6  WITHOUT A 'decided' COLUMN: 6'; the recount script, with the same header predicate, read 76 plane rows = 68 in sections 1-5 + 8 count rows of section 7.",
        "ORDER: org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-l-1.ledger.md@f95470f384 :28 -- 'Every plane table (each table with a `disposition` column, sections 1 to 5) gains a column headed `decided`'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-l-1 2d: every plane table -- each table with a disposition column, sections 1 to 5 -- gains a 'decided' column whose counts the script re-derives over every plane row.",
    "world_is": "Section 7's count table also has a column headed exactly 'disposition', and the checker selects plane tables by that header alone, not by section. Left as it was, the count table would need a 'decided' cell on each of its rows, and those non-plane rows would enter the DECIDED/WAITING count. v1.0 renames that one header cell to 'disposition class'; no count, label or disposition moves. INERT: the rename leaves the checker reading exactly the five tables the order names.",
    "notes": "Filed by 0.9.0_WK_LGIC_CANON~2 from worktree wk-lgic-canon-1-2 while serving TO-CN-l-1. The fixed input was not edited (read-only by the order)."
  },
  {
    "id": "LGIC_CANON-W2-S2",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~2",
    "surfaced_at": "2026-09-15T18:51Z",
    "one_line": "TO-CN-l-1 2e asks that 'the header and the change log read v1.0', but the conformance ledger at @c9048873d1 has no change log (level-2 sections 0 to 8, none a log); v1.0 adds section 9 CHANGE LOG, its earlier entries read from the file's git history.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LEDGER: infra/logic/06_CONFORMANCE_LEDGER.md@c9048873d1 -- the recount script printed 9 SECTION lines (sections 0-8) on it, none a change log; its version appears only in the title line ('v0.3') and in section 7's notes.",
        "GIT: git log -- infra/logic/06_CONFORMANCE_LEDGER.md at f95470f384 lists 5 commits: 4faf061126, a4cc0cb681, 6dab0d76a7, 9cf4a274db, c9048873d1.",
        "ORDER: org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-l-1.ledger.md@f95470f384 :29 -- 'e. The header and the change log read v1.0.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-l-1 2e: the header and the change log read v1.0.",
    "world_is": "The ledger had no change log to update. v1.0 adds one as section 9. Its entries before v1.0 are read from git log of the file (hash, author, subject), not from the document. INERT: the new section moves no row, and the checker's section reads ('THE COUNTS', 'EXCEPTION REGISTER') do not match its heading.",
    "notes": "Filed by 0.9.0_WK_LGIC_CANON~2 from worktree wk-lgic-canon-1-2 while serving TO-CN-l-1. The sibling canon 02_DOCTRINE.md carries its change log as its own last section, which v1.0 follows."
  },
  {
    "id": "LGIC_CANON-W1-S1",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~1",
    "surfaced_at": "2026-09-15T18:58Z",
    "one_line": "Rendering the schema's key.tier list into the canon made the canon contradict itself: its section 1 vocabulary said a tier is one of four medallion values and that state is NOT a tier, and it gave the root code/gold/ prefix as the code home, while the generated section lists state and code in the {tier} segment and the schema grades a new root code/ home OUT-OF-PATTERN. The worker aligned three section 1 rows, which the order's items do not name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CANON v0.3: infra/logic/02_DOCTRINE.md@f95470f384:46 'tier ... one of `bronze` `silver` `gold` `platinum`'; :61 state row, NOT-this column 'a tier'; :54 code home row '(`code/gold/` ...)'.",
        "SCHEMA: org/standards/NAMING_SCHEMA.json@f95470f384:41 key.tier [bronze, silver, gold, platinum, state, code]; :45 key.code 'a legacy root code/ key grades OUT-OF-PATTERN, its canonical_form the code-tier key'.",
        "ORDER: org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-k-1.canon.md@f95470f384:34 'No rule's substance changes except where items 3, 5 and 6 say so'; items 3 and 6 (:27, :30) name R1's text and R1's non-application only."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-k-1 items 3 and 6 name R1's grammar strings, its firm-form lists and its non-application; nothing else in the canon changes in substance.",
    "world_is": "With the section in place, the one document held two readings of 'tier' and of 'code home'. The worker changed words only, and no rule's text. Section 1's tier row now reads 'a MEDALLION tier', with the {tier} segment's full list in the generated section. The state row says state occupies the {tier} segment and is not a MEDALLION tier. The code home row says a new home is the code tier and the root homes are LEGACY (row S1). INERT: vocabulary only, no rule, key or name moves. The edit is judged at L9 under K1-J1 (3.0.0_SA_CVO).",
    "notes": "Filed by the CN-k-1 worker during its v1.0 edit. The firm row's back-ticked spelling list was removed under item 3's census, and is not this row."
  },
  {
    "id": "LGIC_CANON-W1-S2",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~1",
    "surfaced_at": "2026-09-15T18:58Z",
    "one_line": "The exception register's two carriers were already two different lists: the ledger's section 6 carries X6 (opal-data-demo, GRANTED), which the canon's section 4 never carried, and X6's axis value 'tenancy' is outside the A1-A5 domain of the schema line the canon keeps. Now that item 7 makes the ledger the entries' one home, X6 is the one entry that does not fit the register schema.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LEDGER: infra/logic/06_CONFORMANCE_LEDGER.md@f95470f384:135 'X6 | `opal-data-demo` | tenancy | a demo tenant, neither firm nor general | ... | PERMANENT | **GRANTED**'.",
        "CANON v0.3: infra/logic/02_DOCTRINE.md@f95470f384:337-338 schema 'pipeline · axis (A1–A5) · ...'; :340-347 entries X1, X2, X3, X4, X5, X7 and no X6.",
        "DECOMP: org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md@f95470f384:449-450 section 8 choice 2 describes the ledger as carrying the canon's entries 'again: two carriers of one list'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomposition section 8 choice 2: the canon's section 4 and the ledger's section 6 carry the same entries, and the schema's axis column takes A1-A5.",
    "world_is": "The carriers had diverged by one entry (X6, ledger only), and that entry's axis is 'tenancy', a value the kept schema does not admit. The canon v1.0 keeps the schema and points at the ledger for entries, so X6 now sits in the one carrier against a schema it does not fit. The worker did not edit the ledger, which is outside this order's paths. INERT: a register entry classifies and moves nothing (DEC-9). The fix belongs to the ledger's owner this round (cell CN-l-1), or to 1.0.0_SA_CTO or 4.0.0_SA_CRO, who write register entries: give X6 an axis in A1-A5, or widen the schema's axis domain by a Rule-24 act.",
    "notes": "Filed by the CN-k-1 worker while carrying out item 7 (section 4 points at the ledger for its entries)."
  },
  {
    "id": "LGIC_CANON-W5-S1",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~5",
    "surfaced_at": "2026-09-15T20:31Z",
    "one_line": "Judging the MDPF tree's A3 axis from the canon alone, the canon gives two answers for the monolith's tier-first planes: R1's census tag reads '53 of 53 non-SmartX monolith planes CONFORMANT', while R1's own text makes the key source-first in every bucket and R5's census names opal-data-assets gold/ (502) and portal/gold/ (415), which are tier-first or carry no scope segment. Judge B graded by the rule text (A3 VIOLATES, R1).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CANON R1 TEXT: infra/logic/02_DOCTRINE.md@671925aecc:112-120 'THE SAME STRING IN EVERY BUCKET, source first' and 'SUPERSEDED 2026-09-13 ~03:2xZ ... SOURCE-FIRST everywhere'; :167 N1 grammar {source}/{scope}/{tier}/{table}/{partition}; :175 'mdpf/global/..., never mdpf/mdpf/...'.",
        "CANON R1 CENSUS: infra/logic/02_DOCTRINE.md@671925aecc:130 'census: 53 of 53 non-SmartX monolith planes CONFORMANT; SmartX see R2'; :23-24 census tags are 'as of 01_CENSUS.md @d35653da5e'.",
        "CANON R5 CENSUS: infra/logic/02_DOCTRINE.md@671925aecc:314 'opal-data-assets/gold/ 502 (json), portal/gold/ 415'.",
        "TREE: org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/CN_TREE_MDPF.md@671925aecc:23-24 P4 opal-data-assets gold/mdpf/ and gold/mdpf_revamp/ under a root gold/ prefix (502 objects); P5 opal-data-assets portal/gold/ (415 objects).",
        "ANSWER: org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-b.tsv@98ed3177ff row A3 'VIOLATES R1', committed before this row was written."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-j-2 and canon section 0: a seat answers 'is this conformant, and against which rule' from the one document, without a second document.",
    "world_is": "On A3 the one document holds two readings of the same monolith planes: R1's census tag says they conform, and R1's text read against R5's census says they do not. A judge who takes the tag answers A3 differently from one who takes the text, which is the disagreement FWD-1 measures. Whether the tag predates the source-first ruling was not measured (01_CENSUS.md is outside this order's reads). INERT: a census tag classifies and moves nothing (DEC-9). The remedy is a recount of R1's tag, or a note of its vintage, at the canon's next edit.",
    "notes": "Filed by 0.9.0_WK_LGIC_CANON~5 (judge B) on LGIC_CANON.TO-CN-j-2; kept working. This worker judges the row's form, not its significance."
  }
]
```
