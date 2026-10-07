# AMGT_RESAPP task order -- `AMGT-ba-6` -- A SHARE-CAPITAL TABLE, AND A TABLE UNDER ONE REPEATED LABEL, IS REFUSED AS A DRIVER CHART OR A SEGMENT BREAKDOWN (CTO RULING 7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~272</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a pure rule and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- AC3 reads the deployed /thesis route the way the round's other checks do (a GET-shaped invoke); no new read path, no write.
comp-adversary: RUN by the issuer at the cut -- on deployed OVpDhfwD, over 95 covered names: a filing driver chart is served on 2 (BA, ASML NA) and a segment breakdown on 12. ASML NA's driver is "Issued ordinary shares outstanding", unit "number of shares", and its 5 "segments" are share-capital items. PBR's 8 rows are all headed "Other". A prototype of the rule refused exactly those: driver 1 of 2, segments 2 of 12.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; no producer re-run.
</preflight>

**Your worktree:** `C:/tmp/r77-272` (branch `wk-AMGT_RESAPP-272`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-272`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-6` (round 77, decomposition s.85)

CTO ruling 7 (round-76 analysis @c8bbeeac10): "A share-capital or equity-structure table, and a table whose rows carry one
repeated label, is REFUSED as a driver or a segment breakdown. The name then reads its reason. A wrong chart is worse than an
absent one." The specimens: ASML NA serves its share capital as both the driver chart and the segments; PBR's segment rows
are all headed "Other".

Build ONE rule, in a NEW module `lib/research/filings/table_class.py`, as two pure functions:

- `driver_refusal(thesis_driver, passage_text=None)` returns a plain reason, or `None` when the driver is kept.
  - `thesis_driver` is the stored driver object: `{series, unit, why, resolution, points, ...}`. `passage_text` is the text
    of the passage its first point cites, when the caller has it.
  - REFUSED: a driver whose series or unit is a count or description of the company's own shares or capital structure
    (issued or outstanding shares, share capital, treasury shares, nominal or par value, holders and holdings).
  - KEPT: every other driver. A missing or empty driver is not a refusal (`None`).
- `segment_refusal(rows)` returns a plain reason, or `None` when the rows are kept.
  - `rows` is the served list `[{segment, text, cite, ...}]`.
  - REFUSED, class one: half or more of the rows describe share capital or equity structure, by their label or the opening
    of their sentence.
  - REFUSED, class two: two or more rows that all carry ONE label (any label, "Other" included).
  - KEPT: everything else. One row alone is not a repeated label. No rows is not a refusal.
- The two segment classes give DIFFERENT reasons, so a reader can tell them apart. Each reason is one plain sentence for a
  reader of the page: what the kept filing text is about, and that no chart or no breakdown is shown.

Rules for the module:
- It names a CLASS, never a company: no ticker, company name or security key in the code, and neither function takes one.
- Standard library only at module scope, and no import of the filing fetch, document, battery or analyze modules anywhere in
  it. The Lambda will import this module, and its package does not carry the filing fetch stack.
- It reads only what it is handed. No store read, no network.

**Plant tests** in `lib/research/filings/tests/test_table_class.py`: each class refused, each control kept (a two-label
breakdown, a units driver, one row, no rows, a missing driver), and the reasons plain.

**You do NOT wire it.** `lib/research/api/scoped_amgt.py` is another cell's file (`AMGT-ba-11` adds the two calls and the
served `plain_reason`). No stored object is rewritten and no producer is re-run: the rule is applied where the chart and the
breakdown are produced for the page. In your report, name the exact call each site needs.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W272-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. No existing file changes: not `scoped_amgt.py`, not `segment_labels.py`, not `analyze.py` or `drafting_build.py`.
3. Any reason you return is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/filings/table_class.py
lib/research/filings/tests/test_table_class.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~272/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba6.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>on the captured deployed bytes the share-count driver and the share-capital and one-label breakdowns are refused, the BA and BABA business tables are kept, and the planted tables decide each class; C1-C15 PASS; R77 BA6 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba6.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>every reason is plain words and the two segment reasons differ; the module is standard-library-only at module scope, reaches no fetch stack, names no company and is ASCII; C1-C6 PASS; R77 BA6 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba6.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>over the deployed /thesis of every covered name the rule raises on none, refuses ASML NA's driver and the ASML NA and PBR breakdowns, keeps BA, BABA and HD, and refuses fewer than half of the served breakdowns; the refused names are printed; C1-C7 PASS; R77 BA6 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~272 <0.9.0_WK_AMGT_RESAPP~272@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~272/AMGT_RESAPP.TO-AMGT-ba-6.share-capital-and-one-label-refusal.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- AC3's counts: charts and breakdowns served, refused, and every refused name with its reason;
- the exact call each of the two wiring sites needs;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-76 analysis ruling 7, enrichment item 5. "At the producer" is read as the point the chart and the
breakdown are produced for the page (`thesis_driver_chart`, `read_segment_breakdown`): the stored driver and segment findings
come from the model stage, which is not re-run (Andrew's standing no-fleet-rerun word), so a write-time refusal there would
move no served name. The wiring is ba-11's (wave 1). The BA "one heading per segment" item is page work and sits in ba-5.
Checks dry-run at base: AC1, AC2, AC3 FAIL as expected (the module is absent); a scratch prototype read YES on all three
(the green arm), refusing driver 1 of 2 and segments 2 of 12.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~272</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
