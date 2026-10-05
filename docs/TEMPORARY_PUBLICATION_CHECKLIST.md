# Temporary Public Publication Checklist

## Before publishing
- Confirm the repository contains only sanitized project documentation.
- Confirm no credentials, tokens, keys, certificates, personal data, case data, transaction data, internal URLs, IP addresses, production configuration, vulnerability reports, or raw internal attachments are present.
- Confirm no open-source license is unintentionally granted.
- Review `PUBLIC_DISCLOSURE.md`.
- Treat publication as potentially permanent even if the repository will later be made private.

## During the public window
- Avoid adding raw source documents or internal screenshots.
- Do not use the repository for production secrets or operational configuration.
- Review every commit before pushing.

## When the public window ends
- Change repository visibility to private.
- Review forks, releases, GitHub Pages, Actions artifacts, issues, pull requests, and attachments for material that may remain public.
- Rotate any credential immediately if one was accidentally published.
- Keep a record of what was publicly exposed and for how long.

A visibility change cannot guarantee removal of prior copies, caches, forks, screenshots, or clones.
