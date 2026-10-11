# MDPF_CANON task order -- `CN-c-1` -- THE COMBINED SLICE'S BASIS, MADE TRUE (M7 recut, FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-c-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~8</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE a document and one ledger citation; no IAM is read or changed.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r3_checks.py basis 0 of 3 at base (the file is absent); a reference tree reads 3 of 3 (the arms can pass).
EGRESS CLASS, declared: NONE (the worker reads S3 and writes no AWS).
</preflight>

## 1. THE CELL -- `CN-c-1` (round 3, decomposition v3)

The round-2 basis (`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~5/X2_GLOBAL_BASIS.md`, read-only: do not edit it) asserts that
every combined (`global`) figure sums at least 2 firms. The CTO's read of the producer's own `global` output on 2026-10-08 found that
the written reason does not match what is emitted: 12 `by_model` entries are held at ONE firm (6 of them at 3 or fewer accounts,
each value equal to that firm's), and two series are one firm's alone (`non_model_aua`, `inflection_non_model_aua`).

Write a NEW basis that is true of the output, at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~8/X2_GLOBAL_BASIS.md`.
It is a plain statement of what is emitted. It does NOT argue the figure is safe and it does NOT propose a fix (that is Andrew's call).

**As-of is fixed: 2026-10-08.** Read these objects (read-only `get`), bucket `opal-data-assets`, for each scope in `global`, `49financial`,
`inflection`, `cottonwood`:
- `portal/gold/mdpf/<scope>/aum-metrics/2026-10-08.json` (top-level `by_model` is a LIST of `{model_name, account_count, aum, ...}`);
- `portal/gold/mdpf/<scope>/account-distribution/2026-10-08.json` (top-level `by_model` is a DICT keyed by model name; each value has
  `account_count`; the date may be 2026-10-09 for a scope that has no 2026-10-08 object: say which object you read);
- `portal/gold/mdpf/<scope>/aggregate-aua-timeseries/2026-10-08.json` (series keys at the top level, among them `by_model`,
  `non_model_aua`, `inflection_non_model_aua`).

Document three headings, in this order, and the two header lines `AS-OF: 2026-10-08` and `DENOMINATOR: <what you counted>` above them
(the denominator names the number of `global` `by_model` entries read and the number of series keys read):

1. **Field families** -- one table. Header cells exactly: `family | min firms | entries | evidence`. One row each for `headline sums`,
   `by_model`, `non_model_aua`, `inflection_non_model_aua`. `min firms` is an INTEGER: the fewest firms (of the three firm scopes)
   that any entry of that family combines at the as-of. `entries` is how many entries of the family you read. `evidence` is the object
   key and field path.
2. **Single-firm entries** -- every `global` entry whose value is one firm's value: entry name, the one firm, and that entry's
   `account_count`. Print the count of such entries and the denominator (entries read). No account id and no dollar figure appears.
3. **Method** -- how a `global` entry was matched to each firm scope (how model names were matched if they differ between scopes),
   what counted as "held at a firm" (a nonzero `account_count`), and what you could not read.

Then in `infra/logic/06_CONFORMANCE_LEDGER.md`, the X2 row cites the new file's path in place of the round-2 path. Do not change the
row's status: moving X2 from OWED to GRANTED is Andrew's acknowledgement, not this cell's.

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`/`rm`, no IAM call. A read-only `get`/`describe`/`head`/`list`
   is allowed. No install, no push. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **CLIENT DATA:** never print a client figure or an account id. Counts of accounts per entry are allowed; dollar values are not needed.
4. If a model name cannot be matched across scopes, say so in Method and count it as read-and-unmatched; never guess a match.
5. Keep each file's line endings as you find them (read them first). No non-ASCII. Use the Edit tool for existing files.
6. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
infra/logic/06_CONFORMANCE_LEDGER.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~8/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` (the global fold),
`data/mdpf/scripts/gold/mdpf_model_registry.json`, and the round-2 basis above. The issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round3/checks/r3_checks.py` is also read-only (never edit it).

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-c-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round3/checks/r3_checks.py" basis; echo "exit=$?"</invocation><expect>ROUND 3 BASIS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-c-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round-3 close (never self-graded): a seat that did not write the file reads the same objects at the same
as-of and reads back every `min firms` integer and every single-firm entry's account count equal.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~8/MDPF_CANON.TO-CN-c-1.proof_of_spec.json`, with AC3
UNVERIFIABLE-BY-INSTRUMENT and status_reason "graded at the round-3 close". **Flip this order's `<status>` to `complete` in the SAME
commit as your proof instance**, and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W8-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at
filing. Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 3 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round2.md` @71e85b7191 section 3 item 2. Issued after Andrew
lifted the dell1 hold (CTO msg 3378, record commit cbcfdc0c1c). Base box/dell1. LF only. Whether FWD-3 can be REALIZED on a true basis is
Andrew's call at section 4 of that analysis; this cell is needed under either option.

<status>complete</status>
<round>3</round>
<to_id>MDPF_CANON.TO-CN-c-1</to_id>
<slot>~8</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
