# AMGT_RESAPP task order -- `AMGT-hh-4` -- THE STORE HALF WITH PARAGRAPH PASSAGES: RE-CUT AND RE-ANALYZE THE STORED 20-F NAMES, ASML NA FIRST, UNDER A NEW FOUR-WRITE PAIR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-hh-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~332</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; hand runs under one pair.
comp-iam: RUN by round 81's drafting read (round81_prep/GROUP_STORE_NOTES.md) -- existing grants; no grant moves.
comp-adversary: RUN at the cut -- round 82's gg-2 stopped at ASML NA's gate (0 of 11 served locations from Item 4.B) and rolled ASML back byte-equal; condition 5's write trace held. This act runs only after AMGT-hh-2's offline proof reads YES.
EGRESS CLASS, declared: SEC EDGAR GETs (one filing per name) and one Anthropic model run per name (egress open except Bloomberg).
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-332`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-hh-4` (round 83, decomposition s.91)

The same act as round 82's AMGT-gg-2 (`task-orders/AMGT_RESAPP.TO-AMGT-gg-2.the-store-half-with-the-repaired-cutter.md` -- read
its worker face whole: the in-process cut check before the first live act, the four keys per name, the per-name before/after
listing, the ASML gate, no half-landed name, rollback by re-writing prior versions, never a delete), now with AMGT-hh-1's
paragraph passages merged and under a NEW pair (COO + 1.0.0_SA_CTO~DELL1) the GO names. Names: ASML_NA_Equity (first and gated),
BABA_US_Equity, NU_US_Equity, SAP_GY_Equity; PBR_US_Equity only if the GO says AMGT-hh-3 has merged, else held.

**The model key (CTO~DELL1 round-82 analysis R2):** read it ONLY as
`ANTHROPIC_API_KEY="$(comp-secrets get anthropic-api-key --reveal --value-only)" <command>` inside the SAME shell call that
needs it. Never export the whole `--reveal` output, never echo, print or log the value, never write it to a file. The last
criterion scans what you wrote for a key value.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W332-S<k>` (dell1's registered coordinate is D1), `disarm_owner` `2.0.0_SA_COO~R1`.

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
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~332/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-hh-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81_prep/checks/r81_store.py" --crit AC1; echo "exit=$?"</invocation><expect>ASML NA's latest stored source carries a business section cut from its own heading; S1-S3 PASS; R81 STORE AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-hh-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round81_prep/checks/r81_store.py" --crit AC2 --where deployed; echo "exit=$?"</invocation><expect>the live /thesis for ASML NA answers 200, serves the share-capital refusal sentence 0 times and cites a business section; T1-T3 PASS; R81 STORE AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-hh-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round83_prep/checks/r83_nokey.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~332" .scratch; echo "exit=$?"</invocation><expect>no file you wrote carries a model key value; R83 NOKEY: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~332 <0.9.0_WK_AMGT_RESAPP~332@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~332/AMGT_RESAPP.TO-AMGT-hh-4.the-store-half-with-paragraph-passages.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- per name: the pre-act VersionIds and attempt-state, the new ones, the silver part written, model calls and tokens, the four-prefix diff;
- every criterion's output lines;
- the change-management entry's slug and state;
- any name not re-cut, and why;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-82 analysis enrichment item 4. STAGED: waits for AMGT-hh-1 merged, AMGT-hh-2's AC1 YES, and a NEW pair (COO + 1.0.0_SA_CTO~DELL1) carrying round 82's conditions 1-5. Checks dry-run at the base: AC1 base FAIL (parser 1.0.0 at the base), AC2 base FAIL (0 of 11), AC3 base PASS (a bound).

<status>staged</status>
<round>83</round>
<slot>0.9.0_WK_AMGT_RESAPP~332</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending -- GO 2026-10-09T09:3xZ by the issuer: condition 6 met -- AMGT-hh-1 merged @ac6ad315b6 (not a site-Z producer path while the analyzer task is disabled) and AMGT-hh-2's offline ASML proof YES @7d99ec5339. Pair COO @a84986e02f + CTO @4b37e0dcea (round-82 conditions 1-5, plus 6 and 7: the key only with --value-only in the same call; a transcript showing it is a STOP). FOUR names: ASML_NA_Equity (first, gated), BABA_US_Equity, NU_US_Equity, SAP_GY_Equity; PBR_US_Equity HELD (AMGT-hh-3 not merged: its site-Z half is owed). Worktree ~332 cut from box/dell1 after this line. Graded by no gate limb (a modification).</status>
