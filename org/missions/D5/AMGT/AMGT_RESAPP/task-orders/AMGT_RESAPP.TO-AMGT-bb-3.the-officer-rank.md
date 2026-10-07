# AMGT_RESAPP task order -- `AMGT-bb-3` -- THE OFFICER RANK: CHIEF EXECUTIVE, THEN CHIEF FINANCIAL OFFICER, THEN THE LIST AS SERVED (RULING 9)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~291</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_A_NOTES.md) -- A chief-executive row is present and not first in 17 of 93 served rosters; 3 stored lists carry no chief-executive title. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-291` (branch `wk-AMGT_RESAPP-291`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-291`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-3` (round 78, decomposition s.86)

Build the officer rank as a NEW module, `lib/research/management/officer_rank.py`, with two PURE functions (no store read, no
network, no import beyond `re`):

- `title_rank(title)` returns 0 for the company's chief executive, 1 for its chief financial officer, 2 for anyone else
  (including None, an empty title and a non-string).
- `rank_officers(officers, title_field="role")` returns a NEW list holding the SAME row objects: every rank-0 row, then every
  rank-1 row, then the rest, each group in the order given. It never drops, copies, edits or adds a row, never changes the
  input list, and ranking a ranked list changes nothing.

The rule reads the title text only. Titles come in two shapes: Bloomberg's ("President/CEO:Group/Rep Exec Officer", roles
joined by `/`, a unit after `:`) and a filing's prose ("Executive Vice President; President and Chief Executive Officer of
Boeing Defense, Space & Security").

1. Split the title on `/` and `;`. Judge each piece alone; the title has the rank of its best piece.
2. In a piece, text after a `:` names a unit. A piece with a `:` counts only when what follows is empty or is "Group",
   "Company" or "Corporation". Look for the role only in the text BEFORE the `:`.
3. A chief-executive mention is "CEO", "Co-CEO", "Chief Executive", "Chief Executive Officer", "Co-Chief Executive Officer"
   (any case, whole words). A chief-financial mention is "CFO", "Chief Financial Officer", "Chief Finance Officer", or
   "Chief Financial and <one word> Officer".
4. A mention counts only when what stands directly before it in the piece is nothing, a comma, or one of: and, &, Group,
   Global, Interim, Acting, Rotating, our. So "Deputy CEO", "Regional Chief Executive", "Brazil Chief Executive Officer",
   "US CEO", "Special Advisor to the CEO" and "Dpty CFO" do not count.
5. A mention does not count when it is followed by "of <a unit>" (but "of the Company", "of the Group" and "of the
   Corporation" are fine), or by a comma and then a unit's name. After a comma these openings are NOT a unit: and, a member,
   member, President, Chair..., Director, Founder, Co-Founder, Chief, Executive, Managing, Secretary, Treasurer.
6. Rank 0 wins over rank 1 when a title earns both.

Worked examples, all real titles. Rank 0: "Chairman/CEO", "President/CEO:Group", "Co-Chairman/Co-President/Co-CEO",
"Interim CEO & Mng Dir", "Vice Chairman/CEO", "Chairman of the Board, Chief Executive Officer and President", "President and
Chief Executive Officer, and a member of the Board". Rank 1: "Exec VP/CFO/Interim Controller", "Sr VP:Finance/CFO", "Senior
Managing Corporate Executive Offi/CFO:Group", "Executive Vice President and Chief Financial Officer". Rank 2: "Chairman",
"President", "Exec VP/CEO:Europe", "Chairman & CEO:BNP Paribas Fortis", "Head:Chief Executive Office Strategy & Sustainabil",
"Chief Executive Officer, Alibaba E-commerce Business Group", "CFO:EMEA", "Deputy CFO".

Plant tests in `lib/research/management/tests/test_officer_rank.py`: both title shapes, each exclusion, co-chiefs kept in
order, a roster with no chief executive left as given, the empty list, a missing title, `title_field="title"`.

**You do NOT edit `lib/research/api/scoped_amgt.py`, `lib/research/management/exec_roster_chain.py` or
`lib/research/management/bloomberg_fallback.py`.** The hookup is the adapter cell's. Name it in your report:
`officers = officer_rank.rank_officers(officers)` at the top of `scoped_amgt._serve_management_document`
(`scoped_amgt.py:4553`), the one place every served roster passes (a stored management object and the request-time
chain's filing or Bloomberg roster alike). It returns the same rows reordered, so every count on that block is unchanged.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W291-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited: the round's adapter cell, AMGT-bb-17, makes every hookup. Name yours in your report.
3. A list with no chief-executive title is left in the order it was served.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/management/officer_rank.py
lib/research/management/tests/test_officer_rank.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~291/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb3.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>every labelled title reads its rank (69 of 69); a roster in Boeing's filing order comes back chief executive, chief financial officer, then as given; the function is stable and safe; C1-C3 PASS; R78 BB3 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb3.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>every stored Bloomberg officer list is ranked without losing or misordering a row (N of N); NKE US opens with "President/CEO" then its CFO; C1-C2 PASS; R78 BB3 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb3.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>every plant case in test_officer_rank.py passes; R78 BB3 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~291 <0.9.0_WK_AMGT_RESAPP~291@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~291/AMGT_RESAPP.TO-AMGT-bb-3.the-officer-rank.proof_of_spec.json`.
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

**ISSUER NOTES:** CTO round-77 ruling 9. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_A_NOTES.md` (cell A2), committed @643863854d before the cut. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~291</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @357436b20d; proof VALID rc=0 on the worker's checker; every criterion re-run by the issuer on the shared tree reads SERVED: YES; served only after the adapter cell bb-17</status>
