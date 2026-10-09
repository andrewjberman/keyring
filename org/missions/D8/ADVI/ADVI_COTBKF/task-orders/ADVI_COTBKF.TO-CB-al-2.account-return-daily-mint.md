# TO ADVI_COTBKF.TO-CB-al-2.account-return-daily-mint -- round 38 CB-al-2: mint Cottonwood account_return_daily under a never-widen pair

<to_id>ADVI_COTBKF.TO-CB-al-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~CB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>38</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-al-2` (`decompositions/ADVI_COTBKF_DECOMP.round38.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-al-1, both pair halves, any BLOCKING gap ruled

---

## WORKER FACE

### THE CELL

Round 38's `CB-al-1` builds Cottonwood's `account_return_daily` partitions locally:
- files at `.scratch/advi_cotbkf/ard_cottonwood/date=<D>/data.parquet`;
- a manifest with each file's sha256;
- built through the table's one producer, `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, with its schema and
  `emit_day(upload=False)`.

The target prefix `s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/` holds 0 objects, so this write MINTS new
keys.

**Your item. Do not start until this order's AMENDMENT names both pair halves and CB-al-1's drained manifest.**

1. **Pair first:**
   - the COO half signed by `2.0.0_SA_COO~C2` and the CTO half by `1.0.0_SA_CTO~DELL2`;
   - the blast radius is exactly the day prefixes listed, both files each;
   - the rollback deletes exactly those minted keys. A delete of a key this act minted, with no prior version, is the pair's own
     rollback; it is not a deletion of standing data.
2. **Open the ledger** with `deploy_ledger.py open`, which commits its own files.
3. **Re-list the prefix** and STOP if any key now exists.
4. **Land each day** through the producer's `emit_day(upload=True)`. Read back each `data.parquet`, and confirm its sha256 equals
   the manifest's.
5. **Close the ledger** with the day count and the read-back result.

**AMENDMENT 1 (issuer, 2026-10-09 ~13:5xZ) -- HELD on row D2-W66-S1 (BLOCKING).** The producer's `emit_day(upload=True)` writes a
`manifest.json` whose method text and `method_version` state the CUSTODIAN method. FWD-3's Cottonwood rows are positions x as-traded
close, after fees, so landing them through `emit_day` unchanged would publish a false claim. This order does NOT run until both:
- IRPT_DASHBD changes its producer, with either a truthful `return_basis` value plus a method row, or a Cottonwood `sources.json` entry
  with a manifest-text parameter;
- the CTO rules on it.

The gap is routed to `1.0.0_SA_CTO~DELL2`. A hand-written manifest or a second writer is never the workaround.

**AMENDMENT 2 (issuer, 2026-10-09 ~14:0xZ) -- the gap is ruled; this order is still HELD.** CTO msg 3414 / IRPT_DASHBD ADDENDUM 13.1
@49293e07e9 rules:
- IRPT_DASHBD's per-firm sources entry gains the structured fields `valuation_source`, `fee_treatment` and `price_basis`.
- The manifest never defaults; a firm with no entry writes `absent`.
- `return_basis` stays `TWR` or `NOT_MEASURABLE`, with no enum edit.

That cell is `2.0.0_SA_COO~D2`'s. This order waits until it drains. Then the issuer re-points the build: the adapter sets
`return_basis=TWR` on measured rows, and the Cottonwood sources entry carries the method fields. A rebuild and a fresh manifest
follow before any pair is asked.

**AMENDMENT 3 (issuer, 2026-10-09 ~14:5xZ) -- still HELD, on a second IRPT_DASHBD producer cell.** CTO msg 3500 / IRPT_DASHBD
ADDENDUM 13.2 @304cb81ef6: CB-al-2 is NOT minted as built.
- The producer's `build_manifest()` writes `method_version: 2` (the custodian-equity row) into every manifest. That is row W70-S1.
- `2.0.0_SA_COO~D2` cuts one LOCAL producer cell in which `build_manifest()` takes `method_version` from the firm's sources entry:
  - a positions-based entry gets its own method row, with its rule-24 record;
  - a firm with nothing declared writes `absent`, never 2;
  - the custodian firms keep 2 explicitly.
- When that cell drains, the issuer rebuilds through it from round 43's entry (adding the entry's method row reference if the cell
  requires one) and writes the pair on the rebuilt manifests. Then this order runs under that pair.

**AMENDMENT 4 (issuer, 2026-10-09 ~16:0xZ) -- the content and apply path are ready; the COO half is GIVEN; waits ONLY on the CTO half.**

- **Content:** round 47 (method_version 3, drained @9c6b230812) and round 49 (`--apply`, drained @26cf9c42db).
- **COO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R38_ARD_COTTONWOOD_MINT_COO_HALF.md`.
- **The act, once the CTO half is cited by AMENDMENT 5:**
  `python data/assets/scripts/silver/commonwealth_account_return_daily.py --apply --pair <COO half> --pair <CTO half>
  --manifest org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~74/ard_cottonwood_manifest.json`.
  - The local files are under `.scratch/advi_cotbkf/ard_cottonwood_r47/` in the shared tree.
- **Acceptance** becomes `--verify-served --manifest <the same manifest> --out .scratch/advi_cotbkf/ard_cottonwood_verify`, with
  `ARD-COTTONWOOD-VERIFY days=3325 match=3325/3325`. The criterion's bar (`ARD-COTTONWOOD-VERIFY days=`) is unchanged.
- **Rollback is NOT a delete.** The minted keys stay unread behind the reader gate, and their list goes to the ledger for Andrew.
  The BOUNDS line "Delete only the keys this act minted" is struck.

### ACCEPTANCE

<criterion id="CB38al2-AC1" cell_refs="CB-al-2"><invocation>python data/assets/scripts/silver/commonwealth_account_return_daily.py --verify-served --out .scratch/advi_cotbkf/ard_cottonwood_verify</invocation><expect>ARD-COTTONWOOD-VERIFY days=</expect></criterion>
`CB38al2-AC1` -- every minted day reads back equal to its local file. The `--verify-served` mode is added by CB-al-1, or by the
amendment that releases this order.

<expected_criteria>CB38al2-AC1</expected_criteria>

## BOUNDS

- **Grant.** Exactly the listed day prefixes (`data.parquet` and `manifest.json` each), the ledger files for this deploy, and this
  order's file.
- **Pair first.** No write before both halves exist and this order's amendment cites them.
- **Refusal clause.** If a key exists at write time or a read-back differs, stop. Delete only the keys this act minted, write the
  reason in the ledger, and file a NEW surprise row (id `ADVI_COTBKF-D2-WCB2-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your repo WRITE grant. The S3 grant is the listed day prefixes.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round38.md</decomp_doc> (round 38), cell `CB-al-2`.
<owned_cells>CB-al-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB38al2-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-al-2.account-return-daily-mint.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB38al2-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the pair files; the ledger entry; the day count; the first and last key; the read-back result.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time mint; a daily schedule for Cottonwood is IRPT_DASHBD's.
comp-iam: RUN at apply time -- the dell2 identity's PutObject under opal-data-cottonwood irpt/cottonwood/gold/account_return_daily/; BLIND: none beyond the listed prefixes.
comp-adversary: RUN -- pair before write; empty-prefix re-list; the producer's own emit_day; sha256 read-back; BLIND: a reader before its own pair (the CTO's gate).
lane: SERVED write by the box applier; the issuer signs the COO half on CB-al-1's manifest.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 11.2 @43bbe32935 (msg 3363).
