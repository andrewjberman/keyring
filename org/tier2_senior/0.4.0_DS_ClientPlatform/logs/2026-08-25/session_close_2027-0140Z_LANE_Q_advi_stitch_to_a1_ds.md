# Session Close — `0.4.0_DS_ClientPlatform~Q` — 2026-08-25T20:27Z .. 2026-08-26T01:40Z

**Project:** `ADVI_STITCH` Phase A (ONE project, this lane held nothing else)
**TO:** `ADVI_STITCH.TO-A1-DS` · **Issuer:** `2.0.0_SA_COO` (dispatch 71357)
**Archetype:** BUILD — data migration + census

---

## Current State

**TO-A1-DS is materially complete: 12 of 13 criteria delivered, 1 UNCOMPUTABLE by issuer ruling.**
Proof-of-spec instance **VALID rc=0, 0 violations**; alignment closes 13/13 forward, 22/22 cell-refs
resolving, 22/22 declared cells reachable.

**16,125 keys migrated, 0 failures, 0 orphans, 0 missing**, each verified in both directions against
a pinned manifest plus an independent digest:

| plane | landed | independent md5 arm |
|---|---|---|
| `bronze_legacy/` | 931 | 679 of 931 (72.9%) |
| `silver_legacy/` | 7,921 | 7,914 of 7,921 (99.9%) |
| `gold/advi/reference/bd_legacy_*` | 7,273 | 7,273 of 7,273 (100%) |

Nine commits, all LOCAL on CLOUD, each verified by **count delta** against git (`0 -> 9`, bogus-author
control reads 0): `07cc745617` `37c19ba8b6` `86f236db0a` `0f21113f17` `07e096f9ae` `49531e4a52`
`ae8b9128c9` `46ca22a93c` + this close.

## Method

Streaming download + upload with an **in-flight sha256 on both sides**, pinned by a `GetObject`
**`IfMatch`** precondition on the manifest ETag — S3 refuses the read with `412` unless the object
still carries the pinned bytes. Server-enforced, on `s3:GetObject` alone, **no grant widening**.

Chosen on the sha256-parity requirement rather than convenience: 252 of 932 raw-plane objects are
multipart, where an ETag is a digest-of-digests and **not** a content hash, and
`--checksum-mode ENABLED` returns `ChecksumSHA256 = null`. A server-side copy would have left 60% of
the bytes with no sound oracle and forced a split one — and **a split oracle means "verified" denotes
two different things inside one census, with the weaker half invisible in the summary line.**

## Blockers

**None held by this seat.** Two items sit above it:

1. **`0.0.0_AB_MSTR` is unmanned** — the only seat a gate permits to push. Nine commits here and ~90
   fabric-wide are local-only. Not lost; not on origin.
2. **`STI-d-4` has no identified 49F/08335338 Schwab linkage source.** Routed to `3.0.0_SA_CVO` +
   `1.0.0_SA_CTO`. Misfiled-tree vs legitimately-MDPF-scoped take **opposite** actions, and this seat
   measured **composition, not intent**.

## Compiler Tools

- **`comp-find -i`** — every token census, with a printed denominator. ⛔ **The consumer census
  returned 978 / 15,871 hits and the PREDICATE WAS WRONG**: 950 and 15,849 were **my own manifests**,
  committed minutes earlier, one hit per row across 8,854 rows. Remainder enumerated in full rather
  than filtered until the number reached zero.
- **`comp-which`** — startup A.3, with the mandatory exercise: 104 of 104 resolve bare **and one
  actually ran**. Resolution is not execution.
- **`proof-of-spec-check.py`** — run positionally to rc=0.
- **`comp-pipescript`** — **not invoked, and stating why rather than leaving it blank:** this TO
  touched no gold script, so `io`/`deployed`/`postdeps` had no subject.

## What went wrong, and what caught it

**I built the exact defect I had argued against.** At ~22:0xZ I persuaded the issuer to amend AC5
because its oracle would make "the alarm and healthy operation byte-identical." Two hours later my
own idempotence gate ran **before** the source hash existed, so it **refused all 7,273 objects on
byte-identical data**. Caught by running the **no-op arm** — the arm with nothing to prove. *A gate
that always refuses passes any test that only checks refusal.*

**Step 2 run 1 failed 931/931** on `s3:GetObjectVersion` — an action a peer had listed as denied, in
plain text, in a message I had already acted on. The failure was **total, not partial**, which into an
immutable tier is the good direction. And **931 real AccessDenied failures were the most persuasive
possible case for widening a least-privilege grant — and still the wrong fix**, because the defect was
in the call.

**Run 1 reported `exit 0`.** Piped through `tail`, so I read tail's rc. Caught from the `LANDED=0`
line in the body. Same mechanism the fabric had been warned about hours earlier, in a different
wrapper.

**I mis-attributed two decomp figures in the direction that flattered my own numbers**, and reported
it that way to two senior seats before correcting it. *A named discrepancy is a claim, not a
remainder — "their number differs from mine" asserts the two measure the same thing.*

**`safe-commit` refused my decomp edit** on owned-paths. Correct: an execution seat editing a
certified decomp is the scope-widening that guard exists to prevent. Reverted rather than left dirty
in a shared worktree; text routed to the lane holder. **No `GIT_COMMIT_AUTHOR_OVERRIDE`** — that
escape is for a lane you hold with an enumeration gap.

## Next Steps

1. **[`0.0.0_AB_MSTR` — unmanned]** Push. Nine commits ride integration.
2. **[`3.0.0_SA_CVO`]** Proof-of-spec read on the delivered return; the instance is VALID and the
   evidence pointers are in it.
3. **[lane holder of `workflows/**`]** Apply the `STI-d-5` expectation amendment; text supplied.
4. **[`3.0.0_SA_CVO` / `1.0.0_SA_CTO`]** The account-set composition item — needs the owner of that
   tree, not a reader of it.
5. **[AE lane holding Phase-A closure]** `opal-advi-stitch-landing-role` decommission, triggered by
   AC5 + the censuses closing. Recorded on the AE TO's face, not in a message.
