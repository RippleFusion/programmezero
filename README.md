# Programme Zero

Site for [programmezero.com](https://programmezero.com), hosted on GitHub Pages.

## How the password works

The pages in the repo root (`index.html`, `contact.html`, `privacy.html`) are **encrypted** copies of the pages in `src/`. Visitors see a password screen and the page decrypts in their browser.

- Edit the real pages in `src/`.
- Rebuild the locked pages: `PASSWORD='the-password' node tools/lock.mjs` (needs Node 18+), then commit the changed root files.
- The password is not stored in this repo.
- To launch publicly: copy `src/*.html` over the root files, and set `robots.txt` back to `Allow: /`.

Note: this is a light gate, not high security. Anything in `src/` is readable if the repo is public.
