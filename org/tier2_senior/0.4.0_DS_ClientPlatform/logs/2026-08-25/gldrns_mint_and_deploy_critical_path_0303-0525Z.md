# OPAL_GLDRNS -- c04 disarm, the minted status, and the deploy critical path -- 0.4.0_DS_ClientPlatform~H

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Window:** 2026-08-25T03:03Z -> 05:25Z (delta since `gldrns_twr_d1_mirror_surfaces_abcd_0200-0303Z.md` @52f9098e6d)
**Lane:** `0.4.0_DS_ClientPlatform~H` (logged under the base folder; no lane folder exists)
**Project:** OPAL_GLDRNS -- the twr_daily D-1 mirror remedy. ONE project.

---

## What changed in this window

The project went from a repaired pipeline to **the critical path under a sovereign publish
intent**, and two defects were found and closed that only appeared *because* the remedy
worked.

**Commits, all now ON `origin/CLOUD` and all DEPLOYED:**

| commit | what | deployed |
|---|---|---|
| `77ecd4f0de` | c04 check-7 disarm (COO-ruled) | 03:23:48Z |
| `2ee5f8ca43` | the minted status `NO-PRIOR-BALANCE-ACCOUNT-ABSENT` | 05:06:45Z |

(`b9a665364f`, from the prior window, deployed 03:01:42Z.)

---

## 1. Andrew-direct: publish intent, and this project became the critical path

Relayed by `1.0.0_SA_CTO` @`742fc3dfec`, VERBATIM: *"I do want to publish i want to get this
shit live but we need to validate that it actually works on the backend side."*

CTO's re-order: `twr_daily` refused 7,335 of 7,335 rows at the frontier, so **until the
remedy landed the backend computed not one return and no frontend work could change that.**
The gate's test is EXERCISED -- Rule 22a's BEHAVIOR layer in his own words -- and "works"
means the scheduled run's own artifact read, never a successful invocation.

## 2. BLOCKING: the ratified acceptance was unachievable without doing the forbidden thing

The relayed acceptance required `REFUSED-NO-BMV -> ZERO` on the scheduled run. My exercise
produced **17**. I measured what they were before reporting:

```
accounts at D=2026-08-19 .......... 7,332
accounts at D-1=2026-08-18 ........ 7,315
at D but ABSENT at D-1 ............ 17     == the REFUSED-NO-BMV count, EXACTLY
```

These accounts did not exist the prior trading day. **Zeroing them requires manufacturing a
BMV, which `GLD-inv-1` and `GLD-a-4` both forbid** -- so taken literally the criterion could
only be satisfied by committing the defect the decomp's own invariant exists to prevent.

I offered **(A)** narrow the criterion (cheaper, my recommendation) or **(B)** split the
status, and adopted neither on my own authority.

**CTO ruled (B), declining (A) for a better reason than I had:** narrowing would encode
today's population fact into a ratified sentence -- the moment-as-mechanism class, *which is
the class I had named in raising it*. CVO's framing was the decisive one: **the criterion is
not wrong, the AXIS is incomplete.**

## 3. The mint (`2ee5f8ca43`)

`piv.get()` returns the SAME `None` for two states with OPPOSITE remedies:

- the D-1 **partition** is not loaded -> a WIRING state -> `REFUSED-NO-BMV`. The mirror
  remedy moves it. This is the population the acceptance requires to reach zero.
- the partition IS loaded and **this account** is not in it -> a POPULATION state -> nothing
  moves it, ever.

**Discriminator:** `dates_loaded = set(piv.index.get_level_values("business_date"))` -- a
fact already in the frame c02 builds. No new input, no second calendar source.

**NAME:** minted `NO-PRIOR-BALANCE-ACCOUNT-ABSENT`, deliberately NOT CTO's offered
`...-NEW-ACCOUNT`. Absent-at-D-1 is what is MEASURED; "new" is an inference the data does not
support -- an account can be absent for a day and return. CTO was told and offered the swap.

**Rule 24, four postulates, shipped with the mint** (full record in the commit message). The
load-bearing one is (iv): **the wiring value moves on the mirror remedy and the population
value NEVER moves** -- which is exactly why they cannot share a label. Cited the c04
precedent from two hours earlier as the template, one layer down.

**Result on real data:** `{'OK': 6393, 'UNCOMPUTABLE-ZERO-BMV': 922,
'NO-PRIOR-BALANCE-ACCOUNT-ABSENT': 17}` -- **`REFUSED-NO-BMV` = 0.** The ratified acceptance
is satisfiable AS WRITTEN with nothing amended.

**`GLD-inv-1` mutant RE-RUN on the minted path**, both directions -- the guard is not
inherited when the branch it guards is edited. Defaults -> 3 FAIL naming the new status;
revert -> byte-identical `md5 e809f172674fd30e3c34da9462588a34`. Tests 24 -> 25.

## 4. c04 check-7 disarm (`77ecd4f0de`)

`c04_validation_battery.py:140` passed `twr_daily=None` HARDCODED while every sibling table
loaded via `_try(...)`, so the anomalous-return census **had never evaluated a return and
could not**, while the manifest reported as though all checks ran. Its else-branch message
was also falsified by this remedy.

COO ruled the **disclosure** half mine and the **remediation** (actually passing the frame)
CTO's, sequenced after the mirror remedy. Minted `NOT-EVALUATED` -- a WIRING state, distinct
from `PENDING-BACKFILL`, which asserts a backfill will fix it *and no backfill can*. Landed
on all four surfaces carrying the claim (check, manifest, printed line, docstring
vocabulary). Exercised: `BATTERY: 8 of 9 checks RAN | NOT-EVALUATED (not wired):
['anomalous_return_census']`.

**Residual I measured and deliberately did not absorb:** an AST census found 14 `grade()`
call sites, 4 unconditional. **Three checks are hardcoded constants with no implementation**
(`cash_txn_vs_balance_roll`, `bmv_rolls_from_prior_emv`, `economic_pnl_identity`), so my own
`checks_ran: 8` still counts them as "ran". Better than "9 checks" and **not yet true**. I
did not regrade them -- classifying "pending" vs "unimplemented" is a Rule 24 act on checks I
do not own, and one of the four constants (`schwab_native_return_tie`) is legitimately final.
Routed to COO; still open.

## 5. An error of mine that travelled three seats

I asserted my work was unpushed/undeployed **from last-known context instead of measuring
it**, on a sovereign critical path. CTO carried it into a push request to MSTR. I caught and
retracted it same-turn; CVO independently falsified it with a controlled `ls-remote` read;
MSTR closed it from the integrator record. **Nothing was spent because both corrections
arrived before the integrator acted.**

Thereafter I measured push state with both controls every time -- `ls-remote` against the
tracking ref (ruling out the stale-ref mode that would fake the result) plus a bogus hash as
a negative control.

## 6. The gap I caught because of that lesson

After the mint I measured rather than assumed, and found `2ee5f8ca43` **NOT on the remote**
and the deployed `c02` carrying **0** occurrences of the new status (positive control
`REFUSED-NO-BMV` = 3). At 12:45Z that would have emitted the pre-mint vocabulary and **failed
the acceptance the mint existed to make achievable**.

COO found a possible escape -- their remedy (A) is basis-independent and might have passed
anyway -- and asked the one question that decided it: **does the pre-mint c02 emit the D/D-1
account-set delta onto the artifact?** Measured from the deployed bytes: the manifest is six
fields and emits **zero** population-delta tokens. **So (A) was not dischargeable either;
12:45Z would have failed both forms.**

**I declined to run the deploy myself** although Rule 13 makes it my lane and
`safe-deploy.sh` accepts explicit files. Rule 13's own sequence is commit -> **push** -> S3
cp; deploying first would put bytes on the executing surface **whose build input is not on
the remote**, which is worse than stale because `comp-pipescript` can see stale and cannot
see unresolvable provenance. MSTR pushed at ~05:05Z and the deploy rode the pre-push hook.

## 7. Deploy verified at the APPLIED layer, three seats, by CONTENT

I re-read rather than inferring it landed:

```
mint marker NO-PRIOR-BALANCE-ACCOUNT-ABSENT ... 2
dates_loaded (the discriminator) .............. 2
POSITIVE CONTROL REFUSED-NO-BMV ............... 5
NEGATIVE CONTROL zzz_no_such_marker_9999 ...... 0
deployed (CRLF-normalized)    f8b761f3d05acee12d2f7f8af8f44b7b
repo @2ee5f8ca43 (normalized) f8b761f3d05acee12d2f7f8af8f44b7b   IDENTICAL
2ee5f8ca43 ancestor of origin/CLOUD (controlled fetch)
```

MSTR adopted the normalized-hash-against-the-building-ref as **the better form** over a
marker count, and is folding it into the `comp-closure` repair TO as a reference
implementation.

**The CRLF trap fired twice on live evidence.** A raw hash of a deployed object against its
git blob reports MISMATCH on a *correct* deploy (deployed CRLF, blob LF). I hit it first and
nearly reported false drift; CTO hit it independently and it **nearly became a provenance
accusation** against this deploy. Three disagreeing signals saved it -- `git status` clean,
token grep positive, hash negative. **A hash alone would have convicted.** I also made the
adjacent error once: resolving c04's source **by filename** at a ref that predates its
disarm, which reported GENUINELY DIFFERS. The file was right; the REF was wrong.

## Blockers

**None.** Nothing is held on this seat and nothing is asked of anyone by me.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `-i 'REFUSED-NO-BMV'` | PASS | consumer census before minting -- established no consumer branches on the refusal status STRINGS |
| `comp-find` | `-i 'twr_daily' <runners_49f>` | PASS | located c04 as the only twr_daily consumer in the tree |
| `comp-pipescript` | `deployed c02_twr_engine.py` | **REFUSED rc=2** | see gap below |

**What worked:** `comp-find`'s BAND separation made the consumer-safety call cheap and
defensible -- it distinguished a comment mention in `perfrp_rollup` from real branching.

**What failed / GAP FOUND:** `comp-pipescript deployed c02_twr_engine.py` **refuses at this
seat** (`--pipeline` required) and offers only `inf-runners_inf` and `cot-runners_cot` --
**neither is the 49f tree under test**. Yet `0.0.0_AB_MSTR` cited `[advi:gold] MATCH` (filter
matched 1 of 57) and `3.0.0_SA_CVO` cited `STALE` (1 of 69) from what reads as the same
command. Three seats, three behaviours, and two differing denominators. **Raised as an
OBSERVATION, not routed as a finding** -- both their verdicts were corroborated by other
evidence and the STALE one matched my byte read exactly. It matters only because this is the
instrument that established both a MATCH and a STALE on a publish path, and a same-name
script in three trees is the shape that yields a confident answer about the wrong file. A
flagless full sweep exceeded 120s at this seat and was left running rather than chased.

## Files Modified

See commit messages `77ecd4f0de`, `2ee5f8ca43` -- both carry full reasoning and the Rule 24
records.

| file | change |
|---|---|
| `c04_validation_battery.py` | `NOT-EVALUATED` grade; `checks_ran`/`not_evaluated` in the manifest; printed line; docstring vocabulary |
| `c02_twr_engine.py` | minted `NO-PRIOR-BALANCE-ACCOUNT-ABSENT` with the `dates_loaded` discriminator |
| `tests/test_c02_twr_engine.py` | +1 test exercising BOTH sides of the wiring/population split; two fixtures updated |

Tests: **25 passed**. CVO re-ran them at their own seat: 13 passed, true rc=0, discriminator
confirmed sound.

## MCP traffic

~30 messages handled, 8 sent. Significant: Andrew-direct publish intent (CTO 68655); my
BLOCKING acceptance finding (68685); CTO's option-B ruling (68735); AE~G's self-falsification
of their own s.14(a) baseline figure (68753); my deploy-state correction (68764); CVO's STALE
corroboration (68845); COO's ship-the-mint routing + the (A)-discharge question (68848); my
answer (68865); MSTR's deploy confirmation (68873); CTO's both-halves-armed close (68884).

## Current State

**All 21 owned cells DELIVERED, COMMITTED, PUSHED and DEPLOYED.** `GLD-f-2`'s APPLIED layer
is satisfied for every file this seat touched, each verified by reading deployed bytes
against the ref that built them, CRLF-normalized, with positive and negative controls.

The chain executes from `s3://opal-data-49financial/_code/` via `aws s3 sync --delete` fresh
on every run (AE~G's SSM `get-document` read of the actual `runCommand`, not the Terraform
comment describing it), so **the code channel IS the executing surface here** and no Lambda
package re-pin is involved -- CVO withdrew that caveat after finding no
`lambda-source-map.json` entry for this chain.

**Schedule: `cron(45 12 * * ? *)` UTC, ENABLED**, target `advi-49f-gold-dispatch`.

## Next Steps

1. **[unassigned -- the artifact, not a seat]** `GLD-f-1` closes ONLY on the 12:45Z SCHEDULED
   run's own artifact: `REFUSED-NO-BMV` = 0, real returns present with the count and its
   denominator printed, and the three legitimate refusal classes reported in their own words.
   **No ad-hoc run** -- Andrew's own rule makes one a QA instrument and never production
   evidence, and COO has backed that refusal. `3.0.0_SA_CVO` has pre-declared their s.14(c)
   read so it cannot be shaped by what the artifact shows.
2. **[2.0.0_SA_COO]** the three unimplemented-constant c04 checks (68380) -- still open.
3. **[1.0.0_SA_CTO]** `GLD-f-3` deploy-completion ledger entry. The deploy has already
   completed, so the honest form is a CLOSED retrospective entry rather than an open one. I
   named it rather than opening it because I am not the pusher; I will write it if asked.
4. **[whoever owns comp-pipescript]** the tree-resolution discrepancy above. One run settles
   it; nothing gates on it.
5. **Surface (e)** remains held out under Rule 24(iv), its 6 partitions still UNCLASSIFIED by
   status. The contract's `refused_dates` names the dates but not which of the three statuses
   each carries, and I have not quoted them as classified.
