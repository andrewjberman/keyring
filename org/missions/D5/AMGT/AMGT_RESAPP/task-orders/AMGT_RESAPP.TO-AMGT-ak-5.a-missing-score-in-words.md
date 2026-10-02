# AMGT_RESAPP task order -- `AMGT-ak-5` -- A MISSING SCORE IN WORDS: THE POSTURE DRAFTER NEVER WRITES A STATUS TOKEN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ak-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~203</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; drafter code and a read-only plan.
comp-iam: DECLARED-NOT-APPLICABLE -- the plan builder only READS the pool (the stored posture documents).
comp-adversary: RUN by the issuer at the cut -- AC2 FAILS at the base: C1 2 of 12 served posture claims carry "ABSENT" (BA basis[1], VLO basis[5]); C2 no normalizer exists.
EGRESS CLASS, declared: NONE. NO MODEL CALL: `judge.anthropic_call` is a vendor call reserved to Andrew per use. Never run the judge.
</preflight>

**Your worktree:** `C:/tmp/r61-203` (branch `wk-AMGT_RESAPP-203`, cut from the issuance commit; full checkout). Work and commit only there.

## 1. THE ACT -- `AMGT-ak-5` (round 61, decomposition s.69; DSGN round-21 analysis section 3B cell B4, CTO msg 28264)

The served `thesis.posture.basis[*].claim` is text the posture judge (`lib/research/posture/judge.py`) drafted through a model and
stored. Two served claims print a status token:
- BA_US_Equity basis[1]: "Fit scores for both names are ABSENT (unmeasured) on both presets, so no factor-based discrimination is possible."
- VLO_US_Equity basis[5]: "... and fit scores are ABSENT for both and therefore unmeasured on either side."

The drafter must state a missing score in words and never write a status token (`ABSENT`, `NULL`, `MISSING`, upper case; a lower-case
word in a sentence is fine).

1. **The drafter's inputs.** The judge's instructions (`judge.py` ~lines 105-112: "Where a pack says ABSENT ...", "A fit score whose
   status is ABSENT is unmeasured, not low") and the pack lines (`packs.py`, `fit.py` summary lines such as "DIVZ ABSENT 0 of 13") teach
   the model the token. Change the text the MODEL READS so a missing score reaches it in words ("not measured: 0 of 13 factors present"),
   and the instruction says to write a missing score in words. Keep machine fields (`status` values in the stored JSON) as they are:
   only the drafted prose and the prose the model reads change.
2. **`plain_claim(text: str) -> str`** in `lib/research/posture/judge.py`: a DETERMINISTIC normalizer on the drafter's write path. Every
   drafted claim passes through it before the document is written. It rewrites a status token as words that keep the sentence's
   meaning (for example "fit scores are ABSENT for both" -> "fit scores are not measured for both"; "ABSENT (unmeasured)" -> "not
   measured"), and leaves a claim with no token byte-identical.
3. **The rewrite plan for the STORED claims.** A read-only builder lists every stored posture document in the pool whose served
   `basis[*].claim` carries a token, and computes each replacement BY CALLING `plain_claim` (never a hand-typed string). Emit
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~203/posture_claim_plan.json`:
   `{"denominator": <posture documents scanned>, "entries": [{"security_key", "route": "thesis", "json_path": ".posture.basis[<i>].claim", "store_key": "<the exact pool key>", "store_field": "<the field path inside the stored document>", "before": "<as served>", "after": "<plain_claim(before)>"}]}`.
   BA_US_Equity and VLO_US_Equity must be entries. The builder WRITES NOTHING to the pool and calls no model.
4. **Tests** in `lib/research/posture/tests/`: `plain_claim` on both claims above answers no token; a token-free claim is unchanged;
   the instruction and pack text the model reads carry no status token for an absent score.

## 2. BOUNDS

1. Write only the paths below. No deploy, NO STORE WRITE (ak-6 writes), NO MODEL OR VENDOR CALL, no portal write. Prose only: no
   verdict, score, citation or machine status value changes.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/posture/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~203/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ak-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/posture/ lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ak-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/checks/b_served_text.py --cell b4 --where local --plan org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~203/posture_claim_plan.json; echo "exit=$?"</invocation><expect>C0 PASS (every plan entry's before equals what the route serves now), C1 PASS (0 of BA's and VLO's served posture claims carry a status token), C2 PASS (the old claims carry it; plain_claim answers words); B4 EVERY POSTURE CLAIM STATES A MISSING SCORE IN WORDS: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~203 <0.9.0_WK_AMGT_RESAPP~203@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~203/AMGT_RESAPP.TO-AMGT-ak-5.a-missing-score-in-words.proof_of_spec.json`.
Report once: the commit hash, both criteria's output lines, the instruction and pack lines you changed, the plan's denominator and
entries, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 28264 (analysis @b74c090804, cell B4); issuer ruling R2 (no model call; the stored claims serve through
`plain_claim` by ak-6's field rewrite). DSGN AV-z-1's page guard stands until ak-6 serves.

<status>pending</status>
<round>61</round>
<slot>0.9.0_WK_AMGT_RESAPP~203</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
