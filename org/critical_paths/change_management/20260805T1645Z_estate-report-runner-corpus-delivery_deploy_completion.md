# Deploy-completion ledger: estate-report-runner corpus DELIVERY fix (OPAL_KIMIPIPELINE.DEP2)

**Opened:** 2026-08-05T16:00Z by 0.7.0_AE_CloudOps · **Status:** CLOSED 2026-08-05T16:45Z
**Authority:** 2.0.0_SA_COO GO @155926Z (TO @a07d14e45); held by me at COO's own tip-control 1608Z;
HOLD RELEASED @163441Z on the tip.
Second deploy of the day to the same key. DEP1 ledger: `20260805T1456Z_estate-report-runner-corpus-vintage_deploy_completion.md`.

## The act

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`.
Transient instance, systemd oneshot pulls on boot -> re-uploading IS the deploy (`EC2_MANIFEST.json:571`).

| | commit | note |
|---|---|---|
| DEPLOYED | `9a1856bc03` | tip; corpus delivery + budget-axis correction in-source + non-ASCII strip |
| pinned by GO | `f023857ab3` | superseded by two commits landed AFTER the GO was drafted |

## Evidence

| | value |
|---|---|
| Phase-2 local md5 | `5ff45f5e968d4a43422c973b5e8f0657` |
| Phase-3 head-object ETag | `"5ff45f5e968d4a43422c973b5e8f0657"` (no `-N`; plain md5, valid) |
| PRE | ETag `"a110981492b461e19fb9be7848b9ad09"` / 62,875 B / 2026-08-05T14:56:59Z **(= my DEP1 artifact; COO discriminator #1 PASS -- nobody deployed in between)** |
| POST | 70,281 B / 2026-08-05T16:45:22Z / VersionId `08mkactqbO4tmNg.DdLZgMqZBileQwav` |
| discriminator #2 | Phase-2 md5 **DIFFERS** from DEP1's -> genuinely new bytes, not a re-upload. PASS |
| read-back (MANDATED this TO) | served md5 identical, `cmp` byte-for-byte identical, `py_compile` PASS, **non-ASCII on served bytes = 0** |
| corpus delivery on served bytes | `CORPUS_PROMPT_BUDGET` 2 · `_bounded_json` 2 · `corpus_coverage` 11 · `KIMI_LENGTH_STARVED` 3 |
| rollback | both prior versions retained |

## Third pin-staleness event on this file in seven hours -- all three caught by one control

| # | pinned | actual tip | delta | severity |
|---|---|---|---|---|
| 1 | `765233590` | `a254104b34` | REAL CODE (`_utc` -04:00 fix) | would have shipped a filed defect |
| 2 | `f023857ab3` | `f13671cfa3` | comments: budget-axis correction | cosmetic **but directional** -- would have re-armed a wrong hypothesis |
| 3 | `f023857ab3` | `9a1856bc03` | comments: non-ASCII strip | ASCII hygiene on an AWS-running file |

The tip-check is **load-bearing, not ceremonial.** One check, three different severities, nothing shipped wrong.

## The instrument that made #2/#3 a ten-second call

`git diff` said 3,150 bytes changed -- which alone would have forced a full re-adjudication under deadline.
Instead I compared **parsed ASTs**, which discard comments:

```
f023857ab3  AST-sha256 6a70e3679fcc65a3a1c9288abf8b1019
9a1856bc03  AST-sha256 6a70e3679fcc65a3a1c9288abf8b1019   IDENTICAL
```
plus a line audit: 31 changed lines, **zero** non-comment non-blank. Same program; nothing behavioural to
re-adjudicate. That is what let COO settle a vintage CVO had not named *without* assuming an acceptance
extends -- the difference was **measurable**, not a judgement.

**LESSON I OWE THE RECORD (COO's, and it corrects me): an instrument that returns IDENTICAL is worthless
until it is shown able to return DIFFERENT.** COO ran the negative control I did not -- mutating
`CORPUS_PROMPT_BUDGET` 25000->20000 CHANGED the hash. I reported an identity before proving the tool
discriminates. Run the mutant before quoting the match.

## The budget refutation that decided the shape of this deploy

CTO~B flagged a risk and offered to retune `CORPUS_PROMPT_BUDGET` 25000 -> 20000: the new prompt is 61,378
chars vs "the only size ever exercised," 60,000, and KIMI_EMPTY was "reasoning-budget starvation, the exact
dimension this sits on." **Checked instead of nodded, and it does not hold -- two different budgets:**

```
INPUT  prompt size    ~60KB -> 61,378 chars   <- what the patch grows
OUTPUT max_tokens     4000  -> 32000          <- what KIMI_EMPTY ACTUALLY was; UNCHANGED here
```
Grounded: `95e1f0283f`'s diff is literally `-"max_tokens": 4000 / +32000` (a COMPLETION budget);
`OPAL_KIMIPIPELINE_PRD.md:38` says the starvation happened *"on the ~60KB production prompt"* -- so that
input size was already fine. `f023857ab:965` keeps `max_tokens: 32000`. ~350 added input tokens consume
zero `max_tokens`.

**And 60,000 was never a tested boundary:** `a254104b34:826` is `json.dumps(resources, indent=2)[:60000]`
-- a hand-picked slice on ONE half, not model-derived. Calling it "the only size ever exercised" dressed an
arbitrary internal constant as a validated limit. Retuning would have traded 5,000 chars of the corpus --
the thing the patch exists to deliver -- against a misidentified risk.

CTO~B verified every claim at source, withdrew the retune, and landed the correction **in the source
comments** (`f13671cfa3`) so tomorrow's responder meets it where the failure happens. CVO reached the same
verdict independently off the 8x output margin -- two seats, **different derivations**.

**OPEN RESIDUAL, not cleared:** kimi-k3's real context window is not pinned in-repo (`KIMI_MODEL` resolves
from env via `var.kimi_model`, `instance.tf:120`). "61,378 is comfortable" is an **ESTIMATE, not a
measurement.** The settling instrument is vendor egress, which requires Andrew's per-use word. Not called.

## Scope honesty

**Deployed != exercised.** Box transient and stopped; **nothing has run this code.** Tomorrow's 13:00Z boot
is the first execution of BOTH of today's deploys. CVO owns the served-report verdict.
The corpus remains the frozen `AWS_ESTATE_CENSUS_20260730` mirror -- this **delivers** 153 nuggets we
already hold, it does not make them **current**. B6 capture uploader remains the substrate fix.
No alert/alarm/SNS/SES/checker/monitor built.
