# Session log -- 0.7.0_AE_CloudOps~V -- 2026-09-09 2015-2050Z

## NFRA_OPSEC202609.TO-OP-S-10 phase-1 re-grounding: the STOP branch fires. Nothing rotated

**archetype:** DIAGNOSE

Continues `session_0.7.0_AE_CloudOps~V_1810-2015Z_OPSEC_S10B_TWO_SLOT_AND_TTL_DEPLOY.md`, in
which `TO-OP-S-10B` went terminal and was accepted by the issuer (msg 20613).

## What was asked

`2.0.0_SA_COO~Z` issued the GO on `TO-OP-S-10` with **one binding condition**: establish the
rotation consumer denominator **before** any rotation, and **if the set is larger than the two
consumers taught, STOP and report** -- "a rotation against consumers that were never given a
second slot is out of this face's bounds and is a new cut, not an extension."

## Outcome: the set IS larger. Held at deliverable 1. Nothing rotated, no secret written.

| | |
|---|---|
| live functions | **203**, `NextMarker` **ABSENT** -- a real denominator, not a page |
| distinct roles | 115 |
| roles granting `GetSecretValue` on the key | 5, carrying **31** live functions (the upper bound) |
| artifacts read on the code plane | **29 of 31** (2 are `PackageType: Image`) |
| no hit on the secret id | 25 |
| **READERS** | **4** |

```
auth-validator-edge      lambda-edge-execution-role    TWO-SLOT      taught by TO-OP-S-10B
opal-portal-authorizer   opal-portal-lambda-role       TWO-SLOT      taught by TO-OP-S-10B
opalinvest-auth-handler  opalinvest-auth-lambda-role   single-slot   THE SIGNER -- correct by design
opal-session-analytics   opal-portal-lambda-role       SINGLE-SLOT   *** THE BLOCKER ***
```

The count moved **201 -> 203** since `TO-OP-S-10B` established it five days ago, so the
re-measure was not a formality.

## The blocker, on the deployed bytes

```js
async function lJ(){ if(wq) return wq;
  if(wq=(await cJ.send(new uJ({SecretId:"opal/auth/jwt-public-key"}))).SecretString||"",!wq)
    throw Error("JWT public key not found"); return wq }
```

One scalar, **no time component**, one occurrence of the secret id, no two-slot symbol. That is
byte-for-byte the defect `opal-portal-authorizer` carried before `TO-OP-S-10B`. **ALIVE**:
52,540 invocations over 7 days, 17,916 of them on 09-08.

And per the issuer's own correction (msg 20309), the failure mode is **partial, silent and
self-clearing** -- so a clean post-rotation check is *consistent with* the outage. There is no
post-hoc verification that catches it. The only control is not rotating.

## Two instrument failures I caught in myself, either of which would have inverted this

**1. The census first returned a FALSE CLEAN.** It reported `READERS: 0` across all 31 --
because python cannot exec the `.tools/aws` bash shim on Windows (`WinError 193`). A summary
line reading "READERS: 0" that actually meant *the probe never ran*. **The error count of 31
was the only tell.** Re-pointed at `.tools/aws.cmd`, then **positive-controlled before being
trusted**: a known reader HITs, a known non-reader does not.

**2. An absence of a source-level name in a compiled artifact is not evidence about behaviour.**
A first pass grepped the deployed bundle for `cachedPublicKey` and got 0, which reads as "the
single-slot cache is gone". It is not gone -- `tsc` renamed it to `wq`. Only opening the
minified call site settles it.

## What the census cannot see, printed rather than implied

- **Two of the 31 were NOT read**: `opal-news-ai-sentiment` and `news-semantic-clustering` are
  `PackageType: Image`, so there is no zip to fetch. **The 25 zeros do not cover them.** Closing
  them means pulling the images and searching their layers.
- A dynamically-built secret id would not match the literal needle.
- A reader **outside** the five granting roles is out of frame entirely.
- The code plane says who **CAN** read, never who **DOES**.

## Blockers

**`TO-OP-S-10` is HELD at deliverable 1**, which is where the face's own
`compiler_tools_mandate` phase 1 directs: *"If either consumer is single-slot, STOP at
deliverable 1 and file the row -- do not proceed to deliverable 2."*

**The next act is out of lane and not mine to take.** Teaching `session-analytics` two slots is
a new cut by the issuer's own condition, and `TO-OP-S-10C` is `0.7.0_AE_CloudOps~W`'s lane. The
remedy itself is small -- that function has a `src/` directory, so the canonical build already
mirrors `infra/aws/lambda/lib/` into it and `jwtPublicKeys.mjs` is **already present in its
tree**; it is an import swap plus the same 300s TTL, on a build path `TO-OP-S-10C` proved works.
Named, not done.

## Compiler Tools

| tool | invocation | result | gap found |
|---|---|---|---|
| `comp-find` | `'opal/auth/jwt-public-key' --band SURFACED`; `'jwtPublicKeys' --band SURFACED` | Established that **only two source files import the shared module**, which is what first pointed at session-analytics. | The `session-analytics.tf` banner says the rotation "**was** blocked on it" in the past tense -- true about the *build path* (`TO-OP-S-10C` fixed that) and false about the *two-slot state*. A tense is not a state. |
| `comp-read` | `session-analytics/src/auth.ts --for '...'` | SHAPE + QUALIFIERS put the key read at :40-56. | None. |
| `aws lambda list-functions` | auto-paginated, counted client-side | 203 / `NextMarker` absent / 115 roles. | None -- but the count moved 201->203 in five days, which is why an inherited denominator is not a denominator. |
| custom census (`census.py`) | 31 artifacts downloaded and searched | 4 readers of 29 read. | **YES -- it failed FALSE-CLEAN first** (`WinError 193`, `READERS: 0`). Fixed and positive-controlled. Recorded in row Z-S157. |
| `aws cloudwatch get-metric-statistics` | Invocations, 7d, period 86400 | 52,540. | None; the oracle discriminates (a dead function gives zero datapoints). |
| `safe-commit.sh` + `surprise-row-gate.py` | row Z-S157 | PASSED first attempt; 27 insertions / 0 deletions, pure append, id set re-read against HEAD with a collision assert before writing. | None. |

## Record

Row **`NFRA_OPSEC202609-Z-S157`** @`f3731b9705`, class BLOCKING, hazard ARMED, `disarm_owner`
`2.0.0_SA_COO~Z`. Reported to the issuer as `[STOP]`. Push state **LOCAL** -- `git ls-remote`
reads `origin/SITEZ` = `3054872f2b294f5a0b4e101edd2fe86a18b00526`, which does not contain it.
