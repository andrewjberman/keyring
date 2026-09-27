# Deploy Completion Record
**Date opened:** 2026-09-27T01:57:43.050470+00:00
**Status:** OPEN
**Deploy:** Cross-viewer title binding (packet 474495c0; CTO @e0423ca880, CRO pending): reports/request_composition.py @f8c72944f3 in the resident FIRST (fe64236bbb-rr -> fe64236bbb-xv), then irpt-ycharts-generate; rollback in reverse
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package fe64236bbb-xv | SUMS vs rr package: exactly request_composition.py + bindings; queue 0/0; controlled stop; install rc 0; polls; host sha eecca9cf | resident FIRST (CTO condition): package fe64236bbb + certify@ad817b55ea + resident_main/host_capture@746ddee18a + request_composition@f8c72944f3; SUMS vs the rr package = request_composition.py (b82c1ad7 -> eecca9cf) + bindings only; tar 91d83eb9.. S3 version QP5ad0z9FvT97iI5fJcqR1ToeCg9pqfY; after ~Y's S151 wrapper run finished (101704); SSM 2d2ff336: SUMS OK, factory OK, queue 0/0, controlled stop, install rc 0, active MainPID 166182 since 02:08:38Z on /opt/irpt-resident/fe64236bbb-xv, polls 2, 0 tracebacks; host request_composition.py sha eecca9cf.. = f8c72944f3 blob; rollback root fe64236bbb-rr kept | CLOSED 20260927T020928Z |
| G1 | activation | irpt-ycharts-generate artifact + apply | census vs /iFhTAvT: exactly request_composition.py; code-only plan; safe-apply; readback; import census 0 failed; replan 0 | after R1 (resident first): publish aa366c1b80 (request_composition.py staged at f8c72944f3, sha eecca9cf..); first build lbC+5oFQ carried CRLF templates.json (08f6ee3d, the hop-3 trap) -> NOT applied; working file rewritten from the LF blob and rebuilt: G/TqLPdLz+n84hvDpe5nwR3YEEyj3LixSKcwW2qqVXs= 538180 bytes, S3 version 84.MsfapwdEBVuB6ufbYNcwlybW7V.Nw; census vs live /iFhTAvT: 111=111, exactly request_composition.py differs; package_import_check + irpt-common:5 OK; full ycharts plan 0/1/0 code only; invoke {} CONTRACT_VERSION before; safe-apply 02:15:03Z; readback G/TqLPdL Active/Successful; deployed import census {modules 59, failed {}}; invoke {} CONTRACT_VERSION after; replan -detailed-exitcode 0 | CLOSED 20260927T021643Z |
| V1 | verify | second-viewer re-proof | ~Y offline_submit_proof.py on the new served zip, no overlay, as a second viewer: ACCEPTED |  | OPEN |

## Log

- 20260927T015743Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260927T020928Z LEG R1 closed: resident FIRST (CTO condition): package fe64236bbb + certify@ad817b55ea + resident_main/host_capture@746ddee18a + reques
- 20260927T021643Z LEG G1 closed: after R1 (resident first): publish aa366c1b80 (request_composition.py staged at f8c72944f3, sha eecca9cf..); first build
