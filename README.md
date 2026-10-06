# UAP Open Archive

This is a public shelf for the U.S. government's own UFO files, built so a person or an AI can search them without guessing. It starts with the six 2026 releases the Department of War posted at [war.gov/UFO](https://www.war.gov/UFO/) under the name PURSUE. Every fact is tied to a government URL and, where one exists, an archived copy. When something could not be checked, the page says so. Nothing here was filled in to make the story smoother.

The files themselves are mostly still on the government's servers. This site holds the official catalog, a page for every item in it, and plain-language case files for the episodes people actually ask about.

## Start here

Ten episodes, each in one sentence. The longer page is linked.

- [Seven federal employees, two days in 2023, and no technical data.](cases/western-us-event-2023.md) AARO called it one of the most compelling reports it holds, and said in June 2026 that it was still unresolved.
- [A senior intelligence official in a helicopter, late 2025, and a handful of dark stills.](cases/western-us-test-range-orbs-2025.md) Glowing orbs over a western U.S. test installation. Not the same episode as the one above.
- [A 1964 Navy pilot, a destroyer's radar, and a track at about 3,800 knots.](cases/puerto-rico-radar-1964.md) The memos say November 19, 1964. One spreadsheet cell says February 1, 1965.
- [An AC-130 crew, "cold orbs" over the Gulf of Oman, and a phone pointed at the screen.](cases/gulf-of-oman-orbs-2021.md) The plane's own recorder was not working.
- [A Navy photographer's 1952 film from Tremonton, Utah.](cases/tremonton-1952.md) A Navy lab would not call the objects ordinary. A later Air Force file says likely seabirds. Part of the released print is a sewing demonstration.
- [Three dots in an Apollo 17 photo.](cases/apollo-17-three-dots.md) The frame is NASA's AS17-147-22470. The government says the dots might be a real object, and that a full analysis is coming. It is not in this catalog yet.
- [Wally Schirra's 1962 "lathe shavings."](cases/schirra-mercury-atlas-8.md) The official audio description says particles from his own capsule, plus a burst of light he could not identify. It does not say a craft tagged along.
- [The AAWSAP contract and 37 technical papers.](cases/aawsap.md) A real Defense Intelligence Agency contract from 2008. The papers themselves say they are not proof of warp drives.
- [A Colorado officer's silent, multicolored light.](cases/colorado-police-2023.md) The town and the time of night were blurred out. A news account of the transcript adds height and a radar check. Those details are the newspaper's, not the catalog's.
- [The clip titled "Syrian UAP instant acceleration."](cases/syria-instant-acceleration.md) The government's own caption says the camera stopped following the spot.

All twelve write-ups, including astronaut "fireflies" and the 2019–2020 drone reports that are *not* in this catalog, are listed in [cases](cases/README.md).

## The releases at a glance

Counts in the table are rows in the Department of War spreadsheet captured by the Internet Archive on September 29, 2026 (`release=6v5`). There are **450** rows. **271** (60.2%) have the redaction flag set. That flag is a yes or no. It does not say how many words were blacked out.

Those are not the only official counts. Release 01's earliest stored spreadsheet, May 20, already has 158 rows, but launch-week news counted 162. Release 06 was 71 rows on the morning of September 18 and 75 by September 29. Each release manifest has the dated table. Use that table, not a single number.

| Release | Posted | Rows | Flagged redacted | Who contributed the most |
| --- | --- | ---: | ---: | --- |
| [01](sources/pursue-01/manifest.md) | May 8, 2026 | 158 | 105 (66.5%) | War 79, FBI 57, NASA 15, State 7 |
| [02](sources/pursue-02/manifest.md) | May 22, 2026 | 64 | 54 (84.4%) | War 52, NASA 7, Energy 3, plus one CIA and one ODNI |
| [03](sources/pursue-03/manifest.md) | June 12, 2026 | 72 | 12 (16.7%) | FBI 29, CIA 18, War 12, NASA 11 |
| [04](sources/pursue-04/manifest.md) | July 10, 2026 | 40 | 19 (47.5%) | War 28, NASA 7, CIA 2, Energy 2, FBI 1 |
| [05](sources/pursue-05/manifest.md) | August 7, 2026 | 41 | 14 (34.1%) | War 19, FBI 17, CIA 2, State 2, Executive Office of the President 1 |
| [06](sources/pursue-06/manifest.md) | September 18, 2026 | 75 | 67 (89.3%) | War 67, local police 8 |

By agency, across all six: Department of War 257, FBI 104, NASA 40, CIA 23, State 9, local law enforcement 8, Energy 5, and one each from the Executive Office of the President, ODNI, an unnamed "Intelligence Community Agency," and "U.S. Government."

By type: 270 documents, 134 videos, 30 images, 16 audio files. Six of the document cells are the word PDF with a stray space on the end. They are counted as documents.

No row is credited to the NSA, the NRO, the FAA, the Department of Homeland Security, or the Space Force. A text search of the spreadsheet finds none of those names. More on that in [absent agencies](analysis/absent-agencies.md).

The download bundles on the official page are large (Release 02's videos are listed at 5.6 GB). They are not in this repository. Links and the stated sizes are on each release's manifest.

## How to read a label

Every page marks where a sentence comes from.

- **Official** means the government said it, and there is a URL.
- **Press** means a newsroom. Linked, not copied.
- **Advocate** means a UFO or disclosure source, or an interested person's public claim. Useful as a lead. Not a fact by itself.
- **Skeptic** means a skeptical investigator. Same rule.
- **Analysis** means this archive did the arithmetic or the reading. You can throw that part out and keep the quotation.

The labels matter because the interesting sentences and the ordinary explanations often sit in the same file. The Syria clip's title says "instant acceleration." The caption says the camera let go. Both can be true as descriptions of a title and a caption. Only one of them is a claim about the object's speed.

A case is marked **explained**, **disputed**, or **unexplained**. Read the first paragraph. On the fireflies page, "explained" means NASA's own catalog text already gives the explanation. On the AAWSAP page, "disputed" means people argue about what the program was, not that a light in the sky is in dispute.

## Use it with an AI

Point the model at this repository and ask it to follow [AI_GUIDE.md](AI_GUIDE.md). It should quote a record, keep the label, and refuse to invent a detail the file does not contain.

Questions that work:

- "What did the government actually release about the 1964 Puerto Rico radar case? Quote the catalog and do not smooth over the date conflict."
- "Which PURSUE files mention Tremonton, and where do the official assessments disagree?"
- "Is the Schirra audio a tag-along sighting, or is that someone else's story?"
- "How redacted is each release, and what does the redaction flag not tell me?"
- "Find every catalog row whose description says the video is a phone filming a screen."
- "Which famous cases are not in this catalog at all?"

A human can do the same search with `python scripts/search.py "tremonton"` or by opening [data/records.csv](data/records.csv).

## Honest limits

This version did not open the PDFs, and it did not watch the videos or play the audio. On October 6, 2026, war.gov returned HTTP 403 to this project. The Internet Archive had the spreadsheet and the press pages. It did not, in the checks that were run, have the individual media files. Record pages quote the catalog description and, where a DVIDS id exists, the DVIDS page description. DVIDS download-menu sizes are the text DVIDS printed; those menu URLs returned HTTP 403, so their exact byte lengths were not measured. The public MP4 linked from each DVIDS page was downloaded on October 6, 2026 only long enough to compute a SHA-256. The bytes were not committed. A hash is stored on the catalog row the page matches. It is not stored on a row whose DVIDS id points at a different file. Details are in [what was not opened](gaps/not-opened.md) and [DVIDS coverage](gaps/dvids-coverage.md).

The live site could not be checked for a seventh release. The homepage archived on October 4, 2026 still showed Release 06 as the latest.

Counts that do not match what you may have read in the news:

- **Release 01.** The September 29 catalog has **158** rows and **105** flagged redacted (116 PDFs, 27 videos, 14 images, 1 audio). The May 20 spreadsheet, the earliest CSV stored here, also has 158 rows and 105 redaction flags, but it has **28 videos and no audio**. NASA-UAP-D003A, the Gemini 7 excerpt, was retyped from video to audio after May 20. Launch-day coverage counted **162** entries (120 PDFs, 28 videos, 14 images, 108 redacted). That is a press count of catalog rows. It is not a count of files inside the zip. The difference from the May 20 CSV is 4 PDF rows and 3 redaction flags. No May 8–19 CSV is stored here. An advocate site's story that duplicate PDFs were merged on May 11 is [unverified](gaps/unverified-claims.md).
- **Release 06.** The spreadsheet at 11:39 UTC on September 18 has **71** rows (55 PDFs, 15 videos, 1 audio, 64 redacted): four Colorado videos and no transcripts. A `release=6v3` capture the same afternoon has **72**, because transcript LLE-UAP-D001 was added. September 19 is still 72. September 29 has **75**, after D002, D003, and D004 were added, and **67** redaction flags. D003 is not flagged. A same-day news count of 71 matches the morning spreadsheet.
- The press releases for May 22 and June 12 say the website had "over 1 billion" and "over 1.7 billion" hits. Those are the Department's figures, copied from the archived press pages. This archive did not audit the hit counter.

A research memo prepared on October 5, 2026 was used as a lead. An independent fact-check of that memo, also dated October 5, compared twelve Wayback copies of the catalog and is treated as the correction wherever the two disagree. Where a sentence matches the spreadsheet, the case pages cite the catalog. Corrections from the fact-check:

- Release counts moved. The memo's single numbers (158 and 75) are the September 29 snapshot, not the launch-day counts. The zip-bundle explanation for 162 versus 158 is dropped.
- Rep. Luna's March 31, 2026 letter (46 items, 50 videos, deadline April 14) is not the March 6 request for 51 records. Release 02's videos track her list. The March 6 letter is not public here. See [the letter note](sources/house-oversight/README.md).
- Apollo 17 frame AS17-147-22470 is the NASA scan behind NASA-UAP-VM006. The catalog does not print the frame number. See [that case](cases/apollo-17-three-dots.md).
- The Denver Gazette's October 2023 details (about 300 feet, a radar check, about 15 minutes) are in the September 22, 2026 article, which is summarizing the posted transcript. They are press, not catalog fields.
- The AAWSAP statement of objectives, the original award, and modification P00001 were already public through DIA FOIA postings. Do not call that paper trail new. Modifications P00002–P00005 might be new. That is unconfirmed.
- Wording: Delbert Newhouse is a Navy warrant officer specializing in photography in one file, and a chief warrant officer in others. He is not a "chief photographer." The Air Force line is seabirds, not seagulls. Catalog sentences are not tightened into quotations he did not say.

Other places the memo and the spreadsheet differ, checked here:

- It rounded Release 03's redaction share to 17 percent and Release 04's to 48 percent. The cells are 12 of 72 (16.7 percent) and 19 of 40 (47.5 percent).
- It reported the Puerto Rico incident as November 19, 1964, which is what the description says. It did not flag that the date cell on CIA-UAP-D022 says February 1, 1965.
- It called the FBI "Photo B" series stills. In the spreadsheet, B001 through B024 are type PDF. A001 through A008 are type image. The A-series description says a U.S. government system. The B-series says a U.S. military system. The files were not opened.
- It said the Robertson Panel favored seagulls for the Tremonton film. The catalog description of the panel's report does not mention Tremonton or gulls. That panel claim stays [unverified](gaps/unverified-claims.md). DOW-UAP-D105 does say the Air Force later assessed the objects were likely seabirds.
- Dollar figures for AAWSAP, and sentences from AARO's 2024 historical report, were not re-opened. aaro.mil returned HTTP 403. They are not quoted here as if this archive had read them.
- It used the spelling "Western" for location cells that the spreadsheet spells "Westen" on seven rows. The typo is preserved on the record pages.
- It did not mention two DVIDS ids that point at the wrong second file (1006111 and 1007720), or a Western United States Event rendering whose title says 2026. Those are in [catalog quality](analysis/catalog-quality.md).

Thirteen claims from the memo that the fact-check could not verify are listed, and left unverified, in [gaps/unverified-claims.md](gaps/unverified-claims.md).

The memo's September 29 headline counts (450; 158/64/72/40/41/75; the agency totals; 271 redaction flags; 270/134/30/16 by type) match that spreadsheet. So do the title-versus-date clashes it listed, the FBI-UAP-D014 double id, the Syria camera note, the Gulf of Oman phone-video note, and the absence of Nimitz, Gimbal, Roswell, and Rendlesham as named files.

## If something is wrong

Say which page, which sentence, and which source shows the correction. [CONTRIBUTING.md](CONTRIBUTING.md) explains how to add a later release and how to re-count the spreadsheet. The short log of this version is [CHANGELOG.md](CHANGELOG.md).

## License

Original writing and the indexes are [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The scripts are MIT. The U.S. government records quoted here are public domain. The split is spelled out in [LICENSE](LICENSE).
