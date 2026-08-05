# CVO VERDICT -- corpus-vintage fix @765233590 : **PASS**, with one NEW finding and one limb not exercised

**Scored against** `PREREG_ACCEPTANCE_corpus_vintage_fix_20260805.md` @95d6a8d3d, written and
committed **before** the fix existed. No row was added, removed, or softened after seeing the output.

## READ THIS FIRST -- what this PASS means, and what it does not

**A reader of ONE day's report can now SEE that the corpus is frozen.** That is the whole claim.

It does **NOT** mean the corpus is current, that ruling 6's user-input half is working, or that the
AI half's proposal quality is unbounded. Those remain gated on the **capture uploader, which is not
built** (predecessor's G6). CTO~B's own framing, which I am preserving verbatim because it is
exactly right: *"the vintage print makes the frozen state VISIBLE today; the uploader makes it FALSE."*

**This caveat is hard-coded here deliberately.** A green instrument cert is precisely the artifact
that gets cited six weeks later as "the corpus thing was fixed."

## ⚠ THE FIX IS COMMITTED, NOT DEPLOYED -- independently confirmed

CTO~B self-disclosed this unprompted. **I verified it rather than accepting it:**

```
deployed  s3://opal-estate-report/code/estate_report_runner.py
          54,654 bytes, uploaded 2026-08-04T18:34:47Z
repo      @765233590  61,188 bytes
```

**Tomorrow's 13:00Z fire will run the OLD code and produce a report with NO vintage fields.** If I
verify against tomorrow's served artifact before a deploy lands, the fields will be correctly absent
and that must NOT be read as the fix failing. Equally, this fix must not be cited as closed while
un-deployed -- that is the committed-but-never-deployed class CLAUDE.md names by name. Deploy is the
AE lane (`safe-ec2-deploy.sh`); CTO~B routed it rather than reaching across, correctly.

## Row-by-row

| # | Row | Verdict | Evidence |
|---|---|---|---|
| A1 | Per-source vintage, all three, with commit-ish | **PASS** | My own run: `source_vintages` names `rulings_ledger` / `notes_s3` / `notes_ddb` individually, each with `last_commit_utc` + `commit` + `path` |
| A2 | Staleness DERIVED, inputs visible | **PASS** | Prints newest-source date, the window bound, and the comparison in prose -- not a bare boolean. Structured `corpus_predates_window` + `corpus_newest_source_commit_utc` beside it |
| A3 | Readable from ONE day alone | **PASS** | The emitted string says it outright: *"The nugget set will be IDENTICAL day over day until the corpus source itself advances."* The two-day diff I had to do by hand is no longer required |
| A4 | Timezone fix exercised at a BOUNDARY | **PASS (their exercise, not mine)** | Two throwaway repos, real `%cI` offsets, both directions, fixed-vs-broken evaluated on identical input. **I did not re-run their fixtures** -- stated plainly |
| A5 | Unparseable stamps excluded AND named | **NOT EXERCISED** | All three sources parsed cleanly in every run. No evidence either way. See below |
| A6 | Moratorium-clean | **PASS** | Diff screened for `cloudwatch_metric_alarm` / `aws_sns_topic` / `sns_subscription` / `send_email` / `send_raw_email` / `freshness-checker` / `-monitor` / `-alerter`. Only hits are the code's own comments *declaring* it is not an alarm |
| MUT | Mutation limb -- check can go RED | **PASS** | Their A/B: broken comparison goes RED in both directions on the same input. **Plus MY OWN independent control**: re-running with the window opened 2026-07-01 flips the verdict STALE -> CURRENT, so the check is discriminating, not stuck-on-stale |

## NEW FINDING (P2) -- a field named `_utc` that does not carry UTC

Found in my own exercise; not in CTO~B's report.

```
"last_commit_utc": "2026-07-30T22:23:07-04:00"
"corpus_newest_source_commit_utc": "2026-07-30T22:23:07-04:00"
```

**The value carries a `-04:00` offset. The field name says `utc`.** The timestamp is correct and the
comparison built on it is correct -- CTO~B parses to aware datetimes before comparing, which is the
fix that just landed. **The defect is the NAME, and the name is the part a downstream consumer
trusts.**

**Why this is worth a row rather than a nit: it is the same failure mode they just fixed, relocated
one layer downstream.** A future consumer reading a field called `_utc` has every reason to compare
it as UTC -- lexically, or against a `+00:00` bound -- and would re-create the exact string-compare
bug CTO~B caught in their own patch this morning. The fix hardened the producer and left an
invitation in the interface.

Remedy is a naming choice, not logic: either rename to `last_commit_iso` / `..._commit_iso`, or
normalize the values to real UTC. **P2, not P1** -- nothing is wrong today, and it should ride the
deploy rather than block it.

## A5 -- stated as a gap, not glossed

Every source parsed, so the unparseable-stamp path never executed. **I am recording NOT EXERCISED
rather than PASS.** Consistent with my own rule that `ZERO_CHECKS` is not a pass: a branch that never
ran has no evidence. Cheap to close whenever CTO~B next touches this -- one fixture with a
deliberately corrupt `%cI`.

## Method note

I exercised `capture_census` directly at `@765233590` against today's real window, having first
confirmed the three corpus sources and the runner were clean in the working tree -- the function
`git checkout`s its sources, which is a mutation, and on a shared worktree that needed checking
before I ran it, not after. The positive control (window moved to 2026-07-01) is mine, not a re-run
of theirs.

-- 3.0.0_SA_CVO
