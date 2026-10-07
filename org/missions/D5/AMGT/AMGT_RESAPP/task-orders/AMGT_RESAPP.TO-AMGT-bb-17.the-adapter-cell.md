# AMGT_RESAPP task order -- `AMGT-bb-17` -- THE ADAPTER CELL: EVERY HOOKUP OF THE ROUND IN THE ONE SERVED MODULE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-17</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~302</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_D_NOTES.md) -- At the base H1 to H5 fail (no hookup made) and H6 reads 2 wrong rows of 60; the round-77 served shape reads YES. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-302` (branch `wk-AMGT_RESAPP-302`, cut by the issuer AFTER bb-2, bb-3, bb-8, bb-9, bb-10 and bb-11 drain, from the drained tree, with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-302`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-17` (round 78, decomposition s.86)

Six cells of this round each built a new module and named a hookup. You make every hookup. You are the ONLY writer of
`lib/research/api/scoped_amgt.py` this round. Each module is already merged into your worktree's base: read each module and
its tests before you call it. Each hookup below gives the function, the place by line number as measured at the cut, and the
effect; line numbers may have moved by a few lines, so find the named function.

1. **The coverage marker** (`lib/research/api/coverage_marker.py`, `marker(security_key, covered_keys)`). Where the overlay
   bundle and the thesis bundle are assembled (near `:3467` and `:3629`), add the key `research_coverage` holding the marker for
   the requested company, with `covered_keys` from `covered_security_keys()` as the adapter already reads it. A company outside
   the covered set then says so in ONE place.
2. **The country** (`lib/research/api/country_name.py`, `with_plain_country(header_figures)`). In `read_security_overlay`
   (near `:3472`) and `read_thesis_bundle` (near `:3632`), serve `"header_figures": country_name.with_plain_country(header_figures)`
   AFTER the figure checks have been computed from the stored list, so no check result moves.
3. **The one statement of inputs** (`lib/research/api/inputs_statement.py`, `statement(input_provenance, thesis)`). In
   `read_thesis_bundle`, after `passage_coverage` is set (near `:3700`), set
   `bundle["input_provenance"] = inputs_statement.statement(_overlay_input_provenance(resolved_key), bundle)`. On the overlay
   (near `:3495`) serve the SAME statement under the same key; the overlay does not hold the thesis parts, so pass `None` for
   `thesis` there ONLY if reading the thesis would add a store read to the overlay's first paint, and say in your report which
   you did and what it costs. Do not remove the `/ledger` route or the overlay's `provenance` block.
4. **The officer rank** (`lib/research/management/officer_rank.py`, `rank_officers(officers)`). At the top of
   `_serve_management_document` (near `:4553`), the one place every served roster passes:
   `officers = officer_rank.rank_officers(officers)`. Same rows, reordered; every count on the block is unchanged.
5. **The source names** (`lib/research/api/source_names.py`). `read_feed`: pass `items` through `with_publisher_names` and add a
   `source_name` beside `source` (near `:5316` and `:5346`). `_overlay_provenance`: a `source_name` on each of its three entries
   (near `:3290`). `_compose_ledger_provenance`: a `source_name` on the News class and on a Filings class that has a source
   (near `:6015` and `:6026`). Each is ADDED beside the raw text; the raw `source` values do not change.
6. **The peer price's own listing** (`lib/research/peers/price_listing.py`, `record_for_price(member, resolve)`). In
   `_with_price_currency` (near `:2371`), the record asked for a row's currency becomes
   `price_listing.record_for_price(m, _resolve_held_form)["record_key"]` in place of `price_currency.member_record_key(m)`. A row
   whose answer carries a `reason` is served `price_currency_reason` equal to that reason and NO `price_currency`.

NOT in this cell, and not to be wired by you: the segment table (`segment_table.py`), the segment period labels
(`segment_period.py`), the Seeking Alpha record reader (`collector_record.py`), the slash-safe officers reader (it needs no
hookup) and the Peers V reason (it needs none). Their serving waits on rulings outside this cell.

Run `lib/research/api/tests/` before your commit and report its last line.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W302-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. You are the ONLY writer of `lib/research/api/scoped_amgt.py` this round. Edit no module another cell built: if one is wrong, file a row and say so in your report.
3. The segment table, the segment period labels and the Seeking Alpha record reader are NOT wired by this cell.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~302/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-17"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb17.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>a covered name reads covered and a pool name outside coverage says so once; the country reads in plain case with the stored text beside it; the thesis carries one statement of inputs with one filings row before the pack row; a chief-executive row leads every sampled roster that holds one; every provenance entry carries a source name key; no sampled peer row is served a United States record's currency behind a foreign price; H1-H6 PASS; R78 BB17 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-17"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb17.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>the round-77 served shape still reads YES on the tree; B1 PASS; R78 BB17 AC2 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~302 <0.9.0_WK_AMGT_RESAPP~302@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~302/AMGT_RESAPP.TO-AMGT-bb-17.the-adapter-cell.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-77 analysis enrichment list; CTO rulings file @f97be3fd6f. WAVE 1: cut from the drain of bb-2, bb-3, bb-8, bb-9, bb-10, bb-11. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_D_NOTES.md` (cell D2), committed in the issuance commit's parent. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes.

<status>staged</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~302</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-07 ~17:0xZ):** all sixteen wave-0 cells are drained; the six modules you hook up are on the tree your worktree is cut from (`C:/tmp/r78-302`). Gate limb: GATE (viii) on a modify (`<placeholders>` NONE).

<status>pending</status>
