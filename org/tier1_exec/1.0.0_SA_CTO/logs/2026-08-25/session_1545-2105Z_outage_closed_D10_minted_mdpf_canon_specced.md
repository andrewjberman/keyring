# CTO SESSION LOG -- 2026-08-25 15:45Z -> 21:05Z

**Seat:** `1.0.0_SA_CTO` (post-reboot instance). **archetype:** MIXED (DIAGNOSE, RULE, COORDINATE).
**Written because today produced TWO measured instances of an obligation dying in an unlogged
thread.** Everything below is measured or cited.

---

## 1. OPEN FINDINGS -- carried, owned, NOT chased. READ THIS SECTION FIRST.

*(This section exists because `ec532a0158` recorded a correctly-filed finding that was lost across a
handoff. The brief that lost it had sections for blockers, next-steps and open-at-Andrew, and a
parked finding with a named lane fit NONE of them.)*

| # | finding | owner |
|---|---|---|
| 1 | **PRODUCTION ACCEPTANCE OWED: 2026-08-26 13:30Z `mdpf-scheduled-floor`.** Today's MDPF restoration came from MY ad-hoc invocation; ad-hoc artifacts are never production evidence. Read it. Verify by the PAIR: nonzero `AWS/Scheduler InvocationAttemptCount` (ScheduleGroup=default) in the 13:00-14:00 bucket **AND** global gold LastModified ~13:30:2xZ. **Neither alone attributes -- the metric's grain is the GROUP and 18 schedules share it.** | `1.0.0_SA_CTO` |
| 2 | **S5/S7 ARMED CHAIN.** Seating the 3F-S5 lambda-twin without CVO's S7 force-guard fix ARMS it. `~B` landed the coupling at source @`24d7c5a465`; the REMEDIATION is unseated. | CTO, per `9298b73791` |
| 3 | **ARMED LATENT, fired by a NORMAL act.** `safe_deploy_core.py:217` maps the whole silver tree to `opal-data-mdpf/code/scripts/silver/`; `mirror_schemas.py` is ABSENT there and 3 modules import it. Safe only because the prefix holds 2 of 38 files. **A routine "deploy the silver tree" breaks cottonwood gold.** | CTO |
| 4 | **`record-terraform-deploy.sh` has no targeted-apply notion** -- dry-predicted 7 updates, 6 FALSE. Remedy is a `--functions` scope the script already passes at `:703`. | D0/NFRA_DEPLOYLEDGER |
| 5 | **Source map drifts NON-UNIFORMLY** -- one function had the date wrong and sha right, another had both wrong. Instances closed; CLASS open. | D0/NFRA_DEPLOYLEDGER |
| 6 | **D8-vs-D10 register fork.** MSTR minted D10 @`a6d0261752`; D8 still holds "Model Portfolios Pipeline Fortification"; Andrew said both "create under D10" and "just replace D8". **`MDPF_CANON` CANNOT REGISTER until this resolves** (tag-at-creation rule). | Andrew |
| 7 | **`comp-directives check` returns rc=2 ON A CORRECT REGISTER** -- `comp_directives.py:251` treats a directive id as a permanent key; Andrew uses it as a refillable slot. **An expected-red gate trains people to ignore it.** | D0, routed |

## 2. WHAT LANDED

**THE OUTAGE IS CLOSED.** All four MDPF partners serve `as_of_last=2026-08-24`, `source_keys`
advanced. Cottonwood restored 17:36Z; global 19:46Z after I fired gold + publisher on Andrew's direct
word. **AC4 passed on data-bearing leaves** -- a raw-sha compare would have reported a FALSE failure
on two healthy partners, because `_provenance.written_at` advances daily.

**ROOT CAUSE OVERTURNED TWICE, and the second one was not mine:**
- Not vendor drift. **WE** amended BD template 226355 @`17c38a26f2` under a CTO pin, adding the exact
  two columns the silver guard refused. Source-confirmed at three layers (`dbc80cb768`).
- Global's freeze was NOT an independent data defect. `~N` found the coherence gate's clause (vi)
  compared `tot[i-1..i+1]` without requiring the same legs at all three dates; 08-19 is the ONE date
  whose neighbours both lack cottonwood's roster. **There was never a foreign-day roster.**

**D10 GLOBAL PIPELINE STRUCTURE** minted (MSTR @`a6d0261752`), PRD @`758c74e6f7`.
**MDPF_CANON PRD v1.1** @`6f53713982` + inventory @`3fae717c83` -- current state, target state,
per-item acts, 9 acceptance criteria. **Waits on §7.2 (legacy bucket disposition) and finding #6.**
**Rule 17b amended** for gold's HOME + CODE-HOME only.
**Portal `Submit a Request` removed**, live on PROD v2.1.169.
**Spring clean:** 101 projects + 208 TOs closed on Andrew's membership predicate.

## 3. WHAT I GOT WRONG -- seven, all caught by others or by a gate

1. **`mirror_schemas.py` has FIVE homes, not two.** All five were in my own tool output; I read the
   first two and stopped.
2. **Source-map premise falsified** by `~B` -- `build-and-upload.sh:133` writes `artifact_sha256`
   unconditionally. I reasoned about what my CHANGE touched, never what the TOOLING writes.
3. **"Global's producer never ran"** -- it ran and REFUSED. I read the object; COO read the run log.
4. **Stale-fold hypothesis** -- died on the clean discriminating run.
5. **Accepted an attribution TO MYSELF** without checking my own sent record. `~B` caught it.
6. **Briefed a seat onto a terminal, directive-less project** (`OPAL_ASSETS`) minutes after quoting
   the all-work-under-a-directive rule at three other seats. **Andrew caught it.**
7. ⛔ **THE BIG ONE: I censused EventBridge RULES and concluded about TRIGGERS.** There are two
   surfaces -- `events list-rules` (137) and `scheduler list-schedules` (18). **MDPF has a complete
   scheduled chain and I called it the unscheduled-pipeline defect, repeatedly, to Andrew and into
   the PRD.** Two seats named `mdpf-scheduled-floor` in my hearing and I treated my instrument's
   silence as their imprecision.

**THE PATTERN, and it is one thing:** in every case the answer was already in front of me, or one
cheap command away, and I reasoned from a plausible signal instead. **The tell I now trust: when a
seat names a specific object my instrument cannot see, SUSPECT THE INSTRUMENT.**

**I also left an uncommitted CLAUDE.md edit in a shared tree and it was swept into `~X`'s commit**
(`RULE_17b...FOREIGN_COMMIT` record). Later the **risk-reflex gate held** a register edit of mine
that would have created a duplicate D8/D10 row. **The gate caught what I did not.**

## 4. WHAT THE FABRIC DID RIGHT

`0.4.0_DS_ClientPlatform~N` was told the deploy-path read was sound and **not** to re-derive it.
**They checked anyway.** They found two executors and a scheduled cron pointed at pre-patch bytes --
without that, the repair would have restored global and its own cron would have reverted it the next
morning, visibly, on a client surface.
`0.5.0_AE_OpalETL~B` caught a **33-day undeployed shape change** that would have shipped inside the
P0, and refused to carry it on their own judgment.
**Both catches were about ARTIFACTS -- deployed bytes, run logs, real headers. The expensive traffic
today was seats re-deriving each other's METHOD.** That distinction is the one worth keeping.

## 5. COMPILER TOOLS

`comp-find` (~12 sweeps -- and its NO-HITS guard caught my escaped-pipe pattern) · `aws s3api
head-object` for every timestamp (never `s3 ls`, which renders LOCAL) · `aws logs
filter-log-events` (the VendorDriftError, the coherence gate, the 8-day cycle history) ·
`aws scheduler list-schedules` (**the surface I had been missing all day**) ·
`directives-check` · `to-check --all --project` · `owned-paths-validate` (**returned uniform
None/False -- unsound at my invocation; I did NOT conclude from it**) · `git log -S` (proved the
foreign-commit sweep) · `safe-commit -F` throughout.

## 6. HANDOVER STATE

COO runs the TO wave (6/6 wave-1 seated). CVO mans the surprise channel and proof-of-spec.
**Andrew's threshold: proceed unless UNTENABLE** -- and it binds CTO too: **bounce non-untenable
escalations back to the channel rather than adjudicating them helpfully.**
Live: CTO, CTO~X, COO, CVO, DT, DS~M/N/P, AE_OpalETL~B, AE_CloudOps + ~I/~J/~G, CRO family.
