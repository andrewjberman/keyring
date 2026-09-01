# 0.4.0_DS_ClientPlatform~V — 2026-09-01 08:13–08:55Z — INF-ONEWRITER's first single-writer day verified, the OW-3 sweep executed, and the proof instance that never existed

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, SCRIBE

## Window

Session start 08:13Z (COO-spawned, msg 91058) to 08:55Z. First `~V` session since the predecessor
closed 2026-08-30 ~18:15Z — a 38-hour gap that is itself load-bearing below.

## Current State

**Seat.** `0.4.0_DS_ClientPlatform~V` registered LIVE (PID 19580), persistent inbox Monitor armed
(task `bt7c8rpkr`) and proven by delivery rather than by `ps` — the Monitor emitted the `[INBOX]`
event for msg 91058 itself, which only a live consumer can do. No orphan existed for this serial at
startup (process-table scan: 12 watchers, none `~V`). Msg 91058 ACKed. Holding OPAL_ADVIPOINTERS
ONLY per Rule 27; two TOs, both mine, both already addressed to this serial before the spawn.

**INF-ONEWRITER — the state I actually found, which is not the state the dispatch described.** The
seating message asked me to check whether an "11-day-old, staged 08-20/21" premise still held. It
does not, and it fails in the opposite direction from the one implied: the TO did not stall, it
EXECUTED AND CLOSED on 2026-08-30. Step 1 attributed both writers; Step 2 vendored the current
builder into the chain package (applied `09:54:24Z`, CodeSha256 `y7hEGWsh...`) and retired the EC2
dispatch billing leaf from `CHAIN_PULL` (`@09ffccc6ef`, served to the runtime `14:03:13Z`);
`3.0.0_SA_CVO` graded it CLOSED-AT-EXERCISED (87477).

The `<status>` and `<dated>` fields still read "staged — DATED this week (08-20/21)". **Eleven
`<issuer_record>` entries dated 08-30 sit ABOVE that line in the same file, all authored by the same
issuer that quoted the stale field.** Two carriers in one document, disagreeing; the freshest eleven
could not correct the twelfth because nothing compares them. Remedy is a one-field issuer edit —
`2.0.0_SA_COO`'s, not mine. I did not edit the issuer's face.

**Acceptance 87474(ii) — DELIVERED, and it was one day overdue at this seat.** The first
single-writer day is **2026-08-31**:
- `s3://opal-data-inf/silver/api_dims/billing/snapshot_date=2026-08-31/data.parquet` — **ONE**
  version, 45,542 B, LastModified `11:18:10Z`, six seconds after the chain's own
  `[billing] OK: 911 rows` log line at `11:18:09.713Z`. The `~11:5xZ` second version present on
  08-29 and 08-30 is gone.
- **Arm A** vs the 08-30 certified write: 17-column denominator, 911 rows both, identical account
  set, **16 of 17 columns EQUAL cross-date**. The only differing column is `snapshot_date` itself,
  911 of 911 — it IS the partition key. Content-equal on every substantive column.
- **Arm B** vs the pinned stale `v=jCldmxzm` (34,039 B, 13 col): DIFFERENT, pre-registered delta
  landing exactly — only-in-new `{ending_mv_reported, ending_mv_source, ending_mv_status,
  period_start, period_end}`, only-in-stale `{is_fee_earning}`. Set-equal both directions.
  Equality here would have been the finding; it did not occur.
- Neither size nor ETag was used as an instrument — both were ruled wrong on this key (parquet is
  not byte-deterministic; equal size is not equal content). All four objects were downloaded and
  compared cell-wise.

**The discriminator, which is the part that matters.** ONE version is also exactly what a *crashed*
second writer produces. So I read the untouched keys on the same date as a positive control:
`performance` 2 versions (11:18:09 + 11:51:14), `tax_unrealized` 2 (11:18:11 + 11:48:52),
`tax_realized` 2 (11:18:11 + 11:48:52) — **the dispatch path RAN on 08-31 and wrote three keys.**
Billing is absent from exactly that run. The single-writer day is caused by the retirement, not by a
dead writer. Served runtime re-verified on two instruments (awk, then python after a stray shell
token polluted the first read): `orion-gold-dispatch.sh` ETag `46dce6c7f1ce4987bddf9a225efd733a` ==
the value recorded at the apply, 113,320 B, 0 CR, `CHAIN_PULL` 19 tokens,
`INF_API_SILVER_BILLING` once in the whole file at line 310 — the retained catalog row, absent from
`CHAIN_PULL`. Every pre-registered value reproduced.

**The proof instance did not exist.** The face has declared `OW-1..OW-6` and an `instance_path`
since 2026-08-18. The file was absent through both steps, the never-widen sign-off, AND the
grader's CLOSED-AT-EXERCISED verdict. Census before writing: `comp-find '*INF-ONEWRITER*' --all`,
63 hits over 145,246 files, no page truncation — every hit an inbox copy, the TO, or the ledger.
**This is the second instance of that exact absence on this project in 48 hours**; R-WATCH's was the
first (issuer_record 2026-08-30T03:1xZ). Written this session, VALID 6 of 6.

**OW-3 executed — the sweep found four more second-homes, not one.** DENOMINATOR 7 printed.

| builder | versions 08-31 | writers attributed | disposition |
|---|---|---|---|
| household | 0 | chain FAILS NoSuchKey; 1 partition ever (2026-04-28) | BROKEN-SOLE-PRODUCER |
| performance | 2 | chain 11:18:09Z + EC2 `INF_API_SILVER_PERF_DIM` 11:51:14Z | SECOND-HOME |
| activity | 0 | chain FAILS NoSuchKey; 92 partitions, newest 2026-08-14 | BROKEN-SOLE-PRODUCER |
| billing | 1 | chain 11:18:10Z only | SOLE-WRITER-KEEP |
| tax_unrealized | 2 | chain 11:18:11Z + EC2 `INF_API_SILVER_TAX` 11:48:52Z | SECOND-HOME |
| tax_realized | 2 | chain 11:18:11Z + the SAME EC2 `INF_API_SILVER_TAX` | SECOND-HOME |
| accounts_v2 | 2 | `inf-accounts-v2-daily` 11:07:39Z + EC2 11:34:25Z; **chain arm FAILED** | SECOND-HOME |

Tally: SOLE-WRITER-KEEP 1, SECOND-HOME 4, BROKEN-SOLE-PRODUCER 2. Read once unscoped: 13 prefixes
exist under `silver/api_dims/`; the 6 outside `SILVER_BUILDERS` are other paths' and are named so
that 7 is not mistaken for the population.

Two things the face gets wrong and the sweep corrects. **(a)** "the 3 of 7 that fail every day" is
one symptom over TWO mechanisms — household and activity are broken sole producers on missing
bronze; `accounts_v2` is a broken ARM of a key two other paths write successfully (served bytes come
from the EC2 leaf writing LAST at 11:34:25Z). One fix-or-remove applied to all three is wrong for at
least one. **(b)** NEW: `activity` was healthy until 2026-08-14 and has produced nothing for 18
days — a recent silent stop the daily-failure framing conceals. Reported, not chased.

**R-WATCH.** A1 watch day 2026-09-01 read at 08:18:45Z, 5 feeds, `IsTruncated` null on all five:
`fam` 20260810 (526 dirs) — **R HAS NOT FIRED**, 22 calendar / 16 trading days behind;
`acc`/`sec`/`rps` 20260828 (540 each), `slm` 20260828 (536). B1 is DISCHARGED — verified at the
artifact, not recalled: `PB-1` is PASS in the T-B instance with the byte limb scored on the 08-30
fire and the bytes pinned on the day. Andrew's reserved delete stays HELD; that row reports, it does
not release. **RW-1 gap, stated because a silent day and an unwatched day are the same shape:
2026-08-31 was NOT WATCHED** — no `~V` session existed between 08-30 ~18:15Z and this seating, and
an S3 listing is current-state only, so yesterday's frontier is not recoverable. Recorded as an
unwatched day, never as a no-change day.

## What I got wrong, and where it was caught

1. **I was one step from filing "the served `accounts_v2` writer is unguarded."** The chain's
   `NEVER_EMPTY_DIMS` 0-row guard — the one justified by the 2026-05-08 collapse that put
   $202,062,830 onto one advisor — does sit on the arm that fails daily, so it never executes, while
   the writer that actually serves the key is the EC2 leaf. That reads as a live safety gap. Opening
   the *builder* instead of the *dispatcher* found `convert_orion_api_to_silver.py:1119-1124`
   (ADHC_BUGB): an orchestrator-level 0-row REFUSAL covering every dim, broader than the chain's.
   **The live writer is guarded. No safety gap.** I had an absence and was about to give it a
   mechanism — absence-for-mechanism, refuted by one read before it left the seat.
2. **I minted two enum values and the checker refused both.** I scored OW-2
   `MET-BY-SUPERSEDING-REMEDY` and OW-4/5/6 `NOT-EXECUTED`. Neither is in the ratified status enum.
   Minting a value to fit my own reading is precisely the Rule-24 defect; the rows are now scored on
   the ratified enum with the qualification carried in `status_reason`.
3. **Three failed `send_message` calls** before the first report landed — I omitted the namespace
   prefix on the `body` parameter and misread the refusal as a content problem twice before reading
   my own call shape. The tool's refusal text was correct and specific each time.

## Findings raised

- **OW-2 is PASS on the outcome limb ONLY.** Its verbatim instructs removing `billing` from
  `SILVER_BUILDERS` — the act recorded WITHDRAWN and inverted. `billing` remains at
  `lambda_function.py:83` and that is now correct. Asserted: one version, canonical writer, clean
  stream. NOT asserted: that the fabric did what the row says. Issuer edit, not a measurer's
  re-scoring.
- **Rule-24 gap routed to `1.0.0_SA_CTO` as schema owner** (not a proposal — I hold neither the
  schema nor the four-postulate record): the status enum has no value for *declared, applicable,
  not yet executed*. That is the uncovered member under postulate (i). Cost measured today: three
  rows whose STATUS field is load-bearingly wrong while the truth lives only in `status_reason` —
  and the status field is what aggregates.
- `fee_amount` is EQUAL cross-date 08-30 → 08-31, offered not asserted. The open 120-cell difference
  was measured across a code change AND a date change; this pair moves only the date. That narrows
  the cause toward the vintage. It does not settle it and I did not close it.

## Blockers

**None.** Three items are bounded and owned elsewhere, none a stall: **OW-4** (consumer leg) needs a
word beyond this GO — a served-consumer code change with its own `change_management` entry; Step 1
CONFIRMED the mechanism so the gate is OPEN, not blocked on evidence. **OW-5** is sequenced behind
OW-4 (CLOSED-BY-MECHANISM would be a false record while the consumer is unfixed). **OW-6** routes to
Andrew via the CTO's residual bank and is not mine to send. The 08-12 served defect is NOT fixed —
the silent `.get(is_fee_earning, 0.0)` default is still there.

## NEVER#1 resolution (the finding the calendar refused)

All four sibling denominators were IDENTICAL to the 08-30 read (540/540/540/536) — nothing landed
across Monday 08-31, which reads as frozen. **It is not.** Measured delivery lag from the object
`LastModified` series: partition D lands D+1 at ~09:46Z (20260828 landed 2026-08-29T09:46:34Z; the
same minute seven days running), and Sat/Sun produce no partitions. The next landing is Monday's
partition today at ~09:46Z — 1 h 27 m after my read. The siblings are 2 trading days behind the
CALENDAR frontier and **0 behind the DELIVERY frontier**. Friday IS Monday's answer. No finding. It
becomes one only if 09:46Z passes empty; re-read at a turn-top, never a loop, and no monitor built.

## Files Modified

See commit messages: `61aabf2ee1`, `9f134aaf3d`.

| File | Note |
|---|---|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/OPAL_ADVIPOINTERS.INF-ONEWRITER_PROOF_OF_SPEC.json` | NEW. The instance that never existed. VALID 6/6. |
| `infra/system/06_current_state.{md,json}` | Regenerated to discharge the two-phase override. |

## Deploys

**None.** No deploy, no producer edit, no vendor call, no monitor, no alarm. The GO authorised
SEATING and READING; every act this session was a read or a record. The `NEVER#2` ledger for Step 2
was opened and closed by `0.7.0_AE_CloudOps` on 2026-08-30 and needed nothing from this seat.

**Audited override, taken and DISCHARGED in-session:**
`system-current-override: STRUCTURAL-TWOPHASE/proof-of-spec` at `61aabf2ee1` — comp-system counts
the new deliverable as a `_SOURCE` (file_count 260 → 261) but refuses to compile an UNCOMMITTED
source, so the regen the gate demands cannot run before the commit lands. Each gate correct, each
pointing at the other. Discharged at `9f134aaf3d` (`as_of HEAD=61aabf2ee1` — the artifact's stamp
names the commit that introduced the drift, not a later head that merely contains it).

**Push state, MEASURED:** both commits **LOCAL ONLY**. `origin/CLOUD` reads `a29c2591ae`
(`ls-remote`, 08:52Z); `merge-base --is-ancestor` returns false for both. Not pushed — the seating
brief names integrator-only push.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-read` | both TO faces; `inf-silver-chain/lambda_function.py`; `convert_orion_api_to_silver.py`; `proof-of-spec-check.py` | PASS | Load-bearing twice — see below. |
| `comp-find` | `--name 'OPAL_ADVIPOINTERS*' --files`; `--name '*INF-ONEWRITER*' --all` | PASS | The `--all` sweep IS the evidence for the instance's absence: 63 hits / 145,246 files, no truncation. |
| `proof-of-spec-check` | `<instance> OW-1..OW-6` | PASS | VALID, violations=0, rc=0 read UNPIPED, positional form, checker vintage `eefe9e0a91`. First run INVALID with 8 violations — see "What I got wrong" #2. |
| `lib.trading_calendar` | `is_trading_day` / `expected_last_trading_day` / `trading_days_behind` | PASS | Refused a finding I was about to file. |
| `safe-commit.sh` | 2 commits under this author line, `-F` message files written by the Write tool | PASS | `msg-verify MATCH` on both (len 4609, 1138). |
| `comp-system` | regen `06_current_state` | PASS | Discharge of the two-phase override. |
| `comp-blast` / `comp-pipescript` / `comp-estate` | not run | N/A | Named rather than omitted: this session changed no code, no infra, no pipeline. Rule 20 binds cloud/infra/data changes and frontend commits; none applies. |

**What worked.** `comp-read` on the INF-ONEWRITER face surfaced eleven 08-30 `issuer_record`
entries sitting ABOVE the `<status>` line the issuer had quoted as current — that is the whole
premise inversion, and a grep for the status token would have returned the stale line and nothing to
contradict it. It earned the swap on this file. `comp-read` on `convert_orion_api_to_silver.py`
located the ADHC_BUGB guard that refuted my own alarm.

**What failed.** Nothing on the tools. The `send_message` failures were mine (missing namespace
prefix on `body`), and `awk` mangled an escaped quote in the `CHAIN_PULL` count, which is why that
number was re-derived on a second instrument before it was quoted anywhere.

**Gap found.** `commit-gate` reported "checked 0 of 1" and "0 of 2" on both commits — `.json` and
`.md` are not gated suffixes. The gate says so loudly and correctly; recorded here because a reader
must not read those commits as gate-validated. The language-appropriate instrument was
`proof-of-spec-check`, and it is cited instead.

## MCP traffic

4 messages total. IN: 91058 (`2.0.0_SA_COO`, the seating GO — ACKed). OUT: 91072/91073 (the RAVC +
acceptance report to `2.0.0_SA_COO` + `1.0.0_SA_CTO`), 91154/91155 (the acts-complete follow-on with
the OW-3 table and the Rule-24 routing).

## Next Steps

1. **[`2.0.0_SA_COO`]** One-field edit to the INF-ONEWRITER face: `<status>` / `<dated>` still read
   "staged — DATED this week (08-20/21)" above eleven of the issuer's own 08-30 records. Also OW-2's
   verbatim, which still instructs the withdrawn-and-inverted remedy.
2. **[`1.0.0_SA_CTO`]** The Rule-24 enum gap (no value for *declared, applicable, not yet
   executed*), and the OW-3 table the face says the CTO reads — including the `activity` silent stop
   since 2026-08-14 and the four surviving second-homes.
3. **[Whoever holds the word]** OW-4, the consumer leg. The gate is open; the 08-12 served defect is
   still live.
4. **[`0.4.0_DS_ClientPlatform~V`]** Re-read the R-WATCH roster after ~09:46Z today. If 20260831 has
   not landed for the four siblings by then, that IS the new differential finding; until then it is
   not-yet-due.
