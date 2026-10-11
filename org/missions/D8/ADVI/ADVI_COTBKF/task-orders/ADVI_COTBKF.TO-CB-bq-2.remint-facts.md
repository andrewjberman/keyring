# TO ADVI_COTBKF.TO-CB-bq-2.remint-facts -- round 69 CB-bq-2: the facts of the re-mint: the 2 day files, the chain of served writes, their captured state, every reader

<to_id>ADVI_COTBKF.TO-CB-bq-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~107</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>69</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bq-2` (`decompositions/ADVI_COTBKF_DECOMP.round69.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT for a sign-off. NOTHING IS APPLIED, SERVED OR WRITTEN REMOTELY. The issuer writes the sign-off half from your
record; you write no half.**

**Read first:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` from the heading `## ADDENDUM v0.5` to the end; `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_69_20261011.md` section 2 item 1 and section 3 item 2; the round-68
record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~104/R28_VS_R29_AT_PIN.json`, its `.md` and
`CHANGED_DATES_AT_PIN.csv` (the two dates: 2014-12-03 and 2020-11-13); the mint's sign-off of round 59,
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R59_ARD_COTTONWOOD_MINT_COO_HALF.md` (the form a half takes
here: blast radius, both branches, rollback per key, writers and readers); `data/assets/scripts/silver/commonwealth_account_return_daily.py`
(`build`, `source_addresses`, `apply_days`, `verify_served`, `--show-day-manifest`) and `commonwealth_fwd3_serve.py` (`--apply`, `--verify`,
`--dry-run`).

**What the sign-off must name** (PRD ADDENDUM v0.5 as narrowed by v0.6; the half cites v0.6): the 2 day files, the pin, both branches, and every reader of the served table with
one read through each. A re-mint that would replace any other file is a STOP.

**Your item.**

1. **The chain of served writes a re-mint needs, in order.** The mint adapter builds `account_return_daily` from the SERVED FWD-3 silver
   tables (`source_addresses()`), which are the `method_r28` build. So establish from the code, and say plainly: must the FWD-3 silver
   tables be re-served under `method_r29` first, and which of the three objects would change? For each served object a re-mint would
   WRITE (silver and gold): its address (from the code's builder call, never typed by hand), and by a read-only `head_object` its
   current ETag, size, version id and LastModified; whether the bucket keeps versions.
2. **What changes inside each object.** Using the round-68 runs at the served pin if they are still in THIS worktree's scratch
   (`.scratch/w104/fwd3_method_r28`, `.scratch/w104/fwd3_method_r29`: this worktree's own), else your own runs: for each of the three
   FWD-3 tables, rows differing between r28 and r29 (daily returns: expect 2; say what the value and month-grade tables do: round 68
   noted one account-month's computed percentage changes with its verdict unchanged). For the gold table: which day files differ, by
   date. It must be exactly the 2 dates. If the adapter cannot build day files from local tables, say so and derive the day-file
   list from the daily returns rows instead, stating that it is derived.
3. **Rows inside the 2 day files:** for each date, the rows in the served day file (read it, read-only: its row count and its
   measured count) and how many rows a re-mint changes (expect 1 each), and whether the day's manifest, the reasons sidecar and the
   method row change (the sidecar lists blank account-days: does either changed row enter or leave it?).
4. **Every reader of each object a re-mint writes.** Use the estate's own instruments, each run alone and unpiped: `comp-pipescript io`
   on the adapter and on the serve script, and `comp-find` for the gold table's name `account_return_daily` scoped to
   `data/assets/scripts`, to `portal` if this checkout has it, and to `infra` (quote each DENOMINATOR line). List each reader with
   its file and line and whether it reads Cottonwood's scope or another firm's. For each Cottonwood reader, the one read through it
   that a sign-off would cite (the command, not run if it writes anything). If there are none, say none, with the denominators.
5. **Both branches and the rollback.** Branch A: the 2 day files (and whatever step 1 found upstream) are as captured. Branch B:
   anything differs from the capture (an ETag moved, a third file would change, the control is not exact): STOP. Rollback per key:
   the prior version id of each object, and the command that restores it.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~107/REMINT_FACTS.json`. Top-level keys, exactly: `pin` (`{"as_of", "sha256"}`), `writes` (a list of `{"object", "tier",
   "address", "etag", "size", "version_id", "last_modified", "rows_changed", "why"}`), `day_files` (a list of `{"date", "rows",
   "measured", "rows_changed", "day_manifest_changes", "sidecar_changes"}`), `silver_must_be_reserved_first` (true | false, with the
   line of code), `readers` (a list of `{"object", "reader", "file", "line", "scope", "one_read"}`), `reader_census` (the DENOMINATOR
   lines), `branches`, `rollback`, `not_established`.

### ACCEPTANCE

<criterion id="CB69bq2-AC1" cell_refs="CB-bq-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~107/REMINT_FACTS.json',encoding='utf-8'));f=d['day_files'];print('REMINT-FACTS-RECORD pin=%s day_files=%d dates=%s day_rows_changed=%d writes=%d readers=%d silver_first=%s'%(d['pin']['as_of'],len(f),','.join(sorted(x['date'] for x in f)),sum(x['rows_changed'] for x in f),len(d['writes']),len(d['readers']),d['silver_must_be_reserved_first']))"</invocation><expect>REMINT-FACTS-RECORD pin=2026-10-09T11:52:52Z day_files=2 dates=2014-12-03,2020-11-13</expect></criterion>
`CB69bq2-AC1` -- the facts name exactly the 2 day files at the served pin, every object a re-mint writes with its captured state, and
the readers found. The issuer writes the sign-off half from this record and the CTO reviews it.

<expected_criteria>CB69bq2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry. You write no sign-off half.**
- Read-only `head_object` and `get_object` of the named served objects of THIS project are allowed; no listing of another firm's
  prefix; no read of the restricted CRM prefix.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets, heads and listings are allowed where the cell
  says so. No push. No `--refresh`. No vendor call (no Yahoo, no Bloomberg).
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price,
  ratios, version ids, ETags and reason codes only. A build log line carrying `read_account=` is never echoed: filter it out.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W107-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round69.md</decomp_doc> (round 69), cell `CB-bq-2`.
<owned_cells>CB-bq-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB69bq2-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~107/ADVI_COTBKF.TO-CB-bq-2.remint-facts.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB69bq2-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** whether the silver tables must be re-served first, with the line of code; every object a re-mint writes with its address, ETag, size, version id and LastModified; rows changed per object; the 2 day files with their row and measured counts and what else changes for each day; every reader found, with the census DENOMINATOR lines; the two branches; the rollback per key; the `REMINT-FACTS-RECORD` line; what is not established; a statement that nothing was applied or written remotely; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement; the re-mint itself is a later hand-run act under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE read-only head and get of this project's own served objects; no write; BLIND: comp-iam was not run by the issuer.
comp-adversary: RUN -- the day-file list is pinned to the two measured dates and a third is a STOP; addresses come from the code's builder calls; the reader search prints its denominators so a zero is not read as an absence without its scope; the upstream silver write is asked about explicitly so it cannot ride unnamed; BLIND: a reader outside this checkout (another repository) is not seen by a search of this one.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-69 analysis @e0f9682779 (msg 5206), section 3 item 2, and PRD ADDENDUM v0.6 @df488019bf (msg 5217); `3.0.0_SA_CVO` REMEDIATION_v39 @22e2566c22.
