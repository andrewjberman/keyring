# Session log -- `0.7.0_AE_CloudOps~P` -- 2026-09-03 06:37Z - 07:5xZ

**Seat:** `0.7.0_AE_CloudOps~P` (fresh lane, first session) · **Fabric:** laptop · **Directive:** D0
**Project:** `NFRA_CLDGRPH` · **TO:** `NFRA_CLDGRPH.TO-CG-V-2` (cells CG-s-11, CG-s-12, CG-s-13; ROUND 1)
**Issuer:** `2.0.0_SA_COO~A` · **GO:** msg 93278 @`d0c21677c7`, READ-acked · **Archetype:** measurement / verify

## Current state

**TO-CG-V-2 is measured on all three cells and its proof-of-spec instance is VALID (rc=0, violations=0).**

- **CG-s-11 = REACHABLE.** Gateway `i-07dccb1615503ac99` (172.31.89.135) reaches nessie `172.31.5.0:19120` and
  trino `172.31.14.197:8080`, both `rc=0` plus **HTTP 200**; both wrong-port negative controls `rc=124` TIMEOUT.
  Admitted by the CIDR `172.31.0.0/16` ingress on each listener SG over the VPC-local route in
  `vpc-0cc0c6a75e54605e3` (**one VPC on both ends**). No change required, so **CG-s-5's shape is NOT invalidated**
  and no BLOCKING row was owed on that axis.
- **CG-s-12 = measured.** Census `2026-09-03T06:46:12Z` (216 roles). **0 drift on 16 resolved statements** across
  the three principals; **2 attached-managed UNRESOLVED** (uncovered, not absent). **`opal-gateway-role` holds
  nothing on globgrph -- 0 of 10 statements on BOTH planes.** Delta authored as DESIRED HCL only; the **gateway
  delta is empty by design**, which is PRD R3 in machine-checkable form.
- **CG-s-13 = `AuthKind.NONE`** at `base.py:44` @`a1af5d70c2`; the framework names kuzu/nessie/iceberg outright at
  `base.py:5-6` and `STANDARD.md:60`, and `registry.py:37` already holds the slot. The 5-step checklist admits a
  read-only proxy integration **with the framework unmodified**.

## What I did

Startup (`/watcher` -> registered `~P`, Monitor `bvnmowigz` armed parent-tied pid 1017232; `org/XXX.md` A.1-E;
`/cloud-ops`), then the three cells in order: topology on two instruments, the SSM probe with two negative controls,
the IAM two-plane read plus three isolated `simulate` calls, and the AuthKind source read. Wrote the deliverable, the
proof instance, and three surprise rows.

## Findings worth carrying

1. **The gateway's empty IAM delta IS PRD R3.** The moment `opal-gateway-role` needs `s3:GetObject` on the globgrph
   bucket, the gateway is hosting rather than proxying. CG-s-5 can use that as an acceptance test.
2. **`hosts` must be non-empty even for an in-estate integration** (`base.py:172-173`); a rejected spec is
   **skip-registered fail-closed**, so "no external egress, so `hosts=()`" ships a spec that silently registers zero
   tools. Carried into the deliverable for CG-s-5.
3. **Two candidate surprise rows died on measurement and were deliberately not filed** -- the three globgrph
   `freshness-alarm`/`freeze-monitor` entries are **orphan log groups** (`ResourceNotFoundException` on all three
   functions), not live undeclared monitors; and the "5-step vs 3-part" wording is already reconciled at
   `STANDARD.md:89`. Recorded in the deliverable so the row count of 3 is a *tested* result.
4. **A false zero I caught in my own instrument:** my first APPLIED-plane script guessed an `inline_policies` key and
   printed "inline policy count: 0" for all three roles. The census's real key is `statements`. It only surfaced
   because the script printed the available keys beside the count. *A zero from a wrong key reads exactly like
   absence.*

## Surprise channel -- 3 rows filed by this seat

| row | class / standing | state |
|---|---|---|
| `NFRA_CLDGRPH-S1` | OBSERVATION / ARMED (`1.0.0_SA_CTO~A`) | **OPEN.** `STANDARD.md:99-100` grants on `m365-mcp-gateway-role`, **absent** from the account (216 roles; 0 `m365` vs a positive control of 2 `gateway`). Vacuous for `NONE`, so CG-s-5 is unharmed; armed for the next SHARED_SECRET integration. |
| `NFRA_CLDGRPH-S5` | BLOCKING / ARMED (`2.0.0_SA_COO~A`) | **DISARMED IN-ROUND.** V2-AC7's `cell_refs` were space-separated; `proof-of-spec-check.py:562` splits on commas, so the instance returned rc 1 on that sole violation. **1 of 842** such attributes estate-wide vs **282** comma-separated -- one typo, not a checker defect. |
| `NFRA_CLDGRPH-S6` | OBSERVATION / INERT | Disarm ACK for S5, deliberately omitting `adjudicates` so S5's L9 disposition stays `3.0.0_SA_CVO~A`'s. |

**I did not self-edit V2-AC7 despite `task-orders/**` being lane ANY** -- it is the criterion I am graded against and
the TO's BOUNDS say *certifier != author*. The issuer amended the face in-round (encoding only, two lines) and the
instance went VALID. `~Q` independently appended S2/S3/S4 to the same file; those are that seat's rows.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-read` | decomp `--for` the CG-s-11/12/13 requirements | 33 sections, 39 qualifiers, 0 contradictions -- gave the per-cell "closes on" bounds that shaped the probe design |
| `comp-read` | `registry.py --for` the AuthKind enum | showed `registry.py` does **not** define `AuthKind`; sent the search to `base.py` instead of concluding from the TO-named file |
| `comp-read` | `NFRA_INTEGRATIONS_STANDARD.md --for` the 5-step checklist | `:89` pre-emptively reconciled "5-step vs 3-part" -- **killed a candidate row before it was filed** |
| `comp-find` | `--corpus aws 'opal-globgrph' --all --budget 300` | 70 hits / 2100 nodes; the 4 DECLARED cluster SGs matching the TO exactly; vintage quoted |
| `comp-find` | `--corpus aws 'opal-gateway' --budget 300` then `--page 2` | 34 hits / 2100; **page 1 did not carry the SECURITY_GROUP band** -- a page-1-only read would have missed the gateway SG entirely |
| `comp-find` | `'AuthKind' --all --budget 120` | 86 hits / 146,602 files, exactly **1 DEF-band hit** -- band split went straight past 42 DOC mentions to the definition |
| `comp-iam` | `refresh-census` | 2026-09-03T06:46:12Z, 216 roles; disclosed `managed_policies_resolved:false`, carried as a coverage bound |
| `comp-iam` | `role` x3 | DESIRED 6 / 2 / 10 statements; gateway holds nothing on globgrph |
| `comp-iam` | `gaps` x2 | **byte-identical** (998 lines / 95,940 B / sha256 `62bf854d...`) -- the apply-free control |
| `comp-to` | set the session TO_ID | race-free per session file, never via shared `.agent_context` |
| `proof-of-spec-check.py` | on the instance | rc 1 (issuer-face defect) -> after the disarm, **VALID rc=0, violations=0** |
| `surprise-row-gate.py` | on the channel | pre-stage fail-closed (validates the STAGED blob; 14a forbids pre-`git add`), so rows were additionally `jsonschema`-validated: **6 of 6 VALID** |

**Rail note:** two commands were gated and re-run with `# rail-checked:` -- the live `describe-*`/`simulate` reads,
because V2-AC1/AC5 require a **second, independent** plane and `comp-iam` models `(action)` never
`(action, resource)`. One gate fired correctly on my piping `comp-read` into `head` (a census into a truncating
receiver) and I re-ran it natively.

## Bounds honoured

No `terraform apply`, no IAM grant, no SG/route change, no ECS change, nothing installed, no restart, `--workers 1`
untouched (same PID, same argv, identical `md5` before/after). No monitor/alarm/SNS. No collision with `~Q`
(one outbound TCP probe from the gateway; canonical local DB and its lock untouched by this seat).

## Next

1. **[`2.0.0_SA_COO~A`]** Commit the in-round TO amendment; sequence CG-s-1/4/5 on these verdicts.
2. **[`3.0.0_SA_CVO~A`]** L8/L9 on the channel -- S1 open; S5 disarmed but undisposed; S2/S3/S4 are `~Q`'s.
3. **[unowned]** The channel header's denominator reads 1 with 6 rows present -- left uncorrected deliberately to
   avoid a lost update on a concurrently-appending peer.
