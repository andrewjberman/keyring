# AMENDMENT to `b1b873ddce` (drive_log_20260831T0035Z.md) -- 2026-08-31T00:4xZ

**Scoped to the refuted clause only.** The log concluded that remedy 3 could not be satisfied and that a
rebuilt arm would be born unsound. **That is wrong.** `3.0.0_SA_CVO~X` corrected it at 00:36:24Z with a
live read; I verified before accepting.

## What is refuted

| the log said | the measurement says |
|---|---|
| *"remedy 3 cannot be satisfied by the arm's code"* | **Remedy 3 is available and already landed**, under option (b) |
| *"a rebuilt arm would be born UNSOUND on day one"* | **False.** The primary bytes are retrievable from an immutable run-addressed URI |
| *"no arm I write can produce that property"* | **False.** Resolve the URI, verify the digest, cache locally |

**The carrier:** `s3://opal-313476888478-globgrph/c3materialize-b4/out/eb009c01-c27e-46b3-af85-eb22dbfba01a-b4231e6374ce/W_STRUCTURE_FACTORIZED.json`

**Verified on this seat's own instrument, not inherited** — `s3api head-object`: **2,662,267 bytes**,
LastModified **2026-08-28T20:22:00Z**, ETag `6d6709789cfe0c6d398f86d23d0caa45`. Byte count matches the
local file exactly, and the local `.tmp` mtime of 20:36:35Z sits **fourteen minutes later** — the shape of
a download, not an original.

## ⛔ The answer was in my own card, in a field named for the relationship

`4e7016f471` — **which I authored** — carries at `artifact.location` a **`projection_of`** entry naming
that exact S3 URI. **The card already records the `.tmp` file as a projection of the immutable object.**

I read `rederive_l3w2.py:39` (`FACT = ".tmp-cro-b4-eb009-audit/..."`), concluded the input had no custody,
and **never re-opened the card I wrote that resolves it.**

**Tonight's class again, and this time both carriers were mine to check:** I measured ONE carrier — the
`.py` source line — and treated it as the whole answer while the **neighbouring** carrier held the
resolution. Same shape as reading `blocked_on` and missing the route, or the GAP key and missing
`owner_and_prd_1i_iv_vi` two keys below. **The aggravating difference: the neighbouring carrier was not a
peer's artifact I had to think to consult — it was my own card, and the field is called `projection_of`.**

⚠ **And note the direction the error ran, because it is the one nobody checks: it made me MORE cautious,
not less.** I declined to build, routed a custody question to another lane, and stated a conservative
fallback. **Nothing was damaged and no wrong artifact shipped — which is exactly why a false blocker is
worth correcting loudly.** An over-cautious wrong conclusion produces no visible failure, so nothing forces
it to the surface; it quietly costs a tick and asks other seats for work already done.

## What STANDS from the log, unchanged

The `.tmp` copy **is** uncustodied, **was** never committed anywhere (`git log --all` empty), and **must
not be cited** by the arm. The content address `e91d6991…` measured locally is confirmed correct — it
matches a fresh download. The three disqualifying grounds read at source (`:421` one draw, `:403` shared
RNG stream, `:39` temp path) all stand. The `date -u -r` mtime discipline stands.

## Consequence

**The arm is GO** and builds against the **served URI** with mandatory size + sha256 verification and a
**loud refusal** on retrieval failure or digest mismatch — never the temp path. That refusal is not
decoration: **an arm that silently fell back to a local cache would reintroduce the exact uncustodied
input the card disqualified its predecessor for.**

**PLACEMENT MEASURED:** origin/CLOUD `ea912ac001` at my 00:29:27Z read; `b1b873ddce` and this amendment
ride the next window.
