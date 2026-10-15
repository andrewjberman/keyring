# TO ADVI_COTBKF.TO-CB-ck-2.price-the-move-per-account -- round 89 CB-ck-2: what each policy of the use_class guard would change, per active account, counts only; the figures a never-widen pair needs

<to_id>ADVI_COTBKF.TO-CB-ck-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~178</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>89</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ck-2` (`decompositions/ADVI_COTBKF_DECOMP.round89.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-ck-1 (the switch)

---

## WORKER FACE

### THE CELL

**STAGED behind `CB-ck-1`: you act when your own order `ADVI_COTBKF.TO-CB-ck-1` reads `complete` in your worktree (it is yours: same slot `~178`, same worktree). Until then do nothing.**

**Why.** The CTO ruled that a fix that changes a served value goes under a never-widen pair that PRICES THE MOVE PER ACCOUNT, and that whether already-served days are blanked now or kept labelled interim is Andrew's reading of his own word (call `3adb`). That pair and that answer need numbers nobody has: how much would each policy change, for which accounts. `CB-ck-1` built the switch. You measure what it would do. **This cell changes no code and no served object; it reads and counts.**

**Read first:** your own `CB-ck-1` record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~178/USE_CLASS_SERVE_RECORD.json` (the `real_run` block: whether a default run's data exists and where) and the module `data/assets/scripts/silver/commonwealth_fwd3_serve.py` as you left it. The active set: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ACTIVE_COTTONWOOD_SET_V2.csv` (sha256 `5cef7ab0c9e10fe299cb757d4dba31792d069bad35f7250defa76e18773046ae`; columns `account_key,source_side,cusip,ticker,held_from,held_to,window_basis`; raw account numbers: they never leave the process), and the reverse match `.../REVERSE_MATCH_V3.csv` (sha256 `0783f088aecbf29e46751aa5d80239b8aa53f16484778162e34ee1c09783c66f`; `account_key,predecessor_key,match_basis,reason`: it ties each active Black Diamond account to its Commonwealth predecessor, if any).

**Your items.**

1. **Whether you can measure.** If `CB-ck-1`'s `real_run` says `NO_DATA_DIR`, STOP this cell: write the record with `measured: false` and the reason, file no row, and report; the issuer decides whether a default run is built in a later round. Do not build one yourself here.
2. **Two builds, one input.** Run `commonwealth_fwd3_serve.py` (local only: no `--apply`) over the default run's data twice into folders under your worktree `.scratch/` (never committed): `--yahoo-active-policy interim` and `--yahoo-active-policy blank`. These are READS of local parquet plus the one index read; no S3 write.
3. **Count, per the pair's needs** (all counts; an account is counted, never named):
   - **Accounts.** The number of Commonwealth accounts whose chain is ACTIVE: a Commonwealth account is active when the reverse match ties it (as `predecessor_key`) to a current account in `REVERSE_MATCH_V3.csv`, `match_basis` `crosswalk_matched` or `account_links`. State how many Commonwealth accounts the data holds and how many are active.
   - **Under `interim`:** the number of active accounts, account-days and months whose `use_class` label reads `NOT_FOR_ACTIVE` (they keep their values and gain the label); the same for `INACTIVE_USE`; and the number of account-days priced on Yahoo at all.
   - **Under `blank`:** the number of account-days blanked (reason `HELD_SOURCE_UNDER_REVIEW`) and how many of them belong to ACTIVE accounts; the number of active accounts with at least one blanked day; the months whose grade changes (`month_grades`: verdict before and after, counts by verdict pair); and, per active account, the share of its account-days blanked, summarised as a distribution (the count of active accounts in each band 0, (0,1], (1,10], (10,50], (50,100] percent).
   - **The securities behind it:** how many distinct CUSIPs the `blank` policy holds, and how many of those are held by active accounts only, by inactive accounts only, by both.
   - **Control:** the `interim` run's three tables equal the pre-change build's (hash per table; one pre-change build on the same input from `git stash`-free means: check out nothing, instead run the module at the commit BEFORE `CB-ck-1` through `git show <commit>:<path>` into `.scratch/` and run that copy). If they differ, say so; it is the cell's most important line.
4. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~178/MOVE_PRICED_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `data_dir_basis` (what run the data came from: its date and `run_commit`, no path to a client file), `accounts` (`{"commonwealth", "active"}`), `interim` (`{"active_accounts_not_for_active", "active_account_days_not_for_active", "active_months_not_for_active", "account_days_yahoo_priced", "inactive_use_account_days"}`), `blank` (`{"account_days_blanked", "of_which_active", "active_accounts_touched", "month_grade_changes" (counts by "before->after" verdict pair), "active_share_bands" (counts by band)}`), `securities_held` (`{"total", "active_only", "inactive_only", "both"}`), `control` (`{"interim_tables_equal_pre_change": true|false, "hashes_compared": 3}`), `not_established`; and a short `.md`. No account number, name or dollar value in either.

### ACCEPTANCE

<criterion id="CB89ck2-AC1" cell_refs="CB-ck-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~178/MOVE_PRICED_RECORD.json',encoding='utf-8'));m=d['measured'];print('MOVE-PRICED measured=%s' % m + ((' active=%d blank_days=%d of_active=%d active_touched=%d interim_equal=%s'%(d['accounts']['active'],d['blank']['account_days_blanked'],d['blank']['of_which_active'],d['blank']['active_accounts_touched'],d['control']['interim_tables_equal_pre_change'])) if m else ' reason=%s'%d['reason']))"</invocation><expect>^MOVE-PRICED measured=(True active=\d+ blank_days=\d+ of_active=\d+ active_touched=\d+ interim_equal=True|False reason=NO_DATA_DIR)$</expect></criterion>
`CB89ck2-AC1` -- the move is priced and the interim control holds, or the cell states plainly that no data run exists.

<criterion id="CB89ck2-AC2" cell_refs="CB-ck-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~178/MOVE_PRICED_RECORD.json',encoding='utf-8'));b=d.get('blank') or {};bands=sum((b.get('active_share_bands') or {}).values());ok=(not d['measured']) or (bands==d['accounts']['active'] and b['of_which_active']<=b['account_days_blanked'] and d['securities_held']['active_only']+d['securities_held']['inactive_only']+d['securities_held']['both']==d['securities_held']['total']);print('MOVE-PRICED-SUMS consistent=%s'%ok)"</invocation><expect>MOVE-PRICED-SUMS consistent=True</expect></criterion>
`CB89ck2-AC2` -- the record's figures add up: the share bands sum to the active accounts, the active blanked days do not exceed the blanked days, and the security split sums to the total.

<expected_criteria>CB89ck2-AC1,CB89ck2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder and your own NEW channel row. You change no code, test or committed file; scratch outputs stay under the worktree `.scratch/` (never committed) and are deleted when you finish, since they hold per-account values.
- **AWS: READ-ONLY,** the one index read the module makes; no write, no serve, no `--apply`. No vendor call.
- **No account number, name or dollar value** in the record, the report or any message: counts, bands, verdict pairs and CUSIP counts only.
- **NEVER** serve, apply, overwrite, push, override a gate or `--force`; do not run the module at a commit that is not `CB-ck-1`'s parent or its own result.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W178-S<k>` (k continues after any row of `CB-ck-1`; `date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round89.md</decomp_doc> (round 89), cell `CB-ck-2`.
<owned_cells>CB-ck-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB89ck2-AC1, CB89ck2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~178/ADVI_COTBKF.TO-CB-ck-2.price-the-move-per-account.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB89ck2-AC1,CB89ck2-AC2` BEFORE the flip. Both criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when both criteria PASS** (the flip is inside your grant: the order's own face is lane ANY). A cell that reports `NO_DATA_DIR` still PASSES AC1 and AC2: the order asks for the measurement or the plain statement that none exists.
</proof_of_spec>

**REPORT:** FIRST the `MOVE-PRICED` line. Then: the data run's basis; the active and total Commonwealth accounts; the interim and blank counts; the month-grade changes by pair; the share-band distribution; the securities split; the control result; the two criterion lines; commits; every gate refusal and hook denial, verbatim. No account number or value in the report.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read and a count; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE one read-only index read under the existing role; no new permission.
comp-adversary: RUN -- the control (the `interim` tables equal the pre-change build's) is the check on `CB-ck-1`; the counts add up by construction (AC2); BLIND: "active" is read from the reverse match, so a Commonwealth account matched only after a person's confirmation (the near matches) is not counted active here; the data run's date may be older than today's holdings; and per-account shares are shown as bands to keep the record free of any account-level figure.
lane: the <paths> block IS the grant (worker RULING 1). A read and a count: nothing outside the deliverables folder and one channel row is written.
</preflight>

**ISSUER NOTES:** STAGED behind `CB-ck-1` (the same slot continues). Source: `1.0.0_SA_CTO~DELL1` msg 6175 ("a fix that changes a served value goes under a never-widen pair that prices the move per account"; call `3adb`). The figures feed the COO half of that pair, which this seat writes after the CTO and Andrew rule.
