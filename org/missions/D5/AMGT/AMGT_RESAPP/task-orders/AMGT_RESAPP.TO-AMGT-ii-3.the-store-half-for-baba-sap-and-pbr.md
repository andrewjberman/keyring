# AMGT_RESAPP task order -- `AMGT-ii-3` -- THE STORE HALF FOR BABA, SAP AND PBR: RE-CUT AND RE-ANALYZE IN ENGLISH WITH CLEAN SECTIONS, UNDER A NEW FOUR-WRITE PAIR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ii-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~336</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; hand runs under one pair.
comp-iam: RUN by round 81's drafting read (round81_prep/GROUP_STORE_NOTES.md) -- existing grants; no grant moves.
comp-adversary: RUN at the cut -- round 83's hh-4 rolled BABA back (Portuguese draft, 0 of 40 served) and never ran SAP, both on the language stamp; PBR was held for its cut. This act runs only after AMGT-ii-1 and AMGT-ii-2 merge.
EGRESS CLASS, declared: SEC EDGAR GETs (one filing per name) and one Anthropic model run per name (egress open except Bloomberg).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-336`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ii-3` (round 84, decomposition s.92)

The same act as round 83's AMGT-hh-4 (`task-orders/AMGT_RESAPP.TO-AMGT-hh-4.the-store-half-with-paragraph-passages.md` -- read its
worker face whole, and the faces it cites: the in-process cut check before the first live act, the four keys per name, the
per-name before/after listing, no half-landed name, rollback by re-writing prior versions, never a delete), now with AMGT-ii-1's
language stamp and AMGT-ii-2's header strip merged, under a NEW pair the GO names. Names, in order: BABA_US_Equity (first and gated:
its AC1 and AC2 read YES for BABA before any other name), SAP_GY_Equity, PBR_US_Equity. ASML_NA_Equity and NU_US_Equity are NOT
touched (no served passage of theirs carries a header).

**Before the first live act, per name, in-process with no write:** run `fetch.build_source_object` on the name's cached filing
(`r84_language.py` shows how) and STOP that name unless it is stamped `en` with business, risk and mdna cut.

**The model key (CTO~DELL1 round-82 analysis R2):** read it ONLY as
`ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal --value-only)" <command>` inside the SAME shell call that
needs it. Never export the whole `--reveal` output, never echo, print or log the value, never write it to a file. The last
criterion scans what you wrote for a key value.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W336-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

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
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~336/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ii-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" py -3.12 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_store.py" --key BABA_US_Equity,SAP_GY_Equity,PBR_US_Equity --crit AC1; echo "exit=$?"</invocation><expect>each name's latest stored source is parser 2.0.0, carries a business section and is stamped en; R84 STORE AC1 ALL: YES 3 of 3; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ii-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_store.py" --key BABA_US_Equity,SAP_GY_Equity,PBR_US_Equity --crit AC2 --where deployed; echo "exit=$?"</invocation><expect>each name's live /thesis answers 200, cites its business section and serves English sentences; R84 STORE AC2 ALL: YES 3 of 3; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ii-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_nokey.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~336" .scratch; echo "exit=$?"</invocation><expect>no file you wrote carries a model key value; R83 NOKEY: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~336 <0.9.0_WK_AMGT_RESAPP~336@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~336/AMGT_RESAPP.TO-AMGT-ii-3.the-store-half-for-baba-sap-and-pbr.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- per name: the pre-act VersionIds and attempt-state, the new ones, the silver part written, the stamped language, model calls and tokens, the four-prefix diff;
- every criterion's output lines;
- the change-management entry's slug and state;
- any name not re-cut, and why;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-83 analysis enrichment items 1-2 (the store half for the names the language stamp and PBR's cut held). STAGED: waits for AMGT-ii-1 and AMGT-ii-2 merged under 1.0.0_SA_CTO~Z's halves and a NEW pair (COO + 1.0.0_SA_CTO~DELL1) carrying round 83's conditions 1-7. Checks dry-run at the base: AC1 base FAIL (0 of 3), AC2 base FAIL (BABA 0 business locations), AC3 base PASS (a bound).

<status>staged</status>
<round>84</round>
<slot>0.9.0_WK_AMGT_RESAPP~336</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending -- GO 2026-10-09T11:2xZ by the issuer: condition 9 met -- AMGT-ii-1 merged @acb31d3592 (CTO~Z @344af2c348) and AMGT-ii-2 merged @b9ce1ef7cb (CTO~Z @4d6a429d98); on the merged tree r84_language YES (5 of 5 en), r84_header YES, r82_cut 15/15. Pair COO @c59a18f623 + CTO @a7ea763339 (round-83 conditions 1-7; 8 the per-name in-process language-and-cut check -- a failing name is skipped and reported, the others proceed; 9 met; 10 PBR last and only on a clean offline cut). Order: BABA_US_Equity (first; its AC1/AC2 YES before SAP), SAP_GY_Equity, PBR_US_Equity. Worktree ~336 cut from box/dell1 after this line. Graded by no gate limb (a modification).</status>
<status>pending -- AMENDMENT 1 (issuer, 2026-10-09T11:4xZ): AC2's T3 English test (r84_store.py) counted only ' the / and / of ' and read SAP's number-heavy English segment sentences as unmarked (26 of 34, 76%, below the 80% floor) -- the issuer read all 8 unmarked sentences: plain English ('ATS segment profit increased 19% ... from ... to ...'). The marker set is widened to common English function words (the, and, of, to, in, from, at, on, with, its, is, are, was, were, by, for, versus); negative control: 0 of 3 planted Portuguese/Spanish sentences marked. Same invocation, @this commit. Issuer's read on the live function after the act: AC1 ALL YES 3 of 3 (all parser 2.0.0, stamped en, business cut); AC2 ALL YES 4 of 4 incl. NU (BABA 10 of 20 business locations, SAP 9 of 20, PBR 14 of 28; 100% English). Graded by no gate limb (a modification; <placeholders>NONE).</status>
