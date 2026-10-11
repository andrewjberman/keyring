# MDPF_CANON task order -- `CN-d-2` -- THE X2 BASIS COUNTS A `count_as_of` ENTRY AS A CARRY AND LISTS EACH WITH ITS AGE (W8-S2; FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-d-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~11</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell writes a document and one ledger citation.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell reads served objects with read-only gets and changes no policy.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r4_cn_d_2.py reads 1 of 4 arms at base (arm B2, the data property, is a control that holds today) and 4 of 4 on a reference tree (the arms can pass).
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-d-2` (round 4, decomposition v4)

The round-3 basis (`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~8/X2_GLOBAL_BASIS.md`, read-only: do not edit it) is true of the
output, and it counts two `global` `by_model` entries (`opal_growth_sma`, `opal_div_sma`) as "held by no firm", so its `by_model` family
reads `min firms 0`. Those two entries are not an accident: the producer carries the last known account count forward for exactly those
two keys when the count source cannot supply a frontier count, and each entry WEARS the date of that count in its own `count_as_of` field
(`SMA_COUNT_PRESERVE_KEYS`, `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` about :1679; ruled by the CTO 20260723T051427Z, a lagged
count wearing its date is honest). The CTO has ruled (ADDENDUM 1 @187b53dbe6) that the fold does not change and the BASIS states this.

Write a NEW basis at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~11/X2_GLOBAL_BASIS.md`, built the way the round-3 file is
built (read it first: same as-of, same twelve objects, same three headings, same match rules and the same two header lines), with these
changes and no others:

1. **The rule.** A `global` aggregate-aua-timeseries `by_model` entry that carries a `count_as_of` key is a CARRY: it is a lagged count of a
   firm that is no longer reporting that entry, not a firm holding it at the as-of. A carry is NOT counted in `min firms`, and it is NOT counted
   among the held entries. State this rule in `Method`, citing `SMA_COUNT_PRESERVE_KEYS` and the CTO's ruling date above.
2. **Field families.** Recompute the `by_model` row's `min firms` over the entries that are held (nonzero `account_count` at a firm scope, as
   in round 3) and say in `evidence` how many entries are carries and that they are listed under `Carries`. Keep the other three rows as they
   are. The `DENOMINATOR:` line states how many entries were read, how many are held and how many are carries.
3. **A new heading `# Carries`** (between `Single-firm entries` and `Method`): one table with the header cells exactly
   `entry | display name | count at as-of | count_as_of | age in trading days | firms holding it at the as-of`. One row for EVERY `global`
   aggregate-aua-timeseries `by_model` entry that wears `count_as_of` and has a nonzero count at the as-of. `age in trading days` is the
   number of trading days in the interval (`count_as_of`, as-of], counted with `lib/trading_calendar.py` `trading_days_between(count_as_of
   + 1 day, as-of)`: print the integer. `firms holding it` is the list of firm scopes whose own object holds the SAME key at a nonzero
   count at the as-of (write `none` when there is none). Print the number of carries and the denominator (entries read) under the table.
4. **The close statement** (one paragraph under the table): every `by_model` entry of the global aggregate-aua-timeseries object with a
   nonzero count at the as-of is either held by at least one firm scope or wears `count_as_of`, and every one that wears it is in the table.
   If that is not true of what you read, say which entry breaks it and file a BLOCKING row; do not soften the sentence.
5. **The ledger citation.** In `infra/logic/06_CONFORMANCE_LEDGER.md`, the X2 row's `written basis:` path changes from the `~8` path to the
   `~11` path, by exact string replacement on that row only. Do not change the row's status, decider or date.

Do not describe whether a 2026-07-17 carry should still serve: that is part of Andrew's X2 call (open call fe9b), not this cell's.

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`/`rm`, no IAM call. A read-only `get`/`describe`/`head`/`list`
   is allowed. No install, no push. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **CLIENT DATA:** never print a client figure or an account id. Counts of accounts per entry are allowed; dollar values are not needed.
4. If a model name cannot be matched across scopes, say so in Method and count it as read-and-unmatched; never guess a match.
5. Keep each file's line endings as you find them (read them first). No non-ASCII in the new file. Use the Edit tool for the ledger row.
6. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
infra/logic/06_CONFORMANCE_LEDGER.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~11/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular the round-3 basis above, `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` and
`lib/trading_calendar.py`. The issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_2.py` is also read-only (never edit it).

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-d-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_2.py"; echo "exit=$?"</invocation><expect>ROUND 4 CARRIES: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-d-2" judgment="true"/>
</proof_of_spec>

AC2 is JUDGMENT, graded at the round-4 close (never self-graded): a seat that did not write the file reads the same objects at the same
as-of and reads back every `min firms` integer, every carry row (entry, `count_as_of`, age) and every single-firm entry's account count equal.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~11/MDPF_CANON.TO-CN-d-2.proof_of_spec.json`, with AC2
UNVERIFIABLE-BY-INSTRUMENT and status_reason "graded at the round-4 close". **Flip this order's `<status>` to `complete` in the SAME commit as
your proof instance**, and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W11-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round3.md` @ae094ea51d section 3 item 2 AC1 as re-cut by
ADDENDUM 1 @187b53dbe6. Slot ~11, its own chain (a document and one ledger cell; it shares no file with `CN-d-1`). It moves no served output.
FWD-3 stays NOT REALIZED until Andrew's X2 call fe9b whatever this cell reads. Base box/dell1. LF only.

<status>staged</status>
<round>4</round>
<to_id>MDPF_CANON.TO-CN-d-2</to_id>
<slot>~11</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
