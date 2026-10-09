# AMGT_RESAPP task order -- `AMGT-hh-2` -- THE OFFLINE PROOF: RE-ANALYZE ASML NA ON ITS STORED EXCERPT WITH THE PARAGRAPH PASSAGES, NO STORE WRITE, AND SHOW ITEM 4.B SERVED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-hh-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~330</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one hand run.
comp-iam: DECLARED-NOT-APPLICABLE -- reads the stored silver part read-only; writes nothing to any store.
comp-adversary: RUN at the cut -- round 82's analysis built from 8 business passages served 0 of 11 locations from Item 4.B and refused 14 sentences; the round-82 worker printed the model key into its transcript (row D1-W324-S3).
EGRESS CLASS, declared: one Anthropic model run (analyze's passes) on ASML NA (egress open except Bloomberg). No SEC fetch.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-330`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-hh-2` (round 83, decomposition s.91)

R1 of the round-82 analysis: prove OFFLINE, before any store write, that with AMGT-hh-1's paragraph passages ASML NA's business
text reaches served locations and every served sentence passes the verbatim gate.

Read `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/GROUP_PASSAGE_NOTES.md` WHOLE, including its
section "The offline run": it gives the exact commands that build the analysis and the draft from ASML NA's stored excerpt with
NO store write. Run them with `py -3.12`, writing the analysis and draft JSON under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~330/offline/` (`analysis.json`, `draft.json`). Never pass
`--write-pool` or any flag that writes a store. If the notes' commands would write anywhere but that folder, STOP with a BLOCKING row.

**The model key (CTO~DELL1 round-82 analysis R2):** read it ONLY as
`ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal --value-only)" <command>` inside the SAME shell call that
needs it. Never export the whole `--reveal` output, never echo, print or log the value, never write it to a file. The last
criterion scans what you wrote for a key value.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W330-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. No store write of any kind; no deploy; no SEC fetch; no Bloomberg call.
2. No `bun`, `npm` or `pip install`.
3. Standing: no S3 delete, no push of shared branches.
4. You write only your deliverables folder and the surprise channel; no code edit.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~330/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-hh-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" py -3.12 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_offline.py" --crit AC1 --analysis "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~330/offline/analysis.json" --draft "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~330/offline/draft.json"; echo "exit=$?"</invocation><expect>at least one served sentence cites a passage inside Item 4.B, every served sentence passes the pipeline's own verbatim gate, and fewer sentences are refused than served; O1-O3 PASS; R83 OFFLINE AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-hh-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_nokey.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~330" .scratch; echo "exit=$?"</invocation><expect>no file you wrote carries a model key value; R83 NOKEY: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~330 <0.9.0_WK_AMGT_RESAPP~330@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~330/AMGT_RESAPP.TO-AMGT-hh-2.the-offline-reanalysis-of-asml-na.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the served / held / refused counts and the Item 4.B served sentences with their cited passage ids;
- model calls and tokens;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-82 analysis R1 (the offline proof) + R2 (the key read). Chained after AMGT-hh-1 (its worktree is cut from hh-1's merge). Checks dry-run at the base: AC1 base FAIL on the rolled-back round-82 objects (0 served cite 4.B); AC2 base PASS (a bound).

<status>staged</status>
<round>83</round>
<slot>0.9.0_WK_AMGT_RESAPP~330</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
