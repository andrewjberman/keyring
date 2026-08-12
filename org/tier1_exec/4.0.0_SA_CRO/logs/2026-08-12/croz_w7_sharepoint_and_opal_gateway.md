# 4.0.0_SA_CRO~Z — 2026-08-12 — W7 SharePoint reach + registry, and the OPAL_GATEWAY formalization

**archetype:** EXPLORE

Second work block of the site-Z session (the first is `croz_w8_bbg_blpapi_pipe_map.md`). Covers
OPAL_ANALYST.W7 @`3ea5f17245`, Andrew's `integrations/` reorganisation, and the OPAL_GATEWAY brief.

## W7 — SharePoint reach + registry (CLOSED)
Routed by CTO~Z 182248Z as a within-program reassignment. Rung 2 first: verify and register what
exists, deliverable is the registry, not a client. **Read-only throughout.**

| Inc | Commit | Content |
|---|---|---|
| 1 | `2627d66fc3` | reach + capability registry + unverified premises |
| 2 | `aa79dba9f7` | read tools exercised per class + 3 proof-of-spec groups |

**THE FINDING — the mandate's own word does not hold uniformly.** Andrew's Part 2 is *"properly
hooked up to read sharepoint documents."* Exercised per class: `.xlsx` reads fully via
`read_site_workbook`; text/csv reads via `read_site_file`; **`.pdf`/`.docx`/`.pptx` return a
RENDITION and NO TEXT** from `read_document`. **The reach reads spreadsheets and does not read
documents.** Clean boundary rather than a bug — the tool's contract says v1 is lean by design and
text-extract is *"an honest follow-on, NOT a silently-wrong partial scrape."* A tool that refuses
beats one that half-succeeds, because a half-scrape is indistinguishable from a complete read at the
call site. **A config read would have certified a capability the estate does not have** — which is
why W7-REACH-C2 forbids one.

**Enumeration finding, on the FIRST act:** `find_sharepoint_site("Opal")` → 6 sites;
`"*"` → 15. **Short by 9**, no error, and the missed set contains the largest corpus on the tenant
(`Shared`: 78 root folders, Marketing 3.2GB, Software 3.0GB). Registering off the natural query would
have produced a registry 40% short **and internally consistent**.

**Identity finding:** the gateway is OAuth'd as **Andrew Berman personally**, not a service
principal. So every "not found" is indistinguishable from "exists but Andrew cannot see it", and
every call attributes to him. No absence claim in the registry is a claim about the tenant.

Proof-of-spec: 3 groups, 6 of 6 criteria, all rc=0, negative-controlled (bogus id → rc=1). The REG
mutant **did not fire** (3 of 3 probed sites carry one library) and is reported as non-firing rather
than as absence of the hazard.

## `integrations/` reorganisation (Andrew-direct)
Bloomberg consolidated (`1ed08a1960`), gateway formalized (`8205c4d97a`), brief amended
(`24ad90f585`). Two costs, both caught by after-checks rather than by anything failing loudly, and
both the same shape — **a structural change silently invalidates controls attached to the old
location**:
1. **A 63-minute schedule revert.** Re-registering through the sanctioned `register_daily_task.ps1`
   moved the production pull 07:00 → 08:03, because the script's `-At` default was stale relative to
   an Andrew-direct ruling. It printed a success banner. Restored, and the default fixed.
2. **An ownership hole.** A new root directory matched no `.owned-paths.yaml` rule, so the files went
   UNDEFINED. Landed under the audited override restoring the lane they already held; the permanent
   rule was **routed to CTO~Z, not self-landed** (grantee does not grant themselves).

## The magnitude chain — the day's sharpest process lesson
On "how much still says m365": **72 → 1 → 5 → 12**, four measurements, three of them wrong, each
issued while correcting the previous. Mine were two of the misreads. **Every wrong one was a COUNT
REPLACING A COUNT; the right one was an ENUMERATION.** Three different proxies (path prefix, file
type, line-prefix comment markers) each misclassified the *same* file, and none measured the actual
discriminator — whether the literal sits inside an evaluated expression. CTO~Z named the root: a
summary of an enumeration is not an enumeration, and relaying one creates a lossy second home for a
set whose whole point is its membership.

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `--name "tools.py"`, `"m365-gateway"`, `"IntegrationSpec"` | located the gateway source in-repo; 144 hits/25,734 files on the naming census |
| gateway read tools | 14 read-class calls | 7 of 8 read capabilities exercised; `search_site_files` deliberately deferred |
| `.tools/proof-of-spec-check.py` | positional, rc captured per-call, no pipe | 3 W7 groups VALID; negative control rc=1, usage rc=2 |
| `.tools/commit-gate.sh` | on every `.py` touched | clean; caught an f-string-without-placeholder before commit |
| raw `aws` / `git grep` | `# rail-checked:` marked | **GAP: no comp-tool models the M365/SharePoint tenant** — comp-tools model the AWS/portal estate. Recorded as a SCOPE BOUNDARY, not a coverage gap, and routed as such. |

**Encoding note worth carrying:** `EC2_MANIFEST.json` fails a default-encoding Python read
(cp1252, byte `0x9d`). Read it with explicit `encoding="utf-8"`. The `commit_gate_runner` docstring
we spent three messages arguing about describes precisely that class.

## Open / not mine
- Andrew's Parts 3 (document text-extract research + AWS-graph registry) and 4 (Bloomberg data-shape
  spec) **not started, held at his sequencing**.
- Bloomberg metering model unanswered; 11 of 100 data points spent, budget approved.
- `integrations/**` permanent owned-paths rule landed by CTO~Z @`affde927d3`.
