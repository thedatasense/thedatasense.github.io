# Binesh Kumar's Personal Website

This is the source code for my personal academic website, built using Jekyll and hosted on GitHub Pages.

## About

I'm a Senior Principal R&D Engineer (Technical Fellow) at Medtronic Surgical Innovation. I successfully defended my Ph.D. dissertation in Engineering and Applied Science (Data Science) at the University of New Haven on August 26, 2026. My research focuses on measuring and mitigating reliability failures in medical vision-language models and evaluating their deployment safety.

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

Reading progress, the Goodreads bookshelf, and Strava activity live in `_includes/life.html` on the About page. Notes bookmarks for `#books` and `#running` redirect there. Third-party widgets include direct links when the embeds are unavailable.

To run this website locally:

```bash
bundle install
bundle exec jekyll serve
```

Then open your browser to `http://localhost:4000`

## Contact

- Email: contact(at)bineshkumar(dot)me
- LinkedIn: [https://www.linkedin.com/in/bineshk](https://www.linkedin.com/in/bineshk)
- Personal Website: [https://www.bineshkumar.me](https://www.bineshkumar.me)

## License

The content of this website is © Binesh Kumar. The underlying theme is available under the MIT license.
