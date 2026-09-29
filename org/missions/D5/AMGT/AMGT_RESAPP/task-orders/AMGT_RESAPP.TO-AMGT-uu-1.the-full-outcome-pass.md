# AMGT_RESAPP task order -- `AMGT-uu-1` -- ROUND 46: one evidence row per outcome, FWD-1..FWD-31, measured on the served state after round 46's redeploy, and the Base-case basis table

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-uu-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~167</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only evidence pass.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads and read-only invokes of the deployed opal-amgt-scoped-api only.
comp-adversary: RUN by the issuer at the cut -- the adversarial arm is the fence read as written: AC2 requires every fence quote VERBATIM in the PRD, so a paraphrased clause (the round's classic silent redirect) fails; the judgment criterion puts each Base-case input's BASIS beside its ratio, which the ratio band alone cannot show.
EGRESS CLASS, declared: NONE beyond reads of Opal-owned surfaces (S3 GET/LIST, lambda:Invoke of GET routes). No vendor, no write.
</preflight>

## 1. THE CELL -- `AMGT-uu-1`

**Where this came from.** The PRD `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` declares 31 outcomes, FWD-1..FWD-31
(its `endpoint_outcomes` header list, from `:11`). Each has a fence with a `DONE WHEN` clause, and several carry dated ADDENDA
and CORRECTIONS beneath them that bind how the fence is read (read every addendum under an outcome before measuring it). The
project has never had a full pass. Your worktree is cut AFTER this round's redeploy (uu-4), so the source you read and the served
state you measure are the same vintage.

**Build two files in your deliverables, nothing else:**
- `FWD_EVIDENCE_ROUND46.json`: `{"prd": "<path>@<commit>", "run_at": "<UTC>", "code_sha256": "<the deployed CodeSha256 you
  read>", "outcomes": [ ... 31 rows ... ]}`, each row `{"id": "FWD-<n>", "fence_quote": "<the DONE WHEN clause, VERBATIM from
  the PRD>", "instrument": "<the exact command or read you ran>", "output_excerpt": "<the lines that answer the clause>",
  "state": "met" | "unmet" | "unmeasurable", "reason": "<required when unmeasurable>", "notes": "<name any addendum applied>"}`.
- `BASE_CASE_BASIS.json`: `{"read_at": "<UTC>", "code_sha256": "...", "served_base_served_count": <M>, "rows": [...]}`, ONE row
  per live-library name whose SERVED `/thesis` `model.cases.base.status` is `SERVED`, each `{"security_key", "consensus_eps",
  "consensus_eps_basis", "trailing_median_pe", "trailing_median_pe_basis", "window", "base_value", "px_last",
  "ratio_to_px_last", "currency"}` copied from the served object (the basis fields as served, never re-worded), `M` the count of
  such names on your read. Plus a `.md` twin of each file as a readable table.

**How to measure.** The served plane: one read-only invoke per route of the deployed `opal-amgt-scoped-api` (the helper
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~158/capture_lib.py` `_invoke` / `capture`), S3 reads,
git reads, and `lib/research/api/scoped_amgt.py` called as a library. The population is the LIVE research library
(`lib.research.corpus.library.list_folders(library.library_root())`, keys via `lib.research.identity.crosswalk.harvester_key` +
`scoped_amgt.resolve_identity`); print its denominator and read time. The page: the portal's own node harnesses under
`portal/src/pages/SecurityAnalysis/__harness__/` rendering a served capture (`exportCompare.harness.cjs`, `tabs.harness.cjs`),
which render static markup; NO dev server, NO browser. A fence whose clause needs a live browser (hover, focus, computed
colour, layout) and that no harness answers is `unmeasurable`, with that reason. `state` is YOUR measurement of the clause as
written, not a grade of the outcome. FWD-12 limb 3 / FWD-24: the team's cited cases are known heading-only (row Z-S293) --
measure and say so, do not re-derive it.

## 2. BOUNDS

- NO write anywhere but your four files (and a channel row if you file one). NO vendor call, NO S3 write, NO deploy, NO dev
  server, NO `--write`/`fire`/`pull`. Pure ASCII. Scratch outside the repository.
- REFUSE a criterion you cannot satisfy as written, with your measurement.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~167/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-uu-1.the-full-outcome-pass.md
</paths>

READ-ONLY: the whole repository and every S3 object.

## 4. PROOF OF SPEC (each invocation LITERAL, timeout 120; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-uu-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-1.AC1.sh</invocation><expect>(?m)^VALID$</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-uu-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-1.AC2.sh</invocation><expect>fence_quotes_verbatim 31 of 31</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-uu-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-1.AC3.sh</invocation><expect>(?m)^paths_outside_grant 0$</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-uu-1" judgment="true"/>
</proof_of_spec>

- AC1 the files' shape: 31 of 31 outcomes, every row complete, unmeasurable rows with a reason; every basis row complete and
  their count equal to `served_base_served_count`. AC2 every fence quote verbatim in the PRD. AC3 the bound.
- AC4 (JUDGMENT, the CVO's at L9; record it UNVERIFIABLE-BY-INSTRUMENT, no verdict): read `BASE_CASE_BASIS.md` -- for each served
  Base case, do both inputs name the adjusted basis, and does the value read as a plausible price beside `px_last`?

## 5. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~167/AMGT_RESAPP.TO-AMGT-uu-1.the-full-outcome-pass.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes; commit the files you changed plus the instance.
4. Report ONCE: the count of met / unmet / unmeasurable, by id, and M.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-45 analysis s.4 item 1 (model `AMGT_CORPUS.TO-CRPS-i-5`). Issued with the round, SPAWNED only after
uu-4's served verification (decomposition s.54e), its worktree cut from CLOUD at that moment. Base: AC1/AC2 FAIL (MISSING file),
AC3 PASS (bound). No dev server: port 5174 is Andrew's walk build (record @c027b4726f); the issuer's real run at close is on it.

<status>complete</status>
<round>46</round>
<slot>~167</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
