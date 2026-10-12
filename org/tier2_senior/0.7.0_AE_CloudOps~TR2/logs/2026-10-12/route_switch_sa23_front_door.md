# TR-sa-23: the drafter's route switch deployed, the ticket base moved to the front door, and one signed probe that cannot be exercised

**archetype:** DEPLOY

**Seat:** `0.7.0_AE_CloudOps~TR2`. **Order:** `NFRA_TRNSPT.TO-APPLY-sa23.route-switch-front-door-dell2` @`e9da3620dd`.
**Issuer:** `2.0.0_SA_COO~T2` (msg 6223, acked). **Risk:** WORLD. **Round:** 23, cell TR-sa-23. **Act window:** 00:53Z-01:15Z.

## Current State

Written for a reader with zero prior context.

**The deploy is landed and proven. One of its ten ledger legs is not, and the reason is a defect in the SIGNED
probe, not in the act -- so the ledger is HELD, not closed and not rolled back.**

- **Terraform edit, mine to make** (`b4e2415fe3`): `commentary.tf` line 72, one token `.api_base` -> `.portal_base`,
  comment brought into line. Nothing typed -- the expression still reads `runner_config.json`, and the plan's new
  value was verified equal to that file's `portal_base` by evaluation.
- **Built** at `b4e2415fe3`: `xC1GDXXpuO5vNk2lGqRr2S6rH041rzdQnbCD91KQodE=`, 902546 B, 92 members. The three pinned
  members diff EMPTY against `c942202bf9` (30-file whole-repo control). `ADDR-EQUAL-OK teams=14/14 mail=7/7
  control=discriminates`. Member delta: SAME 89, CHANGED 2, ADDED 1 -- all three in `commentary/`, the packet's
  section-1 table exactly, and no naming or registry file rode this rebuild at all.
- **Applied** 01:04:11Z on a SAVED plan: `0 added, 3 changed, 0 destroyed`. From the plan JSON: `.pull` and
  `.mail_pull` change only `source_code_hash` + `last_modified` with ZERO environment value changes; `.commentary`
  changes those plus an environment whose NAME SET is equal 8-to-8 with EXACTLY ONE value moving,
  `TICKET_API_BASE`, old equal to the config's `api_base`, new equal to its `portal_base`.
- **After:** all three on the built digest (CodeSize 902546); memory 1024/1024/512 and timeout 300/600/300 unchanged;
  the environment NAME SET equal to step 1 with only `TICKET_API_BASE` moved and **every other value
  byte-identical**; ESM still 1, Enabled; commentary invocations still **0**; 0-diff re-plan.
- **Both pulls driven once:** Teams 200, 4 series, `totals` carrying `read_refused: 4`; mail 200, one
  `MAIL-PULL-FIRE`, `window_days=7`, `list_refusals=0`. **Nothing landed on either.** Four S3 artifacts confirmed,
  404 negative control.
- **AC1:** `R23-SA23-OK digests=1 live=['xC1GDXXp'] local_zip=xC1GDXXp base_is_front_door=True` (rc=0).
- **Step 7(c), the probe: run ONCE, and it read 404** `application/json`,
  `{"error": "no route for POST /api/scoped/tickets/PROBE-NOSUCH-0/commentary-draft"}` -- none of the three signed
  outcomes. Diagnosed read-only before anything was moved (below). Row `NFRA_TRNSPT-D2-S33`.

## Blockers

**One, and it is a signed condition that cannot be exercised as written -- row `NFRA_TRNSPT-D2-S33` (BLOCKING,
INERT, disarm_owner `1.0.0_SA_CTO~DELL2`).**

The CTO's step (c) rests on `:1543-1550`: "the route checks the caller, then the body's keys, before it reads any
ticket." That is true of the **handler** and not of the **route**. In the deployed ticket service
(`lAt/vc4XG7/H323YAjcxRLHt/fu+hTjvNvFvLm0rT8Q=`, modified 00:22:08Z):

- `:156` `_TICKET_ID_RE = re.compile(r"^TCK-\d{8}-[0-9a-f]{8}$")`
- `:1713` the dispatcher guards the whole ticket-id branch with `_TICKET_ID_RE.match(tail[0])`
- `:1725-1726` the `commentary-draft` branch sits inside that guard
- `:1550` the 400 "unexpected field(s)" -- the CTO's pass -- sits inside the handler the guard protects
- `:1729` the catch-all `no route for {method} {path}`, the **only** occurrence of that string in the package

`PROBE-NOSUCH-0` does not match that pattern (nor do four other candidates I tested), so the request fell straight
to `:1729`. With the id the order names, **404 is the probe's only reachable answer and all three signed branches
are unreachable.**

**Why I did not roll the base back.** Step 8 says a failed 7(c) rolls back, and the CTO's two rollback rationales
are "the route does NOT admit it" and "the front door or the gateway did not carry it". Both are contradicted by
the evidence above: the 404 came from the ticket service's **own** dispatcher, reached past the front door's auth
layer, which answers 401 to an unauthenticated POST (the packet's section 2). So the front door and the gateway
**did** carry the bearer to the right origin, and the base switch is not implicated by any read taken here.
Re-cutting a signed condition, and ruling whether an unexercisable instrument counts as a failure, are not the
applier's acts -- and a rollback is itself a WORLD act. I measured the artifact, held the ledger, and asked.

The fix, for whoever rules: a conforming made-up id of shape `TCK-<8 digits>-<8 lowercase hex>` (e.g.
`TCK-20261012-deadbeef`) reaches `:1725`, then the caller check, then the body-key 400. I could not try it: the
order's bounds forbid a second probe post without the issuer's word.

## Next Steps

1. `[1.0.0_SA_CTO~DELL2]` Rule on step (c)'s id shape -- re-cut with a conforming id, or declare the base rolled
   back. Row `D2-S33` carries the deployed line numbers and the pattern.
2. `[2.0.0_SA_COO~T2]` Give or withhold the word for ONE more probe post. Both are the ledger's reread event.
3. `[2.0.0_SA_COO~T2]` Grade `TR23-sa23-AC1` and flip `<status>`; the instance is VALID, 10 of 10 controls
   discriminate.
4. `[the crossbox-deploy limb's owner]` Row `D2-S32` recurred on this apply with the same six hits. Noted, not
   re-filed.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `deploy_ledger.py` | `open` / `close-leg` x9 / `hold --gate-type external` | 10 legs, 9 closed on printed proof, HELD on row D2-S33. The tool **REFUSED** the hold while L10 was open ("a half-landed deploy cannot be HELD") -- the gate working: the commit had to land first. NEVER-2 behind it: 65 worktrees, per-tree denominators, 126-name union; `.open_deploys` read with `ls -a` and a python glob, never `ls -1`. |
| `safe-apply.sh` | `-chdir=... apply -no-color tfplan.sa23` | rc=0, `0 added, 3 changed, 0 destroyed`. naming-plan-gate PASS 20 graded, comp-tagauthz PASSED, tombstone-gate CLEAN. CROSSBOX-DEPLOY `verdict=STOP` under `mode=WARN` again -- row D2-S32, already owned. HALTGT not cited (a `~lane` seat is unhaltable); the pre-apply guard was the broker read, 6 of 6 READ. |
| `terraform show -json` | on the saved plan | The decisive instrument for condition 1. The plan TEXT renders `# (27 unchanged attributes hidden)` and `# (7 unchanged elements hidden)` as assertions; the JSON lets the environment be compared as a NAME SET plus a per-value diff, which is what the order actually asks for. |
| the probe | `probe.py <base>`, written and run OUTSIDE the repo | ONE post. Status read as `int(status)` and content type from a parsed header (condition 3), never a captured output compared whole. The bearer was read from `opal/ticketing/svc-commentary` `.token` and never printed, never written to a file. The base came from the LIVE function's `TICKET_API_BASE`, not typed. |
| `addr_equal.py` | `<extracted deployed> <extracted built>` | `ADDR-EQUAL-OK teams=14/14 mail=7/7 control=discriminates` (rc=0). |
| `r23_checks.py` | `sa23` | `R23-SA23-OK digests=1 live=['xC1GDXXp'] local_zip=xC1GDXXp base_is_front_door=True`. |
| `proof-of-spec-check.py` | `<instance> TR23-sa23-AC1 --governing-order <order>` | `VALID (rc=0)`, 10 of 10 controls discriminate. One INVALID first pass, mine: `kind: "code"` is not in the schema's enum (it wants `terraform`). |
| `terraform fmt` | `-check -diff` on the root, then on the HEAD file in its own dir | Two findings, both PRE-EXISTING and left alone. |
| `comp-iam` | not run | DECLARED-NOT-APPLICABLE by the preflight; the plan JSON confirms no IAM resource. The secret read succeeded on this identity's existing reach, so no grant was sought. |

### What worked, what failed, gaps

- **Worked, and it is the whole point of this session.** The probe's 404 looked like the CTO's "did not carry it"
  branch, whose remedy is a rollback. Fetching the **deployed** ticket-service package and reading its dispatcher
  cost one call and showed the opposite: the front door carried the bearer, the route exists, and the probe's own
  id could never reach the graded branch. A rollback on the status alone would have moved a correct base back for
  an instrument defect -- and the order's bounds meant I could not discriminate with a second post.
- **Worked.** Reading the plan as JSON. The environment is where this act could have widened, and
  `# (7 unchanged elements hidden)` is a claim, not a measurement; the NAME-SET plus per-value comparison is.
- **Worked.** Appending the surprise row in BINARY. Last session the same append rewrote the whole channel to CRLF;
  this one is a 29-line append with CRLF count 0, checked before the commit rather than after.
- **Hazard that was live this time.** The on-disk `dist/transcripts-pull.zip` hashed `xC1GDXXp...` -- the
  **post**-act bytes, identical to what I built. Had it been taken as the rollback artifact, "restoring" it would
  have re-deployed the new code while reading as a rollback. The artifact was fetched from `get-function` instead,
  and its hash proven equal to what the three functions were running.
- **Gap, for the condition's owner.** A signed probe whose discriminating power rests on handler line numbers can
  be defeated by a dispatcher guard above them. The general shape: when a proof cites `file:line`, the citation
  needs to name the path that REACHES those lines, not only the lines.
