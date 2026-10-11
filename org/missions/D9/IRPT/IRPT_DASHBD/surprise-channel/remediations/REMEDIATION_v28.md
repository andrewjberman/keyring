# IRPT_DASHBD: remediations, round 68 (workstream B)

<sweep_watermark>2026-10-11T15:54Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T15:54:08Z. Input: msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104).
Graduated, round label v69: 13 rows, OPEN, INERT. Closed in place in REMEDIATION_v27: D2-W86-S1.
The nine rows this seat graduated as filed at the last slug are now read: 1 closed, 8 open, both ARMED rows still armed.

**For the CTO's analysis:**
1. **The whole thresholds object is copied into every served manifest** (row D2-W100-S3). The last tracked copy of that file carried
   two keys holding account-number-shaped digit runs. **Read by this seat on the served object:** 49 Financial's method row 2 manifest
   (written 2026-10-03, in that firm's own bucket) carries a thresholds object of 24 keys, two of them named per_account, and 12
   digit runs of 8 or more that are not part of a decimal. Cottonwood's carries 6 keys and none. No value was printed or kept.
2. **The R45 release as packaged serves none of method row 2's new columns** (row D2-W101-S2): the function it replaces never writes
   the method table. They reach a served object only through a producer upload that no order or pair covers.
3. **The reworded income reason is in the code and not served** (rows D2-S13, D2-W103-S2). Its apply waits on your half and a named
   applier. Two prose lines of the contract still carry the old wording.
4. **The tie-out's 244 unexplained segments: 154 classed, 90 not**, and the claim is inferred. The 90 need a custodian read.
5. FWD-11 and FWD-12 stay parked. The Cottonwood account id join is not established: the directory lists no published key.

```json
[
 {
  "id": "IRPT_DASHBD-D2-W100-S3",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-125: the whole thresholds object is copied into every returns manifest.json (build_manifest) and into the method-row manifest (emit_method_row), so whatever the live thresholds file carries beyond the five values is served; the last tracked blob carried 24 keys, two of them holding account-number-shaped digit runs.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W100-S3",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "The live thresholds file carries only what may be served, or the manifests copy the five thresholds and their claims and nothing else. The served 49 Financial manifest is read by this seat as carrying 24 keys, two named per_account.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v69"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W101-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-126: the reporting-gold Lambda this release replaces never writes dim_return_method (the handler omits emit_method_row and the role's Terraform omits the prefix), so the release alone gives method row 2 no new column; they reach a served object only through a later producer main() upload, which no order or pair covers.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W101-S2",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "A pair covers the producer upload that first serves method row 2's new columns, or the release packet says the release serves none.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v69"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W101-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-126: the order says the R45 release gives 49 Financial's method row 2 two new columns (income_basis_claim, income_basis_reason); the producer's dry run at the four pins gives NINE, and account_return_daily.py moved through four commits since REFRESH_2, not one.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W101-S1",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "The R45 packet states nine new columns and four commits, as the dry run measured.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v69"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W100-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-125 (the CTO's item 3): the 49 Financial thresholds file states no claim for any of its five thresholds, so the producer writes every one as held and the method row's threshold_claims_source as defaulted_no_claims, though two of the five are measured and one is derived.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W100-S1",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "The 49 Financial thresholds file states a claim for each of its five thresholds.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v69"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W100-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-125: the handler reads the thresholds only from a local file (the bundled path, then a repo path); no served S3 object exists, so 'the served copy' is the file inside the live function's code package, which this order does not download, and the equal-to-served question reads NOT_ESTABLISHED.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W100-S2",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "The tracked thresholds file is compared to the copy inside the live function's package, by content.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v69"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W99-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-124: the thresholds file the handler reads (MEASURED_THRESHOLDS_R1.json) was deleted from the tree by df127f168c because the removal set carried real client account numbers, and its last tracked blob holds 14 account-number-shaped digit runs; a tracked copy for DB-b-125 cannot be the served bytes verbatim, so 'sha256 recorded against the served copy' will read unequal by construction.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W99-S1",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "The tracked thresholds file is rebuilt without the account-number-shaped runs, and what it is equal to is stated.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v69"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W102-S4",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-127: the Cottonwood directory the reporting read mints from lists 0 published account keys, so the gold-to-directory id join is NOT_ESTABLISHED; the gold id form and the directory's declared raw-key form differ in shape on 12 of 12 ids read.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W102-S4",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "The gold-to-directory account id join is established on a published directory, or the reporting read states it cannot name a Cottonwood account.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v69"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W102-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-127: COLUMNS_NULL's method_version text is corrected in the adapter, but the tracked Cottonwood build manifest still carries the old 'NULL on purpose' text, and the key stays inside a dict named for nulls (ROW_FOR_ISSUER).",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W102-S1",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "The tracked Cottonwood build manifest carries the corrected method_version text, and the key leaves the dict named for nulls.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v69",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v69"
  },
  "closed": true
 },
 {
  "id": "IRPT_DASHBD-D2-W102-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-127: method row 3 as emitted for Cottonwood does not itself state as-traded close or net of fees; its fee_basis is the pointer PER_ENTRY_FEE_TREATMENT and its value_basis defers to 'the entry's declared price_basis' (ROW_FOR_ISSUER).",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W102-S2",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "Method row 3 as emitted states its price basis and fee treatment, or the page reads them from the entry.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v69"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W102-S3",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-127: method row 3's flow_convention is the producer's default END, not a stated or measured Cottonwood fact (ROW_FOR_ISSUER).",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W102-S3",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "Method row 3's flow convention is stated or measured for Cottonwood, with its claim.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v69"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W103-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-128: method_version_of refuses a custodian_reported entry naming row 3, but an entry that declares NO valuation_source is not refused for naming it; 0 of 2 sources.json entries do, so the reworded row-3 reason holds today.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W103-S1",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "method_version_of refuses an entry that names row 3 and declares no valuation source.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v69",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v69"
  },
  "closed": true
 },
 {
  "id": "IRPT_DASHBD-D2-W103-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-128: two prose lines of the dim_return_method contract (line 6, the authored_under history; line 35, the income_basis column meaning) still give 'FWD-3 does not separate income' as the cause of row 3's absent income; only the example row was ordered reworded.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W103-S2",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "The two prose lines of the method contract are reworded with the example row.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v69",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v69"
  },
  "closed": true
 },
 {
  "id": "IRPT_DASHBD-D2-W104-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-129: of the 244 UNEXPLAINED segments, 154 class from the records already on this box and 90 cannot: no repo or private record holds a per-segment field that names their cause, and the next read is an S3 read this round forbids.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W104-S1",
   "msg 5259 (round 68 fully drained @780ba55bde; records under deliverables/0.9.0_WK_IRPT_DASHBD~99 to ~104)"
  ],
  "remedy": "The 90 unexplained segments are classed by the custodian read the round forbade, or stated as unclassed where the tie-out is shown.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v69",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v69"
  },
  "closed": false
 }
]
```
