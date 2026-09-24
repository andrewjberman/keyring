# AMGT_RESAPP task order -- `AMGT-rl-5` -- PEERS: the five columns that exist, the twelve that do not behind one disclosure, the basis as a chip with its test one hover away

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rl-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~134</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the L1 brief at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. react-dom/server harnesses only; no browser, no HTTP, no vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~134`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`test -f portal/scripts/ui-class-census.mjs && echo INSTRUMENT-OK`, and **`git -C portal log -1 --format=%h` must print
`c657eb91` or a descendant of it** (`git -C portal merge-base --is-ancestor c657eb91 HEAD && echo PEERS-BASE-OK`) -- your
portal is based on the Peers closer branch, which carries the five-column carry (`1ec5446c`) and the READ_FAILED harness
(`c657eb91`). Absent = BLOCKING row, stop. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~134;`.
**NEVER RUN AN INSTALL. No vite dev server on this cell.** Never push, merge, rebase, `checkout --` or `clean`. **Portal is
a NESTED repository at `<worktree>/portal`:** portal files are committed inside it
(`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~134 <0.9.0_WK_AMGT_RESAPP~134@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts and logs under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~134/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rl-5` (round 37, decomposition s.45)

**`FWD-25`:** *"the table renders the PRESENT columns only; an 'Absent columns (N)' disclosure lists each with its registry
reason; the basis is a status chip with the test statement one hover away. ACCEPT: A PM reads five real columns instead of
scanning twelve that say ABSENT. TODAY: 17 columns, 12 ABSENT in all 18 rows, under a 696-char paragraph."*

**The target (brief Part V, Peers):** ONE white panel (`Panel variant="nested"`). Basis as a chip ("derived" /
"analyst-entered"; navy outline, 2px radius, label size -- build it LOCAL, `src/ui/components/StatusBadge.tsx` is a dark
idiom and is not used) with the ranker's test statement (the 696-character derivation reason) in a `HelperTip`
(`@/components/HelperTip`, read-only import); comparable count, universe vintage and as-of as the panel subtitle. A
heatmap-style table (numeral 14px/400 tabular, right-aligned figures, a sign on every change value) over the PRESENT
columns ONLY (`PRESENT_CARRIED` and `PRESENT_NOT_CARRIED`), the subject row bold, the summary rows on a sunken `#E8EBF0`
fill (C3 sunken). A present-not-carried cell renders an em-dash with the reason in the column head's tooltip. Below the
table an "Absent columns (N)" disclosure (`<details>`), collapsed by default, listing each ABSENT column with its registry
reason at footnote size (11px). The counts line stays ("5 present / 12 absent of 17 declared; 5 column(s) carry ...") at
footnote size. The `(read READ_FAILED)` / `(read ABSENT)` distinction is KEPT verbatim on the absent-basis branch.

## 2. BOUNDS

1. **Files:** `tabs/PeersTab.tsx`, `cscTable.ts`, `__harness__/peersCarry.harness.cjs` and `__harness__/peersReadFailed.harness.cjs`
   (yours; keep both PASS), and the NEW `__harness__/peersPattern.harness.cjs`. Everything else in the page directory is
   another cell's this round; `src/ui/**`, `src/components/**`, `src/api/**` read-only. `IdentityLine` is being inverted
   by another cell in parallel -- render it unchanged.
2. **`cscTable.ts`'s computed shape is KEPT:** `buildCscTable` still returns every column with its state and reason, the
   carried count, the summary rows with their denominators (`n=12`) and the P/E (NTM) / P/E (trailing) labels under the R-1
   `display_label` at NTM grain (rk-14). The table RENDERS a subset; the model still names all seventeen -- that is what
   the disclosure reads from.
3. **The contract is `portal/DESIGN.md` C1-C12** as in every cell this round; the four designed states for
   empty/loading/error/no-permission (C12).
4. **KEPT:** the identity line, the three-state reads, the Peers/Posture symmetry (`usePeerSet` unchanged), R-1 served whole.
   **No route, DTO, query key or figure moves.**
5. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue.**

## 3. THE HARNESS YOU ADD -- `__harness__/peersPattern.harness.cjs`

Same loader as `peersCarry.harness.cjs` (actual `PeersTab` + `PostureTab`, installed typescript, `react-dom/server`, hooks
stubbed with the carry harness's `sample` object -- 5 present codes, 12 absent, 12 members -- and with a READ_FAILED
object). Prints `CHECK <name> <value> (expected <value>)` per line and `CHECKS-OK n of n`; expected counts READ OFF THE
OBJECT: `panel_is_light` · `table_columns_rendered` == present columns (5) · `absent_columns_in_table` == 0 ·
`absent_disclosure_count` == 12 and its label reads "Absent columns (12)" · `absent_reasons_listed` == 12 ·
`basis_chip_text` == "derived" · `helper_tip_carries_test_statement` (the derivation reason text is in the markup, not in
the visible paragraph) · `subject_row_bold` · `summary_rows_sunken` (the summary `<tr>` carry the sunken fill class) ·
`not_carried_em_dash` (each PRESENT_NOT_CARRIED cell renders an em-dash and the column head carries the reason) ·
`counts_line_present` · `read_failed_distinct` (the READ_FAILED render says "(read READ_FAILED)" and differs from the ABSENT
render) · `posture_calls_subject_then_comparable` (the Posture render still calls `usePeerSet` twice, subject then comparable).

## 4. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/cscTable.ts
portal/src/pages/SecurityAnalysis/__harness__/peersCarry.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersReadFailed.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BA_US_Equity.json
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx
portal/src/components/HelperTip.tsx
portal/scripts/ui-class-census.mjs
portal/DESIGN.md
portal/src/ui/components/states/index.ts
portal/src/ui/components/panels/Panel.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~134/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

Of these you WRITE only the first five; `PostureTab.tsx` is ANOTHER cell's file and is read-only here (your harness renders it
to prove the symmetry).

## 5. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rl-5"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/peersPattern.harness.cjs</invocation><expect>THE BUILT BEHAVIOUR: CHECKS-OK 13 of 13 with every CHECK line printed beside its object-derived expected value -- panel_is_light true, table_columns_rendered 5, absent_columns_in_table 0, absent_disclosure_count 12, absent_reasons_listed 12, basis_chip_text derived, helper_tip_carries_test_statement true, subject_row_bold true, summary_rows_sunken true, not_carried_em_dash true, counts_line_present true, read_failed_distinct true, posture_calls_subject_then_comparable true</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rl-5"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis/tabs/PeersTab.tsx src/pages/SecurityAnalysis/cscTable.ts</invocation><expect>THE INVERSION IS COMPLETE ON YOUR FILES: FILES 2 TOTAL 0, both lines idiom=0 size=0 weight=0 radius=0 shadow=0 (the walk counted 24 in PeersTab before this cell; a non-zero FAILS)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rl-5"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/peersCarry.harness.cjs &amp;&amp; node src/pages/SecurityAnalysis/__harness__/peersReadFailed.harness.cjs</invocation><expect>THE CARRY AND THE READ_FAILED CONTROLS STILL PASS: peersCarry prints {"result":"PASS",...} with fixture_cases 6 (the five present codes carried at n=12 and the NTM-grain labels unchanged) and peersReadFailed prints {"result":"PASS",...} -- both PASSED on the closer branch before this cell; a regression FAILS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~134/AMGT_RESAPP.TO-AMGT-rl-5.peers-present-columns.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
portal commit hash and its parent (must be `c657eb91` or its descendant), the outer commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

# pipeline-override: LIMB 6 only -- the BRIEF half reads STALE at 8da812bf80 (owed by 4.0.0_SA_CRO~Z, asked 05:59Z); R-10 (Andrew-direct 2026-09-23 ~21:2xZ, 'agreed with your rec': the L4-R signature is not a BAR for AMGT, the review is kept) + ADDENDUM B B.6 + 1.0.0_SA_CTO~Z msg 25282 (3) 'no round is held on it'; the review stays owed and is not skipped. The PRD_HEADER key refusal is CLEARED at 8da812bf80; coverage is NOTED at EXECUTING (enrichment recut).

**ISSUER NOTES:** wave 1, spawned after rl-1 merges, the ONE cell whose portal worktree is provisioned with
`--portal-ref c657eb91` (the closer branch's nested portal), because its files already moved there (`1ec5446c`,
`c657eb91`) and a cut off DEV `c1ac41ec` would re-diverge them. At the drain this branch's portal merges into the same
line as the closer branch; MSTR's integration of the closer branch to CLOUD/DEV precedes or accompanies it.

<status>pending</status>
<round>37</round>
<slot>~134</slot>
<fabric>site-z</fabric>
