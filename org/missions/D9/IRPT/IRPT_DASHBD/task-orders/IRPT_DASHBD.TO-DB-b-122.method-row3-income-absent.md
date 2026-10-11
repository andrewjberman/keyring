# TO IRPT_DASHBD.TO-DB-b-122 -- method row 3 states income ABSENT by design, with its reason; row 2 unchanged and a test shows it; contract 0.6.0; the never-widen packet for the one served object (no S3 write here)

<to_id>IRPT_DASHBD.TO-DB-b-122</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~97</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>66</round>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 4634 (2026-10-11 ~09:55Z): "version 3's method row states income ABSENT by design with its reason (FWD-3 does not separate income; it sits inside the value through the cash leg); versions 1 and 2 are unchanged and a test shows it. It rewrites one served object, so it comes with a pair" | **Decomp cell:** `DB-b-122` (decomposition section 68) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-120 (complete).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-97` (branch `wk-irpt-dashbd-66-97`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~97/`.

**The defect.** `emit_method_row` in `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (near line 1948) writes
`"income_basis": "cash_when_received"` on EVERY method row (line ~1969). For method row 3 (positions-based; the Cottonwood table minted by
ADVI_COTBKF) that is false as served: the two income columns of that table are null on every row, because the method does not separate income --
it sits inside the value through the cash leg. A method row is what a reader rejects on; today it states something the table does not do.
Zero readers bind income today.

**The cell (`DB-b-122`), in this order:**

1. **Rule-24 record FIRST, before any code** (`METHOD_ROW3_INCOME.json`, key `rule24`: `mece`, `same_grain`, `intent_coherence`,
   `state_coherence`, each {finding, evidence: [{file, line}]}; and `token_census`). The shape to record and then build:
   - `income_basis` becomes a per-row fact carried by `METHOD_ROWS` (row 2: `cash_when_received`; row 3: no value).
   - Two new columns on the method row, following the claim pattern DB-b-118 and DB-b-120 already use on this table:
     `income_basis_claim` (the producer's existing `THRESHOLD_CLAIMS` vocabulary: `absent` for row 3; for row 2 the claim that is TRUE of a
     stated method choice -- decide which of measured / inferred / held and say why in the record) and `income_basis_reason` (row 3: the
     reason in plain words, as the CTO states it; row 2: null).
   - NO new enum value is minted: `absent` is already in the vocabulary. If your record finds this shape fails a postulate, STOP with a row
     and build nothing; do not invent a different shape.
   - The token census is word-boundary, over the repo, for `income_basis`, `cash_when_received`, `income_basis_claim`, `income_basis_reason`
     (`comp-find -i` with its denominator printed; never piped into head): who writes and who reads each.
2. **The producer.** Row 3 returns `income_basis` None, `income_basis_claim` `absent`, `income_basis_reason` non-empty. Row 2 returns
   `cash_when_received` exactly as today. `income_basis` and the two new columns land TYPED as string (a null never lands as the null type; see
   how `typed` is built near line 2008). Every one of the 29 existing columns stays, with the same value it has today for the same input.
   The legacy call `src=None` (row 2) behaves as row 2.
3. **A test** in `data/assets/scripts/gold/irpt_reporting/tests/` (a new file): row 2's dry-run row, for a fixed thresholds input, equals a
   pinned expected on all 29 pre-existing columns except `measured_at`; row 3 states income absent with its reason; a row 3 carrying a value
   under the claim `absent` is refused (follow the existing refusal for the tie-out near line 1944). Run the folder's existing tests too:
   none may newly fail (record passed / failed, and which failed before you started, measured before your first edit).
4. **The contract** `org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json` to 0.6.0: `income_basis` nullable true with its meaning
   restated; the two new columns; `schema_hash` recomputed the way the file's own rule states (sha256 over the sorted `name:type` lines joined
   by a newline); the example rows and the token census text brought in line; a changelog entry citing CTO msg 4634. Follow the 0.5.0 entry's
   shape exactly.
5. **The never-widen PACKET, and NO S3 write.** `NEVER_WIDEN_PACKET_METHOD_ROW3_INCOME.md` in your folder, for the later act of rewriting the
   ONE served object, the Cottonwood `dim_return_method` partition `method_version=3`:
   - `object_address`: the address your own dry run returns for the row-3 entry (it is `lib/opal_naming.py address()` output; never typed).
   - The live object as it is now: ONE `head-object` or `list-objects-v2` on that exact prefix (key, size, last-modified, version id if the
     bucket is versioned), through the `.tools/aws` shim. If the read is denied, record the denial verbatim; do not widen and do not retry
     another way.
   - WRITERS of that object, counted and named with file and line (N writers = N rules read): at least this producer and whatever ADVI_COTBKF
     path minted it (`commonwealth_account_return_daily.py` is where to start). READERS, counted the same way; zero is a value, with the
     denominator of the search printed.
   - The exact before row and after row side by side (the dry run's), the columns that change (3) and the 29 that do not.
   - Blast radius and rollback per key (the prior version id, or the prior bytes' sha256 and how they are restored), and which act lands it
     and who verifies (2.0.0_SA_COO~C2's read-back, per the CTO).
   - The record's `packet` {path, sha256, object_address, writers_counted, readers_counted, rollback} and `s3_writes: 0`.

<criterion id="DB66-1-AC1" cell_refs="DB-b-122"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r66/p66_round66.py" . DB66-1-AC1</invocation><expect>DB66-1-AC1 PASS</expect></criterion>
`DB66-1-AC1` -- row 3 states income absent with a reason and lands typed; row 2 still reads cash_when_received with a true claim; all 29 earlier columns are kept. Base: FAIL.

<criterion id="DB66-1-AC2" cell_refs="DB-b-122"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r66/p66_round66.py" . DB66-1-AC2</invocation><expect>DB66-1-AC2 PASS</expect></criterion>
`DB66-1-AC2` -- contract 0.6.0 equals the row, with its rule-24 record, token census and a passing new test. Base: FAIL.

<criterion id="DB66-1-AC3" cell_refs="DB-b-122"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r66/p66_round66.py" . DB66-1-AC3</invocation><expect>DB66-1-AC3 PASS</expect></criterion>
`DB66-1-AC3` -- the packet names the one object by the builder's address, counts its writers and readers, states the rollback, and nothing was written to S3. Base: FAIL.

<expected_criteria>DB66-1-AC1,DB66-1-AC2,DB66-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call. AWS reads are limited to the ONE
  object read item 5 names. No read of any returns-gold body. No vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant is a defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W97-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~97/
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/
org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-122.method-row3-income-absent.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 68 (round 66), cell `DB-b-122`.
<owned_cells>DB-b-122</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB66-1-AC1,DB66-1-AC2,DB66-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~97/IRPT_DASHBD.TO-DB-b-122.method-row3-income-absent.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB66-1-AC1,DB66-1-AC2,DB66-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the rule-24 findings in one line each and the claim chosen for row 2 with why; the before and after of row 3's three income members; the tests (passed, failed, failing before you started); the contract's new version and hash; the packet -- the object's address, what the one live read returned, the writers and readers with their counts, the rollback; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; the cell writes nothing served, and the packet's own writer and reader counts are the blast read the later act is signed on.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: one read of one object through the worker's own credentials; a denial is recorded, not worked around.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the producer's scheduled fire runs from source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the base state is measured by the check's own dry run, all three criteria FAIL at base.
lane: the <paths> block IS the grant.
</preflight>
