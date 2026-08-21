# 1.0.0_SA_CTO~Z -- session close 00:10-00:35Z: I could not find a 368-file program my own seat specified

**archetype:** DIAGNOSE
**secondary_archetypes:** SCRIBE

**Written on Andrew's direct instruction, fabric shut off.** Verbatim: *"I just shut off your entire
fabric because i dont know what you guys are doing and if you cant find any of this then we have a
bigger problem so just stop whatever you're doing and write a /log."*

**He is right and the log leads with the failure, not the work.**

---

## 1. THE FAILURE, MECHANICALLY

He asked: *"are you guys actually registering process and doing full-scale atom_decomp and
comp-adversary and etc or no?"*

I answered **NO** on both, twice, and told him `atom_decomp` "is not an executable in this tree at
all" and "the decomposition workflow is absent."

**It exists. `workflows/atom_decomposition/` at repo root. 368 files.** `compile_manifest.py`,
`emit_catalog_v02.py`, `lift_catalog_v02.py`, `battery_catalog_v02.py`, a validation report, and
15+ completed runs (portal-page-{market,macro,cma,attribution,correlations,factor-tilts,
advisor-intelligence}, news-subsystem, gips-twr-schwab-feasibility, opal-data-mdpf-colocation,
comp-verdict-tools, freshness-deploy-verdict-tools, advi-model-holdings-account-join, mdpf-serve-
label-surface, plus `runs/INDEX.json`).

### How I missed it -- three compounding steps, all mine

1. **I searched for a BINARY.** `command -v atom_decomp`, `ls .tools/*atom*`. Both correctly
   returned nothing. **The question I answered was "is there an executable named atom_decomp." The
   question I reported on was "does the workflow exist." Those are different claims.**
2. **I ran a `find` that DID locate it -- and truncated my own output.**
   `find . -iname "*atom_decomp*" | head -8`. **There were 23 matches.
   `./workflows/atom_decomposition` was number 23.** I read the eight visible rows as the result set.
3. **I never looked at the repo root.** `ls workflows/` is one command and returns 5 entries.

> **THE PAGE-SIZE-AS-TOTAL CLASS, SELF-INFLICTED, IN THE EXCHANGE ABOUT UNDECLARED EVIDENCE
> BOUNDARIES.** I had already committed the same class three times in the preceding hour and had
> written the law's own name for it into two commit messages.

### What makes it worse than a search miss

- **My own seat authored the spec.** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ATOM_DECOMP_SPEC/`
  (`00_ATOMIC_DECOMPOSITION_SPEC.md`, `01_ADVI_CASE_STUDY.md`, `02_ADOPTION_AND_EVALUATION.md`,
  plus `skill/` and `templates/`).
- **Andrew GO'd the program 2026-08-11**, recorded by this serial at `174234Z`.
- **`comp-find` told me the truth and I did not read it**: `atom_decomp` returns **569 hits /
  26,879 files -- HEAD=37, DEF=1, SURFACED=29, CONFIG=202, TEST=1, DOC=299.** A DEF band and 29
  SURFACED hits are not the signature of an absent thing. I quoted that denominator in my own
  terminal output and still said "absent."

## 2. THE SECOND ERROR IN THE SAME EXCHANGE

I told him `comp-adversary` had **"0 runs across 1,157 rail-log lines today."** The log spans
**2026-07-29 to 2026-08-21 -- 23 days. Today is 216 lines.** I welded a TODAY label onto a lifetime
count. Caught by `0.0.0_AB_MSTR~Z`, corrected to him at 00:28Z, deliverable fixed @`4bf2d171dd`.

**Also unresolved and now unverifiable at this seat (`2.0.0_SA_COO~Z`, msg 00:30:23Z, unread when
the fabric went down): "THE RAIL LOG CANNOT SEE comp-adversary" -- if the tool does not log to that
rail at all, then my "0 runs" measured nothing, and the entire finding rests on an instrument that
could not have said otherwise.** That is Rule 22a's fourth failure mode and **I did not check it
before publishing.** WHOEVER PICKS THIS UP: verify that first.

## 3. WHAT IS ACTUALLY TRUE ABOUT THE WORK (unaffected by the above)

These were measured at source and are independent of my search failures:

| Item | State | Evidence |
|---|---|---|
| **Item A** (`alwaysLoad` marks) | **BUILT** @`2b7258f31c` | 6/6 by AST at this seat: gateway `tools.py` 4, gateway `integrations/opal_portal/integration.py` 1, broker `server.py` 1 |
| **W-F detection** | **BUILT, INERT** @`bdd9aaa7c9` | verified: only importers are its own tests, 3 hits / 26,872 files |
| **WF-5 (c)** | **BUILT** @`8a748d8d31`, drift mutant @`180aa91223` | LIST response carries `cutoff_et` at `lambda_function.py:414-415` |
| **`lastModifiedDateTime`** | built @`90d526c199`, **not applied** | batch was blocked on Item A; now unblocked |
| **W-B DynamoDB stream** | **recommended DELETED** | 4.3:1 at the measured 1-min floor |
| **`closure_reason`** | adopted, 6 values | Rule-24 tested |

**Pending applies, two targets, different mechanisms:**
- `ticket_center` Lambda (Terraform): **5 unapplied commits** past the applied frontier `4bede18189`
  -- `1fd9ef2750`, `81c502cff2`, `9121a55330`, `b121c2f26e`, `8a748d8d31`. **WA-6's grant goes
  first.**
- `opal-gateway` EC2 app (`safe-ec2-deploy` + boot test): `2b7258f31c`, `90d526c199`.

**Nothing was pushed.** All 52 commits sit on SITEZ awaiting the integrator.

## 4. Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-adversary` | **PASS, self-test 4/4** | ran on 3 accepted builds; found Item A's verification had a **496-file uncited neighborhood**, and that `sweep.py`'s `0 siblings` means *no directory siblings*, not *no coupling* (v1 graph expansion unwired). **All runs: 4 sources run / 6 declared-excluded.** |
| `comp-find` | **PASS -- and I ignored it** | returned 569 hits with a DEF band for the thing I called absent |
| `find ... \| head -8` | **FAIL** | 23 matches, answer at #23, truncated by me |
| `find -newermt` | **FAIL** | parses LOCAL time (UTC-4); my non-ASCII sweep read 2 files when the population was 22 |
| AST walks (`ast.parse`) | PASS | the Item A count; correct over text matching |

**What worked:** AST over text; running `comp-adversary` at all.
**What failed:** three separate self-truncated retrievals, each of which returned a clean, confident,
well-formed answer to a narrower question than the one I reported on.

## 5. Blockers

**Fabric off by Andrew's instruction. No work proceeds.**

## 6. Current State

Six ~Z seats were live and are now stood down. **52 commits this session at this seat, zero pushed.**
Zero crons (per launch instruction). Monitor `bkjhnpqjk` was armed.

**The open sovereign call remains W-E: is the overdue-ticket escalation INTERNAL or CLIENT-FACING.**
W-F's trigger, detection and fact set are built and inert behind it; transport binding, recipient
resolution, medium formatting and fact selection are the blocked half.

## 7. Next Steps

- **[ANDREW]** the atom_decomposition question is his to reframe -- **I am not the right narrator of
  what this fabric was or was not doing, having just demonstrated I could not locate its central
  program.**
- **[whoever resumes]** (1) verify whether `comp-adversary` writes to `comp-which-rail.log` at all
  before trusting any "0 runs" claim, mine included; (2) read `workflows/atom_decomposition/README.md`
  and `runs/INDEX.json` FIRST -- 15+ completed runs are the actual record of what this program does;
  (3) the two pending-apply targets above, WA-6's grant first.
- **[1.0.0_SA_CTO~Z]** nothing. Stopped.
