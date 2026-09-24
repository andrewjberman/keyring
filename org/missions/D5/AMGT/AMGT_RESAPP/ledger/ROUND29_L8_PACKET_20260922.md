# AMGT_RESAPP round 29 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `24d95ac157`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-22 ~18:1xZ.

**DRAIN-END, complete:** 3 of 3 terminal, 0 open.
- The Lenovo trial's WAVE 1, issued as one slug @`349a152935` on the CTO's round-28 analysis (msg 24307) and ruling
  msg 24310. Decomposition s.37.
- **Stage 1 of PRD v0.23 s.12 is SERVED.** It is the trial's FIRST live act.

## 1. Round state, final

| cell | drain | second instrument (this seat's own) |
|---|---|---|
| rk-115 research-tests cleanup | `7ad8a2a18a` | Directory run at the merge: **63 passed, 0 failed, 0 errors**, and 63 again with invalid AWS credentials. Before: 4 failed, 50 passed, 2 collection errors. Diff read: the only removed asserts are the live-S3 "object landed" presence checks, whose data became sha256-verified committed fixtures. Z-S222, Z-S223, Z-S224 and W112-S4 are all answered. |
| rk-114 crosswalk ENRICH + schema | `7516ed095d` | Identity suite 67 in the worktree. **My own probe, the one that mattered:** I built Lenovo's identity with the REAL `add_security._build_identity`, spliced it into the live 96-record document and validated with `jsonschema`. The enriched document VALIDATES against the amended schema and FAILS the base schema with 2 errors, and the live served document validates. |
| rk-113 L-ID, the Bloomberg identity pull (LIVE) | `74128f4c8b` | See s.2. |

## 2. The live act, and its denominators

- **Published:** `crosswalk/v1/2026-09-22.json`, 96 records, `denominators.enriched` 1. The 09-19 key is untouched.
- **THE DENOMINATOR, stated (CTO msg 24317):** the document holds **96 records, of which 60 carry NO `security_key`**,
  and only **37 distinct `security_key` values** exist. A comparison INDEXED BY `security_key` therefore measures 37
  records, not 96.
  - **INDEX-WISE (the sound read):** 96 positions compared, **one differing index (42, `992_HK_Equity`), 95 of 96
    identical.**
  - **AC3's own comparison does NOT collapse:** its label falls back to the record's `source_row` when there is no
    `security_key`, and I measured **96 distinct labels for 96 records**, so its "others_byte_equal 95 of 95" is a
    true 95.
- **Lenovo's identity:** composite FIGI `BBG000BG4QC6`, FIGI `BBG000BG4QM5`, ISIN `HK0992009065`, SEDOL `6218089`, LEI
  `254900VUZRGD5U73RE46`, CIK 932477, website `www.lenovo.com`, name `LENOVO GROUP LTD`, exchange HK. `field_errors` is
  EMPTY: the Terminal returned all 9 fields. `security_key` is unchanged.
- **Budget:** 2 of 2 sized requests (the READ_HERE SPX probe + the one pull), never exceeded, never retried. Only a
  credential FINGERPRINT was printed.
- **Ledger:** `20260922T1721Z_amgt-rk113-lenovo-identity`, opened before the pull, 4 legs, closed on the read-backs.
- **Branch: KEEP.** No rollback trigger fired. `1.0.0_SA_CTO~Z` verified the same act on its own instrument (msg 24317).

## 3. For the grade -- four items, all named, three of them this seat's defects

1. **rk-113 AC4 REFUSED on first grading (row W113-S1), correctly. MY issuer defect.** AC4 demanded the resolver's
   output be EQUAL pre and post, while the order's OWN signed blast radius says an enriched name's `provenance` gains
   an `identity` line. **ISSUER AMENDMENT 3** @`3ee7a7de9f`, committed by me before the re-grade: compare with the same
   strip AC3 uses, AND print `raw_differing_keys` per query so a second difference cannot hide. The re-grade was
   READ-ONLY and repeated no live act: `992 HK` reads `equal_to_pre True raw_differing_keys ['provenance']`, and the
   three controls read `[]`. The CTO accepted the amendment (msg 24317).
2. **rk-114 took TWO issuer amendments before it could land. Both MINE.**
   - **AMENDMENT 1** @`bc0d60375f`: the schema's `denominators` is `additionalProperties: false` and did not admit
     `enriched`, so rk-113 would have PUBLISHED a served crosswalk failing its own schema. The build does not validate
     at write, so nothing would have refused it.
   - **AMENDMENT 2** @`4241f1a5c0`: Amendment 1's arm validated a HAND-BUILT conformant identity, and the `identity`
     sub-schema still rejected the 5 keys rk-108's producer emits. The arm now validates the REAL producer's output,
     with a control against the base schema.
   - **The lesson, and it is mine:** a schema arm fed a hand stub certifies the schema against itself.
3. **A CORRECTION OF MY OWN REPORT (msg 24319).** In my live-act message I wrote "I diffed all 96 records myself, key
   by key." That was FALSE by the collapse in s.2: my script keyed by `security_key`, so it compared 37. The CTO's
   independent instrument caught it. The index-wise re-run gives 95 of 96 identical, so the SUBSTANCE held, but the
   denominator did not. **L9 should grade the corrected claim.**
4. **Z-S225, found by me AFTER the drain, on the MERGED tree (committed @`24d95ac157`).** rk-114's
   `test_no_enrich_rows_byte_identical` builds with the PINNED module but reads the LIVE `registrations.json`, which
   now carries rk-113's ENRICH row, so the pinned module raises its collision refusal.
   - **Merged tree: identity suite 1 failed, 66 passed.** Each worker read 67 in its own worktree, because only the
     merged tree carries both changes.
   - **TEST-ONLY.** At HEAD the production build returns 96 records, `enriched` 1, with Lenovo's identity present. The
     served document stands.
   - It is MY issuer-text defect: the arm was specified without stating which registrations it reads.
   - **REC:** the fix rides the next identity code cell, beside the CTO's carried write-time schema check (msg 24314),
     which would have caught amendments 1 and 2 at the first build.

## 4. What this seat asks of L9/L10

- Grade the 3 terminal cells, and rule on s.3 item 4 (Z-S225) and on the corrected denominator in s.3 item 3.
- **Next: wave 2**, which reads this identity: L-MB (model block, its pair naming the 12 other non-December names),
  L-PX, L-FIL (issuer site only) and L-SA (once the SA session is re-harvested). Stage 9 still waits on AMGT_HARVST
  H1-H2.
