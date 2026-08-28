# Session log -- 0.7.0_AE_CloudOps~L -- ADVI_49F.P14-VEHICLE -- 2026-08-27T23:30Z..2026-08-28T00:55Z

**Archetype:** RESPAWN + EXECUTE. Predecessor (pid 22168) died 23:02:19Z, 17 min after `820c5945b1`,
leaving no orphan. This seat re-instantiated from the durable artifacts exactly as that design
intended and re-derived every load-bearing figure rather than inheriting it.

**State at close:** **THE CAMPAIGN IS RUNNING.** Started 00:52Z, 532 of 533 remaining. V14-4c(e)
judged AFFIRMATIVE and **FINAL** (not provisional) after V14-2 was re-exercised on the correct host
in the order `2.0.0_SA_COO` 77146 sequenced. Date 1 ARTIFACT-COMPLETE. Zero crons.

---

## 1. Startup

`/watcher`: NOT REGISTERED (genuine fresh session). `ps` sweep found 9 live watchers, **none for
this serial** -- so the PID-identity discriminator resolved cleanly to "genuine orphan absent, arm
fresh", with no kill required. Registered pid 36668; Monitor `bcyyn1g2k` armed, banner
`parent-tied: pid 3061421` -- a REAL pid, so the self-exit protection is live. 11 messages read and
READ-clock ACKed across the session. `CronList` empty, matching the XXX.md Step 1b-F Tier-2/3 row.

## 2. The gate, re-read at the faces and never inherited

Four separate messages told me the gate state (`0.0.0_AB_MSTR` 77026, `0.4.0_DS_ClientPlatform~U`
76987/77045, `2.0.0_SA_COO` 77068). All were correct. I read the faces anyway, with a **positive
control** -- P14-VEHICLE's own face reads `pending`, proving the predicate discriminates rather than
returning `complete` for everything.

| input | face @00:10:15Z | |
|---|---|---|
| (1) ADVI_49F.P14-STAMP | `complete` @f3a51ab26e | satisfied |
| (2) ADVI_49F.c00-SIGNING | `complete` @8e72ca42b6 | satisfied |
| (3) date-1 re-drive | mine | executed this session |

## 3. My named step had gone stale under me

The CTO-76738 applied-entrypoint PASS at `a52a2224ce` was taken on deployed bytes at LastModified
**22:08:00Z**. The deployed entrypoint now reads **23:17:36Z**. Re-ran: 4 of 4 checks PASS, every
negative control FIRED, rc=0 bare.

**DEPLOYED-BYTES RE-PIN** (`0.0.0_AB_MSTR` 76976 asked every seat holding a timestamp detector to do
this). 5 of 5 objects, LF-normalised sha256(16), the DS lane's own instrument:

- **4 IDENTICAL** to the attested digests -- a pure timestamp move, so the identity claim carries
  forward.
- **c00_flow_ledger.py DIFFERED** (`46ca96edded3172c` vs attested `dca0665181c02de0`). Resolved **BY
  CONTENT** -- walked the file's history LF-hashing each blob -- to committed vintage `b27fb8d73d`
  "feat(ADVI_49F.c00-SIGNING SG-2)". Input (2)'s own work in flight. The instrument was right to
  refuse to call it attested and I was right not to stop on it.
- The 23:17Z `_code` re-sync **did not touch gold objects**; date 1's newest gold object was
  2026-08-19. My freshness discriminator has no false-positive source from it.

## 4. A guard of mine had one reachable arm

`0.4.0_DS_ClientPlatform~U` 76987 moved `attested` to all four tables. Reading that change against
the code it lands on exposed my own sentinel guard:

```
if man["attested"] == -1 and basis != BASIS_DECLARED:      # fires on the ATTESTED branch: 27 of 533
```

The arm it could not see is a **DECLARED date returning a real count** -- a00 on the converter branch
while the driver drove declared -- which is **506 of 533**. A control set whose failing half is the
rare one has one reachable arm. Three arms now (+ two conforming baselines), **5 of 5 correct**. Arm
C (basis present, `attested` ABSENT) would have been *wrong to write* before tonight, because its
absence was the normal case until `eb99599a50`.

## 5. Date 1 refused -- and the refusal was the vehicle working

Fired 00:11:33Z. Failed rc=2 in 15.2s. Hard-stop: flag not toggled, not retried, ledger row written,
operator judgment requested. Nothing written to gold.

    bd-49f-auto-login-role/i-0fa1846f04ed7e337 is not authorized: s3:ListBucket on opal-data-49financial

**ROOT CAUSE: WRONG HOST.** The driver's constant read
`INSTANCE_ID = "i-0fa1846f04ed7e337"  # bd-49f-auto-login` -- **and the comment was TRUE.** That id
really is the BD auto-login box. It was correct about what it NAMED and wrong about what it should
have named, which is exactly why no reading of the line ever caught it.

**MY INSTRUMENT, reached before the ruling arrived:** InstanceId across the document's own
invocation history -- 16 invocations, denominator printed, **15 of 16 on `i-01003b035d2988dfb` over
8 days; mine was the only send ever made to the login box.** `1.0.0_SA_CTO` 77108 reached the same
answer from Terraform source. Two planes, one answer -- corroboration, not repetition.

**NOT a regression, measured before anyone could call it one:** CloudTrail on that role since
2026-08-27T00:00:00Z returns **0 events**. Limit stated: a ResourceName-scoped management-event
lookup is evidence of no IAM *write*, not a universal negative.

⛔ **THE DANGEROUS REPAIR WAS THE OBVIOUS ONE.** "Fix the AccessDenied by granting the permission"
would have handed a session-login box permanent read/write on the whole 49F data estate to repair a
typo'd constant. The fix is the re-point and nothing else; `bd-exporter-ec2-role` already carries all
three grants via `advi-49f-chain-access` (read live, not assumed).

## 6. The re-point created a hazard neither ruling covered, and it was the destructive half

`halt_host()` stopped a RUNNING host unconditionally. Harmless on a single-purpose login box; **not
harmless on a shared gold-layer runner** -- `bd-exporter-ec2-role` also carries schwab,
`opal-data-bd`, `opal-data-inf`, `opal-data-assets` and the platinum publisher, so stopping a host
this driver found running could kill another lane's in-flight run it cannot see. Made conditional on
`_DRIVER_STARTED_HOST`. `1.0.0_SA_CTO` 77133 ruled it correct and **superseded its own 77108 3(b)**:
`StartedByDispatcher` stays OMITTED, because sending it true would self-halt after every date -- the
74209 dispatcher-halt trap the TO forbids by name.

The fix exercised itself on its first live run: *"was ALREADY RUNNING when this driver arrived --
NOT halting."*

## 7. Date 1 landed, and I did not stop at my own oracle

Re-fired 00:33:45Z. Success rc=0, wall 120.7s, ARTIFACT-COMPLETE. All four manifests carry
`declared-historical-pre-epoch` + `attested=-1`, all fresh. `flow_ledger` 1.0 -> **1.3**,
`nna_canonical` 1.0 -> **1.1**, `twr_daily` and `dim_account` **created** (both were ABSENT).

The driver's oracle scoring the driver's own run is not independent of itself, so I re-read the
objects under `0.4.0_DS_ClientPlatform~U` 77123's criterion, which my oracle does not look at:
admission vocabulary `['pair-match','text-counterpart']` -- **no `code-rule`**; the recovered
magnitude sits in the EXCLUDED bucket (4,910 rows / $2,310,079.96). Boundary holds, on a second
criterion.

## 8. I nearly shipped a retracted oracle

77045 handed me "a re-driven twr_daily must not move" and **I wrote back that I would treat a twr
move as stop-and-report from date 2.** Its author retracted it at 77097 -- 526 of 533 served ledgers
are schema 1.0, so a re-driven twr_daily *should* differ on nearly every date, and the rule would
have stopped the campaign on essentially all of them.

**Had it not been retracted in time, that would have been my defect to own, not theirs:** I accepted
an oracle without asking what its scope was. My own census (twr 532 present / 1 absent;
dim_account 10 / 523) is what prompted their re-measurement, but prompting a correction is not the
same as having caught it.

Replacement adopted, **only the structurally-impossible arm gates** -- `code-rule` reaching the
ADMISSION vocabulary. Everything else records; gating the excluded bucket's *presence* would
false-stop every date that simply has no such rows, the same error one level down. Controls **4 of
4**. Signal 3 (residue == TR count) is **not computable** -- `cf_input_census` publishes no TR
population -- so it is named in the code rather than written as a check that cannot run.

## 9. V14-2 restored before (e) was judged

The original V14-2 proved a real property of the DOCUMENT **on the wrong box**. Re-exercised
00:42:50-00:47Z on `i-01003b035d2988dfb`, rc=0 bare: subject control first
(`Name=bd-gold-layer-runner`), 2 consecutive sends with `StartedByDispatcher` omitted (121.2s,
105.6s), host `running` across **three** ec2 reads -- instance state, never send rc -- plus the
conditional-halt arm refusing to stop a host it did not start. First attempt aborted on **my own
script bug** (`basis_for` is nested inside `main()`) *before any send*; nothing was written.

## 10. Compiler Tools

| `<run>` | observed | vs `<expect>` |
|---|---|---|
| `comp-iam service advi-49f-chain-dispatch` (Phase 1) | **`No service matching`** -- the SSM document is not a Lambda service in the tool's universe (185 lambdas / 178 roles listed) | **NOT a clean sweep.** The mandate names a target this tool cannot resolve. Recorded as an exclusion, not reported as clear. The grant question was answered on the APPLIED plane instead (`iam get-role-policy`, live) |
| `comp-iam service bd-49f-auto-login` | DESIRED plane; source `infra/aws/ec2/bd-49f-auto-login`; "No AWS operations detected" (the chain is not a boto3 lambda). Tool printed its own limits: 24 policy blocks NOT ATTACHED, 2 deny statements unparsed | PASS as a FLOOR only. Its own banner says DESIRED != APPLIED != EXERCISED, so the live `get-role-policy` read is what the verdict rests on |
| `comp-pipescript postdeps chain_49f_entrypoint --firm bd` | **NOT RUN this session** | **N/A by the mandate's own trigger** -- Phase 1 is "before write" on the SSM document and **no document edit occurred**; the fix was a driver constant. Recorded rather than silently skipped. (Predecessor sessions recorded it REFUSED rc=2 -- the chain lives in the `assets` tree, which `--firm` does not enumerate; consumer set remains UNMEASURED and declared as an exclusion) |
| `comp-iam gaps` (Phase 2) | **N/A by its own trigger rule** -- no `iam.tf` changed, and by ruling no IAM change was permitted | N/A, recorded not skipped |
| `aws ssm get-document --name advi-49f-chain-dispatch` `# rail-checked` (Phase 3) | DocumentVersion 3 = Active; parameters Date + DeclaredHistorical + StartedByDispatcher; `aws s3 sync` runs **unconditionally before the branch** under `set -uo pipefail` (no `-e`), so a failing sync does not abort; historical path renders `--date {{Date}} --upload` and prohibits `--production` | PASS -- the APPLIED plane. **This read is what explained the failure mode**: the sync fails soft, so the chain dies at the missing file rather than at the denial |
| `.tools/commit-gate.sh` | green on every `.py` touched, 3 invocations | PASS |

**The rail refused a `grep infra/*.tf`** and was right to -- I ran `comp-iam` instead, then used an
audited `# rail-checked:` marker for the one statement-body read `comp-iam` does not surface.

## 11. Commits (push state: LOCAL -- CLOUD is integrator-only, LD-0367)

| commit | what |
|---|---|
| `c29f17b5c9` | sentinel guard: 3 arms + schema_version recorded-not-gated |
| `c143be5f10` | the re-point, conditional halt, ledger **first commit** (it was untracked), substrate-card row 6 |
| `3fa0cc63c7` | date-1 acceptance, V14-2 restored, boundary invariant adopted |

## 12. What this session actually cost and caught

Three defects in my own artifacts, none found by a peer: the one-armed sentinel guard, the wrong
host, and the unconditional halt on a shared box. The wrong host was found **by the first live send**
-- which is precisely what V14-4c(a)'s "measure one real date first" exists for, and it would have
burned 533 dates had the campaign started on a document-plane probe alone.

**Every earlier probe measured the DOCUMENT; none measured the HOST.** Substrate-card row 6
(key/identity space) is the always-skipped one, and it is now on the face.

## 13. Next

The campaign runs. It self-pauses at the pre-fire blackout ahead of the 12:45Z nightly (~371 dates
at the measured 115.8s mean) and will not resume until the nightly's OWN artifact is read. A pause at
~12:2xZ is the design working. Reporting per V14-4c(c): per 100 dates or session boundary, whichever
first; immediately on any refusal outside the enumerated expectation. A successor resumes from the
committed ledger, never from this log.
