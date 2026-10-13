# TO NFRA_DEVPLN.TO-DP-s-1 -- round 1 THREAD DP-s-1: the settlement list Andrew rules from (DEV groups, PROD-only commits, branches with work not on DEV)

<to_id>NFRA_DEVPLN.TO-DP-s-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~5</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-s-1` (`decompositions/NFRA_DEVPLN_DECOMP.round1.md`) | **outcome_ref:** FWD-6 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Portal DEV and PROD have diverged both ways: DEV is ahead of PROD by about 201 commits and PROD ahead of DEV by about 33; 9 or more remote branches hold work not on DEV. Andrew rules the backlog once, per feature group
(approve forward, hold on a branch, or drop), from ONE list. Build the tool that writes that list from git, and run it once. Your worktree has the portal repo at `portal/` with `origin/DEV` and `origin/PROD` present (do not fetch).

### BUILD

`python .tools/portal-settlement-list.py [--portal portal] [--out <file>]` and `python .tools/portal-settlement-list.py --selftest`. Python standard library; every git call is a read, run as `git -C <portal> ...`.

1. DEV-not-PROD groups. Files = `git diff --name-only origin/PROD...origin/DEV`. Group by the first match of these prefixes (the class column is the unsure rule, an INPUT and not a measurement):

   | group | path prefix | class |
   |---|---|---|
   | InvestorReporting | `src/pages/InvestorReporting` | client-facing |
   | SecurityAnalysis | `src/pages/SecurityAnalysis` | opal-internal |
   | TicketCenter | `src/pages/TicketCenter` | client-facing |
   | AdvisorIntelligence | `src/pages/AdvisorIntelligence` | client-facing |
   | api | `src/api/endpoints` | client-facing |
   | firmAccess | `src/lib/firmAccess.ts` | client-facing |
   | other | every file matching none of the above | client-facing |

   FIRST measure the real path prefixes in the repo (`git -C portal diff --name-only origin/PROD...origin/DEV | head -40` shows them; the table's `src/` roots are the issuer's guess and you correct them to what the repo
   holds, stating the correction in the report). For each group print: files changed, commits touching it (`git rev-list --count origin/PROD..origin/DEV -- <prefix>`), the top three committers by commit count
   (`%an`), and the class.
2. PROD-only commits: `git rev-list origin/DEV..origin/PROD` with author, date, subject, and for each whether a DEV commit carries the same patch (`git cherry origin/DEV origin/PROD`: a `-` line means DEV has it).
3. Branches with work not on DEV: every remote branch `origin/<b>` (excluding `DEV`, `PROD`, `HEAD`) with `git rev-list --count origin/DEV..origin/<b>` above 0. For each: ahead count, tip author, tip date, and the `git cherry origin/DEV origin/<b>`
   split (`+` = patch not on DEV, `-` = already on DEV under another commit), and an `owner` column equal to the tip author.
4. Write the markdown file (default `org/missions/D0/NFRA/NFRA_DEVPLN/ledger/SETTLEMENT_LIST.md`): a header with the measured refs (short shas of `origin/DEV` and `origin/PROD` and the UTC time), the three tables, and a closing block of
   machine lines. The LAST stdout line, also written into the file, is
   `SETTLEMENT-LIST dev_ahead=<n> prod_ahead=<m> groups=<g> files_total=<t> files_other=<o> branches=<b>` where `dev_ahead` is `rev-list --count origin/PROD..origin/DEV`, `prod_ahead` is `rev-list --count origin/DEV..origin/PROD`,
   `groups` counts the named groups (not `other`), and `files_other` is the count in `other`.
5. `--selftest` builds a temporary repo with a DEV, a PROD and a branch with known counts and ends with `SETTLEMENT-LIST-SELFTEST cases=<k>/<n> ok=True|False`: the group file counts, the commit counts, the cherry split and `dev_ahead`/`prod_ahead`
   equal the known values; a path matching no prefix lands in `other`; the file is written.

### RULES FOR THIS CELL

Read only: no fetch, no push, no write to the portal repo. No non-ASCII in the tool or the list. Ruff clean on the tool. The only files you write are the three in `<paths>`.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPs1-AC1" cell_refs="DP-s-1"><invocation>python .tools/portal-settlement-list.py --selftest</invocation><expect>ok=True</expect></criterion>
`DPs1-AC1` -- the self-test above, every case passing.

<criterion id="DPs1-AC2" cell_refs="DP-s-1"><invocation>python .tools/portal-settlement-list.py --portal portal --out org/missions/D0/NFRA/NFRA_DEVPLN/ledger/SETTLEMENT_LIST.md</invocation><expect>SETTLEMENT-LIST dev_ahead=</expect></criterion>
`DPs1-AC2` -- the live run against the real portal refs; it writes the list Andrew reads.

<criterion id="DPs1-AC3" cell_refs="DP-s-1"><invocation>bash org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/2.0.0_SA_COO~DV/checks/check_devpln_settlement.sh org/missions/D0/NFRA/NFRA_DEVPLN/ledger/SETTLEMENT_LIST.md portal</invocation><expect>SETTLEMENT-COUNTS-MATCH</expect></criterion>
`DPs1-AC3` -- the issuer's independent denominator: the list's two headline counts equal `rev-list --count` read directly (the check script is the issuer's; run it, do not edit it).
</proof_of_spec>

<expected_criteria>DPs1-AC1,DPs1-AC2,DPs1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~5/NFRA_DEVPLN.TO-DP-s-1.settlement-list.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPs1-AC1,DPs1-AC2,DPs1-AC3`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md</decomp_doc>
<owned_cells>DP-s-1</owned_cells>
</decomp_ref>

<paths>
.tools/portal-settlement-list.py
org/missions/D0/NFRA/NFRA_DEVPLN/ledger/SETTLEMENT_LIST.md
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
lane: the <paths> block IS the grant (worker RULING 1). Portal worktree: this order needs `--portal-ref` at the spawn.
</preflight>

Source: PRD `prd/NFRA_DEVPLN_PRD.md` v0.2 @d2b7385bee C-SETTLE (measured F5-F8), S05; brief Part IV F5-F8 and Part VII (branch ownership not checked). Ratified-text SIGNED by 3.0.0_SA_CVO~L (current). The list is the input to issuer acts A2 and A3.
