# AMGT_RESAPP task order -- `AMGT-ff-2` -- THE PEERS TABLE'S CAP HEADING NAMES THE CODES ITS FIGURES CARRY, AND THE TICKER CELL SAYS "NO TICKER HELD" INSTEAD OF A COMPANY NAME (PORTAL DEV CANDIDATE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ff-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~388</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ff-2.the-peers-cap-heading-names-its-codes-and-the-ticker-cell-says-no-ticker-held</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two functions of one module, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS; the check renders statically over a captured payload.
comp-adversary: RUN at the cut -- r94_peers_units.cjs FAILs H1 and T1 at the base and PASSes H2, T2, T3, and PASSes 5 of 5 against a throwaway cscTable candidate (nothing written to the tree); the stock peers harness (13 of 13), the tabs harness (21 of 21) and the peersCarry harness still pass with the candidate. Read 2026-10-11: 68 of 243 subjects carry at least one member whose Ticker cell would print a company name (361 member rows); the CVO's browser walk (C-S67) read 'Mkt Cap (local)' over USD peer values. Security Analysis is an Opal-internal (staff-only) page.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-388` (branch `wk-AMGT_RESAPP-388`, cut from the issuance commit; its nested portal worktree is `C:/dev/wk-resapp-388/portal`, branch `wk-AMGT_RESAPP-388-portal`, cut from portal DEV 00989b8b). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-388` (or the portal path named below); a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-ff-2` (round 94, decomposition s.102)

CTO~DELL1 round-93 analysis items 2 and 3 (the CVO's two unasked notes, C-S67), both in one module because both are functions of
`portal/src/pages/SecurityAnalysis/cscTable.ts`. In the PORTAL repository, in the nested worktree `C:/dev/wk-resapp-388/portal` on a branch
`wk-AMGT_RESAPP-388-portal` cut from `DEV`:

1. **`columnHeading(displayLabel, codes)`** (a money column's heading). It drops the served label's trailing parenthetical, then appends `(<code>)` only when every
   figure carries ONE code, else `(local)`: the Mkt Cap column of ASML (subject EUR, peers USD) reads "Mkt Cap (local)" over cells that print USD. The heading
   must NAME what its figures carry: the DISTINCT non-empty codes, sorted, joined with a comma and a space (`Mkt Cap (EUR, USD)`); when some figures carry no
   code, add `, not stated` after the codes (`(USD, not stated)`); when NO figure carries a code, `(currency not stated)`. One code stays `(USD)` as today. The
   word "local" is not printed.
2. **`memberTicker(member)`** (the Ticker cell). A MEASURED identity with a security key prints the key in house form: unchanged. Otherwise, today, when the served
   `ticker` is empty, all digits or SEDOL-shaped, the COMPANY NAME prints, which puts a name in a ticker column (Tencent, SK hynix, Samsung, Novo Nordisk). It
   must print the explicit words `no ticker held` there (the Name cell of the row already carries the name); any other served ticker prints as it is. Return type
   stays `string | null`.

Nothing else moves: no other function of the module, no component, token or served field. The exported names and signatures stay. ASCII only.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W388-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only, nested worktree `C:/dev/wk-resapp-388/portal`, branch `wk-AMGT_RESAPP-388-portal` from `DEV`; never push; never touch `PROD`.
2. Edit `cscTable.ts` only; no other file, no new file in the portal.
3. No deploy, no store write, no AWS call, no network. `bun install` is NOT allowed (the worktree's `node_modules` is a link to the main tree's).
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/cscTable.ts
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~388/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ff-2"><invocation>cd C:/dev/wk-resapp-388/portal &amp;&amp; node ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_peers_units.cjs; echo "exit=$?"</invocation><expect>run in the PORTAL worktree, PASS H1, PASS H2, PASS T1 (4 rows read, none wrong), PASS T2, PASS T3; arms passed 5 of 5; R94 PEERS UNITS: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ff-2"><invocation>cd C:/dev/wk-resapp-388/portal &amp;&amp; node src/pages/SecurityAnalysis/__harness__/peersPattern.harness.cjs &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs; echo "exit=$?"</invocation><expect>the stock harnesses still read CHECKS-OK 13 of 13 and CHECKS-OK 21 of 21 (the control: nothing else on the page moved); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ff-2"><invocation>cd C:/dev/wk-resapp-388/portal &amp;&amp; bun run typecheck; echo "exit=$?"</invocation><expect>the portal typechecks (tsc -b) with 0 errors; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~388 <0.9.0_WK_AMGT_RESAPP~388@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~388/AMGT_RESAPP.TO-AMGT-ff-2.the-peers-cap-heading-names-its-codes-and-the-ticker-cell-says-no-ticker-held.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash (and the portal branch and commit hash);
- every criterion's output lines;
- the diff of each edited product file, in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-93 analysis @bfa6b04c8c items 2 and 3: "The cap header names the unit its values carry (or the values are converted, ONLY where a rate the page already serves states it)"; "The Ticker cell serves the identity's ticker or an explicit 'no ticker held'. It is a portal or API cell, whichever owns the field. The issuer reads which." READ: the API serves `ticker` raw (a SEDOL or an exchange number for the members the scanner names that way); the NAME in the Ticker column is the portal's own fallback in `cscTable.memberTicker` (AV-zzr-1 amendment 2); the `(local)` heading is the portal's `columnHeading`. So both are portal, one module. No value is converted (the page serves no rate). A portal candidate touching a product file: the CTO reviews it before the DEV landing; PROD is a separate pair; Security Analysis is Opal-internal. `portal_ref` for the cut: `00989b8b9df229e7b765b3a063102873abd9a89d` (origin/DEV at the cut, carrying ss-1). The check is the issuer's: the real PeersTab over the live payloads of ASML, ROG and BA (fixture `round94_prep/fixtures/peers_and_header_figures_ASML_ROG_BA_20261011.json`).

<status>pending</status>
<round>94</round>
<slot>0.9.0_WK_AMGT_RESAPP~388</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- issuer close 2026-10-11T12:53Z (2.0.0_SA_COO~R1): the portal DEV CANDIDATE is built -- portal branch wk-AMGT_RESAPP-388-portal @f0229015 (cscTable.ts +11/-7), proof @669d1e185c VALID, merged to box/dell1. Issuer re-run in the portal worktree: AC1 R94 PEERS UNITS YES (H1 'Mkt Cap (EUR, USD)' on ASML and '(CHF, USD)' on ROG, H2 BA '(USD)', T1 4 rows read none wrong, T2, T3), AC2 peersPattern CHECKS-OK 13 of 13 and tabs CHECKS-OK 21 of 21 (and peersCarry PASS), AC3 tsc -b exit 0 (worker). No value is converted (the page serves no rate); the word local is gone from the module. Worker row W388-S1 (the portal repo has no committer identity; the worker set GIT_COMMITTER_* per call and wrote no config) ruled: stands. Owed: the CTO's product-file review before the DEV landing; PROD is a separate pair; L9: the CVO's browser walk of the peers page on DEV.</status>
