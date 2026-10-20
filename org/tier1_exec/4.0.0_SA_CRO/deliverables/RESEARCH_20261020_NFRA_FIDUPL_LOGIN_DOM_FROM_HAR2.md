# RESEARCH 2026-10-20 -- NFRA_FIDUPL: the Wealthscape login pages, element by element (from HAR 2)

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1) | **Asked by:** 2.0.0_SA_COO~P1 msg 8624. FU-x-1's live sign-in timed out (row
NFRA_FIDUPL-D1-W1-S9) and signin.py's selectors were guessed.
**Source:** `wealthcentral.advisorchannel.com2.har` on dell1, Andrew's own sign-in of 2026-10-19 17:23Z. Structure only: element tags,
ids, names, attributes and visible labels. No values, cookies, tokens or personal data.

## Headline: the pages are script-rendered, and pages 2-4 use web components with shadow DOM

- **No login page carries a static `<form>` in its HTML.** Every element below comes from the page's JavaScript bundle, as captured in
  the HAR:
  - **Page 1** is an AngularJS 1.5 app (`ng-app="fi.portal.commonlogin.login"`). Its template is in
    `appcontent/app/commonlogin/commonlogin-v26.9.30.S1.min.js` and is plain DOM.
  - **Pages 2-4** are a modern Angular app at `wealthcentral.advisorchannel.com/auth/platform-login/` (`main-G64SBBAN.js`, 16 MB).
    Its fields are **custom elements** (`bwc-input`, `bwc-button`, `bwc-radio-group`, `pvd-*`). Each wraps a native input inside a
    shadow root: the bundle references `_nativeInputEl` and `showHidePassword`.
- **Selector consequence (inferred):**
  - The ids below sit on the **custom element**, not on the `<input>`.
  - Playwright's CSS engine pierces open shadow roots, so `#passwordInput input` reaches the native field. Filling `#passwordInput`
    itself may time out or do nothing.
  - In the live DOM, Angular attributes are lower-case: `formcontrolname`, `id-label`.
  - If a shadow root is closed, click the host element, then type with `page.keyboard`.

## Page 1 -- `https://www.wealthscape.com/` (username)

HAR entries #75-#92: a 301 from `wealthscape.com`, then GET `www.wealthscape.com/` (14,625 B HTML, 0 `<input>` tags in the HTML).

| # | Element | Attributes | Visible text |
|---|---|---|---|
| 1 | `form` | `id="clLoginForm"` `name="clLoginForm"` `novalidate` `ng-if="!commonLogin.userIdProcessed"` | -- |
| 2 | `label` | `for="userInput"` `class="text-label"` | "Username" |
| 3 | `input` | `id="userInput"` `name="userID"` `type="text"` `size="24"` `required` `ng-model="commonLogin.userID"` | -- |
| 4 | `input` | `id="rememberMe"` `name="rememberMyUsername"` `type="checkbox"` `class="input-checkbox__input"` | (remember-me label) |
| 5 | `input` | `type="submit"` `value="Next"` `class="bttn-text-primary"` `ng-click="commonLogin.processNextButtonClick()"` | "Next" |

**Next** fires POST `www.wealthscape.com/auth/api/redirect-info` with body key `userId` (HAR #92). The browser then POSTs to
`wealthcentral.advisorchannel.com/auth/login` with body keys `productId`, `username`, `wealthscapeDomain` (HAR #96). That load is the
page-2 app.

## Page 2 -- `wealthcentral.advisorchannel.com/auth/login` (password)

The `formGroup` is submitted on `ngSubmit`.

| # | Element (custom) | Attributes | Visible text |
|---|---|---|---|
| 1 | card | `id="card"` | -- |
| 2 | error box | `id="errMsg"` `msg-type="error"` `title="Error"` (only when an error is shown) | -- |
| 3 | checkbox | `id="rememberUser"` `label="Remember my username"` | "Remember my username" |
| 4 | input (bwc) | `id="passwordInput"` `id-label="password"` `type="password"` `formControlName="password"` `size="25"` `aria-label="Enter password"` `showHidePassword` | "Password" |
| 5 | button (bwc) | `id="submitButton"` `type="submit"` `variant="main-text-primary"` | (submit) |
| 6 | loading layer | `id="loadingLayer"` `label="Loading"` | "Loading" |

The username shown on this page arrives from page 1; a block for it shows conditionally (`ngIf`).

**Submit** fires, on `ecaap.advisorchannel.com`:
- POST `/user/factor/password/authentication` (body keys `username`, `password`; HAR #152);
- POST `/user/session/login` (#158), which returns `authenticators`: `OTPSMS`, `OTPVOICE`, `OTPREP`;
- GET `/user/factor/otp/state` (#162);
- GET `/user/identity/attributes` (#165), which returns the masked phone list.

## Page 3 -- factor choice, card heading "Extra security step required."

| # | Element | Attributes | Visible text |
|---|---|---|---|
| 1 | card | `id="card"` `heading="Extra security step required."` | "Extra security step required." |
| 2 | method choice | a `bwc-radio-group`, rendered in a conditional child template from the `authenticators` and phone attributes. **Its option markup is NOT in static consts; it is data-driven.** Expect one option per method (text, voice, rep) and phone. | (method / phone labels) |
| 3 | link (bwc) | `id="callRep"` `variant="link"` | (call a rep) |
| 4 | button (bwc) | `id="submitButton"` `type="submit"` `bttn-aria-label="Generate code"` | (Generate code) |
| 5 | link (bwc) | `id="cancelButton"` `bttn-aria-label="Cancel login process"` | -- |
| 6 | loading layer | `id="loadingLayer"` `label="Generating code"` | "Generating code" |

- A second variant of this page has `id="continueButton"` (aria "Generate code") and a link `id="changeUser"` in place of `callRep`.
- **Generate code** fires POST `/user/factor/otp/sms/authentication` with body keys `phone`, `template` (HAR #174, at 17:23:33.154Z).
- The SMS reached Quo at 17:23:34.780Z.

## Page 4 -- code entry

| # | Element | Attributes | Visible text |
|---|---|---|---|
| 1 | text | `id="subHeading"` | (instruction) |
| 2 | input (bwc) | `id-label="code"` `type="text"` `formControlName="securityCode"` `placeholder="XXXXXX"` `maxlength="6"` `hint-text="Code expires in 30 minutes."` | "Security Code" |
| 3 | link (bwc) | `id="resendCode"` `variant="link"` | (resend) |
| 4 | link (bwc) | `id="seeOptions"` `variant="link"` | (other options) |
| 5 | button (bwc) | `id="submitButton"` `type="submit"` `bttn-aria-label="Verify the code"` | (Verify) |
| 6 | link (bwc) | `id="cancelButton"` `bttn-aria-label="Cancel Login Process"` | -- |
| 7 | loading layer | `id="loadingLayer"` | "Verifying code" |

The code input has **no `id`**. Reach it by `[formcontrolname="securityCode"] input`, or by `[id-label="code"] input`.

**Verify** fires, in order:
- PUT `/user/factor/otp/sms/authentication` (body key `securityCode`; HAR #191, at 17:23:40.914Z);
- POST `wealthcentral.../ssc/platform-authorization/api/v2/authorize` (body keys `appName`, `loginSite`, `loginType`; #198);
- GET `/container/home` (#199), which means signed in.

## Timing (measured, HAR 2)

- The landing GET is at 17:23:23Z; the code submit is at 17:23:40.9Z.
- The whole human sign-in took about **18 s**. A 30 s wait per page is generous; a timeout points at a selector, not slowness.

## Suggested selector set for signin.py (inferred from the above; the worker proves it)

```
page 1:  #userInput            -> fill username;  input[type=submit][value="Next"]  -> click
page 2:  #passwordInput input  -> fill password;  #submitButton  -> click
page 3:  (if shown) choose the text-message option in the bwc-radio-group (data-driven; match label text containing "text"/"SMS"
         or the phone ending); then #submitButton or #continueButton ("Generate code")
page 4:  [formcontrolname="securityCode"] input  -> fill the Quo code;  #submitButton  -> click
done:    URL reaches /container/home
```

## Not measured

- The radio option markup on page 3 (data-driven, not in the static bundle).
- Whether the shadow roots are open or closed.
- Whether page 3 appears every time or only when there is more than one method. Andrew's session showed the SMS send right after
  `otp/state` and `identity/attributes`.
