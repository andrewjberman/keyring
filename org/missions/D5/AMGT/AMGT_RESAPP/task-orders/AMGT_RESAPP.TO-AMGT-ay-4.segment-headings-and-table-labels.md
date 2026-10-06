# AMGT_RESAPP task order -- `AMGT-ay-4` -- SEGMENT ROWS HEADED BY THE SEGMENT'S OWN NAME; TABLE PASSAGES SERVED WITH THEIR ROW AND COLUMN LABELS (CTO RULING 6)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ay-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~260</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- the same stored filing analyses and drafting records the route already reads.
comp-adversary: RUN by the issuer at the cut -- on deployed 0MZWPl7n, BA's 11 segment rows carry 9 headings including "ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS" (x2), "BCA" beside "Commercial Airplanes", and "BGS total backlog of $29,720 million at December 31, 2025"; BA's 3 driver-chart passages are flattened number runs (54-81% numeric tokens) with no labels. r75 c61 base: see the issuance commit.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r75-260` (branch `wk-AMGT_RESAPP-260`, cut from the issuance commit with `--portal-ref 4ca437eb`, the portal DEV head at the cut (the api suite reads a portal fixture)). Work and commit only there. Start every shell call with `cd /c/tmp/r75-260`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ay-4` (round 75, decomposition s.83)

CTO ruling 6 (from the CTO's DSGN 43+44 review @0c9b9db840).
1. **Segment headings.** `_segment_rows` (`lib/research/api/scoped_amgt.py`, called by `read_segment_breakdown` ~`:3691`) serves the
   stored filing analysis's segment findings. Each row's `segment` must be the segment's own name, ONE segment per heading:
   - a filing-section heading ("ITEM 7...") takes the segment the sentence is about;
   - an abbreviation the filing defines (BCA = Commercial Airplanes, BDS = Defense, Space & Security, BGS = Global Services on BA) takes
     the segment's full name;
   - a sentence used as a heading takes its segment's name.
   Read the mapping from the stored filing text; do not hand-type one per company. A row whose segment cannot be named from stored text
   is served under a plain "Other" heading with a reason, never dropped.
2. **Table passages.** `_point_passage` (~`:3743`) serves `passage_text`. Where the passage is a table run (half or more of its tokens
   numeric), also serve `passage_table: {"columns": [...], "rows": [{"label", "values": [...]}]}` recovered from the stored
   drafting or filing records.
   - If the labels cannot be recovered from stored bytes, serve `passage_table: null` with a plain `passage_table_reason`, and file a
     row naming how many.
   - No SEC or vendor fetch.
3. **Write only** `_segment_rows`, `_point_passage` and new helper modules under `lib/research/api/`. The /freshness functions in
   `scoped_amgt.py` belong to ay-2; do not edit them.
4. **Plant tests** in `lib/research/api/tests/test_segment_labels.py`.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W260-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. No served figure or sentence changes; only headings and the added table labels.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/segment_labels.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~260/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ay-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell c61 --where local; echo "exit=$?"</invocation><expect>0 filing-section or figure headings across the covered names, BA's headings 3 or fewer segment names, and every table passage labelled; C1 and C2 PASS; R75 C61 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ay-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_segment_labels.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~260 <0.9.0_WK_AMGT_RESAPP~260@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~260/AMGT_RESAPP.TO-AMGT-ay-4.segment-headings-and-table-labels.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- BA's headings before/after; table passages labelled n of N;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-74 analysis item 5, ruling 6. Served by ay-5. Shares scoped_amgt.py with ay-2 (disjoint functions; issuer ruling at the cut).

<status>pending</status>
<round>75</round>
<slot>0.9.0_WK_AMGT_RESAPP~260</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
