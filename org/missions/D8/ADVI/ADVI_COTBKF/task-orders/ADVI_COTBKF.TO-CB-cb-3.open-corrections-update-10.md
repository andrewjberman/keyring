# TO ADVI_COTBKF.TO-CB-cb-3.open-corrections-update-10 -- round 80 CB-cb-3: the correction list re-cut after the read-back: PRD v0.10, the lander, and the two reads of round 80

<to_id>ADVI_COTBKF.TO-CB-cb-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~157</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>80</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cb-3` (`decompositions/ADVI_COTBKF_DECOMP.round80.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-cb-1, CB-cb-2

---

## WORKER FACE

### THE CELL

**This cell UPDATES one tracked file from records already in the tree. It measures nothing new and changes no code. It runs LAST,
after the read-back of the fund closes: both records below are in the tree when you start; if one is absent, that is the refusal
clause.**

**Read first:** the list as it stands, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json` and `OPEN_CORRECTIONS.md` (revision 9); `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_80_20261012.md` whole, section 4 ("It predates
v0.10 and dell1's answer ... It is re-cut after item 2."); the PRD `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` from `## ADDENDUM v0.8` to the end of the file.

1. **What revision 9 lacked, in the merged entry (`adjusted-close-used-as-price`):** under `c_basis`, ADDENDUM v0.10 quoted with its
   lines (v0.9's split sentence WITHDRAWN and what replaces it), the PRD's version and commit, and the sign-off state as
   `python .tools/prd-signoff.py status ADVI_COTBKF` prints it (quote; do not interpret). Under `extent.sechist.owning_fabric_answer`
   (now `relay file not in this tree`): if the relay file `org/tier0_exec/0.0.0_AB_MSTR/deliverables/relays/RELAY_DELL1_H1_SECHIST_ANSWER_FOR_C2_20261012T0213Z.md`
   is in your tree, quote it, labelled the OWNING fabric's measurement; else leave the string. Under a new key `extent.lander`:
   dell1's ruling (`git show origin/box/dell1:org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_AS_TRADED_CLOSES_VIA_DEMQUE_20261012.md`; if that ref does not resolve in your tree say so and quote nothing), and the request
   file `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF-TIER2-15-FUNDS-AS-TRADED-20261012.request.json` with its commit.
2. **This round's two records, into `extent`:** `.../0.9.0_WK_ADVI_COTBKF~155/THREE_EQUITIES.json` under `three_equities` (the
   securities off 1.0; held and served days; the four ratios; the causes; whether a served day carries a split-sized error;
   whether the contract widens); `.../0.9.0_WK_ADVI_COTBKF~156/FUND_CLOSES_READ_BACK.json` under `fund_closes_read_back` (where;
   the held trading days present of 20,718; the 14 funds classed by the price paid from dell1's column beside round 76's
   classes; the split arm IN THE RECORD'S OWN WORDS).
3. The two unreconciled items revision 9 added on PRD-against-record tensions (the possible double scaling; the signed sentence
   against the basis record): each is answered by v0.10 to the extent v0.10's text says, quoted; it stays open where the round's
   records leave it open.
4. Every other entry is left alone unless a record moved. Update `as_of`; append one item to `revisions` (round 80); rewrite
   `OPEN_CORRECTIONS.md` to match. Keep the file's indentation as it is. No string `record absent` in the file.

**AMENDMENT 1 (issuer `2.0.0_SA_COO~C2`, 2026-10-13T13:2xZ) -- both records are now in the tree** (merges 7b6def6fe8 for `FUND_CLOSES_READ_BACK.json`, 409f039d8a for
`THREE_EQUITIES.json`). Where a record's number differs from this order's words, write the RECORD's number and put the difference under `unreconciled`: item 2 says "the 14 funds
classed" and `FUND_CLOSES_READ_BACK.json` has all 15 funds with trade units and only 7 with a dell1 column (8 `not_landed`); `THREE_EQUITIES.json` lists 5 securities off 1.0, not 3, and
sets `served_day_with_split_sized_error` true (APH, 48 minted account-days; row ADVI_COTBKF-D2-W155-S1, carried to the CTO the same hour). Carry both facts and the cause
`not_established` exactly as the records word them; `widens_c_basis` as the record holds it. The channel rows ADVI_COTBKF-D2-W155-S1 to S4 and ADVI_COTBKF-D2-W156-S1 to S5 may be
cited by id; do not restate their bodies.

**Rules.** Print each number from its record before you write it. A number no record holds is `NOT_MEASURED` with the record looked
in. Where two records disagree, both go under `unreconciled`. No opinion on whether a correction should be made. No account id; a
security by its ticker.

### ACCEPTANCE

<criterion id="CB80cb3-AC1" cell_refs="CB-cb-3"><invocation>python -c "import json;p='org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json';d=json.load(open(p,encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};m=[x for x in c if x['id']=='adjusted-close-used-as-price'][0];e=m['extent'];print('OPEN-CORRECTIONS-RECORD revisions=%d record_absent=%d v0_10=%s lander=%s three_equities=%s fund_closes_read_back=%s in_force=%s state=%s corrections=%d keys_complete=%s evidence_rows=%d unreconciled=%d'%(len(d['revisions']),open(p,encoding='utf-8').read().count('record absent'),'v0.10' in json.dumps(m['c_basis']),'lander' in e,'three_equities' in e,'fund_closes_read_back' in e,'in_force' in m,m['state'],len(c),all(k<=set(x) for x in c),len(m['evidence']),sum(len(x['unreconciled']) for x in c)))"</invocation><expect>OPEN-CORRECTIONS-RECORD revisions=10 record_absent=0 v0_10=True lander=True three_equities=True fund_closes_read_back=True in_force=True state=OPEN corrections=6</expect></criterion>
`CB80cb3-AC1` -- the list is at its tenth revision with six entries; the merged entry carries v0.10, the lander and this round's
two records. The issuer reads each change against its record.

<expected_criteria>CB80cb3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (the deliverables folder, where the list sits at its top level, and your own NEW channel row)
  and the file of this order.
- **You change no code, test, config, manifest or registry, and no other seat's record.** Everything is local; no AWS call. The
  commands you run beyond python and git are `python .tools/prd-signoff.py status ADVI_COTBKF` and `git show` of one ref, reads.
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
  `ADVI_COTBKF-D2-W157-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round80.md</decomp_doc> (round 80), cell `CB-cb-3`.
<owned_cells>CB-cb-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB80cb3-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~157/ADVI_COTBKF.TO-CB-cb-3.open-corrections-update-10.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB80cb3-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** v0.10 as quoted with its lines and the sign-off state as the tool printed it; what the relay and lander keys hold; every entry changed and what changed in it, with the record and the number printed from it; how the two revision-9 unreconciled items were answered; what is still unreconciled; every NOT_MEASURED and the record looked in; the `OPEN-CORRECTIONS-RECORD` line; the account-id scan's DENOMINATOR line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document updated from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- held until both other cells drain; the PRD and the ruling are quoted, not paraphrased; the split arm is carried in the record's own words; an earlier item is answered only by what the contract or a record says; BLIND: a ruling given only in a message.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-80 analysis @7bfd7c4664 (msg 6406), section 3 item 3; `3.0.0_SA_CVO` REMEDIATION_v48 @222ab69461.
