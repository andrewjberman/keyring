# ETFS_SATELLITES.TO-2 -- ISSUER'S DISPOSITION, and the measurement that moved the evidence bar

`1.0.0_SA_CTO~Z`, 2026-08-27 ~23:4xZ. Arch-gate ruling. Two broadcasts: msg 11054 (disposition),
msg 11078 (the correction to my own 11054 section 4.1).

---

## 1. DISPOSITION: TO-1 and TO-2 are DELIVERED. No successor TO is needed to BUILD a predicate.

The board read `ACTIVE -- UNBLOCKED; WAITING ON A SEAT.` on both. **MEASURED, not taken from the
producer's self-report:**

```
dc56a72c21  0.4.0_DS_ClientPlatform~W  2026-08-27 14:14:26 -0400
            satellites_registry.py 320L · satellites_weights.py 270L · test_satellites.py 481L
            2 fixtures · TO-1 + TO-2 PROOF_OF_SPEC · 2382 insertions
7f44de8371  proofs re-pinned off PENDING-COMMIT
ON ORIGIN   origin/CLOUD and origin/SITEZ   (git branch -r --contains)
```

STOP: nothing was waiting on a seat. The work was built, proven and pushed roughly five hours before
the panel concluded the critical path had no producer. The producer's own message said
`LOCAL @dc56a72c21`; the branch-contains read says otherwise. **An UNDER-stated push state survives
review exactly as any conservative error does** -- see `conservative-error-passes-its-own-check`.

## 2. Andrew's two rulings are CONSISTENT; the file gave the right expression the wrong JOB.

| ruling | verbatim | what it settles |
|---|---|---|
| ~16:1xZ | "Some SMA that has a blend of a Satellite and Opal Model is not a Satellite, they merely are allocating to a Satellite." | IS-A vs HOLDS-A |
| ~22:5xZ | "it should simply be 'Does it say \"Opal Satellite\" in the name? Add it and track henceforth if so.'" + "if it says 'opal satellite with some other shit' that is not acceptable" + "if it is formatted as the other opal satellites then its fine" | membership is a PREDICATE, and it is ANCHORED-AND-FORMATTED |

`satellites_registry.py:213` already carries `^Opal Satellite <N>$` -- deliberately as a DRIFT ORACLE,
never as a membership test. The later ruling **promotes it**. The act is one decision, not a rebuild.

STOP: **the file's ~40-line "WHY THERE IS NO PREDICATE" section must be STRUCK, not annotated.** It
argues, with swept planes and positive controls, that no predicate can exist -- citing the ~16:1xZ
ruling that ~22:5xZ supersedes. Left standing beside the predicate it forbids, it is a
confidently-wrong mechanism, and those propagate as CITATIONS rather than as gaps
(`a-true-conclusion-without-its-mechanism-is-re-derivable-wrongly`, the mirror). A rule stated next
to its own violation launders the violation.

`:55-58` additionally says a false positive "costs one question" -- true of the oracle job, FALSE of
the predicate job. Promotion raises the correctness bar to exactly the one the file says the
expression does not meet. That sentence goes with the section.

## 3. THE MEASUREMENT THAT MOVED THE BAR -- and it reversed my own ruling section 4.1

I first ruled the negative arm sound because 21 near-miss rows exist in-corpus. Then I tested whether
they DISCRIMINATE. Over `roster_2026-08-27.json`, 65 rows, provenance claim `measured`:

```
FULL    ^Opal Satellite \d+$   (as shipped)  ->  9 matches, 0 false admits
NO TRAILING ANCHOR  ^Opal Satellite \d+      ->  9 matches, 0 false admits
NO LEADING ANCHOR    Opal Satellite \d+$     ->  9 matches, 0 false admits
NEITHER ANCHOR       Opal Satellite \d+      ->  9 matches, 0 false admits
SUBSTRING (naive)    /opal satellite/i       ->  9 matches, 0 false admits   <- RULED OUT BY ANDREW
```

STOP: **every variant scores identically, including the one the sovereign explicitly rejected.**
A green run certifies nothing about the design.

**Why, and it is subtler than "the blend row is missing":** the blend rows ARE present --
`Blended Opal / Satellite 50`, `Opal - Cash + Satellite 50`, `Opal Sat 50+ 15% cash`,
`Opal UST/Sat 80 33/67`, `Core | Satellite 98`, and 16 more. But **not one of the 21 contains the
contiguous string `Opal Satellite`.** Every one fails at the FIRST discriminator, so the leading
anchor and the trailing `$` are never reached.

> **21 near-misses that all miss the same way are ONE test run 21 times.**

`2.0.0_SA_COO~Z`'s stated fact (the blend row is absent) is refuted; their INSTINCT -- that a green
run on this corpus would look like proof -- is correct for a reason neither of us had named.

**My error class, and it recurs:** I validated on the axis I had searched (*do near-miss rows
exist?*) rather than the axis the question was about (*would a WRONG predicate score differently?*).
See `i-validate-on-the-axis-i-searched-not-the-axis-asked` and
`a-criterion-that-cannot-fail-over-its-own-window`. A row set that exists is not a control set.

## 4. BINDING ACCEPTANCE CRITERION -- synthetic fixtures, not optional

The real corpus is structurally incapable of exercising the design, so the fixture must carry:

```
MUST REJECT   Opal Satellite 50 + 15% cash   Andrew's named hazard; the ONLY probe separating
                                             the shipped form from no-trailing-anchor
MUST REJECT   Opal Satellite 50 Tax-Free     same limb, different tail
MUST ADMIT    Opal Satellite 55              proves the path DERIVES; a hardcoded list FAILS it
```

STOP: **`Opal Satellite 55` is the load-bearing row and it is a POSITIVE probe.** No negative can
distinguish a derived predicate from the old declared list -- the nine members pass under BOTH
mechanisms, which is exactly how a declared registry looks when nothing has changed. Only an admit
the list does not contain can separate them.

## 5. Constraints that travel with the promotion

1. The 21 non-canonical rows may be asserted, but they are NOT the discrimination evidence (section 3).
2. `REGISTRY_CLAIM` moves `held` -> `measured` only on the genuinely derived path; the nine hand rows
   become the POSITIVE FIXTURE and are not themselves proof -- a fixture drawn from the same 65 rows
   the predicate reads cannot discriminate.
3. **PUBLISH EMPTY, NEVER DELETE** (PT-c-2): a firm deriving zero members writes an empty set. A 404
   carries no reason, so absence must remain recoverable.
4. `RENDER_ZERO_ACCOUNT_MEMBERS` survives unchanged. `Opal Satellite 90` has zero accounts, matches
   the anchor, and IS a member. Membership is the name; rendering is not a membership question. A
   derived path that quietly drops it re-introduces the account-count heuristic Andrew disowned.

## 6. Record corrections owed by the registry owner (`2.0.0_SA_COO~Z`)

- `TO-1`, `TO-2` -> **DELIVERED**. Neither is waiting on a seat.
- The project `Blocking:` field still reads *"OPEN CALL AT ANDREW ... WHO MAINTAINS THE SATELLITE
  MEMBERSHIP REGISTRY?"* -- **DISSOLVED** by the ~22:5xZ derived ruling. A derived set has no
  maintainer; the predicate is the maintainer. That field is the last carrier still showing it open.

Push state: LOCAL at commit time (`0.0.0_AB_MSTR~Z` is the integrator and pushes).
