# AMGT_RESAPP task order -- `AMGT-kk-3` -- THE FIVE STORED 20-F DRAFTS: COMPANY DESCRIPTION FROM THE BUSINESS ITEM ONLY, AND NU'S THREE CUT SENTENCES RESTORED WHOLE, IN PLACE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-kk-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~343</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; five in-place writes under one pair.
comp-iam: RUN by round 85's jj-2 (the drafting/v1 grant) -- no grant moves.
comp-adversary: RUN at the cut -- do NOT rebuild NU from its stored analysis (it still holds the glued text; a rebuild undoes round 85's repair). Live: 24 of 25 description sentences cite Item 5 / 3.D; NU's sentences 6, 11, 19 were cut to their first filing sentence by the old year rule (row W339-S2, now fixed @f36289abfa).
EGRESS CLASS, declared: NONE (no fetch, no model call).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-343`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-kk-3` (round 86, decomposition s.94)

CTO~DELL1 round-85 analysis R2 and R5. IN PLACE, five keys `drafting/v1/<KEY>.json` (ASML_NA_Equity, BABA_US_Equity, NU_US_Equity,
PBR_US_Equity, SAP_GY_Equity), no fetch, no model call:
1. In each, the `company_description` section keeps only sentences whose evidence cites the business item; none left -> the section
   is empty (sentences []). No other section changes.
2. In NU's only, sentences 6, 11 and 19 are restored to the WHOLE filing sentence (round 85 jj-2's `build_repaired.py` without
   `--first-only`; read `deliverables/0.9.0_WK_AMGT_RESAPP~339/`), evidence unchanged.
Build the five locally first under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~343/repaired/`; BEFORE any write print AC1 on NU's local copy. Per key, record the prior
VersionId in the change-management entry (one leg per key) and the before/after version listing; rollback re-puts the prior bytes,
never a delete. The CVO reads the served sections afterwards.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W343-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. The act and nothing else: the five drafting keys, no other key, no deploy, no schedule.
2. No S3 delete, ever.
3. No fetch, no model call, no Bloomberg call. No `bun`, `npm` or `pip install`.
4. Standing: no push of shared branches.
5. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal
   outside the runner's own job, is told to the laptop FIRST.
6. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
7. 49 Financial data never goes into another firm's tree.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~343/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-kk-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" py -3.12 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/checks/r85_repair.py" --crit AC1 --draft "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~343/repaired/NU_US_Equity.json" --exclude-section company_description; echo "exit=$?"</invocation><expect>BEFORE the write, NU's local repaired draft keeps every sentence outside company_description, 0 glued and 0 restated, every sentence verbatim in NU's stored filing, citations intact; K1-K4 PASS; R85 REPAIR AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-kk-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round86_prep/checks/r86_description.py" --crit AC1; echo "exit=$?"</invocation><expect>on the live function every company_description sentence cites the business item, none cites Item 5 or 3.D, and a name with none serves an empty section; D1-D3 PASS; R86 DESCRIPTION AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-kk-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/checks/r85_sentences.py" --crit AC1 --where deployed --exclude-section company_description --base-file "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round86_prep/checks/r86_sentences_base.json"; echo "exit=$?"</invocation><expect>on the live function, outside company_description, no sentence glued or restated over the five names and none below the pre-act base; S1-S3 PASS; R85 SENTENCES AC1: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~343 <0.9.0_WK_AMGT_RESAPP~343@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~343/AMGT_RESAPP.TO-AMGT-kk-3.stored-drafts-description-and-nu-restored.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- per key: prior and new VersionIds, sentences removed from company_description (with their items), and for NU the three restored sentences;
- every criterion's output lines;
- the change-management entry's slug and state;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-85 analysis R2 + R5 (stored half). STAGED: waits for a NEW pair (COO + 1.0.0_SA_CTO~DELL1) naming the five drafting keys. Base recorded @r86_sentences_base.json (ASML 16, BABA 19, NU 28, PBR 22, SAP 13 outside company_description). Checks dry-run at the base: AC1 base FAIL on the pre-round-85 NU draft (K3), AC2 base FAIL (24 of 25), AC3 base PASS (a bound).

<status>staged</status>
<round>86</round>
<slot>0.9.0_WK_AMGT_RESAPP~343</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
