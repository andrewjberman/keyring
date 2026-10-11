# TO ADVI_COTBKF.TO-CB-bp-2.mint-carries-the-pin -- round 68 CB-bp-2: the mint adapter writes the split-store pin into the mint's manifest and refuses to apply without it

<to_id>ADVI_COTBKF.TO-CB-bp-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~102</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bp-2` (`decompositions/ADVI_COTBKF_DECOMP.round68.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_68_20261011.md` section 2 item 5; `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~99/SPLIT_STORE_PIN.json`; `data/assets/scripts/silver/commonwealth_account_return_daily.py` in full
(`build` near line 397 and the manifest it writes near line 590; `stamp_manifest`; `minted_objects`; `apply_days`; `verify_served`);
`data/assets/scripts/silver/commonwealth_fwd3_serve.py` where it writes `fwd3_manifest.json` and its `split_store` field (round 67:
`pinned`, `as_of`, `listed`, `held`, `sha256`, `read_by`); the tests `test_commonwealth_ard_*.py`.

**The gap.** The FWD-3 build's manifest now names the instant its split store was read. The mint adapter builds `account_return_daily`
from the FWD-3 tables and its manifest says nothing of that instant, so a minted table cannot be traced to its inputs' state.

**Your item. No AWS call; tests fake S3. You do NOT run `--apply` or `--verify-served`.**

1. `build` takes the FWD-3 build's manifest (find how `build` locates its inputs today, and take the manifest that sits with them; if
   `build` reads the served FWD-3 tables and no manifest is reachable from there, add a `--fwd3-manifest <path>` argument) and writes
   into the mint's manifest a `split_store` object: the FWD-3 manifest's `split_store` verbatim, plus `carried_from` (the FWD-3
   manifest's path or address and its sha256).
2. `--apply` REFUSES a mint manifest whose `split_store.pinned` is not `true`:
   `REFUSED: the mint's inputs name no split-store instant (split_store.pinned is not true); rebuild from a pinned FWD-3 build`.
3. `--verify-served` is UNCHANGED in what it requires: the table served today was minted before the pin existed, and it must still
   verify. Print one extra token at the end of its line, `split_store=<pinned|unpinned|absent>`, read from the manifest it was given.
4. Tests (synthetic): a pinned FWD-3 manifest is carried verbatim with `carried_from`; `--apply` refuses an unpinned and an absent
   one before any write; `--verify-served` on a manifest with no `split_store` still matches and prints `split_store=absent`. An
   existing test that asserts the verify line ends at `manifests=k/n` changes its expected line to the new one; name each.
5. Run the suite.

### ACCEPTANCE

<criterion id="CB68bp2-AC1" cell_refs="CB-bp-2"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB68bp2-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before.

<criterion id="CB68bp2-AC2" cell_refs="CB-bp-2"><invocation>python -c "a=open('data/assets/scripts/silver/commonwealth_account_return_daily.py',encoding='utf-8').read();print('ARD-PIN-CARRIED split_store_mentions=%d apply_refusal=%s verify_token=%s'%(a.count('split_store'),'split_store.pinned is not true' in a,'split_store=' in a))"</invocation><expect>ARD-PIN-CARRIED split_store_mentions=</expect></criterion>
`CB68bp2-AC2` -- the adapter names the pin, carries the refusal text and prints the verify token. The issuer reads the three values
and the tests by name.

<expected_criteria>CB68bp2-AC1,CB68bp2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch** `commonwealth_fwd3_serve.py`, `commonwealth_daily_valuation.py`, `commonwealth_sweep_regrade.py`, the tracked mint
  manifest under another worker's deliverables, anything under `data/assets/scripts/gold/` or `lib/`.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets and listings the build already makes are allowed.
  No push. No `--refresh`.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, prices per security, ratios,
  version ids and reason codes only. A build log line that prints `read_account=` is never echoed: filter it out before you read a log.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Sequencing:** never start a later step before the earlier one's check has been read.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W102-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
data/assets/scripts/silver/commonwealth_account_return_daily.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round68.md</decomp_doc> (round 68), cell `CB-bp-2`.
<owned_cells>CB-bp-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB68bp2-AC1, CB68bp2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~102/ADVI_COTBKF.TO-CB-bp-2.mint-carries-the-pin.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB68bp2-AC1,CB68bp2-AC2` BEFORE the flip. Both are mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** how `build` now finds the FWD-3 manifest; the `split_store` object it writes; the refusal text and where it fires; the verify line's new token; tests added and tests changed, by name, with each moved expectation; the diff of the adapter; the pytest line; the `ARD-PIN-CARRIED` line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one hand-run adapter and its tests.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; tests fake S3.
comp-adversary: RUN -- the apply refuses an unpinned and an absent pin before any write, by test; the verify of the table served today (minted before the pin) is unchanged in what it requires, by test; BLIND: whether the served FWD-3 tables carry a manifest object the adapter can reach, which the cell reports.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-68 analysis @b3a272fffc (msg 5008), section 3 item 2; `3.0.0_SA_CVO` REMEDIATION_v38 @931dc9ea93.
