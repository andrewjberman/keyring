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
  },
  {
    "id": "LGIC_CANON-W6-S1",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~6",
    "surfaced_at": "2026-09-15T20:53Z",
    "one_line": "A new firm's identity row cannot be written without two values that no builder or rule produces: its LONG and SHORT forms. The schema's firm list is a closed list of four firms, ruled by Andrew, and the only onboarding runbook tells the operator to choose the slug. The checklist therefore takes both forms as inputs from Andrew and derives nothing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SCHEMA: org/standards/NAMING_SCHEMA.json@671925aecc:113 firm_forms lists exactly four firms (49financial/49f, inflection/inf, cottonwood/cot, demo/demo). Its rows_owner text reads 'This file fixes the SHAPE and the closed lists; it mints no row.'",
        "CANON: infra/logic/02_DOCTRINE.md@671925aecc:123-125 R1 'Each firm has ONE sanctioned LONG form and ONE sanctioned SHORT form ... Andrew ~03:5xZ'. No rule in the canon derives a new firm's two forms.",
        "RUNBOOK: infra/aws/users/ONBOARDING.md@671925aecc:164-168 'Step 1 -- Choose the firmId slug. Lowercase, alphanumeric, no spaces.' The one existing firm-onboarding runbook leaves the choice to the operator.",
        "PRACTICE RUN: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD7.md@671925aecc:6 took the fictitious forms quillwater/qwt as fixed by its order; :35 shows that a new FIRM row draws 'WARN ... is not in NAMING_SCHEMA.json firm_forms'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-o-1 THE CELL: the checklist takes a new firm from its identity row to its served dashboard 'with no step where somebody has to invent an answer' (FWD-5), and every name a step produces is the builders' output (CLAUDE.md Rule 30).",
    "world_is": "The identity row's first fields, the firm's LONG and SHORT forms, are what name(), lookup() and address() read, so the builders cannot supply them. The canon rules which form each slot takes, and the schema's closed list names four firms; both rest on Andrew's card-2 word. The only runbook (ONBOARDING.md section 5, step 1) has the operator pick a slug. The checklist does not invent a derivation: its INPUTS table and Step 1 take both forms from Andrew. Whether a rule should derive them (for example, SHORT from LONG) is for 1.0.0_SA_CTO and LGIC_NAMING's owner to carry to Andrew. INERT: the checklist's first real run (C6) is not cut this round.",
    "notes": "Filed by the CN-o-1 worker while writing Step 1 of infra/logic/10_ONBOARDING_CHECKLIST.md."
  },
  {
    "id": "LGIC_CANON-W6-S2",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~6",
    "surfaced_at": "2026-09-15T20:53Z",
    "one_line": "The acts that give a firm's people their sign-in have no LGIC_ENFORCE CONTRACTS builder and are not generated views. They are the opal-partner-<firm> table (one hand-written partner-firms/<firm>.tf per firm), the user rows written with CLI put-item, and the portal page-access map FIRM_ALLOWED_PATHS, which is edited by hand. So the checklist's sign-in step can name only the identity row as its input, and has to take the portal path list from Andrew.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUNBOOK: infra/aws/users/ONBOARDING.md@671925aecc:170-183 creates 'opal-partner-$FIRM' with aws dynamodb create-table 'until 0.7.0_AE_CloudOps ships the TF module'; :82-83 and :109-110 write users with aws dynamodb put-item; :201-213 has the page-access map portal/src/lib/firmAccess.ts FIRM_ALLOWED_PATHS edited by hand (portal/ is a gitlink and that file was not read).",
        "MODULE: infra/aws/terraform/partner-firms/demo.tf@671925aecc:32-35 'module \"firm_demo\" { source = \"../modules/partner-firm-table\" firm_id = \"demo\" }'. There is one hand-written file per firm in that directory (49financial.tf, cottonwood.tf, demo.tf, inflection.tf).",
        "CONTRACTS: org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md@671925aecc:161-171 has nine rows, and none produces the sign-in table, the user rows or the page-access map. lib/opal_naming.py@671925aecc:60-68 VIEWS lists seven generated carriers, and neither partner-firms/*.tf nor firmAccess.ts is among them."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-o-1 THE CELL: every step names its builder or gate by an LGIC_ENFORCE CONTRACTS name; every name a step produces is the builders' output (Rule 30); the last step is the served dashboard its people see.",
    "world_is": "No LGIC_ENFORCE contract builds the firm's sign-in, and no registry field carries the portal paths a firm may open. So Step 14 of the checklist names the identity registry's ROWS as the source of the firm id, email domain and surfaces, says plainly that the three acts sit outside every contract, and STOPs for the path list if Andrew has not given it. FIRM_ALLOWED_PATHS is a per-firm map kept by hand, of the kind DEC-5 turns into generated views, and it is not one of the seven. The canon rules only the storage plane, so no canon rule governs sign-in either; Step 14 cites R6's tenant separation. The owner of the gap is 1.0.0_SA_CTO: a CONTRACTS row, or a DEC-5 carrier. INERT: nothing runs until C6.",
    "notes": "Filed by the CN-o-1 worker while writing Step 14 of infra/logic/10_ONBOARDING_CHECKLIST.md."
  },
  {
    "id": "LGIC_CANON-W6-S3",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~6",
    "surfaced_at": "2026-09-15T20:53Z",
    "one_line": "A new firm's dashboard is served through routes that read tier-first keys: the edge auth validator reads platinum/{firmId}/ownership_map.json in FIRM_BUCKET_MAP[firmId] || `opal-data-${firmId}`, and the router asserts platinum/advi/{firm}/. key() and address() cannot produce those keys, and the list that would admit legacy served paths does not exist yet. So the checklist's platinum step STOPs there instead of having a hand-typed key written.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EDGE: infra/aws/lambda-edge/auth-validator-edge/index.mjs@671925aecc:153-154 'const bucket = FIRM_BUCKET_MAP[firmId] || `opal-data-${firmId}`;' and 'const key = `platinum/${firmId}/ownership_map.json`;'. The key is tier-first, and the fallback bucket is composed by hand.",
        "BUILDERS: lib/opal_naming.py@671925aecc:1287-1300 key() returns only {source}/{scope}/{tier}/{table}/{partition}; :1303-1316 address() returns s3://{bucket}/ followed by that key. Neither can produce 'platinum/<firm>/ownership_map.json'.",
        "ROUTER: infra/aws/lambda-edge/_shared/firm-config.mjs@671925aecc:34, the hazard note above FIRM_CONFIG: 'shared-advisor-router asserts the {firm} segment of platinum/advi/{firm}/', which is also tier-first.",
        "SCHEMA: infra/logic/02_DOCTRINE.md@671925aecc:180-182, the generated N1 'legacy served path' clauses. A legacy served path keeps its bytes only if legacy_served_paths lists it, and that list is 'absent until LN-g-1 lands it'.",
        "REGISTRY: infra/logic/registry/scopes.json@671925aecc, row 49financial: its alias opal-data-bd has planes [bucket] and routed true. The router still serves 49 Financial from its legacy bucket, so no firm is yet served from a canonical firm bucket."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-o-1 THE CELL: every address a step produces is the builders' output (Rule 30), and the last step is the served dashboard the firm's people see.",
    "world_is": "The routes that serve a firm's dashboard read keys the builders refuse to produce, and the membership list for legacy served paths (LN-g-1) does not exist yet. A runner would face two options: type the legacy key by hand, which Rule 30 forbids, or publish at the builder address, which the route never reads. Step 10 of the checklist STOPs there and names this row, and Step 15 points back to it. The owners are the served-route side (ADVI_FIRMBKTS's router work, and LGIC_NAMING's LN-g-1 legacy list), with routing decided by 1.0.0_SA_CTO. INERT: no new firm is being onboarded this round.",
    "notes": "Filed by the CN-o-1 worker while writing Steps 10 and 15 of infra/logic/10_ONBOARDING_CHECKLIST.md."
  },
  {
    "id": "LGIC_CANON-W7-S1",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~7",
    "surfaced_at": "2026-09-15T21:18Z",
    "one_line": "The two blind judges give the MDPF tree's axis A1 the same verdict (UNDETERMINED) but different rule sets, judge A R9,R18 and judge B R9,R20, so J3-AC2 reads FAIL-J3-CITATIONS-DIFFER (4 of 5 axes). The split traces to the canon: section 2's A1 row names R9 and R18, no section 3 rule governs an ingestion mechanism, and the one measured A1 departure (register X1) is decided by R20, which section 2 lists on no axis.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CHECKER: cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py j3-citations, run at 91b11ff0c9, printed 'CITATIONS DIFFER: A1  A=['R18', 'R9']  B=['R20', 'R9']', 'AXES: 5  SAME RULE SET: 4', 'VERDICT: FAIL-J3-CITATIONS-DIFFER', rc=0.",
        "ANSWERS: org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-a.tsv@537f49b8fd:4 'A1 UNDETERMINED R9,R18' (its reason names X1 'DECLARED-EXCEPTION, R20' in prose only); judge-b.tsv@98ed3177ff:2 'A1 UNDETERMINED R9,R20'.",
        "CANON AXIS TABLE: infra/logic/02_DOCTRINE.md@671925aecc:88 'A1 INGESTION | how a source arrives, by what mechanism | R9, R18'; :94 'Process: R18, R19, R20.' (git diff --stat 671925aecc 91b11ff0c9 on the file is empty).",
        "CANON RULE HOMES: infra/logic/02_DOCTRINE.md@671925aecc:362 '### A5 FORMAT' then :364 R9 'BRONZE IS RAW AND UNTOUCHED'; :466 '### PROCESS' then :468 R18 'NO SHADOW PATH, NO DUAL-WRITE, NO STANDING COMPARATOR'; :484 R20 'AN UNDECLARED DEPARTURE IS A VIOLATION; A DECLARED ONE IS THE PATTERN WORKING'. Section 3's headings (:110, :154, :296, :362, :410, :421, :446, :466) carry no A1 heading.",
        "TREE: org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/CN_TREE_MDPF.md@91b11ff0c9:58 register X1, axis A1, PERMANENT, GRANTED; :48-49 the ingestion mechanism is not measured.",
        "TRACE: org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-compare.md section 4, D1 (this row's commit)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-j-3 criterion J3-AC2 expects 'VERDICT: PASS-J3-SAME-CITATIONS': the two judgings give the same rule citations per axis.",
    "world_is": "They give the same set on A2 to A5 and different sets on A1, so the criterion does not produce its named result and the order stays open on J3-AC2. On A2, A3 and A5 both judges cite the rules that decided the verdict, a subset of section 2's list. On A1 no rule decided the verdict (UNDETERMINED). The canon does not say whether a verdict then cites the axis's section 2 list (judge A) or the rules its reasoning used (judge B, who adds R20 for X1 and drops R18). PRD DEC-2 returns a disagreement to CN-k-1 as a canon defect. INERT: the canon classifies and moves nothing (DEC-9).",
    "notes": "Filed by 0.9.0_WK_LGIC_CANON~7 on LGIC_CANON.TO-CN-j-3; kept working. This worker judges the row's form, not its significance."
  },
  {
    "id": "LGIC_CANON-W7-S2",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~7",
    "surfaced_at": "2026-09-15T21:18Z",
    "one_line": "Both blind judges grade naming case J-N3, bd-49f-runner-role (IAM_ROLE), OUT-OF-PATTERN, while the key fixed at L6 reads ALIAS (canonical blackdiamond-49f-runner-role), so J3-AC3 reads FAIL-J3-CASES-OFF-KEY (2 of 3 cases). The key rests on GRADING_RULE.md R3's adjacency test (bd next to a firm token is the VENDOR blackdiamond). The canon's generated naming section does not carry that test, and from the canon alone bd resolves only to the firm, which in a system slot fails the grammar.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CHECKER: cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py j3-naming-key, run at 91b11ff0c9, printed 'CASE OFF THE KEY: J-N3  A=OUT-OF-PATTERN  B=OUT-OF-PATTERN  key=ALIAS', 'CASES: 3  BOTH JUDGES ON THE KEY: 2', 'VERDICT: FAIL-J3-CASES-OFF-KEY', rc=0.",
        "KEY: org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/CN_JUDGE_NAMING_KEY.json@91b11ff0c9:5 'J-N3': 'ALIAS'; :6 canonical_form 'blackdiamond-49f-runner-role'; :3 source 'GRADING_RULE.md @3cc090827f section 9'.",
        "KEY SOURCE: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@3cc090827f:168-173 R3 'bd ... is the VENDOR blackdiamond when a V4 firm token is next to it, before or after, and the FIRM 49financial otherwise ... The test is ADJACENCY to a V4 firm token, never position'; :368 worked case bd-49f-runner-role ALIAS 'R3 bd next to firm 49f reads as the VENDOR blackdiamond'.",
        "CANON: infra/logic/02_DOCTRINE.md@671925aecc:278 N4 'refused in EVERY slot ... The vendor is blackdiamond; the firm is 49financial.'; :285 N5 ALIAS 'for example inflection or bd in a resource name's scope slot'; :286 OUT-OF-PATTERN '... a firm in the system slot'; :222 'never a system: a firm'; :64 a firm's registry aliases are spellings of one key. A case-insensitive search of the file for 'adjacen' and 'next to' returns 0 lines.",
        "REGISTRY: infra/logic/registry/scopes.json@91b11ff0c9:47-53 the bd alias row sits on the firm 49financial, its refused text 'the vendor is blackdiamond, the firm is 49financial'.",
        "ANSWERS: org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-a.tsv@537f49b8fd:11 'J-N3 OUT-OF-PATTERN' ('the refused alias of the FIRM 49financial (N4, N5)'); judge-b.tsv@98ed3177ff:9 'J-N3 OUT-OF-PATTERN' ('the canon's only resolution of bd is as the firm's alias')."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-j-3 criterion J3-AC3 expects 'VERDICT: PASS-J3-CASES-MATCH-KEY': the naming cases match the verdicts fixed at L6, in both judgings.",
    "world_is": "The judges match the key on J-N1 and J-N2 and agree with each other on J-N3, but both are off the key on J-N3, so the criterion does not produce its named result and the order stays open on J3-AC3. The canon's N4 names both referents of bd with no rule for choosing, N5 places a bd alias only in a scope slot, and the registry row puts bd on the firm, so the judges' reading is the one the canon supports and the key's needs GRADING_RULE R3, which the canon does not carry. The generated section is rendered from org/standards/NAMING_SCHEMA.json v1.8 (stamp at 02_DOCTRINE.md:163). Whether the schema carries the test and the renderer drops it, or the schema lacks it, was not read (outside this order's reads). PRD DEC-2 returns the disagreement to CN-k-1. INERT: the canon grades and moves nothing (DEC-9).",
    "notes": "Filed by 0.9.0_WK_LGIC_CANON~7 on LGIC_CANON.TO-CN-j-3; kept working. The trace is in judge-compare.md section 4, D2. This worker judges the row's form, not its significance: whether the canon or the key changes is the L9 and CN-k-1 call."
  },
  {
    "id": "LGIC_CANON-W7-S3",
    "project": "LGIC_CANON",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_CANON~7",
    "surfaced_at": "2026-09-15T22:57Z",
    "one_line": "The review of the onboarding checklist marks 5 of its 16 steps JUDGEMENT (3, 7, 8, 9, 14), so O2-AC2 reads FAIL-O2-JUDGEMENT-STEP, not PASS-O2-NO-JUDGEMENT, and the order stays open. Four of the five trace to the pipeline build that onboarding bundles and that the canon fixes only in form: table names, partition forms, the resource set, function words and a pipeline directory. The fifth is Step 14's mandated opal-partner-<LONG> table, which grade() reads OUT-OF-PATTERN while Step 12 applies only CONFORMANT names.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CHECKER: check_canon_r1.py o2-zero at 894b41f920 printed 'STEPS MARKED: 16  MARKED JUDGEMENT: 5 [3, 7, 8, 9, 14]' and 'VERDICT: FAIL-O2-JUDGEMENT-STEP', rc=0. o2-marks printed 'STEPS: 16  MARKED WITH A REASON: 16' and 'VERDICT: PASS-O2-ALL-MARKED', rc=0.",
        "REVIEW: org/missions/D14/LGIC/LGIC_CANON/deliverables/CHECKLIST_REVIEW.md@894b41f920 carries one line per step, each with its reason and file:line citations at c08fd0c0eb.",
        "CHECKLIST: infra/logic/10_ONBOARDING_CHECKLIST.md@05d5131e5e. :32-42, the inputs table, carries no table name, partition form, resource set, function word or pipeline directory. :98-103, Step 3(c), records 'the name the pipeline's author gave it'. :176-177 is Step 7's resource set. :194-196 and :208-211 are Steps 8 and 9's <table> and <partition> placeholders. :287-289 mandates opal-partner-<LONG>, and :261-263 applies a name only when it reads CONFORMANT.",
        "CANON: infra/logic/02_DOCTRINE.md@c08fd0c0eb. :179 fixes only a table's case. :183-186 offers three partition forms. :364-365, R9, says bronze keeps 'compact YYYYMMDD'. :385-386 is R11's 'dated/timestamped-in-title parquets'. :216 says FN1's word choice binds 'the NAMER, who has the item's description'. :454, R16's non-application, puts the git source tree outside the canon.",
        "BUILDER: lib/opal_naming.py@c08fd0c0eb :1269-1272 (_segment) and :1287-1300 (key()) check table and partition for shape only. grade('opal-partner-demo', 'DYNAMODB_TABLE') returned ('OUT-OF-PATTERN', 'opal-demo-partner-table'), and grade('opal-partner-49financial', 'DYNAMODB_TABLE') returned ('OUT-OF-PATTERN', 'opal-49f-partner-table'), run read-only by this worker.",
        "RUNBOOK AND CENSUS: infra/aws/users/ONBOARDING.md@c08fd0c0eb :187-199: the auth handler builds the table name opal-partner-{firmId}, and portal-auth's IAM grant covers opal-partner-*. comp-find 'opal-partner' over infra/logic, org/standards and org/missions/D14/LGIC (corpus all) found 61 hits across 502 files, none of them in infra/logic/06_CONFORMANCE_LEDGER.md, infra/logic/registry/ or org/standards/."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CN-o-2 criterion O2-AC2 expects 'VERDICT: PASS-O2-NO-JUDGEMENT': no step of infra/logic/10_ONBOARDING_CHECKLIST.md is marked JUDGEMENT (FWD-5: 'no step where somebody has to invent an answer').",
    "world_is": "A reviewer who did not write the checklist marks 5 of its 16 steps JUDGEMENT. So the criterion does not produce its named result, and the order stays open on O2-AC2; O2-AC1 passes, with 16 of 16 steps marked. Steps 3, 7, 8 and 9 share one cause. Onboarding bundles the build of the firm's pipelines, and the canon fixes a pipeline's homes, formats, compute and name grammar but not its contents. Those contents are: the pipeline directory and a master row's label (Step 3); the resource set and the function words (Step 7); the bronze and silver table names and bronze's partition form (Step 8); and the gold table names, the gold partition form and the owner of a combined build (Step 9). No input carries them, and key() and address() accept any choice of valid shape. Step 14 has a separate cause. It mandates opal-partner-<LONG>, which grade() reads OUT-OF-PATTERN, while Step 12 applies only CONFORMANT names. The auth handler requires that name, no register entry declares the departure, and the checklist names no STOP and no owner for the conflict. INERT: the checklist is a document, and nothing runs until cell C6 (PRD DEC-9).",
    "notes": "Filed by 0.9.0_WK_LGIC_CANON~7 on LGIC_CANON.TO-CN-o-2; this worker kept working. CHECKLIST_REVIEW.md carries the reason for each step. This worker judges the row's form, not its significance: whether the checklist, its inputs or the canon change is for L9 (3.0.0_SA_CVO) and the CN-o-1 recut to decide."
  },
  {
   "id": "LGIC_CANON-S3",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T05:52Z",
   "one_line": "render_naming_section.py drops the per-firm note when it reads firm forms from the scope registry instead of the schema. At NAMING_SCHEMA v1.9 the canon's generated section therefore LOST the demo note carrying RULING DM -- the one line saying why demo reads as a firm in every naming slot -- although the registry row itself carries that text in a note field the renderer never reads.",
   "class": "OBSERVATION",
   "hazard_standing": "ARMED",
   "disarm_owner": "2.0.0_SA_COO~G",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "READ infra/logic/render_naming_section.py at CLOUD 4730cec6ca: the module docstring states firm forms come from NAMING_SCHEMA.json firm_forms while that field exists, else from the FIRM rows of infra/logic/registry/scopes.json, and that the registry is read only when the schema carries no firm_forms. The note text is emitted on the schema path only; the registry branch reads long and short and never note.",
     "MEASURED, the registry DOES hold the content: the FIRM rows of infra/logic/registry/scopes.json carry keys 49financial, inflection, cottonwood and demo, and the demo row is the one of the four whose key list includes note. So the loss is the reader, not the data.",
     "MEASURED, the schema at v1.8 carried the same text: git show CLOUD~:org/standards/NAMING_SCHEMA.json firm_forms is four objects and the demo object carries note = one token; the long and short forms are the same string ... so in every naming slot demo reads as a firm (RULING DM, row W6-S4, v1.7).",
     "RUN, the observable loss: python infra/logic/render_naming_section.py --write on the v1.9 tree changes infra/logic/02_DOCTRINE.md by 3 insertions and 4 deletions. Three of the four deletions are the N2 lead line and blank lines; the fourth is the demo note bullet, which no insertion replaces. Corroborated on a SECOND checkout by 4.0.0_SA_CRO at 783e2f3887 (message 97308), which measured the same 3 insertions / 4 deletions and named the same lost bullet.",
     "NEGATIVE CONTROL: --check reads FRESH -- 0 failure(s) after the render. So the gate that exists for a stale section CANNOT see this -- the section is a faithful render of what the renderer chose to read, and the missing line is invisible to it."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "LGIC_CANON PRD DEC-1 b: the schema is the one owner of the naming enumerations and the canon only presents them. CN-k-1 K1-AC2: render_naming_section.py --check exits 0, the section's bytes equal a fresh render of the stamped files.",
   "world_is": "DEC-1 b's one-owner rule was met by moving the firm forms to the registry, but the renderer's two source paths are not equivalent readers: the schema path emits a per-firm note and the registry path does not. Moving the data therefore moved only PART of it into the canon, and the part left behind is the ruling citation rather than a spelling.",
   "notes": "ARMED, disarm_owner 2.0.0_SA_COO~G. The remedy is a one-line read of the FIRM row's note field in the renderer's registry branch, re-rendering the bullet exactly as the schema path did. It is NOT done here: the renderer is drained cell CN-k-1's deliverable, round 1 is at 3.0.0_SA_CVO for L8/L9, and cutting a round-2 cell before round 1's L10 slug would deadlock that L10 (CLAUDE.md Rule 27, LD-0521). It disarms as a LGIC_CANON round-2 cell. The render was landed anyway under 1.0.0_SA_CTO RULING R-1 (97306): a canon that disagrees with the schema at its own HEAD is the worse state, and this line is recorded and cheap to restore. For 3.0.0_SA_CVO at L9: CN-k-1's K1-AC2 verdict is unaffected -- the section IS a fresh render -- and this row is about what a fresh render omits."
  },
  {
   "id": "LGIC_CANON-S4",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T06:41Z",
   "one_line": "The conformance ledger's section 2 says the firm bucket absorbs opal-data-bd's gold, platinum, STATE and code, but no state plane is a row in that table and an unscoped search of the repo finds the string opal-data-bd/state ZERO times. The canon's own R21 census says every real instance of workflow state is state INSIDE a tier plane and VIOLATED-LIVE, so on current evidence no conformant state/ plane exists anywhere in the estate and the ledger names one in prose.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "READ infra/logic/06_CONFORMANCE_LEDGER.md section 2, the opal-data-49financial/gold/ row: the disposition prose reads CONFORMANT on home (THE firm bucket, D10-2 ruled -- it absorbs opal-data-bd's gold/platinum/state/code). The word state appears only in that prose; section 2's table carries rows for opal-data-bd platinum, gold, silver, schwab/silver, canonical/schwab, bronze, smartx/bronze, schwab/bronze, code and logs/gold, and NO state row.",
     "RUN comp-find 'opal-data-bd/state' at CLOUD 14936be222: 0 hit(s) across 165495 file(s) scanned, corpus=all. The zero is printed with its denominator and with its three disclosed exclusions (18 unreadable, 4636 binary, 68544 ephemeral-floor), so it is a measured zero over the scanned set and not a claim of estate-wide absence.",
     "RUN comp-find 'state/' over infra/logic/: 8 hits across 19 files, all DOC band, none a ledger table row. The substantive ones are 02_DOCTRINE.md:501-503.",
     "READ infra/logic/02_DOCTRINE.md:495-503, rule R21: workflow state is a fifth class, state/, never inside a tier plane; its census names gold/_state/, gold/_parity/, gold/meta/*_watermark.json, gold/manifests/ and otp/state.json, and grades them VIOLATED-LIVE as state inside tier planes, with the D8 migration brief IV.6 mapping each to state/. So the canonical state/ plane is a DESTINATION, not an extant plane.",
     "NEGATIVE CONTROL on the instrument: the same comp-find pattern shape returns non-zero on a term that does exist -- 'state/' over the same directory returned 8 hits. So the zero on opal-data-bd/state is the pattern finding nothing, not the tool failing to run."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "LGIC_CANON PRD: the ledger records each plane's disposition against the canon's numbered rules. Round-1 analysis ruling A-13: round 2's second judged tree is chosen BY MEASUREMENT to engage R3, R8, R14, R15, R17, R19 and R21, and the cell prints which of the seven it reaches.",
   "world_is": "A disposition's PROSE names a plane the same table does not carry as a row, and nothing in the repo corroborates it. Either opal-data-bd has a state prefix nobody censused, or the sentence is describing what the firm bucket WILL hold after the D8 migration and reads as a present fact. The two are not distinguishable from the ledger's own text, which is the defect.",
   "notes": "INERT: nothing reads this sentence as code and no disposition turns on it. It is filed because it is MATERIAL TO ROUND 2's CUT rather than for its own sake: R21 is one of A-13's seven, and if no conformant state/ plane exists then NO candidate tree can reach R21 by carrying one -- a tree reaches it only by carrying state INSIDE a tier plane, which is the violated-live shape. CN-j-4 and CN-j-5's cell must be cut to print the reach honestly, including a printed NOT REACHED, rather than be read as failing when it cannot find a plane that does not exist. CN-l-2 owns the ledger and is where the sentence is corrected: either add the row with its census, or reword to the future tense the D8 brief supports. For 3.0.0_SA_CVO at L9: this row makes no claim about whether the migration is right, only that the ledger states a present fact it does not carry."
  },
  {
   "id": "LGIC_CANON-S5",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T07:35Z",
   "one_line": "ISSUER'S CUT DEFECT. Decomposition v4 s.0d states the round's only internal write contention is CN-k-2 and CN-k-4 on infra/logic/02_DOCTRINE.md. Measured from the ten ISSUED orders' own <paths> blocks, THREE cells write it: CN-k-2, CN-k-3 and CN-k-4. CN-k-3 re-renders the generated section with --write, so the canon is necessarily in its grant. Spawning CN-k-3 beside CN-k-2, which the level-0 grouping invited, would have put two workers on one file in two worktrees.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "RUN at CLOUD 68644b3c19: the <paths> block of all ten round-2 orders parsed and inverted to path -> cells. infra/logic/02_DOCTRINE.md maps to ['CN-k-2','CN-k-3','CN-k-4']; every other write surface of the round maps to exactly one cell. Contended paths: 1 of 10.",
     "READ the CN-k-3 order's own cell text item 3: 'Re-render with --write so the section carries the restored note, and leave --check reading FRESH.' The canon is in its <paths> because the cell cannot do its work without writing it. The order is CORRECT; the decomposition's description of it is not.",
     "READ decomposition v4 s.0d: 'INTERNAL contention, the one this round has: CN-k-2 and CN-k-4 both write infra/logic/02_DOCTRINE.md. They take ONE slot, sequenced.' Two cells named where three write.",
     "CAUSE, traced rather than guessed: the disjointness census in s.0d was computed BEFORE the orders existed, from a hand-written per-cell surface list in the issuer's cut script -- a forward list of what the issuer had in mind. CN-k-3's entry in that list named only the renderer. When the order was written, the canon was added to its <paths> correctly, and the decomposition was never re-measured against the orders.",
     "NEGATIVE CONTROL on the same act: the SIBLING-project half of that census WAS a subtraction, over the parsed <paths> of all 15 non-terminal LGIC_NAMING and LGIC_ENFORCE orders, and it is correct -- the intersection with this round is genuinely empty, re-verified here. So the method was right in one half of the same paragraph and recall in the other."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "CLAUDE.md Rule 24: write the enumeration as the printed denominator MINUS what you exclude, never as a forward list of what you thought of. Spine L6: the fan-out is derived from the decomposition's dependency chains; two task orders on one chain belong to ONE worker's queue.",
   "world_is": "A forward list covers what its author had in mind and omits silently. This one omitted a surface the author himself added to the order twenty minutes later, in the same sitting. \u26a0 AND IT READ AS MEASURED: the paragraph prints a denominator -- 15 sibling orders -- for the half that WAS a subtraction, and the printed number lends its authority to the sentence beside it, which was recall. A denominator certifies the sweep it came from and nothing else in the paragraph.",
   "notes": "INERT: no worker was harmed. CN-k-2 is the only canon writer spawned; CN-k-3 and CN-k-4 are HELD and will be handed to the same slot in sequence after CN-k-2 drains, which is the queue rule the spine already states for two orders on one chain. NOT AN EDIT TO THE DECOMPOSITION: the spec is frozen mid-round and a cell that looks wrong is a row, never an edit -- the sequencing is the issuer's to control at spawn, and it is controlled. For the round-2 analysis: s.0d's contention sentence is wrong by one cell and should be re-cut from the orders' own <paths>, which is the only carrier that IS the grant. For 3.0.0_SA_CVO at L9: the orders themselves are correct and no criterion changes."
  },
  {
   "id": "LGIC_CANON-S6",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T08:02Z",
   "one_line": "ISSUER'S CUT DEFECT, caught before spawn. CN-j-6 is the negative arm and must judge WITHOUT the severity order, but it depends on CN-k-2, whose whole job is to PUT the severity order INTO infra/logic/02_DOCTRINE.md -- which is CN-j-6's named rule source, with no vintage pin. So judge E reads the canon after CN-k-2 lands and meets the severity order there. The order's own warning makes it worse: it says to file a row on finding a severity order 'in a file this order does not name', and the canon IS a named file.",
   "class": "BLOCKING",
   "hazard_standing": "ARMED",
   "disarm_owner": "1.0.0_SA_CTO",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "READ the issued order LGIC_CANON.CN-j-6-r2.judge-e-negative-arm.md at CLOUD ccb69f3ef3: 'depends_on: CN-k-2'; 'Your rule source is infra/logic/02_DOCTRINE.md' with NO commit pin and no instruction to read it at a vintage.",
     "READ the issued order LGIC_CANON.CN-k-2-r2.canon-edit.md, item 2: 'State them ORDERED, least severe to most, in a passage the canon names SEVERITY ORDER'. Its criterion K2-AC2 calls check_canon_r2.py k2-severity, which PASSES only when that passage exists in infra/logic/02_DOCTRINE.md.",
     "SO THE TWO ORDERS ARE JOINTLY UNSATISFIABLE AS I READ THEM: CN-k-2 passes only if the canon carries the severity order; CN-j-6 is briefed 'WITHOUT the severity order' and reads the canon after CN-k-2.",
     "THE ORDER'S GUARD DOES NOT CATCH IT: 'If you find one in a file this order does not name, stop and file a surprise row'. The canon IS named in its Read list, so the guard is silent on exactly the leak that will occur.",
     "AND MY OWN CRITERION WOULD HAVE READ PASS OVER IT: j6-noseverity greps CN-j-6's ORDER FILE for the vocabulary and the phrase SEVERITY ORDER. The order file is clean. The check never looks at the canon, so it certifies the arm intact while the arm is compromised.",
     "NOTHING IS MID-FLIGHT: CN-j-6 is HELD and unspawned; the four running cells are CN-k-2, CN-l-2, LN-f-1 and EN-r-4. Caught by re-running the write-surface census over the running and held sets, not by re-reading the order."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "Round-1 analysis ruling A-1 and the s.3 cell table: 'CN-j-6 judge E: the MDPF tree again, briefed WITHOUT the severity order -- the negative arm', depends_on CN-k-2. The CVO's C-S9: round 1's five-of-five agreement may have come from a scale THE CANON DID NOT CARRY.",
   "world_is": "There are TWO coherent readings of what the arm measures and the cut does not choose between them. READING ONE, the arm as I wrote its prose: E must meet no severity order at all, so it has to judge a canon from BEFORE CN-k-2 -- and then its dependency is backwards and the cell should be pinned to a pre-CN-k-2 vintage or run first. READING TWO, and the one the dependency actually implies: what is withheld from E is a BRIEF stating the scale, while the CANON is exactly where E is supposed to find it -- and if E then agrees with C and D, that is the direct evidence that CN-k-2 made the canon carry what the brief used to supply, which answers C-S9 better than reading one does. Under reading two the cell is sound and only its warning text is wrong.",
   "notes": "ARMED, disarm_owner 1.0.0_SA_CTO: choosing between the two readings is a ruling about what A-1's arm measures, not a measurement I can take, and it decides whether the fix is a vintage pin plus a re-ordered dependency or a two-sentence correction to the warning. I have NOT edited the order -- R-7 ruled an hour ago that adding new work to an unspawned order cuts a cell the decomposition does not name, and while I read this as correcting an instruction that contradicts its own cell rather than as new work, that distinction is the one R-7 just drew and it is the CTO's to draw again. CN-j-6 stays HELD either way; it was held on CN-k-2 already, so this costs no time. MY REC: reading two, and correct CN-j-6's warning to say the canon is where the scale legitimately lives and what is withheld is a brief -- plus widen j6-noseverity, or accept that it grades the brief and not the arm, and say which."
  },
  {
   "id": "LGIC_CANON-S7",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T08:07Z",
   "one_line": "j7-blind tests whether one judge's OUTPUT FILE names another's filename. Blindness is a property of what the WORKER READ, and a judge that read a sibling's file without citing it passes cleanly. What actually enforces the blind is WORKTREE ISOLATION plus SPAWN ORDER: the three judges write into ONE directory, so a judge spawned after a sibling's DRAIN has that sibling's output in its own base and the blind is broken silently. Nothing in the cut states that ordering and no criterion can see it.",
   "class": "OBSERVATION",
   "hazard_standing": "ARMED",
   "disarm_owner": "2.0.0_SA_COO~G",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "READ check_canon_r2.py j7_blind at CLOUD 225e7e52b5: it reads each judge TSV and flags a pair only where one file contains the literal string 'judge-<other>'. It tests CITATION, not READING.",
     "MEASURED, the three judges' write surfaces from their own <paths>: CN-j-4 -> exercises/r2/judge-c.tsv, CN-j-5 -> judge-d.tsv, CN-j-6 -> judge-e.tsv. ONE directory, three files.",
     "MEASURED at CLOUD: git ls-tree over exercises/r2/ is EMPTY, so no judge output is on CLOUD yet and every judge spawned from today's HEAD starts blind by construction.",
     "NEGATIVE CONTROL that the path shape is real, not hypothetical: round 1's exercises/ carries judge-a.tsv, judge-b.tsv and judge-compare.md at HEAD. A round-1 judge spawned after its sibling's drain would have had the sibling's verdicts in its base.",
     "THE ENFORCEMENT IS STRUCTURAL AND NOT A CHECK: each worker has its own linked worktree and its own branch, so a sibling's UNDRAINED output is not present in it. That property holds only while no sibling has drained. It is a fact about spawn ordering, which is the ISSUER's to control, and the issuer's alone."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "Round-1 analysis ruling A-13 and decomposition v4 s.0d: the judges are blind to each other and to CN-k-2's author; a scorer never scores its own work. Criterion J7-AC3 (j7-blind) is the round's only mechanical bar on that property.",
   "world_is": "A blindness bar that greps output files can only catch a judge careless enough to name the file it copied. The realistic leak -- reading a sibling's verdicts and writing your own prose -- leaves no trace in the artifact, so the criterion cannot go non-zero on it. The property is real and is genuinely enforced, just not by the thing that claims to enforce it: it is enforced by worktree isolation, which holds until the first judge drains.",
   "notes": "ARMED, disarm_owner 2.0.0_SA_COO~G, and the disarm is a SEQUENCING COMMITMENT rather than an edit, because the control is mine: the three judges CN-j-4, CN-j-5 and CN-j-6 are spawned from bases that predate ANY judge drain, and none of the three is drained until all three have produced their output. That keeps the blind structurally true for the whole arm. It disarms when all three have reported and the issuer records the three spawn bases and the drain order in the drain-end read. \u26a0 THE CRITERION IS NOT REMOVED and is not useless -- it still catches a copied filename, which is the careless case. It is re-read as what it is: a cheap bar on citation, not a measurement of blindness. For 3.0.0_SA_CVO at L9: J7-AC3 passing means no judge file names another, and nothing more; the blindness itself rests on the spawn bases recorded at the drain. Round 1's judges were run before this was noticed and their ordering is not re-litigated here."
  },
  {
   "id": "LGIC_CANON-W1-S3",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~1",
   "surfaced_at": "2026-09-16T07:49Z",
   "one_line": "The CN-k-2-r2 worker face's Read pointer 'org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23' names a path that never existed; the commit that actually carries that file wrote it to a different directory.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "RUN (in this worktree, spawn base 68644b3c19): comp-read org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md --for ... -> 'comp-read: ERROR: not a file: org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md'.",
     "RUN: git show --stat 26ae876d23 -- org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md -> only the commit header, no file stat line: that commit never touched that path.",
     "RUN: git log --oneline -- org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md -> zero commits, whole history.",
     "RUN: comp-find --name 'LGIC_CANON_ROUND1_ANALYSIS.md' --files -> exactly 1 hit: org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND1_ANALYSIS.md; git log -1 --format=%H on that path returns 26ae876d2380fee0de9b6deec55db3d972241a88, the exact commit the worker face cites."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "Worker face 'Read': the round-1 analysis s.2 rulings A-1, A-2, A-4 and A-9 (org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23).",
   "world_is": "No file exists or ever existed at org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md at that commit or any commit; the file the worker face means lives at org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND1_ANALYSIS.md, introduced by that same commit 26ae876d23. Not blocking -- comp-find located it and this cell's five acceptance criteria do not depend on the pointer resolving on the first try -- filed as FORM only.",
   "notes": "INERT: worked around by comp-find within the same turn; nothing in this cell's acceptance criteria (K2-AC1..AC6, K2-J1) reads this path directly. Class is OBSERVATION per Rule 22a footnote (a citation ages separately from what it points at) and the general instruction that a path elsewhere is a surprise row, never a silent workaround."
  },
  {
   "id": "LGIC_CANON-W1-S4",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~1",
   "surfaced_at": "2026-09-16T07:49Z",
   "one_line": "The round-1 analysis's round-2 cell table scopes CN-k-2 to serve ruling A-4 (recount R1's census tag) alongside A-1/A-2/A-9, but this task order's WORKER FACE cell text (five numbered edit items) and its expected_criteria (K2-AC1..AC6, K2-J1) carry no item or criterion for R1's census tag, so this cell does not touch it.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "READ org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND1_ANALYSIS.md@26ae876d23, s.3 cell table, the CN-k-2 row: 'what' column includes \"R1's census tag\"; 'rulings' column lists 'A-1, A-2, A-4, A-9'.",
     "READ this task order's WORKER FACE (LGIC_CANON.CN-k-2-r2, issued 2.0.0_SA_COO~G): the five numbered CN-k-2 edit items (axis vocabulary, SEVERITY ORDER, R20-on-every-axis, citation rule, pipeline-instance rule) name nothing about R1 or a census tag; <expected_criteria> lists only K2-AC1..AC6, K2-J1, none of which reads R1.",
     "READ infra/logic/02_DOCTRINE.md R1's rule block (this cell's edit did not touch R1): its census line already carries a dated SUPERSEDED/source-first marker (2026-09-13) from round 1 (changelog v1.0, cell CN-k-1) -- so A-4's 'if the tag predates the source-first ruling, a vintage mark is the whole fix' may already be satisfied, or may simply have been left out of round 2's cut; the worker face does not say which and this cell has no grant or criterion to act on it either way."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "Decomp table (round-1 analysis s.3): CN-k-2 serves rulings A-1, A-2, A-4, A-9, including 'R1's census tag'.",
   "world_is": "This cell's actual worker face narrows CN-k-2 to five items and six mechanical criteria plus one judgment criterion, none reading R1's census tag; A-4 is named only under 'Read' as background, not as an edit instruction or a tested criterion.",
   "notes": "INERT: no criterion of this cell depends on R1's census tag, and R1 is outside this cell's five stated edit items, so this cell leaves it untouched by design rather than by oversight. Filed so the round's owner can confirm whether A-4 was deliberately dropped from round 2's issuance or is still owed by another cell."
  },
  {
   "id": "LGIC_CANON-W3-S2",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~3",
   "surfaced_at": "2026-09-16T09:05Z",
   "one_line": "check_canon_r2.py's l2_recount() parses ledger_recount.py's SECTION/TOTAL lines with \\S+ single-token regexes, so it cannot read the multi-word disposition-class and register labels (MIGRATE (home), AWAITING a word, PLANE ROWS (the denominator), ...) that round 1's OWN checker (a non-greedy .+?: regex) reads correctly on the SAME script's SAME output; L2-AC4 therefore reads FAIL-L2-COUNTS-REPRODUCED no matter what the ledger's true counts are.",
   "class": "BLOCKING",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "CHECKER (defect): org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py@1416c279781615087e1d53cbe628782c6b6c1a50:550-551 'sec = re.findall(r\"^SECTION\\s+(\\S+)\\s+(\\d+)\", o, re.M)' / 'tot = re.findall(r\"^TOTAL\\s+(\\S+)\\s+(\\d+)\", o, re.M)' -- a single non-whitespace token for the label, then digits as the immediately next whitespace-separated token; :557 'ok = bool(sec) and bool(tot) and not mismatch'.",
     "COMPARISON (same artifact, a working parser): fixed_inputs/r1/check_canon_r1.py@4058a566067c2b6b9bbb66b6f351cd338d0069af:781-782 'totals = {k.strip().lower(): int(v) for k, v in re.findall(r\"^TOTAL (.+?): (\\d+)\\s*$\", out or \"\", re.M)}' and 'sections = re.findall(r\"^SECTION .+: \\d+ rows \\(instrument: .+\\)\\s*$\", out or \"\", re.M)' -- non-greedy, colon-aware, multi-word-safe; this is round 1's OWN validated reader of the SAME script.",
     "SOURCE (unchanged by CN-l-2's own three items -- X6's axis, utf-8, the header revert -- none of which touch these lines): ledger_recount.py:189 'print(\"SECTION %s: %d rows (instrument: %s)\" % (s[\"heading\"], n, instr))' prints the full section heading (spaces included) before the row count; :300 'print(\"TOTAL %s: %d\" % (label, mine))' glues the label to a colon with no separating space, and most section-7 labels are multi-word (MIGRATE (home), MIGRATE (format only), MIGRATE (grammar), AWAITING a word, OUT OF SCOPE, DECLARED EXCEPTION, PLANE ROWS (the denominator), REGISTER ENTRIES (the denominator)) -- none is a single \\S+ token.",
     "RUN, round 1 PASSES on this exact script: timeout 120 python fixed_inputs/r1/check_canon_r1.py l1-recount printed 'script rc: 0  SECTION LINES: 10  COUNT ROWS COMPARED: 14  DIFFERING: 0  RE-DERIVED BY HAND STILL PRINTED: False' and 'VERDICT: PASS-L1-RECOUNT-AGREES', rc=0.",
     "RUN, round 2 FAILS on the same script, same run: timeout 120 python fixed_inputs/r2/check_canon_r2.py l2-recount printed 'SECTION lines: 0 ; TOTAL lines: 6' and \"TOTAL rows the ledger's own table does not carry at the counted value, denominator 6: 6 ['CONFORMANT:', 'RETIRE:', 'GRANTED:', 'OWED:', 'DECIDED:']\" and 'VERDICT: FAIL-L2-COUNTS-REPRODUCED', rc=0 -- the 6 captured TOTAL labels are exactly the single-word disposition/register classes, each mismatched only because \\S+ glues the trailing colon onto the label (e.g. 'CONFORMANT:' vs the ledger's own cell 'CONFORMANT'); the 8 multi-word labels are never even captured, and no SECTION line matches at all since the heading's second word is never digits.",
     "NEGATIVE CONTROL: a \\S+ regex requiring the token immediately after the label to be pure digits is structurally unable to match a label containing an internal space -- no edit to ledger_recount.py's label TEXT can satisfy it without breaking round 1's own already-PASSING l1-recount (which requires the descriptive multi-word format), so the fix is not reachable inside CN-l-2's grant without regressing a drained round-1 criterion."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "LGIC_CANON.CN-l-2-r2 criterion L2-AC4 expects 'VERDICT: PASS-L2-COUNTS-REPRODUCED' from check_canon_r2.py l2-recount: section 7's totals, run through ledger_recount.py, are reproduced by the instrument.",
   "world_is": "check_canon_r2.py's l2_recount() cannot parse ledger_recount.py's SECTION/TOTAL lines for any multi-word label, and even its single-word matches fail on a glued trailing colon; round 1's own checker parses the identical script's identical output correctly with a non-greedy regex. The criterion is unsatisfiable from CN-l-2's grant without either (a) editing the read-only fixed checker, which BOUNDS forbids, or (b) collapsing ledger_recount.py's section-7 labels to single tokens, which would regress round 1's already-PASSING l1-recount and misstate the ledger's own multi-word class names. L2-AC1, L2-AC2 and L2-AC3 PASS by output at this commit; L2-AC4 is recorded FAIL by output, per BOUNDS' 'fixed input is itself DEFECTIVE ... keep your hands off it.'",
   "notes": "Filed by 0.9.0_WK_LGIC_CANON~3 on LGIC_CANON.CN-l-2-r2; kept working, ran the remaining criteria, and recorded this proof_of_spec row as FAIL rather than editing check_canon_r2.py or degrading ledger_recount.py's round-1-validated print format. This worker judges the row's form, not its significance: whether check_canon_r2.py's l2-recount regex is repaired, replaced, or the criterion is re-cut is for 3.0.0_SA_CVO at L9 / 2.0.0_SA_COO~G's recut to decide."
  },
  {
   "id": "LGIC_CANON-W3-S3",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~3",
   "surfaced_at": "2026-09-16T10:40Z",
   "one_line": "Disposes LGIC_CANON-W3-S2: the issuer, 2.0.0_SA_COO~G, repaired check_canon_r2.py's l2_recount() in TWO successive passes -- 143f6da6d9 fixed the \\S+-only SECTION/TOTAL regex, then 463c429147 fixed a SECOND defect that pass exposed (comparing markdown emphasis **23** against the bare number 23) -- confirmed with a planted-wrong-count negative control before landing. L2-AC4 now reads PASS-L2-COUNTS-REPRODUCED; this worker re-ran all four L2-AC criteria fresh against the repaired checker and independently corroborated with a second planted mutant (M5).",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "REPAIR COMMITS (read-only fixed input, not staged/committed by this worker): org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py@143f6da6d9 changes l2_recount()'s SECTION regex to `r\"^SECTION\\s+(.+?):\\s+(\\d+)\\s+rows\"` and TOTAL to `r\"^TOTAL\\s+(.+?):\\s*(\\d+)\\s*$\"`, matching the script's real `SECTION <label>: <n> rows (...)` / `TOTAL <label>: <n>` shape instead of the original `\\S+`-only pair. @463c429147 adds a `cell()` helper stripping `*`/`` ` `` from every section-7 table cell before comparison, replacing the old raw substring test that read the ledger's own bold markup (`**23**`) as a mismatch against the plain number the script prints (`23`).",
     "CONTENT CHECK (this worker's own instrument, not the coordinator's word): `diff <(git show 463c429147:org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py) org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py` at this worker's worktree: empty (byte-identical). The file in-worktree is exactly CLOUD@463c429147, not a claim taken on trust.",
     "RE-RUN, all four criteria fresh against the repaired checker: `check_canon_r2.py l2-x6-axis|l2-utf8|l2-header|l2-recount` printed `VERDICT: PASS-L2-X6-ON-ITS-AXIS`, `PASS-L2-RECOUNT-READS-UTF8`, `PASS-L2-HEADER-REVERTED`, `PASS-L2-COUNTS-REPRODUCED` (l2-recount: `SECTION lines parsed: 10 | TOTAL lines parsed: 14 | section-7 table rows: 20` / `denominator 14: 0 []`), each run 3 times, identical every time.",
     "INDEPENDENT DISCRIMINATION CONTROL (mutant M5, this worker's, distinct from the issuer's own planted-999 control): CONFORMANT's ledger cell changed 21 -> 999, `l2-recount` printed `denominator 14: 1 [('CONFORMANT', '21')] | VERDICT: FAIL-L2-COUNTS-REPRODUCED`, ledger restored via `git checkout 45f5930e32 -- infra/logic/06_CONFORMANCE_LEDGER.md`, confirmed clean by `git diff --stat` (empty).",
     "DRAIN CONFIRMED BY CONTENT: `git merge-base --is-ancestor <c> CLOUD` true for this worker's three commits (45f5930e32, 22cd1add5e, 3074e3bcbf) and for ba15ed94a5, the drain commit on CLOUD naming CN-l-2 and this row's disposition."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "row LGIC_CANON-W3-S2's world_is: L2-AC4 unsatisfiable from CN-l-2's grant because check_canon_r2.py's l2_recount() cannot parse ledger_recount.py's multi-word SECTION/TOTAL output.",
   "world_is": "The finding was correct and the fix landed outside CN-l-2's grant, exactly as S2 said it would have to. The repair took the issuer two passes, not one, and the SECOND defect (markdown emphasis compared as if it were the value) was the same CLASS of instrument error S2 already named in kind -- a checker built expectations of the artifact's presentation rather than its content -- just on a different field. Nothing about the ledger or ledger_recount.py changed for this fix; both were already correct, as S2's own denominator (14 of 14 AGREE via a direct run) and round 1's l1-recount already showed.",
   "notes": "Filed by 0.9.0_WK_LGIC_CANON~3 on LGIC_CANON.CN-l-2-r2 disposing LGIC_CANON-W3-S2's mechanical blocker, per 2.0.0_SA_COO~G's resume instruction. L2-AC4 now PASSES by output; the proof_of_spec instance at org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/LGIC_CANON.CN-l-2-r2.ledger-hygiene.proof_of_spec.json is updated to match and the task order's <status> flips to complete in the same drain. Disposition kept UNDER_INVESTIGATION: GRADUATED is a disposition this project's own channel shows set only by 3.0.0_SA_CVO at L9 adjudication (every GRADUATED row here is surfaced_by 3.0.0_SA_CVO) -- this worker records that the mechanical blocker is resolved and leaves the register's classification of the finding to the CVO, never self-graded."
  },
  {
   "id": "LGIC_CANON-W5-S2",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~5",
   "surfaced_at": "2026-09-16T08:37Z",
   "one_line": "check_canon_r2.py's j5-reach (and j4-reach, j6-reach) subcommand does a whole-file \\bR<n>\\b regex over every judge row, so it cannot tell a rule my row names as REACHED from one my own prose names as NOT REACHED; my judge-d.tsv explicitly determines 3 of 7 reached and 4 of 7 not reached, and the checker's own printed line reads 'REACHED (7): [R3, R8, R14, R15, R17, R19, R21]' because my why-text spells out the not-reached rule ids while explaining why.",
   "class": "OBSERVATION",
   "hazard_standing": "ARMED",
   "disarm_owner": "3.0.0_SA_CVO",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "READ check_canon_r2.py j_reach (this worktree, HEAD): 'blob = \"\\t\".join(...); reached = [r for r in SEVEN_RULES if re.search(r\"\\b%s\\b\" % r, blob)]' -- a plain whole-word search over the ENTIRE row text (every column, including 'why'), with no distinction between a rule cited as reached and one cited while explaining it is not reached.",
     "RUN (this worktree): python .../check_canon_r2.py j5-reach on the committed judge-d.tsv -> stdout 'REACHED (7): [R3, R8, R14, R15, R17, R19, R21]  NOT REACHED (0): []', though judge-d.tsv's own per-row reach column and its last row's why-text state REACHED (3): R14, R17, R19 and NOT REACHED (4): R3, R8, R15, R21, with the reasoning for each.",
     "The criterion itself (J5-AC3) still reads PASS regardless, because j_reach's verdict only requires `reached` non-empty (out(\"PASS-...\" if reached else \"FAIL-...\")) -- so this is not a criterion failure, it is the checker's own summary line disagreeing with the file it just read.",
     "The fixed input CN_SEVEN_RULES.json's own _about field names this exact hazard for R21 by name ('a judge asked to find a state/ plane will not find one, and a criterion that demanded it would be unsatisfiable') but the checker's blob-scan cannot even represent a correctly-printed NOT REACHED without mis-scoring it as reached."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "Order text: '\u26db A PRINTED NOT REACHED IS A CORRECT ANSWER'; check_canon_r2.py j_reach docstring: 'A-13: the cell PRINTS which of the seven rules the tree reaches... A printed NOT REACHED is a legitimate outcome'.",
   "world_is": "The checker's own stdout for j5-reach (and the identical j4-reach/j6-reach shape) cannot distinguish 'this rule is reached' from 'this rule is named while explaining it is not reached', so its printed REACHED/NOT REACHED partition is not evidence of what a judge actually determined -- only the judge's own row content is. A reader (a CN-j-7 preparer, or the L9 adjudicator) who trusts the checker's stdout instead of reading judge-d.tsv's own reach column and why-text would conclude judge D found all seven rules reached, which is the opposite of what this row's own analysis states for R3, R8, R15 and R21.",
   "notes": "ARMED, disarm_owner 3.0.0_SA_CVO: J5-J1 is graded at L9 from the file's content, not from this checker's summary line, so the disarm is reading judge-d.tsv itself (the per-row reach column plus the last row's tree-wide summary) rather than the j5-reach stdout when grading J5-J1 and when CN-j-7 compiles the union across judges C/D/E. I have not touched the checker (fixed input, read-only) and my own criteria (J5-AC1..AC3) all pass as committed; this is filed as FORM on the instrument, not a defect in my row. Judged the row's form, not its significance."
  },
  {
   "id": "LGIC_CANON-S8",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T09:05Z",
   "one_line": "ISSUER'S DISARM OF LGIC_CANON-S7: the three round-2 judges' spawn bases and drain order, measured from git alone -- all three branches created from ONE base at which no judge output existed, and no judge drained until all three had produced.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "S7 established that j7-blind tests CITATION (does one judge's output name another's filename) and cannot see the realistic leak, which is a judge READING a sibling's verdicts. It named the real control as WORKTREE ISOLATION plus SPAWN ORDER, and set the disarm as recording the three spawn bases and the drain order in the drain-end read. This row is that record.",
     "SPAWN BASES, read from each branch's own reflog creation entry (git reflog show <branch> --date=iso, oldest entry 'branch: Created from HEAD'): wk-lgic-canon-2-4 (judge C) 49b4a5b74a at 2026-09-16 04:13:48 -0400; wk-lgic-canon-2-5 (judge D) 49b4a5b74a at 04:14:29; wk-lgic-canon-2-6 (judge E) 49b4a5b74a at 04:15:13. ONE base, all three, inside 85 seconds.",
     "THE BLINDNESS DISCRIMINATOR, at that base: git ls-tree -r --name-only 49b4a5b74a -- .../deliverables/exercises/r2/ returns ZERO paths, so no judge's checkout could have carried a sibling's verdicts however it behaved.",
     "POSITIVE CONTROL on that same read, same command, same commit: git ls-tree -r --name-only 49b4a5b74a -- .../deliverables/exercises/ returns SIX paths (judge-a.tsv, judge-b.tsv, judge-compare.md, naming-a.tsv, naming-b.tsv, naming-compare.md), which is round 1's output. The empty r2 read is a TRUE ABSENCE, not a broken pathspec -- and round 1's files are the negative-arm proof S7 cited, that a judge spawned after a sibling's drain WOULD have found its verdicts in its base.",
     "DRAIN ORDER, and every drain is AFTER all three judges had written their output: judge E 3af1944705, judge D 77db118b74 (merge of wk-lgic-canon-2-5), judge C 44265c6e77 (merge of wk-lgic-canon-2-4). Before the first drain this seat measured that all three worktrees carried their own TSV, which is the condition S7 committed to.",
     "The commitment S7 made, quoted from the channel: 'the three judges CN-j-4, CN-j-5 and CN-j-6 are spawned from bases that predate ANY judge drain, and none of the three is drained until all three have produced their output.' Both halves are measured above and both hold."
    ]
   },
   "disposition": "DISMISSED_WITH_REASON",
   "dismissal_reason": "S7's own disarm condition is met and measured: the three judge branches were created from the single base 49b4a5b74a within 85 seconds, git ls-tree over exercises/r2/ at that base returns ZERO paths while the identical command one directory up returns SIX (the positive control that makes the empty read a true absence rather than a broken pathspec), and all three drains (E 3af1944705, D 77db118b74, C 44265c6e77) landed after all three judges had produced output. S7 asked for the spawn bases and the drain order recorded in the drain-end read; this is that record. Dismissed as the DISARM of S7, not as a judgement that j7-blind measures blindness -- it does not, and J7-AC3 stays in the cut as a bar on citation only.",
   "spec_asserts": "LGIC_CANON-S7: blindness between the round-2 judges is enforced by worktree isolation and spawn order, not by the j7-blind criterion, and the disarm is recording the three spawn bases and the drain order.",
   "world_is": "All three judge branches were created from the single base 49b4a5b74a within 85 seconds, that base carries no file under exercises/r2/ while carrying six files under exercises/ on the identical command, and the three drains all landed after all three judges had produced their output. The sequencing commitment held as written.",
   "notes": "INERT. This disarms S7 and nothing else. J7-AC3 (j7-blind) is NOT removed and is still a cheap bar on a copied filename; it is simply not a measurement of blindness, and nobody at L9 should read its PASS as more than citation hygiene. Judged the row's form, not its significance."
  },
  {
   "id": "LGIC_CANON-S9",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T09:07Z",
   "one_line": "ISSUER'S REPAIR of the defect worker row LGIC_CANON-W5-S2 found in MY fixed input: j_reach scanned the WHOLE judge row for rule ids, so it counted a rule a judge NAMED while explaining it is NOT reached -- and it manufactured a 7-versus-3 disagreement between judges C and D who in fact agree exactly.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "THE DEFECT, as W5-S2 stated it: check_canon_r2.py j_reach built blob = every cell of every judge row joined, then tested each of A-13's seven rule ids with a whole-word regex over that blob. The 'why' column is in the blob, so a judge explaining WHY R21 is not reached made R21 read as reached.",
     "THE DISCRIMINATING PAIR, measured across the three drained judges before touching anything -- whole-row scan versus the TSV's own named 'reach' column: judge C 3 [R14,R17,R19] vs 3 [R14,R17,R19] (agrees); judge D 7 [R3,R8,R14,R15,R17,R19,R21] vs 3 [R14,R17,R19] (DIFFERS); judge E 3 [R8,R14,R19] vs 2 [R14,R19] (DIFFERS, though no j6-reach subcommand exists so E is not graded on reach).",
     "WHY THE DIFFERENCE IS NOT ABOUT THE JUDGES: C and D judged the same tree and reached the SAME determination. The instrument read them differently only because judge D spelled out the not-reached rule ids in its why-text and judge C did not. The reading was a property of each judge's PROSE STYLE, not of what it determined.",
     "THE HARM THIS BLOCKS, and it is the reason the repair happens now rather than at L9: CN-j-7 is the cell that traces DISAGREEMENTS between the judges. Run against the old instrument it would have traced a 7-versus-3 reach disagreement between C and D that does not exist, and an agreement between the two briefed judges is precisely the evidence this round wants.",
     "THE REPAIR: a new column(path, name) helper reads a column by the TSV's OWN HEADER rather than by position (an index breaks silently when a column is inserted; a name refuses loudly), and j_reach now scans only the 'reach' column. When the whole-row scan would differ, the criterion PRINTS that it differs and by how much, so the evidence carries its own discriminator instead of hiding the old reading.",
     "RETROACTIVELY VERDICT-NEUTRAL, MEASURED BEFORE THE EDIT, which is why no drained cell re-opens: j_reach's verdict is PASS if reached is non-empty, and the scoped read is non-empty for every judge (C 3, D 3, E 2). J4-AC3 and J5-AC3 read PASS under BOTH the old and the new instrument. No proof instance is invalidated -- each one's expect is the verdict token, which does not move.",
     "NEGATIVE CONTROLS, because a criterion that now passes must still be able to fail. Run on a COPY of judge-d.tsv: untouched -> PASS (positive control); reach column blanked to '-' -> REACHED (0), FAIL-J5-REACH-PRINTED; reach column deleted entirely -> 'the judge file carries no reach column', FAIL. The artifact was then restored and the restore PROVEN by byte equality against the pre-control bytes (6923 == 6923), not by re-running the checker.",
     "The file compiles under python -W error::SyntaxWarning, stays pure LF (0 CRLF) and keeps its 6 non-ASCII characters -- per CLAUDE.md s.4, a subset removal converts a loud failure into silent mojibake, so the count is held constant deliberately."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "j_reach's docstring: 'A-13: the cell PRINTS which of the seven rules the tree reaches. A printed NOT REACHED is a legitimate outcome.'",
   "world_is": "Until this repair the printed partition was not a reading of what any judge determined -- it was a reading of which rule ids happened to appear anywhere in the judge's row text, including inside prose arguing the opposite. It now reads the judge's own reach column and discloses where the old reading differed.",
   "notes": "INERT: the instrument is fixed and exercised both ways, and no drained cell's verdict moves. THIS DOES NOT DISPOSE W5-S2 -- that row's disarm_owner is 3.0.0_SA_CVO and its disposition is the CVO's at L9, not this seat's; an issuer cannot close a worker's row by repairing the thing it reported. FOURTH defect of mine in a fixed input this session, and the fourth found by a worker rather than by me: 0.9.0_WK_LGIC_CANON~5 filed it, left its order on the evidence, and did not degrade its own file to fit my checker. A worker's measured claim that disagrees with my instrument is evidence about my instrument."
  },
  {
   "id": "LGIC_CANON-W2-S3",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~2",
   "surfaced_at": "2026-09-16T09:34Z",
   "one_line": "The fixed input's k3-contentdiff DOCSTRING says the content-diff arm 'is exercised against a planted removal, which is this criterion's negative control' -- the subcommand plants nothing and runs no control: it reads the flag string out of the renderer's source, runs --content-diff once on the true tree and passes on 'CONTENT-DIFF: 0'. A criterion that only ever sees the zero case cannot distinguish a working arm from a `print(\"CONTENT-DIFF: 0\")`.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "THE CITED BYTES, printed not grepped: check_canon_r2.py:245-260 @7db18a4464 (the file's own last commit is df30196cc1). Line 246-247 is the docstring quoted above; lines 248-260 are the whole body -- read(RENDER), '--content-diff' in src, one subprocess.run of the renderer with --content-diff, clean = 'CONTENT-DIFF: 0' in o, out(PASS/FAIL). There is no copy, no edit, no removal and no second run anywhere in the subcommand.",
     "WHY IT MATTERS HERE RATHER THAN GENERALLY: K3-J1 asks the CVO whether the arm 'would have caught the lost note, rather than re-implementing the freshness check under a new name'. A constant-emitting stub passes K3-AC2 exactly as a real arm does, so the mechanical criterion carries none of that weight and the judgment criterion carries all of it.",
     "THE CONTROL THE DOCSTRING DESCRIBES, SUPPLIED BY HAND INSTEAD, and it is in this cell's result file: a copy of the renderer with the registry path's note read reverted to the pre-fix '' was run from .scratch/ctl/ (two levels deep so Path(__file__).resolve().parents[2] still resolves to the worktree root) against the section as it then stood. --check printed 'CHECK: FRESH -- 0 failure(s)' and --content-diff printed 'CONTENT-DIFF: 1' naming scopes[demo]/note. Same tree, same moment, two instruments, opposite readings.",
     "NOT ACTED ON: the fixed inputs are read-only to this worker by the order's own BOUNDS, and this row is filed instead of a hand-edit precisely because LGIC_ENFORCE round 2 lost an hour to a corrupt fixture that was papered over in the code."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "check_canon_r2.py k3_contentdiff's docstring @7db18a4464: 'A-11: the renderer gains a content-diff arm -- it must REPORT a dropped line, not pass over it. The arm is exercised against a planted removal, which is this criterion's negative control.'",
   "world_is": "The subcommand's thirteen lines contain no planted removal and no negative control. It checks that the flag string occurs in the renderer's source and that one run on the true tree prints CONTENT-DIFF: 0 -- both of which a constant would satisfy. The criterion is a positive-case bar only, and the arm's discrimination is evidence the worker must supply, which this cell did.",
   "notes": "INERT: the criterion under-tests, it does not mis-test -- nothing it PASSES is false, and this cell's arm does report the dropped note (measured above). Judged the row's FORM, not its significance: whether K3-AC2 should be re-cut with the planted-removal arm its docstring describes is the issuer's call at L9, not this worker's."
  },
  {
   "id": "LGIC_CANON-W2-S4",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~2",
   "surfaced_at": "2026-09-16T09:34Z",
   "one_line": "Building the content-diff arm surfaced a SECOND source item the generated section does not carry, of the same shape as the demo note S3 names: NAMING_SCHEMA.json key.legacy_served_paths has FOUR fields and the renderer's one-line render prints THREE -- home, claim, until_present -- and never `producer`. The arm declares it out-of-section rather than rendering it, because rendering it would move output this order held fixed.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "THE SOURCE: infra/logic/render_naming_section.py:157-160 @7db18a4464 (pre-edit bytes) renders legacy_served_paths as one line, '- **legacy served paths list:** home %s; claim: %s; until present: %s', from lsp.get('home'), lsp.get('claim') and lsp.get('until_present'). The fourth key, producer ('LGIC_NAMING cell LN-g-1: every served path below {source}/{scope}/platinum/ ...'), is read by nothing and appears nowhere between the section markers.",
     "MEASURED, not inferred: with producer left IN the arm's domain the run prints 'CONTENT-DIFF: 1' naming /key/legacy_served_paths/producer on a tree whose --check reads FRESH -- the same silent-drop shape as the demo note. The arm sees it; the freshness check cannot, by construction.",
     "WHY IT IS DECLARED OUT rather than rendered: the cell's item 1 says 'No other output moves', and the only way to make this item CARRIED is to add a field to the render, which moves the section beyond the restored note. So it is named in SCHEMA_OUT_OF_SECTION with its reason ('names the cell that will mint the list; provenance, not content'), and every exclusion is PRINTED on every --content-diff run rather than being a silent filter -- a reader who disagrees can see it and argue.",
     "THE EXCLUSION SET IS SMALL AND PRINTED, and the domain is a subtraction from a denominator, not a forward list: 17 schema paths and 4 registry FIRM-row fields are declared out, and anything NOT named is in the domain by default, so a newly added and unrendered source field is LOUD. After the note fix the run reads 'items carried by the section: 198 of 198'.",
     "This is a pre-existing property of the renderer at its CN-k-1 vintage, not something this cell's edit introduced: the render line predates round 2 and is unchanged by this commit."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "The cell: 'A FIRM row's note renders exactly as the schema path rendered it, so the demo bullet returns. No other output moves.' -- and row LGIC_CANON-S3 frames the loss as the schema-to-registry move costing ONE line.",
   "world_is": "The demo note is not the only source content the section drops. key.legacy_served_paths.producer is dropped the same way and for the same reason -- a field no code path reads -- and no criterion in this cell names it. Restoring it would have moved output the cell froze, so the arm declares and prints it as out-of-section instead, which keeps the fact visible without widening the order.",
   "notes": "INERT: nothing is broken by the exclusion and no criterion turns on it. Filed so that the arm's domain is the CVO's to accept or reject at L9 rather than this worker's quiet choice -- an exclusion that nobody reviews is how a content check becomes a constant. Judged the row's form, not its significance."
  },
  {
   "id": "LGIC_CANON-W7-S4",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~7",
   "surfaced_at": "2026-09-16T12:05Z",
   "one_line": "CN-j-7's cell text asks whether judge E's verdicts diverge from judges C's and D's, but C and D judged the INFLECTION tree (13 planes) and E judged the MDPF tree (7 planes) by their own orders, so the two populations share no plane and no per-plane divergence is computable; the fixed input CN_SEVERITY.md names the intended comparator itself -- round 1's judges on the same tree -- and the comparison was run that way and labelled.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "THE ORDER'S OWN WORDS, at this worktree's base 7db18a4464: org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.CN-j-7-r2.judge-comparison.md item 3, 'C and D had the severity order; E did not. State whether E's verdicts diverge from C's and D's in the way the severity order would predict.'",
     "C's AND D's TREE: LGIC_CANON.CN-j-4-r2.judge-c.md:37 and LGIC_CANON.CN-j-5-r2.judge-d.md:36 both name fixed_inputs/r2/CN_TREE_INFLECTION.md as the tree to judge; judge-c.tsv and judge-d.tsv each carry 13 plane rows whose names are that file's planes.",
     "E's TREE: LGIC_CANON.CN-j-6-r2.judge-e-negative-arm.md, 'Your tree is round 1's MDPF tree, org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/CN_TREE_MDPF.md, unchanged'; judge-e.tsv carries 7 plane rows, P1..P7, all MDPF addresses.",
     "THE FIXED INPUT SAYS SO FROM BOTH SIDES: CN_TREE_INFLECTION.md, 'CN-j-6 (judge E) does NOT read this file -- its tree is round 1's MDPF tree, unchanged, as the negative arm'; CN_SEVERITY.md, 'Judge E judges the same tree round 1's judges did, with the same canon, and WITHOUT this file.'",
     "INTERSECTION, measured: the set of plane strings in judge-c.tsv/judge-d.tsv and the set in judge-e.tsv share ZERO members (13 and 7, union 20). A per-plane-per-axis divergence between E and C/D therefore has an empty denominator.",
     "WHAT WAS DONE INSTEAD, and it is printed in full in the deliverable rather than worked around: section 3a compares E against round 1's judge-a.tsv and judge-b.tsv on the SAME MDPF tree (the population CN_SEVERITY.md names), disclosing that E's 7 planes had to be rolled up per axis with the canon's most-severe rule (02_DOCTRINE.md:130) because E emitted no tree-level verdict; section 3b reports E against C and D at the only grain that population supports, vocabulary and decision discipline, and says so on the section.",
     "NEITHER PART OF THE CELL WAS DROPPED: J7-AC1 (6 disagreement rows, 0 untraced) and J7-AC2 (7 of 7 rules named, NOT REACHED printed) both PASS by output on the delivered file."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "TO LGIC_CANON.CN-j-7-r2, THE CELL item 3: 'C and D had the severity order; E did not. State whether E's verdicts diverge from C's and D's in the way the severity order would predict.' -- and item 1, 'Agreement and disagreement, per plane per axis' over judge-c.tsv, judge-d.tsv and judge-e.tsv together.",
   "world_is": "C and D judged CN_TREE_INFLECTION (13 planes) and E judged CN_TREE_MDPF (7 planes); the two plane sets intersect in zero members, so 'per plane per axis' has a common denominator for C-versus-D (65 axis cells) and none for E-versus-C/D. The with-scale/without-scale contrast the cell exists to read has shared planes only against round 1's judges A and B, which is the comparator CN_SEVERITY.md itself names. Both comparisons are delivered and each is labelled with the population it rests on.",
   "notes": "Filed by 0.9.0_WK_LGIC_CANON~7 on LGIC_CANON.CN-j-7-r2; kept working, nothing edited outside the grant, no fixed input touched. This worker judges the row's FORM, not its significance -- whether the cut intended the cross-tree reading is the issuer's call and whether the substituted comparison answers A-1 is 3.0.0_SA_CVO's at L9."
  },
  {
   "id": "LGIC_CANON-W7-S5",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~7",
   "surfaced_at": "2026-09-16T12:07Z",
   "one_line": "CN_SEVERITY.md claims it is 'the only thing that separates the two arms', but measured on the three round-2 judge outputs the severity ORDER was exercised by NEITHER arm: zero severity-ranking statements in judge C, D or E, where round 1's A and B produced three between them -- because round 2 changed the output grain to per-plane-per-axis, which never forces the most-severe roll-up the order exists to decide.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "THE CLAIM: CN_SEVERITY.md, 'If E's verdicts move toward C's and D's anyway, the agreement round 1 measured was agreement on the canon; if they do not, round 1's five-of-five agreement was partly an artifact of a shared scale that the canon did not carry. That is ruling A-1's question and this file is the only thing that separates the two arms.'",
     "RANKING-LANGUAGE CENSUS, case-insensitive whole-phrase over 'severity | most severe | more severe | less severe', per file, run at base 7db18a4464: judge-c.tsv 0, judge-d.tsv 0, judge-e.tsv 0. ROUND 1, same census, same command: judge-a.tsv 1 ('less severe than UNDETERMINED'), judge-b.tsv 2 ('UNDETERMINED is the more severe finding', 'VIOLATES is the most severe finding').",
     "WHY THE GRAIN AND NOT THE BRIEF EXPLAINS IT: round 1's judges emitted ONE verdict per axis for a whole tree (judge-a.tsv and judge-b.tsv carry 5 axis rows plus 3 naming cases), so two facts on one axis had to be RANKED and both judges said so in prose. Round 2's judges emit one verdict per plane per axis (13 x 5 for C and D, 7 x 5 for E), and a per-plane verdict never forces a roll-up, so the order has no cell to decide.",
     "C AND D HELD THE FILE: LGIC_CANON.CN-j-4-r2.judge-c.md:28 and :37, LGIC_CANON.CN-j-5-r2.judge-d.md:27 and :36 each name fixed_inputs/r2/CN_SEVERITY.md in the Read list. They used it for the VOCABULARY (the five closed values) and, on the evidence of their own text, never for the ORDER.",
     "THE SECOND HALF OF THE SEPARATION IS ALSO GONE, and this is design rather than defect: the canon E read CARRIES the withheld content verbatim -- infra/logic/02_DOCTRINE.md:105-130 (v1.1, landed by CN-k-2 this round) holds the five-value vocabulary, the order CONFORMS < DECLARED-EXCEPTION < DEPARTS-RECOMMENDED < UNDETERMINED < VIOLATES, both non-obvious placements and the most-severe roll-up rule. check_canon_r2.py k2-severity prints '5 of 5 axis verdicts, in this order' and k2-vocab '5 present, absent: none'. RULING R-8 (row LGIC_CANON-S6) states this is intended: what is withheld is a BRIEF, not the canon.",
     "CONSEQUENCE, stated in the deliverable section 3c rather than hidden: the arm as run can answer 'does the canon supply the classification vocabulary' (it does -- j7-e-vocab, denominator 4, absent 0) and cannot answer 'would a judge with no scale at all agree', because no round-2 output contains a place where the ORDER would show.",
     "AND THE MATCH IS A WEAK DISCRIMINATOR INDEPENDENTLY: E's rolled-up axis verdicts (computed by this comparer with the canon's own max rule, since E printed none) tolerate 2 plane-verdict flips on A3 and A5, 4 on A2, 6 on A1 and 7 on A4 before the roll-up moves, so 5-of-5 agreement with round 1's A and B survives several independent reading errors."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "CN_SEVERITY.md: 'THIS FILE IS GIVEN TO CN-j-4 AND CN-j-5 AND IS WITHHELD FROM CN-j-6. THE WITHHOLDING IS THE MEASUREMENT' and 'this file is the only thing that separates the two arms'; TO LGIC_CANON.CN-j-7-r2 item 3, that E's divergence or non-divergence answers C-S9.",
   "world_is": "Measured on the outputs, the file separated nothing observable: 0 severity-ranking statements in the with-scale judges C and D and 0 in the without-scale judge E, against 3 in round 1's two with-scale judges. The severity ORDER is load-bearing only where a roll-up is demanded, and round 2's per-plane grain demands none from any arm. Separately, the canon E read now carries the withheld text verbatim at 02_DOCTRINE.md:105-130, so the without-scale condition no longer exists in this estate even in principle. A no-divergence finding therefore supports 'the canon carries the classification vocabulary' and does not support 'the canon carries the scale that produced round 1's agreement'.",
   "notes": "Filed by 0.9.0_WK_LGIC_CANON~7 on LGIC_CANON.CN-j-7-r2, from the three judge files, round 1's two, the two orders and the canon -- no fixed input edited and nothing outside the grant touched. INERT: nothing degrades by being left alone; it bounds how a PASS on this cell may be read. This worker judges the row's FORM, not its significance: whether the arm should be re-cut to demand a roll-up is the issuer's call and how much the non-divergence proves is 3.0.0_SA_CVO's at L9, which J7-J1 already names."
  },
  {
   "id": "LGIC_CANON-W8-S2",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~8",
   "surfaced_at": "2026-09-16T09:39Z",
   "one_line": "The CN-o-3-r2 worker face swaps the ruling labels on two of its five items: item 2 cites A-10 for 'the sovereign inputs are named where the inputs are given' and item 5 cites A-6 for \"Step 6's second block\", while the round-1 analysis has A-6 = the sovereign inputs and A-10 = Step 6's second comment block. Item 5 then describes A-6's CONTENT (LONG sovereign, SHORT derived) as the thing Step 6 must say once -- which item 2 forbids, since it requires a sovereign mark to live in the INPUTS section and NOT in a step. Worked both elements to the analysis's own CN-o-3 cell row instead of to either label.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "ORDER: org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.CN-o-3-r2.checklist-edit.md @7db18a4464 -- item 2 'The sovereign inputs are named where the inputs are given (A-10)'; item 5 \"Step 6's second block (A-6): LONG is sovereign and SHORT is derived by name(); the step says so once.\"",
     "ANALYSIS: org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND1_ANALYSIS.md @26ae876d23 :73-76 -- 'A-6 (W6-S1) LONG is a sovereign input; SHORT is DERIVED by name() from LONG ... the checklist's INPUTS table names each sovereign input AS a sovereign input'; :95-96 -- 'A-10 (C-S13) Step 6 names the second comment block and keeps it verbatim; the replace-all is scoped to the header.'",
     "CELL ROW: the same analysis's decomposition table, the CN-o-3 line -- 'the checklist edit: sovereign inputs named; Step 6 second block; Step 10's STOP names ADVI_FIRMBKTS; Step 14's STOP names X8; steps 3, 7, 8, 9 take the family | A-6, A-7, A-8, A-9, A-10'. The five ELEMENTS are unambiguous whichever way the two labels are read, so both were built: the INPUTS table gained the SOVEREIGN marks (A-6) and Step 6 gained the second-comment-block clause (A-10).",
     "PATH: the same order names that analysis at org/tier1_exec/1.0.0_SA_CTO/deliverables/LGIC_CANON_ROUND1_ANALYSIS.md@26ae876d23; `git show` there is fatal/does-not-exist, and `git ls-tree -r --name-only 26ae876d23` finds exactly one carrier, the deliverables path above. Same commit, different directory; read at the path that resolves."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "The order's item 2 attributes the sovereign-inputs element to ruling A-10 and item 5 attributes Step 6's second block to ruling A-6; item 5 also says Step 6 must state that LONG is sovereign and SHORT is derived.",
   "world_is": "The round-1 analysis @26ae876d23 assigns those the other way round, and item 5's stated content belongs to A-6, whose own text places it in the INPUTS table rather than in a step. Both elements were implemented per the analysis: SOVEREIGN marks in the INPUTS section only (item 2's own instruction), and the second-comment-block clause in Step 6 (A-10's text).",
   "notes": "INERT: no criterion reads a ruling label, and the five elements the cell row names are built. Filed so that CN-o-4's reviewer and the L9 grade read the checklist against A-6 and A-10 as the analysis states them, not as this order's labels do. The order's citation of the analysis path is also stale in its directory (see evidence PATH), corrected in the same read."
  },
  {
   "id": "LGIC_CANON-W8-S3",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~8",
   "surfaced_at": "2026-09-16T09:39Z",
   "one_line": "Ruling A-6's clause 'SHORT is DERIVED by name() from LONG' does not hold at HEAD: nothing in lib/opal_naming.py derives a short form from a long one. name() LOOKS THE SHORT FORM UP on the identity row, and validate() REFUSES a scopes.json row whose `short` is missing or empty -- so a new firm's SHORT is still a value somebody supplies once, into Step 1's row; only its re-use is derived. The checklist was written to the measurement, not to the clause.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "LOOKUP, NOT DERIVATION: lib/opal_naming.py:1552 @7db18a4464 -- inside name(), `body.append(_long_scope(reg, scope, NAME_SCOPE_CLASSES)[\"short\"])`. The value comes out of the registry row; no function in the file computes a short form from a long one.",
     "REQUIRED FIELD: lib/opal_naming.py:279-281 @7db18a4464 -- for every scopes.json row, `for f in (\"key\", \"class\", \"long\", \"short\", \"tenancy\", \"bucket\"): if not isinstance(row.get(f), str) or not row.get(f): refuse(where, f, \"missing or empty\")`. A FIRM row with no `short` is REFUSED, so Step 1 cannot be completed without the value.",
     "RULING: org/missions/D14/LGIC/LGIC_CANON/deliverables/1.0.0_SA_CTO/LGIC_CANON_ROUND1_ANALYSIS.md@26ae876d23 :73-74 -- 'A-6 (W6-S1) LONG is a sovereign input; SHORT is DERIVED by name() from LONG unless Andrew supplies one'.",
     "PRIOR ROW: LGIC_CANON-W6-S1 (this channel) measured the same thing from the other side at @671925aecc -- NAMING_SCHEMA.json:113 firm_forms is a closed list of four ruled pairs and 'mints no row'; 02_DOCTRINE.md:123-125 R1 says each firm has ONE sanctioned LONG and ONE sanctioned SHORT form, and no canon rule derives either."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "The order's item 5, carrying A-6, states as fact that SHORT 'is derived by name()' and asks the checklist to say so.",
   "world_is": "name() reads `short` off the identity row and validate() refuses a row that lacks it, so the value is supplied, not derived. The checklist's INPUTS table therefore marks `<SHORT>` SOVEREIGN where Andrew gives one and DERIVED otherwise, and states precisely what is derived: the run types it ONCE into Step 1's row, and every later name and generated view reads it from there (name() :1552, Step 4's scope_short and fence patterns).",
   "notes": "INERT: nothing live depends on the clause, and the checklist as written is true of the code. Left for 1.0.0_SA_CTO, A-6's author, if the ruling's wording is to be corrected; a worker judges the form of a surprise, never its significance."
  },
  {
   "id": "LGIC_CANON-W8-S4",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~8",
   "surfaced_at": "2026-09-16T09:39Z",
   "one_line": "check_canon_r2.py o3-sovereign prints 'the INPUTS section names 9 SOVEREIGN input(s)' where 9 is the number of OCCURRENCES of the token SOVEREIGN anywhere in the section -- definition list, prose and table cells alike -- not the number of inputs marked SOVEREIGN, which is 5 of 9 rows. The VERDICT is sound (the token's presence is all the criterion claims to test); only the evidence line mis-describes the set it counted. Not touched: a fixed input is read-only.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "CHECKER: org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_canon_r2.py @7db18a4464, o3_sovereign() -- `marked = re.findall(r\"SOVEREIGN\", blob)` then `print(\"the INPUTS section names %d SOVEREIGN input(s)\" % len(marked))`. findall over a bare token counts occurrences, and the pass test is `if marked`, i.e. presence.",
     "RUN: `timeout 120 python <that file> o3-sovereign` in worktree wk-lgic-canon-2-8 printed 'the INPUTS section names 9 SOVEREIGN input(s)' and 'VERDICT: PASS-O3-SOVEREIGN-INPUTS-NAMED', rc 0, against a table of 9 input rows of which 5 carry the SOVEREIGN mark (4 GIVEN). The two 9s are a coincidence of this edit, which is exactly why the line reads as though it had counted the rows.",
     "BASELINE: the same subcommand on the unedited checklist printed 'the INPUTS section names 0 SOVEREIGN input(s)' / 'VERDICT: FAIL-O3-SOVEREIGN-INPUTS-NAMED', so the criterion does discriminate; the defect is in the evidence line's denominator, not in the verdict."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "O3-AC4's clause: 'the INPUTS section marks its SOVEREIGN inputs', graded by check_canon_r2.py o3-sovereign, whose printed line offers a count of SOVEREIGN inputs.",
   "world_is": "The printed count is of token occurrences in the section blob, not of marked inputs. A reader quoting '9 SOVEREIGN inputs' from this run would be quoting a number that certifies the sweep and not the set: the checklist marks 5 of 9 input rows SOVEREIGN and 4 GIVEN.",
   "notes": "INERT: the criterion's verdict stands and nothing downstream reads the count. Filed rather than worked around -- the fixed inputs are read-only by this order's own bound, and the count that belongs in the record is the one stated here: 5 SOVEREIGN of 9 input rows."
  },
  {
   "id": "LGIC_CANON-S10",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T10:20Z",
   "one_line": "ISSUER'S DISARM OF LGIC_CANON-S3: CN-k-3 drained at 5a391b0c46 and the demo note carrying RULING DM is back in the canon's generated section -- verified by this seat on the SERVED artifact with its own instrument, not from the worker's report.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "S3 said render_naming_section.py's registry path hard-coded the note to empty where the schema path emitted it, so NAMING_SCHEMA v1.9's move of the firm forms cost the canon the demo bullet carrying RULING DM -- the one line saying why demo reads as a firm in every naming slot -- although the registry's own demo row carries that text.",
     "THE REMEDY LANDED: CN-k-3 drained at 5a391b0c46. firm_rows() now reads r.get('note', '') or '' on the registry path, and the --write re-render adds exactly 2 lines to infra/logic/02_DOCTRINE.md with 0 deletions (measured on the drain's first-parent numstat: 2 0). 'No other output moves' is measured, not asserted.",
     "VERIFIED BY THIS SEAT ON THE SERVED ARTIFACT, at HEAD, on the shared checkout rather than in the worker's worktree (an issuer re-run in the worker's own tree is repetition, not corroboration): parsed infra/logic/registry/scopes.json directly -- 4 FIRM rows, exactly ONE (demo) carries a note, which is S3's own measured claim reproduced independently -- then tested that note's text for VERBATIM occurrence in infra/logic/02_DOCTRINE.md. Result: 1 of 1 carried. 'RULING DM' is present in the canon.",
     "MY FIRST READ OF THIS FAILED AND THE FAILURE IS WORTH THE LINE: I assumed scopes.json was a dict of scope objects and it is a dict with _about / tenant_kinds / scopes, so the read raised AttributeError rather than returning a wrong answer. A shape assumption that RAISES is the benign case; had the file been a list of pairs it could have returned an empty FIRM set and read as a clean zero.",
     "THE ARM THAT MAKES THIS NOT RECUR IS THE CELL'S REAL DELIVERABLE, and it is why S3 asked for more than the one-line fix: --content-diff enumerates the SOURCES' content (198 in-domain items, 185 schema + 13 registry) and asks item by item whether the section carries it, printing CONTENT-DIFF: 0 on a correct tree. S3's whole point was that --check could not see this class -- a freshness check compares the section against a fresh render, so a line NO render produces is invisible to it by construction. The worker's own discriminating pair on the pre-fix tree: --check reads 'FRESH -- 0 failure(s)' while --content-diff reads 'DROPPED: scopes.json scopes[demo]/note, CONTENT-DIFF: 1'."
    ]
   },
   "disposition": "DISMISSED_WITH_REASON",
   "dismissal_reason": "The defect S3 named is repaired and the repair is verified at HEAD on the served canon by this seat's own read of the source registry and the generated section (1 of 1 FIRM notes carried verbatim; RULING DM present), not from the worker's report. The arm S3 asked for exists and prints a denominator. INERT: nothing is armed and no act is owed by another seat.",
   "spec_asserts": "The canon's generated naming section renders every FIRM row's note, so RULING DM's demo line reaches a reader of 02_DOCTRINE.md.",
   "world_is": "It does again at HEAD, and a content-diff arm now fails loudly if any source item stops reaching the section -- which is the half that prevents a recurrence, where the note read alone only fixed one line.",
   "notes": "INERT. This disarms S3 and nothing else. \u26a0 TWO THINGS THE SAME CELL RAISED STAY OPEN AND ARE NOT DISPOSED HERE: LGIC_CANON-W2-S3 (my k3-contentdiff criterion's docstring claims it plants a removal as a negative control and the body plants nothing -- a constant print would pass it; the worker supplied the control by hand) and LGIC_CANON-W2-S4 (key.legacy_served_paths has four fields and the render prints three; `producer` is read by nothing, declared out-of-section with its reason rather than rendered, for the CVO to accept). Both are the CVO's at L9 and both ride the round-2 slug. 1.0.0_SA_CTO has ruled (R-9) that W2-S3 rides the slug with nothing further owed now."
  },
  {
   "id": "LGIC_CANON-S11",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T10:30Z",
   "one_line": "LGIC_CANON ROUND 2 CANNOT REACH 'every order terminal' ON ITS OWN: CN-k-4 waits on ruling A-3's adjacency test landing in NAMING_SCHEMA.json, that edit is LGIC_NAMING's, and it is NOT at HEAD -- so the round-2 L10 slug is gated behind a LGIC_NAMING round that has not been cut.",
   "class": "BLOCKING",
   "hazard_standing": "ARMED",
   "disarm_owner": "2.0.0_SA_COO~G",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "THE CELL'S OWN TEXT: CN-k-4 says 'Ruling A-3 puts the bd adjacency test into NAMING_SCHEMA.json, and that edit is LGIC_NAMING's, not yours. When it lands, the canon's generated section must be re-rendered... If the schema does not carry an adjacency test when you run, K4-AC1 FAILs by measurement and your order stays open -- that is a correct result and NOT a reason to edit the schema, which is not yours.' Its header reads depends_on: LGIC_NAMING's schema cell (cross-project READ dependency, disclosed); spawned only when it drains.",
     "MEASURED AT HEAD, TWO INSTRUMENTS. (1) comp-find 'adjacen' org/standards/NAMING_SCHEMA.json --limit 10: 0 hit(s) across 1 file(s) scanned. (2) A structural read of the parsed JSON, printing its denominator: 271 schema paths total, 0 matching 'adjacen', 0 matching 'test'; raw text occurrences of 'adjacen' and 'adjacency' are both 0. The schema declares version v1.9.",
     "THE SECOND INSTRUMENT EXISTS BECAUSE THE FIRST COULD NOT BE TRUSTED ALONE: comp-find's own output says a zero over one scanned file is 'not a claim the term is absent' and warns that the pattern may be wrong. The structural read answers a different question -- what the schema DOES carry -- and its 9 paths matching 'bd' are LAMBDA type entries and /refused_tokens/bd, none of them an adjacency test. So the absence is of the TEST, established by enumerating what is present rather than by failing to find what is not.",
     "THE CHAIN, and it is the reason this is BLOCKING rather than a note: LGIC_CANON round 2's L10 slug requires every order terminal. CN-k-4 cannot go terminal until A-3's edit lands. A-3's edit is LGIC_NAMING's and was not in its round 4 (round 4 is fully terminal at 31 orders and handed to 3.0.0_SA_CVO for L8). So it belongs to LGIC_NAMING round 5 -- which under LD-0521 is cut only AFTER round 4's L10 slug and 1.0.0_SA_CTO's round-4 analysis.",
     "WHAT IS NOT CLAIMED HERE: that anyone is late or that any seat holds work it should have done. Round 4's slug is 3.0.0_SA_CVO's to produce and the analysis is 1.0.0_SA_CTO's, both in the correct order, and neither is overdue. This row records a DEPENDENCY SHAPE, not a delay."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "A round's cells are cut so that the round can reach terminality within itself; L6's coverage is the whole decomposition and L10 closes when every order is terminal and every row dispositioned.",
   "world_is": "Round 2 carries one cell whose acceptance depends on an artifact another project produces in a round that is itself gated behind two other seats' limbs. Round 2 can reach 'every OTHER order terminal' and stop there; the last order's terminality is not reachable by any act of this seat or this project.",
   "notes": "ARMED, disarm_owner 2.0.0_SA_COO~G. NOT SPAWNING CN-k-4 on a known-red measurement: the cell would correctly FAIL K4-AC1 and leave its order open, which costs a worker, a worktree and about 1.5 GB to learn what two reads just established for free. Disarms when either (a) A-3's adjacency test is at HEAD in NAMING_SCHEMA.json and CN-k-4 is spawned against it, or (b) 1.0.0_SA_CTO rules at the round-2 analysis that CN-k-4 is carried OUT of round 2 into a later round, which would let round 2's slug close on the cells it can actually finish. \u26a0 (b) is the CTO's call and not this seat's to assume -- the decomposition is FROZEN mid-round and moving a cell out of a round is not an issuer's act. Raised to 1.0.0_SA_CTO with the round-2 state rather than held silently."
  },
  {
   "id": "LGIC_CANON-S12",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T10:25Z",
   "one_line": "ISSUER'S DISARM OF LGIC_CANON-S11 on its branch (b): 1.0.0_SA_CTO RULING R-10 carried CN-k-4 out of round 2 by WITHDRAWAL, and round 2 now reads 9 of 10 orders terminal by the gate's own reader, the tenth being CN-o-4 which is running.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "S11 set two disarm branches: (a) A-3's adjacency test at HEAD and CN-k-4 spawned against it, or (b) 1.0.0_SA_CTO rules CN-k-4 carried OUT of round 2. Branch (b) is taken: RULING R-10 @41026094e7, 'take (a), and not weakly', by withdrawal rather than deferral.",
     "THE FLIP LANDED at cc6ed04bab: CN-k-4's <status> reads `withdrawn` with a note citing S11 and R-10 and stating the obligation VERBATIM -- re-render the canon's generated section after NAMING_SCHEMA.json carries the bd adjacency test, K4-AC1 as cut -- carried into round 3 behind LGIC_NAMING round 5's schema cell.",
     "MECHANISM CHECKED BY CALLING THE GATE RATHER THAN READING IT: imported surprise-row-gate.py and ran its own TO_STATUS_RE against the edited file. It captures 'withdrawn', and 'withdrawn' is in its own TERMINAL_TO_WORDS tuple. The pattern is ANCHORED AT LINE START (a 2026-09-10 fix after a bare .search() matched a prose mention), so the tag had to open its line; it does.",
     "ROUND-2 TERMINALITY, measured with the same imported reader over the round's own denominator: 10 orders, 9 TERMINAL (8 by the word `complete`, 1 by the word `withdrawn`), 1 OPEN -- CN-o-4, which is running now. So round 2 slugs on its nine cells the moment CN-o-4 drains, exactly as R-10 provides.",
     "THE FILE EDIT WAS CHECKED FOR COLLATERAL: 0 CRLF (the file is pure LF and stayed so), the 6 non-ASCII characters unchanged, and both <criterion> elements untouched -- a status flip must not move a criterion."
    ]
   },
   "disposition": "DISMISSED_WITH_REASON",
   "dismissal_reason": "S11's branch (b) is taken by a ruling from the seat that owns the call, the flip is committed at cc6ed04bab, and the gate's own reader confirms the resulting round-2 tally is 9 of 10 terminal with only the running CN-o-4 open. Nothing further is owed by this seat on S11. INERT.",
   "spec_asserts": "S11: round 2 cannot reach 'every order terminal' while CN-k-4 waits on an artifact another project produces in a round not yet cut.",
   "world_is": "True as filed, and resolved by withdrawal rather than by waiting: the cell is terminal by a word the gate admits, its obligation is carried into round 3 in full text rather than by reference, and round 2's closure no longer depends on LGIC_NAMING.",
   "notes": "INERT. \u26d4 THIS DISARMS S11 AND DISCHARGES NOTHING. The obligation CN-k-4 carried is UNMET, not met: the canon and NAMING_SCHEMA.json may disagree at HEAD until round 3's re-render lands, round 2 ships with that disagreement open, and R-10 is explicit that withdrawal does not weaken the cell. A reader who sees a terminal word here and stops has read this row backwards. The chain, one owner per link: 3.0.0_SA_CVO's LGIC_NAMING round-4 slug -> 1.0.0_SA_CTO's round-4 analysis -> 2.0.0_SA_COO~G's LGIC_NAMING round 5 -> the schema carries the test -> LGIC_CANON round 3's re-render cell."
  },
  {
   "id": "LGIC_CANON-S13",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T10:40Z",
   "one_line": "FOR 3.0.0_SA_CVO AT L8/L9, so nobody assumes the other did it: MY 'ISSUER'S DISARM' ROWS DISPOSE NOTHING. They set hazard_standing on a NEW row and leave the original UNDISPOSITIONED. Measured with the gate's own resolver: 34 of 41 LGIC_CANON items and 59 of 91 LGIC_ENFORCE items read undispositioned right now.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "MEASURED BY CALLING THE GATE'S OWN FUNCTION, not by reading it: imported surprise-row-gate.py and ran _resolve_latest over every channel document of each project. LGIC_CANON: 41 items, 34 UNDISPOSITIONED. LGIC_ENFORCE: 91 items, 59 UNDISPOSITIONED. Among the still-open ones are LGIC_CANON-S3, S7 and S11 -- the three this seat filed 'issuer's disarm' rows for THIS SESSION (S10, S8 and S12 respectively).",
     "WHY THEY DO NOT DISPOSE, from the gate's own rule at :149: 'an item is dispositioned by a NEW row that names it (the disposition is the item's); else the item's own row. UNDER_INVESTIGATION, or an item no row carries, is not dispositioned.' The NAMING is a structured `adjudicates` field carrying target ids -- _resolve_latest reads `r.get(\"adjudicates\")` -- and PROSE naming an id in one_line or notes is not read at all.",
     "MY DISARM ROWS CARRY NO `adjudicates` FIELD. They say 'ISSUER'S DISARM OF LGIC_CANON-S7' in prose and set hazard_standing INERT on themselves, while the original row's own disposition still reads UNDER_INVESTIGATION. This is exactly the failure this estate already names: an adjudication that disarms in prose disposes nothing.",
     "AND THAT IS THE CORRECT DIVISION OF LABOUR, not a defect to fix by adding the field: a census of who actually carries `adjudicates` shows it is the CVO's instrument. LGIC_CANON: 8 carrying rows, ALL in ADJUDICATION_v1.md, ALL by 3.0.0_SA_CVO. LGIC_ENFORCE: 14 in ADJUDICATION_v1.md, all by 3.0.0_SA_CVO, plus exactly ONE in INVESTIGATION_v1.md -- W3-S11 by 0.9.0_WK_LGIC_ENFORCE~3, disposing its OWN earlier row W3-S10 as GRADUATED. So a seat may dispose its own row; an issuer does not dispose the round's items.",
     "SO THE TWO THINGS ARE DIFFERENT ACTS AND BOTH ARE NEEDED: hazard_standing answers 'is the HAZARD still live' and is the disarm_owner's; disposition answers 'has this item been ADJUDICATED' and is the CVO's at L9. My rows do the first and supply the evidence for the second. Neither substitutes for the other, and the L10 precondition counts only the second."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "The L10 precondition: the route-carrying row is refused while any investigation item of the project is not dispositioned.",
   "world_is": "93 items across the two projects are undispositioned as this round closes, and that is the expected pre-L9 state rather than a backlog anyone is late on -- but it means the slug cannot close on my disarm rows, and no amount of issuer-side disarming changes the count.",
   "notes": "INERT: nothing here is a hazard, it is a hand-off statement. \u26d4 THE POINT IS TO STOP A SYMMETRICAL MISTAKE: I must not read my own disarm rows as closing anything, and 3.0.0_SA_CVO must not read them as an issuer having already disposed items. THE ONE THING I WOULD HAVE GOT WRONG: I nearly 'fixed' this by adding `adjudicates` to my own rows, which would have had the graded party disposing the round's items -- a boundary read from a field the graded party writes is no boundary. The census of who carries the field is what stopped me. Filed on LGIC_CANON because its round-2 slug is imminent; the identical statement holds for LGIC_ENFORCE and its numbers are printed above."
  },
  {
   "id": "LGIC_CANON-W9-S1",
   "project": "LGIC_CANON",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_CANON~9",
   "surfaced_at": "2026-09-16T10:12Z",
   "one_line": "The canon's own header is stale against its body: infra/logic/02_DOCTRINE.md's title line still reads v1.0 and section 0's census line still reads 'RULES CARRYING ALL THREE PARTS: 21 of 21', while the file carries 22 rule blocks (R22, inserted between R13 and R14) and its change log's last row reads v1.1. R22 itself carries all three parts, so the shortfall is in the count and the version stamp, not in the rule.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "COUNT: infra/logic/02_DOCTRINE.md@d173e700f7 (blob last touched @4ee952a3e4; unmodified in worktree wk-lgic-canon-2-10, `git status --porcelain` empty on the path). `re.findall(r'^\\*\\*(R\\d+)\b', text, re.M)` returns 22 ids in file order: R1..R13, R22, R14..R21. The same expression is the one section 0 names for its own recount ('a line opening **R<n> to the next rule, heading or rule line').",
     "HEADER: the same file's line 1 reads '# 02 -- THE PLATFORM LOGIC CANON (the doctrine) -- v1.0' and section 0 carries the single line 'RULES CARRYING ALL THREE PARTS: 21 of 21'. The change log's last row reads '| v1.1 | 2026-09-16 | round 2 (0.9.0_WK_LGIC_CANON~1, cell CN-k-2) ...', so the version is stamped in the log and not in the title.",
     "RULE IS COMPLETE: R22 at :459-468 carries plane (compute), authority (LGIC_CANON_ROUND1_ANALYSIS.md ruling A-9, W7-S3), census (n/a, a definitional rule) and non-application (the FIRST pipeline of a new vendor) -- so 22 of 22 would be the true reading of that line, not 21 of 22."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "02_DOCTRINE.md section 0 states its rule count as a recounted census line ('RULES CARRYING ALL THREE PARTS: 21 of 21') and the document stamps its version in its title line; the canon is the one document a seat answers conformance from without opening a second.",
   "world_is": "The body carries 22 rules and the change log carries v1.1, while both header carriers still read the v1.0 values. A reader who takes the census line at face value reads a canon of 21 rules and can conclude R22 is not canon text -- which is exactly the rule four onboarding-checklist steps (3, 7, 8, 9) now rest on.",
   "notes": "Off-task for CN-o-4: found while grounding R22 for the checklist review, and it belongs to CN-k-2's artifact, which is not in this order's <paths>. Not touched. No mark in CHECKLIST_REVIEW_R2.md depends on the count -- R22's own text was read in full at :459-468. INERT: nothing reads the census line mechanically (render_naming_section.py --check stamps the GENERATED section, not this line)."
  }
]
```
