# /self-drive laptop directives -- self-drive log, ticks 5-6 (2026-08-25 09:35Z - 10:16Z)

**Driver:** `1.0.0_SA_CTO`. **state: ARMED.** **cadence:** 30m. **cron:** `f03462e0`.
**archetype:** COORDINATE. **secondary_archetypes:** VALIDATE.
**Push state:** landed LOCAL, rides MSTR integration. Continues `..._tick4.md` @`fe2e7a6cb9`.

## THE HEADLINE: HIS PRIORITY IS LIVE, VERIFIED ON THE APPLIED LAYER

**Andrew ~08:5xZ: *"let's just get the data part sorted."***
```
live Lambda cot-rebalancer-runner  MODEL_DETAIL_SCOPE = "all"   (was "opal_closure")
control BD_FIRM_ID = "cottonwood"  (the read discriminates)
LastModified 2026-08-25T09:50:45Z   ledger cotmdl-model-detail-scope-all CLOSED
```
**Applied by `0.7.0_AE_CloudOps~H` `-target`-scoped to their own resource**, leaving three other lanes' drift
untouched. **Authorized ~06:0xZ, seated ~09:1xZ, live ~09:5xZ.**

## SCOPE + COMPLETION (ticks 5 and 6, both re-resolved)

```
5 laptop directives [D0 D1 D2 D3 D5] of 9 live -> 12 projects   scanned 328 JSONs
open TOs: D0=4  D1=0  D2=18  D3=6  D5=0
COMPLETION: 0 of 12 complete | 4 UNREACHABLE (no JSON) | UNCHANGED across ticks 2-6
OPEN CALLS: 0 adjudicable both ticks -- no empty pitch sent (skill s.1 zero-case)
```

## !! TWO ARMED FINDINGS RULED THIS WINDOW, BOTH FOUND BY THE EXECUTING SEAT

**1. THE TF DIRECTORY CARRIES THREE OTHER LANES' UNAPPLIED CHANGES.** `AE~H` ran `terraform plan` on a TO
that describes itself as *"ONE TERRAFORM LINE"* and got **4 to change**; `git status` clean, so
**COMMITTED-BUT-UNAPPLIED DRIFT.** One is an MDPF **producer repoint**
(`gold/mdpf_revamp/_aggregate_aua/` -> `portal/gold/mdpf/_staging/aggregate_aua/`) -- **NEVER#3 territory
riding in on ANY full apply by ANY seat, whose plan output would look routine to them because it is not their
change.** Plus `Outputs: + mdpf_egress_publisher_live_serve_cosigned = true`.
> !! **A CO-SIGN FLAG FLIPPING TO `true` AS A SIDE EFFECT OF AN APPLY IS EXACTLY THE SHAPE A CO-SIGN EXISTS TO
> PREVENT.** A sign-off is two named humans agreeing; an output asserting one happened is a RECORD, and a
> record that lands because Terraform ran is not evidence anybody decided.
**RULED:** `-target` the one resource (sanctioned; the FULL apply would be the violation). Disarm owner
`2.0.0_SA_COO`; `3.0.0_SA_CVO` files the surprise. Co-sign provenance traced before it applies anywhere.

**2. !! THE FIX I AUTHORIZED WOULD HAVE TRADED ONE PERMANENT GAP FOR ANOTHER.** Source-confirmed at
`lambda_function.py:300/:316`: **the child-descent is guarded OFF in `all` mode**, so the modes are mutually
exclusive, not cumulative. Tomorrow would land 64 roster models and **none of the 8 non-roster sub-models it
lands today -- 5 of them OPAL-NAMED, the sleeves the constituent data lives in.**
**RULED: the guard comes off; `all` must mean ROSTER UNION CLOSURE** (a strict superset of both modes).
COO cut `TO-R2-AE`. **Time-boxed before 2026-08-26 06:00Z -- per-date, so after that fire those sub-models
are permanently absent from that partition.**
*The cost structure I used to argue the flip was urgent condemned its side effect equally, and I did not see it.*

## !! MY OWN ERRORS THIS WINDOW -- FOUR, ON TWO FINDINGS

**A. "30 OF 64" IS TWO POPULATIONS IN ONE FRACTION** (`AE~H` 70056). Of 30 detail files, **22 are on the
roster and 8 are transitive children.** **TRUE ROSTER COVERAGE WAS 22 OF 64; THE GAP WAS 42, NOT 34.**
I put "30 of 64" in front of Andrew repeatedly. **The defect was WORSE than I reported** -- the direction
strengthens the authorization -- **but a fraction whose numerator and denominator count different things is
not a coverage number.** The denominator law's own shape: the number was real, the frame was wrong.

**B-D. THE `to-check` FINDING: RIGHT PATTERN, WRONG MECHANISM, TWICE, THEN A WRONG POPULATION.**
| # | my claim | falsified by | what I actually did |
|---|---|---|---|
| B | "returns 0 for every tilde lane" -> mechanism = the tilde | `AE~G` 70008, **at source** | `SERIAL_RE:98` **captures the suffix**; serials are found WITH tildes and discarded downstream. **The discriminator is the `**SEATED: \`serial\`**` PROSE NOTATION.** Controlled experiment: tilde removed from SEATED prose still fails; tilde present in clean notation works. **My split was a CONFOUND -- two variables moved together and I blamed the visible one.** |
| C | remedy: "run the BASE serial" | `DE~D` 69987 | their TO appears under **NEITHER** query; base-serial recovery recovers some TOs and not others, **and nothing in the output says which.** |
| D | "EVERY lane -> 0, EVERY base -> real count" | `DS~G` 70076 | **`~A`=10, `~B`=9, `CRO~C`=1.** **I SAMPLED THREE LANES THAT SHARE A PROPERTY AND GENERALISED TO THE POPULATION.** |

> !! **B AND D ARE THE SAME FAMILY AN HOUR APART: I HAD A CLEAN-LOOKING RESULT AND DID NOT CHECK WHETHER THE
> SET I MEASURED WAS THE SET I WAS CLAIMING ABOUT.** Once as a confound, once as an unrepresentative sample.
> **Neither was caught by care; both were caught by a peer holding a different sample.**
!! **AND B WAS THE DANGEROUS ONE: A FIX TO TILDE MATCHING WOULD HAVE CHANGED NOTHING AND WOULD HAVE READ AS
SUCCESSFUL** -- lane seats still blind, fix reported as landed.
**All four corrected IN PLACE in `org/XXX.md` B.1, each marked, none deleted** -- `f7acd42f8a` -> `d6bdd72dd1`
-> `9207136b9c` -> `a05282b261`. **The operational guidance never changed: your TO is the file named in your
dispatch message.**

## DRIVER ACTS (own lane only -- no TO, no dispatch, no apply)

| act | ref |
|---|---|
| `XXX.md` B.1 measured-broken warning + 3 self-corrections | `f7acd42f8a` `d6bdd72dd1` `9207136b9c` `a05282b261` |
| Ruled `-target` on the TF drift; disarm owner named | 70038 |
| Ruled ROSTER UNION CLOSURE, time-boxed to 06:00Z | 70071 |
| Corrected "30 of 64" -> 22 of 64 to Andrew and the fabric | 70071 |

## RESERVED (at Andrew) -- 3, unchanged

1. **`ADVI_COTKEY` key of record.** 2. **Register integrity** (4 phantom members, D1/D5 empty).
3. **CVO's condition-4 no-gates test** as a clarification of his own rule.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `aws lambda get-function-configuration` | the APPLIED env var + a control var | **`all` live** -- DESIRED (source) confirmed against APPLIED (live), Rule 22a |
| `directives-check.py --json` | ticks 5, 6 | unchanged; 4 members still no-JSON |
| `to-check.py --assignee` | 8 serials incl. 3 lanes I had not sampled | **the falsification of my own claim** |
| `sed` at `lambda_function.py:295-322` | the scope branches | **the descent guard, read not inferred** |
| `safe-commit -F` (msg-verify) | 5 commits | all MATCH, path-scoped |
| comp-rail | gated my `infra/*.tf` grep | **correctly** -- re-run with a `# rail-checked:` marker naming why no comp-tool returns a TF literal |

**What failed:** four claims of mine (s. A-D). **Gap found:** `to-check`'s notation set does not recognise
`SEATED: <serial>`; the correct fix is to widen it, and a tilde fix would have been a false green.

## Next

- **[0.7.0_AE_CloudOps~H]** `TO-R2-AE` union fix before 2026-08-26 06:00Z.
- **[2.0.0_SA_COO]** TF drift disarm; co-sign provenance.
- **[0.0.0_AB_MSTR]** register: 4 phantom members, D1/D5.
- **[1.0.0_SA_CTO]** tick 7 at :43; **read the 12:45Z artifact (~2h30m)**; next log tick 8.
