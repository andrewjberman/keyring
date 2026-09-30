# AMGT_CORPUS task order -- `CRPS-w-3` -- ROUND 21: a unit-map discriminator that does not rest on magnitude alone, and never guesses

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-w-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 raw reads only (bronze refdata/histdata/bestdata).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 21. Serves **the served unit on the six names whose units the map could
not measure**.

## 1. THE CELL -- `CRPS-w-3`

**Where this came from.** `integrations/bloomberg/research/build_unit_map.py` classifies a field's unit by comparing ONE
sampled magnitude against the field family's known scale (`classify_unit`). For large-number currencies (JPY, TWD) that
comparison cannot tell absolute from millions, so `integrations/bloomberg/research/field_map.json` holds nine facts as
`UNRESOLVED-ON-<security>: sampled magnitude N does not discriminate absolute vs millions`:
- `SALES_REV_TURN`: `6501 JP Equity`, `8316 JP Equity`;
- `CURR_ENTP_VAL`: `6501 JP Equity`, `9433 JP Equity`, `8035 JP Equity`, `8766 JP Equity`, `TSM US Equity`;
- `NET_DEBT`: `8316 JP Equity`;
- `BEST_SALES`: `6501 JP Equity` (a per-security exception under a scalar field).

The CTO ruled (round-20 analysis addendum) that this project builds a discriminator from a CROSS-FIELD consistency read. For
example, enterprise value against price x shares from resolved fields, or revenue against resolved per-share figures x shares.
A name the read cannot decide stays UNRESOLVED and is never guessed.

The map's MEASURED anchors include:
- `CUR_MKT_CAP`, scalar `ABSOLUTE (full currency units)`;
- `PX_LAST` (per-share price, local trading currency);
- `IS_SH_FOR_DILUTED_EPS` (per security).

Read each anchor's per-security status for the name before relying on it: an anchor that is itself unmeasured on that name
cannot resolve anything.

**RULED -- what you build:**
1. In `build_unit_map.py`: `discriminate_facts(facts, s3=None) -> list[dict]`, where `facts` is a list of `(security,
   mnemonic)` tuples.
   - Read each name's raw through the module's own `load_raw_for_key(s3, security_key(security))` and `prepare_header(...)`
     (S3 reads only).
   - Return one dict per fact: `{"security", "mnemonic", "state": "RESOLVED"|"UNRESOLVED", "unit"` (the map's unit label,
     e.g. `MILLIONS` or `ABSOLUTE (full currency units)`, when RESOLVED)`, "evidence"` (when RESOLVED: the fields, values,
     ratio and the band that decided it)`, "reason"` (when UNRESOLVED)`}`.
2. **The rule: never a guess.**
   - A fact is RESOLVED only when a cross-field ratio falls inside the band of exactly ONE unit hypothesis. The two hypotheses
     are 1e6 apart; state the bands in the code.
   - A missing or unmeasured anchor, a ratio in no band, or a ratio in more than one band leaves it UNRESOLVED with that
     reason.
   - Magnitude alone never decides.
3. `integrations/bloomberg/research/tests/test_build_unit_map_discriminate.py` (new), with stub raw and no network:
   - a consistent millions case resolves;
   - a consistent absolute case resolves;
   - a PLANTED inconsistent case (a ratio in no band) stays UNRESOLVED;
   - a missing anchor stays UNRESOLVED.
   Keep the builder's three suites green.
4. Do NOT write `field_map.json` and do NOT run the CLI's real write. A unit-map commit and any re-derive are the issuer's acts
   under a pair.

## 3. SURFACES

<paths>
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_build_unit_map_discriminate.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-w-3.unit-map-cross-field-discriminator.md
</paths>

READ-ONLY: every other file (`field_map.json` NEVER written; `model_block_pull.py` read-only), every S3 object. Scratch
`.scratch/w3/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`); `data/`, `portal/` and the rest of
`infra/` are absent by design. If you need a path outside the cone, file a row and stop that criterion; never disable the sparse
checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible (no `newline=` on a `Path` text call).
- NO vendor call, NO S3 write, NO write to `field_map.json`.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-w-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round21/w3_AC1.sh</invocation><expect>(?m)^w3 facts 9 of 9 answered resolved (\d+) unresolved (\d+) resolved_with_evidence \1 unresolved_with_reason \2 control SAP_GY_CURR_ENTP_VAL MILLIONS agrees True$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-w-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round21/w3_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: all nine facts answered. Every RESOLVED fact carries a unit and evidence, and every UNRESOLVED fact a reason; the counts
  are yours to report, and the AC does not demand any fact resolve. The MEASURED control (`SAP GY Equity` `CURR_ENTP_VAL`,
  MILLIONS in the map) is re-derived as MILLIONS by your read.
- AC2: your tests (the planted inconsistent case included) with the builder's three suites.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-w-3.unit-map-cross-field-discriminator.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE: each AC line, the `FACT` lines `w3_check.py` prints (all nine plus the control), and the bands you set.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-20 analysis ADDENDUM @`7708a8506f` (msg 26893), cell 3. Dry-run at base CLOUD `f17ca57280`:
- w3_AC1 FAIL as expected: AttributeError, no `discriminate_facts`; no `w3` line.
- w3_AC2 FAIL as expected (no tests ran).

The AC deliberately does not require any fact to resolve: "never guessed" means an honest 0 of 9 passes, and a forced
resolution would be the defect. The control proves the read discriminates where the answer is known.
<risk>LOCAL</risk>
<status>pending</status>
<round>21</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
