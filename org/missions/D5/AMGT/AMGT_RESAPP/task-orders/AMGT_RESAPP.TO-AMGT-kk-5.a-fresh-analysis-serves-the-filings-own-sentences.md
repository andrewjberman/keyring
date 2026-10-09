# AMGT_RESAPP task order -- `AMGT-kk-5` -- A FRESH ANALYSIS SERVES THE FILING'S OWN SENTENCE FOR A FIGURE ITEM, PROVED OFFLINE ON NU AT THE STORED FLOOR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-kk-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~345</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one module, its tests and one offline run.
comp-iam: DECLARED-NOT-APPLICABLE -- reads NU's stored silver part read-only; writes no store.
comp-adversary: RUN at the cut (round86_prep/GROUP_YIELD_NOTES.md) -- pass 1 makes quoting optional (analyze.py:176-178); the citation's cited_text never reaches the item; the drafting gate needs an 8-token verbatim run (drafting_build.py:205-220), so a paraphrase-only item is held: the surviving fresh NU draft serves 22 (0 wholly verbatim); 15 of 17 held items cite a passage that holds the filing's own sentence.
EGRESS CLASS, declared: one Anthropic model run on NU (egress open except Bloomberg).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-345`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-kk-5` (round 86, decomposition s.94)

CTO~DELL1 round-85 analysis R4 (row W338-S1). Read `round86_prep/GROUP_YIELD_NOTES.md` whole. Repair (the notes' option B, figures
first): when an item's own text is a paraphrase, drafting serves the cited passage's sentence that carries the item's figures, so the
served sentence is the filing's own text; narrative items keep today's rule. Code in `lib/research/filings/drafting_build.py` (after
AMGT-kk-2 merges -- same file) plus tests. Then ONE offline NU run, no store write (round83_prep/GROUP_PASSAGE_NOTES.md "The offline
run"; never `--write-pool`), writing `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~345/offline/draft.json`.

**The model key (CTO~DELL1 round-82 analysis R2):** read it ONLY as
`ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal --value-only)" <command>` inside the SAME shell call that
needs it. Never print, log or write the value. The last criterion scans what you wrote for a key value.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W345-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. No store write; no deploy; no SEC fetch; no Bloomberg call.
2. No `bun`, `npm` or `pip install`.
3. Standing: no S3 delete, no push of shared branches.
4. You edit `drafting_build.py` and one test file only.

## 3. SURFACES

<paths>
lib/research/filings/drafting_build.py
lib/research/filings/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~345/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-kk-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" py -3.12 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round86_prep/checks/r86_yield.py" --crit AC1 --draft "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~345/offline/draft.json"; echo "exit=$?"</invocation><expect>NU's fresh offline draft serves at least 38 sentences, every served sentence verbatim, 0 glued and 0 restated; Y1-Y3 PASS; R86 YIELD AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-kk-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_nokey.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~345" .scratch; echo "exit=$?"</invocation><expect>no file you wrote carries a model key value; R83 NOKEY: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~345 <0.9.0_WK_AMGT_RESAPP~345@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~345/AMGT_RESAPP.TO-AMGT-kk-5.a-fresh-analysis-serves-the-filings-own-sentences.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- served / held / refused counts and how many served sentences came from the cited passage;
- model calls and tokens (ONE run expected);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-85 analysis R4. STAGED behind AMGT-kk-2 (same file). Checks dry-run at the base: AC1 base FAIL (round 85's fresh draft: Y1 22 of 38, Y2 0 of 22); AC2 base PASS (a bound).

<status>staged</status>
<round>86</round>
<slot>0.9.0_WK_AMGT_RESAPP~345</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending -- GO 2026-10-09T15:0xZ by the issuer: AMGT-kk-2 merged @246654e7a6 (same file, drafting_build.py). Worktree ~345 cut from box/dell1 after this line. ONE offline NU run expected. Graded by no gate limb (a modification).</status>
