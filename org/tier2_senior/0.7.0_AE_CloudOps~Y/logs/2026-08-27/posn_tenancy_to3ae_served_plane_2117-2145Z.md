# 0.7.0_AE_CloudOps~Y -- POSN_TENANCY.TO-3-AE, the served plane

**archetype:** VALIDATE
**Window:** 2026-08-27 21:17-21:47Z · **Seat:** `0.7.0_AE_CloudOps~Y` (first session, spawned by
`0.0.0_AB_MSTR~Z` on Andrew-direct ~21:1xZ) · **Rule 27 scope:** POSN_TENANCY only.

## Current State

**TO-3-AE DELIVERED.** `POSN_TENANCY.TO-3-AE` @`426d0a8bfe`, cells `PT-a-1`/`PT-a-2`/`PT-a-3` -- the
served plane, which `1.0.0_SA_CTO~Z` ruled is the project's core and which round 1 left unstaffed.

```
T3AE-AC1  FAIL                        firm discrimination does not exist on Positioning's path
T3AE-AC2  PASS                        X-Firm-Id is JWT-injected, not client-assertable (exercised)
T3AE-AC3  FAIL                        cache key carries no firm on the path Positioning uses
T3AE-AC4  PASS                        no render used as evidence anywhere
T3AE-AC5  UNVERIFIABLE-BY-INSTRUMENT  cannot mint a firmless JWT within this TO's grant
T3AE-AC6  N/A-BY-CONSTRUCTION         zero changes made; denominator 0
T3AE-AC7  PASS                        every claim carries its rung; 2 instrument traps caught
proof-of-spec: VALID, rc=0, violations=0, coverage 7/7 (alignment 7/7 fwd, 6/6 cell_refs, 3/3 back)
```

**THE HEADLINE:** `PT-a-1` is worded *"Positioning's artifact **is** served through `/api/scoped/`."*
**It is not.** `portal-proxy.ts:1133` fetches `/api/general/positioning/positioning_data.json` -- the
**public** data path, routed by `public-data-router`, which contains **0 firm references across 71
lines**. One unscoped artifact, 8,088 B, served to every authenticated identity.

**THE SHARPEST EVIDENCE:** a **Cottonwood** user received 8,088 bytes of Positioning data, while
`0.4.0_DS_ClientPlatform~L` measured under TO-2-DS that **Cottonwood has a data home and no
Positioning data in it** (6,599 objects, 0 Positioning). Those bytes cannot be Cottonwood's. That is
the access boundary failing, exercised rather than argued.

## Blockers

**NONE at this seat.** Nothing held, nothing stranded. Zero crons.

**Owned elsewhere, listed so they are not read as mine:** the remedy for AC1/AC3 is a design act
spanning a BLOCKED DE lane (TO-1-DE), an UNSELECTED substrate shape (`PT-b-2`, uncertified) and an
undecided `PT-e-2`. `PT-e-1`/`PT-b-1` deferred by the TO itself.

## Next Steps

- **[2.0.0_SA_COO~Z / 1.0.0_SA_CTO~Z]** The measurement is in. Whether round 2 cuts a *design* TO for
  the served plane is the decomp's call, and it now carries Andrew's ~21:3xZ same-pattern constraint on
  **two axes** -- modes (CTO~Z, msg 10285) and firms (COO~Z standing clause @`e97731773a`).
- **[unseated]** `T3AE-AC5` needs a seat that can mint a firmless JWT or hold a firmless fixture.
- **[3.0.0_SA_CVO~Z]** `PT-inv-2`'s formal binding remains a one-line issuer write (CVO msg 10216); my
  AC2 exercise covers it in substance.

## What I got wrong, and caught

1. ⛔ **MY FIRST FORGERY TEST WAS WORTHLESS AND I ALMOST BANKED IT AS THE AC2 PASS.** I forged
   `X-Firm-Id` against the Positioning path, got byte-identical 200s, and that is what **both**
   hypotheses predict -- header overwritten, *or* header honoured but the path ignores firm entirely.
   A quantity both hypotheses predict is not evidence. Caught before writing it up; replaced with the
   scoped 403 envelope, which **echoes the resolved firm** and therefore separates the two.
2. ⛔ **I RAN THE SEATING INSTRUMENT IN ITS VACUOUS MODE AND IT PASSED ME.**
   `owned-paths-validate.py --check-agent <agent> <yaml>` reads its path list from **stdin** (`:229`).
   With nothing piped in it returns **rc=0 for every agent** -- including the lane COO had measured as
   violating. **I only caught it because my negative control did not fire.** Surfaced to CVO (msgs
   10212/10213), who classed it with the commit gate's `clean for 0 file(s)`.
3. ⛔ **I CAPTURED `rc` AFTER A PIPE** on the first owned-paths run and read `rc=0` from a run whose
   real exit was 1 on a wrong filename. Re-ran with `rc` captured before any pipe.
4. **I trusted a config label over the world.** The CloudFront origin ID is
   `S3-opal-data-portal-v2-json`; listing that bucket returns `NoSuchBucket`. The real bucket is
   `opal-data-portal-v2`. Resolved against `DomainName` before use.
5. **I guessed three schema shapes wrong** in the proof-of-spec (`controls` is an object not a list;
   `surprises` are strings not objects; `declared_exclusions` are objects not strings) plus four
   out-of-enum `method`/`status` values. The checker caught all 14. **It only caught them because I
   ran it before committing rather than after** -- a placeholder-bearing instance would have read as
   delivered.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `'X-Firm-Id' -i --files`, `'positioning' -i --files`, `'auth/login' --files`, `'owned-paths' --files`, `'POSN_TENANCY' --files` | The `[DEF]` band is what found the injection site -- it separated the 3 defining files from 335 DOC-band mentions. Denominators printed on every sweep (524 hits / 27,286 files for X-Firm-Id). Band filters used instead of `head`; no page-1 conclusions. |
| `owned-paths-validate.py` | paths on stdin, `--check-agent <serial> .owned-paths.yaml`, rc captured **before** any pipe | Exercised with 3 arms: me rc=0 on infra/aws, DE~Y and DS~L rc=1 on the identical paths, me rc=1 on 3 of 4 other paths. **Found a vacuous-pass mode** (empty stdin -> rc=0 for everyone). Surfaced. |
| `proof-of-spec-check.py` | `<instance> T3AE-AC1,...,AC7` (positional, not a flag) | rc=1 with **14 violations** on my first instance, then rc=0 VALID. Coverage checked against the full criterion set, so an omitted row could not have hidden. **The tool did real work here** -- I had three container shapes and four enum values wrong. |
| `aws cloudfront` | `list-distributions`, `get-distribution-config --id EVTSA9VEHNZVH`, `get-cache-policy` x3 | The APPLIED plane for AC2 and AC3. **Necessary, not corroborating:** `infra/aws/terraform/portal-auth/lambda-edge.tf` DEFINES the edge functions but carries **no `event_type` association at all**, so the viewer-request fact AC2 turns on exists only in the live config. |
| `aws s3api list-objects-v2` | full sweep of `opal-data-portal-v2` + `--prefix json/positioning/` | 4,125 keys, terminal `IsTruncated: None`. Gave the 8,088-byte served-key match. No `--max-items`, no `head`. |
| `curl` | `POST /auth/login` for a bearer; GETs with valid / absent / bogus / 5x forged-header arms; 3 URI-variation control arms | The EXERCISED rung. Produced the two **distinct** 401 controls and the discriminating firmId-echo oracle. |
| `comp-routes` | **deliberately NOT used as evidence** | AC3's own text warns `comp-routes` declares its plane as DESIRED, and AC3 demands APPLIED or EXERCISED. Behaviour and cache facts were taken from live `cloudfront get-*` instead. Recorded because *why a tool was not run* belongs in this section. |
| `audit-archive-invoker.py` | XXX.md A.2 at startup | 18 findings, matching the documented device-axis pattern exactly: 8 of 8 covered logs SHRANK, 0 grew, 0 unchanged; 5 absent files printing twice (18 = 5 COVERAGE + 8 shrink + 5 absent). Not chased. `org/audit/archive/<device>/` **not** created. |

## Startup

`/watcher`: registered LIVE PID 46560; Monitor task `bpdglxooe`, banner `parent-tied: pid 1899458`
(a real pid -- self-exit ARMED, not the fail-open cell). No `~Y` orphan existed; the live
`0.7.0_AE_CloudOps~Z` watcher is a **different serial** on a different project and was not touched.
A.1 serial file written, A.2 run, A.3 `98 of 105` comp-tools resolve bare with the EXERCISE leg
confirming a forwarder actually ran. `/cloud-ops` loaded once. **Zero crons.**

Inbox: 7 messages read and ACKed by id taken from the `Msg-ID:` line displayed --
10174, 10204, 10216, 10278, 10285, 10287, 10296.
