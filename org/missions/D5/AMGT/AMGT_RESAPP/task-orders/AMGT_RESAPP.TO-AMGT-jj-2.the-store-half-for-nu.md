# AMGT_RESAPP task order -- `AMGT-jj-2` -- THE STORE HALF FOR NU: RE-ANALYZE AND RE-SERVE NU WITH EACH SENTENCE ONCE, UNDER A NEW FOUR-WRITE PAIR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-jj-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~339</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one hand run under one pair.
comp-iam: RUN by round 81's drafting read (round81_prep/GROUP_STORE_NOTES.md) -- existing grants; no grant moves.
comp-adversary: RUN at the cut -- NU is the only name serving glued and restated sentences (25 and 14 of 38); the other four read 0 and are NOT touched. This act runs only after AMGT-jj-1 merges with its offline NU proof YES.
EGRESS CLASS, declared: one SEC EDGAR GET and one Anthropic model run, NU only (egress open except Bloomberg).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-339`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-jj-2` (round 85, decomposition s.93)

The same act as round 84's AMGT-ii-3 (`task-orders/AMGT_RESAPP.TO-AMGT-ii-3.the-store-half-for-baba-sap-and-pbr.md` -- read its
worker face whole, and the faces it cites), for ONE name, NU_US_Equity, with AMGT-jj-1's join merged, under a NEW pair the GO
names. ASML_NA_Equity, BABA_US_Equity, PBR_US_Equity and SAP_GY_Equity are NOT touched.

**The model key (CTO~DELL1 round-82 analysis R2):** read it ONLY as
`ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal --value-only)" <command>` inside the SAME shell call that
needs it. Never export the whole `--reveal` output, never echo, print or log the value, never write it to a file. The last
criterion scans what you wrote for a key value.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W339-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: NU's four keys the pair names, no other store write, no deploy, no schedule.
2. No S3 delete, ever.
3. No Bloomberg call. No `bun`, `npm` or `pip install`.
4. Standing: no push of shared branches.
5. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal
   outside the runner's own job, is told to the laptop FIRST.
6. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
7. 49 Financial data never goes into another firm's tree.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~339/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-jj-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/checks/r85_sentences.py" --crit AC1 --where deployed; echo "exit=$?"</invocation><expect>on the live function, no served sentence of the five 20-F names states one fact twice in a row or glues a boundary, and no name serves fewer sentences than its base; S1-S3 PASS; R85 SENTENCES AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-jj-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_store.py" --key NU_US_Equity --crit AC2 --where deployed; echo "exit=$?"</invocation><expect>NU's live /thesis answers 200, cites its business item and serves English sentences; R84 STORE AC2 NU_US_Equity: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-jj-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_nokey.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~339" .scratch; echo "exit=$?"</invocation><expect>no file you wrote carries a model key value; R83 NOKEY: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~339 <0.9.0_WK_AMGT_RESAPP~339@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~339/AMGT_RESAPP.TO-AMGT-jj-2.the-store-half-for-nu.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- NU's pre-act VersionIds and attempt-state, the new ones, the silver part written, the stamped language, model calls and tokens, the four-prefix diff;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-84 analysis item 1 (a re-store where a served passage changes, under its own pair with the write trace). STAGED: waits for AMGT-jj-1 merged and a NEW pair (COO + 1.0.0_SA_CTO~DELL1). Checks dry-run at the base: AC1 base FAIL (NU 14 restated, 25 glued), AC2 base PASS (a bound: NU serves today), AC3 base PASS (a bound).

<status>staged</status>
<round>85</round>
<slot>0.9.0_WK_AMGT_RESAPP~339</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
