# CTO ROUND-69 ANALYSIS -- IRPT_DASHBD (workstream B) -- answering the round-68 L10 slug (2026-10-11 ~16:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v28.md`
@595332678c (3.0.0_SA_CVO msg 5269). **Prior:** the round-68 analysis @0005d9fd9a. **No PRD addendum in this analysis.**

## 1. Where the project stands

Round 68's six cells are drained; no served write was made in it. Thirteen rows are open, none newly armed. Two pairs were
signed today and neither is applied: the R45 release (waits for Monday's fire) and the income-reason rewrite (waits for its
applier's order).

## 2. Item 1 comes first: account-number-shaped values inside a served manifest (row D2-W100-S3)

**What is measured, by the reviewer on the served object:** 49 Financial's method row 2 manifest, written 2026-10-03 in that
firm's own bucket, carries a thresholds object of 24 keys, two named `per_account`, and 12 digit runs of 8 or more.
Cottonwood's carries 6 keys and none. **What is NOT measured:** whether the daily returns manifests the live function
writes carry the same object. The code copies the whole thresholds object into both (`build_manifest`, `emit_method_row`),
so it depends on the thresholds file inside the live function's package, which nobody has read by content (row D2-W100-S2).

**What it is and is not.** It is in the firm's own bucket, so it is not one firm's data in another's home. It is still a
defect: the gold names accounts by an opaque id, and a manifest beside it should not carry what looks like the custodian's
account numbers. Who can read those manifests is whoever can read that bucket.

**Ruled, both halves of the row's remedy, in this order:**
1. **A read first, counts and key names only, no value printed or kept:** the thresholds file inside the live function's
   package (downloaded, by content), and ONE recent daily returns manifest for 49 Financial. For each: the key names of the
   thresholds object, and the count of digit runs of 8 or more. That says whether one served object carries them or
   thousands.
2. **The code:** the manifests copy the five thresholds and their claims and nothing else. Whatever else a thresholds file
   holds stays out of a served object by construction.
3. **The already-served objects** are NOT rewritten in this round. A rewrite leaves the prior versions in a versioned
   bucket, and removing a version is a delete, which is Andrew's act. That question goes to him with item 1's count in hand,
   not before: its size is not known today.

## 3. The slug's other items

2. **R45 serves none of method row 2's new columns (row D2-W101-S2).** Agreed, and this seat's half @fb97b13d71 says so: the
   release only. The producer upload that first serves them is its own pair, and it is not cut before section 2's code
   change, since that upload writes a method manifest.
3. **The reworded income reason.** This seat's half is signed @34a6a32212 and the applier named. The two prose lines of the
   contract (row D2-W103-S2) are reworded in the same round.
4. **The 244: 154 classed, 90 not.** The 90 are stated as unclassed wherever the tie-out is shown. The custodian read that
   would class them is ordered as one read-only cell, counts by cause.
5. **FWD-11 and FWD-12 stay parked. Row D2-W102-S4:** the Cottonwood directory lists no published account key, so the
   reporting read cannot name a Cottonwood account. That is a fact about the directory, held with the Cottonwood half, and
   it un-parks with it.

Rows D2-W102-S2 and S3 (method row 3 does not itself state its price basis, fee treatment or a measured flow convention):
accepted as open. Each is stated on the row with its claim before the first Cottonwood partition is minted, not before.

## 4. ENRICHMENT LIST for round 69 (ONE issuance, in this order)

1. The read of section 2 item 1.
2. The manifests copy five thresholds and their claims only (section 2 item 2); the thresholds file is compared with the
   live package's copy by content (row D2-W100-S2).
3. The contract's two prose lines; the stale Cottonwood build manifest text (rows D2-W103-S2, D2-W102-S1).
4. `method_version_of` refuses an entry that names row 3 and declares no valuation source (row D2-W103-S1).
5. The custodian read for the 90 unclassed segments, counts only.

## 5. Acts only Andrew can do

- Removing versions of an already-served object in a client firm's bucket, if section 2's read shows it is wanted
  (CLAUDE.md, Agent Autonomy: S3 deletes need human confirmation). Not asked until the count is read.

## 6. What this analysis did not measure

It rests on the slug as filed. This seat read no served object in this round; one listing it attempted was refused by the
comp-rail and it did not go around the refusal.

-- 1.0.0_SA_CTO~DELL2
