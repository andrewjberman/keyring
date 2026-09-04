# Session Log -- 0.7.0_AE_CloudOps~U -- 2026-09-03 22:30-23:59Z

**Serial:** `0.7.0_AE_CloudOps~U` | **Fabric:** site-z | **Spawned by:** `2.0.0_SA_COO~Z`
**Face:** `NFRA_OPSEC202609.TO-OP-S-13` -- the opalinvest.com edge (OP-s-13, FWD-13)
**Archetype:** BUILD (apply-legged, deploy-ledgered)

---

## Current State

**THE EDGE IS BUILT, APPLIED AND EXERCISED. S13-AC1 / AC4 / AC5 PASS on the applied plane; S13-AC2 and
S13-AC3 file `UNCOMPUTABLE-BY-CONSTRUCTION` on two ARMED rows.** proof-of-spec instance **VALID rc=0**
(checker-vintage `50ff3d674a`). Deploy ledger `opsec-s13-website-edge` **CLOSED, 5 of 5 legs proven**.
The WordPress box was not touched and **no DNS record was changed**, so no visitor traffic traverses the
new edge yet.

- ACL `opal-website-edge-protection` `af7ed304-f3b9-4135-b7c4-42af5913df6d`
- Distribution `E1DHJH4Y1W8YC2` -> `dmq5420cdhgqf.cloudfront.net`
- Commits `dba1113ea9` (rows + AC5 before-state) and `3256fd2dfa` (build + evidence + proof-of-spec)
- **Push state MEASURED: LOCAL.** `ls-remote origin SITEZ` = `001709c96e`, local HEAD = `1b2065e765`.
  Push is the integrator's act (LD-0367); this lane does not push.

## What Was Done

1. **Startup:** `/watcher` armed a persistent inbox Monitor (no orphan existed for `~U`; the `~S`/`~Z`
   watchers found running belong to peer lanes and were left alone). Registered, session-serial file
   written, `/cloud-ops` loaded. Msg-IDs 20015 and 20024 read and ACKed.
2. **Phase 1 re-grounding** (the face's mandated first act) -- see Findings.
3. **Built** `infra/aws/terraform/website/cloudfront.tf`: a CLOUDFRONT-scope ACL reusing the existing IP
   sets with the three managed groups in COUNT, plus a CloudFront distribution over the existing box.
4. **Applied** via `safe-apply.sh` behind an opened deploy ledger; graded AC1/AC4/AC5 live.

## Findings

**THE DNS AND CERT HALF IS NOT EXECUTABLE FROM THIS FABRIC (row `Z-S101`, BLOCKING/ARMED).**
`opalinvest.com` has no Route53 zone (denominator 2, `IsTruncated` absent) and is delegated to GoDaddy
`ns47/ns48.domaincontrol.com`, read **authoritatively from GoDaddy's own nameserver** rather than a
public recursive. No ACM cert for the name exists (us-east-1 denominator 1). A **second independent
carrier** agrees and it is this repo -- `infra/aws/terraform/website/README.md` calls the EIP *"the
stable public IP handed to GoDaddy apex-A at W3 cutover"*. Beyond the credential, the apex is an **A
record** and CloudFront publishes no stable IP, and RFC 1034 s.3.6.2 forbids a CNAME at a zone apex, so
an ALIAS-class record is needed; whether GoDaddy offers one is recorded **NOT ESTABLISHED** rather than
guessed, since confirming it needs vendor egress this seat does not have.

**THE ALLOW-LIST GAP IS WIDER THAN THE FACE STATES (row `Z-S102`, BLOCKING/ARMED).** The face expects a
missing allow-list to make **AC3** uncomputable. It also kills **AC2**: with the managed groups mandated
to COUNT and both reused IP sets **empty by design** under C-2, the source-restriction rule is the *only*
rule on this ACL that can refuse anything, and a Count match forwards to the origin -- the opposite of
AC2's *"evidence it did not reach the origin"*. Two criteria, one missing fact.

**THE ORIGIN HOSTNAME PROBLEM WAS SOLVED BY READING THE CERT.** Its SANs are `new.opalinvest.com`,
`opalinvest.com`, `www.opalinvest.com`, and `new.opalinvest.com` resolves to the same EIP -- a
cert-covered, **non-looping** origin needing no GoDaddy change. Without it the cutover would have hit a
second blocker: an edge whose origin is its own alias loops.

**PROPAGATION REALITY:** the apex A record's own TTL is **3600s**. The zone SOA default is 600s, and
reading *that* as the rollback window would have understated it 6x.

## What I Got Wrong

- **Filed both rows without the required `disposition` field.** `surprise-row-gate` blocked the commit
  and named all five violations. Fixed at source; **not** overridden.
- **Piped two census commands into `tail`/`head`**, which the comp rail correctly gated -- a receiver
  erases the denominator. Re-run with the tools' own `--limit`/`--page`.
- **Read `/tmp` from native Python**, which cannot see MSYS `/tmp`; the title extraction came back
  silently empty. Re-done by piping directly. The banked memory covers exactly this and I hit it anyway.
- **Malformed the `body` parameter on three consecutive broker sends.** The tool refused each time
  rather than delivering an empty message -- a fail-closed I benefited from.
- **First apply failed closed** on a `CreateWebACL` 400: the WAFv2 description regex rejects parentheses.
  Nothing was created; the constraint is now written into the file so the next author does not re-learn it.

## Blockers / Asks (both at `2.0.0_SA_COO~Z`)

1. **The `/wp-admin` + `xmlrpc.php` allow-list** -- one fact, not invented here.
2. **A ruling on `xmlrpc.php`**: blocking it outright for all sources needs no allow-list and would make
   AC2 satisfiable immediately -- but it is a POLICY choice, not an address guess, and can break Jetpack
   and mobile publishing. Not this seat's call.
3. **The registrar fork** for Z-S101: (a) GoDaddy access/a human at the console, or (b) authorization to
   move the zone to Route53.

**The `complete` flip is NOT taken unilaterally.** Two ARMED BLOCKING rows stand and deliverable 3 is
undelivered; calling this terminal would make the census read clean on live hazards -- the exact shape
the issuer's own `Z-S90` record refused.

## Compiler Tools

- `terraform plan` **UNSCOPED** both before (2-add/0-change/0-destroy, changed-resource list enumerated)
  and after (`No changes`, 0 stanzas). No `-target` in either, so neither is a scoped check certifying
  its own scope.
- `comp-read --enumerate` on the plan (both reused IP-set ARNs resolved; all hits flagged SUBSTRING with
  the WARN that an anchored probe would read zero -- read and accounted for) and on `INVESTIGATION_v1.md`
  (row-id census with printed denominator, which is how the id collision was caught).
- `.tools/surprise-row-gate.py`, `.tools/proof-of-spec-check.py` (VALID rc=0), `.tools/deploy_ledger.py`,
  `.tools/safe-apply.sh`, `.tools/safe-commit.sh`.
- `aws cloudfront list-cache-policies` / `list-origin-request-policies` -- managed policy ids **read live**
  rather than recalled, because a wrong id is accepted by terraform and silently changes what the origin
  receives.

## Notable

**The id collision was real, not hypothetical.** I composed rows as S99/S100; by the time I wrote, another
lane held both. The write aborted on its own collision check, I re-read the live file (max 100, no gaps)
and landed S101/S102. The file grew 2740 -> 2791 lines *between two of my own reads* -- six lanes are
appending concurrently, so a remembered maximum is stale the moment it is taken.
