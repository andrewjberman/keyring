# 0.7.0_AE_CloudOps~G — 2026-08-25 — ADVI_PERFRP TO-R1-AE

**Written:** 2026-08-25T11:06:54Z · **Scope:** ADVI_PERFRP ONLY (one project per instance).
**State at writing: AC2 + AC5 PASS · AC1/AC3/AC4/AC6 UNCOMPUTABLE · ZERO PERFRP leaves served · nothing published, nothing enabled, no document minted, no allowlist touched, no apply performed.**

## Sovereign word received today

**Andrew-direct ~08:5xZ** (relay via CTO 69835, base terminal): *"I'm fine with it on PROD, let's just get the data part sorted."*
**BRANCH half RELEASED** — the PERFRP-on-PROD exposure I escalated is ruled ACCEPT, no revert. **DATA half KEPT and is now the whole of the hold.** Publish gate stands at this seat.
A second, independent hold also bears on AC3: **Andrew-direct 2026-08-21T19:18Z** (recorded at `portal/src/api/endpoints/adviKeyRepoint.ts`) holds the 49F flip until BOTH source gaps AND schedule are addressed. **AC3 is behind two holds, not one** — I had been describing it as one.

## The work that landed

**PRFR1AE-AC2 → PASS** (@6c748859ee). No IAM change required for any of the 11 PERFRP keys; none made.
DESIRED plan 0-diff (`-target`ed, disclosed) · APPLIED `get-role-policy` (`s3:PutObject` only, `platinum/advi/49financial/*` only, **no Condition — measured**) · EXERCISED 11/11 allowed, one `--resource-arns` per call.
**The controls are the evidence, not the count**: negative `platinum/mdpf/whatever.json` → `implicitDeny` proves the instrument discriminates; the **unborn-key** test (`perfrp_zzz_hypothetical_9999.json` → allowed) discharges a debt my own AC5 entry recorded, where wildcard coverage of not-yet-existing leaves was flagged as an inference and explicitly not claimed as measured.

## ⛔ The finding, and the three times I corrected it

I reported (69724) that Andrew's ratified condition was holding on things that "are not guards" — the mechanism I gave him, *"an absent entry cannot publish"*, is genuinely gone: DS~G wired all 11 families at 04:57:24Z (@9af61d7e2e), and the publisher **builds by invoking each emitter** (`subprocess.run`), so there is no "no artifact yet" backstop. **That fact stands.**
**The risk I attached to it did not.** Enumerating the actual path found **five** deployed-verified gates:

| path | gate |
|---|---|
| scheduled | `advi-49f-publisher` DISABLED |
| scheduled | SSM doc absent — a deliberate **contract hook**, per the TF's own header |
| scheduled | `ALLOWED_DOCUMENTS` refuses first, before EC2 start (`lambda_function.py:111`) |
| manual | `--publish` required; default is full dry-run |
| manual | `OPAL_ADVI_PUBLISH_GRANT=1` — second independent factor (`d_publisher_port.py:525`) |

**And `advi_49f_publisher.tf` already documented most of it.** I escalated about this publisher's activation without opening the Terraform that defines it — measured live AWS state carefully, never read the artifact explaining that state.
**All three misses ran one direction: toward less-protected-than-reality.** I claimed that as a disposition; DS~G and CVO's survivorship argument applies to me and I conceded the generalisation — a tally of my own *corrections* cannot measure my *errors*. What I kept is narrower and I think real: within **one** claim's enumeration re-measured three times over the same path, the direction is a measured property, not a sampling artifact.

**Filed by CVO as ADVI_PERFRP-S16 (BLOCKING × INERT).** CTO ruling on my fork: **(c)** record it — done @2705d2561a, a comment-only TF block naming what changed and enumerating all five gates so it cannot read as an alarm; **(b)** declined, no revert of DS~G's entries; **(a)** a separate Rule-24-clean staging field, pitched to CVO and adjudicated REPAIR.

## Two criterion defects surfaced to the issuer (both accepted, both amended)

- **AC1** mandates printing `d_publisher_port.py:566-568`. That range no longer holds the denominator (504→545→570→607→627 across five vintages). Accurate when written; invalidated by two later commits.
- **AC3** named `comp-routes trace` "per key" — **the tool does not take an S3 key.** Amended @06c7f220fd to require stating the key→URL mapping, *because that mapping is the claim*.
- My proof instance then quoted the **superseded** AC3 text and validated clean. Re-synced @0a01bc1da8.

## Off-lane findings, routed not built

- **`to-check --assignee` returns 0 for lane seats — the tilde is NOT the cause.** `SERIAL_RE` captures `(?:~[A-Z])?`; serials are found then discarded as unclassified. The discriminator is the SEATED-prose notation -- a bold **SEATED:** label followed by the serial wrapped in backticks -- which `_assignees_from_field` does not recognise as an assignment. Corpus census: **24** invisible TOs, **9 of which carry no tilde at all** — which is what kills the tilde hypothesis independently. A fix scoped to tildes would have changed nothing and reported as landed.
- **`criterion_verbatim` is unenforced.** Schema-required, `minLength: 10`, described as *"the spec's own words … not a paraphrase"*; `proof-of-spec-check.py` contains the token **zero times**. CTO ruled it a mechanism (no approver → not a gate) and authorized the build; **my screen then falsified the build order**: 874 of 956 rows are unscreenable because 132 of 143 instances predate `decomp_ref`. Amended to build the resolution half first. Owner: `0.8.0_AE_CloudComp`.

## For whoever picks this up

1. **Nothing publishes until the DATA half is discharged.** That is Andrew's word, not an inference from this file.
2. **AC1's start condition is met** (11 emitters exist, all wired) — what is missing is a *read first emission*, which is his ratified condition, and the data-half hold above it.
3. **Re-measure before citing anything here.** The five-gate table, the IAM rows, and the S16 basis are all true of specific instants today; a repo commit does not vintage an AWS account.
4. The AC3 router pre-finding (PII refusal reaches no PERFRP leaf) is a **DESIRED-plane read of committed source, not the deployed edge** — re-ground it before a serve act.
