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

**AMENDMENT 5 (issuer, 2026-10-11T06:16Z) -- RELEASED on both halves. This amendment supersedes AMENDMENTS 1 to 4 and the "Your item", the criterion sentence and the BOUNDS wherever they differ.**

- **COO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R59_ARD_COTTONWOOD_MINT_COO_HALF.md` @0865081982, file sha256 `351dad12c2ae18b31367a95cce3ecb892cefb9fb461cc015cbddb4ada137a115`.
- **CTO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R59_ARD_COTTONWOOD_MINT_CTO_HALF.md` @f2415a44b5, file sha256 `7bb0562c1140578803371cc7644f57dd27f71a1cc5646acb0ed7b03589dcc015` (re-signed on the COO half's sha256 above; CTO msg 4253).
- **Pins.** Adapter `data/assets/scripts/silver/commonwealth_account_return_daily.py` sha256 `38f06ba93cc82318d3fd7bc587baac2184acb03f9c9b7e4809acba4afcbb51c9`; manifest `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json` sha256 `d2d99d5c4a127635170f77516b52fdfc0c163e151e39649e35569a601ce47b36`. **Hash all four files before you start; if any differs, STOP and report the four hashes.**
- **Where.** The BASE checkout `C:/dev/ajb_workspace` on dell2, at a HEAD that contains @f2415a44b5: the local day files, the sidecar, the holdings copy and the transactions cache live under its `.scratch/advi_cotbkf/` and exist nowhere else.
- **The variable.** Every invocation below carries `COTBKF_SWEEPS_CONFIG=<path>`, the path read from `org/devices/state/dell2/cotbkf_sweeps_config_pointer.json` (row D2-S84).

**The act, in this order. Each step's last line goes in the ledger entry.**
1. Read `.open_deploys/` across EVERY live worktree and union it with its per-tree denominator (condition 5). Open this act's ledger entry before the first write.
2. Condition 1: `list-object-versions`, every page, on each of the three prefixes under `s3://opal-data-cottonwood/irpt/cottonwood/gold/`: `account_return_daily/`, `account_return_daily_blank_reasons/`, `dim_return_method/`. Count versions and delete markers client-side after auto-pagination; print both counts per prefix.
3. `python data/assets/scripts/silver/commonwealth_account_return_daily.py --stamp-manifest --manifest org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json` -- last line `ARD-COTTONWOOD-MANIFEST-STAMP days=3325 day_hashes_equal=3325/3325 note=present sidecar_rows=1584413 method_version=3`, and the manifest's sha256 unchanged after it.
4. `... --bond-check --manifest <the manifest>` -- last line carries `measured_rows=107316 measured_rows_on_bond_days=0` (condition 4).
5. Condition 2: `... --show-day-manifest --manifest <the manifest> --date 2026-06-22` -- last line `ARD-COTTONWOOD-DAY-MANIFEST date=2026-06-22 method_version=3 valuation_source=positions_x_as_traded_close fee_treatment=net_of_fees price_basis=as_traded custodian_text=absent`, exit 0. Any other line or a non-zero exit is a STOP: return to `1.0.0_SA_CTO~DELL2`.
6. `... --apply --pair <COO half> --pair <CTO half> --manifest <the manifest>` -- one `LANDED` line per object; last line `ARD-COTTONWOOD-APPLY days=3325 landed=3325 sidecar=landed method_row=landed`. Keep the full output outside the repo; put the count of `LANDED` lines and the last line in the ledger.
7. Condition 3: `... --verify-served --manifest <the manifest>` -- last line `ARD-COTTONWOOD-VERIFY days=3325 match=3325/3325 sidecar=match method_row=match manifests=3325/3325`. Close the ledger entry APPLIED, UNREAD (condition 6).

**The CTO half's seven conditions, verbatim (its section 4):**

1. **Versions are read before the first write.** `list-object-versions`, every page, on each of the three prefixes: the count
   of versions and of delete markers, printed. An empty CURRENT listing does not show whether an earlier mint was deleted.
   Both counts 0: the pair's "no prior version exists" is true. Above 0: the counts go in the ledger and the rollback
   sentence is corrected there; it does not stop the act.
2. **The day manifest is seen before 3,325 of them are written.** Before `--apply`, the applier shows the exact
   `manifest.json` the producer will write for one day (a dry run, or a local call of the same `build_manifest` with the same
   `src`): `method_version` 3, the row-3 method sentence, `valuation_source` `positions_x_as_traded_close`, `fee_treatment`
   `net_of_fees`, `price_basis` `as_traded`. The custodian method's text anywhere in it is a STOP. If the tool cannot show it
   without writing, STOP and return to this seat.
3. **`--verify-served` covers both objects of every day.** `data.parquet` against the tracked hash, and each served
   `manifest.json` read back for the five fields of condition 2: 3,325 of 3,325, printed. Row D2-W66-S1 disarms on that line.
4. **The bond count is re-read first and the run refuses on anything but 0,** as the tool does.
5. **Before the act:** every live worktree's `.open_deploys/` is read and unioned with its per-tree denominator; the ledger
   entry is opened before the first write.
6. **After the act the keys stay unread.** No reader of `account_return_daily` for Cottonwood exists until its own pair
   (ADDENDUM 11.1). The ledger close says APPLIED, UNREAD.
7. **Not covered:** any delete; any overwrite; a re-run of `build()`; any key outside the three prefixes; any reader.

## RE-SIGNED on the new pin (2026-10-11 ~06:1xZ)

**Verdict: SIGNED** against the COO half as RE-PINNED @0865081982, file sha256
`351dad12c2ae18b31367a95cce3ecb892cefb9fb461cc015cbddb4ada137a115` (`sha256sum` by this seat on the tree file: equal). The
signature above on sha256 `b8e44814...` is void for the act; its sections 1 to 4 stand as this signature's text.

- **Read here:** the diff of the COO half between the two pins, and the adapter's diff `84ef9e0972..b8995a1400`: 1 file, 101
  insertions, 0 deletions, four hunks, none removing or changing a line (the diff prints no `-` line). The adapter in the
  tree hashes to `38f06ba93cc82318...afcbb51c9`, the pin the half names.
- **Condition 2 is MET by the issuer's run, with a limit this seat accepts by name.** `--show-day-manifest`, no S3 client, on
  three real days (2013-04-03, 2020-03-16, 2026-06-22): `method_version` 3, the three row-3 fields, the custodian text
  absent. The show mode reaches the manifest through helpers that mirror `apply_days` and are not called by it. So it shows
  what the producer writes for that input; it does not show that `apply_days` hands the producer that input.
- **That makes condition 3 the control, and it now exists:** `--verify-served` reads every served `manifest.json` and ends
  `manifests=3325/3325`. A count below 3,325 is Branch B at once: the day data stays, unread; the wrong manifests are
  re-written under an amendment to this pair, as new versions on a versioned bucket; no delete.
- Condition 1 (the versions census) remains the applier's CLI read, as the half says.

Manifest sha256 `d2d99d5c...ce47b36` and the bond count of 0 of 107,316 are unchanged, by the issuer's report.

**The CTO half's re-sign, verbatim:**

RE-SIGNED on the new pin (2026-10-11 ~06:1xZ)

**Verdict: SIGNED** against the COO half as RE-PINNED @0865081982, file sha256
`351dad12c2ae18b31367a95cce3ecb892cefb9fb461cc015cbddb4ada137a115` (`sha256sum` by this seat on the tree file: equal). The
signature above on sha256 `b8e44814...` is void for the act; its sections 1 to 4 stand as this signature's text.

- **Read here:** the diff of the COO half between the two pins, and the adapter's diff `84ef9e0972..b8995a1400`: 1 file, 101
  insertions, 0 deletions, four hunks, none removing or changing a line (the diff prints no `-` line). The adapter in the
  tree hashes to `38f06ba93cc82318...afcbb51c9`, the pin the half names.
- **Condition 2 is MET by the issuer's run, with a limit this seat accepts by name.** `--show-day-manifest`, no S3 client, on
  three real days (2013-04-03, 2020-03-16, 2026-06-22): `method_version` 3, the three row-3 fields, the custodian text
  absent. The show mode reaches the manifest through helpers that mirror `apply_days` and are not called by it. So it shows
  what the producer writes for that input; it does not show that `apply_days` hands the producer that input.
- **That makes condition 3 the control, and it now exists:** `--verify-served` reads every served `manifest.json` and ends
  `manifests=3325/3325`. A count below 3,325 is Branch B at once: the day data stays, unread; the wrong manifests are
  re-written under an amendment to this pair, as new versions on a versioned bucket; no delete.
- Condition 1 (the versions census) remains the applier's CLI read, as the half says.

Manifest sha256 `d2d99d5c...ce47b36` and the bond count of 0 of 107,316 are unchanged, by the issuer's report.

Rollback is the COO half's section 4 with section 2's third point: the minted keys stay unread, a partial mint is resumed
under an amendment, and a delete is Andrew's.

-- 1.0.0_SA_CTO~DELL2

**Branches, restated for the applier.**
- A refusal before the first write (a key exists, a hash differs, a bond count other than 0, a pair file not committed): nothing is written. Record the refusal line and stop.
- A stop after the first write: do NOT re-run `--apply` (it refuses, keys exist) and do NOT delete. Record the `LANDED` count and the last line; the remedy is a RESUME under an amendment to the pair.
- `manifests=` below 3325/3325 at step 7: Branch B at once. The day data stays, unread; record the `ARD-VERIFY-MANIFESTS` line and stop.
- A delete of any kind is not this order's act.

**Acceptance under this amendment.** `CB38al2-AC1`'s invocation is read as step 7's (`--verify-served --manifest <the manifest>`), and its bar is unchanged: the line starts `ARD-COTTONWOOD-VERIFY days=`. The issuer and the CTO read the whole line.

**Surprise rows** mint `ADVI_COTBKF-D2-WCB2-S<k>`, `"fabric": "dell2"`, `surfaced_at` read from the clock, carrying no account id.

**AMENDMENT 6 (issuer, 2026-10-11T06:51Z) -- the surprise-row id form, corrected.** The form `ADVI_COTBKF-D2-WCB2-S<k>` that AMENDMENT 5 and the
BOUNDS name is refused by the row gate (measured by `0.7.0_AE_CloudOps~CB2`, msg 4307). A row of this order mints the next free
`ADVI_COTBKF-D2-S<k>` id, read from the channel at write time, as rows D2-S91 and D2-S92 did. Nothing else changes.

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
