# AMGT_CORPUS task order -- `CRPS-d-3` -- ROUND 2: the composed per-security DOSSIER in gold `research-dossier` -- every field cited or ABSENT with a reason, `as_of` in the object name, a rebuild on unchanged inputs writes nothing, one reader by security key, and the side-by-side interface sheet for the page

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-d-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 (round-1 read, 214 roles on the DESIRED plane, not re-run this cut); BLIND to this box's credential; this cell's first put to the NEW research-dossier prefix measures it.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continued from `CRPS-d-2`. Work ONLY in your worktree.
- **First act:** print `git rev-parse --abbrev-ref HEAD`, and test that `continuation.py` exposes `thesis_summary` in its
  fields and that `extract.py` defines `METHOD_VERSION_2`. If either is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE LIBRARY.** Every input is a stored object.

## 1. THE CELL, inlined in full -- `CRPS-d-3` (manifest row R12, NEW; serves FWD-10, FWD-11, FWD-12, FWD-13, FWD-15 and FWD-17's store half)

**FWD-13, verbatim:** *"Every folded field is CITED or ABSENT with a readable reason. DONE WHEN EXERCISED -- a census over
the dossier's fields prints zero fields that are neither cited nor reason-bearing, with the denominator of fields scanned;
and a negative control shows a deliberately uncitable field rendering ABSENT rather than blank or inferred."*
**FWD-17 (store half), verbatim:** *"... the dossier's inputs_sha16 changes ... and the prior as_of object still reads; and
a rebuild with UNCHANGED inputs writes NOTHING and says so."*

**THE CONTRACTS, verbatim (PRD v0.6 CONTRACTS -- A.5):**
- **`C-DOSSIER-IS-COMPOSED-NEVER-AUTHORED`.** *"The dossier is a COMPOSITION of artifacts that already exist -- the
  continuation artifact, the sector template, the fund form, the typecast, the bronze extraction -- plus the cited
  passages. No cell authors a new judgment into it and no field is synthesised across reports."*
- **`C-DOSSIER-DATE-IN-THE-OBJECT-NAME`.** *"`as_of` lives in the OBJECT NAME, `<YYYY-MM-DD>.<inputs_sha16>.json`, one
  object per rebuild whose inputs changed, never overwritten, reader takes the newest `as_of`."* The builder REFUSES a
  two-level partition; the partition is `security_key=<KEY>` only.
- **`C-DOSSIER-TABLE-SPELLING`.** *"THE SPELLING IS `research-dossier`."* (hyphen; the builder accepts both spellings and
  refuses neither, so the spelling is a rule you keep, not one the builder keeps for you).
- **`C-DOSSIER-REBUILD-IS-A-NO-OP-ON-UNCHANGED-INPUTS`.** *"A rebuild whose `inputs_sha16` is unchanged writes nothing and
  says so."*
- **`C-CITED-OR-ABSENT`**, **`C-INPUT-HASHED`**, **`C-NO-RAW-BRONZE-AT-SERVE`** (only the gold dossier of cited passages is
  servable; no report bytes and no whole extraction travel in it), **`C-EXEC-MANAGEMENT`** (the filing roster stays the
  authority on the page; the dossier's `management` is the team's cited passage BESIDE it, never a replacement).

**RULED -- what you build, new module `lib/research/corpus/dossier.py`:**
- `TABLE = "research-dossier"`, `METHOD_VERSION = "amgt-corpus-dossier/1"`. `build(security_key, client)` composes ONE
  document: `{artifact, method_version, subject{security_key}, as_of, inputs[{key, sha256}], fields{...}, content_sha256}`.
- **`fields`, each `{value, citation}` or `{value: null, absent: <reason a person can read>}`:**
  from the continuation artifact (read via `continuation.read_latest`): `thesis_pillars`, `thesis_summary`, `kpi_set`,
  `fund_of_record`, `last_stated_position` (carry their citations through);
  from the sector template / fund form / typecast (read via `substrate`'s members): `sector_template_ref`, `fund_form_ref`,
  `typecast_ref` as `{uri, content_sha256}` members (references, not copies), plus `model_rows` -- the typecast's shared
  mnemonic core and the sector template's KPI set for this name's business type, as an ORDERED list of `{mnemonic|label,
  source}` with NO figures (FWD-12: the 22 added mnemonics' FIGURES wait on Andrew's separate word; every row reads
  `figure: {value: null, absent: "Bloomberg figure pull not authorized (R-16 V3)"}` -- which is FWD-13 working);
  from the v2 EXTRACTION of the most recent class A pack AND the most recent class B update (through `typed.reports_for`
  and the v2 object beside each row's `extract_key`; v1 when no v2 exists): the SECTIONS `recommendation` (the line after
  the RECOMMENDATION lead, <= 160 chars), `company_description`, `growth_algorithm`, `investment_thesis_summary`, `risks`
  (the RISKS block; `pre_mortem` as a sub-field where a `Pre-mortem:` lead opens it), `ownership`, `management` (the
  MANAGEMENT / BOARD or MANAGEMENT AND CAPITAL ALLOCATION block), `special_items`, `cases` ({upside, base, downside} blocks),
  `why_we_own`, `positives`, `negatives`, `comparison_set` (the COMMON STOCK COMPARISON block as text, a cited FIELD, never
  a ranker). A section is the lines from its lead to the next section lead; its citation is `{report_key, report_id,
  locator: page index or paragraph index, passage: first 300 chars}`; a section the two reports do not carry is ABSENT
  with the reason naming which report classes were read (`no MANAGEMENT section in class A 2026-07-17 or class B
  2026-09-10`). Nothing is paraphrased, merged across reports or defaulted.
- **Address and name from the builder, printed, never typed:** the partition `security_key=<KEY>` through
  `lib.opal_naming.address(...)` exactly as `gold.address_of` does for the other research tables; the object name
  `as_of=<YYYY-MM-DD>.<inputs_sha16>.json` where `as_of` is the UTC date of the build and `inputs_sha16` is the same
  canonical hash rule `continuation._inputs_sha16` uses. Through `gold.gold_put` (never overwriting).
- **`write_one(security_key)`:** FIRST reads the newest stored object for the key; if its `inputs` equal the fresh
  `current_inputs`, it writes NOTHING and prints `unchanged inputs_sha16 <x> wrote 0`; else it puts the new object and
  prints `address <uri> put_performed 1 existed 0 inputs_sha16 <x>`. **`--write --security-key <KEY>`** runs `write_one`
  TWICE in one invocation and prints both outcomes (the second MUST be the no-op) -- the difference control is inside the
  criterion. **`--write`** (no key) rebuilds every resolved name as a BUILD STEP, totals first and last.
- **`read_dossier(security_key, client)`:** the newest `as_of` object for the key (lexicographic on the object name; a
  newer as_of wins, then a later hash on the same day is a rebuild the same day and both stay readable), returned with
  `{uri, content_sha256}`; `LookupError` with the folder-shaped reason when none exists.
- **`--census`:** over EVERY stored dossier: `dossiers D fields_scanned N cited C absent_with_reason A neither 0` (N = C + A),
  printed first and last, and the NEGATIVE CONTROL: compose one document with a planted section name no report carries
  (`PLANTED-UNCITABLE-SECTION`) and print `negative_control absent_with_reason 1` -- the planted field must land as ABSENT
  with a reason, never as a blank or an inferred value. The planted document is NOT written to the store.
- **`DOSSIER_INTERFACE.md`** in your deliverables dir: the dossier's field list SIDE BY SIDE, field name against
  `ThesisBundle`'s slot (`portal/src/pages/SecurityAnalysis/types.ts:955` -- `drafted_sections` ids `company_description`,
  `investment_thesis`, `risks`, `ceo_bio`, `recommendation` with `generated: true|false` per sentence; `management`;
  `model_cases`; `model_status`/`fiscal_year_figures`; `posture`), naming the INTERSECTION and, for each dossier field with
  no slot, the words "no slot today". One accepted and one refused example payload (a served name; a name with no dossier)
  printed as JSON. This sheet is what `AMGT_RESAPP`'s round cuts the adapter against; it is a document, not code.

**What this cell does NOT do:** no portal or `scoped_amgt.py` edit (another lane's surface); no new extraction rule; no
Bloomberg call; no synthesis of any field; no second partition key.

## 2. WHERE THIS CAME FROM
Round 2, decomposition v2.0, chain A, cell 3 of 4 on this slot, after `CRPS-d-1` and `CRPS-d-2` drained VALID. `CRPS-d-4`
reads what this cell writes.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/DOSSIER_INTERFACE.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-d-3.composed-dossier.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` module, `lib/research/harvest/store.py`, `lib/opal_naming.py`,
`portal/src/pages/SecurityAnalysis/types.ts`. Scratch in `.scratch/d3/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **NO S3 DELETE OF ANY KIND**; a superseded dossier is a new object beside the old one (that IS FWD-17).
- **Pure ASCII source, LF, Python 3.9-compatible.** `ensure_ascii=True` on every stored document.
- **S3:** writes ONLY through `gold_put`, never overwriting, ONLY at the builder's address, table spelled
  `research-dossier`. **Run `--write` as a BUILD STEP.**
- **Tests:** offline under the poison, every input seeded through the package's own writers into
  `substrate.StubS3Client`: a composed document with every section present; one with a missing section reading ABSENT
  with its reason; the no-op rebuild; the newest-as_of reader with two objects on one key; the census arithmetic; the
  planted negative control.
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as
  written**, and report it with your measurement.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 600`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-d-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_dossier.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-d-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.dossier --write --security-key IMB_LN_Equity 2>&1 | tail -8</invocation><expect>(?s)address s3://opal-data-harvest/amgt/harvest/gold/research-dossier/security_key=IMB_LN_Equity/as_of=\d{4}-\d{2}-\d{2}\.[0-9a-f]{16}\.json put_performed [01] existed [01] inputs_sha16 ([0-9a-f]{16}).*unchanged inputs_sha16 \1 wrote 0</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-d-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.dossier --census 2>&1 | tail -4</invocation><expect>(?s)dossiers [1-9]\d* fields_scanned [1-9]\d* cited \d+ absent_with_reason \d+ neither 0\b.*negative_control absent_with_reason 1\b</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-d-3" judgment="true"/>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe against the real store for the already-resolved IMB_LN_Equity, with the
  no-op rebuild as the difference control inside it; AC3 FWD-13's own census with its negative control.
- **AC4 (JUDGMENT, the CVO's):** `DOSSIER_INTERFACE.md`. Does the side-by-side name a true intersection with `ThesisBundle`,
  and does every field with no slot say so rather than being mapped by force? Record the sheet's path and the two example
  payloads, with NO verdict.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-d-3.composed-dossier.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes. Commit via safe-commit with the pathspec of
   exactly the files you changed plus the instance.
4. Report ONCE: the AC2 two-outcome lines, the census line, and the `--write` totals (names N written W existed E).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the sections come from the two most recent reports (class A pack, class B update) by L5 ruling 2, never
synthesised across the corpus. The interface sheet is the artifact `AMGT_RESAPP`'s round cuts its adapter against; the
issuer delivers it to `2.0.0_SA_COO~Z` at the drain as an interface publication.

<status>complete</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
