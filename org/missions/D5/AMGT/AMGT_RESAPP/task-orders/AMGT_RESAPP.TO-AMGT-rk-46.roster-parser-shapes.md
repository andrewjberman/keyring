# AMGT_RESAPP task order -- `AMGT-rk-46` -- the roster parser: a title is never a name; the "Name (age) Role (year)" table; original-script names kept; the age-in-role mis-split; the HAL / INTU / KMB section shapes

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-46</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~48</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the DISABLED task
  OpalResearch-ExecManagement is neither read nor written (AMGT-rk-44's); the standing collection-stays-off /
  no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order READS the pool (filings/v1/ source objects for five keyed names) under
  the existing credentials, writes NO pool object, grants no permission and provisions no resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~48`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and `lib/research/management/`
exist; if any is absent, STOP with a BLOCKING row. Your second act tests that the validation's scratch folder exists --
`C:\Users\OPALBL~1\AppData\Local\Temp\claude\C--Users-Opal-Bloomberg-Desktop-ajb-workspace\d60f6524-dc92-4e15-937e-45e7685911cb\scratchpad\instantiation_validation\`
with `sources/CAT_US_Equity.source.json`, `sources/CSL_AU_Equity.source.json`, `sources/6861_JP_Equity.source.json`
and `docs/cat-20251231.htm` (present on this device 2026-09-18 ~20:xxZ when this order was drafted); **if it is gone,
STOP with a BLOCKING row naming the four files -- do NOT fetch them yourself** (a re-download is egress the COO
decides). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~48;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-46` (R14-E4; FWD-17; validation V5 = D20, D21, D22; intake rows E2, E3)

**The analysis row, verbatim** (`ROUND_ANALYSIS.round13.md` s.4 @`9c8e04cd9a`): *"the roster parser: a title is never a
name (D20); the "Name (age) Role (year)" table (D21); original-script names kept (D22); the age-in-role mis-split; the
HAL / INTU / KMB section shapes"* -- serves FWD-17, V5, E2, E3; co-sign: pool writes.

**THE MEASURED STATE (read at HEAD `4f44431d34`; the pool read 2026-09-18 ~20:xxZ by the drafting seat -- RE-MEASURE AT
SPAWN with AC2).** `lib/research/management/roster.py` declares THREE shapes (`:17-26`): narrative-entry, table-age,
table-year; a section none reads is UNRESOLVED-SOURCE with the reason *"no declared shape read this section"*
(`:461-465`). Against that:
- **D20 -- a title is accepted as a name.** `_NAME_TOKEN` (`:97-98`) is any capitalised word, and `_NAME_ROLE_RE`
  (`:118-119`) takes the shortest capitalised run before a `_ROLE_LEAD` word as the name. On VLO's persisted 10-K (in the
  pool today, `filings/v1/VLO_US_Equity/000162828026011499.source.json`, a "Name / Current Position / Age" table whose
  second row WRAPS the name across two lines -- `Harminder S.` / `"Homer" Bhullar` / `Senior Vice President and Chief
  Financial Officer 45`) the served object `management/v1/VLO_US_Equity/2026-09-18.json` carries an officer NAMED
  **`Senior Vice`** with role `President and Chief Financial Officer 45`. The validation measured the same class on CSL:
  RESOLVED with 6 "officers" called "Executive Vice" / "Senior Vice", the real CFO and interim CEO missed (report D20,
  `:219-220`). PRD v0.13 @`1699960261` `C-EXEC-MANAGEMENT` (`:733-734`): *"A roster row must be a PERSON. A title alone
  ("Executive Vice", "Senior Vice") is never accepted as a name. A roster whose rows all fail this test is not
  RESOLVED."*
- **The age-in-role mis-split.** VLO's rows end in a bare two-digit age with NO year before it, so `_SINCE_COLUMN_RE`
  (`:121`, which needs `<year> <age>$`) does not fire and the age stays inside the role: served roles read *"Chairman
  of the Board, Chief Executive Officer and President 60"*, *"... Chief Operating Officer 61"*, *"... General Counsel
  60"*, *"... Trading and Wholesale 57"* (all five VLO officers; `age` null on each). Intake E3.
- **D21 -- CAT's "Name (age) Role (year)" table reads 0 candidates** even on the correct section (report D21
  `:221-222`; the validation's `s07b` re-cut of "Information about our Executive Officers", 2,494 chars, 17 usable lines,
  0 candidates). No declared shape carries a parenthesised age or a parenthesised year.
- **D22 -- original-script names are erased.** `_usable_lines()` (`:193-201`) runs `asciify()` (`:157-171`) over the
  WHOLE section before any parse; `asciify` drops every character NFKD cannot reduce to ASCII (`:167-170`), so a Kanji
  name becomes an empty string and the officer vanishes. Keyence's Yuho officer table (`sources/6861_JP_Equity.source.json`,
  item `\u5f79\u54e1\u306e\u72b6\u6cc1` -- written here as its JSON escape, since this order is ASCII -- 3,190 chars,
  2,536 of them non-ASCII, 54 lines) reads UNRESOLVED; the validation's scratch parse found 12 of 12 declared officers
  (report D22 `:223-224`). The pool object's BYTES stay ASCII whatever the name holds: `crosswalk.serialise()` writes
  `ensure_ascii=True` (`crosswalk.py:439-441`), so a non-ASCII name lands as `\uXXXX` escapes -- the "no non-ASCII in
  AWS" rule is met by the serialiser, not by erasing the name.
- **HAL / INTU -- the section INCORPORATES BY REFERENCE.** HAL's persisted Item 10 (20 usable lines) says *"The
  information required for the directors and executive officers of the Registrant is included under Part I on pages 7
  and 8 of this annual report"*; INTU's (4 lines) says the information *"is incorporated by reference from the
  information contained in our Proxy Statement"*. Both read "no declared shape" today; the honest outcome names WHERE the
  filing says the roster lives, so the filings cutter (R14-F2, intake E10) can cut that place -- CAT's Item 10 has the
  same shape (report D10 `:196-197`: it cross-refers to Item 1D, 27,766 chars of cross-reference text).
- **KMB -- a narrative variant no regex reads.** KMB's section (194 usable lines, 0 candidates) is
  *"Ehab Abou-Oaf , 59, was elected President, International Family Care and Professional in 2024."* -- a name, a
  SPACE-COMMA, the age, then "was elected <role> in <year>" (or "has served as <role> since <date>"). `_HD_RE`
  (`:114-115`) needs the literal `, age NN,`; `_AGE_LEAD_RE` (`:116-117`) needs `NAME NN ROLE`; neither matches
  ` , 59, was elected`. At least ten officers sit in the first fourteen lines.
- **One placeholder hazard in the reader:** `load_source_object()` takes `sorted(keys)[-1]` (`:496`) as the LATEST
  accession; `UNRESOLVED-SOURCE.source.json` sorts after every digit-named accession, so a name carrying BOTH a real
  accession and a placeholder would have its roster built from the placeholder.

**RULED -- what this order builds (all in `lib/research/management/`: `roster.py`, `management.schema.json`,
`tests/`).**
1. **A title is never a name (D20).** A candidate name is REFUSED when every one of its tokens is title vocabulary
   (`_ROLE_LEAD` words plus Officer, Board, Member, Interim, Group, Division, Operations, Company and their plurals) or
   when its last token is one; a name needs at least one token outside that vocabulary. A wrapped name -- a line that is
   ONLY name tokens (a quoted nickname allowed: `"Homer"`) followed by a line that is only name tokens -- is JOINED
   before the role line is read. A section whose every row fails the person test is UNRESOLVED-SOURCE with the reason
   *"every candidate row is a title, not a person"* (so the fallback, R14-E5, applies to it).
2. **The age is a column, never part of a role.** A role line ending in a bare two-digit number 20-99 with no year
   before it yields `age` = that number and a role WITHOUT it (the table-name-position-age shape: `NAME ROLE AGE` on one
   line, or a wrapped name then `ROLE AGE`), declared as `parse_strategy: "table-name-position-age"`.
3. **The "Name (age) Role (year)" table (D21)**, `parse_strategy: "table-paren"`: `NAME (NN) ROLE (YYYY)`, `age` = NN,
   `role_start` = YYYY with `role_start_basis: filing-since-column` (the filing's own "present position held since"
   column); measured from the CAT fixture below, never guessed from this description.
4. **KMB's narrative variant**, read by the existing narrative-entry strategy through one more entry regex:
   `NAME\s*,\s*(NN),\s+(was elected|has served as|has been|is|serves as)\s+ROLE\s+(in|since)\s+DATE` -- `role_start`
   from the `in/since DATE` clause with `filing-since-clause`; a row stating two roles with two dates keeps the FIRST
   role and its date and records the sentence as the role's own words (the schema's `role` is *"the filing's own words
   for the role"*, `management.schema.json:109`).
5. **Incorporated by reference (HAL, INTU, CAT's Item 10).** When no candidate is read AND the section carries
   `incorporated by reference` / `included under Part I` / `included in Part I` / `Item 1D` / `Executive Officers of the
   Registrant` as a pointer, the roster is UNRESOLVED-SOURCE with `roster_reason` = *"the officer section INCORPORATES BY
   REFERENCE: <the pointer sentence, verbatim, ASCII-folded>"* and a new field `section_refers_to` = that sentence
   (string or null; `management.schema.json` admits it). `absence_reason_class` stays `enrich.py`'s (`:165-195`, not this
   order's file) and will read pull-missed for a RESOLVED filing, which is the true class: the document exists, the cut
   took the wrong item.
6. **Original-script names kept (D22).** `_usable_lines()` folds PUNCTUATION AND SPACING ONLY (the `_FOLD` table
   `:80-86` plus NFKC width normalisation) and keeps every other character; `asciify()` survives for `name_ascii` and for
   every log line. Each officer carries `name` = the filing's own characters and `name_ascii` = `asciify(name)` (may be
   empty -- an empty `name_ascii` is never used as the name). `text_normalization` on the document says so. Log lines
   print `name_ascii` or `<non-ascii name, N chars>`; no non-ASCII reaches a log. The Yuho officer table is a declared
   shape, `parse_strategy: "table-yuho"`: the validation's scratch parse read 12 of 12 (report `:278-279`) and its script
   sits in the scratch folder beside the sources -- port that read into `roster.py` as a shape (role, name, birth date
   per header line; career lines; a `(\u6ce8)` footnote closes the block), the count bar is 12 of 12 on the fixture.
7. **The reader's latest pick (`:496`)**: a placeholder key is chosen ONLY when no accession key exists.
8. **Fixtures beside the producer, under version control** (`C-PRODUCTION-HOME`, PRD v0.13 `:1643-1650`): reduce the
   three validation sources to the SMALLEST text that still carries each shape and commit them as pure-ASCII JSON
   (`json.dump(..., ensure_ascii=True)`) under `lib/research/management/tests/fixtures/` -- `cat_officers_paren.json` (the
   "Information about our Executive Officers" block of `docs/cat-20251231.htm`, the cut the validation's `s07b` script
   made), `csl_titles_as_names.json` (the CSL rows that produced "Executive Vice"/"Senior Vice"), `keyence_yuho_officers.json`
   (the 54-line officer table), plus `vlo_name_position_age.txt`-style rows and KMB rows reduced from the POOL objects
   (a read). The tests read ONLY the committed fixtures -- never the scratch folder, never a worker's folder.
9. **Schema (`management.schema.json`)**: `parse_strategy` enum (`:49-53`) gains `table-paren`, `table-name-position-age`,
   `table-yuho`; the officer gains `name_ascii` (string or null); the document gains `section_refers_to` (string or
   null); `text_normalization`'s description (`:55`) is re-stated. The closed-schema tests (`test_management.py:240-244`)
   keep passing.

**THIS ORDER WRITES NO POOL OBJECT.** The analysis marks the cell "pool writes"; every rebuild of a keyed name's roster
is a re-run of the covered population, which Andrew's word bars before the process is validated end to end
(`C-VALIDATION-NAMES`, PRD v0.13 `:1652-1655`). The proof is the fixture tests (planted negatives from the three
validation names) and DRY reads of the five keyed names' pool filings (`build_roster` in-process, AC2/AC4). The
rebuild of HAL/INTU/KMB/VLO's objects is the instantiation run's, after validation -- stated here so it does not close
by silence; if the COO widens this order to the three rebuilds, that widening is the COO's carded act, not this text's.

## 2. WHERE THIS CAME FROM

**ROUND 14**, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis @`9c8e04cd9a` s.4 row R14-E4 (chain E, independent); the
intake `CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md` s.2B rows E2 (`:161`), E3 (`:162`) and s.2E row V5 (`:323`);
the validation report `INSTANTIATION_VALIDATION_REPORT_20260918.md` @`b527b93214` D10 (`:196-197`), D20-D22
(`:219-224`), s.5 item 5 (`:276-279`); the CRO's brief `BRIEF_EXEC_MANAGEMENT_CURRENT_TO_DESIRED_20260918.md` s.1.1
(`:46-50`), s.4 item 6 (`:135-138`). **PRD v0.13 @`1699960261`**: `C-EXEC-MANAGEMENT` the filing as authority (`:723`),
the PERSON rule (`:733-734`), the zero-officer rule (`:731-732`); `C-PRODUCTION-HOME` (`:1643-1650`);
`C-VALIDATION-NAMES` (`:1652-1658`).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/roster.py
lib/research/management/management.schema.json
lib/research/management/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~48/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-46.roster-parser-shapes.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** `enrich.py` (rk-45's, and R14-E5/E6's) and `batch.py` (rk-44's) are
  READ ONLY here. A READ needs no grant: the pool's `filings/v1/<key>/` objects, the validation's scratch folder (read
  once, to REDUCE into committed fixtures), and `management/v1/VLO_US_Equity/2026-09-18.json`. Scratch is
  `<your worktree>/.scratch/` only.
- `tests/test_management.py` is ALSO appended by `AMGT-rk-44` (a census test) and `AMGT-rk-45` (pool tests) -- an
  append-only shared file inside one chain; add your classes at the END of the file and never reorder existing ones.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~48 <0.9.0_WK_AMGT_RESAPP~48@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer; every `.py` edit passes `.tools/commit-gate.sh`). Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** **No vendor call** -- none is named; `roster.py --dry-run` makes none (`:616-618`). **No pool
write** -- never `enrich.py --write-pool`, never a batch. **No fetch** -- the fixtures come from the scratch folder or
the pool, or the order STOPS. **No non-ASCII in anything you write**: fixtures are `ensure_ascii=True` JSON, test
source names characters by `\uXXXX` escapes or `chr(0x....)` (the pattern `roster.py:77-79` already uses), and
`roster.py` stays pure ASCII (`len(b) - len(b.decode("utf-8")) == 0`). **PUSH: never;** LD-0522 puts the push with
`0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the HAL 20 / INTU 4 / KMB 194
usable-line counts, VLO's five served rows and the "12 of 12" Keyence figure are this document's; AC2 re-measures the
pool ones at spawn, AC1 measures the fixture ones.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W48-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize
it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.** Two known off-task
facts you WILL meet: ASML and PBR carry an EMPTY Item 6 cut (a filings-stage defect, R14-F2's) and stay UNRESOLVED with
that reason -- they are AC2's unchanged controls, not yours to chase; and `enrich.name_matches()` folds through
`asciify` (`enrich.py:314-338`), so a non-Latin name can never match a Lusha row -- that is R14-E7's and a row, not a fix.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-46"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest lib.research.management.tests.test_management -v 2>&1 | tail -60</invocation><expect>every test passes ("OK" on the last line; "Ran N tests" with N >= 33 -- 25 at HEAD plus at least eight planted here, each named in the -v output): (1) D20 PLANTED on VLO's wrapped row -- Harminder S. / "Homer" Bhullar / Senior Vice President and Chief Financial Officer 45 -- yields name Harminder S. "Homer" Bhullar, role Senior Vice President and Chief Financial Officer, age 45, and NEVER a name "Senior Vice"; (2) D20 PLANTED on the CSL fixture -- no officer named "Executive Vice" or "Senior Vice", and a section of only such rows is UNRESOLVED with the "title, not a person" reason; (3) the age-in-role PLANT -- R. Lane Riggs Chairman of the Board, Chief Executive Officer and President 60 yields age 60 and a role that does not end in a digit; (4) D21 on the CAT fixture -- parse_strategy table-paren, N officers with age and a four-digit role_start each, basis filing-since-column, N printed against the fixture's row count; (5) KMB's variant -- Ehab Abou-Oaf, age 59, role_start 2024 (filing-since-clause) and at least one has-served-since row; (6) HAL and INTU fixtures -- UNRESOLVED-SOURCE, roster_reason begins "the officer section INCORPORATES BY REFERENCE", section_refers_to non-null and quoting the pointer sentence; (7) D22 on the Keyence fixture -- parse_strategy table-yuho, 12 of 12 declared officers, every name equal to the fixture's own characters (compared as Python str), name_ascii present, the serialised bytes pure ASCII via crosswalk.serialise; (8) the reader PLANT -- a _StubS3 carrying both filings/v1/X/000000000000000001.source.json and filings/v1/X/UNRESOLVED-SOURCE.source.json picks the accession, and one carrying only the placeholder picks the placeholder</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-46"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.management import roster
import json
for key in ('HAL_US_Equity', 'INTU_US_Equity', 'KMB_US_Equity', 'VLO_US_Equity', 'ASML_NA_Equity', 'PBR_US_Equity'):
    src, label = roster.load_source_object(key)
    doc, diag = roster.build_roster(src, '2026-09-18', label)
    offs = doc['officers']
    print(key, 'accession', doc.get('source_accession'), 'status', doc['roster_status'], 'strategy', doc.get('parse_strategy'), 'lines', diag.get('lines'), 'candidates', diag.get('candidates'), 'officers', len(offs), 'with_role_start', sum(1 for o in offs if o.get('role_start')), 'ages', [o.get('age') for o in offs][:6], 'refers_to', (doc.get('section_refers_to') or '')[:70], 'reason', (doc.get('roster_reason') or '')[:70])
    for o in offs[:6]:
        print('   |', o.get('name_ascii') or ('<non-ascii name, %d chars>' % len(o.get('name') or '')), '|', (o.get('role') or '')[:60], '|', o.get('role_start'), '|', o.get('age'))
print('DENOMINATOR names read 6 (3 round-13 zero-officer names + VLO + 2 empty-cut controls); DRY: nothing written')
"</invocation><expect>an in-process DRY read of six keyed names' persisted filings from the pool (a read, no write, no vendor call), re-measured at spawn: KMB reads RESOLVED with at least 10 officers, every one carrying an age and a role_start (0 officers today); HAL and INTU read UNRESOLVED-SOURCE with section_refers_to non-null and a reason beginning "the officer section INCORPORATES BY REFERENCE" (today "no declared shape read this section"); VLO reads RESOLVED with exactly 5 officers whose names are R. Lane Riggs, Harminder S. "Homer" Bhullar, Gary K. Simmons, Richard J. Walsh, Eric A. Fisher, ages 60/45/61/60/57, and no role ending in a digit (today: a "Senior Vice" officer and five roles ending in the age); ASML and PBR read UNRESOLVED-SOURCE with the EMPTY-officer-section reason, UNCHANGED (the controls this order must not move); denominator 6 printed</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-46"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io, json, glob
b = io.open('lib/research/management/roster.py', 'rb').read()
print('roster.py non-ascii bytes', len(b) - len(b.decode('utf-8')))
fx = sorted(glob.glob('lib/research/management/tests/fixtures/*.json'))
for f in fx:
    raw = io.open(f, 'rb').read()
    print(f, 'bytes', len(raw), 'non-ascii', len(raw) - len(raw.decode('utf-8')), 'escapes', raw.count(b'\\\\u'))
s = json.load(io.open('lib/research/management/management.schema.json', encoding='utf-8'))
print('parse_strategy enum', s['properties']['parse_strategy']['enum'])
print('officer has name_ascii', 'name_ascii' in s['definitions']['officer']['properties'], 'document has section_refers_to', 'section_refers_to' in s['properties'])
print('DENOMINATOR fixtures', len(fx))
"</invocation><expect>roster.py has 0 non-ASCII bytes; at least three committed fixtures exist under tests/fixtures/ (CAT, CSL, Keyence), EVERY one with 0 non-ASCII bytes, and the Keyence fixture carrying a nonzero count of \u escapes (the original script is present, escaped -- never erased); the schema's parse_strategy enum carries table-paren, table-name-position-age and table-yuho beside the three at HEAD; name_ascii and section_refers_to are admitted; the denominator of fixtures printed</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-46"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.management import roster, enrich
from lib.research.identity import crosswalk
import json, io, glob
fx = sorted(glob.glob('lib/research/management/tests/fixtures/*.json'))
n_ok = 0
for f in fx:
    obj = json.load(io.open(f, encoding='utf-8'))
    src = obj if 'officer_section' in obj else obj.get('source_object')
    doc, diag = roster.build_roster(src, '2026-09-18', 'fixture:' + f)
    doc.setdefault('security_key', src.get('security_key') or 'FIX_US_Equity')
    doc['ceo_public_profile'] = None
    ok, errors = enrich.validate(doc)
    payload = crosswalk.serialise(doc)
    print(f, 'status', doc['roster_status'], 'strategy', doc.get('parse_strategy'), 'officers', len(doc['officers']), 'schema_valid', ok, 'bytes_non_ascii', len(payload) - len(payload.decode('utf-8')), 'errors', errors[:2])
    n_ok += 1 if ok else 0
print('DENOMINATOR fixtures', len(fx), 'schema_valid', n_ok)
"</invocation><expect>every committed fixture, run through the real build_roster and validated against the CLOSED schema by enrich.validate, is schema-valid (schema_valid equals the fixture count) and serialises through crosswalk.serialise to bytes with 0 non-ASCII -- the Keyence document included, with its 12 officers' names intact in the object; the CSL fixture reads UNRESOLVED-SOURCE (titles only) or RESOLVED with real persons and NEVER a title-named officer; denominator printed</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC2 is run ONCE BEFORE any edit (the pre-act bar: 0 / 0 / 0 officers for HAL, INTU, KMB; the "Senior Vice" row on VLO)
and ONCE AFTER; both outputs recorded.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~48/AMGT_RESAPP.TO-AMGT-rk-46.roster-parser-shapes.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once, naming the before/after AC2 lines for HAL, INTU, KMB and VLO side by
side, and the fixture files committed with their byte counts.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never
`git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~48</slot>
<fabric>site-z</fabric>
