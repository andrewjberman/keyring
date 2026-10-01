# AMGT_RESAPP task order -- `AMGT-ag-2` -- EVERY SERVED REASON IN PLAIN WORDS; BA'S RESEARCH-PACK CLAIMS AGREE (CONTRACT s.4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ag-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~200</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; served-text code.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read or write.
comp-adversary: RUN by the issuer at the cut -- AC2 FAILS at the base (C1: 16 of 1,106 served reason strings across 3 names x 4 routes carry a status token; C3: ASML's absent posture carries no absent_reason). C2 PASSES at the base: "no research pack" appears in no served string for BA, so the sentence the CTO cites may be page text; item 3 settles it.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r57-200` (branch `wk-AMGT_RESAPP-200`, cut from the issuance commit; full checkout, `portal/` included).
Work and commit only there.

## 1. THE ACT -- `AMGT-ag-2` (round 57, decomposition s.65)

The shared CONTRACT s.4: the words "not served", "unsupported", "ABSENT" and "REFUSED" never reach the page for a field the route
serves; a truly absent value carries `absent_reason` from the server in plain words. This order changes TEXT only.

1. **Every served `*reason` string in plain words.** Today 16 served reasons carry a status token, for example thesis
   `scores.peers_v.measures[i].absent_reason` = "ABSENT for the subject (measure not computable from its own row)", `scores.divergence`,
   and `management.ceo_profile_reading.reason` ("... ABSENT is the honest result ..."). Rewrite each at the function that BUILDS the
   string, as words a reader of the page understands. Do not strip words in a post-filter. Lower-case "absent" in a sentence is fine;
   the status tokens are not.
2. **Posture.** A posture whose `verdict` is `absent` (ASML, HAL, PBR at the cut) gains `absent_reason`: one plain sentence saying why no
   verdict was made (today its `reason` reads "comparable null: R-1 carries no held member ..."). It must carry no internal label (R-1,
   M-1), no `null`/`None`, and no status token. `reason` may stay as the technical record.
3. **BA's research pack (CTO msg 27539; DSGN round-14 ruling 3).** The DSGN page's Thesis tab for BA_US_Equity reads "no research pack
   for this security" while Exec and Model presuppose one. Find where that sentence comes from (`portal/src/pages/SecurityAnalysis/`
   is readable in your worktree). If a SERVED field produces it, correct the field that is wrong and say which. If the page writes it
   (no served field does), file ONE ROW naming the page component, the condition that shows the sentence, and the served field the
   page should read instead, `disarm_owner` `2.0.0_SA_COO~Z`. Do not edit the portal.
4. **Test** `lib/research/api/tests/test_served_reasons_plain.py` for items 1 and 2.

## 2. BOUNDS

1. Write only the paths below. Text only: no figure, verdict, ranking or field name changes beyond the new `absent_reason`. No deploy
   (ag-1 deploys), no store write, no vendor call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~200/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ag-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/ lib/research/posture/; echo "exit=$?"</invocation><expect>every test passes, test_served_reasons_plain.py included (342 + 22 at the cut), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ag-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round56/checks/af_7_text.py; echo "exit=$?"</invocation><expect>C1, C2 and C3 PASS; EVERY SERVED REASON IS PLAIN WORDS AND BA'S PACK CLAIMS AGREE: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~200 <0.9.0_WK_AMGT_RESAPP~200@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~200/AMGT_RESAPP.TO-AMGT-ag-2.served-reasons-in-plain-words.proof_of_spec.json`.
Report once: the commit hash, both criteria's output lines, every producer function whose text you changed, the BA finding, and any
row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-56 analysis enrichment item 2 (CTO msg 27539; DSGN round-14 rulings 2-3). Rides ag-1's redeploy. No positive
arm was simulated (the fix is text at many producers). The base FAILS C1 and C3 on the named strings; C2's base PASS is the open
question that item 3 answers. The worktree is a FULL checkout (round-56 ruling 3: the sparse cone cost a round).

<status>pending</status>
<round>57</round>
<slot>0.9.0_WK_AMGT_RESAPP~200</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-01 ~07:4xZ):** worker ~200 `678e9ac1c5`, drained `cb5f25b9de`. Re-graded on the full tree: AC1 375 passed exit=0; AC2 YES (0 bad of 1,115; C3 ASML absent_reason plain). BA finding: the sentence is page text (`reasonWords.ts:33` rewrites the served class-A reason to "research pack"); row Z-W200-S1 routed to COO~D (CONTRACT s.0). Left for a later cell: coverage `most_discussed_basis` reads "ABSENT -- P-1 ..." (its key does not end in `reason`). Served at ag-1.

<status>complete</status>
