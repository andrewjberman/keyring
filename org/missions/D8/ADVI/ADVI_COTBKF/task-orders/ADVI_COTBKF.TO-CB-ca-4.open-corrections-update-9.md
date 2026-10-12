# TO ADVI_COTBKF.TO-CB-ca-4.open-corrections-update-9 -- round 79 CB-ca-4: the correction list brought current: contract C-BASIS, and the three reads of round 79 (the issuer's addition)

<to_id>ADVI_COTBKF.TO-CB-ca-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~154</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>79</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-ca-4` (`decompositions/ADVI_COTBKF_DECOMP.round79.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-ca-1, CB-ca-2, CB-ca-3

---

## WORKER FACE

### THE CELL

**This cell UPDATES one tracked file from records already in the tree. It measures nothing new and changes no code.**

**Read first:** the list as it stands, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json` and `OPEN_CORRECTIONS.md` (six entries, one struck, eight revisions, a `tooling`
object, a `rulings_in_force` pointer); `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the two sections headed `## ADDENDUM v0.8` (near line 292: it is also the round-79 analysis and holds the ENRICHMENT LIST) and `## ADDENDUM v0.9` (near line 343, the SIGNED text: it REPLACES item 2 of C-BASIS; v0.8's two tokens AS_TRADED and ADJUSTED are WITHDRAWN and are not used anywhere), whole.

**Your item: change only what a record supports. This cell runs LAST: all three records below are in the tree when you start; if
one is absent, that is the refusal clause.**

1. **CONTRACT C-BASIS, in the merged entry (`adjusted-close-used-as-price`),** under a key `c_basis`: items 1, 3, 4 and 5 quoted with
   their lines from the PRD's ADDENDUM v0.8, item 2 and the new item 3 quoted from ADDENDUM v0.9 (the SIGNED text: the basis is the
   build's existing column `basis` with the values `as_traded_close` and `store`; v0.8's two tokens are WITHDRAWN: do not write
   `AS_TRADED` or `ADJUSTED` as values anywhere), and the proof as both addenda state it (v0.9 adds the split arm); that v0.8's
   half was REFUSED and v0.9's SIGNED, with the review's path; the PRD's version and commit; and the sign-off
   state as `python .tools/prd-signoff.py status ADVI_COTBKF` prints it when you run it (quote the two lines; do not interpret).
   `closes_when.now` becomes: C-BASIS built and its proof graded (quoted), the former text moved to the earlier conditions.
   `in_force` is kept and gains the addendum's sentence that the row stays BLOCKING "until C-BASIS is built and its proof graded".
2. **This round's three records, into the merged entry's `extent`:**
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~151/SECHIST_AS_IT_STANDS.json` under `sechist` (the owner and
   fabric; the read scope; whether the history exists; its fields; whether it carries a basis; the 15 funds' coverage and the count
   of held trading days UNPRICED under C-BASIS; any ask that goes through `0.0.0_AB_MSTR~DELL2`);
   `.../0.9.0_WK_ADVI_COTBKF~152/TICKER_MANY_NAMES.json` under `ticker_many_names` (the denominators; the classes; how many held
   securities are not priced from their own rows, with the account-day counts; the 15 apart; the no-ticker half);
   `.../0.9.0_WK_ADVI_COTBKF~153/STORE_WRITER.json` under `store_writer` (the versions; what changed between them; the code that
   matches the live shape; the run and whose, or not established; the owner today).
   **AMENDMENT 1 (issuer, on CTO msg 6286):** and cell 2's second record,
   `.../0.9.0_WK_ADVI_COTBKF~152/BASIS_VALUE_AGAINST_SPLIT_SCALING.json`, under `basis_against_split_scaling` (where the basis value
   is written and where the split scaling runs; the order; whether a point can leave the build marked `as_traded_close` and
   unscaled, path by path; for which security types the signed sentence holds). If the PRD has been amended on it by the time you
   run (a heading past `## ADDENDUM v0.9`), quote the amendment with its line beside it. This record too is in the tree when you
   start.
3. **What C-BASIS changes in earlier items:** the unreconciled item saying a corrected basis has no store to come from is answered
   by C-BASIS item 3 (the source is named: the securities history) and stays open to the extent cell 1 shows the history does not
   yet hold it: reword it with both, in the records' words. The item about the 15 funds classed with the flat-charge allowance is
   answered by C-BASIS item 5 (re-derived after the re-pricing): add that sentence, quoted; the item stays until it is done.
4. **The 2022-factor entry:** check the PRD for any addendum on the spin-off factor (the headings `## ADDENDUM v0`; v0.8 is the
   fund basis, not the factor); quote it with its line if one landed; else unchanged.
5. Every other entry is left alone unless a record moved. Update `as_of`; append one item to `revisions` (round 79); rewrite
   `OPEN_CORRECTIONS.md` to match. No string `record absent` in the file.

**Rules.** Print each number from its record before you write it. A number no record holds is `NOT_MEASURED` with the record looked
in. Where two records disagree, both go under `unreconciled`. No opinion on whether a correction should be made. No account id; a
security by its ticker.

### ACCEPTANCE

<criterion id="CB79ca4-AC1" cell_refs="CB-ca-4"><invocation>python -c "import json;p='org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json';d=json.load(open(p,encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};m=[x for x in c if x['id']=='adjusted-close-used-as-price'][0];e=m['extent'];print('OPEN-CORRECTIONS-RECORD revisions=%d record_absent=%d c_basis=%s in_force=%s sechist=%s ticker_many_names=%s store_writer=%s state=%s corrections=%d keys_complete=%s evidence_rows=%d unreconciled=%d'%(len(d['revisions']),open(p,encoding='utf-8').read().count('record absent'),'c_basis' in m,'in_force' in m,'sechist' in e,'ticker_many_names' in e,'store_writer' in e,m['state'],len(c),all(k<=set(x) for x in c),len(m['evidence']),sum(len(x['unreconciled']) for x in c)))"</invocation><expect>OPEN-CORRECTIONS-RECORD revisions=9 record_absent=0 c_basis=True in_force=True sechist=True ticker_many_names=True store_writer=True state=OPEN corrections=6</expect></criterion>
`CB79ca4-AC1` -- the list is at its ninth revision with six entries; the merged entry carries the contract, the ruling still in
force, and this round's three records. The issuer reads each change against its record.

<expected_criteria>CB79ca4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (the deliverables folder, where the list sits at its top level, and your own NEW channel row)
  and the file of this order.
- **You change no code, test, config, manifest or registry, and no other seat's record.** Everything is local; no AWS call. The one
  command you run beyond python and git is `python .tools/prd-signoff.py status ADVI_COTBKF`, a read.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W154-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round79.md</decomp_doc> (round 79), cell `CB-ca-4`.
<owned_cells>CB-ca-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB79ca4-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~154/ADVI_COTBKF.TO-CB-ca-4.open-corrections-update-9.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB79ca4-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the contract as written, with its lines, and the sign-off state as the tool printed it; every entry changed and what changed in it, with the record and the number printed from it; how the two earlier unreconciled items were reworded; whether an addendum on the 2022 factor exists; what is still unreconciled; every NOT_MEASURED and the record looked in; the `OPEN-CORRECTIONS-RECORD` line; the account-id scan's DENOMINATOR line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document updated from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- held until all three other cells drain; the contract is quoted with its lines and its sign-off state is quoted as the tool prints it, not interpreted; the ruling in force is kept; an earlier item is reworded only by what a record or the contract says; BLIND: a ruling given only in a message.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` PRD ADDENDUM v0.8 @fab39b5beb, which is also the round-79 analysis (msg 6275), its ENRICHMENT LIST item 4, with ADDENDUM v0.9 @95da777fbf (msg 6282), the SIGNED text; `3.0.0_SA_CVO` REMEDIATION_v47 @77527824fd.
