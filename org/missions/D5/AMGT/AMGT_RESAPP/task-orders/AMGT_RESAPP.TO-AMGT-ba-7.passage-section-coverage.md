# AMGT_RESAPP task order -- `AMGT-ba-7` -- EACH NAME'S PASSAGE SET LISTS THE FILING SECTIONS IT COVERS AND THE SECTIONS IT DOES NOT (CTO ADDENDUM 1, ROW Z-W20-S8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~273</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a reader and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads `filings/v1/` objects in the pool the function role already reads (the segment breakdown reads the same prefix); no new read path, no write.
comp-adversary: RUN by the issuer at the cut -- over 95 covered names the newest stored source object reads: a filing read on 12, a reason on 41, no object on 42. Of the 12: both sections kept on 9, the operating review missing on 2 (ASML NA and PBR, the two names whose "segments" are not business lines), the risk factors missing on 1 (HAL); a section cut short on 8. BABA keeps 70,000 of 350,005 characters of its risk factors and 80,000 of 131,933 of its operating review. No field says any of this today.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; stored objects only.
</preflight>

**Your worktree:** `C:/tmp/r77-273` (branch `wk-AMGT_RESAPP-273`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-273`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-7` (round 77, decomposition s.85)

CTO ADDENDUM 1 (@3bad4be9e0) on row Z-W20-S8: "each name's passage set lists the sections it covers and the sections it does
not." Today a reader cannot tell that a name's filing notes rest on its risk factors alone, or on the first part of a long
section. The facts are already stored: the source object `filings/v1/<key>/<accession>.source.json` carries
`excerpt.items`, `excerpt.item_keys`, `excerpt.item_chars`, `excerpt.item_full_chars` and `excerpt.truncated_items`, and the
analysis beside it (`<accession>.analysis.json`) carries `passage_map`, each passage's `location` opening on its section.

Build a NEW module `lib/research/filings/section_coverage.py`:

- `wanted_items(form)` returns `[(key, item label), ...]`: the sections a filing of that form is read for. It must equal the
  producer's own table (`fetch.EXCERPT_ITEMS` for the keys, and the item labels `document.py` cuts by) for 10-K and 20-F.
  Hold the table in this module and prove the equality in a test; do NOT import `fetch.py` or `document.py` from the
  module. A form the producer does not cut, or `None`, returns `[]`.
- `coverage_from_source(source, passage_map=None)` returns the coverage block from ONE stored source object. It is pure:
  ```
  {"sections": [{"key", "item", "chars", "full_chars", "share", "truncated", "passages"}],
   "not_covered": [{"key", "item", "reason"}],
   "passages_outside_sections": <int or None>,
   "source": {"form", "filing_date", "accession"},
   "reason": None}
  ```
  - `sections`: one entry per kept section, in the stored order. `share` is `chars / full_chars`. `truncated` is true when the
    section was cut short. `passages` is the count of `passage_map` entries whose location opens on that section (compare
    the first part of `location`, case-folded, with the item label); `None` when no passage map is handed in.
  - `not_covered`: each wanted section the source did not keep, by key and item label, with a plain reason.
  - `passages_outside_sections`: passages under no kept section (ASML NA has one, located "TABLE"); never dropped silently.
  - A source that is missing, empty or not a read filing returns `sections: []`, `not_covered: []` and a plain `reason`.
- `read_section_coverage(security_key, pool_client, bucket)` returns the same block for a name's NEWEST stored source object,
  with the passage counts from the analysis beside it. `pool_client` is a zero-argument callable returning an S3-shaped
  client. Bounded: one listing of the name's prefix and at most two object reads. It NEVER raises: a name with no object, or a
  read that did not complete, returns the block with a plain `reason`. An optional keyword `passage_map` may skip the
  analysis read when the caller already holds it.

Rules for the module:
- Standard library only at module scope, and no import of the filing fetch, document, battery or analyze modules anywhere in
  it. The Lambda will import this module, and its package does not carry the filing fetch stack. The slash-safe key helper
  (`lib.research.identity.crosswalk.slash_safe_key`) may be imported inside the reader.
- Every reason is one plain sentence for a reader of the page.

**Tests** in `lib/research/filings/tests/test_section_coverage.py`: the wanted table equals the producer's; a two-section
source; a one-section source (the other listed as not covered); a cut-short section; a passage outside every section; a
source that is not a read filing; the reader over a planted directory client (a name with objects, a name with none, a read
that raises).

**You do NOT wire it.** `lib/research/api/scoped_amgt.py` is another cell's file (`AMGT-ba-11` adds the block to the /thesis
body). In your report, name the exact call that site needs.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W273-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. No existing file changes: not `fetch.py`, `document.py`, `passages.py`, `battery.py` or `scoped_amgt.py`. No stored object is
   rewritten and no filing is fetched again.
3. Any reason you return is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/filings/section_coverage.py
lib/research/filings/tests/test_section_coverage.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~273/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba7.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>the block equals the stored facts on 12 of 12 captured source objects; BABA lists both sections as cut short with their shares; ASML NA and PBR list the operating review as not covered and HAL the risk factors; a passage outside every section is counted; a name with no filing read serves a plain reason; C1-C8 PASS; R77 BA7 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba7.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>over the real stored objects of every covered name the reader raises on none and each name serves its sections or a plain reason; the read block equals the stored facts wherever the stored filing is the captured one; the planted absent name serves a reason; C1-C5 PASS; R77 BA7 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba7.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the wanted sections of a 10-K and a 20-F equal the producer's own table; the module is standard-library-only at module scope, reaches no fetch or document layer and is ASCII; every reason is plain words; C1-C6 PASS; R77 BA7 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~273 <0.9.0_WK_AMGT_RESAPP~273@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~273/AMGT_RESAPP.TO-AMGT-ba-7.passage-section-coverage.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- AC2's counts: names with a filing read, with a reason, with a section not covered, with a section cut short;
- the exact call the wiring site needs;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO adjudication ADDENDUM 1 @3bad4be9e0 (row Z-W20-S8, offered by the COO @fb9ca91ad5), enrichment item 10. The
block is built from facts the producer already stores; nothing is fetched or re-run. The wiring (`passage_coverage` on the
/thesis body) is ba-11's (wave 1); the page work is DSGN's. Checks dry-run at base: AC1, AC2, AC3 FAIL as expected (the module is
absent); a scratch prototype read YES on all three (the green arm): a filing read on 12 of 95, a section not covered on 3, cut
short on 8.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~273</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
