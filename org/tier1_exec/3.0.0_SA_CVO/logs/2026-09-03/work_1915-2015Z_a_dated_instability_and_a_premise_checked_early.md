# 3.0.0_SA_CVO~Z -- work log 2026-09-03 19:15-20:15Z: a dated instability that clears accepted work, and a premise checked before the stamp

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake. **Prior log:** `work_1820-1915Z_*`. **Push state as read:** local HEAD
392601a248; origin/SITEZ 001709c96e. **Loops:** none. Inbox empty throughout.

## 1. Z-S67 -- premise verified now rather than at the stamp, and one piece of history the row does not carry

`0.7.0_AE_CloudOps~Z` filed (on the issuer's instruction, discharged at issuance) that a criterion demanding
BYTE-IDENTICAL executable lines quietly assumes the files already pass the commit gate they will be committed
through; where they do not, the criterion and Rule 14 are jointly unsatisfiable and the work stalls on lint debt
belonging to nobody on the face.

**Premise VERIFIED at this seat**, because this row is INERT and discharged but this seat still has to disposition
it at L9 and a false premise would matter there. `.tools/commit-gate.sh` is a two-line wrapper that execs
`commit_gate_runner.py`; that runner's `_run_ruff` invokes `ruff check --target-version py39 --extend-select FA
<target>` on the WHOLE FILE with `cwd=WORKSPACE` -- **no `--diff`, no changed-line scoping** -- and any non-zero
return blocks (`BLOCKED: ruff check failed on {f}` -> `return 1`). **So pre-existing debt anywhere in a file
blocks a commit touching an unrelated part of it, and the row's bind is real.**

**AND ONE THING THE ROW DOES NOT CARRY, recorded here because I said it would be** rather than trusting myself to
recall it at adjudication: the runner's own comments at :308-314 state that F541 -- the exact rule the row cites --
was *"the exact rule of the 18c92b9ac audited bypass whose remediation was certified 'closed'"*, found live again
when shebang-aware dispatch closed a filename-proxy gap. **This particular rule has a history of being certified
fixed while the violation was live.** That belongs in front of whoever decides how to clear the debt.

**No row filed for this.** The finding is inert, discharged at issuance, and generalised by its own author; a
confirmation row would cost reader attention and change nothing. The verification lives here and travels to L9.

## 2. Z-S68 -> my Z-S69 @392601a248 -- the instability is DATED, and that CLEARS accepted work

`0.7.0_AE_CloudOps~S` found that `opal-cloudfront-protection` never re-plans 0-diff after its apply while the live
ACL reads exactly as specified -- a stable remove-and-re-add of three managed-rule-group rules, a rule-SET hash
instability rather than drift. So S418-AC3's 0-diff limb is unsatisfiable while every other limb passes.

**Mechanism confirmed on the DECLARED plane** (the row reasons from plan output; I read the declaration):
`portal-auth/waf-cloudfront.tf` carries `managed_rule_group_statement` 3 times, `version =` 0 times,
`managed_rule_group_configs` 0 times, `rule_action_override` 0 times -- exactly the config-versus-state asymmetry
the row names.

**WHY I DID NOT STOP THERE.** Z-S68 says that root NEVER re-plans clean. **TO-OP-S-5's `S5-AC7` is FILED PASS**
and its `output_evidence` reads verbatim: *"RE-PLAN 0-DIFF ON EVERY MODULE TOUCHED ... portal-auth
-detailed-exitcode = 0, opsec = 0, opal-gateway = 0 -- 3 of 3."* An accepted criterion contradicted by a new
finding is exactly what must not be left to the stamp.

**THE RESOLUTION IS VINTAGE, NOT ERROR** -- measured per blob across that file's entire history: the three managed
rule groups entered at **7987571c9a, 15:40Z today, in TO-OP-S-4-18's OWN commit**; 2866bd5f1f (05:27Z),
a6d4f52ed7 (07-20) and 8f221e2d04 (07-08) each carry **ZERO**. TO-OP-S-5 completed at f49c82b891, **06:28Z, nine
hours before the construct existed**. **S5-AC7's PASS was correct when made and stays correct; nothing is
re-graded and no accepted work reopens.** Two other completed faces checked and clear on their own terms:
TO-OP-S-8's S8-AC5 states in its own evidence that it re-planned partner-firms and shared-infra and NOT
portal-auth (a declared departure, not a hidden one); TO-OP-S-2's S2-AC5 names shared-infra/apigateway-portal.

**So the face that found the instability is the face that introduced it, and its own 0-diff check caught its own
side effect inside twenty minutes.** The row reads as a discovery about an old resource and is a discovery about
the current apply; worth saying plainly so nobody triages it as legacy drift.

**THE FORWARD EXPOSURE IS SCOPED TO A ROOT, NOT A FACE, and it has a clock.** Any criterion whose 0-diff covers
`infra/aws/terraform/portal-auth/` is now unsatisfiable as written, whoever owns it. S418-AC3 is known.
**TO-OP-S-1 is PENDING and its S1-AC5 requires "0-diff on every module touched"** -- its Lane names
`portfolio-management/` as its Terraform root while `portal-auth` appears 11 times in its text, so whether
portal-auth lands among the modules it touches turns on where the new authorizer declaration goes. **Not guessed
at**; flagged to the issuer while that face is still pending, because it is far cheaper before the apply.

## 3. Method note, kept because it is the correction of my own earlier failure

20 of this project's 126 criteria mention a 0-diff or re-plan. **That count is NOT the exposure** -- most name
other roots -- and I read each one rather than reporting the number. This is deliberate: earlier today I ran a
reach probe for a different class that returned three hits and was **wrong about all three** on reading (a
denominator alternative and two outcome alternatives, none an instrument menu). A regex over criteria answers
"how many mention the words", never "how many are affected". Both the row and the message to the issuer say so
explicitly, so the scope claim carries its own limit.

## 4. State at close

Channel **69 rows**, 21 this seat's. Task orders **7 of 9 complete**, TO-OP-S-1 PENDING, TO-OP-S-17R-28 STAGED
(plus TO-OP-S-4-18, TO-OP-S-6, TO-OP-S-7, TO-OP-S-9-11 staged in the wider round-2 set). Inbox empty, everything
acked. Both of this seat's own verdict corrections remain disarmed by the issuer's rulings.

**The one blocked item, unchanged:** the four round-1 closure rows (S2, S11, S13, S17) -- remediated inside round
1, needing no route, refused by a gate whose ruled exemption sits on the other device behind an ASSESS-ONLY leg.
Gate here still `c3ef3a2530`, 0 occurrences of `REMEDIATED`. Script ready, refuses over a dirty file. Cost:
nothing live; their closure sits in prose on Z-S19 rather than in a machine-readable field.
