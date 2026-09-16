# Aditya Tanna — personal research website

Static academic homepage for **https://adityatanna29.github.io/**.

The single-page layout follows the supplied Ishaan Watts reference: left profile column, section navigation, light/dark themes, timeline, publication figures, and projects. The implementation uses original semantic HTML, CSS, and JavaScript. It is not the earlier al-folio preview.

## Hosting

In repository **Settings → Pages**, select **Deploy from a branch**, **main**, **/ (root)**, then save. The `.nojekyll` file tells GitHub Pages to serve the HTML directly. No Ruby, Jekyll, Node build, or additional theme is required.

The default address is determined by the owner and repository name. Changing an HTML title or a Jekyll `title:` does not change the address. This repository matches the current owner `adityatanna29`, so its default Pages URL is `https://adityatanna29.github.io/`.

## Edit the website

- Publication metadata: `data/profile.json`.
- Biography, timeline, and project text: `build.py`.
- Styles and responsive layout: `css/site.css`.
- Color-theme switch: `js/site.js`.
- Run `python3 build.py` after editing content, then commit the regenerated `index.html` with your changes. Python uses only its standard library.
- You can also edit `index.html` directly, but a later generator run will replace those manual edits.

## Images

| File | Use |
|---|---|
| `images/profile.png` | Supplied portrait |
| `images/sides/tabtune.png` | Rendered from the supplied one-page TabTune figure PDF |
| `images/sides/fine-tuning.jpg` | Fine-tuning overview |
| `images/sides/clinical-qa.png` | Ontology-grounded clinical QA |
| `images/sides/orion-msp.png` | Orion-MSP |
| `images/sides/orion-bix.png` | Orion-BiX |
| `images/sides/peraugy.png` | Personalized summarization |
| `images/sides/distillation.png` | Shared by the structured-health and Pocket Foundation Models papers |

Supplied image contents are preserved. Figures open at their full available resolution when clicked. Publications without a supplied figure have no invented placeholder. Publication metadata and claims follow the supplied résumé; the résumé itself and all CV download links are excluded.

## Attribution and validation

Design reference: https://wattsishaan.github.io/. Its source credits Sebastin Santy's minimal-research-theme and Lakshay A Agrawal's adaptations. Their personal content, photos, analytics, and verification tokens are not included.

Before upload, local image and asset links, section anchors, JavaScript syntax, publication counts, and the absence of CV files were checked. Browser rendering has not been independently validated.
