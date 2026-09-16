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
  }
]
```
