# HANDOVER ANNEX — FRI 2026-08-21 11:30Z COT_SUPERVISED G4/G4b acceptance

**Author:** 1.0.0_SA_CTO · **Written:** 2026-08-21 ~0125Z · **Status:** EVIDENCE, for whoever COO places

**Why this file exists, and it is the point:** the two corrections this acceptance depends on were
both sent to `0.6.2_AE_PartnerETL`'s inbox **after Andrew closed that seat**. Measured just now:
that inbox holds exactly **2 unread messages** — MSTR's `20260821T011546Z` correction and my
`20260821T012032Z` verification — **and no session will ever read either.**

> **THE CORRECTION THAT MUST OUTLIVE A SEAT CANNOT LIVE IN THAT SEAT'S INBOX.**
> Two senior seats independently made the same routing error within five minutes of each other,
> each believing they had discharged a handover. A `QUEUED` receipt is explicitly *"not a delivery
> — it waits for the seat"*; when the seat is gone, it waits forever. This is the SENT-vs-READ
> gap (Rule 22b) in its terminal form: **the send succeeded, the delivery cannot.**
> A committed record is the only artifact that survives a session. Hence this file.

**I am not taking 0.6.2's lane and not manufacturing a gate.** COO places the seat. This records
evidence I already measured so the successor starts from measurement, not from scratch.

---

## 1. THE ACCEPTANCE IS UNAFFECTED — verified at my seat, 2026-08-21 ~0118Z

Site Z's leg-2 deploy at ~01:04Z rewrote deploy-scope objects with **identical bytes**. I fetched
and hashed them rather than reading a timestamp:

| S3 object (`opal-data-cot`) | LastModified (UTC) | Size | sha256 (16) | vs 0.6.2 pin | vs repo |
|---|---|---|---|---|---|
| `code/bronze/cot_bronze_ingest.py` | **01:04:18Z** *(moved)* | 80,599 | `c8764a43c1fe7189` | **SAME** | **SAME** |
| `code/bronze/templates/account_attributes.json` | 18:06:01Z *(untouched)* | 1,225 | `32200b3df7bda4e3` | **SAME** | n/a |
| `code/gold/A_00.accounts_dimension.py` | 01:04:23Z *(moved)* | 40,517 | `1d79e0b480fe89ac` | n/a | **SAME** |

**The 11:30Z run pulls exactly the bytes 0.6.2 verified.** `account_attributes.json` never moved
because it is `.json` and `.json` is never in deploy scope (`safe_deploy_core.py:351/:389`).

## 2. ⛔ THE RE-PIN — the one thing that will fire falsely if missed

0.6.2 pinned **both** sha256 and LastModified, and recorded *"a surprise deploy shows up as a hash
change."* **That is true for a content change and BLIND to a rewrite.**

- **If the verifier compares sha256 only** → correct and unaffected. Do nothing.
- **If any limb compares LastModified** → **re-pin `cot_bronze_ingest.py` to `01:04:18Z`, or drop
  that limb.** Otherwise it fires falsely at ~11:35Z on a healthy pipeline.

**The general form, because it will recur:** the two detectors have **opposite** blind spots —
sha256 sees content change and cannot see an identical-bytes rewrite; LastModified sees every
write but **cannot distinguish a rewrite from a real change**. Neither is stronger; they answer
different questions. For *"did the executed bytes change?"* — the only question this acceptance
asks — sha256's blindness is the **correct** blindness. **A verifier holding BOTH limbs and
alarming on disagreement fires on the healthy case**, because after any merge-triggered deploy leg
`hash-same + timestamp-moved` is the NORMAL state.

**Mechanism, source-confirmed at my seat** (`.tools/safe_deploy_core.py`): the `aws s3 cp` at
`:548` is **unconditional** — no content comparison against S3 anywhere before it; `head-object`
runs at `:555`, **after**; `MATCH` at `:565` is returned on `local_md5 == s3_etag` **post-write**.
The docstring at `:529` states it: *"Upload file to S3 and verify ETag == local MD5."* The only
pre-upload `head-object` (`:405-414`) is the shared-home **existence** guard, not a content check.
**So `MATCH` means UPLOADED-AND-VERIFIED, never SKIPPED-BECAUSE-IDENTICAL** — a word that reads
like a skip, which is how the false "inert leg" claim survived in the `/integrate` skill for weeks
(MSTR retracted it on a source read within the hour; corrected in place).

## 3. THE WATCH IS GONE, AND ITS ABSENCE IS THE SILENT HALF

Monitor `bgx6dde2b` died with the session. **A Monitor is session-bound.** Two failure modes now
exist and they take **different** remedies:

| | failure | remedy | how it presents |
|---|---|---|---|
| **(a)** | nobody ACTS on the landing | an owner | loud enough — work visibly does not proceed |
| **(b)** | nobody NOTICES a NO-SHOW | a watch | **silent — the pipeline reads healthy** |

**(b) is the one that hurts**, and it is the limb that died with the rest: 0.6.2's Monitor emitted
on **OVERDUE** as well as LANDING. An owner who arrives at 11:35Z and finds nothing has learned
something; **an absent watch on an absent fire teaches nobody anything.**

⛔ **DO NOT ARM A MONITOR NOW FOR AN 11:30Z FIRE.** The fire is ~10 hours out; any Monitor armed
tonight dies with tonight's session. **Arming one is worse than not arming one, because it
manufactures the belief that something is watching.** The watch is the morning seat's **first
act**, not a thing tonight can bank.

## 4. WHAT SURVIVES (start here, do not re-derive)

- Belt verifier @`d4a86a84e1`, **negative-controlled 8/12 pre-fire** — their own control run, not
  an assertion.
- Baseline **19 cols / 18,051 rows**.
- 0.6.2's final log @`d172142b44` (21:06Z) with the corrected window and the clock correction.
- **⏰ THE CLOCK IS `FRI 2026-08-21 11:30Z` (07:30 ET), live-verified ENABLED — NOT the stale
  02:00Z that had propagated to four seats.** Andrew-direct and load-bearing.
- G4b deploy prereqs verified live in S3, re-verified post-merge, and re-verified again in §1 here.

## 5. SUCCESSOR'S FIRST ACTS

1. **Re-arm the watch** — emitting on **LANDING *and* OVERDUE**; a landing-only watch is silent on
   the failure that matters.
2. **Settle the re-pin** (§2) before the fire, not after the alarm.
3. Run the belt verifier against the §1 bytes; then G1/G4/G4b proof instance → RAVC close to COO,
   cc CTO.
4. Read the two stranded messages directly from `org/mcp/inbox/0.6.2_AE_PartnerETL/` — they are
   files on disk; nothing will deliver them.

**Open in that lane, untouched by tonight and their own question:** the G1 bronze-fetch leg (shared
with `0.2.0_DS`, Rule 13) and three STAGED at `0.6.2_AE_PartnerETL~A` (MDPF_3FIRMS 3F-B4 / 3F-B6 /
3F-S1).

**Sequencing unchanged:** this sits inside the FRI belt at 11:30Z, ahead of R14's 12:45Z first
green and my 13:30Z PB-1 proof-read.
