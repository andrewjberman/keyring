# AMGT_RESAPP task order -- `AMGT-gg-2` -- THE STORE HALF WITH THE REPAIRED CUTTER: RE-CUT AND RE-ANALYZE THE FIVE STORED 20-F NAMES, ASML NA FIRST, UNDER A FOUR-WRITE PAIR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-gg-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~324</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; five hand runs under one pair.
comp-iam: RUN by round 81's drafting read (round81_prep/GROUP_STORE_NOTES.md) -- existing grants; no grant moves.
comp-adversary: RUN at the cut -- round 81's ee-4 stopped at ASML NA (UNRESOLVED-SOURCE, the cutter cut nothing); it wrote one state key outside its pair. This order's pair names FOUR writes per name (silver, analysis, drafting, the attempt-state key).
EGRESS CLASS, declared: SEC EDGAR GETs (one filing per name) and one Anthropic model call per name (egress open except Bloomberg).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-324`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-gg-2` (round 82, decomposition s.90)

The same act as round 81's AMGT-ee-4 (`task-orders/AMGT_RESAPP.TO-AMGT-ee-4.the-store-half-five-20f-names.md` -- read its face whole:
the per-name steps, the no-delete rollback and the ASML gate are unchanged), now with the cutter AMGT-gg-1 repaired, and under a
pair that names FOUR writes per name: the silver part, the analysis, the drafting document, and the attempt-state key
`amgt/harvest/state/filing_attempt/security_key=<KEY>/...` that `fetch.persist` writes on an unresolved source.

Differences from ee-4:
1. **Before the first live act, prove the cut on the real filing in-process with no write:** run `r82_cut.py --crit AC1` and
   STOP with a BLOCKING row unless ASML NA's three cells read OK.
2. Record each name's attempt-state key's current state (head-object; absent is a state) in the entry before the first write.
3. ASML NA's attempt-state key from round 81 (`.../security_key=ASML_NA_Equity/UNRESOLVED-SOURCE.json`, VersionId
   XCTQo1uW9rvomS3k12_BqMRLq4EFm81B) is named by the pair; leave it as the producer leaves it.
Everything else -- `py -3.12`, the CIK measured from the stored row, `--source-json` always, the ASML gate, no half-landed name,
rollback by re-writing prior versions, never a delete -- as ee-4's face says.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W324-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the four keys per name the pair names, no other store write, no deploy, no schedule.
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
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~324/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-gg-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81_prep/checks/r81_store.py" --crit AC1; echo "exit=$?"</invocation><expect>ASML NA's latest stored source carries a business section cut from its own heading; S1-S3 PASS; R81 STORE AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-gg-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81_prep/checks/r81_store.py" --crit AC2 --where deployed; echo "exit=$?"</invocation><expect>the live /thesis for ASML NA answers 200, serves the share-capital refusal sentence 0 times and cites a business section; T1-T3 PASS; R81 STORE AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-gg-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81/checks/r81_ee4_census.py"; echo "exit=$?"</invocation><expect>the census names the five stored 20-F names, all at parser opal-filings-fetch/2.0.0, ASML NA's business from its own heading, no risk item from the fallback heading; E1-E4 PASS; R81 EE4 CENSUS: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~324 <0.9.0_WK_AMGT_RESAPP~324@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~324/AMGT_RESAPP.TO-AMGT-gg-2.the-store-half-with-the-repaired-cutter.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- per name: the pre-act VersionIds and attempt-state, the new ones, the silver part written, model calls and tokens;
- every criterion's output lines;
- the change-management entry's slug and state;
- any name not re-cut, and why;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-81 analysis R1 / enrichment item 2: the store half under a NEW four-write pair. STAGED: waits for AMGT-gg-1's merge (itself waiting on 1.0.0_SA_CTO~Z) and this act's pair (COO + 1.0.0_SA_CTO~DELL1). Checks dry-run at the base: AC1 base FAIL, AC2 base FAIL, AC3 base FAIL, as round 81 measured.

<status>staged</status>
<round>82</round>
<slot>0.9.0_WK_AMGT_RESAPP~324</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
