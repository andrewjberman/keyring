# AMGT_RESAPP task order -- `AMGT-jj-1` -- THE ANALYSIS JOINS THE MODEL'S TEXT BLOCKS WITH A SPACE AND KEEPS THE FILING'S SENTENCE OVER ITS PARAPHRASE, PROVED OFFLINE ON NU

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-jj-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~338</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one module, its tests and one offline run.
comp-iam: DECLARED-NOT-APPLICABLE -- reads NU's stored silver part and drafting document read-only; writes no store.
comp-adversary: RUN at the cut (round85_prep/GROUP_SENTENCE_NOTES.md) -- analyze.py:643 (and :427, :502) joins the model's text blocks with "": a paraphrase ending "...in 2024." fuses onto the filing's verbatim sentence restating the same figures. Live: NU 25 of 38 served texts glued, 14 restated; ASML, BABA, PBR, SAP 0.
EGRESS CLASS, declared: one Anthropic model run on NU (egress open except Bloomberg). No SEC fetch.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-338`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-jj-1` (round 85, decomposition s.93)

CTO~DELL1 round-84 analysis item 1 (capture 004's defect). Read
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/GROUP_SENTENCE_NOTES.md` WHOLE first, then
`lib/research/filings/analyze.py` around :427, :502 and :643.

1. Join the model's text blocks with one space (never "").
2. Where a paraphrase block is followed by the filing's own sentence restating the same fact, keep the FILING's sentence (the
   paraphrase would fail the verbatim gate); never keep both.
3. Tests in `lib/research/filings/tests/`: planted blocks for each case (a paraphrase + its verbatim twin; two distinct sentences
   that must both stay, joined by a space; a block that genuinely ends mid-sentence).
4. **The offline proof, NO store write:** re-run NU_US_Equity's analysis on its CURRENT stored silver source, exactly as
   `round83_prep/GROUP_PASSAGE_NOTES.md` section "The offline run" does for ASML (never `--write-pool`), and write the drafting
   document it builds to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~338/offline/draft.json`.

**The model key (CTO~DELL1 round-82 analysis R2):** read it ONLY as
`ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal --value-only)" <command>` inside the SAME shell call that
needs it. Never export the whole `--reveal` output, never echo, print or log the value, never write it to a file. The last
criterion scans what you wrote for a key value.

Run `lib/research/filings/tests/` and `lib/research/drafting/` before your commit (an empty `fitz.py` on PYTHONPATH) and report
both last lines.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W338-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. No store write of any kind; no deploy; no SEC fetch; no Bloomberg call.
2. No `bun`, `npm` or `pip install`.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `analyze.py` and one test file only.

## 3. SURFACES

<paths>
lib/research/filings/analyze.py
lib/research/filings/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~338/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-jj-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/checks/r85_sentences.py" --crit AC1 --where file --keys NU_US_Equity --draft "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~338/offline/draft.json" --no-floor; echo "exit=$?"</invocation><expect>NU's offline draft states no fact twice in a row, glues no sentence boundary, (S3, the sentence floor, printed but not graded -- AMENDMENT 1); S1-S2 PASS; R85 SENTENCES AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-jj-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_nokey.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~338" .scratch; echo "exit=$?"</invocation><expect>no file you wrote carries a model key value; R83 NOKEY: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~338 <0.9.0_WK_AMGT_RESAPP~338@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~338/AMGT_RESAPP.TO-AMGT-jj-1.machine-sentences-served-once.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the two test folders' last lines;
- model calls and tokens;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-84 analysis @f928f73e6e item 1. analyze.py is imported by site-Z hand-run tools only; the analyzer task is disabled (CTO msg 1267 rule) -- the merge re-reads that census. Checks dry-run at the base: AC1 base FAIL as expected on NU's current stored draft through the file arm (14 restated, 25 glued of 38); AC2 base PASS (a bound).

<status>pending</status>
<round>85</round>
<slot>0.9.0_WK_AMGT_RESAPP~338</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending -- AMENDMENT 1 (issuer, 2026-10-09T13:0xZ) on CTO~DELL1 msg 2442 and row AMGT_RESAPP-D1-W338-S1: a fresh model draw's yield (10 of 11 NU draws paraphrase-only; 22 served vs the stored 38) is not the join repair's to control, so AC1 grades S1-S2 on the offline draft with --no-floor; the served floor moves to AMGT-jj-2 (graded on the live function after NU's stored draft is repaired in place, ADDENDUM 2). W338-S1 is carried to round 86. Graded by no gate limb (a modification; <placeholders>NONE).</status>
