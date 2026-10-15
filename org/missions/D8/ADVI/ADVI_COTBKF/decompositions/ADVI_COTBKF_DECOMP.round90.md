# ADVI_COTBKF decomposition -- ROUND 90 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-15) -- the CRM job's record made safe, the dell1 leak scan read back, one review packet

**Status: DRAFT -> ISSUED in one issuance.**

**Numbering.** The CTO's round-88 analysis (`ledger/ROUND_ANALYSIS.round88.md` @644852b53a, msg 6222) calls its enrichment list "round 89". Round 89 was already issued at @5c1cd69c65 from the CTO's msgs 6161 and 6175 and carries the analysis's item 2 (the `use_class` guard, both `3adb` branches behind one switch, no served move; worker `~178`, in flight). So THIS round is 90 and cuts the analysis's items 1, 3 and 4. Item 5 (W176-S2 and D1-S1, inert) is carried.

**Cut on:** the analysis's enrichment list. Item 1: CVO row `ADVI_COTBKF-D1-C-S3` (ARMED, BLOCKING, disarm owner this seat; `surprise-channel/adjudications/ADJUDICATION_v62.md` @4824a91a1f): `cotbkf_crm_match_job.py` :260-261 copies each CSV member's first line verbatim into the committed `JOB_RECORD.json`; a headerless member would put a CRM data row into git. Item 3: row `ADVI_COTBKF-D1-W170-S3`: the hashed account-id list is absent on dell1 (`~/.opal/account_id_hashes.txt`), so no dell1 commit has been scanned; `0.0.0_AB_MSTR~DELL1` provisions the list off git (asked, msg of 20:45Z); this seat's cell is the read-back. Item 4: row `W175-S4` and FWD-9: no candidate link is applied without a person's word; ONE review packet, link ids and corroboration flags only, no PII values. **Not cut:** a CRM re-run (waits on call `bccc` and item 1), any served change from the guard (waits on call `3adb`), any contact with Cottonwood.

**Rule 24.** Domain: the analysis's items 1 to 5. Subtraction: 1 -> CB-cl-1; 2 -> round 89 (in flight); 3 -> CB-cl-2; 4 -> CB-cl-3; 5 -> carried. Uncovered in this round: none (item 3 is withdrawn by the CTO's ruling).

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cl-1` | the CRM job's run record never carries member text: it records per member a header-cell COUNT and the ROLE NAMES the job classified, never raw header text; a headerless member's first line cannot reach the record; tests incl. a canary | FWD-8, FWD-9 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~179` |
| `CB-cl-2` | **WITHDRAWN BY RULING, no cell.** The read-back of the dell1 leak scan: the CTO withdrew item 3 (msg 6228; `ROUND_ANALYSIS.round88.md` amendment 1 @384ecc0e4c): the dell1 hash list stays set aside on Andrew's 10-09 word ("I don't care about the client data getting committed to Git"), `0.0.0_AB_MSTR~DELL1` restores nothing (msg 6229); row `W170-S3` is dispositioned by-design. | FWD-7 | n/a | n/a | none |
| `CB-cl-3` | ONE near-match review packet: the R4 candidates and the exact-name rows over the 219 as link ids and flags, one row per distinct pair, source and overlap stated, no account number, no name | FWD-8, FWD-9 | LOCAL | none (reads round 87's outputs) | `0.9.0_WK_ADVI_COTBKF~180` |

**Fan-out (to state at the cut):** `2 of 2 chains, cap 8` (cl-1 and cl-3; cl-2 withdrawn by ruling). No edge: cl-1 writes the job module and its test, cl-3 writes only a deliverable.
