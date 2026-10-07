# AMGT_RESAPP task order -- `AMGT-ba-10` -- THE TRANSLATED TEXT BESIDE THE ORIGINAL ON A SERVED SENTENCE, WITH ITS FLAG AND SOURCE LANGUAGE (ROW Z-S221)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~276</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a pure projection and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no store read or write; the sentence is handed in.
comp-adversary: RUN by the issuer at the cut -- `text_translated` appears in lib/research/filings/translate.py and drafting_build.py:322-323 and in 0 files under lib/research/api/. r77_ba10 AC1 and AC2 FAIL at the base (no module, no test file).
EGRESS CLASS, declared: NONE. No vendor, SEC or model call: this cell TRANSLATES NOTHING; it serves what the producer already stored.
</preflight>

**Your worktree:** `C:/tmp/r77-276` (branch `wk-AMGT_RESAPP-276`, cut from the issuance commit with `--portal-ref 13509c52`, the portal DEV head at the cut (the api suite reads a portal fixture)). Work and commit only there. Start every shell call with `cd /c/tmp/r77-276`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-10` (round 77, decomposition s.85)

Row Z-S221, ruled by the CTO (`ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` ADDENDUM 1 @3bad4be9e0): **the API serves
`text_translated` beside the original, with a translated flag and the source language.**

What exists. The producer already carries the translation per drafted sentence
(`lib/research/filings/drafting_build.py:316-325`): `text_original`, `text_translated` when a translation ran, and a
`translation` block (`translated`, `source_language`, `translated_at`, and `failed` on a failed call;
`lib/research/filings/translate.py:157-199`). The served sentence drops all of it: `lib/research/api/scoped_amgt.py` builds the
served sentence at about lines 2962-2970 from `text`, `generated`, `evidence`, `verbatim_check` and `quoted_spans` only.

Build the projection as a NEW module, `lib/research/api/translated_text.py`, exporting ONE pure function:

`served_translation(sentence)` returns a NEW dict with exactly three keys:
- `text_translated`: the stored translated text, or `None` when the sentence carries none;
- `translated`: `True` only when the sentence carries a non-empty `text_translated` AND its `translation.translated` is true;
  otherwise `False`;
- `source_language`: `translation.source_language` when the sentence carries a `translation` block, else `None`.

Rules: it never changes the sentence it is given; it never makes a value up (a sentence with no translation serves `None`,
`False`, `None`); a FAILED translation serves `translated: False`, `text_translated: None` and its language. The original `text`
is untouched and stays what every quote and cite is checked against.

Plant tests in `lib/research/api/tests/test_translated_text.py`: translated, untranslated, failed, a `translation` block with no
`text_translated`, and the unchanged-input case.

**You do NOT edit `lib/research/api/scoped_amgt.py`.** The round's adapter cell, AMGT-ba-11, merges your three keys into each
served sentence. Your report names the hookup: every place in `scoped_amgt.py` that builds a served drafted sentence (the
sections builder at about 2962-2970 is one; census the file for others that serve a sentence's `text` with its
`verbatim_check`, with line numbers), and whether the driver's own translated fields (`series_translated`, `unit_translated`,
`why_translated`) have a served object that drops them too. Report that as a finding; do not build a driver projection.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W276-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/filings/` is READ, never edited: the producer and the translator keep their bytes.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/translated_text.py
lib/research/api/tests/test_translated_text.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~276/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-10"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba10.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>a translated sentence serves its text, translated True and its language; an untranslated one serves None, False, None; a failed one serves False with its language; the input is unchanged; C1-C4 PASS; R77 BA10 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-10"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba10.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>every plant case in test_translated_text.py passes; R77 BA10 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~276 <0.9.0_WK_AMGT_RESAPP~276@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~276/AMGT_RESAPP.TO-AMGT-ba-10.translated-text-on-a-served-sentence.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the hookup list for the adapter cell (each served-sentence site in `scoped_amgt.py`, with its line);
- the driver finding;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-76 analysis item 10 (the translated text); CTO ADDENDUM 1 @3bad4be9e0, row Z-S221. Detection was fixed by rk-107; this is the API limb. The merge into the served sentence is AMGT-ba-11's hookup. Checks dry-run at the base: ba-10 AC1 base FAIL as expected, AC2 base FAIL as expected.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~276</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @42969eda8b; proof VALID (worktree checker); translated_text.served_translation projection; AC1 4 of 4, AC2 7 plant tests; api suite 739 passed in the worktree; two hookup sites named</status>
