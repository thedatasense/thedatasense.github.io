# Binesh Kumar's Personal Website

This is the source code for my personal academic website, built using Jekyll and hosted on GitHub Pages.

## About

I'm a Senior Principal R&D Engineer (Technical Fellow) at Medtronic Surgical Innovation. I completed my Ph.D. in Engineering and Applied Science (Data Science) at the University of New Haven in October 2026, after successfully defending my dissertation on August 26, 2026. My research focuses on measuring and mitigating reliability failures in medical vision-language models and evaluating their deployment safety.

## Website Features

- **About**: Personal information and academic background
- **Research**: Current research projects and interests
- **Publications**: Academic papers and research outputs
- **Scratchpad**: Writing on machine learning, medical AI, and research
- **Repositories**: Featured GitHub projects focusing on medical AI and vision-language models
- **CV**: Academic curriculum vitae

## Technical Details

This website is built using:
- [Jekyll](https://jekyllrb.com/) - Static site generator
- [al-folio theme](https://github.com/alshedivat/al-folio) - Academic Jekyll theme
- GitHub Pages for hosting

## Local Development

The main site and the sibling `notes` repository share `/assets/css/shared.css`, served by this site. Publish the main site before the notes update. Navigation keeps Research, Scratchpad, and CV; the site name returns to About. Publications, the portfolio, and the thesis are linked from Research. Scratchpad retains the `/notes/` address.

Reading progress, the Goodreads bookshelf, and recent runs live in `_includes/life.html` on the About page. Notes bookmarks for `#books` and `#running` redirect there. Third-party widgets include direct links when the embeds are unavailable.

To run this website locally:

```bash
bundle install
bundle exec jekyll serve
```

Then open your browser to `http://localhost:4000`

### Strava runs

The Running section lists the five latest runs from `_data/strava.json`. The Pages workflow runs `scripts/fetch_strava.py` before every build, and the workflow also runs twice a day on a schedule. The script skips rides and walks, runs under 1 km, and the shorter copy of a run recorded twice within five minutes. Without the secrets below, or if Strava fails, the site keeps the committed file.

To turn on the daily update:

1. Create an API application at https://www.strava.com/settings/api with `localhost` as the Authorization Callback Domain.
2. Open `https://www.strava.com/oauth/authorize?client_id=CLIENT_ID&response_type=code&redirect_uri=http://localhost&approval_prompt=force&scope=activity:read_all` and approve. The browser lands on a `localhost` page that will not load; copy the `code` value from its address.
3. Exchange the code for a refresh token:

   ```bash
   curl -X POST https://www.strava.com/oauth/token \
     -d client_id=CLIENT_ID -d client_secret=CLIENT_SECRET \
     -d code=CODE -d grant_type=authorization_code
   ```

4. Add `STRAVA_CLIENT_ID`, `STRAVA_CLIENT_SECRET`, and the `refresh_token` from that response as `STRAVA_REFRESH_TOKEN` under Settings → Secrets and variables → Actions.
5. Run "Deploy Jekyll site to GitHub Pages" from the Actions tab to check it.

If a run log warns that Strava issued a new refresh token, repeat steps 2 to 4.

## Contact

- Email: contact(at)bineshkumar(dot)me
- LinkedIn: [https://www.linkedin.com/in/bineshk](https://www.linkedin.com/in/bineshk)
- Personal Website: [https://www.bineshkumar.me](https://www.bineshkumar.me)

## License

The content of this website is © Binesh Kumar. The underlying theme is available under the MIT license.
