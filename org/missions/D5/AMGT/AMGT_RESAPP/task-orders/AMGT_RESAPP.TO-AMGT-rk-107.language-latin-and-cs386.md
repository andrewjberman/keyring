# AMGT_RESAPP task order -- `AMGT-rk-107` -- L-0a: `document.detect_language` tells Latin-alphabet languages apart from English (Z-S221), plus the C-S386 one-liner in `_first_differing_outcome_field`; CODE ONLY, ahead of any Lenovo filing analysis

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-107</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~107</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- edits two library modules and adds two test files; arms no cron, alarm,
  monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; no AWS call at all.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~107`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. Your first act
prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel` and tests that `org/`, `.tools/` and the
existing paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~107;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out branch
`wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-107` (round 28, the Lenovo trial's wave 0)

**The governing text, verbatim.**
- PRD v0.22 s.12 (`prd/AMGT_RESAPP_PRD.md` @`d0597e7e0a`), Preconditions: *"**Language (Z-S221).** No filing is analysed
  until the detector distinguishes Latin-alphabet languages. This is the CVO's ordering ruling, `ADJUDICATION_v30`
  @`921cc430c1`."*
- Row `AMGT_RESAPP-Z-S221`, `one_line`: *"detect_language returns 'en' whenever ASCII letters are over half of all letters,
  so German, French, Italian and every Latin-alphabet language read as English and are never translated, with no
  warning; the API also drops text_translated from every drafted sentence."*
- CTO round-27 analysis (msg 24239, `ledger/ROUND_ANALYSIS.round27.md` @`0a57690e2e`): *"C-S386, graduated. The
  CHANGED-HELD message's length branch reports flattened outcome-field counts, not attempts. The refusal is correct and
  the operator text is wrong. It rides 2.0.0_SA_COO~Z's NEXT code cell as a one-line fix."*

**THE MEASURED STATE at SITEZ `96cc4dae9d` (re-read every line at your branch HEAD before editing):**
- `lib/research/filings/document.py:330-365` `detect_language(text)`: letter shares (kana, CJK, hangul, ascii). It
  returns `ja` / `zh` / `ko`, then `"en"` when `ascii_share > 0.5`, else `"unknown"`. It returns a dict with `language`
  and four shares.
- Callers (Grep, non-test, 4): `analyze.py:1327`, `document.py:866`, `battery.py:412`, `fetch.py:417`. Each reads
  `["language"]`. Tests: `lib/research/filings/tests/test_document.py:155` and `:162`.
- `lib/research/harvest/filings.py:297-312` `_first_differing_outcome_field`. Its length branch (`:311`) prints
  `len(old_fields)` / `len(new_fields)`, the FLATTENED `(label, value)` pair counts, labelled "battery.attempts length".
- Suites at the cut: `lib/research/filings/tests` **100 passed**; `lib/research/harvest/tests` **79 passed**;
  `test_document.py` **9 passed**.

**RULED, what you build:**
1. `document.detect_language`: when the ascii-letter share would today return `"en"`, apply a STOPWORD test over the
   lower-cased word tokens of the sample:
   - A fixed, small, ASCII-only stopword set per language: `en`, `de`, `fr`, `it`, `es`, `nl`, `pt`, `sv`, `da`, each
     about 15-25 of its most frequent function words, stated as a module constant.
   - The language with the most stopword hits wins. It returns `"en"` ONLY when English wins, or when no language
     reaches the minimum hit count (a named constant). Otherwise it returns that language's code.
   - The dict gains `"stopword_hits"`: `{lang: count}` for every language scored, so a wrong call is visible.
   - Non-ASCII Latin letters (e.g. a-umlaut, e-acute) still count as letters and never move the `ja`/`zh`/`ko` branches.
   - A language outside the table falls through to `"en"` only by the minimum-hit rule. Say so in the docstring as a known
     limit.
2. `harvest/filings.py` `_first_differing_outcome_field`, the length branch ONLY: report the ATTEMPTS counts,
   `len((existing.get("battery") or {}).get("attempts") or [])` against the same for `new`, labelled
   `battery.attempts length: <old> -> <new>`. Nothing else in the function changes.
3. New test `lib/research/filings/tests/test_language_latin.py`, with arms:
   - `test_german_text_is_de`, `test_french_text_is_fr`, `test_italian_text_is_it`: fixtures of about 60 words each,
     written in ASCII-transliterated form plus one accented word each;
   - `test_english_text_still_en`;
   - `test_japanese_text_unchanged_ja`: a kana fixture;
   - `test_stopword_hits_reported`.
4. New test `lib/research/harvest/tests/test_changed_held_length_text.py` with ONE arm,
   `test_length_branch_reports_attempt_counts`: 2 attempts against 3 attempts, with an equal common prefix, gives the
   text `battery.attempts length: 2 -> 3`.

**What this cell does NOT change:** the four callers; `analyze.py`; any translation code; the API's `text_translated`
drop (gap G-6, recorded for the trial report); `store.py`. No S3 read or write, no model call, no deploy.

## 2. WHERE THIS CAME FROM

**ROUND 28**, decomposition s.36 (cut by `2.0.0_SA_COO~Z`): the Lenovo trial's wave 0 (PRD v0.22 s.12, ADMITTED; CTO
msgs 24257 and 24261). Andrew-direct ~15:12Z governs one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/document.py
lib/research/harvest/filings.py
lib/research/filings/tests/test_language_latin.py
lib/research/harvest/tests/test_changed_held_length_text.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~107/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-107.language-latin-and-cs386.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (every existing test file included). Reads need no grant. Scratch is
  `<your worktree>/.scratch/r107/`, never committed.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~107 <0.9.0_WK_AMGT_RESAPP~107@opal.agent>" -F <msgfile> -- <paths>`,
  with the message file written by the Write tool. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

- **CODE ONLY.** No AWS, vendor or model call.
- **Imports in tests use the QUALIFIED `lib.<pkg>.<mod>` names** (W85-S1). **Run each test directory in its OWN pytest call.**
- **A script that carries a backslash is a FILE** (W84-S1).
- **Every comparison is pinned to `96cc4dae9d`.**
- **Non-ASCII in production code: 0.** Fixtures in the test file may carry accented letters; record their count in AC4.
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row, never
  repaired or widened.
- **COUNT BARS ARE READ AT SPAWN (AC0).**
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W107-S<k>`, with `"project": "AMGT_RESAPP"` and `"fabric": "site-z"`, spliced into the one
  fenced JSON array; `disarm_owner` is `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; each runs under timeout 600)

`.scratch/r107/ac4.py`:
```
import subprocess
out = subprocess.run(["git", "diff", "--name-only", "96cc4dae9d", "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
for f in sorted(out):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for ch in b.decode("utf-8") if ord(ch) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-107"><invocation>cd "$(git rev-parse --show-toplevel)" && sed -n '330,365p' lib/research/filings/document.py && sed -n '297,312p' lib/research/harvest/filings.py && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit: the detector body with its `ascii_share > 0.5` "en" branch, and the length branch printing len(old_fields)/len(new_fields); then F0 (100) and H0 (79). Record both counts; they are the baselines</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-107"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests/test_language_latin.py -v -p no:cacheprovider 2>&1 | tail -9</invocation><expect>"6 passed" and 0 failed, with the six named arms PASSED -- de, fr and it are detected, English stays en, Japanese stays ja, and stopword_hits is reported</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-107"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_changed_held_length_text.py -v -p no:cacheprovider 2>&1 | tail -3</invocation><expect>"1 passed", test_length_branch_reports_attempt_counts PASSED (the text reads "battery.attempts length: 2 -> 3")</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-107"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>filings "N passed" with N = F0 + 6, and harvest "M passed" with M = H0 + 1; 0 failed in both. Every existing detector arm (test_document.py) still passes inside F0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-107"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r107/ac4.py</invocation><expect>"changed_code_files" lists EXACTLY the four paths in section 3's code lines; each "compiles True crlf 0"; non_ascii_chars 0 for document.py and harvest/filings.py (production), and the recorded count for the new test fixtures</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~107/AMGT_RESAPP.TO-AMGT-rk-107.language-latin-and-cs386.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, and grade it with YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4` (rc 0 is the verdict). Flip the order's status on the
record face to `complete` only if every criterion passes, commit with `--only -- <paths>`, and report once.

**MUTATION DISCIPLINE:** snapshot working-tree bytes to `.scratch/r107/` before editing. Never `git checkout --`, `git stash`
or `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5):**
1. The stopword test is the MINIMUM that meets the ruling. No new dependency: no langdetect, and no install. A language
   outside the table can still fall to "en", which is a stated limit.
2. Lenovo's annual report is expected to be English, so this cell guards the ORDERING (no analysis before the fix), not a
   known Lenovo defect.
3. No new security_key dependency (Andrew-direct @`5c20841dd1`).

<status>complete</status>
<round>28</round>
<slot>~107</slot>
<fabric>site-z</fabric>
