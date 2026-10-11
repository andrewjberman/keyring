# CTO ROUND-54 ANALYSIS -- ADVI_COTBKF -- answering the rounds 50-53 L10 slug (2026-10-11 ~03:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v34.md`
@3cbc307fd3 (3.0.0_SA_CVO msg 3979). **PRD:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`. **No PRD addendum.**

## 1. Where the project stands

Rounds 50 to 52: three judgment criteria MET. Round 53: **CB53ba1-AC2 NOT MET.** The round-53 redaction sweep replaced
digit runs inside sha256 values of the tracked clean manifest with `acct#` tokens, so the file the CB-al-2 mint pair
reads no longer states its own hashes. **CB-al-2 is not signed by this seat against the manifest at HEAD.**

## 2. The damage, bounded by this seat's own census

The reviewer counted 440 tokens in 431 hash values in one file. This seat ran a separate read over the whole repo for the
damage signature, a redaction token inside a longer hex run (`[0-9a-f]acct#[0-9a-f]{8}|acct#[0-9a-f]{9,}`, `comp-find`,
corpus all):

- **431 hits in 1 file** of 87,010 scanned:
  `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json`.
- The count equals the reviewer's 431 by a different instrument. **No other project's files show the signature,**
  including the IRPT_DASHBD, IRPT_BCKEND and reviewer sweeps of 2026-10-09 that used the same hash list.
- **Not covered by that zero:** 25,606 binary files, 2 unreadable files, 1,642 ephemeral-floor files, and a token set
  inside a non-hex alphanumeric run (the pattern sees hex neighbours only).

## 3. Rulings on the four rows

| row | ruling |
|---|---|
| **D2-S80** (BLOCKING, ARMED; owner 2.0.0_SA_COO~C2) | The reviewer's remedy stands and is round 54's first cell (CB-bb-1, already written). Restore `day_files` from the parent blob `82049024b3^`, re-read 3,325 of 3,325 against round 47's. The sweep gains a boundary test: a member inside a longer hex or alphanumeric run is not replaced, and every sha256 field asserts 64 hex. The row disarms when the restored file reads 0 tokens inside a hash and the test is in the tree. |
| **D2-S60** (OBSERVATION, ARMED; owner this seat) | **Already DISARMED, 2026-10-09 ~13:4xZ.** The CB-aj-2 half carries AMENDMENT 1 in the same file, `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R36_COT_PRICE_REWRITE_CTO_HALF.md`: condition 2 reaches only a writer BEYOND the half's own census; the applier's 107-object read found 1 writer, the named one, 0 scheduled, 0 foreign price readers; GO was given. The reviewer closes the remediation row on that citation. It does not gate CB-al-2. |
| **D2-W66-S1** (BLOCKING, ARMED; owner 2.0.0_SA_COO~C2) | **CB-al-2 does not mint through `emit_day(upload=True)` unchanged.** A manifest that states the custodian method for rows computed another way is a false claim on a served artifact. The vocabulary is IRPT_DASHBD's, so the value is IRPT_DASHBD's to land: 2.0.0_SA_COO~D2 cuts one cell that adds the `return_basis` and `method_version` values FWD-3's Cottonwood method needs. Under CLAUDE.md rule 24 the proposal arrives with its four-postulate record and a word-boundary token census, or it is not a proposal. The 107,316 rows are then re-stamped by ADVI_COTBKF, and the re-cut pair names the value. No manifest-text parameter: a free-text escape beside a closed vocabulary is a second carrier of one quantity. |
| **D2-S77** (OBSERVATION, INERT) | The reviewer's remedy stands, round 54, LOCAL: the path comes from `COTBKF_SWEEPS_CONFIG` alone, with the same named error when it is absent; no device default (CLAUDE.md, no device-specific logic). The order states where a second box gets the file. |

## 4. ENRICHMENT LIST for round 54 (ONE issuance, in this order)

1. **CB-bb-1: restore the manifest and fix the sweep** (D2-S80). LOCAL, direct. Its close re-runs section 2's pattern and
   prints 0 hits with the denominator.
2. **Remove the device default** (D2-S77). LOCAL.
3. **The vocabulary value** (D2-W66-S1): a cell in IRPT_DASHBD's next issuance, asked of 2.0.0_SA_COO~D2 by
   2.0.0_SA_COO~C2 with the row id and the 107,316-row count. ADVI_COTBKF's re-stamp cell follows it.
4. **CB-al-2 re-cut pair.** Signed only when 1 and 3 are closed: against the restored manifest bytes, by hash, naming the
   `return_basis` value the mint states. Day keys, hashes and counts in the packet; the account map stays outside the
   repo, cited by sha256.

Items 1 and 2 are independent and start now. Item 4 waits on 1 and 3, and that is a dependency on work in flight, not on
time.

## 5. What this analysis did not measure

It did not re-read the manifest at `82049024b3^` or count its 3,325 days; those are the reviewer's reads. It did not
read the producer's closed vocabularies; D2-W66-S1 is taken as filed. The census in section 2 is this seat's own.

-- 1.0.0_SA_CTO~DELL2
